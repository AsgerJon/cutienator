//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <cstring>

//  Only a class built on QQmlJSCompilePass may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSCompilePass : QQmlJSCompilePass {
  using QQmlJSCompilePass::generate_Add;
  using QQmlJSCompilePass::generate_As;
  using QQmlJSCompilePass::generate_BitAnd;
  using QQmlJSCompilePass::generate_BitAndConst;
  using QQmlJSCompilePass::generate_BitOr;
  using QQmlJSCompilePass::generate_BitOrConst;
  using QQmlJSCompilePass::generate_BitXor;
  using QQmlJSCompilePass::generate_BitXorConst;
  using QQmlJSCompilePass::generate_CallGlobalLookup;
  using QQmlJSCompilePass::generate_CallName;
  using QQmlJSCompilePass::generate_CallPossiblyDirectEval;
  using QQmlJSCompilePass::generate_CallProperty;
  using QQmlJSCompilePass::generate_CallPropertyLookup;
  using QQmlJSCompilePass::generate_CallQmlContextPropertyLookup;
  using QQmlJSCompilePass::generate_CallValue;
  using QQmlJSCompilePass::generate_CallWithReceiver;
  using QQmlJSCompilePass::generate_CallWithSpread;
  using QQmlJSCompilePass::generate_CheckException;
  using QQmlJSCompilePass::generate_CloneBlockContext;
  using QQmlJSCompilePass::generate_CmpEq;
  using QQmlJSCompilePass::generate_CmpEqInt;
  using QQmlJSCompilePass::generate_CmpEqNull;
  using QQmlJSCompilePass::generate_CmpGe;
  using QQmlJSCompilePass::generate_CmpGt;
  using QQmlJSCompilePass::generate_CmpIn;
  using QQmlJSCompilePass::generate_CmpInstanceOf;
  using QQmlJSCompilePass::generate_CmpLe;
  using QQmlJSCompilePass::generate_CmpLt;
  using QQmlJSCompilePass::generate_CmpNe;
  using QQmlJSCompilePass::generate_CmpNeInt;
  using QQmlJSCompilePass::generate_CmpNeNull;
  using QQmlJSCompilePass::generate_CmpStrictEqual;
  using QQmlJSCompilePass::generate_CmpStrictNotEqual;
  using QQmlJSCompilePass::generate_Construct;
  using QQmlJSCompilePass::generate_ConstructWithSpread;
  using QQmlJSCompilePass::generate_ConvertThisToObject;
  using QQmlJSCompilePass::generate_CreateCallContext;
  using QQmlJSCompilePass::generate_CreateClass;
  using QQmlJSCompilePass::generate_CreateMappedArgumentsObject;
  using QQmlJSCompilePass::generate_CreateRestParameter;
  using QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject;
  using QQmlJSCompilePass::generate_DeadTemporalZoneCheck;
  using QQmlJSCompilePass::generate_Debug;
  using QQmlJSCompilePass::generate_DeclareVar;
  using QQmlJSCompilePass::generate_Decrement;
  using QQmlJSCompilePass::generate_DefineArray;
  using QQmlJSCompilePass::generate_DefineObjectLiteral;
  using QQmlJSCompilePass::generate_DeleteName;
  using QQmlJSCompilePass::generate_DeleteProperty;
  using QQmlJSCompilePass::generate_DestructureRestElement;
  using QQmlJSCompilePass::generate_Div;
  using QQmlJSCompilePass::generate_Exp;
  using QQmlJSCompilePass::generate_GetException;
  using QQmlJSCompilePass::generate_GetIterator;
  using QQmlJSCompilePass::generate_GetLookup;
  using QQmlJSCompilePass::generate_GetOptionalLookup;
  using QQmlJSCompilePass::generate_GetTemplateObject;
  using QQmlJSCompilePass::generate_Increment;
  using QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone;
  using QQmlJSCompilePass::generate_IteratorClose;
  using QQmlJSCompilePass::generate_IteratorNext;
  using QQmlJSCompilePass::generate_IteratorNextForYieldStar;
  using QQmlJSCompilePass::generate_Jump;
  using QQmlJSCompilePass::generate_JumpFalse;
  using QQmlJSCompilePass::generate_JumpNoException;
  using QQmlJSCompilePass::generate_JumpNotUndefined;
  using QQmlJSCompilePass::generate_JumpTrue;
  using QQmlJSCompilePass::generate_LoadClosure;
  using QQmlJSCompilePass::generate_LoadConst;
  using QQmlJSCompilePass::generate_LoadElement;
  using QQmlJSCompilePass::generate_LoadFalse;
  using QQmlJSCompilePass::generate_LoadGlobalLookup;
  using QQmlJSCompilePass::generate_LoadImport;
  using QQmlJSCompilePass::generate_LoadInt;
  using QQmlJSCompilePass::generate_LoadLocal;
  using QQmlJSCompilePass::generate_LoadName;
  using QQmlJSCompilePass::generate_LoadNull;
  using QQmlJSCompilePass::generate_LoadOptionalProperty;
  using QQmlJSCompilePass::generate_LoadProperty;
  using QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup;
  using QQmlJSCompilePass::generate_LoadReg;
  using QQmlJSCompilePass::generate_LoadRuntimeString;
  using QQmlJSCompilePass::generate_LoadScopedLocal;
  using QQmlJSCompilePass::generate_LoadSuperConstructor;
  using QQmlJSCompilePass::generate_LoadSuperProperty;
  using QQmlJSCompilePass::generate_LoadTrue;
  using QQmlJSCompilePass::generate_LoadUndefined;
  using QQmlJSCompilePass::generate_LoadZero;
  using QQmlJSCompilePass::generate_Mod;
  using QQmlJSCompilePass::generate_MoveConst;
  using QQmlJSCompilePass::generate_MoveReg;
  using QQmlJSCompilePass::generate_MoveRegExp;
  using QQmlJSCompilePass::generate_Mul;
  using QQmlJSCompilePass::generate_PopContext;
  using QQmlJSCompilePass::generate_PopScriptContext;
  using QQmlJSCompilePass::generate_PushBlockContext;
  using QQmlJSCompilePass::generate_PushCatchContext;
  using QQmlJSCompilePass::generate_PushScriptContext;
  using QQmlJSCompilePass::generate_PushWithContext;
  using QQmlJSCompilePass::generate_Resume;
  using QQmlJSCompilePass::generate_Ret;
  using QQmlJSCompilePass::generate_SetException;
  using QQmlJSCompilePass::generate_SetLookup;
  using QQmlJSCompilePass::generate_SetUnwindHandler;
  using QQmlJSCompilePass::generate_Shl;
  using QQmlJSCompilePass::generate_ShlConst;
  using QQmlJSCompilePass::generate_Shr;
  using QQmlJSCompilePass::generate_ShrConst;
  using QQmlJSCompilePass::generate_StoreElement;
  using QQmlJSCompilePass::generate_StoreLocal;
  using QQmlJSCompilePass::generate_StoreNameSloppy;
  using QQmlJSCompilePass::generate_StoreNameStrict;
  using QQmlJSCompilePass::generate_StoreProperty;
  using QQmlJSCompilePass::generate_StoreReg;
  using QQmlJSCompilePass::generate_StoreScopedLocal;
  using QQmlJSCompilePass::generate_StoreSuperProperty;
  using QQmlJSCompilePass::generate_Sub;
  using QQmlJSCompilePass::generate_TailCall;
  using QQmlJSCompilePass::generate_ThrowException;
  using QQmlJSCompilePass::generate_ThrowOnNullOrUndefined;
  using QQmlJSCompilePass::generate_ToObject;
  using QQmlJSCompilePass::generate_TypeofName;
  using QQmlJSCompilePass::generate_TypeofValue;
  using QQmlJSCompilePass::generate_UCompl;
  using QQmlJSCompilePass::generate_UMinus;
  using QQmlJSCompilePass::generate_UNot;
  using QQmlJSCompilePass::generate_UPlus;
  using QQmlJSCompilePass::generate_UShr;
  using QQmlJSCompilePass::generate_UShrConst;
  using QQmlJSCompilePass::generate_UnwindDispatch;
  using QQmlJSCompilePass::generate_UnwindToLabel;
  using QQmlJSCompilePass::generate_Yield;
  using QQmlJSCompilePass::generate_YieldStar;
};

//  A QQmlJSCompilePass that Python can take functions over in. Every QQmlJSCompilePass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSCompilePassCall0)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall1)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall2)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall3)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall4)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall5)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall6)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall7)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall8)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall9)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall10)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall11)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall12)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall13)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall14)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall15)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall16)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall17)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall18)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall19)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall20)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall21)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall22)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall23)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall24)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall25)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall26)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall27)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall28)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall29)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall30)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall31)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall32)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall33)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall34)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall35)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall36)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall37)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall38)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall39)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall40)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall41)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall42)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall43)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall44)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall45)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall46)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall47)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall48)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall49)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall50)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall51)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall52)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall53)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall54)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall55)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall56)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall57)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall58)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall59)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall60)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall61)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall62)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall63)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall64)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall65)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall66)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall67)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall68)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall69)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall70)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall71)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall72)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall73)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall74)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall75)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall76)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall77)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall78)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall79)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall80)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall81)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall82)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall83)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall84)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall85)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall86)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall87)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall88)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall89)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall90)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall91)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall92)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall93)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall94)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall95)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall96)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall97)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall98)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall99)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall100)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall101)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall102)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall103)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall104)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall105)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall106)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall107)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall108)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall109)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall110)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall111)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall112)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall113)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall114)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall115)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall116)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall117)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall118)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall119)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall120)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall121)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall122)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall123)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall124)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall125)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall126)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall127)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall128)(const void *, int, int *);
typedef void (*CuteQQmlJSCompilePassCall129)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall130)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCompilePassCall131)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall132)(const void *, int *);
typedef void (*CuteQQmlJSCompilePassCall133)(const void *, int, int *);
class CuteQQmlJSCompilePass : public QQmlJSCompilePass {
public:
  using QQmlJSCompilePass::QQmlJSCompilePass;
  void *taken[134] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_AddEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler11generate_AsEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitAndEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitAndConstEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_BitOrEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_BitOrConstEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitXorEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitXorConstEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallGlobalLookupEiii")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CallNameEiii")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_CallPossiblyDirectEvalEii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_CallPropertyEiiii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_CallPropertyLookupEiiii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_CallQmlContextPropertyLookupEiii")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CallValueEiii")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallWithReceiverEiiii")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CallWithSpreadEiiii")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CheckExceptionEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CloneBlockContextEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpEqEi")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpEqIntEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpEqNullEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGeEi")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGtEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpInEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_CmpInstanceOfEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLeEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLtEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpNeEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpNeIntEi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpNeNullEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CmpStrictEqualEi")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CmpStrictNotEqualEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_ConstructEiii")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConstructWithSpreadEiii")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConvertThisToObjectEv")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CreateCallContextEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_CreateClassEiii")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler36generate_CreateMappedArgumentsObjectEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_CreateRestParameterEi")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler38generate_CreateUnmappedArgumentsObjectEv")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler30generate_DeadTemporalZoneCheckEi")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_DebugEv")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeclareVarEii")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_DecrementEv")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_DefineArrayEii")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_DefineObjectLiteralEiii")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeleteNameEi")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_DeletePropertyEii")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_DestructureRestElementEv")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_DivEi")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ExpEi")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_GetExceptionEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_GetIteratorEi")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_GetLookupEi")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetOptionalLookupEii")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetTemplateObjectEi")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_IncrementEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler40generate_InitializeBlockDeadTemporalZoneEii")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_IteratorCloseEv")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_IteratorNextEii")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler33generate_IteratorNextForYieldStarEiii")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_JumpEi")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_JumpFalseEi")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_JumpNoExceptionEi")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_JumpNotUndefinedEi")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_JumpTrueEi")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadClosureEi")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadConstEi")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadElementEi")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadFalseEv")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_LoadGlobalLookupEi")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_LoadImportEi")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadIntEi")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadLocalEi")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNameEi")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNullEv")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadOptionalPropertyEii")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_LoadPropertyEi")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_LoadQmlContextPropertyLookupEi")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadRegEi")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadRuntimeStringEi")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_LoadScopedLocalEii")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadSuperConstructorEv")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadSuperPropertyEi")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadTrueEv")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_LoadUndefinedEv")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadZeroEv")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ModEi")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_MoveConstEii")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_MoveRegEii")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_MoveRegExpEii")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_MulEi")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_PopContextEv")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PopScriptContextEv")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushBlockContextEi")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushCatchContextEii")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_PushScriptContextEi")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_PushWithContextEv")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_ResumeEi")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_RetEv")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_SetExceptionEv")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_SetLookupEii")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_SetUnwindHandlerEi")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShlEi")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShlConstEi")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShrEi")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShrConstEi")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_StoreElementEii")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_StoreLocalEi")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameSloppyEi")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameStrictEi")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_StorePropertyEii")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_StoreRegEi")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_StoreScopedLocalEii")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_StoreSuperPropertyEi")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_SubEi")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_TailCallEiiii")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_ThrowExceptionEv")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_ThrowOnNullOrUndefinedEv")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ToObjectEv")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_TypeofNameEi")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_TypeofValueEv")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UComplEv")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UMinusEv")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UNotEv")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_UPlusEv")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UShrEi")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_UShrConstEi")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_UnwindDispatchEv")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_UnwindToLabelEii")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_YieldEv")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_YieldStarEv")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14endInstructionENS0_5Instr4TypeE")) {
      taken[133] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJSCompilePass::generate_Add(int a0)
  void generate_Add(int a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall0 call = reinterpret_cast<CuteQQmlJSCompilePassCall0>(taken[0]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Add(a0);
  }

  //  void QQmlJSCompilePass::generate_As(int a0)
  void generate_As(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall1 call = reinterpret_cast<CuteQQmlJSCompilePassCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_As(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAnd(int a0)
  void generate_BitAnd(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall2 call = reinterpret_cast<CuteQQmlJSCompilePassCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAnd(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAndConst(int a0)
  void generate_BitAndConst(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall3 call = reinterpret_cast<CuteQQmlJSCompilePassCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAndConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOr(int a0)
  void generate_BitOr(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall4 call = reinterpret_cast<CuteQQmlJSCompilePassCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOr(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOrConst(int a0)
  void generate_BitOrConst(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall5 call = reinterpret_cast<CuteQQmlJSCompilePassCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXor(int a0)
  void generate_BitXor(int a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall6 call = reinterpret_cast<CuteQQmlJSCompilePassCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitXor(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXorConst(int a0)
  void generate_BitXorConst(int a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall7 call = reinterpret_cast<CuteQQmlJSCompilePassCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitXorConst(a0);
  }

  //  void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int a1, int
  //      a2)
  void generate_CallGlobalLookup(int a0, int a1, int a2) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall8 call = reinterpret_cast<CuteQQmlJSCompilePassCall8>(taken[8]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallGlobalLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
  void generate_CallName(int a0, int a1, int a2) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall9 call = reinterpret_cast<CuteQQmlJSCompilePassCall9>(taken[9]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallName(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int a0, int
  //      a1)
  void generate_CallPossiblyDirectEval(int a0, int a1) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall10 call = reinterpret_cast<CuteQQmlJSCompilePassCall10>(taken[10]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallPossiblyDirectEval(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_CallProperty(int a0, int a1, int a2,
  //      int a3)
  void generate_CallProperty(int a0, int a1, int a2, int a3) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall11 call = reinterpret_cast<CuteQQmlJSCompilePassCall11>(taken[11]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallProperty(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CallPropertyLookup(int a0, int a1,
  //      int a2, int a3)
  void generate_CallPropertyLookup(int a0, int a1, int a2, int a3) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall12 call = reinterpret_cast<CuteQQmlJSCompilePassCall12>(taken[12]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallPropertyLookup(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(int a0,
  //      int a1, int a2)
  void generate_CallQmlContextPropertyLookup(
      int a0,
      int a1,
      int a2) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall13 call = reinterpret_cast<CuteQQmlJSCompilePassCall13>(taken[13]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
  void generate_CallValue(int a0, int a1, int a2) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall14 call = reinterpret_cast<CuteQQmlJSCompilePassCall14>(taken[14]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallValue(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int a1, int
  //      a2, int a3)
  void generate_CallWithReceiver(int a0, int a1, int a2, int a3) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall15 call = reinterpret_cast<CuteQQmlJSCompilePassCall15>(taken[15]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallWithReceiver(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CallWithSpread(int a0, int a1, int
  //      a2, int a3)
  void generate_CallWithSpread(int a0, int a1, int a2, int a3) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall16 call = reinterpret_cast<CuteQQmlJSCompilePassCall16>(taken[16]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallWithSpread(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CheckException()
  void generate_CheckException() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall17 call = reinterpret_cast<CuteQQmlJSCompilePassCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CheckException();
  }

  //  void QQmlJSCompilePass::generate_CloneBlockContext()
  void generate_CloneBlockContext() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall18 call = reinterpret_cast<CuteQQmlJSCompilePassCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CloneBlockContext();
  }

  //  void QQmlJSCompilePass::generate_CmpEq(int a0)
  void generate_CmpEq(int a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall19 call = reinterpret_cast<CuteQQmlJSCompilePassCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEq(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
  void generate_CmpEqInt(int a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall20 call = reinterpret_cast<CuteQQmlJSCompilePassCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqNull()
  void generate_CmpEqNull() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall21 call = reinterpret_cast<CuteQQmlJSCompilePassCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqNull();
  }

  //  void QQmlJSCompilePass::generate_CmpGe(int a0)
  void generate_CmpGe(int a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall22 call = reinterpret_cast<CuteQQmlJSCompilePassCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpGt(int a0)
  void generate_CmpGt(int a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall23 call = reinterpret_cast<CuteQQmlJSCompilePassCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpIn(int a0)
  void generate_CmpIn(int a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall24 call = reinterpret_cast<CuteQQmlJSCompilePassCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpIn(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
  void generate_CmpInstanceOf(int a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall25 call = reinterpret_cast<CuteQQmlJSCompilePassCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpInstanceOf(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLe(int a0)
  void generate_CmpLe(int a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall26 call = reinterpret_cast<CuteQQmlJSCompilePassCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLt(int a0)
  void generate_CmpLt(int a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall27 call = reinterpret_cast<CuteQQmlJSCompilePassCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNe(int a0)
  void generate_CmpNe(int a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall28 call = reinterpret_cast<CuteQQmlJSCompilePassCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
  void generate_CmpNeInt(int a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall29 call = reinterpret_cast<CuteQQmlJSCompilePassCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeNull()
  void generate_CmpNeNull() override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall30 call = reinterpret_cast<CuteQQmlJSCompilePassCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeNull();
  }

  //  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
  void generate_CmpStrictEqual(int a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall31 call = reinterpret_cast<CuteQQmlJSCompilePassCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
  void generate_CmpStrictNotEqual(int a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall32 call = reinterpret_cast<CuteQQmlJSCompilePassCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictNotEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
  void generate_Construct(int a0, int a1, int a2) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall33 call = reinterpret_cast<CuteQQmlJSCompilePassCall33>(taken[33]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Construct(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_ConstructWithSpread(int a0, int a1,
  //      int a2)
  void generate_ConstructWithSpread(int a0, int a1, int a2) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall34 call = reinterpret_cast<CuteQQmlJSCompilePassCall34>(taken[34]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConstructWithSpread(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_ConvertThisToObject()
  void generate_ConvertThisToObject() override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall35 call = reinterpret_cast<CuteQQmlJSCompilePassCall35>(taken[35]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConvertThisToObject();
  }

  //  void QQmlJSCompilePass::generate_CreateCallContext()
  void generate_CreateCallContext() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall36 call = reinterpret_cast<CuteQQmlJSCompilePassCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateCallContext();
  }

  //  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
  void generate_CreateClass(int a0, int a1, int a2) override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall37 call = reinterpret_cast<CuteQQmlJSCompilePassCall37>(taken[37]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateClass(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
  void generate_CreateMappedArgumentsObject() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall38 call = reinterpret_cast<CuteQQmlJSCompilePassCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateMappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
  void generate_CreateRestParameter(int a0) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall39 call = reinterpret_cast<CuteQQmlJSCompilePassCall39>(taken[39]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateRestParameter(a0);
  }

  //  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
  void generate_CreateUnmappedArgumentsObject() override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall40 call = reinterpret_cast<CuteQQmlJSCompilePassCall40>(taken[40]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
  void generate_DeadTemporalZoneCheck(int a0) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall41 call = reinterpret_cast<CuteQQmlJSCompilePassCall41>(taken[41]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeadTemporalZoneCheck(a0);
  }

  //  void QQmlJSCompilePass::generate_Debug()
  void generate_Debug() override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall42 call = reinterpret_cast<CuteQQmlJSCompilePassCall42>(taken[42]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Debug();
  }

  //  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
  void generate_DeclareVar(int a0, int a1) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall43 call = reinterpret_cast<CuteQQmlJSCompilePassCall43>(taken[43]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeclareVar(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Decrement()
  void generate_Decrement() override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall44 call = reinterpret_cast<CuteQQmlJSCompilePassCall44>(taken[44]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Decrement();
  }

  //  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
  void generate_DefineArray(int a0, int a1) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall45 call = reinterpret_cast<CuteQQmlJSCompilePassCall45>(taken[45]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DefineArray(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0, int a1,
  //      int a2)
  void generate_DefineObjectLiteral(int a0, int a1, int a2) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall46 call = reinterpret_cast<CuteQQmlJSCompilePassCall46>(taken[46]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DefineObjectLiteral(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_DeleteName(int a0)
  void generate_DeleteName(int a0) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall47 call = reinterpret_cast<CuteQQmlJSCompilePassCall47>(taken[47]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteName(a0);
  }

  //  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
  void generate_DeleteProperty(int a0, int a1) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall48 call = reinterpret_cast<CuteQQmlJSCompilePassCall48>(taken[48]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_DestructureRestElement()
  void generate_DestructureRestElement() override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall49 call = reinterpret_cast<CuteQQmlJSCompilePassCall49>(taken[49]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DestructureRestElement();
  }

  //  void QQmlJSCompilePass::generate_Div(int a0)
  void generate_Div(int a0) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall50 call = reinterpret_cast<CuteQQmlJSCompilePassCall50>(taken[50]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Div(a0);
  }

  //  void QQmlJSCompilePass::generate_Exp(int a0)
  void generate_Exp(int a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall51 call = reinterpret_cast<CuteQQmlJSCompilePassCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Exp(a0);
  }

  //  void QQmlJSCompilePass::generate_GetException()
  void generate_GetException() override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall52 call = reinterpret_cast<CuteQQmlJSCompilePassCall52>(taken[52]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetException();
  }

  //  void QQmlJSCompilePass::generate_GetIterator(int a0)
  void generate_GetIterator(int a0) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall53 call = reinterpret_cast<CuteQQmlJSCompilePassCall53>(taken[53]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetIterator(a0);
  }

  //  void QQmlJSCompilePass::generate_GetLookup(int a0)
  void generate_GetLookup(int a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall54 call = reinterpret_cast<CuteQQmlJSCompilePassCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
  void generate_GetOptionalLookup(int a0, int a1) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall55 call = reinterpret_cast<CuteQQmlJSCompilePassCall55>(taken[55]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetOptionalLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
  void generate_GetTemplateObject(int a0) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall56 call = reinterpret_cast<CuteQQmlJSCompilePassCall56>(taken[56]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetTemplateObject(a0);
  }

  //  void QQmlJSCompilePass::generate_Increment()
  void generate_Increment() override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall57 call = reinterpret_cast<CuteQQmlJSCompilePassCall57>(taken[57]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Increment();
  }

  //  void QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int
  //      a0, int a1)
  void generate_InitializeBlockDeadTemporalZone(int a0, int a1) override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall58 call = reinterpret_cast<CuteQQmlJSCompilePassCall58>(taken[58]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_IteratorClose()
  void generate_IteratorClose() override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall59 call = reinterpret_cast<CuteQQmlJSCompilePassCall59>(taken[59]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorClose();
  }

  //  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
  void generate_IteratorNext(int a0, int a1) override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall60 call = reinterpret_cast<CuteQQmlJSCompilePassCall60>(taken[60]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorNext(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int a0, int
  //      a1, int a2)
  void generate_IteratorNextForYieldStar(int a0, int a1, int a2) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall61 call = reinterpret_cast<CuteQQmlJSCompilePassCall61>(taken[61]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorNextForYieldStar(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_Jump(int a0)
  void generate_Jump(int a0) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall62 call = reinterpret_cast<CuteQQmlJSCompilePassCall62>(taken[62]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Jump(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpFalse(int a0)
  void generate_JumpFalse(int a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall63 call = reinterpret_cast<CuteQQmlJSCompilePassCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpFalse(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNoException(int a0)
  void generate_JumpNoException(int a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall64 call = reinterpret_cast<CuteQQmlJSCompilePassCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNoException(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
  void generate_JumpNotUndefined(int a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall65 call = reinterpret_cast<CuteQQmlJSCompilePassCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNotUndefined(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpTrue(int a0)
  void generate_JumpTrue(int a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall66 call = reinterpret_cast<CuteQQmlJSCompilePassCall66>(taken[66]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpTrue(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadClosure(int a0)
  void generate_LoadClosure(int a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall67 call = reinterpret_cast<CuteQQmlJSCompilePassCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadClosure(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadConst(int a0)
  void generate_LoadConst(int a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall68 call = reinterpret_cast<CuteQQmlJSCompilePassCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadConst(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadElement(int a0)
  void generate_LoadElement(int a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall69 call = reinterpret_cast<CuteQQmlJSCompilePassCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadElement(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadFalse()
  void generate_LoadFalse() override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall70 call = reinterpret_cast<CuteQQmlJSCompilePassCall70>(taken[70]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadFalse();
  }

  //  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
  void generate_LoadGlobalLookup(int a0) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall71 call = reinterpret_cast<CuteQQmlJSCompilePassCall71>(taken[71]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadGlobalLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadImport(int a0)
  void generate_LoadImport(int a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall72 call = reinterpret_cast<CuteQQmlJSCompilePassCall72>(taken[72]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadImport(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadInt(int a0)
  void generate_LoadInt(int a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall73 call = reinterpret_cast<CuteQQmlJSCompilePassCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadInt(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadLocal(int a0)
  void generate_LoadLocal(int a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall74 call = reinterpret_cast<CuteQQmlJSCompilePassCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadName(int a0)
  void generate_LoadName(int a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall75 call = reinterpret_cast<CuteQQmlJSCompilePassCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadName(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadNull()
  void generate_LoadNull() override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall76 call = reinterpret_cast<CuteQQmlJSCompilePassCall76>(taken[76]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadNull();
  }

  //  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
  void generate_LoadOptionalProperty(int a0, int a1) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall77 call = reinterpret_cast<CuteQQmlJSCompilePassCall77>(taken[77]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadOptionalProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadProperty(int a0)
  void generate_LoadProperty(int a0) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall78 call = reinterpret_cast<CuteQQmlJSCompilePassCall78>(taken[78]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
  void generate_LoadQmlContextPropertyLookup(int a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall79 call = reinterpret_cast<CuteQQmlJSCompilePassCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadReg(int a0)
  void generate_LoadReg(int a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall80 call = reinterpret_cast<CuteQQmlJSCompilePassCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadReg(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
  void generate_LoadRuntimeString(int a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall81 call = reinterpret_cast<CuteQQmlJSCompilePassCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadRuntimeString(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
  void generate_LoadScopedLocal(int a0, int a1) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall82 call = reinterpret_cast<CuteQQmlJSCompilePassCall82>(taken[82]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadSuperConstructor()
  void generate_LoadSuperConstructor() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall83 call = reinterpret_cast<CuteQQmlJSCompilePassCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperConstructor();
  }

  //  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
  void generate_LoadSuperProperty(int a0) override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall84 call = reinterpret_cast<CuteQQmlJSCompilePassCall84>(taken[84]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadTrue()
  void generate_LoadTrue() override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall85 call = reinterpret_cast<CuteQQmlJSCompilePassCall85>(taken[85]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadTrue();
  }

  //  void QQmlJSCompilePass::generate_LoadUndefined()
  void generate_LoadUndefined() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall86 call = reinterpret_cast<CuteQQmlJSCompilePassCall86>(taken[86]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadUndefined();
  }

  //  void QQmlJSCompilePass::generate_LoadZero()
  void generate_LoadZero() override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall87 call = reinterpret_cast<CuteQQmlJSCompilePassCall87>(taken[87]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadZero();
  }

  //  void QQmlJSCompilePass::generate_Mod(int a0)
  void generate_Mod(int a0) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall88 call = reinterpret_cast<CuteQQmlJSCompilePassCall88>(taken[88]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mod(a0);
  }

  //  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
  void generate_MoveConst(int a0, int a1) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall89 call = reinterpret_cast<CuteQQmlJSCompilePassCall89>(taken[89]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveConst(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
  void generate_MoveReg(int a0, int a1) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall90 call = reinterpret_cast<CuteQQmlJSCompilePassCall90>(taken[90]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveReg(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
  void generate_MoveRegExp(int a0, int a1) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall91 call = reinterpret_cast<CuteQQmlJSCompilePassCall91>(taken[91]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveRegExp(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Mul(int a0)
  void generate_Mul(int a0) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall92 call = reinterpret_cast<CuteQQmlJSCompilePassCall92>(taken[92]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mul(a0);
  }

  //  void QQmlJSCompilePass::generate_PopContext()
  void generate_PopContext() override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall93 call = reinterpret_cast<CuteQQmlJSCompilePassCall93>(taken[93]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopContext();
  }

  //  void QQmlJSCompilePass::generate_PopScriptContext()
  void generate_PopScriptContext() override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall94 call = reinterpret_cast<CuteQQmlJSCompilePassCall94>(taken[94]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopScriptContext();
  }

  //  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
  void generate_PushBlockContext(int a0) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall95 call = reinterpret_cast<CuteQQmlJSCompilePassCall95>(taken[95]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushBlockContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
  void generate_PushCatchContext(int a0, int a1) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall96 call = reinterpret_cast<CuteQQmlJSCompilePassCall96>(taken[96]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushCatchContext(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
  void generate_PushScriptContext(int a0) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall97 call = reinterpret_cast<CuteQQmlJSCompilePassCall97>(taken[97]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushScriptContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushWithContext()
  void generate_PushWithContext() override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall98 call = reinterpret_cast<CuteQQmlJSCompilePassCall98>(taken[98]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushWithContext();
  }

  //  void QQmlJSCompilePass::generate_Resume(int a0)
  void generate_Resume(int a0) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall99 call = reinterpret_cast<CuteQQmlJSCompilePassCall99>(taken[99]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Resume(a0);
  }

  //  void QQmlJSCompilePass::generate_Ret()
  void generate_Ret() override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall100 call = reinterpret_cast<CuteQQmlJSCompilePassCall100>(taken[100]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Ret();
  }

  //  void QQmlJSCompilePass::generate_SetException()
  void generate_SetException() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall101 call = reinterpret_cast<CuteQQmlJSCompilePassCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetException();
  }

  //  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
  void generate_SetLookup(int a0, int a1) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall102 call = reinterpret_cast<CuteQQmlJSCompilePassCall102>(taken[102]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
  void generate_SetUnwindHandler(int a0) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall103 call = reinterpret_cast<CuteQQmlJSCompilePassCall103>(taken[103]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetUnwindHandler(a0);
  }

  //  void QQmlJSCompilePass::generate_Shl(int a0)
  void generate_Shl(int a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall104 call = reinterpret_cast<CuteQQmlJSCompilePassCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shl(a0);
  }

  //  void QQmlJSCompilePass::generate_ShlConst(int a0)
  void generate_ShlConst(int a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall105 call = reinterpret_cast<CuteQQmlJSCompilePassCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShlConst(a0);
  }

  //  void QQmlJSCompilePass::generate_Shr(int a0)
  void generate_Shr(int a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall106 call = reinterpret_cast<CuteQQmlJSCompilePassCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shr(a0);
  }

  //  void QQmlJSCompilePass::generate_ShrConst(int a0)
  void generate_ShrConst(int a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall107 call = reinterpret_cast<CuteQQmlJSCompilePassCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
  void generate_StoreElement(int a0, int a1) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall108 call = reinterpret_cast<CuteQQmlJSCompilePassCall108>(taken[108]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreElement(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreLocal(int a0)
  void generate_StoreLocal(int a0) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall109 call = reinterpret_cast<CuteQQmlJSCompilePassCall109>(taken[109]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
  void generate_StoreNameSloppy(int a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall110 call = reinterpret_cast<CuteQQmlJSCompilePassCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameSloppy(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
  void generate_StoreNameStrict(int a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall111 call = reinterpret_cast<CuteQQmlJSCompilePassCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameStrict(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
  void generate_StoreProperty(int a0, int a1) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall112 call = reinterpret_cast<CuteQQmlJSCompilePassCall112>(taken[112]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreReg(int a0)
  void generate_StoreReg(int a0) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall113 call = reinterpret_cast<CuteQQmlJSCompilePassCall113>(taken[113]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreReg(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
  void generate_StoreScopedLocal(int a0, int a1) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall114 call = reinterpret_cast<CuteQQmlJSCompilePassCall114>(taken[114]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
  void generate_StoreSuperProperty(int a0) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall115 call = reinterpret_cast<CuteQQmlJSCompilePassCall115>(taken[115]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_Sub(int a0)
  void generate_Sub(int a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall116 call = reinterpret_cast<CuteQQmlJSCompilePassCall116>(taken[116]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Sub(a0);
  }

  //  void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int a2, int
  //      a3)
  void generate_TailCall(int a0, int a1, int a2, int a3) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall117 call = reinterpret_cast<CuteQQmlJSCompilePassCall117>(taken[117]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TailCall(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_ThrowException()
  void generate_ThrowException() override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall118 call = reinterpret_cast<CuteQQmlJSCompilePassCall118>(taken[118]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowException();
  }

  //  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
  void generate_ThrowOnNullOrUndefined() override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall119 call = reinterpret_cast<CuteQQmlJSCompilePassCall119>(taken[119]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowOnNullOrUndefined();
  }

  //  void QQmlJSCompilePass::generate_ToObject()
  void generate_ToObject() override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall120 call = reinterpret_cast<CuteQQmlJSCompilePassCall120>(taken[120]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ToObject();
  }

  //  void QQmlJSCompilePass::generate_TypeofName(int a0)
  void generate_TypeofName(int a0) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall121 call = reinterpret_cast<CuteQQmlJSCompilePassCall121>(taken[121]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofName(a0);
  }

  //  void QQmlJSCompilePass::generate_TypeofValue()
  void generate_TypeofValue() override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall122 call = reinterpret_cast<CuteQQmlJSCompilePassCall122>(taken[122]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofValue();
  }

  //  void QQmlJSCompilePass::generate_UCompl()
  void generate_UCompl() override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall123 call = reinterpret_cast<CuteQQmlJSCompilePassCall123>(taken[123]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UCompl();
  }

  //  void QQmlJSCompilePass::generate_UMinus()
  void generate_UMinus() override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall124 call = reinterpret_cast<CuteQQmlJSCompilePassCall124>(taken[124]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UMinus();
  }

  //  void QQmlJSCompilePass::generate_UNot()
  void generate_UNot() override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall125 call = reinterpret_cast<CuteQQmlJSCompilePassCall125>(taken[125]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UNot();
  }

  //  void QQmlJSCompilePass::generate_UPlus()
  void generate_UPlus() override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall126 call = reinterpret_cast<CuteQQmlJSCompilePassCall126>(taken[126]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UPlus();
  }

  //  void QQmlJSCompilePass::generate_UShr(int a0)
  void generate_UShr(int a0) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall127 call = reinterpret_cast<CuteQQmlJSCompilePassCall127>(taken[127]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShr(a0);
  }

  //  void QQmlJSCompilePass::generate_UShrConst(int a0)
  void generate_UShrConst(int a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall128 call = reinterpret_cast<CuteQQmlJSCompilePassCall128>(taken[128]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_UnwindDispatch()
  void generate_UnwindDispatch() override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall129 call = reinterpret_cast<CuteQQmlJSCompilePassCall129>(taken[129]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindDispatch();
  }

  //  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
  void generate_UnwindToLabel(int a0, int a1) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall130 call = reinterpret_cast<CuteQQmlJSCompilePassCall130>(taken[130]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindToLabel(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Yield()
  void generate_Yield() override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall131 call = reinterpret_cast<CuteQQmlJSCompilePassCall131>(taken[131]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Yield();
  }

  //  void QQmlJSCompilePass::generate_YieldStar()
  void generate_YieldStar() override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall132 call = reinterpret_cast<CuteQQmlJSCompilePassCall132>(taken[132]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_YieldStar();
  }

  //  void QV4::Moth::ByteCodeHandler::endInstruction(Moth::Instr::Type
  //      instr)
  void endInstruction(QV4::Moth::Instr::Type instr) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSCompilePassCall133 call = reinterpret_cast<CuteQQmlJSCompilePassCall133>(taken[133]);
      call(this, static_cast<int>(instr), &handled);
      if (handled) return;
    }
  }
};

//  int QQmlJSCompilePass::firstRegisterIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQmlJSCompilePass18firstRegisterIndexEv(
    const QQmlJSCompilePass *self) {
  return self->firstRegisterIndex();
}

//  bool QQmlJSCompilePass::isArgument(int registerIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQmlJSCompilePass10isArgumentEi(
    const QQmlJSCompilePass *self,
    int registerIndex) {
  return self->isArgument(registerIndex);
}

//  QQmlJSRegisterContent QQmlJSCompilePass::argumentType(int registerIndex)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK17QQmlJSCompilePass12argumentTypeEi(
    const QQmlJSCompilePass *self,
    int registerIndex) {
  return new QQmlJSRegisterContent(self->argumentType(registerIndex));
}

//  bool QQmlJSCompilePass::isQmlScopeObject(QQmlJSRegisterContent content)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlJSCompilePass16isQmlScopeObjectE21QQmlJSRegisterContent(
    QQmlJSCompilePass *self,
    const QQmlJSRegisterContent *content) {
  return self->isQmlScopeObject(*content);
}

//  State QQmlJSCompilePass::initialState(const Function *function)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::State *ritual_ZN17QQmlJSCompilePass12initialStateEPKNS_8FunctionE(
    QQmlJSCompilePass *self,
    const QQmlJSCompilePass::Function *function) {
  return new QQmlJSCompilePass::State(self->initialState(function));
}

//  State QQmlJSCompilePass::nextStateFromAnnotations(const State &oldState,
//      const InstructionAnnotations &annotations)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::State *ritual_ZN17QQmlJSCompilePass24nextStateFromAnnotationsERKNS_5StateERK8QFlatMapIiNS_21InstructionAnnotationESt4lessIiE5QListIiES7_IS4_EE(
    QQmlJSCompilePass *self,
    const QQmlJSCompilePass::State *oldState,
    const QQmlJSCompilePass::InstructionAnnotations *annotations) {
  return new QQmlJSCompilePass::State(
      self->nextStateFromAnnotations(
          *oldState,
          *annotations));
}

//  QQmlJS::SourceLocation QQmlJSCompilePass::sourceLocation(int
//      instructionOffset) const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK17QQmlJSCompilePass14sourceLocationEi(
    const QQmlJSCompilePass *self,
    int instructionOffset) {
  return new QQmlJS::SourceLocation(self->sourceLocation(instructionOffset));
}

//  QQmlJS::SourceLocation QQmlJSCompilePass::nonEmptySourceLocation(int
//      instructionOffset) const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK17QQmlJSCompilePass22nonEmptySourceLocationEi(
    const QQmlJSCompilePass *self,
    int instructionOffset) {
  return new QQmlJS::SourceLocation(
      self->nonEmptySourceLocation(
          instructionOffset));
}

//  QQmlJS::SourceLocation QQmlJSCompilePass::currentSourceLocation() const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK17QQmlJSCompilePass21currentSourceLocationEv(
    const QQmlJSCompilePass *self) {
  return new QQmlJS::SourceLocation(self->currentSourceLocation());
}

//  QQmlJS::SourceLocation QQmlJSCompilePass::currentNonEmptySourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK17QQmlJSCompilePass29currentNonEmptySourceLocationEv(
    const QQmlJSCompilePass *self) {
  return new QQmlJS::SourceLocation(self->currentNonEmptySourceLocation());
}

//  QQmlJS::SourceLocation QQmlJSCompilePass::currentFunctionSourceLocation()
//      const
extern "C" Q_DECL_EXPORT
QQmlJS::SourceLocation *ritual_ZNK17QQmlJSCompilePass29currentFunctionSourceLocationEv(
    const QQmlJSCompilePass *self) {
  return new QQmlJS::SourceLocation(self->currentFunctionSourceLocation());
}

//  void QQmlJSCompilePass::addError(const QString &message, int
//      instructionOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass8addErrorERK7QStringi(
    QQmlJSCompilePass *self,
    const QString *message,
    int instructionOffset) {
  self->addError(*message, instructionOffset);
}

//  void QQmlJSCompilePass::addSkip(const QString &message, int
//      instructionOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass7addSkipERK7QStringi(
    QQmlJSCompilePass *self,
    const QString *message,
    int instructionOffset) {
  self->addSkip(*message, instructionOffset);
}

//  void QQmlJSCompilePass::addError(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass8addErrorERK7QString(
    QQmlJSCompilePass *self,
    const QString *message) {
  self->addError(*message);
}

//  void QQmlJSCompilePass::addSkip(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass7addSkipERK7QString(
    QQmlJSCompilePass *self,
    const QString *message) {
  self->addSkip(*message);
}

//  bool
//      QQmlJSCompilePass::instructionManipulatesContext(QV4::Moth::Instr::Ty
//      pe type)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQmlJSCompilePass29instructionManipulatesContextEN3QV44Moth5Instr4TypeE(
    QV4::Moth::Instr::Type type) {
  return QQmlJSCompilePass::instructionManipulatesContext(type);
}

//  void QQmlJSCompilePass::generate_Add(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_AddEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Add(a0);
}

//  void QQmlJSCompilePass::generate_As(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass11generate_AsEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_As(a0);
}

//  void QQmlJSCompilePass::generate_BitAnd(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15generate_BitAndEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitAnd(a0);
}

//  void QQmlJSCompilePass::generate_BitAndConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_BitAndConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitAndConst(a0);
}

//  void QQmlJSCompilePass::generate_BitOr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_BitOrEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitOr(a0);
}

//  void QQmlJSCompilePass::generate_BitOrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_BitOrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitOrConst(a0);
}

//  void QQmlJSCompilePass::generate_BitXor(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15generate_BitXorEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitXor(a0);
}

//  void QQmlJSCompilePass::generate_BitXorConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_BitXorConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_BitXorConst(a0);
}

//  void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_CallGlobalLookupEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_CallGlobalLookup(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_CallNameEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_CallName(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass31generate_CallPossiblyDirectEvalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_CallPossiblyDirectEval(a0, a1);
}

//  void QQmlJSCompilePass::generate_CallProperty(int a0, int a1, int a2, int
//      a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_CallPropertyEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  self->generate_CallProperty(a0, a1, a2, a3);
}

//  void QQmlJSCompilePass::generate_CallPropertyLookup(int a0, int a1, int
//      a2, int a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass27generate_CallPropertyLookupEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  self->generate_CallPropertyLookup(a0, a1, a2, a3);
}

//  void QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(int a0, int
//      a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_CallQmlContextPropertyLookup(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_CallValueEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_CallValue(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int a1, int a2,
//      int a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_CallWithReceiverEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  self->generate_CallWithReceiver(a0, a1, a2, a3);
}

//  void QQmlJSCompilePass::generate_CallWithSpread(int a0, int a1, int a2,
//      int a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_CallWithSpreadEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  self->generate_CallWithSpread(a0, a1, a2, a3);
}

//  void QQmlJSCompilePass::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_CheckExceptionEv(
    QQmlJSCompilePass *self) {
  self->generate_CheckException();
}

//  void QQmlJSCompilePass::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_CloneBlockContextEv(
    QQmlJSCompilePass *self) {
  self->generate_CloneBlockContext();
}

//  void QQmlJSCompilePass::generate_CmpEq(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpEqEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpEq(a0);
}

//  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_CmpEqIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpEqInt(a0);
}

//  void QQmlJSCompilePass::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_CmpEqNullEv(
    QQmlJSCompilePass *self) {
  self->generate_CmpEqNull();
}

//  void QQmlJSCompilePass::generate_CmpGe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpGeEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpGe(a0);
}

//  void QQmlJSCompilePass::generate_CmpGt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpGtEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpGt(a0);
}

//  void QQmlJSCompilePass::generate_CmpIn(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpInEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpIn(a0);
}

//  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass22generate_CmpInstanceOfEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpInstanceOf(a0);
}

//  void QQmlJSCompilePass::generate_CmpLe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpLeEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpLe(a0);
}

//  void QQmlJSCompilePass::generate_CmpLt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpLtEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpLt(a0);
}

//  void QQmlJSCompilePass::generate_CmpNe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_CmpNeEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpNe(a0);
}

//  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_CmpNeIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpNeInt(a0);
}

//  void QQmlJSCompilePass::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_CmpNeNullEv(
    QQmlJSCompilePass *self) {
  self->generate_CmpNeNull();
}

//  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_CmpStrictEqualEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpStrictEqual(a0);
}

//  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_CmpStrictNotEqualEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CmpStrictNotEqual(a0);
}

//  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_ConstructEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_Construct(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_ConstructWithSpread(int a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass28generate_ConstructWithSpreadEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_ConstructWithSpread(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass28generate_ConvertThisToObjectEv(
    QQmlJSCompilePass *self) {
  self->generate_ConvertThisToObject();
}

//  void QQmlJSCompilePass::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_CreateCallContextEv(
    QQmlJSCompilePass *self) {
  self->generate_CreateCallContext();
}

//  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_CreateClassEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_CreateClass(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass36generate_CreateMappedArgumentsObjectEv(
    QQmlJSCompilePass *self) {
  self->generate_CreateMappedArgumentsObject();
}

//  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass28generate_CreateRestParameterEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_CreateRestParameter(a0);
}

//  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSCompilePass *self) {
  self->generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass30generate_DeadTemporalZoneCheckEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_DeadTemporalZoneCheck(a0);
}

//  void QQmlJSCompilePass::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_DebugEv(
    QQmlJSCompilePass *self) {
  self->generate_Debug();
}

//  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_DeclareVarEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_DeclareVar(a0, a1);
}

//  void QQmlJSCompilePass::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_DecrementEv(
    QQmlJSCompilePass *self) {
  self->generate_Decrement();
}

//  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_DefineArrayEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_DefineArray(a0, a1);
}

//  void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass28generate_DefineObjectLiteralEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_DefineObjectLiteral(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_DeleteName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_DeleteNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_DeleteName(a0);
}

//  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_DeletePropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_DeleteProperty(a0, a1);
}

//  void QQmlJSCompilePass::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass31generate_DestructureRestElementEv(
    QQmlJSCompilePass *self) {
  self->generate_DestructureRestElement();
}

//  void QQmlJSCompilePass::generate_Div(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_DivEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Div(a0);
}

//  void QQmlJSCompilePass::generate_Exp(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_ExpEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Exp(a0);
}

//  void QQmlJSCompilePass::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_GetExceptionEv(
    QQmlJSCompilePass *self) {
  self->generate_GetException();
}

//  void QQmlJSCompilePass::generate_GetIterator(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_GetIteratorEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_GetIterator(a0);
}

//  void QQmlJSCompilePass::generate_GetLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_GetLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_GetLookup(a0);
}

//  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_GetOptionalLookupEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_GetOptionalLookup(a0, a1);
}

//  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_GetTemplateObjectEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_GetTemplateObject(a0);
}

//  void QQmlJSCompilePass::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_IncrementEv(
    QQmlJSCompilePass *self) {
  self->generate_Increment();
}

//  void QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int a0,
//      int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_InitializeBlockDeadTemporalZone(a0, a1);
}

//  void QQmlJSCompilePass::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass22generate_IteratorCloseEv(
    QQmlJSCompilePass *self) {
  self->generate_IteratorClose();
}

//  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_IteratorNextEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_IteratorNext(a0, a1);
}

//  void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass33generate_IteratorNextForYieldStarEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  self->generate_IteratorNextForYieldStar(a0, a1, a2);
}

//  void QQmlJSCompilePass::generate_Jump(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass13generate_JumpEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Jump(a0);
}

//  void QQmlJSCompilePass::generate_JumpFalse(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_JumpFalseEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_JumpFalse(a0);
}

//  void QQmlJSCompilePass::generate_JumpNoException(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass24generate_JumpNoExceptionEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_JumpNoException(a0);
}

//  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_JumpNotUndefinedEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_JumpNotUndefined(a0);
}

//  void QQmlJSCompilePass::generate_JumpTrue(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_JumpTrueEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_JumpTrue(a0);
}

//  void QQmlJSCompilePass::generate_LoadClosure(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_LoadClosureEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadClosure(a0);
}

//  void QQmlJSCompilePass::generate_LoadConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_LoadConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadConst(a0);
}

//  void QQmlJSCompilePass::generate_LoadElement(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_LoadElementEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadElement(a0);
}

//  void QQmlJSCompilePass::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_LoadFalseEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadFalse();
}

//  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_LoadGlobalLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadGlobalLookup(a0);
}

//  void QQmlJSCompilePass::generate_LoadImport(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_LoadImportEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadImport(a0);
}

//  void QQmlJSCompilePass::generate_LoadInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass16generate_LoadIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadInt(a0);
}

//  void QQmlJSCompilePass::generate_LoadLocal(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_LoadLocalEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadLocal(a0);
}

//  void QQmlJSCompilePass::generate_LoadName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_LoadNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadName(a0);
}

//  void QQmlJSCompilePass::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_LoadNullEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadNull();
}

//  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass29generate_LoadOptionalPropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_LoadOptionalProperty(a0, a1);
}

//  void QQmlJSCompilePass::generate_LoadProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_LoadPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadProperty(a0);
}

//  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadQmlContextPropertyLookup(a0);
}

//  void QQmlJSCompilePass::generate_LoadReg(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass16generate_LoadRegEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadReg(a0);
}

//  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_LoadRuntimeStringEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadRuntimeString(a0);
}

//  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass24generate_LoadScopedLocalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_LoadScopedLocal(a0, a1);
}

//  void QQmlJSCompilePass::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass29generate_LoadSuperConstructorEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadSuperConstructor();
}

//  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_LoadSuperPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_LoadSuperProperty(a0);
}

//  void QQmlJSCompilePass::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_LoadTrueEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadTrue();
}

//  void QQmlJSCompilePass::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass22generate_LoadUndefinedEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadUndefined();
}

//  void QQmlJSCompilePass::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_LoadZeroEv(
    QQmlJSCompilePass *self) {
  self->generate_LoadZero();
}

//  void QQmlJSCompilePass::generate_Mod(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_ModEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Mod(a0);
}

//  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_MoveConstEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_MoveConst(a0, a1);
}

//  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass16generate_MoveRegEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_MoveReg(a0, a1);
}

//  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_MoveRegExpEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_MoveRegExp(a0, a1);
}

//  void QQmlJSCompilePass::generate_Mul(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_MulEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Mul(a0);
}

//  void QQmlJSCompilePass::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_PopContextEv(
    QQmlJSCompilePass *self) {
  self->generate_PopContext();
}

//  void QQmlJSCompilePass::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_PopScriptContextEv(
    QQmlJSCompilePass *self) {
  self->generate_PopScriptContext();
}

//  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_PushBlockContextEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_PushBlockContext(a0);
}

//  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_PushCatchContextEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_PushCatchContext(a0, a1);
}

//  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass26generate_PushScriptContextEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_PushScriptContext(a0);
}

//  void QQmlJSCompilePass::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass24generate_PushWithContextEv(
    QQmlJSCompilePass *self) {
  self->generate_PushWithContext();
}

//  void QQmlJSCompilePass::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15generate_ResumeEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Resume(a0);
}

//  void QQmlJSCompilePass::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_RetEv(QQmlJSCompilePass *self) {
  self->generate_Ret();
}

//  void QQmlJSCompilePass::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_SetExceptionEv(
    QQmlJSCompilePass *self) {
  self->generate_SetException();
}

//  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_SetLookupEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_SetLookup(a0, a1);
}

//  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_SetUnwindHandlerEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_SetUnwindHandler(a0);
}

//  void QQmlJSCompilePass::generate_Shl(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_ShlEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Shl(a0);
}

//  void QQmlJSCompilePass::generate_ShlConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_ShlConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_ShlConst(a0);
}

//  void QQmlJSCompilePass::generate_Shr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_ShrEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Shr(a0);
}

//  void QQmlJSCompilePass::generate_ShrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_ShrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_ShrConst(a0);
}

//  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass21generate_StoreElementEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_StoreElement(a0, a1);
}

//  void QQmlJSCompilePass::generate_StoreLocal(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_StoreLocalEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_StoreLocal(a0);
}

//  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass24generate_StoreNameSloppyEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_StoreNameSloppy(a0);
}

//  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass24generate_StoreNameStrictEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_StoreNameStrict(a0);
}

//  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass22generate_StorePropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_StoreProperty(a0, a1);
}

//  void QQmlJSCompilePass::generate_StoreReg(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_StoreRegEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_StoreReg(a0);
}

//  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass25generate_StoreScopedLocalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_StoreScopedLocal(a0, a1);
}

//  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass27generate_StoreSuperPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_StoreSuperProperty(a0);
}

//  void QQmlJSCompilePass::generate_Sub(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass12generate_SubEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_Sub(a0);
}

//  void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int a2, int a3)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_TailCallEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  self->generate_TailCall(a0, a1, a2, a3);
}

//  void QQmlJSCompilePass::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_ThrowExceptionEv(
    QQmlJSCompilePass *self) {
  self->generate_ThrowException();
}

//  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSCompilePass *self) {
  self->generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSCompilePass::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass17generate_ToObjectEv(
    QQmlJSCompilePass *self) {
  self->generate_ToObject();
}

//  void QQmlJSCompilePass::generate_TypeofName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass19generate_TypeofNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_TypeofName(a0);
}

//  void QQmlJSCompilePass::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass20generate_TypeofValueEv(
    QQmlJSCompilePass *self) {
  self->generate_TypeofValue();
}

//  void QQmlJSCompilePass::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15generate_UComplEv(
    QQmlJSCompilePass *self) {
  self->generate_UCompl();
}

//  void QQmlJSCompilePass::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass15generate_UMinusEv(
    QQmlJSCompilePass *self) {
  self->generate_UMinus();
}

//  void QQmlJSCompilePass::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass13generate_UNotEv(QQmlJSCompilePass *self) {
  self->generate_UNot();
}

//  void QQmlJSCompilePass::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_UPlusEv(
    QQmlJSCompilePass *self) {
  self->generate_UPlus();
}

//  void QQmlJSCompilePass::generate_UShr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass13generate_UShrEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_UShr(a0);
}

//  void QQmlJSCompilePass::generate_UShrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_UShrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  self->generate_UShrConst(a0);
}

//  void QQmlJSCompilePass::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass23generate_UnwindDispatchEv(
    QQmlJSCompilePass *self) {
  self->generate_UnwindDispatch();
}

//  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass22generate_UnwindToLabelEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  self->generate_UnwindToLabel(a0, a1);
}

//  void QQmlJSCompilePass::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass14generate_YieldEv(
    QQmlJSCompilePass *self) {
  self->generate_Yield();
}

//  void QQmlJSCompilePass::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQmlJSCompilePass18generate_YieldStarEv(
    QQmlJSCompilePass *self) {
  self->generate_YieldStar();
}

//  a Python function taken by a CuteQQmlJSCompilePass, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSCompilePass(
    QQmlJSCompilePass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSCompilePass *>(self)->take(key, call);
}

//  void QQmlJSCompilePass::generate_Add(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_AddEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Add(
      a0);
}

//  void QQmlJSCompilePass::generate_As(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass11generate_AsEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_As(
      a0);
}

//  void QQmlJSCompilePass::generate_BitAnd(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass15generate_BitAndEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitAnd(
      a0);
}

//  void QQmlJSCompilePass::generate_BitAndConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_BitAndConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitAndConst(
      a0);
}

//  void QQmlJSCompilePass::generate_BitOr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_BitOrEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitOr(
      a0);
}

//  void QQmlJSCompilePass::generate_BitOrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_BitOrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitOrConst(
      a0);
}

//  void QQmlJSCompilePass::generate_BitXor(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass15generate_BitXorEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitXor(
      a0);
}

//  void QQmlJSCompilePass::generate_BitXorConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_BitXorConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_BitXorConst(
      a0);
}

//  void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_CallGlobalLookupEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallGlobalLookup(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_CallNameEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallName(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass31generate_CallPossiblyDirectEvalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallPossiblyDirectEval(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_CallProperty(int a0, int a1, int a2, int
//      a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_CallPropertyEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallProperty(
      a0,
      a1,
      a2,
      a3);
}

//  void QQmlJSCompilePass::generate_CallPropertyLookup(int a0, int a1, int
//      a2, int a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass27generate_CallPropertyLookupEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallPropertyLookup(
      a0,
      a1,
      a2,
      a3);
}

//  void QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(int a0, int
//      a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallQmlContextPropertyLookup(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_CallValueEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallValue(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int a1, int a2,
//      int a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_CallWithReceiverEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallWithReceiver(
      a0,
      a1,
      a2,
      a3);
}

//  void QQmlJSCompilePass::generate_CallWithSpread(int a0, int a1, int a2,
//      int a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_CallWithSpreadEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CallWithSpread(
      a0,
      a1,
      a2,
      a3);
}

//  void QQmlJSCompilePass::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_CheckExceptionEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CheckException();
}

//  void QQmlJSCompilePass::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_CloneBlockContextEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CloneBlockContext();
}

//  void QQmlJSCompilePass::generate_CmpEq(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpEqEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpEq(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_CmpEqIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpEqInt(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_CmpEqNullEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpEqNull();
}

//  void QQmlJSCompilePass::generate_CmpGe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpGeEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpGe(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpGt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpGtEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpGt(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpIn(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpInEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpIn(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass22generate_CmpInstanceOfEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpInstanceOf(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpLe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpLeEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpLe(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpLt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpLtEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpLt(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpNe(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_CmpNeEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpNe(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_CmpNeIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpNeInt(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_CmpNeNullEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpNeNull();
}

//  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_CmpStrictEqualEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpStrictEqual(
      a0);
}

//  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_CmpStrictNotEqualEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CmpStrictNotEqual(
      a0);
}

//  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_ConstructEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Construct(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_ConstructWithSpread(int a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass28generate_ConstructWithSpreadEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ConstructWithSpread(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass28generate_ConvertThisToObjectEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ConvertThisToObject();
}

//  void QQmlJSCompilePass::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_CreateCallContextEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CreateCallContext();
}

//  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_CreateClassEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CreateClass(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass36generate_CreateMappedArgumentsObjectEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CreateMappedArgumentsObject();
}

//  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass28generate_CreateRestParameterEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CreateRestParameter(
      a0);
}

//  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass30generate_DeadTemporalZoneCheckEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DeadTemporalZoneCheck(
      a0);
}

//  void QQmlJSCompilePass::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_DebugEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Debug();
}

//  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_DeclareVarEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DeclareVar(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_DecrementEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Decrement();
}

//  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_DefineArrayEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DefineArray(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass28generate_DefineObjectLiteralEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DefineObjectLiteral(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_DeleteName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_DeleteNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DeleteName(
      a0);
}

//  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_DeletePropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DeleteProperty(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass31generate_DestructureRestElementEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_DestructureRestElement();
}

//  void QQmlJSCompilePass::generate_Div(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_DivEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Div(
      a0);
}

//  void QQmlJSCompilePass::generate_Exp(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_ExpEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Exp(
      a0);
}

//  void QQmlJSCompilePass::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_GetExceptionEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_GetException();
}

//  void QQmlJSCompilePass::generate_GetIterator(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_GetIteratorEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_GetIterator(
      a0);
}

//  void QQmlJSCompilePass::generate_GetLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_GetLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_GetLookup(
      a0);
}

//  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_GetOptionalLookupEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_GetOptionalLookup(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_GetTemplateObjectEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_GetTemplateObject(
      a0);
}

//  void QQmlJSCompilePass::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_IncrementEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Increment();
}

//  void QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int a0,
//      int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass22generate_IteratorCloseEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_IteratorClose();
}

//  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_IteratorNextEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_IteratorNext(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass33generate_IteratorNextForYieldStarEiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_IteratorNextForYieldStar(
      a0,
      a1,
      a2);
}

//  void QQmlJSCompilePass::generate_Jump(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass13generate_JumpEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Jump(
      a0);
}

//  void QQmlJSCompilePass::generate_JumpFalse(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_JumpFalseEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_JumpFalse(
      a0);
}

//  void QQmlJSCompilePass::generate_JumpNoException(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass24generate_JumpNoExceptionEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_JumpNoException(
      a0);
}

//  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_JumpNotUndefinedEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_JumpNotUndefined(
      a0);
}

//  void QQmlJSCompilePass::generate_JumpTrue(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_JumpTrueEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_JumpTrue(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadClosure(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_LoadClosureEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadClosure(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_LoadConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadConst(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadElement(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_LoadElementEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadElement(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_LoadFalseEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadFalse();
}

//  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_LoadGlobalLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadGlobalLookup(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadImport(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_LoadImportEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadImport(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadInt(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass16generate_LoadIntEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadInt(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadLocal(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_LoadLocalEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadLocal(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_LoadNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadName(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_LoadNullEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadNull();
}

//  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass29generate_LoadOptionalPropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadOptionalProperty(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_LoadProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_LoadPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadProperty(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadReg(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass16generate_LoadRegEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadReg(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_LoadRuntimeStringEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadRuntimeString(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass24generate_LoadScopedLocalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadScopedLocal(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass29generate_LoadSuperConstructorEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadSuperConstructor();
}

//  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_LoadSuperPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadSuperProperty(
      a0);
}

//  void QQmlJSCompilePass::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_LoadTrueEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadTrue();
}

//  void QQmlJSCompilePass::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass22generate_LoadUndefinedEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadUndefined();
}

//  void QQmlJSCompilePass::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_LoadZeroEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_LoadZero();
}

//  void QQmlJSCompilePass::generate_Mod(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_ModEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Mod(
      a0);
}

//  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_MoveConstEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_MoveConst(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass16generate_MoveRegEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_MoveReg(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_MoveRegExpEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_MoveRegExp(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_Mul(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_MulEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Mul(
      a0);
}

//  void QQmlJSCompilePass::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_PopContextEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PopContext();
}

//  void QQmlJSCompilePass::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_PopScriptContextEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PopScriptContext();
}

//  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_PushBlockContextEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PushBlockContext(
      a0);
}

//  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_PushCatchContextEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PushCatchContext(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass26generate_PushScriptContextEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PushScriptContext(
      a0);
}

//  void QQmlJSCompilePass::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass24generate_PushWithContextEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_PushWithContext();
}

//  void QQmlJSCompilePass::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass15generate_ResumeEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Resume(
      a0);
}

//  void QQmlJSCompilePass::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_RetEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Ret();
}

//  void QQmlJSCompilePass::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_SetExceptionEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_SetException();
}

//  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_SetLookupEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_SetLookup(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_SetUnwindHandlerEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_SetUnwindHandler(
      a0);
}

//  void QQmlJSCompilePass::generate_Shl(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_ShlEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Shl(
      a0);
}

//  void QQmlJSCompilePass::generate_ShlConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_ShlConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ShlConst(
      a0);
}

//  void QQmlJSCompilePass::generate_Shr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_ShrEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Shr(
      a0);
}

//  void QQmlJSCompilePass::generate_ShrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_ShrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ShrConst(
      a0);
}

//  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass21generate_StoreElementEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreElement(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_StoreLocal(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_StoreLocalEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreLocal(
      a0);
}

//  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass24generate_StoreNameSloppyEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreNameSloppy(
      a0);
}

//  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass24generate_StoreNameStrictEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreNameStrict(
      a0);
}

//  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass22generate_StorePropertyEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreProperty(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_StoreReg(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_StoreRegEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreReg(
      a0);
}

//  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass25generate_StoreScopedLocalEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreScopedLocal(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass27generate_StoreSuperPropertyEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_StoreSuperProperty(
      a0);
}

//  void QQmlJSCompilePass::generate_Sub(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass12generate_SubEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Sub(
      a0);
}

//  void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int a2, int a3)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_TailCallEiiii(
    QQmlJSCompilePass *self,
    int a0,
    int a1,
    int a2,
    int a3) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_TailCall(
      a0,
      a1,
      a2,
      a3);
}

//  void QQmlJSCompilePass::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_ThrowExceptionEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ThrowException();
}

//  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSCompilePass::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass17generate_ToObjectEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_ToObject();
}

//  void QQmlJSCompilePass::generate_TypeofName(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass19generate_TypeofNameEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_TypeofName(
      a0);
}

//  void QQmlJSCompilePass::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass20generate_TypeofValueEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_TypeofValue();
}

//  void QQmlJSCompilePass::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass15generate_UComplEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UCompl();
}

//  void QQmlJSCompilePass::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass15generate_UMinusEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UMinus();
}

//  void QQmlJSCompilePass::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass13generate_UNotEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UNot();
}

//  void QQmlJSCompilePass::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_UPlusEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UPlus();
}

//  void QQmlJSCompilePass::generate_UShr(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass13generate_UShrEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UShr(
      a0);
}

//  void QQmlJSCompilePass::generate_UShrConst(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_UShrConstEi(
    QQmlJSCompilePass *self,
    int a0) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UShrConst(
      a0);
}

//  void QQmlJSCompilePass::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass23generate_UnwindDispatchEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UnwindDispatch();
}

//  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass22generate_UnwindToLabelEii(
    QQmlJSCompilePass *self,
    int a0,
    int a1) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_UnwindToLabel(
      a0,
      a1);
}

//  void QQmlJSCompilePass::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass14generate_YieldEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_Yield();
}

//  void QQmlJSCompilePass::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQmlJSCompilePass18generate_YieldStarEv(
    QQmlJSCompilePass *self) {
  static_cast<OwnQQmlJSCompilePass *>(self)->OwnQQmlJSCompilePass::generate_YieldStar();
}
