//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscodegenerator_p.h, Qt
//  6.12.0. Edited by hand on 2026-11-25: added by hand, instances of
//  templates of the class: 3. Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscodegenerator_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlJSCodeGenerator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSCodeGenerator : QQmlJSCodeGenerator {
  using QQmlJSCodeGenerator::generate_Ret;
  using QQmlJSCodeGenerator::generate_Debug;
  using QQmlJSCodeGenerator::generate_LoadConst;
  using QQmlJSCodeGenerator::generate_LoadZero;
  using QQmlJSCodeGenerator::generate_LoadTrue;
  using QQmlJSCodeGenerator::generate_LoadFalse;
  using QQmlJSCodeGenerator::generate_LoadNull;
  using QQmlJSCodeGenerator::generate_LoadUndefined;
  using QQmlJSCodeGenerator::generate_LoadInt;
  using QQmlJSCodeGenerator::generate_MoveConst;
  using QQmlJSCodeGenerator::generate_LoadReg;
  using QQmlJSCodeGenerator::generate_StoreReg;
  using QQmlJSCodeGenerator::generate_MoveReg;
  using QQmlJSCodeGenerator::generate_LoadImport;
  using QQmlJSCodeGenerator::generate_LoadLocal;
  using QQmlJSCodeGenerator::generate_StoreLocal;
  using QQmlJSCodeGenerator::generate_LoadScopedLocal;
  using QQmlJSCodeGenerator::generate_StoreScopedLocal;
  using QQmlJSCodeGenerator::generate_LoadRuntimeString;
  using QQmlJSCodeGenerator::generate_MoveRegExp;
  using QQmlJSCodeGenerator::generate_LoadClosure;
  using QQmlJSCodeGenerator::generate_LoadName;
  using QQmlJSCodeGenerator::generate_LoadGlobalLookup;
  using QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup;
  using QQmlJSCodeGenerator::generate_StoreNameSloppy;
  using QQmlJSCodeGenerator::generate_StoreNameStrict;
  using QQmlJSCodeGenerator::generate_LoadElement;
  using QQmlJSCodeGenerator::generate_StoreElement;
  using QQmlJSCodeGenerator::generate_LoadProperty;
  using QQmlJSCodeGenerator::generate_LoadOptionalProperty;
  using QQmlJSCodeGenerator::generate_GetLookup;
  using QQmlJSCodeGenerator::generate_GetOptionalLookup;
  using QQmlJSCodeGenerator::generate_StoreProperty;
  using QQmlJSCodeGenerator::generate_SetLookup;
  using QQmlJSCodeGenerator::generate_LoadSuperProperty;
  using QQmlJSCodeGenerator::generate_StoreSuperProperty;
  using QQmlJSCodeGenerator::generate_Yield;
  using QQmlJSCodeGenerator::generate_YieldStar;
  using QQmlJSCodeGenerator::generate_Resume;
  using QQmlJSCodeGenerator::generate_CallValue;
  using QQmlJSCodeGenerator::generate_CallWithReceiver;
  using QQmlJSCodeGenerator::generate_CallProperty;
  using QQmlJSCodeGenerator::generate_CallPropertyLookup;
  using QQmlJSCodeGenerator::generate_CallName;
  using QQmlJSCodeGenerator::generate_CallPossiblyDirectEval;
  using QQmlJSCodeGenerator::generate_CallGlobalLookup;
  using QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup;
  using QQmlJSCodeGenerator::generate_CallWithSpread;
  using QQmlJSCodeGenerator::generate_TailCall;
  using QQmlJSCodeGenerator::generate_Construct;
  using QQmlJSCodeGenerator::generate_ConstructWithSpread;
  using QQmlJSCodeGenerator::generate_SetUnwindHandler;
  using QQmlJSCodeGenerator::generate_UnwindDispatch;
  using QQmlJSCodeGenerator::generate_UnwindToLabel;
  using QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck;
  using QQmlJSCodeGenerator::generate_ThrowException;
  using QQmlJSCodeGenerator::generate_GetException;
  using QQmlJSCodeGenerator::generate_SetException;
  using QQmlJSCodeGenerator::generate_CreateCallContext;
  using QQmlJSCodeGenerator::generate_PushCatchContext;
  using QQmlJSCodeGenerator::generate_PushWithContext;
  using QQmlJSCodeGenerator::generate_PushBlockContext;
  using QQmlJSCodeGenerator::generate_CloneBlockContext;
  using QQmlJSCodeGenerator::generate_PushScriptContext;
  using QQmlJSCodeGenerator::generate_PopScriptContext;
  using QQmlJSCodeGenerator::generate_PopContext;
  using QQmlJSCodeGenerator::generate_GetIterator;
  using QQmlJSCodeGenerator::generate_IteratorNext;
  using QQmlJSCodeGenerator::generate_IteratorNextForYieldStar;
  using QQmlJSCodeGenerator::generate_IteratorClose;
  using QQmlJSCodeGenerator::generate_DestructureRestElement;
  using QQmlJSCodeGenerator::generate_DeleteProperty;
  using QQmlJSCodeGenerator::generate_DeleteName;
  using QQmlJSCodeGenerator::generate_TypeofName;
  using QQmlJSCodeGenerator::generate_TypeofValue;
  using QQmlJSCodeGenerator::generate_DeclareVar;
  using QQmlJSCodeGenerator::generate_DefineArray;
  using QQmlJSCodeGenerator::generate_DefineObjectLiteral;
  using QQmlJSCodeGenerator::generate_CreateClass;
  using QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject;
  using QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject;
  using QQmlJSCodeGenerator::generate_CreateRestParameter;
  using QQmlJSCodeGenerator::generate_ConvertThisToObject;
  using QQmlJSCodeGenerator::generate_LoadSuperConstructor;
  using QQmlJSCodeGenerator::generate_ToObject;
  using QQmlJSCodeGenerator::generate_Jump;
  using QQmlJSCodeGenerator::generate_JumpTrue;
  using QQmlJSCodeGenerator::generate_JumpFalse;
  using QQmlJSCodeGenerator::generate_JumpNoException;
  using QQmlJSCodeGenerator::generate_JumpNotUndefined;
  using QQmlJSCodeGenerator::generate_CheckException;
  using QQmlJSCodeGenerator::generate_CmpEqNull;
  using QQmlJSCodeGenerator::generate_CmpNeNull;
  using QQmlJSCodeGenerator::generate_CmpEqInt;
  using QQmlJSCodeGenerator::generate_CmpNeInt;
  using QQmlJSCodeGenerator::generate_CmpEq;
  using QQmlJSCodeGenerator::generate_CmpNe;
  using QQmlJSCodeGenerator::generate_CmpGt;
  using QQmlJSCodeGenerator::generate_CmpGe;
  using QQmlJSCodeGenerator::generate_CmpLt;
  using QQmlJSCodeGenerator::generate_CmpLe;
  using QQmlJSCodeGenerator::generate_CmpStrictEqual;
  using QQmlJSCodeGenerator::generate_CmpStrictNotEqual;
  using QQmlJSCodeGenerator::generate_CmpIn;
  using QQmlJSCodeGenerator::generate_CmpInstanceOf;
  using QQmlJSCodeGenerator::generate_As;
  using QQmlJSCodeGenerator::generate_UNot;
  using QQmlJSCodeGenerator::generate_UPlus;
  using QQmlJSCodeGenerator::generate_UMinus;
  using QQmlJSCodeGenerator::generate_UCompl;
  using QQmlJSCodeGenerator::generate_Increment;
  using QQmlJSCodeGenerator::generate_Decrement;
  using QQmlJSCodeGenerator::generate_Add;
  using QQmlJSCodeGenerator::generate_BitAnd;
  using QQmlJSCodeGenerator::generate_BitOr;
  using QQmlJSCodeGenerator::generate_BitXor;
  using QQmlJSCodeGenerator::generate_UShr;
  using QQmlJSCodeGenerator::generate_Shr;
  using QQmlJSCodeGenerator::generate_Shl;
  using QQmlJSCodeGenerator::generate_BitAndConst;
  using QQmlJSCodeGenerator::generate_BitOrConst;
  using QQmlJSCodeGenerator::generate_BitXorConst;
  using QQmlJSCodeGenerator::generate_UShrConst;
  using QQmlJSCodeGenerator::generate_ShrConst;
  using QQmlJSCodeGenerator::generate_ShlConst;
  using QQmlJSCodeGenerator::generate_Exp;
  using QQmlJSCodeGenerator::generate_Mul;
  using QQmlJSCodeGenerator::generate_Div;
  using QQmlJSCodeGenerator::generate_Mod;
  using QQmlJSCodeGenerator::generate_Sub;
  using QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone;
  using QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined;
  using QQmlJSCodeGenerator::generate_GetTemplateObject;
  using QQmlJSCodeGenerator::endInstruction;
};

//  A QQmlJSCodeGenerator that Python can take functions over in. Every QQmlJSCodeGenerator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSCodeGeneratorCall0)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall1)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall2)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall3)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall4)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall5)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall6)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall7)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall8)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall9)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall10)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall11)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall12)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall13)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall14)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall15)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall16)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall17)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall18)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall19)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall20)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall21)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall22)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall23)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall24)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall25)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall26)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall27)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall28)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall29)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall30)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall31)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall32)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall33)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall34)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall35)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall36)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall37)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall38)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall39)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall40)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall41)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall42)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall43)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall44)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall45)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall46)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall47)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall48)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall49)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall50)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall51)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall52)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall53)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall54)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall55)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall56)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall57)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall58)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall59)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall60)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall61)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall62)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall63)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall64)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall65)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall66)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall67)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall68)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall69)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall70)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall71)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall72)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall73)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall74)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall75)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall76)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall77)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall78)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall79)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall80)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall81)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall82)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall83)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall84)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall85)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall86)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall87)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall88)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall89)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall90)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall91)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall92)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall93)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall94)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall95)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall96)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall97)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall98)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall99)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall100)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall101)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall102)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall103)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall104)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall105)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall106)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall107)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall108)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall109)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall110)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall111)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall112)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall113)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall114)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall115)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall116)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall117)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall118)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall119)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall120)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall121)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall122)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall123)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall124)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall125)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall126)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall127)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall128)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall129)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall130)(const void *, int, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall131)(const void *, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall132)(const void *, int, int *);
typedef void (*CuteQQmlJSCodeGeneratorCall133)(const void *, int, int *);
class CuteQQmlJSCodeGenerator : public QQmlJSCodeGenerator {
public:
  using QQmlJSCodeGenerator::QQmlJSCodeGenerator;
  void *taken[134] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_RetEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_DebugEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadConstEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadZeroEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadTrueEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadFalseEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNullEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_LoadUndefinedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadIntEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_MoveConstEii")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadRegEi")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_StoreRegEi")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_MoveRegEii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_LoadImportEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadLocalEi")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_StoreLocalEi")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_LoadScopedLocalEii")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_StoreScopedLocalEii")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadRuntimeStringEi")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_MoveRegExpEii")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadClosureEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNameEi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_LoadGlobalLookupEi")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_LoadQmlContextPropertyLookupEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameSloppyEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameStrictEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadElementEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_StoreElementEii")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_LoadPropertyEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadOptionalPropertyEii")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_GetLookupEi")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetOptionalLookupEii")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_StorePropertyEii")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_SetLookupEii")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadSuperPropertyEi")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_StoreSuperPropertyEi")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_YieldEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_YieldStarEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_ResumeEi")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CallValueEiii")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallWithReceiverEiiii")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_CallPropertyEiiii")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_CallPropertyLookupEiiii")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CallNameEiii")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_CallPossiblyDirectEvalEii")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallGlobalLookupEiii")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_CallQmlContextPropertyLookupEiii")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CallWithSpreadEiiii")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_TailCallEiiii")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_ConstructEiii")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConstructWithSpreadEiii")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_SetUnwindHandlerEi")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_UnwindDispatchEv")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_UnwindToLabelEii")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler30generate_DeadTemporalZoneCheckEi")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_ThrowExceptionEv")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_GetExceptionEv")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_SetExceptionEv")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CreateCallContextEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushCatchContextEii")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_PushWithContextEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushBlockContextEi")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CloneBlockContextEv")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_PushScriptContextEi")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PopScriptContextEv")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_PopContextEv")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_GetIteratorEi")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_IteratorNextEii")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler33generate_IteratorNextForYieldStarEiii")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_IteratorCloseEv")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_DestructureRestElementEv")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_DeletePropertyEii")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeleteNameEi")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_TypeofNameEi")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_TypeofValueEv")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeclareVarEii")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_DefineArrayEii")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_DefineObjectLiteralEiii")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_CreateClassEiii")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler36generate_CreateMappedArgumentsObjectEv")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler38generate_CreateUnmappedArgumentsObjectEv")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_CreateRestParameterEi")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConvertThisToObjectEv")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadSuperConstructorEv")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ToObjectEv")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_JumpEi")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_JumpTrueEi")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_JumpFalseEi")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_JumpNoExceptionEi")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_JumpNotUndefinedEi")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CheckExceptionEv")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpEqNullEv")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpNeNullEv")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpEqIntEi")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpNeIntEi")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpEqEi")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpNeEi")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGtEi")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGeEi")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLtEi")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLeEi")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CmpStrictEqualEi")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CmpStrictNotEqualEi")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpInEi")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_CmpInstanceOfEi")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler11generate_AsEi")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UNotEv")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_UPlusEv")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UMinusEv")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UComplEv")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_IncrementEv")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_DecrementEv")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_AddEi")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitAndEi")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_BitOrEi")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitXorEi")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UShrEi")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShrEi")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShlEi")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitAndConstEi")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_BitOrConstEi")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitXorConstEi")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_UShrConstEi")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShrConstEi")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShlConstEi")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ExpEi")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_MulEi")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_DivEi")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ModEi")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_SubEi")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler40generate_InitializeBlockDeadTemporalZoneEii")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_ThrowOnNullOrUndefinedEv")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetTemplateObjectEi")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14endInstructionENS0_5Instr4TypeE")) {
      taken[133] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJSCodeGenerator::generate_Ret()
  void generate_Ret() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall0 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Ret();
  }

  //  void QQmlJSCodeGenerator::generate_Debug()
  void generate_Debug() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall1 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Debug();
  }

  //  void QQmlJSCodeGenerator::generate_LoadConst(int index)
  void generate_LoadConst(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall2 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall2>(taken[2]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadConst(index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadZero()
  void generate_LoadZero() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall3 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadZero();
  }

  //  void QQmlJSCodeGenerator::generate_LoadTrue()
  void generate_LoadTrue() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall4 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadTrue();
  }

  //  void QQmlJSCodeGenerator::generate_LoadFalse()
  void generate_LoadFalse() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall5 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadFalse();
  }

  //  void QQmlJSCodeGenerator::generate_LoadNull()
  void generate_LoadNull() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall6 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadNull();
  }

  //  void QQmlJSCodeGenerator::generate_LoadUndefined()
  void generate_LoadUndefined() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall7 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadUndefined();
  }

  //  void QQmlJSCodeGenerator::generate_LoadInt(int value)
  void generate_LoadInt(int value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall8 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall8>(taken[8]);
      call(this, value, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadInt(value);
  }

  //  void QQmlJSCodeGenerator::generate_MoveConst(int constIndex, int
  //      destTemp)
  void generate_MoveConst(int constIndex, int destTemp) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall9 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall9>(taken[9]);
      call(this, constIndex, destTemp, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_MoveConst(constIndex, destTemp);
  }

  //  void QQmlJSCodeGenerator::generate_LoadReg(int reg)
  void generate_LoadReg(int reg) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall10 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall10>(taken[10]);
      call(this, reg, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadReg(reg);
  }

  //  void QQmlJSCodeGenerator::generate_StoreReg(int reg)
  void generate_StoreReg(int reg) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall11 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall11>(taken[11]);
      call(this, reg, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreReg(reg);
  }

  //  void QQmlJSCodeGenerator::generate_MoveReg(int srcReg, int destReg)
  void generate_MoveReg(int srcReg, int destReg) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall12 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall12>(taken[12]);
      call(this, srcReg, destReg, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_MoveReg(srcReg, destReg);
  }

  //  void QQmlJSCodeGenerator::generate_LoadImport(int index)
  void generate_LoadImport(int index) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall13 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall13>(taken[13]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadImport(index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadLocal(int index)
  void generate_LoadLocal(int index) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall14 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall14>(taken[14]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadLocal(index);
  }

  //  void QQmlJSCodeGenerator::generate_StoreLocal(int index)
  void generate_StoreLocal(int index) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall15 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall15>(taken[15]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreLocal(index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadScopedLocal(int scope, int
  //      index)
  void generate_LoadScopedLocal(int scope, int index) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall16 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall16>(taken[16]);
      call(this, scope, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadScopedLocal(scope, index);
  }

  //  void QQmlJSCodeGenerator::generate_StoreScopedLocal(int scope, int
  //      index)
  void generate_StoreScopedLocal(int scope, int index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall17 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall17>(taken[17]);
      call(this, scope, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreScopedLocal(scope, index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadRuntimeString(int stringId)
  void generate_LoadRuntimeString(int stringId) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall18 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall18>(taken[18]);
      call(this, stringId, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadRuntimeString(stringId);
  }

  //  void QQmlJSCodeGenerator::generate_MoveRegExp(int regExpId, int
  //      destReg)
  void generate_MoveRegExp(int regExpId, int destReg) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall19 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall19>(taken[19]);
      call(this, regExpId, destReg, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_MoveRegExp(regExpId, destReg);
  }

  //  void QQmlJSCodeGenerator::generate_LoadClosure(int value)
  void generate_LoadClosure(int value) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall20 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall20>(taken[20]);
      call(this, value, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadClosure(value);
  }

  //  void QQmlJSCodeGenerator::generate_LoadName(int nameIndex)
  void generate_LoadName(int nameIndex) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall21 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall21>(taken[21]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadName(nameIndex);
  }

  //  void QQmlJSCodeGenerator::generate_LoadGlobalLookup(int index)
  void generate_LoadGlobalLookup(int index) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall22 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall22>(taken[22]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadGlobalLookup(index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(int
  //      index)
  void generate_LoadQmlContextPropertyLookup(int index) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall23 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall23>(taken[23]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(index);
  }

  //  void QQmlJSCodeGenerator::generate_StoreNameSloppy(int nameIndex)
  void generate_StoreNameSloppy(int nameIndex) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall24 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall24>(taken[24]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreNameSloppy(nameIndex);
  }

  //  void QQmlJSCodeGenerator::generate_StoreNameStrict(int name)
  void generate_StoreNameStrict(int name) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall25 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall25>(taken[25]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreNameStrict(name);
  }

  //  void QQmlJSCodeGenerator::generate_LoadElement(int base)
  void generate_LoadElement(int base) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall26 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall26>(taken[26]);
      call(this, base, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadElement(base);
  }

  //  void QQmlJSCodeGenerator::generate_StoreElement(int base, int index)
  void generate_StoreElement(int base, int index) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall27 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall27>(taken[27]);
      call(this, base, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreElement(base, index);
  }

  //  void QQmlJSCodeGenerator::generate_LoadProperty(int nameIndex)
  void generate_LoadProperty(int nameIndex) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall28 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall28>(taken[28]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadProperty(nameIndex);
  }

  //  void QQmlJSCodeGenerator::generate_LoadOptionalProperty(int name, int
  //      offset)
  void generate_LoadOptionalProperty(int name, int offset) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall29 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall29>(taken[29]);
      call(this, name, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadOptionalProperty(name, offset);
  }

  //  void QQmlJSCodeGenerator::generate_GetLookup(int index)
  void generate_GetLookup(int index) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall30 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall30>(taken[30]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_GetLookup(index);
  }

  //  void QQmlJSCodeGenerator::generate_GetOptionalLookup(int index, int
  //      offset)
  void generate_GetOptionalLookup(int index, int offset) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall31 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall31>(taken[31]);
      call(this, index, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_GetOptionalLookup(index, offset);
  }

  //  void QQmlJSCodeGenerator::generate_StoreProperty(int name, int
  //      baseReg)
  void generate_StoreProperty(int name, int baseReg) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall32 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall32>(taken[32]);
      call(this, name, baseReg, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreProperty(name, baseReg);
  }

  //  void QQmlJSCodeGenerator::generate_SetLookup(int index, int base)
  void generate_SetLookup(int index, int base) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall33 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall33>(taken[33]);
      call(this, index, base, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_SetLookup(index, base);
  }

  //  void QQmlJSCodeGenerator::generate_LoadSuperProperty(int property)
  void generate_LoadSuperProperty(int property) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall34 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall34>(taken[34]);
      call(this, property, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadSuperProperty(property);
  }

  //  void QQmlJSCodeGenerator::generate_StoreSuperProperty(int property)
  void generate_StoreSuperProperty(int property) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall35 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall35>(taken[35]);
      call(this, property, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_StoreSuperProperty(property);
  }

  //  void QQmlJSCodeGenerator::generate_Yield()
  void generate_Yield() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall36 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Yield();
  }

  //  void QQmlJSCodeGenerator::generate_YieldStar()
  void generate_YieldStar() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall37 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_YieldStar();
  }

  //  void QQmlJSCodeGenerator::generate_Resume(int a0)
  void generate_Resume(int a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall38 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Resume(a0);
  }

  //  void QQmlJSCodeGenerator::generate_CallValue(int name, int argc, int
  //      argv)
  void generate_CallValue(int name, int argc, int argv) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall39 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall39>(taken[39]);
      call(this, name, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallValue(name, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallWithReceiver(int name, int
  //      thisObject, int argc, int argv)
  void generate_CallWithReceiver(
      int name,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall40 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall40>(taken[40]);
      call(this, name, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallWithReceiver(name, thisObject, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallProperty(int name, int base,
  //      int argc, int argv)
  void generate_CallProperty(
      int name,
      int base,
      int argc,
      int argv) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall41 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall41>(taken[41]);
      call(this, name, base, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallProperty(name, base, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallPropertyLookup(int
  //      lookupIndex, int base, int argc, int argv)
  void generate_CallPropertyLookup(
      int lookupIndex,
      int base,
      int argc,
      int argv) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall42 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall42>(taken[42]);
      call(this, lookupIndex, base, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallPropertyLookup(lookupIndex, base, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallName(int name, int argc, int
  //      argv)
  void generate_CallName(int name, int argc, int argv) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall43 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall43>(taken[43]);
      call(this, name, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallName(name, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(int argc,
  //      int argv)
  void generate_CallPossiblyDirectEval(int argc, int argv) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall44 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall44>(taken[44]);
      call(this, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallGlobalLookup(int index, int
  //      argc, int argv)
  void generate_CallGlobalLookup(int index, int argc, int argv) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall45 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall45>(taken[45]);
      call(this, index, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallGlobalLookup(index, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(int
  //      index, int argc, int argv)
  void generate_CallQmlContextPropertyLookup(
      int index,
      int argc,
      int argv) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall46 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall46>(taken[46]);
      call(this, index, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(index, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_CallWithSpread(int func, int
  //      thisObject, int argc, int argv)
  void generate_CallWithSpread(
      int func,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall47 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall47>(taken[47]);
      call(this, func, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CallWithSpread(func, thisObject, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_TailCall(int func, int thisObject,
  //      int argc, int argv)
  void generate_TailCall(
      int func,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall48 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall48>(taken[48]);
      call(this, func, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_TailCall(func, thisObject, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_Construct(int func, int argc, int
  //      argv)
  void generate_Construct(int func, int argc, int argv) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall49 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall49>(taken[49]);
      call(this, func, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Construct(func, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_ConstructWithSpread(int func, int
  //      argc, int argv)
  void generate_ConstructWithSpread(int func, int argc, int argv) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall50 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall50>(taken[50]);
      call(this, func, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ConstructWithSpread(func, argc, argv);
  }

  //  void QQmlJSCodeGenerator::generate_SetUnwindHandler(int offset)
  void generate_SetUnwindHandler(int offset) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall51 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall51>(taken[51]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_SetUnwindHandler(offset);
  }

  //  void QQmlJSCodeGenerator::generate_UnwindDispatch()
  void generate_UnwindDispatch() override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall52 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall52>(taken[52]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UnwindDispatch();
  }

  //  void QQmlJSCodeGenerator::generate_UnwindToLabel(int level, int
  //      offset)
  void generate_UnwindToLabel(int level, int offset) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall53 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall53>(taken[53]);
      call(this, level, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UnwindToLabel(level, offset);
  }

  //  void QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(int name)
  void generate_DeadTemporalZoneCheck(int name) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall54 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall54>(taken[54]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(name);
  }

  //  void QQmlJSCodeGenerator::generate_ThrowException()
  void generate_ThrowException() override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall55 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall55>(taken[55]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ThrowException();
  }

  //  void QQmlJSCodeGenerator::generate_GetException()
  void generate_GetException() override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall56 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall56>(taken[56]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_GetException();
  }

  //  void QQmlJSCodeGenerator::generate_SetException()
  void generate_SetException() override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall57 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall57>(taken[57]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_SetException();
  }

  //  void QQmlJSCodeGenerator::generate_CreateCallContext()
  void generate_CreateCallContext() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall58 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall58>(taken[58]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CreateCallContext();
  }

  //  void QQmlJSCodeGenerator::generate_PushCatchContext(int index, int
  //      name)
  void generate_PushCatchContext(int index, int name) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall59 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall59>(taken[59]);
      call(this, index, name, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PushCatchContext(index, name);
  }

  //  void QQmlJSCodeGenerator::generate_PushWithContext()
  void generate_PushWithContext() override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall60 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall60>(taken[60]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PushWithContext();
  }

  //  void QQmlJSCodeGenerator::generate_PushBlockContext(int index)
  void generate_PushBlockContext(int index) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall61 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall61>(taken[61]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PushBlockContext(index);
  }

  //  void QQmlJSCodeGenerator::generate_CloneBlockContext()
  void generate_CloneBlockContext() override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall62 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall62>(taken[62]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CloneBlockContext();
  }

  //  void QQmlJSCodeGenerator::generate_PushScriptContext(int index)
  void generate_PushScriptContext(int index) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall63 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall63>(taken[63]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PushScriptContext(index);
  }

  //  void QQmlJSCodeGenerator::generate_PopScriptContext()
  void generate_PopScriptContext() override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall64 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall64>(taken[64]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PopScriptContext();
  }

  //  void QQmlJSCodeGenerator::generate_PopContext()
  void generate_PopContext() override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall65 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall65>(taken[65]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_PopContext();
  }

  //  void QQmlJSCodeGenerator::generate_GetIterator(int iterator)
  void generate_GetIterator(int iterator) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall66 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall66>(taken[66]);
      call(this, iterator, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_GetIterator(iterator);
  }

  //  void QQmlJSCodeGenerator::generate_IteratorNext(int value, int
  //      offset)
  void generate_IteratorNext(int value, int offset) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall67 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall67>(taken[67]);
      call(this, value, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_IteratorNext(value, offset);
  }

  //  void QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(int
  //      iterator, int object, int offset)
  void generate_IteratorNextForYieldStar(
      int iterator,
      int object,
      int offset) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall68 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall68>(taken[68]);
      call(this, iterator, object, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(iterator, object, offset);
  }

  //  void QQmlJSCodeGenerator::generate_IteratorClose()
  void generate_IteratorClose() override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall69 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall69>(taken[69]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_IteratorClose();
  }

  //  void QQmlJSCodeGenerator::generate_DestructureRestElement()
  void generate_DestructureRestElement() override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall70 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall70>(taken[70]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DestructureRestElement();
  }

  //  void QQmlJSCodeGenerator::generate_DeleteProperty(int base, int
  //      index)
  void generate_DeleteProperty(int base, int index) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall71 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall71>(taken[71]);
      call(this, base, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DeleteProperty(base, index);
  }

  //  void QQmlJSCodeGenerator::generate_DeleteName(int name)
  void generate_DeleteName(int name) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall72 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall72>(taken[72]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DeleteName(name);
  }

  //  void QQmlJSCodeGenerator::generate_TypeofName(int name)
  void generate_TypeofName(int name) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall73 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall73>(taken[73]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_TypeofName(name);
  }

  //  void QQmlJSCodeGenerator::generate_TypeofValue()
  void generate_TypeofValue() override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall74 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall74>(taken[74]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_TypeofValue();
  }

  //  void QQmlJSCodeGenerator::generate_DeclareVar(int varName, int
  //      isDeletable)
  void generate_DeclareVar(int varName, int isDeletable) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall75 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall75>(taken[75]);
      call(this, varName, isDeletable, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DeclareVar(varName, isDeletable);
  }

  //  void QQmlJSCodeGenerator::generate_DefineArray(int argc, int args)
  void generate_DefineArray(int argc, int args) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall76 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall76>(taken[76]);
      call(this, argc, args, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DefineArray(argc, args);
  }

  //  void QQmlJSCodeGenerator::generate_DefineObjectLiteral(int
  //      internalClassId, int argc, int args)
  void generate_DefineObjectLiteral(
      int internalClassId,
      int argc,
      int args) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall77 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall77>(taken[77]);
      call(this, internalClassId, argc, args, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_DefineObjectLiteral(internalClassId, argc, args);
  }

  //  void QQmlJSCodeGenerator::generate_CreateClass(int classIndex, int
  //      heritage, int computedNames)
  void generate_CreateClass(
      int classIndex,
      int heritage,
      int computedNames) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall78 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall78>(taken[78]);
      call(this, classIndex, heritage, computedNames, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CreateClass(classIndex, heritage, computedNames);
  }

  //  void QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject()
  void generate_CreateMappedArgumentsObject() override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall79 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall79>(taken[79]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject();
  }

  //  void QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject()
  void generate_CreateUnmappedArgumentsObject() override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall80 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall80>(taken[80]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject();
  }

  //  void QQmlJSCodeGenerator::generate_CreateRestParameter(int argIndex)
  void generate_CreateRestParameter(int argIndex) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall81 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall81>(taken[81]);
      call(this, argIndex, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CreateRestParameter(argIndex);
  }

  //  void QQmlJSCodeGenerator::generate_ConvertThisToObject()
  void generate_ConvertThisToObject() override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall82 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall82>(taken[82]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ConvertThisToObject();
  }

  //  void QQmlJSCodeGenerator::generate_LoadSuperConstructor()
  void generate_LoadSuperConstructor() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall83 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_LoadSuperConstructor();
  }

  //  void QQmlJSCodeGenerator::generate_ToObject()
  void generate_ToObject() override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall84 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall84>(taken[84]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ToObject();
  }

  //  void QQmlJSCodeGenerator::generate_Jump(int offset)
  void generate_Jump(int offset) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall85 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall85>(taken[85]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Jump(offset);
  }

  //  void QQmlJSCodeGenerator::generate_JumpTrue(int offset)
  void generate_JumpTrue(int offset) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall86 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall86>(taken[86]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_JumpTrue(offset);
  }

  //  void QQmlJSCodeGenerator::generate_JumpFalse(int offset)
  void generate_JumpFalse(int offset) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall87 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall87>(taken[87]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_JumpFalse(offset);
  }

  //  void QQmlJSCodeGenerator::generate_JumpNoException(int offset)
  void generate_JumpNoException(int offset) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall88 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall88>(taken[88]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_JumpNoException(offset);
  }

  //  void QQmlJSCodeGenerator::generate_JumpNotUndefined(int offset)
  void generate_JumpNotUndefined(int offset) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall89 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall89>(taken[89]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_JumpNotUndefined(offset);
  }

  //  void QQmlJSCodeGenerator::generate_CheckException()
  void generate_CheckException() override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall90 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall90>(taken[90]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CheckException();
  }

  //  void QQmlJSCodeGenerator::generate_CmpEqNull()
  void generate_CmpEqNull() override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall91 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall91>(taken[91]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpEqNull();
  }

  //  void QQmlJSCodeGenerator::generate_CmpNeNull()
  void generate_CmpNeNull() override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall92 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpNeNull();
  }

  //  void QQmlJSCodeGenerator::generate_CmpEqInt(int lhs)
  void generate_CmpEqInt(int lhs) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall93 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall93>(taken[93]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpEqInt(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpNeInt(int lhs)
  void generate_CmpNeInt(int lhs) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall94 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall94>(taken[94]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpNeInt(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpEq(int lhs)
  void generate_CmpEq(int lhs) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall95 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall95>(taken[95]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpEq(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpNe(int lhs)
  void generate_CmpNe(int lhs) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall96 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall96>(taken[96]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpNe(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpGt(int lhs)
  void generate_CmpGt(int lhs) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall97 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall97>(taken[97]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpGt(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpGe(int lhs)
  void generate_CmpGe(int lhs) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall98 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall98>(taken[98]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpGe(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpLt(int lhs)
  void generate_CmpLt(int lhs) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall99 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall99>(taken[99]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpLt(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpLe(int lhs)
  void generate_CmpLe(int lhs) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall100 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall100>(taken[100]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpLe(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpStrictEqual(int lhs)
  void generate_CmpStrictEqual(int lhs) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall101 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall101>(taken[101]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpStrictEqual(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpStrictNotEqual(int lhs)
  void generate_CmpStrictNotEqual(int lhs) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall102 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall102>(taken[102]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpStrictNotEqual(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpIn(int lhs)
  void generate_CmpIn(int lhs) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall103 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall103>(taken[103]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpIn(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_CmpInstanceOf(int lhs)
  void generate_CmpInstanceOf(int lhs) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall104 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall104>(taken[104]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_CmpInstanceOf(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_As(int lhs)
  void generate_As(int lhs) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall105 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall105>(taken[105]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_As(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_UNot()
  void generate_UNot() override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall106 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall106>(taken[106]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UNot();
  }

  //  void QQmlJSCodeGenerator::generate_UPlus()
  void generate_UPlus() override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall107 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall107>(taken[107]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UPlus();
  }

  //  void QQmlJSCodeGenerator::generate_UMinus()
  void generate_UMinus() override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall108 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall108>(taken[108]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UMinus();
  }

  //  void QQmlJSCodeGenerator::generate_UCompl()
  void generate_UCompl() override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall109 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall109>(taken[109]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UCompl();
  }

  //  void QQmlJSCodeGenerator::generate_Increment()
  void generate_Increment() override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall110 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall110>(taken[110]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Increment();
  }

  //  void QQmlJSCodeGenerator::generate_Decrement()
  void generate_Decrement() override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall111 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall111>(taken[111]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Decrement();
  }

  //  void QQmlJSCodeGenerator::generate_Add(int lhs)
  void generate_Add(int lhs) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall112 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall112>(taken[112]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Add(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitAnd(int lhs)
  void generate_BitAnd(int lhs) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall113 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall113>(taken[113]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitAnd(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitOr(int lhs)
  void generate_BitOr(int lhs) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall114 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall114>(taken[114]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitOr(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitXor(int lhs)
  void generate_BitXor(int lhs) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall115 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall115>(taken[115]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitXor(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_UShr(int lhs)
  void generate_UShr(int lhs) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall116 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall116>(taken[116]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UShr(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Shr(int lhs)
  void generate_Shr(int lhs) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall117 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall117>(taken[117]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Shr(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Shl(int lhs)
  void generate_Shl(int lhs) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall118 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall118>(taken[118]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Shl(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitAndConst(int rhs)
  void generate_BitAndConst(int rhs) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall119 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall119>(taken[119]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitAndConst(rhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitOrConst(int rhs)
  void generate_BitOrConst(int rhs) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall120 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall120>(taken[120]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitOrConst(rhs);
  }

  //  void QQmlJSCodeGenerator::generate_BitXorConst(int rhs)
  void generate_BitXorConst(int rhs) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall121 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall121>(taken[121]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_BitXorConst(rhs);
  }

  //  void QQmlJSCodeGenerator::generate_UShrConst(int rhs)
  void generate_UShrConst(int rhs) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall122 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall122>(taken[122]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_UShrConst(rhs);
  }

  //  void QQmlJSCodeGenerator::generate_ShrConst(int value)
  void generate_ShrConst(int value) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall123 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall123>(taken[123]);
      call(this, value, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ShrConst(value);
  }

  //  void QQmlJSCodeGenerator::generate_ShlConst(int rhs)
  void generate_ShlConst(int rhs) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall124 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall124>(taken[124]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ShlConst(rhs);
  }

  //  void QQmlJSCodeGenerator::generate_Exp(int lhs)
  void generate_Exp(int lhs) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall125 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall125>(taken[125]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Exp(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Mul(int lhs)
  void generate_Mul(int lhs) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall126 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall126>(taken[126]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Mul(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Div(int lhs)
  void generate_Div(int lhs) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall127 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall127>(taken[127]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Div(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Mod(int lhs)
  void generate_Mod(int lhs) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall128 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall128>(taken[128]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Mod(lhs);
  }

  //  void QQmlJSCodeGenerator::generate_Sub(int lhs)
  void generate_Sub(int lhs) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall129 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall129>(taken[129]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_Sub(lhs);
  }

  //  void
  //      QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(int
  //      firstReg, int count)
  void generate_InitializeBlockDeadTemporalZone(
      int firstReg,
      int count) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall130 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall130>(taken[130]);
      call(this, firstReg, count, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(firstReg, count);
  }

  //  void QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined()
  void generate_ThrowOnNullOrUndefined() override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall131 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall131>(taken[131]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined();
  }

  //  void QQmlJSCodeGenerator::generate_GetTemplateObject(int index)
  void generate_GetTemplateObject(int index) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall132 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall132>(taken[132]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::generate_GetTemplateObject(index);
  }

  //  void QQmlJSCodeGenerator::endInstruction(QV4::Moth::Instr::Type a0)
  void endInstruction(QV4::Moth::Instr::Type a0) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSCodeGeneratorCall133 call = reinterpret_cast<CuteQQmlJSCodeGeneratorCall133>(taken[133]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlJSCodeGenerator::endInstruction(a0);
  }
};

//  QQmlJSCodeGenerator::QQmlJSCodeGenerator(const QV4::Compiler::Context
//      *compilerContext, const QV4::Compiler::JSUnitGenerator
//      *unitGenerator, const QQmlJSTypeResolver *typeResolver, QQmlJSLogger
//      *logger, const BasicBlocks &basicBlocks, const InstructionAnnotations
//      &annotations, bool noAotValidation)
extern "C" Q_DECL_EXPORT
QQmlJSCodeGenerator *ritual_ZN19QQmlJSCodeGeneratorC1EPKN3QV48Compiler7ContextEPKNS1_15JSUnitGeneratorEPK18QQmlJSTypeResolverP12QQmlJSLoggerRK8QFlatMapIiN17QQmlJSCompilePass10BasicBlockESt4lessIiE5QListIiESI_ISF_EERKSD_IiNSE_21InstructionAnnotationESH_SJ_SI_ISO_EEb(
    const QV4::Compiler::Context *compilerContext,
    const QV4::Compiler::JSUnitGenerator *unitGenerator,
    const QQmlJSTypeResolver *typeResolver,
    QQmlJSLogger *logger,
    const QQmlJSCompilePass::BasicBlocks *basicBlocks,
    const QQmlJSCompilePass::InstructionAnnotations *annotations,
    bool noAotValidation) {
  return new CuteQQmlJSCodeGenerator(
      compilerContext,
      unitGenerator,
      typeResolver,
      logger,
      *basicBlocks,
      *annotations,
      noAotValidation);
}

//  QQmlJSCodeGenerator::~QQmlJSCodeGenerator()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGeneratorD1Ev(QQmlJSCodeGenerator *self) {
  delete self;
}

//  QQmlJSAotFunction QQmlJSCodeGenerator::run(const Function *function, bool
//      basicBlocksValidationFailed)
extern "C" Q_DECL_EXPORT
QQmlJSAotFunction *ritual_ZN19QQmlJSCodeGenerator3runEPKN17QQmlJSCompilePass8FunctionEb(
    QQmlJSCodeGenerator *self,
    const QQmlJSCompilePass::Function *function,
    bool basicBlocksValidationFailed) {
  return new QQmlJSAotFunction(
      self->run(
          function,
          basicBlocksValidationFailed));
}

//  LookupSignatures QQmlJSCodeGenerator::lookupSignatures() const
extern "C" Q_DECL_EXPORT
LookupSignatures *ritual_ZNK19QQmlJSCodeGenerator16lookupSignaturesEv(
    const QQmlJSCodeGenerator *self) {
  return new LookupSignatures(self->lookupSignatures());
}

//  QString QQmlJSCodeGenerator::metaObject(const QQmlJSScope::ConstPtr
//      &objectType)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator10metaObjectERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *objectType) {
  return new QString(self->metaObject(*objectType));
}

//  QString QQmlJSCodeGenerator::metaType(const QQmlJSScope::ConstPtr &type)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator8metaTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->metaType(*type));
}

//  void QQmlJSCodeGenerator::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_RetEv(
    QQmlJSCodeGenerator *self) {
  self->generate_Ret();
}

//  void QQmlJSCodeGenerator::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_DebugEv(
    QQmlJSCodeGenerator *self) {
  self->generate_Debug();
}

//  void QQmlJSCodeGenerator::generate_LoadConst(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_LoadConstEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_LoadConst(index);
}

//  void QQmlJSCodeGenerator::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_LoadZeroEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadZero();
}

//  void QQmlJSCodeGenerator::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_LoadTrueEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadTrue();
}

//  void QQmlJSCodeGenerator::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_LoadFalseEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadFalse();
}

//  void QQmlJSCodeGenerator::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_LoadNullEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadNull();
}

//  void QQmlJSCodeGenerator::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generate_LoadUndefinedEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadUndefined();
}

//  void QQmlJSCodeGenerator::generate_LoadInt(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator16generate_LoadIntEi(
    QQmlJSCodeGenerator *self,
    int value) {
  self->generate_LoadInt(value);
}

//  void QQmlJSCodeGenerator::generate_MoveConst(int constIndex, int
//      destTemp)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_MoveConstEii(
    QQmlJSCodeGenerator *self,
    int constIndex,
    int destTemp) {
  self->generate_MoveConst(constIndex, destTemp);
}

//  void QQmlJSCodeGenerator::generate_LoadReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator16generate_LoadRegEi(
    QQmlJSCodeGenerator *self,
    int reg) {
  self->generate_LoadReg(reg);
}

//  void QQmlJSCodeGenerator::generate_StoreReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_StoreRegEi(
    QQmlJSCodeGenerator *self,
    int reg) {
  self->generate_StoreReg(reg);
}

//  void QQmlJSCodeGenerator::generate_MoveReg(int srcReg, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator16generate_MoveRegEii(
    QQmlJSCodeGenerator *self,
    int srcReg,
    int destReg) {
  self->generate_MoveReg(srcReg, destReg);
}

//  void QQmlJSCodeGenerator::generate_LoadImport(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_LoadImportEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_LoadImport(index);
}

//  void QQmlJSCodeGenerator::generate_LoadLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_LoadLocalEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_LoadLocal(index);
}

//  void QQmlJSCodeGenerator::generate_StoreLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_StoreLocalEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_StoreLocal(index);
}

//  void QQmlJSCodeGenerator::generate_LoadScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_LoadScopedLocalEii(
    QQmlJSCodeGenerator *self,
    int scope,
    int index) {
  self->generate_LoadScopedLocal(scope, index);
}

//  void QQmlJSCodeGenerator::generate_StoreScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_StoreScopedLocalEii(
    QQmlJSCodeGenerator *self,
    int scope,
    int index) {
  self->generate_StoreScopedLocal(scope, index);
}

//  void QQmlJSCodeGenerator::generate_LoadRuntimeString(int stringId)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_LoadRuntimeStringEi(
    QQmlJSCodeGenerator *self,
    int stringId) {
  self->generate_LoadRuntimeString(stringId);
}

//  void QQmlJSCodeGenerator::generate_MoveRegExp(int regExpId, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_MoveRegExpEii(
    QQmlJSCodeGenerator *self,
    int regExpId,
    int destReg) {
  self->generate_MoveRegExp(regExpId, destReg);
}

//  void QQmlJSCodeGenerator::generate_LoadClosure(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_LoadClosureEi(
    QQmlJSCodeGenerator *self,
    int value) {
  self->generate_LoadClosure(value);
}

//  void QQmlJSCodeGenerator::generate_LoadName(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_LoadNameEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  self->generate_LoadName(nameIndex);
}

//  void QQmlJSCodeGenerator::generate_LoadGlobalLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_LoadGlobalLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_LoadGlobalLookup(index);
}

//  void QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_LoadQmlContextPropertyLookup(index);
}

//  void QQmlJSCodeGenerator::generate_StoreNameSloppy(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_StoreNameSloppyEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  self->generate_StoreNameSloppy(nameIndex);
}

//  void QQmlJSCodeGenerator::generate_StoreNameStrict(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_StoreNameStrictEi(
    QQmlJSCodeGenerator *self,
    int name) {
  self->generate_StoreNameStrict(name);
}

//  void QQmlJSCodeGenerator::generate_LoadElement(int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_LoadElementEi(
    QQmlJSCodeGenerator *self,
    int base) {
  self->generate_LoadElement(base);
}

//  void QQmlJSCodeGenerator::generate_StoreElement(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_StoreElementEii(
    QQmlJSCodeGenerator *self,
    int base,
    int index) {
  self->generate_StoreElement(base, index);
}

//  void QQmlJSCodeGenerator::generate_LoadProperty(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_LoadPropertyEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  self->generate_LoadProperty(nameIndex);
}

//  void QQmlJSCodeGenerator::generate_LoadOptionalProperty(int name, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator29generate_LoadOptionalPropertyEii(
    QQmlJSCodeGenerator *self,
    int name,
    int offset) {
  self->generate_LoadOptionalProperty(name, offset);
}

//  void QQmlJSCodeGenerator::generate_GetLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_GetLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_GetLookup(index);
}

//  void QQmlJSCodeGenerator::generate_GetOptionalLookup(int index, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_GetOptionalLookupEii(
    QQmlJSCodeGenerator *self,
    int index,
    int offset) {
  self->generate_GetOptionalLookup(index, offset);
}

//  void QQmlJSCodeGenerator::generate_StoreProperty(int name, int baseReg)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generate_StorePropertyEii(
    QQmlJSCodeGenerator *self,
    int name,
    int baseReg) {
  self->generate_StoreProperty(name, baseReg);
}

//  void QQmlJSCodeGenerator::generate_SetLookup(int index, int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_SetLookupEii(
    QQmlJSCodeGenerator *self,
    int index,
    int base) {
  self->generate_SetLookup(index, base);
}

//  void QQmlJSCodeGenerator::generate_LoadSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_LoadSuperPropertyEi(
    QQmlJSCodeGenerator *self,
    int property) {
  self->generate_LoadSuperProperty(property);
}

//  void QQmlJSCodeGenerator::generate_StoreSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator27generate_StoreSuperPropertyEi(
    QQmlJSCodeGenerator *self,
    int property) {
  self->generate_StoreSuperProperty(property);
}

//  void QQmlJSCodeGenerator::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_YieldEv(
    QQmlJSCodeGenerator *self) {
  self->generate_Yield();
}

//  void QQmlJSCodeGenerator::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_YieldStarEv(
    QQmlJSCodeGenerator *self) {
  self->generate_YieldStar();
}

//  void QQmlJSCodeGenerator::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator15generate_ResumeEi(
    QQmlJSCodeGenerator *self,
    int a0) {
  self->generate_Resume(a0);
}

//  void QQmlJSCodeGenerator::generate_CallValue(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_CallValueEiii(
    QQmlJSCodeGenerator *self,
    int name,
    int argc,
    int argv) {
  self->generate_CallValue(name, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallWithReceiver(int name, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_CallWithReceiverEiiii(
    QQmlJSCodeGenerator *self,
    int name,
    int thisObject,
    int argc,
    int argv) {
  self->generate_CallWithReceiver(name, thisObject, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallProperty(int name, int base, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_CallPropertyEiiii(
    QQmlJSCodeGenerator *self,
    int name,
    int base,
    int argc,
    int argv) {
  self->generate_CallProperty(name, base, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallPropertyLookup(int lookupIndex,
//      int base, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator27generate_CallPropertyLookupEiiii(
    QQmlJSCodeGenerator *self,
    int lookupIndex,
    int base,
    int argc,
    int argv) {
  self->generate_CallPropertyLookup(lookupIndex, base, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallName(int name, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_CallNameEiii(
    QQmlJSCodeGenerator *self,
    int name,
    int argc,
    int argv) {
  self->generate_CallName(name, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator31generate_CallPossiblyDirectEvalEii(
    QQmlJSCodeGenerator *self,
    int argc,
    int argv) {
  self->generate_CallPossiblyDirectEval(argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallGlobalLookup(int index, int argc,
//      int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_CallGlobalLookupEiii(
    QQmlJSCodeGenerator *self,
    int index,
    int argc,
    int argv) {
  self->generate_CallGlobalLookup(index, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(int
//      index, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSCodeGenerator *self,
    int index,
    int argc,
    int argv) {
  self->generate_CallQmlContextPropertyLookup(index, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_CallWithSpread(int func, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_CallWithSpreadEiiii(
    QQmlJSCodeGenerator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->generate_CallWithSpread(func, thisObject, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_TailCall(int func, int thisObject, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_TailCallEiiii(
    QQmlJSCodeGenerator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->generate_TailCall(func, thisObject, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_Construct(int func, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_ConstructEiii(
    QQmlJSCodeGenerator *self,
    int func,
    int argc,
    int argv) {
  self->generate_Construct(func, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_ConstructWithSpread(int func, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator28generate_ConstructWithSpreadEiii(
    QQmlJSCodeGenerator *self,
    int func,
    int argc,
    int argv) {
  self->generate_ConstructWithSpread(func, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_SetUnwindHandler(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_SetUnwindHandlerEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_SetUnwindHandler(offset);
}

//  void QQmlJSCodeGenerator::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_UnwindDispatchEv(
    QQmlJSCodeGenerator *self) {
  self->generate_UnwindDispatch();
}

//  void QQmlJSCodeGenerator::generate_UnwindToLabel(int level, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generate_UnwindToLabelEii(
    QQmlJSCodeGenerator *self,
    int level,
    int offset) {
  self->generate_UnwindToLabel(level, offset);
}

//  void QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator30generate_DeadTemporalZoneCheckEi(
    QQmlJSCodeGenerator *self,
    int name) {
  self->generate_DeadTemporalZoneCheck(name);
}

//  void QQmlJSCodeGenerator::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_ThrowExceptionEv(
    QQmlJSCodeGenerator *self) {
  self->generate_ThrowException();
}

//  void QQmlJSCodeGenerator::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_GetExceptionEv(
    QQmlJSCodeGenerator *self) {
  self->generate_GetException();
}

//  void QQmlJSCodeGenerator::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_SetExceptionEv(
    QQmlJSCodeGenerator *self) {
  self->generate_SetException();
}

//  void QQmlJSCodeGenerator::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_CreateCallContextEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CreateCallContext();
}

//  void QQmlJSCodeGenerator::generate_PushCatchContext(int index, int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_PushCatchContextEii(
    QQmlJSCodeGenerator *self,
    int index,
    int name) {
  self->generate_PushCatchContext(index, name);
}

//  void QQmlJSCodeGenerator::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_PushWithContextEv(
    QQmlJSCodeGenerator *self) {
  self->generate_PushWithContext();
}

//  void QQmlJSCodeGenerator::generate_PushBlockContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_PushBlockContextEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_PushBlockContext(index);
}

//  void QQmlJSCodeGenerator::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_CloneBlockContextEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CloneBlockContext();
}

//  void QQmlJSCodeGenerator::generate_PushScriptContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_PushScriptContextEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_PushScriptContext(index);
}

//  void QQmlJSCodeGenerator::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_PopScriptContextEv(
    QQmlJSCodeGenerator *self) {
  self->generate_PopScriptContext();
}

//  void QQmlJSCodeGenerator::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_PopContextEv(
    QQmlJSCodeGenerator *self) {
  self->generate_PopContext();
}

//  void QQmlJSCodeGenerator::generate_GetIterator(int iterator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_GetIteratorEi(
    QQmlJSCodeGenerator *self,
    int iterator) {
  self->generate_GetIterator(iterator);
}

//  void QQmlJSCodeGenerator::generate_IteratorNext(int value, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21generate_IteratorNextEii(
    QQmlJSCodeGenerator *self,
    int value,
    int offset) {
  self->generate_IteratorNext(value, offset);
}

//  void QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(int iterator,
//      int object, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator33generate_IteratorNextForYieldStarEiii(
    QQmlJSCodeGenerator *self,
    int iterator,
    int object,
    int offset) {
  self->generate_IteratorNextForYieldStar(iterator, object, offset);
}

//  void QQmlJSCodeGenerator::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generate_IteratorCloseEv(
    QQmlJSCodeGenerator *self) {
  self->generate_IteratorClose();
}

//  void QQmlJSCodeGenerator::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator31generate_DestructureRestElementEv(
    QQmlJSCodeGenerator *self) {
  self->generate_DestructureRestElement();
}

//  void QQmlJSCodeGenerator::generate_DeleteProperty(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_DeletePropertyEii(
    QQmlJSCodeGenerator *self,
    int base,
    int index) {
  self->generate_DeleteProperty(base, index);
}

//  void QQmlJSCodeGenerator::generate_DeleteName(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_DeleteNameEi(
    QQmlJSCodeGenerator *self,
    int name) {
  self->generate_DeleteName(name);
}

//  void QQmlJSCodeGenerator::generate_TypeofName(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_TypeofNameEi(
    QQmlJSCodeGenerator *self,
    int name) {
  self->generate_TypeofName(name);
}

//  void QQmlJSCodeGenerator::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_TypeofValueEv(
    QQmlJSCodeGenerator *self) {
  self->generate_TypeofValue();
}

//  void QQmlJSCodeGenerator::generate_DeclareVar(int varName, int
//      isDeletable)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_DeclareVarEii(
    QQmlJSCodeGenerator *self,
    int varName,
    int isDeletable) {
  self->generate_DeclareVar(varName, isDeletable);
}

//  void QQmlJSCodeGenerator::generate_DefineArray(int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_DefineArrayEii(
    QQmlJSCodeGenerator *self,
    int argc,
    int args) {
  self->generate_DefineArray(argc, args);
}

//  void QQmlJSCodeGenerator::generate_DefineObjectLiteral(int
//      internalClassId, int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator28generate_DefineObjectLiteralEiii(
    QQmlJSCodeGenerator *self,
    int internalClassId,
    int argc,
    int args) {
  self->generate_DefineObjectLiteral(internalClassId, argc, args);
}

//  void QQmlJSCodeGenerator::generate_CreateClass(int classIndex, int
//      heritage, int computedNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_CreateClassEiii(
    QQmlJSCodeGenerator *self,
    int classIndex,
    int heritage,
    int computedNames) {
  self->generate_CreateClass(classIndex, heritage, computedNames);
}

//  void QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator36generate_CreateMappedArgumentsObjectEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CreateMappedArgumentsObject();
}

//  void QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSCodeGenerator::generate_CreateRestParameter(int argIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator28generate_CreateRestParameterEi(
    QQmlJSCodeGenerator *self,
    int argIndex) {
  self->generate_CreateRestParameter(argIndex);
}

//  void QQmlJSCodeGenerator::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator28generate_ConvertThisToObjectEv(
    QQmlJSCodeGenerator *self) {
  self->generate_ConvertThisToObject();
}

//  void QQmlJSCodeGenerator::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator29generate_LoadSuperConstructorEv(
    QQmlJSCodeGenerator *self) {
  self->generate_LoadSuperConstructor();
}

//  void QQmlJSCodeGenerator::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_ToObjectEv(
    QQmlJSCodeGenerator *self) {
  self->generate_ToObject();
}

//  void QQmlJSCodeGenerator::generate_Jump(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator13generate_JumpEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_Jump(offset);
}

//  void QQmlJSCodeGenerator::generate_JumpTrue(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_JumpTrueEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_JumpTrue(offset);
}

//  void QQmlJSCodeGenerator::generate_JumpFalse(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_JumpFalseEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_JumpFalse(offset);
}

//  void QQmlJSCodeGenerator::generate_JumpNoException(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_JumpNoExceptionEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_JumpNoException(offset);
}

//  void QQmlJSCodeGenerator::generate_JumpNotUndefined(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generate_JumpNotUndefinedEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  self->generate_JumpNotUndefined(offset);
}

//  void QQmlJSCodeGenerator::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_CheckExceptionEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CheckException();
}

//  void QQmlJSCodeGenerator::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_CmpEqNullEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CmpEqNull();
}

//  void QQmlJSCodeGenerator::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_CmpNeNullEv(
    QQmlJSCodeGenerator *self) {
  self->generate_CmpNeNull();
}

//  void QQmlJSCodeGenerator::generate_CmpEqInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_CmpEqIntEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpEqInt(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpNeInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_CmpNeIntEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpNeInt(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpEq(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpEqEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpEq(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpNe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpNeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpNe(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpGt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpGtEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpGt(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpGe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpGeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpGe(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpLt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpLtEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpLt(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpLe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpLeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpLe(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpStrictEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator23generate_CmpStrictEqualEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpStrictEqual(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpStrictNotEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_CmpStrictNotEqualEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpStrictNotEqual(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpIn(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_CmpInEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpIn(lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpInstanceOf(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generate_CmpInstanceOfEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_CmpInstanceOf(lhs);
}

//  void QQmlJSCodeGenerator::generate_As(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator11generate_AsEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_As(lhs);
}

//  void QQmlJSCodeGenerator::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator13generate_UNotEv(
    QQmlJSCodeGenerator *self) {
  self->generate_UNot();
}

//  void QQmlJSCodeGenerator::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_UPlusEv(
    QQmlJSCodeGenerator *self) {
  self->generate_UPlus();
}

//  void QQmlJSCodeGenerator::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator15generate_UMinusEv(
    QQmlJSCodeGenerator *self) {
  self->generate_UMinus();
}

//  void QQmlJSCodeGenerator::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator15generate_UComplEv(
    QQmlJSCodeGenerator *self) {
  self->generate_UCompl();
}

//  void QQmlJSCodeGenerator::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_IncrementEv(
    QQmlJSCodeGenerator *self) {
  self->generate_Increment();
}

//  void QQmlJSCodeGenerator::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_DecrementEv(
    QQmlJSCodeGenerator *self) {
  self->generate_Decrement();
}

//  void QQmlJSCodeGenerator::generate_Add(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_AddEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Add(lhs);
}

//  void QQmlJSCodeGenerator::generate_BitAnd(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator15generate_BitAndEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_BitAnd(lhs);
}

//  void QQmlJSCodeGenerator::generate_BitOr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generate_BitOrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_BitOr(lhs);
}

//  void QQmlJSCodeGenerator::generate_BitXor(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator15generate_BitXorEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_BitXor(lhs);
}

//  void QQmlJSCodeGenerator::generate_UShr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator13generate_UShrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_UShr(lhs);
}

//  void QQmlJSCodeGenerator::generate_Shr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_ShrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Shr(lhs);
}

//  void QQmlJSCodeGenerator::generate_Shl(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_ShlEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Shl(lhs);
}

//  void QQmlJSCodeGenerator::generate_BitAndConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_BitAndConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  self->generate_BitAndConst(rhs);
}

//  void QQmlJSCodeGenerator::generate_BitOrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generate_BitOrConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  self->generate_BitOrConst(rhs);
}

//  void QQmlJSCodeGenerator::generate_BitXorConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20generate_BitXorConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  self->generate_BitXorConst(rhs);
}

//  void QQmlJSCodeGenerator::generate_UShrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generate_UShrConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  self->generate_UShrConst(rhs);
}

//  void QQmlJSCodeGenerator::generate_ShrConst(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_ShrConstEi(
    QQmlJSCodeGenerator *self,
    int value) {
  self->generate_ShrConst(value);
}

//  void QQmlJSCodeGenerator::generate_ShlConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generate_ShlConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  self->generate_ShlConst(rhs);
}

//  void QQmlJSCodeGenerator::generate_Exp(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_ExpEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Exp(lhs);
}

//  void QQmlJSCodeGenerator::generate_Mul(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_MulEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Mul(lhs);
}

//  void QQmlJSCodeGenerator::generate_Div(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_DivEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Div(lhs);
}

//  void QQmlJSCodeGenerator::generate_Mod(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_ModEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Mod(lhs);
}

//  void QQmlJSCodeGenerator::generate_Sub(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator12generate_SubEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  self->generate_Sub(lhs);
}

//  void QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(int
//      firstReg, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSCodeGenerator *self,
    int firstReg,
    int count) {
  self->generate_InitializeBlockDeadTemporalZone(firstReg, count);
}

//  void QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSCodeGenerator *self) {
  self->generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSCodeGenerator::generate_GetTemplateObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator26generate_GetTemplateObjectEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_GetTemplateObject(index);
}

//  Verdict QQmlJSCodeGenerator::startInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::ByteCodeHandler::Verdict ritual_ZN19QQmlJSCodeGenerator16startInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSCodeGenerator *self,
    QV4::Moth::Instr::Type a0) {
  return self->startInstruction(a0);
}

//  void QQmlJSCodeGenerator::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSCodeGenerator *self,
    QV4::Moth::Instr::Type a0) {
  self->endInstruction(a0);
}

//  void QQmlJSCodeGenerator::addInclude(const QString &include)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator10addIncludeERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *include) {
  self->addInclude(*include);
}

//  QString QQmlJSCodeGenerator::conversion(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator10conversionE21QQmlJSRegisterContentS0_RK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to,
    const QString *variable) {
  return new QString(self->conversion(*from, *to, *variable));
}

//  QString QQmlJSCodeGenerator::conversion(const QQmlJSScope::ConstPtr
//      &from, QQmlJSRegisterContent to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator10conversionERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContentRK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *from,
    const QQmlJSRegisterContent *to,
    const QString *variable) {
  return new QString(self->conversion(*from, *to, *variable));
}

//  QString QQmlJSCodeGenerator::conversion(QQmlJSRegisterContent from, const
//      QQmlJSScope::ConstPtr &to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator10conversionE21QQmlJSRegisterContentRK22QDeferredSharedPointerIK11QQmlJSScopeERK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSScope::ConstPtr *to,
    const QString *variable) {
  return new QString(self->conversion(*from, *to, *variable));
}

//  QString QQmlJSCodeGenerator::conversion(const QQmlJSScope::ConstPtr
//      &from, const QQmlJSScope::ConstPtr &to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator10conversionERK22QDeferredSharedPointerIK11QQmlJSScopeES5_RK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *from,
    const QQmlJSScope::ConstPtr *to,
    const QString *variable) {
  return new QString(self->conversion(*from, *to, *variable));
}

//  QString QQmlJSCodeGenerator::convertStored(const QQmlJSScope::ConstPtr
//      &from, const QQmlJSScope::ConstPtr &to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator13convertStoredERK22QDeferredSharedPointerIK11QQmlJSScopeES5_RK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *from,
    const QQmlJSScope::ConstPtr *to,
    const QString *variable) {
  return new QString(self->convertStored(*from, *to, *variable));
}

//  QString QQmlJSCodeGenerator::convertContained(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to, const QString &variable)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator16convertContainedE21QQmlJSRegisterContentS0_RK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to,
    const QString *variable) {
  return new QString(self->convertContained(*from, *to, *variable));
}

//  void QQmlJSCodeGenerator::generateReturnError()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19generateReturnErrorEv(
    QQmlJSCodeGenerator *self) {
  self->generateReturnError();
}

//  void QQmlJSCodeGenerator::reject(const QString &thing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator6rejectERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *thing) {
  self->reject(*thing);
}

//  void QQmlJSCodeGenerator::skip(const QString &thing)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator4skipERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *thing) {
  self->skip(*thing);
}

//  QString QQmlJSCodeGenerator::metaTypeFromType(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator16metaTypeFromTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->metaTypeFromType(*type));
}

//  QString QQmlJSCodeGenerator::metaTypeFromName(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator16metaTypeFromNameERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->metaTypeFromName(*type));
}

//  QString QQmlJSCodeGenerator::compositeMetaType(const QString
//      &elementName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator17compositeMetaTypeERK7QString(
    const QQmlJSCodeGenerator *self,
    const QString *elementName) {
  return new QString(self->compositeMetaType(*elementName));
}

//  QString QQmlJSCodeGenerator::compositeListMetaType(const QString
//      &elementName) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator21compositeListMetaTypeERK7QString(
    const QQmlJSCodeGenerator *self,
    const QString *elementName) {
  return new QString(self->compositeListMetaType(*elementName));
}

//  QString QQmlJSCodeGenerator::contentPointer(QQmlJSRegisterContent
//      content, const QString &var)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator14contentPointerE21QQmlJSRegisterContentRK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *content,
    const QString *var) {
  return new QString(self->contentPointer(*content, *var));
}

//  QString QQmlJSCodeGenerator::contentType(QQmlJSRegisterContent content,
//      const QString &var)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator11contentTypeE21QQmlJSRegisterContentRK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *content,
    const QString *var) {
  return new QString(self->contentType(*content, *var));
}

//  void QQmlJSCodeGenerator::generateSetInstructionPointer()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator29generateSetInstructionPointerEv(
    QQmlJSCodeGenerator *self) {
  self->generateSetInstructionPointer();
}

//  void QQmlJSCodeGenerator::generateLookup(const QString &lookup, const
//      QString &initialization, const QString &resultPreparation)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator14generateLookupERK7QStringS2_S2_(
    QQmlJSCodeGenerator *self,
    const QString *lookup,
    const QString *initialization,
    const QString *resultPreparation) {
  self->generateLookup(*lookup, *initialization, *resultPreparation);
}

//  QString QQmlJSCodeGenerator::getLookupPreparation(QQmlJSRegisterContent
//      content, const QString &var, int lookup)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator20getLookupPreparationE21QQmlJSRegisterContentRK7QStringi(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *content,
    const QString *var,
    int lookup) {
  return new QString(self->getLookupPreparation(*content, *var, lookup));
}

//  void QQmlJSCodeGenerator::generateEnumLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generateEnumLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generateEnumLookup(index);
}

//  QString QQmlJSCodeGenerator::registerVariable(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator16registerVariableEi(
    const QQmlJSCodeGenerator *self,
    int index) {
  return new QString(self->registerVariable(index));
}

//  QString QQmlJSCodeGenerator::lookupVariable(int lookupIndex) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator14lookupVariableEi(
    const QQmlJSCodeGenerator *self,
    int lookupIndex) {
  return new QString(self->lookupVariable(lookupIndex));
}

//  QString QQmlJSCodeGenerator::consumedRegisterVariable(int index) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator24consumedRegisterVariableEi(
    const QQmlJSCodeGenerator *self,
    int index) {
  return new QString(self->consumedRegisterVariable(index));
}

//  QString QQmlJSCodeGenerator::consumedAccumulatorVariableIn() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator29consumedAccumulatorVariableInEv(
    const QQmlJSCodeGenerator *self) {
  return new QString(self->consumedAccumulatorVariableIn());
}

//  QString QQmlJSCodeGenerator::changedRegisterVariable() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator23changedRegisterVariableEv(
    const QQmlJSCodeGenerator *self) {
  return new QString(self->changedRegisterVariable());
}

//  QQmlJSRegisterContent QQmlJSCodeGenerator::registerType(int index) const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK19QQmlJSCodeGenerator12registerTypeEi(
    const QQmlJSCodeGenerator *self,
    int index) {
  return new QQmlJSRegisterContent(self->registerType(index));
}

//  QQmlJSRegisterContent QQmlJSCodeGenerator::lookupType(int lookupIndex)
//      const
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZNK19QQmlJSCodeGenerator10lookupTypeEi(
    const QQmlJSCodeGenerator *self,
    int lookupIndex) {
  return new QQmlJSRegisterContent(self->lookupType(lookupIndex));
}

//  bool QQmlJSCodeGenerator::shouldMoveRegister(int index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSCodeGenerator18shouldMoveRegisterEi(
    const QQmlJSCodeGenerator *self,
    int index) {
  return self->shouldMoveRegister(index);
}

//  void QQmlJSCodeGenerator::recordPropertyLookup(const
//      QQmlJSScope::ConstPtr &base, const QQmlJSMetaProperty &prop)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator20recordPropertyLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK18QQmlJSMetaProperty(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaProperty *prop) {
  self->recordPropertyLookup(*base, *prop);
}

//  void QQmlJSCodeGenerator::recordMethodLookup(const QQmlJSScope::ConstPtr
//      &base, const QQmlJSMetaMethod &method)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18recordMethodLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK16QQmlJSMetaMethod(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaMethod *method) {
  self->recordMethodLookup(*base, *method);
}

//  void QQmlJSCodeGenerator::recordEnumKeyLookup(const QQmlJSScope::ConstPtr
//      &base, const QQmlJSMetaEnum &metaEnum, const QString &keyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator19recordEnumKeyLookupERK22QDeferredSharedPointerIK11QQmlJSScopeERK14QQmlJSMetaEnumRK7QString(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *base,
    const QQmlJSMetaEnum *metaEnum,
    const QString *keyName) {
  self->recordEnumKeyLookup(*base, *metaEnum, *keyName);
}

//  void QQmlJSCodeGenerator::resetState()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator10resetStateEv(
    QQmlJSCodeGenerator *self) {
  self->resetState();
}

//  void QQmlJSCodeGenerator::generateExceptionCheck()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generateExceptionCheckEv(
    QQmlJSCodeGenerator *self) {
  self->generateExceptionCheck();
}

//  void QQmlJSCodeGenerator::generateEqualityOperation(QQmlJSRegisterContent
//      lhsContent, const QString &lhsName, const QString &function, bool
//      invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generateEqualityOperationE21QQmlJSRegisterContentRK7QStringS3_b(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *lhsContent,
    const QString *lhsName,
    const QString *function,
    bool invert) {
  self->generateEqualityOperation(*lhsContent, *lhsName, *function, invert);
}

//  void QQmlJSCodeGenerator::generateEqualityOperation(QQmlJSRegisterContent
//      lhsContent, QQmlJSRegisterContent rhsContent, const QString &lhsName,
//      const QString &rhsName, const QString &function, bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator25generateEqualityOperationE21QQmlJSRegisterContentS0_RK7QStringS3_S3_b(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *lhsContent,
    const QQmlJSRegisterContent *rhsContent,
    const QString *lhsName,
    const QString *rhsName,
    const QString *function,
    bool invert) {
  self->generateEqualityOperation(
      *lhsContent,
      *rhsContent,
      *lhsName,
      *rhsName,
      *function,
      invert);
}

//  void QQmlJSCodeGenerator::generateCompareOperation(int lhs, const QString
//      &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generateCompareOperationEiRK7QString(
    QQmlJSCodeGenerator *self,
    int lhs,
    const QString *cppOperator) {
  self->generateCompareOperation(lhs, *cppOperator);
}

//  void QQmlJSCodeGenerator::generateArithmeticOperation(int lhs, const
//      QString &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator27generateArithmeticOperationEiRK7QString(
    QQmlJSCodeGenerator *self,
    int lhs,
    const QString *cppOperator) {
  self->generateArithmeticOperation(lhs, *cppOperator);
}

//  void QQmlJSCodeGenerator::generateShiftOperation(int lhs, const QString
//      &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generateShiftOperationEiRK7QString(
    QQmlJSCodeGenerator *self,
    int lhs,
    const QString *cppOperator) {
  self->generateShiftOperation(lhs, *cppOperator);
}

//  void QQmlJSCodeGenerator::generateArithmeticOperation(const QString &lhs,
//      const QString &rhs, const QString &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator27generateArithmeticOperationERK7QStringS2_S2_(
    QQmlJSCodeGenerator *self,
    const QString *lhs,
    const QString *rhs,
    const QString *cppOperator) {
  self->generateArithmeticOperation(*lhs, *rhs, *cppOperator);
}

//  void QQmlJSCodeGenerator::generateArithmeticConstOperation(int lhsConst,
//      const QString &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator32generateArithmeticConstOperationEiRK7QString(
    QQmlJSCodeGenerator *self,
    int lhsConst,
    const QString *cppOperator) {
  self->generateArithmeticConstOperation(lhsConst, *cppOperator);
}

//  void QQmlJSCodeGenerator::generateJumpCodeWithTypeConversions(int
//      relativeOffset)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator35generateJumpCodeWithTypeConversionsEi(
    QQmlJSCodeGenerator *self,
    int relativeOffset) {
  self->generateJumpCodeWithTypeConversions(relativeOffset);
}

//  void QQmlJSCodeGenerator::generateUnaryOperation(const QString
//      &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator22generateUnaryOperationERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *cppOperator) {
  self->generateUnaryOperation(*cppOperator);
}

//  void QQmlJSCodeGenerator::generateInPlaceOperation(const QString
//      &cppOperator)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generateInPlaceOperationERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *cppOperator) {
  self->generateInPlaceOperation(*cppOperator);
}

//  void QQmlJSCodeGenerator::generateMoveOutVarAfterCall(const QString
//      &outVar)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator27generateMoveOutVarAfterCallERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *outVar) {
  self->generateMoveOutVarAfterCall(*outVar);
}

//  void QQmlJSCodeGenerator::generateTypeLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator18generateTypeLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generateTypeLookup(index);
}

//  void QQmlJSCodeGenerator::generateVariantEqualityComparison(QQmlJSRegiste
//      rContent nonStorable, const QString &registerName, bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator33generateVariantEqualityComparisonE21QQmlJSRegisterContentRK7QStringb(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *nonStorable,
    const QString *registerName,
    bool invert) {
  self->generateVariantEqualityComparison(
      *nonStorable,
      *registerName,
      invert);
}

//  void QQmlJSCodeGenerator::generateVariantEqualityComparison(QQmlJSRegiste
//      rContent storableContent, const QString &typedRegisterName, const
//      QString &varRegisterName, bool invert)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator33generateVariantEqualityComparisonE21QQmlJSRegisterContentRK7QStringS3_b(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *storableContent,
    const QString *typedRegisterName,
    const QString *varRegisterName,
    bool invert) {
  self->generateVariantEqualityComparison(
      *storableContent,
      *typedRegisterName,
      *varRegisterName,
      invert);
}

//  void QQmlJSCodeGenerator::generateArrayInitializer(int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generateArrayInitializerEii(
    QQmlJSCodeGenerator *self,
    int argc,
    int argv) {
  self->generateArrayInitializer(argc, argv);
}

//  void QQmlJSCodeGenerator::generateWriteBack(int registerIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator17generateWriteBackEi(
    QQmlJSCodeGenerator *self,
    int registerIndex) {
  self->generateWriteBack(registerIndex);
}

//  void QQmlJSCodeGenerator::rejectIfNonQObjectOut(const QString &error)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator21rejectIfNonQObjectOutERK7QString(
    QQmlJSCodeGenerator *self,
    const QString *error) {
  self->rejectIfNonQObjectOut(*error);
}

//  void QQmlJSCodeGenerator::rejectIfBadArray()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator16rejectIfBadArrayEv(
    QQmlJSCodeGenerator *self) {
  self->rejectIfBadArray();
}

//  QString QQmlJSCodeGenerator::initAndCall(int argc, int argv, const
//      QString &callMethodTemplate, const QString &initMethodTemplate,
//      QString *outVar)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator11initAndCallEiiRK7QStringS2_PS0_(
    QQmlJSCodeGenerator *self,
    int argc,
    int argv,
    const QString *callMethodTemplate,
    const QString *initMethodTemplate,
    QString *outVar) {
  return new QString(
      self->initAndCall(
          argc,
          argv,
          *callMethodTemplate,
          *initMethodTemplate,
          outVar));
}

//  QString QQmlJSCodeGenerator::castTargetName(const QQmlJSScope::ConstPtr
//      &type) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QQmlJSCodeGenerator14castTargetNameERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    const QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *type) {
  return new QString(self->castTargetName(*type));
}

//  bool QQmlJSCodeGenerator::inlineStringMethod(const QString &name, int
//      base, int argc, int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator18inlineStringMethodERK7QStringiii(
    QQmlJSCodeGenerator *self,
    const QString *name,
    int base,
    int argc,
    int argv) {
  return self->inlineStringMethod(*name, base, argc, argv);
}

//  bool QQmlJSCodeGenerator::inlineTranslateMethod(const QString &name, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator21inlineTranslateMethodERK7QStringii(
    QQmlJSCodeGenerator *self,
    const QString *name,
    int argc,
    int argv) {
  return self->inlineTranslateMethod(*name, argc, argv);
}

//  bool QQmlJSCodeGenerator::inlineMathMethod(const QString &name, int argc,
//      int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator16inlineMathMethodERK7QStringii(
    QQmlJSCodeGenerator *self,
    const QString *name,
    int argc,
    int argv) {
  return self->inlineMathMethod(*name, argc, argv);
}

//  bool QQmlJSCodeGenerator::inlineConsoleMethod(const QString &name, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator19inlineConsoleMethodERK7QStringii(
    QQmlJSCodeGenerator *self,
    const QString *name,
    int argc,
    int argv) {
  return self->inlineConsoleMethod(*name, argc, argv);
}

//  bool QQmlJSCodeGenerator::inlineArrayMethod(const QString &name, int
//      base, int argc, int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator17inlineArrayMethodERK7QStringiii(
    QQmlJSCodeGenerator *self,
    const QString *name,
    int base,
    int argc,
    int argv) {
  return self->inlineArrayMethod(*name, base, argc, argv);
}

//  void QQmlJSCodeGenerator::generate_GetLookupHelper(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSCodeGenerator24generate_GetLookupHelperEi(
    QQmlJSCodeGenerator *self,
    int index) {
  self->generate_GetLookupHelper(index);
}

//  QString QQmlJSCodeGenerator::resolveValueTypeContentPointer(const
//      QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
//      QString &variable, const QString &errorMessage)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator30resolveValueTypeContentPointerERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContentRK7QStringS9_(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *required,
    const QQmlJSRegisterContent *actual,
    const QString *variable,
    const QString *errorMessage) {
  return new QString(
      self->resolveValueTypeContentPointer(
          *required,
          *actual,
          *variable,
          *errorMessage));
}

//  QString QQmlJSCodeGenerator::resolveQObjectPointer(const
//      QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
//      QString &variable, const QString &errorMessage)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator21resolveQObjectPointerERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContentRK7QStringS9_(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *required,
    const QQmlJSRegisterContent *actual,
    const QString *variable,
    const QString *errorMessage) {
  return new QString(
      self->resolveQObjectPointer(
          *required,
          *actual,
          *variable,
          *errorMessage));
}

//  bool QQmlJSCodeGenerator::generateContentPointerCheck(const
//      QQmlJSScope::ConstPtr &required, QQmlJSRegisterContent actual, const
//      QString &variable, const QString &errorMessage)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator27generateContentPointerCheckERK22QDeferredSharedPointerIK11QQmlJSScopeE21QQmlJSRegisterContentRK7QStringS9_(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *required,
    const QQmlJSRegisterContent *actual,
    const QString *variable,
    const QString *errorMessage) {
  return self->generateContentPointerCheck(
      *required,
      *actual,
      *variable,
      *errorMessage);
}

//  QString QQmlJSCodeGenerator::generateCallConstructor(const
//      QQmlJSMetaMethod &ctor, const QList<QQmlJSRegisterContent>
//      &argumentTypes, const QStringList &arguments, const QString
//      &metaType, const QString &metaObject)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator23generateCallConstructorERK16QQmlJSMetaMethodRK5QListI21QQmlJSRegisterContentERKS3_I7QStringERKS8_SD_(
    QQmlJSCodeGenerator *self,
    const QQmlJSMetaMethod *ctor,
    const QList<QQmlJSRegisterContent> *argumentTypes,
    const QList<QString> *arguments,
    const QString *metaType,
    const QString *metaObject) {
  return new QString(
      self->generateCallConstructor(
          *ctor,
          *argumentTypes,
          *arguments,
          *metaType,
          *metaObject));
}

//  QString QQmlJSCodeGenerator::generateVariantMapGetLookup(const QString
//      &map, const int nameIndex)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator27generateVariantMapGetLookupERK7QStringi(
    QQmlJSCodeGenerator *self,
    const QString *map,
    int nameIndex) {
  return new QString(self->generateVariantMapGetLookup(*map, nameIndex));
}

//  QString QQmlJSCodeGenerator::generateVariantMapSetLookup(const QString
//      &map, const int nameIndex, const QQmlJSScope::ConstPtr &property,
//      const QString &variableIn)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QQmlJSCodeGenerator27generateVariantMapSetLookupERK7QStringiRK22QDeferredSharedPointerIK11QQmlJSScopeES2_(
    QQmlJSCodeGenerator *self,
    const QString *map,
    int nameIndex,
    const QQmlJSScope::ConstPtr *property,
    const QString *variableIn) {
  return new QString(
      self->generateVariantMapSetLookup(
          *map,
          nameIndex,
          *property,
          *variableIn));
}

//  QQmlJSRegisterContent
//      QQmlJSCodeGenerator::originalType(QQmlJSRegisterContent tracked)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN19QQmlJSCodeGenerator12originalTypeE21QQmlJSRegisterContent(
    QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *tracked) {
  return new QQmlJSRegisterContent(self->originalType(*tracked));
}

//  QQmlJSMetaProperty QQmlJSCodeGenerator::originalProperty(const
//      QQmlJSRegisterContent &reg) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaProperty *ritual_ZNK19QQmlJSCodeGenerator16originalPropertyERK21QQmlJSRegisterContent(
    const QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *reg) {
  return new QQmlJSMetaProperty(self->originalProperty(*reg));
}

//  QQmlJSMetaMethod QQmlJSCodeGenerator::originalMethod(const
//      QQmlJSRegisterContent &reg) const
extern "C" Q_DECL_EXPORT
QQmlJSMetaMethod *ritual_ZNK19QQmlJSCodeGenerator14originalMethodERK21QQmlJSRegisterContent(
    const QQmlJSCodeGenerator *self,
    const QQmlJSRegisterContent *reg) {
  return new QQmlJSMetaMethod(self->originalMethod(*reg));
}

//  QQmlJSRegisterContent QQmlJSCodeGenerator::literalType(const
//      QQmlJSScope::ConstPtr &contained)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN19QQmlJSCodeGenerator11literalTypeERK22QDeferredSharedPointerIK11QQmlJSScopeE(
    QQmlJSCodeGenerator *self,
    const QQmlJSScope::ConstPtr *contained) {
  return new QQmlJSRegisterContent(self->literalType(*contained));
}

//  bool QQmlJSCodeGenerator::isRegisterAffectedBySideEffects(int
//      registerIndex)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator31isRegisterAffectedBySideEffectsEi(
    QQmlJSCodeGenerator *self,
    int registerIndex) {
  return self->isRegisterAffectedBySideEffects(registerIndex);
}

//  a Python function taken by a CuteQQmlJSCodeGenerator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSCodeGenerator(
    QQmlJSCodeGenerator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSCodeGenerator *>(self)->take(key, call);
}

//  void QQmlJSCodeGenerator::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_RetEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Ret();
}

//  void QQmlJSCodeGenerator::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_DebugEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Debug();
}

//  void QQmlJSCodeGenerator::generate_LoadConst(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadConstEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadConst(
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadZeroEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadZero();
}

//  void QQmlJSCodeGenerator::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadTrueEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadTrue();
}

//  void QQmlJSCodeGenerator::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadFalseEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadFalse();
}

//  void QQmlJSCodeGenerator::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadNullEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadNull();
}

//  void QQmlJSCodeGenerator::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator22generate_LoadUndefinedEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadUndefined();
}

//  void QQmlJSCodeGenerator::generate_LoadInt(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator16generate_LoadIntEi(
    QQmlJSCodeGenerator *self,
    int value) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadInt(
      value);
}

//  void QQmlJSCodeGenerator::generate_MoveConst(int constIndex, int
//      destTemp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_MoveConstEii(
    QQmlJSCodeGenerator *self,
    int constIndex,
    int destTemp) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_MoveConst(
      constIndex,
      destTemp);
}

//  void QQmlJSCodeGenerator::generate_LoadReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator16generate_LoadRegEi(
    QQmlJSCodeGenerator *self,
    int reg) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadReg(
      reg);
}

//  void QQmlJSCodeGenerator::generate_StoreReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_StoreRegEi(
    QQmlJSCodeGenerator *self,
    int reg) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreReg(
      reg);
}

//  void QQmlJSCodeGenerator::generate_MoveReg(int srcReg, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator16generate_MoveRegEii(
    QQmlJSCodeGenerator *self,
    int srcReg,
    int destReg) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_MoveReg(
      srcReg,
      destReg);
}

//  void QQmlJSCodeGenerator::generate_LoadImport(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_LoadImportEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadImport(
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_LoadLocalEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadLocal(
      index);
}

//  void QQmlJSCodeGenerator::generate_StoreLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_StoreLocalEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreLocal(
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator24generate_LoadScopedLocalEii(
    QQmlJSCodeGenerator *self,
    int scope,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadScopedLocal(
      scope,
      index);
}

//  void QQmlJSCodeGenerator::generate_StoreScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_StoreScopedLocalEii(
    QQmlJSCodeGenerator *self,
    int scope,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreScopedLocal(
      scope,
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadRuntimeString(int stringId)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_LoadRuntimeStringEi(
    QQmlJSCodeGenerator *self,
    int stringId) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadRuntimeString(
      stringId);
}

//  void QQmlJSCodeGenerator::generate_MoveRegExp(int regExpId, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_MoveRegExpEii(
    QQmlJSCodeGenerator *self,
    int regExpId,
    int destReg) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_MoveRegExp(
      regExpId,
      destReg);
}

//  void QQmlJSCodeGenerator::generate_LoadClosure(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_LoadClosureEi(
    QQmlJSCodeGenerator *self,
    int value) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadClosure(
      value);
}

//  void QQmlJSCodeGenerator::generate_LoadName(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_LoadNameEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadName(
      nameIndex);
}

//  void QQmlJSCodeGenerator::generate_LoadGlobalLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_LoadGlobalLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadGlobalLookup(
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadQmlContextPropertyLookup(
      index);
}

//  void QQmlJSCodeGenerator::generate_StoreNameSloppy(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator24generate_StoreNameSloppyEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreNameSloppy(
      nameIndex);
}

//  void QQmlJSCodeGenerator::generate_StoreNameStrict(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator24generate_StoreNameStrictEi(
    QQmlJSCodeGenerator *self,
    int name) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreNameStrict(
      name);
}

//  void QQmlJSCodeGenerator::generate_LoadElement(int base)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_LoadElementEi(
    QQmlJSCodeGenerator *self,
    int base) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadElement(
      base);
}

//  void QQmlJSCodeGenerator::generate_StoreElement(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_StoreElementEii(
    QQmlJSCodeGenerator *self,
    int base,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreElement(
      base,
      index);
}

//  void QQmlJSCodeGenerator::generate_LoadProperty(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_LoadPropertyEi(
    QQmlJSCodeGenerator *self,
    int nameIndex) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadProperty(
      nameIndex);
}

//  void QQmlJSCodeGenerator::generate_LoadOptionalProperty(int name, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator29generate_LoadOptionalPropertyEii(
    QQmlJSCodeGenerator *self,
    int name,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadOptionalProperty(
      name,
      offset);
}

//  void QQmlJSCodeGenerator::generate_GetLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_GetLookupEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_GetLookup(
      index);
}

//  void QQmlJSCodeGenerator::generate_GetOptionalLookup(int index, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_GetOptionalLookupEii(
    QQmlJSCodeGenerator *self,
    int index,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_GetOptionalLookup(
      index,
      offset);
}

//  void QQmlJSCodeGenerator::generate_StoreProperty(int name, int baseReg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator22generate_StorePropertyEii(
    QQmlJSCodeGenerator *self,
    int name,
    int baseReg) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreProperty(
      name,
      baseReg);
}

//  void QQmlJSCodeGenerator::generate_SetLookup(int index, int base)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_SetLookupEii(
    QQmlJSCodeGenerator *self,
    int index,
    int base) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_SetLookup(
      index,
      base);
}

//  void QQmlJSCodeGenerator::generate_LoadSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_LoadSuperPropertyEi(
    QQmlJSCodeGenerator *self,
    int property) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadSuperProperty(
      property);
}

//  void QQmlJSCodeGenerator::generate_StoreSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator27generate_StoreSuperPropertyEi(
    QQmlJSCodeGenerator *self,
    int property) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_StoreSuperProperty(
      property);
}

//  void QQmlJSCodeGenerator::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_YieldEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Yield();
}

//  void QQmlJSCodeGenerator::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_YieldStarEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_YieldStar();
}

//  void QQmlJSCodeGenerator::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator15generate_ResumeEi(
    QQmlJSCodeGenerator *self,
    int a0) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Resume(
      a0);
}

//  void QQmlJSCodeGenerator::generate_CallValue(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_CallValueEiii(
    QQmlJSCodeGenerator *self,
    int name,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallValue(
      name,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallWithReceiver(int name, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_CallWithReceiverEiiii(
    QQmlJSCodeGenerator *self,
    int name,
    int thisObject,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallWithReceiver(
      name,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallProperty(int name, int base, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_CallPropertyEiiii(
    QQmlJSCodeGenerator *self,
    int name,
    int base,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallProperty(
      name,
      base,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallPropertyLookup(int lookupIndex,
//      int base, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator27generate_CallPropertyLookupEiiii(
    QQmlJSCodeGenerator *self,
    int lookupIndex,
    int base,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallPropertyLookup(
      lookupIndex,
      base,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallName(int name, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_CallNameEiii(
    QQmlJSCodeGenerator *self,
    int name,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallName(
      name,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallPossiblyDirectEval(int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator31generate_CallPossiblyDirectEvalEii(
    QQmlJSCodeGenerator *self,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallPossiblyDirectEval(
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallGlobalLookup(int index, int argc,
//      int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_CallGlobalLookupEiii(
    QQmlJSCodeGenerator *self,
    int index,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallGlobalLookup(
      index,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(int
//      index, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSCodeGenerator *self,
    int index,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallQmlContextPropertyLookup(
      index,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_CallWithSpread(int func, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_CallWithSpreadEiiii(
    QQmlJSCodeGenerator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CallWithSpread(
      func,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_TailCall(int func, int thisObject, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_TailCallEiiii(
    QQmlJSCodeGenerator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_TailCall(
      func,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_Construct(int func, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_ConstructEiii(
    QQmlJSCodeGenerator *self,
    int func,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Construct(
      func,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_ConstructWithSpread(int func, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator28generate_ConstructWithSpreadEiii(
    QQmlJSCodeGenerator *self,
    int func,
    int argc,
    int argv) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ConstructWithSpread(
      func,
      argc,
      argv);
}

//  void QQmlJSCodeGenerator::generate_SetUnwindHandler(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_SetUnwindHandlerEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_SetUnwindHandler(
      offset);
}

//  void QQmlJSCodeGenerator::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_UnwindDispatchEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UnwindDispatch();
}

//  void QQmlJSCodeGenerator::generate_UnwindToLabel(int level, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator22generate_UnwindToLabelEii(
    QQmlJSCodeGenerator *self,
    int level,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UnwindToLabel(
      level,
      offset);
}

//  void QQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator30generate_DeadTemporalZoneCheckEi(
    QQmlJSCodeGenerator *self,
    int name) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DeadTemporalZoneCheck(
      name);
}

//  void QQmlJSCodeGenerator::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_ThrowExceptionEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ThrowException();
}

//  void QQmlJSCodeGenerator::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_GetExceptionEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_GetException();
}

//  void QQmlJSCodeGenerator::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_SetExceptionEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_SetException();
}

//  void QQmlJSCodeGenerator::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_CreateCallContextEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CreateCallContext();
}

//  void QQmlJSCodeGenerator::generate_PushCatchContext(int index, int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_PushCatchContextEii(
    QQmlJSCodeGenerator *self,
    int index,
    int name) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PushCatchContext(
      index,
      name);
}

//  void QQmlJSCodeGenerator::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator24generate_PushWithContextEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PushWithContext();
}

//  void QQmlJSCodeGenerator::generate_PushBlockContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_PushBlockContextEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PushBlockContext(
      index);
}

//  void QQmlJSCodeGenerator::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_CloneBlockContextEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CloneBlockContext();
}

//  void QQmlJSCodeGenerator::generate_PushScriptContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_PushScriptContextEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PushScriptContext(
      index);
}

//  void QQmlJSCodeGenerator::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_PopScriptContextEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PopScriptContext();
}

//  void QQmlJSCodeGenerator::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_PopContextEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_PopContext();
}

//  void QQmlJSCodeGenerator::generate_GetIterator(int iterator)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_GetIteratorEi(
    QQmlJSCodeGenerator *self,
    int iterator) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_GetIterator(
      iterator);
}

//  void QQmlJSCodeGenerator::generate_IteratorNext(int value, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator21generate_IteratorNextEii(
    QQmlJSCodeGenerator *self,
    int value,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_IteratorNext(
      value,
      offset);
}

//  void QQmlJSCodeGenerator::generate_IteratorNextForYieldStar(int iterator,
//      int object, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator33generate_IteratorNextForYieldStarEiii(
    QQmlJSCodeGenerator *self,
    int iterator,
    int object,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_IteratorNextForYieldStar(
      iterator,
      object,
      offset);
}

//  void QQmlJSCodeGenerator::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator22generate_IteratorCloseEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_IteratorClose();
}

//  void QQmlJSCodeGenerator::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator31generate_DestructureRestElementEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DestructureRestElement();
}

//  void QQmlJSCodeGenerator::generate_DeleteProperty(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_DeletePropertyEii(
    QQmlJSCodeGenerator *self,
    int base,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DeleteProperty(
      base,
      index);
}

//  void QQmlJSCodeGenerator::generate_DeleteName(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_DeleteNameEi(
    QQmlJSCodeGenerator *self,
    int name) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DeleteName(
      name);
}

//  void QQmlJSCodeGenerator::generate_TypeofName(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_TypeofNameEi(
    QQmlJSCodeGenerator *self,
    int name) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_TypeofName(
      name);
}

//  void QQmlJSCodeGenerator::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_TypeofValueEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_TypeofValue();
}

//  void QQmlJSCodeGenerator::generate_DeclareVar(int varName, int
//      isDeletable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_DeclareVarEii(
    QQmlJSCodeGenerator *self,
    int varName,
    int isDeletable) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DeclareVar(
      varName,
      isDeletable);
}

//  void QQmlJSCodeGenerator::generate_DefineArray(int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_DefineArrayEii(
    QQmlJSCodeGenerator *self,
    int argc,
    int args) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DefineArray(
      argc,
      args);
}

//  void QQmlJSCodeGenerator::generate_DefineObjectLiteral(int
//      internalClassId, int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator28generate_DefineObjectLiteralEiii(
    QQmlJSCodeGenerator *self,
    int internalClassId,
    int argc,
    int args) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_DefineObjectLiteral(
      internalClassId,
      argc,
      args);
}

//  void QQmlJSCodeGenerator::generate_CreateClass(int classIndex, int
//      heritage, int computedNames)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_CreateClassEiii(
    QQmlJSCodeGenerator *self,
    int classIndex,
    int heritage,
    int computedNames) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CreateClass(
      classIndex,
      heritage,
      computedNames);
}

//  void QQmlJSCodeGenerator::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator36generate_CreateMappedArgumentsObjectEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CreateMappedArgumentsObject();
}

//  void QQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSCodeGenerator::generate_CreateRestParameter(int argIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator28generate_CreateRestParameterEi(
    QQmlJSCodeGenerator *self,
    int argIndex) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CreateRestParameter(
      argIndex);
}

//  void QQmlJSCodeGenerator::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator28generate_ConvertThisToObjectEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ConvertThisToObject();
}

//  void QQmlJSCodeGenerator::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator29generate_LoadSuperConstructorEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_LoadSuperConstructor();
}

//  void QQmlJSCodeGenerator::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_ToObjectEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ToObject();
}

//  void QQmlJSCodeGenerator::generate_Jump(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator13generate_JumpEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Jump(
      offset);
}

//  void QQmlJSCodeGenerator::generate_JumpTrue(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_JumpTrueEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_JumpTrue(
      offset);
}

//  void QQmlJSCodeGenerator::generate_JumpFalse(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_JumpFalseEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_JumpFalse(
      offset);
}

//  void QQmlJSCodeGenerator::generate_JumpNoException(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator24generate_JumpNoExceptionEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_JumpNoException(
      offset);
}

//  void QQmlJSCodeGenerator::generate_JumpNotUndefined(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator25generate_JumpNotUndefinedEi(
    QQmlJSCodeGenerator *self,
    int offset) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_JumpNotUndefined(
      offset);
}

//  void QQmlJSCodeGenerator::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_CheckExceptionEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CheckException();
}

//  void QQmlJSCodeGenerator::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_CmpEqNullEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpEqNull();
}

//  void QQmlJSCodeGenerator::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_CmpNeNullEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpNeNull();
}

//  void QQmlJSCodeGenerator::generate_CmpEqInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_CmpEqIntEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpEqInt(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpNeInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_CmpNeIntEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpNeInt(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpEq(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpEqEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpEq(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpNe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpNeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpNe(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpGt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpGtEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpGt(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpGe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpGeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpGe(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpLt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpLtEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpLt(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpLe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpLeEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpLe(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpStrictEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator23generate_CmpStrictEqualEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpStrictEqual(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpStrictNotEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_CmpStrictNotEqualEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpStrictNotEqual(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpIn(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_CmpInEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpIn(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_CmpInstanceOf(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator22generate_CmpInstanceOfEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_CmpInstanceOf(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_As(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator11generate_AsEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_As(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator13generate_UNotEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UNot();
}

//  void QQmlJSCodeGenerator::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_UPlusEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UPlus();
}

//  void QQmlJSCodeGenerator::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator15generate_UMinusEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UMinus();
}

//  void QQmlJSCodeGenerator::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator15generate_UComplEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UCompl();
}

//  void QQmlJSCodeGenerator::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_IncrementEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Increment();
}

//  void QQmlJSCodeGenerator::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_DecrementEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Decrement();
}

//  void QQmlJSCodeGenerator::generate_Add(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_AddEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Add(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_BitAnd(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator15generate_BitAndEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitAnd(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_BitOr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14generate_BitOrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitOr(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_BitXor(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator15generate_BitXorEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitXor(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_UShr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator13generate_UShrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UShr(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Shr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_ShrEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Shr(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Shl(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_ShlEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Shl(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_BitAndConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_BitAndConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitAndConst(
      rhs);
}

//  void QQmlJSCodeGenerator::generate_BitOrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator19generate_BitOrConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitOrConst(
      rhs);
}

//  void QQmlJSCodeGenerator::generate_BitXorConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator20generate_BitXorConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_BitXorConst(
      rhs);
}

//  void QQmlJSCodeGenerator::generate_UShrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator18generate_UShrConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_UShrConst(
      rhs);
}

//  void QQmlJSCodeGenerator::generate_ShrConst(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_ShrConstEi(
    QQmlJSCodeGenerator *self,
    int value) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ShrConst(
      value);
}

//  void QQmlJSCodeGenerator::generate_ShlConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator17generate_ShlConstEi(
    QQmlJSCodeGenerator *self,
    int rhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ShlConst(
      rhs);
}

//  void QQmlJSCodeGenerator::generate_Exp(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_ExpEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Exp(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Mul(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_MulEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Mul(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Div(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_DivEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Div(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Mod(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_ModEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Mod(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_Sub(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator12generate_SubEi(
    QQmlJSCodeGenerator *self,
    int lhs) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_Sub(
      lhs);
}

//  void QQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(int
//      firstReg, int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSCodeGenerator *self,
    int firstReg,
    int count) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_InitializeBlockDeadTemporalZone(
      firstReg,
      count);
}

//  void QQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSCodeGenerator *self) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSCodeGenerator::generate_GetTemplateObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator26generate_GetTemplateObjectEi(
    QQmlJSCodeGenerator *self,
    int index) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::generate_GetTemplateObject(
      index);
}

//  void QQmlJSCodeGenerator::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSCodeGenerator14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSCodeGenerator *self,
    QV4::Moth::Instr::Type a0) {
  static_cast<OwnQQmlJSCodeGenerator *>(self)->OwnQQmlJSCodeGenerator::endInstruction(
      a0);
}

//  a LookupSignatures a ritual of QQmlJSCodeGenerator gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QQmlJSCodeGenerator__LookupSignatures(
    LookupSignatures *self) {
  delete self;
}

//  bool QQmlJSCodeGenerator::reject<bool>(const QString &thing)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QQmlJSCodeGenerator6rejectIbEET_RK7QString(
    QQmlJSCodeGenerator *self,
    const QString *thing) {
  return self->reject<bool>(*thing);
}

//  int QQmlJSCodeGenerator::reject<int>(const QString &thing)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QQmlJSCodeGenerator6rejectIiEET_RK7QString(
    QQmlJSCodeGenerator *self,
    const QString *thing) {
  return self->reject<int>(*thing);
}

//  QString QQmlJSCodeGenerator::reject<QString>(const QString &thing)
extern "C" Q_DECL_EXPORT
QString * ritual_ZN19QQmlJSCodeGenerator6rejectI7QStringEET_RKS1_(
    QQmlJSCodeGenerator *self,
    const QString *thing) {
  return new QString(self->reject<QString>(*thing));
}
