"""
QV4::Moth::ByteCodeHandler binding of the Qt C++
"""
#  Apache-2.0 license
#  Copyright (c) 2026 Asger Jon Vistisen
#  Written by dev_tooling.ClassGenerator from the records of
#  QtQml/6.12.0/QtQml/private/qv4bytecodehandler_p.h, Qt 6.12.0. Changes made
#  here are lost.
#
#  Qt means QV4::Moth::ByteCodeHandler to be private: it declares the class
#  in a header it calls private. cutienator does not care. Qt hands objects
#  of the class out all the same, and a class we are handed is a class we
#  have.
from __future__ import annotations

from typing import TYPE_CHECKING

from worktoy.dispatch import overload

from ..cute import CuteMixin, MetaCute
from . import QV4

if TYPE_CHECKING:  # pragma: no cover, no mutate
  from typing import Never


class ByteCodeHandler(CuteMixin, metaclass=MetaCute):
  """
  The cute side of Qt's QV4::Moth::ByteCodeHandler: a plain Python object
  standing in front of one C++ QV4::Moth::ByteCodeHandler.

  What exists
  -----------

  Every function of Qt's QV4::Moth::ByteCodeHandler that has a ritual and
  that Python can call so far, 138 names in all: 'reset',
  'currentInstructionOffset', 'nextInstructionOffset', 'absoluteOffset',
  'generate_Ret', 'generate_LoadConst', 'generate_LoadZero',
  'generate_LoadTrue', 'generate_LoadFalse', 'generate_LoadNull',
  'generate_LoadUndefined', 'generate_LoadInt', 'generate_LoadRuntimeString',
  'generate_MoveConst', 'generate_LoadReg', 'generate_StoreReg',
  'generate_MoveReg', 'generate_LoadImport', 'generate_LoadLocal',
  'generate_StoreLocal', 'generate_LoadScopedLocal',
  'generate_StoreScopedLocal', 'generate_MoveRegExp', 'generate_LoadClosure',
  'generate_LoadName', 'generate_LoadGlobalLookup',
  'generate_LoadQmlContextPropertyLookup', 'generate_StoreNameSloppy',
  'generate_StoreNameStrict', 'generate_LoadElement',
  'generate_StoreElement', 'generate_LoadProperty',
  'generate_LoadOptionalProperty', 'generate_GetLookup',
  'generate_GetOptionalLookup', 'generate_StoreProperty',
  'generate_SetLookup', 'generate_LoadSuperProperty',
  'generate_StoreSuperProperty', 'generate_ConvertThisToObject',
  'generate_ToObject', 'generate_Jump', 'generate_JumpTrue',
  'generate_JumpFalse', 'generate_JumpNoException',
  'generate_JumpNotUndefined', 'generate_CheckException',
  'generate_CmpEqNull', 'generate_CmpNeNull', 'generate_CmpEqInt',
  'generate_CmpNeInt', 'generate_CmpEq', 'generate_CmpNe', 'generate_CmpGt',
  'generate_CmpGe', 'generate_CmpLt', 'generate_CmpLe',
  'generate_CmpStrictEqual', 'generate_CmpStrictNotEqual', 'generate_CmpIn',
  'generate_CmpInstanceOf', 'generate_UNot', 'generate_UPlus',
  'generate_UMinus', 'generate_UCompl', 'generate_Increment',
  'generate_Decrement', 'generate_Add', 'generate_BitAnd', 'generate_BitOr',
  'generate_BitXor', 'generate_UShr', 'generate_Shr', 'generate_Shl',
  'generate_BitAndConst', 'generate_BitOrConst', 'generate_BitXorConst',
  'generate_UShrConst', 'generate_ShrConst', 'generate_ShlConst',
  'generate_Exp', 'generate_Mul', 'generate_Div', 'generate_Mod',
  'generate_Sub', 'generate_As', 'generate_CallValue',
  'generate_CallWithReceiver', 'generate_CallProperty',
  'generate_CallPropertyLookup', 'generate_CallName',
  'generate_CallPossiblyDirectEval', 'generate_CallGlobalLookup',
  'generate_CallQmlContextPropertyLookup', 'generate_CallWithSpread',
  'generate_Construct', 'generate_ConstructWithSpread',
  'generate_SetUnwindHandler', 'generate_UnwindDispatch',
  'generate_UnwindToLabel', 'generate_DeadTemporalZoneCheck',
  'generate_ThrowException', 'generate_GetException',
  'generate_SetException', 'generate_CreateCallContext',
  'generate_PushCatchContext', 'generate_PushWithContext',
  'generate_PushBlockContext', 'generate_CloneBlockContext',
  'generate_PopContext', 'generate_GetIterator', 'generate_IteratorNext',
  'generate_IteratorClose', 'generate_DestructureRestElement',
  'generate_DeleteProperty', 'generate_DeleteName', 'generate_TypeofName',
  'generate_TypeofValue', 'generate_DeclareVar', 'generate_DefineArray',
  'generate_DefineObjectLiteral', 'generate_CreateMappedArgumentsObject',
  'generate_CreateUnmappedArgumentsObject', 'generate_CreateRestParameter',
  'generate_Yield', 'generate_YieldStar', 'generate_Resume',
  'generate_IteratorNextForYieldStar', 'generate_CreateClass',
  'generate_LoadSuperConstructor', 'generate_PushScriptContext',
  'generate_PopScriptContext', 'generate_InitializeBlockDeadTemporalZone',
  'generate_ThrowOnNullOrUndefined', 'generate_GetTemplateObject',
  'generate_TailCall', 'generate_Debug', 'endInstruction'. None can be made
  from Python: one comes out of a function of another class that gives one
  back.

  What has a ritual and is left out, and why
  ------------------------------------------

  - Qt's 'QV4::Moth::ByteCodeHandler::~ByteCodeHandler()': the destructor:
    Python never removes a C++ QV4::Moth::ByteCodeHandler.
  - Qt's 'Verdict
    QV4::Moth::ByteCodeHandler::startInstruction(Moth::Instr::Type instr)':
    gives the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot
    be named here.

  What has no ritual
  ------------------

  6 of the 146 functions Qt declares: 4 forbidden; 1 the class is abstract,
  so C++ cannot make one, and the C++ class of ours does not fill in every
  function it leaves open; 1 cannot be called and cannot be called through
  the meta-object and cannot be copied.

  What to expect
  --------------

  - The C++ QV4::Moth::ByteCodeHandler is created at the first use, not by
    'QV4::Moth::ByteCodeHandler(...)'.
  - A wrong argument is refused in Python, with 'DispatchException', and
    never reaches C++.
  - None is taken wherever Qt takes an object by its address, or text as C
    has it, and is passed on as nothing. Whether Qt can do with nothing there
    is as in C++.
  - Python never removes the C++ QV4::Moth::ByteCodeHandler.
  - Each name of Qt's QV4::Moth::ByteCodeHandler that has no cute function
    yet, '__init__', 'decode', 'startInstruction', holds a function that
    raises 'NotImplementedError', and its docstring says why.
  """

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  STATIC METHODS   # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  #  NAMESPACE  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

  #  Class Variables
  #  The class of Qt this class stands for.
  __qt_class__ = 'QV4::Moth::ByteCodeHandler'

  #  A C++ QV4::Moth::ByteCodeHandler Python makes is of a C++ class of ours,
  #  in which Python can take functions over. This ritual hands one over; see
  #  'CuteMixin._takeOver'.
  __take_ritual__ = 'ritual_take_QV4_Moth_ByteCodeHandler'

  #  The functions Qt calls itself that QV4::Moth::ByteCodeHandler is the
  #  first to declare and that cannot be handed to Python yet, each as Qt
  #  declares it. A class of a program that writes one of them anew is
  #  refused, since Qt would never call what it wrote; see
  #  'CuteMixin._refuseLeftOut'.
  __virtual_left_out__ = {
      'startInstruction': (
          'Verdict '
          'QV4::Moth::ByteCodeHandler::startInstruction(Moth::Instr::Type)',
      ),
  }

  #  The functions Qt calls itself that QV4::Moth::ByteCodeHandler is the
  #  first to declare. A class of a program built on it can write one anew,
  #  and Qt then calls that. For each name: the key C++ knows the function
  #  by, what it gives, and what it takes.
  __virtual_functions__ = {
      'generate_Ret': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_RetEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadConst': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_LoadConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadZero': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_LoadZeroEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadTrue': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_LoadTrueEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadFalse': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_LoadFalseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadNull': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_LoadNullEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadUndefined': (
          ('_ZN3QV44Moth15ByteCodeHandler22generate_LoadUndefinedEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_LoadInt': (
          ('_ZN3QV44Moth15ByteCodeHandler16generate_LoadIntEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadRuntimeString': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_LoadRuntimeStringEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_MoveConst': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_MoveConstEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadReg': (
          ('_ZN3QV44Moth15ByteCodeHandler16generate_LoadRegEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreReg': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_StoreRegEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_MoveReg': (
          ('_ZN3QV44Moth15ByteCodeHandler16generate_MoveRegEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadImport': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_LoadImportEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadLocal': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_LoadLocalEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreLocal': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_StoreLocalEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadScopedLocal': (
          ('_ZN3QV44Moth15ByteCodeHandler24generate_LoadScopedLocalEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreScopedLocal': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_StoreScopedLocalEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_MoveRegExp': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_MoveRegExpEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadClosure': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_LoadClosureEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadName': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_LoadNameEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadGlobalLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_LoadGlobalLookupEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadQmlContextPropertyLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler37generate_LoadQmlContextPropertyL'
           'ookupEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreNameSloppy': (
          ('_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameSloppyEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreNameStrict': (
          ('_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameStrictEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadElement': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_LoadElementEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreElement': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_StoreElementEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_LoadPropertyEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadOptionalProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler29generate_LoadOptionalPropertyEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_GetLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_GetLookupEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_GetOptionalLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_GetOptionalLookupEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler22generate_StorePropertyEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_SetLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_SetLookupEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadSuperProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_LoadSuperPropertyEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_StoreSuperProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler27generate_StoreSuperPropertyEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_ConvertThisToObject': (
          ('_ZN3QV44Moth15ByteCodeHandler28generate_ConvertThisToObjectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_ToObject': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_ToObjectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_Jump': (
          ('_ZN3QV44Moth15ByteCodeHandler13generate_JumpEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_JumpTrue': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_JumpTrueEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_JumpFalse': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_JumpFalseEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_JumpNoException': (
          ('_ZN3QV44Moth15ByteCodeHandler24generate_JumpNoExceptionEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_JumpNotUndefined': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_JumpNotUndefinedEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CheckException': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_CheckExceptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CmpEqNull': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_CmpEqNullEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CmpNeNull': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_CmpNeNullEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CmpEqInt': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_CmpEqIntEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpNeInt': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_CmpNeIntEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpEq': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpEqEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpNe': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpNeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpGt': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpGtEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpGe': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpGeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpLt': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpLtEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpLe': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpLeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpStrictEqual': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_CmpStrictEqualEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpStrictNotEqual': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_CmpStrictNotEqualEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpIn': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_CmpInEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CmpInstanceOf': (
          ('_ZN3QV44Moth15ByteCodeHandler22generate_CmpInstanceOfEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_UNot': (
          ('_ZN3QV44Moth15ByteCodeHandler13generate_UNotEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_UPlus': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_UPlusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_UMinus': (
          ('_ZN3QV44Moth15ByteCodeHandler15generate_UMinusEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_UCompl': (
          ('_ZN3QV44Moth15ByteCodeHandler15generate_UComplEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_Increment': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_IncrementEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_Decrement': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_DecrementEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_Add': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_AddEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitAnd': (
          ('_ZN3QV44Moth15ByteCodeHandler15generate_BitAndEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitOr': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_BitOrEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitXor': (
          ('_ZN3QV44Moth15ByteCodeHandler15generate_BitXorEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_UShr': (
          ('_ZN3QV44Moth15ByteCodeHandler13generate_UShrEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Shr': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_ShrEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Shl': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_ShlEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitAndConst': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_BitAndConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitOrConst': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_BitOrConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_BitXorConst': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_BitXorConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_UShrConst': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_UShrConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_ShrConst': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_ShrConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_ShlConst': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_ShlConstEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Exp': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_ExpEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Mul': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_MulEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Div': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_DivEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Mod': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_ModEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Sub': (
          ('_ZN3QV44Moth15ByteCodeHandler12generate_SubEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_As': (
          ('_ZN3QV44Moth15ByteCodeHandler11generate_AsEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CallValue': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_CallValueEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallWithReceiver': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_CallWithReceiverEiiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_CallPropertyEiiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallPropertyLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler27generate_CallPropertyLookupEiiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallName': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_CallNameEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallPossiblyDirectEval': (
          ('_ZN3QV44Moth15ByteCodeHandler31generate_CallPossiblyDirectEvalE'
           'ii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallGlobalLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_CallGlobalLookupEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallQmlContextPropertyLookup': (
          ('_ZN3QV44Moth15ByteCodeHandler37generate_CallQmlContextPropertyL'
           'ookupEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CallWithSpread': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_CallWithSpreadEiiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_Construct': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_ConstructEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_ConstructWithSpread': (
          ('_ZN3QV44Moth15ByteCodeHandler28generate_ConstructWithSpreadEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_SetUnwindHandler': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_SetUnwindHandlerEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_UnwindDispatch': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_UnwindDispatchEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_UnwindToLabel': (
          ('_ZN3QV44Moth15ByteCodeHandler22generate_UnwindToLabelEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_DeadTemporalZoneCheck': (
          ('_ZN3QV44Moth15ByteCodeHandler30generate_DeadTemporalZoneCheckEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_ThrowException': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_ThrowExceptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_GetException': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_GetExceptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_SetException': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_SetExceptionEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CreateCallContext': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_CreateCallContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_PushCatchContext': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_PushCatchContextEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_PushWithContext': (
          ('_ZN3QV44Moth15ByteCodeHandler24generate_PushWithContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_PushBlockContext': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_PushBlockContextEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_CloneBlockContext': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_CloneBlockContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_PopContext': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_PopContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_GetIterator': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_GetIteratorEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_IteratorNext': (
          ('_ZN3QV44Moth15ByteCodeHandler21generate_IteratorNextEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_IteratorClose': (
          ('_ZN3QV44Moth15ByteCodeHandler22generate_IteratorCloseEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_DestructureRestElement': (
          ('_ZN3QV44Moth15ByteCodeHandler31generate_DestructureRestElementE'
           'v',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_DeleteProperty': (
          ('_ZN3QV44Moth15ByteCodeHandler23generate_DeletePropertyEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_DeleteName': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_DeleteNameEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_TypeofName': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_TypeofNameEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_TypeofValue': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_TypeofValueEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_DeclareVar': (
          ('_ZN3QV44Moth15ByteCodeHandler19generate_DeclareVarEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_DefineArray': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_DefineArrayEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_DefineObjectLiteral': (
          ('_ZN3QV44Moth15ByteCodeHandler28generate_DefineObjectLiteralEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CreateMappedArgumentsObject': (
          ('_ZN3QV44Moth15ByteCodeHandler36generate_CreateMappedArgumentsOb'
           'jectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CreateUnmappedArgumentsObject': (
          ('_ZN3QV44Moth15ByteCodeHandler38generate_CreateUnmappedArguments'
           'ObjectEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_CreateRestParameter': (
          ('_ZN3QV44Moth15ByteCodeHandler28generate_CreateRestParameterEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_Yield': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_YieldEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_YieldStar': (
          ('_ZN3QV44Moth15ByteCodeHandler18generate_YieldStarEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_Resume': (
          ('_ZN3QV44Moth15ByteCodeHandler15generate_ResumeEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_IteratorNextForYieldStar': (
          ('_ZN3QV44Moth15ByteCodeHandler33generate_IteratorNextForYieldSta'
           'rEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_CreateClass': (
          ('_ZN3QV44Moth15ByteCodeHandler20generate_CreateClassEiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_LoadSuperConstructor': (
          ('_ZN3QV44Moth15ByteCodeHandler29generate_LoadSuperConstructorEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_PushScriptContext': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_PushScriptContextEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_PopScriptContext': (
          ('_ZN3QV44Moth15ByteCodeHandler25generate_PopScriptContextEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_InitializeBlockDeadTemporalZone': (
          ('_ZN3QV44Moth15ByteCodeHandler40generate_InitializeBlockDeadTemp'
           'oralZoneEii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_ThrowOnNullOrUndefined': (
          ('_ZN3QV44Moth15ByteCodeHandler31generate_ThrowOnNullOrUndefinedE'
           'v',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'generate_GetTemplateObject': (
          ('_ZN3QV44Moth15ByteCodeHandler26generate_GetTemplateObjectEi',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
           )),
      ),
      'generate_TailCall': (
          ('_ZN3QV44Moth15ByteCodeHandler17generate_TailCallEiiii',
           ('nothing', 'nothing', ''),
           (
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
               ('int', 'number', ''),
           )),
      ),
      'generate_Debug': (
          ('_ZN3QV44Moth15ByteCodeHandler14generate_DebugEv',
           ('nothing', 'nothing', ''),
           ()),
      ),
      'endInstruction': (
          ('_ZN3QV44Moth15ByteCodeHandler14endInstructionENS0_5Instr4TypeE',
           ('nothing', 'nothing', ''),
           (
               ('int', 'enum', 'QtQml:QV4.Moth.Instr.Type'),
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

  def currentInstructionOffset(self) -> int:
    """
    Calls Qt's 'int QV4::Moth::ByteCodeHandler::currentInstructionOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  int QV4::Moth::ByteCodeHandler::currentInstructionOffset() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Moth15ByteCodeHandler24currentInstructionOffsetEv',
    )

  def nextInstructionOffset(self) -> int:
    """
    Calls Qt's 'int QV4::Moth::ByteCodeHandler::nextInstructionOffset()
    const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  int QV4::Moth::ByteCodeHandler::nextInstructionOffset() const
    return self.uglySide.call(
        'ritual_ZNK3QV44Moth15ByteCodeHandler21nextInstructionOffsetEv',
    )

  @overload(int)
  def absoluteOffset(self, relativeOffset: int) -> int:
    """
    Calls Qt's 'int QV4::Moth::ByteCodeHandler::absoluteOffset(int
    relativeOffset) const'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#absoluteOffset

    Parameters
    ----------

    relativeOffset : int
      Passed on as it is.
    """
    #  int QV4::Moth::ByteCodeHandler::absoluteOffset(int relativeOffset)
    #      const
    return self.uglySide.call(
        'ritual_ZNK3QV44Moth15ByteCodeHandler14absoluteOffsetEi',
        relativeOffset,
    )

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
    Qt's 'QV4::Moth::ByteCodeHandler::ByteCodeHandler()': the class is
    abstract, so C++ cannot make one, and the C++ class of ours does not fill
    in every function it leaves open.
    """
    raise NotImplementedError(
        "'QV4.Moth.ByteCodeHandler.__init__' has no cute function yet. Qt's "
        "'QV4::Moth::ByteCodeHandler::ByteCodeHandler()': the class is "
        "abstract, so C++ cannot make one, and the C++ class of ours does "
        "not fill in every function it leaves open.")

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

  def reset(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::reset()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#reset
    """
    #  void QV4::Moth::ByteCodeHandler::reset()
    self.uglySide.call('ritual_ZN3QV44Moth15ByteCodeHandler5resetEv')

  def generate_Ret(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Ret()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Ret
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Ret()
    self.uglySide.call('ritual_ZN3QV44Moth15ByteCodeHandler12generate_RetEv')

  @overload(int)
  def generate_LoadConst(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadConst(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadConst

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadConst(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_LoadConstEi', index,
    )

  def generate_LoadZero(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadZero()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadZero
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadZero()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_LoadZeroEv',
    )

  def generate_LoadTrue(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadTrue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadTrue
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadTrue()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_LoadTrueEv',
    )

  def generate_LoadFalse(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadFalse()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadFalse
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadFalse()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_LoadFalseEv',
    )

  def generate_LoadNull(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadNull
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadNull()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_LoadNullEv',
    )

  def generate_LoadUndefined(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadUndefined()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler22generate_LoadUndefinedEv',
    )

  @overload(int)
  def generate_LoadInt(self, value: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadInt(int
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadInt

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadInt(int value)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler16generate_LoadIntEi', value,
    )

  @overload(int)
  def generate_LoadRuntimeString(self, stringId: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadRuntimeString(int stringId)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    stringId : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadRuntimeString(int
    #      stringId)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_LoadRuntimeStringEi',
        stringId,
    )

  @overload(int, int)
  def generate_MoveConst(self, constIndex: int, destTemp: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_MoveConst(int
    constIndex, int destTemp)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_MoveConst

    Parameters
    ----------

    constIndex : int
      Passed on as it is.

    destTemp : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_MoveConst(int constIndex,
    #      int destTemp)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_MoveConstEii',
        constIndex, destTemp,
    )

  @overload(int)
  def generate_LoadReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadReg(int reg)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler16generate_LoadRegEi', reg,
    )

  @overload(int)
  def generate_StoreReg(self, reg: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreReg(int reg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_StoreReg

    Parameters
    ----------

    reg : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreReg(int reg)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_StoreRegEi', reg,
    )

  @overload(int, int)
  def generate_MoveReg(self, srcReg: int, destReg: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_MoveReg(int srcReg,
    int destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_MoveReg

    Parameters
    ----------

    srcReg : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_MoveReg(int srcReg, int
    #      destReg)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler16generate_MoveRegEii',
        srcReg, destReg,
    )

  @overload(int)
  def generate_LoadImport(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadImport(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadImport

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadImport(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_LoadImportEi', index,
    )

  @overload(int)
  def generate_LoadLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadLocal(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadLocal(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_LoadLocalEi', index,
    )

  @overload(int)
  def generate_StoreLocal(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreLocal(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_StoreLocal

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreLocal(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_StoreLocalEi', index,
    )

  @overload(int, int)
  def generate_LoadScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadScopedLocal(int
    scope, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadScopedLocal(int scope,
    #      int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler24generate_LoadScopedLocalEii',
        scope, index,
    )

  @overload(int, int)
  def generate_StoreScopedLocal(self, scope: int, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_StoreScopedLocal(int scope, int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    scope : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreScopedLocal(int scope,
    #      int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_StoreScopedLocalEii',
        scope, index,
    )

  @overload(int, int)
  def generate_MoveRegExp(self, regExpId: int, destReg: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_MoveRegExp(int
    regExpId, int destReg)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_MoveRegExp

    Parameters
    ----------

    regExpId : int
      Passed on as it is.

    destReg : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_MoveRegExp(int regExpId, int
    #      destReg)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_MoveRegExpEii',
        regExpId, destReg,
    )

  @overload(int)
  def generate_LoadClosure(self, value: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadClosure(int
    value)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadClosure

    Parameters
    ----------

    value : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadClosure(int value)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_LoadClosureEi', value,
    )

  @overload(int)
  def generate_LoadName(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadName(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadName(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_LoadNameEi', name,
    )

  @overload(int)
  def generate_LoadGlobalLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadGlobalLookup(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadGlobalLookup(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_LoadGlobalLookupEi',
        index,
    )

  @overload(int)
  def generate_LoadQmlContextPropertyLookup(self, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadQmlContextPropertyLookup(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void
    #      QV4::Moth::ByteCodeHandler::generate_LoadQmlContextPropertyLookup(
    #      int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler37generate_LoadQmlContextProper'
        'tyLookupEi',
        index,
    )

  @overload(int)
  def generate_StoreNameSloppy(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreNameSloppy(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreNameSloppy(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameSloppyEi',
        name,
    )

  @overload(int)
  def generate_StoreNameStrict(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreNameStrict(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreNameStrict(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameStrictEi',
        name,
    )

  @overload(int)
  def generate_LoadElement(self, base: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadElement(int
    base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_LoadElement

    Parameters
    ----------

    base : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadElement(int base)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_LoadElementEi', base,
    )

  @overload(int, int)
  def generate_StoreElement(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreElement(int
    base, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreElement(int base, int
    #      index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_StoreElementEii',
        base, index,
    )

  @overload(int)
  def generate_LoadProperty(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_LoadProperty(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadProperty(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_LoadPropertyEi', name,
    )

  @overload(int, int)
  def generate_LoadOptionalProperty(self, name: int, offset: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadOptionalProperty(int name, int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadOptionalProperty(int
    #      name, int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler29generate_LoadOptionalProperty'
        'Eii',
        name, offset,
    )

  @overload(int)
  def generate_GetLookup(self, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_GetLookup(int
    index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_GetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_GetLookup(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_GetLookupEi', index,
    )

  @overload(int, int)
  def generate_GetOptionalLookup(self, index: int, offset: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_GetOptionalLookup(int index, int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_GetOptionalLookup(int index,
    #      int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_GetOptionalLookupEii',
        index, offset,
    )

  @overload(int, int)
  def generate_StoreProperty(self, name: int, base: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_StoreProperty(int
    name, int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreProperty(int name, int
    #      base)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler22generate_StorePropertyEii',
        name, base,
    )

  @overload(int, int)
  def generate_SetLookup(self, index: int, base: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_SetLookup(int
    index, int base)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_SetLookup

    Parameters
    ----------

    index : int
      Passed on as it is.

    base : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_SetLookup(int index, int
    #      base)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_SetLookupEii',
        index, base,
    )

  @overload(int)
  def generate_LoadSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadSuperProperty(int property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadSuperProperty(int
    #      property)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_LoadSuperPropertyEi',
        property,
    )

  @overload(int)
  def generate_StoreSuperProperty(self, property: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_StoreSuperProperty(int property)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    property : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_StoreSuperProperty(int
    #      property)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler27generate_StoreSuperPropertyEi',
        property,
    )

  def generate_ConvertThisToObject(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_ConvertThisToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ConvertThisToObject()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler28generate_ConvertThisToObjectE'
        'v',
    )

  def generate_ToObject(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_ToObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_ToObject
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ToObject()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_ToObjectEv',
    )

  @overload(int)
  def generate_Jump(self, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Jump(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Jump

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Jump(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler13generate_JumpEi', offset,
    )

  @overload(int)
  def generate_JumpTrue(self, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_JumpTrue(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_JumpTrue

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_JumpTrue(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_JumpTrueEi', offset,
    )

  @overload(int)
  def generate_JumpFalse(self, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_JumpFalse(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_JumpFalse

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_JumpFalse(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_JumpFalseEi', offset,
    )

  @overload(int)
  def generate_JumpNoException(self, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_JumpNoException(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_JumpNoException(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler24generate_JumpNoExceptionEi',
        offset,
    )

  @overload(int)
  def generate_JumpNotUndefined(self, offset: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_JumpNotUndefined(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_JumpNotUndefined(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_JumpNotUndefinedEi',
        offset,
    )

  def generate_CheckException(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CheckException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CheckException()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_CheckExceptionEv',
    )

  def generate_CmpEqNull(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpEqNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpEqNull
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpEqNull()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_CmpEqNullEv',
    )

  def generate_CmpNeNull(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpNeNull()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpNeNull
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpNeNull()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_CmpNeNullEv',
    )

  @overload(int)
  def generate_CmpEqInt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpEqInt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpEqInt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpEqInt(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_CmpEqIntEi', lhs,
    )

  @overload(int)
  def generate_CmpNeInt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpNeInt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpNeInt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpNeInt(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_CmpNeIntEi', lhs,
    )

  @overload(int)
  def generate_CmpEq(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpEq(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpEq

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpEq(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpEqEi', lhs,
    )

  @overload(int)
  def generate_CmpNe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpNe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpNe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpNe(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpNeEi', lhs,
    )

  @overload(int)
  def generate_CmpGt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpGt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpGt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpGt(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpGtEi', lhs,
    )

  @overload(int)
  def generate_CmpGe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpGe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpGe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpGe(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpGeEi', lhs,
    )

  @overload(int)
  def generate_CmpLt(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpLt(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpLt

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpLt(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpLtEi', lhs,
    )

  @overload(int)
  def generate_CmpLe(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpLe(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpLe

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpLe(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpLeEi', lhs,
    )

  @overload(int)
  def generate_CmpStrictEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpStrictEqual(int
    lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpStrictEqual(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_CmpStrictEqualEi',
        lhs,
    )

  @overload(int)
  def generate_CmpStrictNotEqual(self, lhs: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CmpStrictNotEqual(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpStrictNotEqual(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_CmpStrictNotEqualEi',
        lhs,
    )

  @overload(int)
  def generate_CmpIn(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpIn(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CmpIn

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpIn(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_CmpInEi', lhs,
    )

  @overload(int)
  def generate_CmpInstanceOf(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CmpInstanceOf(int
    lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CmpInstanceOf(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler22generate_CmpInstanceOfEi', lhs,
    )

  def generate_UNot(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UNot()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UNot
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UNot()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler13generate_UNotEv',
    )

  def generate_UPlus(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UPlus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UPlus
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UPlus()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_UPlusEv',
    )

  def generate_UMinus(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UMinus()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UMinus
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UMinus()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler15generate_UMinusEv',
    )

  def generate_UCompl(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UCompl()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UCompl
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UCompl()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler15generate_UComplEv',
    )

  def generate_Increment(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Increment()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Increment
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Increment()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_IncrementEv',
    )

  def generate_Decrement(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Decrement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Decrement
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Decrement()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_DecrementEv',
    )

  @overload(int)
  def generate_Add(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Add(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Add

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Add(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_AddEi', lhs,
    )

  @overload(int)
  def generate_BitAnd(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitAnd(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitAnd

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitAnd(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler15generate_BitAndEi', lhs,
    )

  @overload(int)
  def generate_BitOr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitOr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitOr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitOr(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_BitOrEi', lhs,
    )

  @overload(int)
  def generate_BitXor(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitXor(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitXor

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitXor(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler15generate_BitXorEi', lhs,
    )

  @overload(int)
  def generate_UShr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UShr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UShr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UShr(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler13generate_UShrEi', lhs,
    )

  @overload(int)
  def generate_Shr(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Shr(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Shr

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Shr(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_ShrEi', lhs,
    )

  @overload(int)
  def generate_Shl(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Shl(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Shl

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Shl(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_ShlEi', lhs,
    )

  @overload(int)
  def generate_BitAndConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitAndConst(int
    rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitAndConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitAndConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_BitAndConstEi', rhs,
    )

  @overload(int)
  def generate_BitOrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitOrConst(int
    rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitOrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitOrConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_BitOrConstEi', rhs,
    )

  @overload(int)
  def generate_BitXorConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_BitXorConst(int
    rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_BitXorConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_BitXorConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_BitXorConstEi', rhs,
    )

  @overload(int)
  def generate_UShrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UShrConst(int
    rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_UShrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UShrConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_UShrConstEi', rhs,
    )

  @overload(int)
  def generate_ShrConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_ShrConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_ShrConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ShrConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_ShrConstEi', rhs,
    )

  @overload(int)
  def generate_ShlConst(self, rhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_ShlConst(int rhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_ShlConst

    Parameters
    ----------

    rhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ShlConst(int rhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_ShlConstEi', rhs,
    )

  @overload(int)
  def generate_Exp(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Exp(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Exp

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Exp(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_ExpEi', lhs,
    )

  @overload(int)
  def generate_Mul(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Mul(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Mul

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Mul(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_MulEi', lhs,
    )

  @overload(int)
  def generate_Div(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Div(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Div

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Div(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_DivEi', lhs,
    )

  @overload(int)
  def generate_Mod(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Mod(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Mod

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Mod(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_ModEi', lhs,
    )

  @overload(int)
  def generate_Sub(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Sub(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Sub

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Sub(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler12generate_SubEi', lhs,
    )

  @overload(int)
  def generate_As(self, lhs: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_As(int lhs)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_As

    Parameters
    ----------

    lhs : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_As(int lhs)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler11generate_AsEi', lhs,
    )

  @overload(int, int, int)
  def generate_CallValue(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CallValue(int name,
    int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CallValue

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallValue(int name, int
    #      argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_CallValueEiii',
        name, argc, argv,
    )

  @overload(int, int, int, int)
  def generate_CallWithReceiver(
      self,
      name: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CallWithReceiver(int name, int
    thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallWithReceiver(int name,
    #      int thisObject, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_CallWithReceiverEiii'
        'i',
        name, thisObject, argc, argv,
    )

  @overload(int, int, int, int)
  def generate_CallProperty(
      self,
      name: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CallProperty(int
    name, int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallProperty(int name, int
    #      base, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_CallPropertyEiiii',
        name, base, argc, argv,
    )

  @overload(int, int, int, int)
  def generate_CallPropertyLookup(
      self,
      lookupIndex: int,
      base: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CallPropertyLookup(int lookupIndex,
    int base, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    lookupIndex : int
      Passed on as it is.

    base : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallPropertyLookup(int
    #      lookupIndex, int base, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler27generate_CallPropertyLookupEi'
        'iii',
        lookupIndex, base, argc, argv,
    )

  @overload(int, int, int)
  def generate_CallName(self, name: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CallName(int name,
    int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CallName

    Parameters
    ----------

    name : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallName(int name, int argc,
    #      int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_CallNameEiii',
        name, argc, argv,
    )

  @overload(int, int)
  def generate_CallPossiblyDirectEval(self, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CallPossiblyDirectEval(int argc, int
    argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallPossiblyDirectEval(int
    #      argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler31generate_CallPossiblyDirectEv'
        'alEii',
        argc, argv,
    )

  @overload(int, int, int)
  def generate_CallGlobalLookup(
      self,
      index: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CallGlobalLookup(int index, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallGlobalLookup(int index,
    #      int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_CallGlobalLookupEiii',
        index, argc, argv,
    )

  @overload(int, int, int)
  def generate_CallQmlContextPropertyLookup(
      self,
      index: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CallQmlContextPropertyLookup(int
    index, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void
    #      QV4::Moth::ByteCodeHandler::generate_CallQmlContextPropertyLookup(
    #      int index, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler37generate_CallQmlContextProper'
        'tyLookupEiii',
        index, argc, argv,
    )

  @overload(int, int, int, int)
  def generate_CallWithSpread(
      self,
      func: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CallWithSpread(int
    func, int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CallWithSpread(int func, int
    #      thisObject, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_CallWithSpreadEiiii',
        func, thisObject, argc, argv,
    )

  @overload(int, int, int)
  def generate_Construct(self, func: int, argc: int, argv: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Construct(int func,
    int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Construct

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Construct(int func, int
    #      argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_ConstructEiii',
        func, argc, argv,
    )

  @overload(int, int, int)
  def generate_ConstructWithSpread(
      self,
      func: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_ConstructWithSpread(int func, int
    argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    func : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ConstructWithSpread(int
    #      func, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler28generate_ConstructWithSpreadE'
        'iii',
        func, argc, argv,
    )

  @overload(int)
  def generate_SetUnwindHandler(self, offset: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_SetUnwindHandler(int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_SetUnwindHandler(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_SetUnwindHandlerEi',
        offset,
    )

  def generate_UnwindDispatch(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UnwindDispatch()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UnwindDispatch()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_UnwindDispatchEv',
    )

  @overload(int, int)
  def generate_UnwindToLabel(self, level: int, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_UnwindToLabel(int
    level, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    level : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_UnwindToLabel(int level, int
    #      offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler22generate_UnwindToLabelEii',
        level, offset,
    )

  @overload(int)
  def generate_DeadTemporalZoneCheck(self, name: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_DeadTemporalZoneCheck(int name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DeadTemporalZoneCheck(int
    #      name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler30generate_DeadTemporalZoneChec'
        'kEi',
        name,
    )

  def generate_ThrowException(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_ThrowException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ThrowException()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_ThrowExceptionEv',
    )

  def generate_GetException(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_GetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_GetException()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_GetExceptionEv',
    )

  def generate_SetException(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_SetException()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_SetException()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_SetExceptionEv',
    )

  def generate_CreateCallContext(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CreateCallContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CreateCallContext()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_CreateCallContextEv',
    )

  @overload(int, int)
  def generate_PushCatchContext(self, index: int, name: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_PushCatchContext(int index, int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PushCatchContext(int index,
    #      int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_PushCatchContextEii',
        index, name,
    )

  def generate_PushWithContext(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_PushWithContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PushWithContext()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler24generate_PushWithContextEv',
    )

  @overload(int)
  def generate_PushBlockContext(self, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_PushBlockContext(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PushBlockContext(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_PushBlockContextEi',
        index,
    )

  def generate_CloneBlockContext(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CloneBlockContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CloneBlockContext()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_CloneBlockContextEv',
    )

  def generate_PopContext(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_PopContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_PopContext
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PopContext()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_PopContextEv',
    )

  @overload(int)
  def generate_GetIterator(self, iterator: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_GetIterator(int
    iterator)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_GetIterator

    Parameters
    ----------

    iterator : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_GetIterator(int iterator)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_GetIteratorEi',
        iterator,
    )

  @overload(int, int)
  def generate_IteratorNext(self, value: int, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_IteratorNext(int
    value, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    value : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_IteratorNext(int value, int
    #      offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler21generate_IteratorNextEii',
        value, offset,
    )

  def generate_IteratorClose(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_IteratorClose()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_IteratorClose()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler22generate_IteratorCloseEv',
    )

  def generate_DestructureRestElement(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_DestructureRestElement()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DestructureRestElement()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler31generate_DestructureRestEleme'
        'ntEv',
    )

  @overload(int, int)
  def generate_DeleteProperty(self, base: int, index: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_DeleteProperty(int
    base, int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    base : int
      Passed on as it is.

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DeleteProperty(int base, int
    #      index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler23generate_DeletePropertyEii',
        base, index,
    )

  @overload(int)
  def generate_DeleteName(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_DeleteName(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_DeleteName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DeleteName(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_DeleteNameEi', name,
    )

  @overload(int)
  def generate_TypeofName(self, name: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_TypeofName(int
    name)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_TypeofName

    Parameters
    ----------

    name : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_TypeofName(int name)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_TypeofNameEi', name,
    )

  def generate_TypeofValue(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_TypeofValue()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_TypeofValue
    """
    #  void QV4::Moth::ByteCodeHandler::generate_TypeofValue()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_TypeofValueEv',
    )

  @overload(int, int)
  def generate_DeclareVar(self, varName: int, isDeletable: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_DeclareVar(int
    varName, int isDeletable)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_DeclareVar

    Parameters
    ----------

    varName : int
      Passed on as it is.

    isDeletable : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DeclareVar(int varName, int
    #      isDeletable)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler19generate_DeclareVarEii',
        varName, isDeletable,
    )

  @overload(int, int)
  def generate_DefineArray(self, argc: int, args: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_DefineArray(int
    argc, int args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_DefineArray

    Parameters
    ----------

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DefineArray(int argc, int
    #      args)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_DefineArrayEii',
        argc, args,
    )

  @overload(int, int, int)
  def generate_DefineObjectLiteral(
      self,
      internalClassId: int,
      argc: int,
      args: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_DefineObjectLiteral(int
    internalClassId, int argc, int args)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    internalClassId : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    args : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_DefineObjectLiteral(int
    #      internalClassId, int argc, int args)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler28generate_DefineObjectLiteralE'
        'iii',
        internalClassId, argc, args,
    )

  def generate_CreateMappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CreateMappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void
    #      QV4::Moth::ByteCodeHandler::generate_CreateMappedArgumentsObject()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler36generate_CreateMappedArgument'
        'sObjectEv',
    )

  def generate_CreateUnmappedArgumentsObject(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CreateUnmappedArgumentsObject()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::
    #      generate_CreateUnmappedArgumentsObject()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler38generate_CreateUnmappedArgume'
        'ntsObjectEv',
    )

  @overload(int)
  def generate_CreateRestParameter(self, argIndex: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_CreateRestParameter(int argIndex)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    argIndex : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CreateRestParameter(int
    #      argIndex)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler28generate_CreateRestParameterE'
        'i',
        argIndex,
    )

  def generate_Yield(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Yield()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Yield
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Yield()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_YieldEv',
    )

  def generate_YieldStar(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_YieldStar()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_YieldStar
    """
    #  void QV4::Moth::ByteCodeHandler::generate_YieldStar()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler18generate_YieldStarEv',
    )

  @overload(int)
  def generate_Resume(self, offset: int) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Resume(int
    offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Resume

    Parameters
    ----------

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Resume(int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler15generate_ResumeEi', offset,
    )

  @overload(int, int, int)
  def generate_IteratorNextForYieldStar(
      self,
      iterator: int,
      object: int,
      offset: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_IteratorNextForYieldStar(int
    iterator, int object, int offset)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    iterator : int
      Passed on as it is.

    object : int
      Passed on as it is.

    offset : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_IteratorNextForYieldStar(int
    #      iterator, int object, int offset)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler33generate_IteratorNextForYield'
        'StarEiii',
        iterator, object, offset,
    )

  @overload(int, int, int)
  def generate_CreateClass(
      self,
      classIndex: int,
      heritage: int,
      computedNames: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_CreateClass(int
    classIndex, int heritage, int computedNames)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_CreateClass

    Parameters
    ----------

    classIndex : int
      Passed on as it is.

    heritage : int
      Passed on as it is.

    computedNames : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_CreateClass(int classIndex,
    #      int heritage, int computedNames)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler20generate_CreateClassEiii',
        classIndex, heritage, computedNames,
    )

  def generate_LoadSuperConstructor(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_LoadSuperConstructor()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_LoadSuperConstructor()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler29generate_LoadSuperConstructor'
        'Ev',
    )

  @overload(int)
  def generate_PushScriptContext(self, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_PushScriptContext(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PushScriptContext(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_PushScriptContextEi',
        index,
    )

  def generate_PopScriptContext(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_PopScriptContext()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_PopScriptContext()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler25generate_PopScriptContextEv',
    )

  @overload(int, int)
  def generate_InitializeBlockDeadTemporalZone(
      self,
      firstReg: int,
      count: int,
  ) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_InitializeBlockDeadTemporalZone(int
    firstReg, int count)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    firstReg : int
      Passed on as it is.

    count : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::
    #      generate_InitializeBlockDeadTemporalZone(int firstReg, int count)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler40generate_InitializeBlockDeadT'
        'emporalZoneEii',
        firstReg, count,
    )

  def generate_ThrowOnNullOrUndefined(self) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_ThrowOnNullOrUndefined()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html
    """
    #  void QV4::Moth::ByteCodeHandler::generate_ThrowOnNullOrUndefined()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler31generate_ThrowOnNullOrUndefin'
        'edEv',
    )

  @overload(int)
  def generate_GetTemplateObject(self, index: int) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::generate_GetTemplateObject(int index)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html

    Parameters
    ----------

    index : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_GetTemplateObject(int index)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler26generate_GetTemplateObjectEi',
        index,
    )

  @overload(int, int, int, int)
  def generate_TailCall(
      self,
      func: int,
      thisObject: int,
      argc: int,
      argv: int,
  ) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_TailCall(int func,
    int thisObject, int argc, int argv)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_TailCall

    Parameters
    ----------

    func : int
      Passed on as it is.

    thisObject : int
      Passed on as it is.

    argc : int
      Passed on as it is.

    argv : int
      Passed on as it is.
    """
    #  void QV4::Moth::ByteCodeHandler::generate_TailCall(int func, int
    #      thisObject, int argc, int argv)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler17generate_TailCallEiiii',
        func, thisObject, argc, argv,
    )

  def generate_Debug(self) -> None:
    """
    Calls Qt's 'void QV4::Moth::ByteCodeHandler::generate_Debug()'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#generate_Debug
    """
    #  void QV4::Moth::ByteCodeHandler::generate_Debug()
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14generate_DebugEv',
    )

  @overload(QV4.Moth.Instr.Type)
  def endInstruction(self, instr: QV4.Moth.Instr.Type) -> None:
    """
    Calls Qt's 'void
    QV4::Moth::ByteCodeHandler::endInstruction(Moth::Instr::Type instr)'.

    Qt's own words:
    https://doc.qt.io/qt-6/qv4-moth-bytecodehandler.html#endInstruction

    Parameters
    ----------

    instr : QV4.Moth.Instr.Type
      Passed on as its number.
    """
    #  void QV4::Moth::ByteCodeHandler::endInstruction(Moth::Instr::Type
    #      instr)
    self.uglySide.call(
        'ritual_ZN3QV44Moth15ByteCodeHandler14endInstructionENS0_5Instr4Typ'
        'eE',
        instr.value,
    )

  @staticmethod
  def decode(*__, **_) -> Never:
    """
    Qt's 'void QV4::Moth::ByteCodeHandler::decode(const char *code, uint
    len)': cannot be called and cannot be called through the meta-object and
    cannot be copied: no header file has its code, Qt's source does not mark
    it or its class for use from outside Qt or writes it 'inline' or nowhere,
    and it is no signal, slot or invokable function giving back nothing, of a
    class built on QObject, and Qt's source has no code for it that could be
    told from the rest.
    """
    raise NotImplementedError(
        "'QV4.Moth.ByteCodeHandler.decode' has no cute function yet. Qt's "
        "'void QV4::Moth::ByteCodeHandler::decode(const char *code, uint "
        "len)': cannot be called and cannot be called through the "
        "meta-object and cannot be copied: no header file has its code, "
        "Qt's source does not mark it or its class for use from outside Qt "
        "or writes it 'inline' or nowhere, and it is no signal, slot or "
        "invokable function giving back nothing, of a class built on "
        "QObject, and Qt's source has no code for it that could be told "
        "from the rest.")

  @staticmethod
  def startInstruction(*__, **_) -> Never:
    """
    Qt's 'Verdict
    QV4::Moth::ByteCodeHandler::startInstruction(Moth::Instr::Type instr)':
    gives the enum 'QV4::Moth::ByteCodeHandler::Verdict', whose class cannot
    be named here.
    """
    raise NotImplementedError(
        "'QV4.Moth.ByteCodeHandler.startInstruction' has no cute function "
        "yet. Qt's 'Verdict "
        "QV4::Moth::ByteCodeHandler::startInstruction(Moth::Instr::Type "
        "instr)': gives the enum 'QV4::Moth::ByteCodeHandler::Verdict', "
        "whose class cannot be named here.")
