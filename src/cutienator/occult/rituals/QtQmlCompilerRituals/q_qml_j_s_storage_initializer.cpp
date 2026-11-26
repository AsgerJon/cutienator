//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsstorageinitializer_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsstorageinitializer_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  Only a class built on QQmlJSStorageInitializer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSStorageInitializer : QQmlJSStorageInitializer {
  using QQmlJSStorageInitializer::endInstruction;
};

//  A QQmlJSStorageInitializer that Python can take functions over in. Every QQmlJSStorageInitializer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSStorageInitializerCall0)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall1)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall2)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall3)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall4)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall5)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall6)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall7)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall8)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall9)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall10)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall11)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall12)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall13)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall14)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall15)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall16)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall17)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall18)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall19)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall20)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall21)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall22)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall23)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall24)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall25)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall26)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall27)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall28)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall29)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall30)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall31)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall32)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall33)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall34)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall35)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall36)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall37)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall38)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall39)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall40)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall41)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall42)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall43)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall44)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall45)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall46)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall47)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall48)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall49)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall50)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall51)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall52)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall53)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall54)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall55)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall56)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall57)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall58)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall59)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall60)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall61)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall62)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall63)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall64)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall65)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall66)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall67)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall68)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall69)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall70)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall71)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall72)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall73)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall74)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall75)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall76)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall77)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall78)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall79)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall80)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall81)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall82)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall83)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall84)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall85)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall86)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall87)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall88)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall89)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall90)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall91)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall92)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall93)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall94)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall95)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall96)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall97)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall98)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall99)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall100)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall101)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall102)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall103)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall104)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall105)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall106)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall107)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall108)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall109)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall110)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall111)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall112)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall113)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall114)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall115)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall116)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall117)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall118)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall119)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall120)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall121)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall122)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall123)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall124)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall125)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall126)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall127)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall128)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall129)(const void *, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall130)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall131)(const void *, int, int, int *);
typedef void (*CuteQQmlJSStorageInitializerCall132)(const void *, int *);
typedef void (*CuteQQmlJSStorageInitializerCall133)(const void *, int *);
class CuteQQmlJSStorageInitializer : public QQmlJSStorageInitializer {
public:
  using QQmlJSStorageInitializer::QQmlJSStorageInitializer;
  void *taken[134] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14endInstructionENS0_5Instr4TypeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_AddEi")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler11generate_AsEi")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitAndEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitAndConstEi")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_BitOrEi")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_BitOrConstEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_BitXorEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_BitXorConstEi")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallGlobalLookupEiii")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CallNameEiii")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_CallPossiblyDirectEvalEii")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_CallPropertyEiiii")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_CallPropertyLookupEiiii")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_CallQmlContextPropertyLookupEiii")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CallValueEiii")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_CallWithReceiverEiiii")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CallWithSpreadEiiii")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CheckExceptionEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CloneBlockContextEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpEqEi")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpEqIntEi")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpEqNullEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGeEi")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpGtEi")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpInEi")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_CmpInstanceOfEi")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLeEi")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpLtEi")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_CmpNeEi")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_CmpNeIntEi")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_CmpNeNullEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_CmpStrictEqualEi")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CmpStrictNotEqualEi")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_ConstructEiii")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConstructWithSpreadEiii")) {
      taken[35] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_ConvertThisToObjectEv")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_CreateCallContextEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_CreateClassEiii")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler36generate_CreateMappedArgumentsObjectEv")) {
      taken[39] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_CreateRestParameterEi")) {
      taken[40] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler38generate_CreateUnmappedArgumentsObjectEv")) {
      taken[41] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler30generate_DeadTemporalZoneCheckEi")) {
      taken[42] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_DebugEv")) {
      taken[43] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeclareVarEii")) {
      taken[44] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_DecrementEv")) {
      taken[45] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_DefineArrayEii")) {
      taken[46] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler28generate_DefineObjectLiteralEiii")) {
      taken[47] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_DeleteNameEi")) {
      taken[48] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_DeletePropertyEii")) {
      taken[49] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_DestructureRestElementEv")) {
      taken[50] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_DivEi")) {
      taken[51] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ExpEi")) {
      taken[52] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_GetExceptionEv")) {
      taken[53] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_GetIteratorEi")) {
      taken[54] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_GetLookupEi")) {
      taken[55] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetOptionalLookupEii")) {
      taken[56] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_GetTemplateObjectEi")) {
      taken[57] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_IncrementEv")) {
      taken[58] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler40generate_InitializeBlockDeadTemporalZoneEii")) {
      taken[59] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_IteratorCloseEv")) {
      taken[60] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_IteratorNextEii")) {
      taken[61] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler33generate_IteratorNextForYieldStarEiii")) {
      taken[62] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_JumpEi")) {
      taken[63] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_JumpFalseEi")) {
      taken[64] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_JumpNoExceptionEi")) {
      taken[65] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_JumpNotUndefinedEi")) {
      taken[66] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_JumpTrueEi")) {
      taken[67] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadClosureEi")) {
      taken[68] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadConstEi")) {
      taken[69] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_LoadElementEi")) {
      taken[70] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadFalseEv")) {
      taken[71] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_LoadGlobalLookupEi")) {
      taken[72] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_LoadImportEi")) {
      taken[73] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadIntEi")) {
      taken[74] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_LoadLocalEi")) {
      taken[75] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNameEi")) {
      taken[76] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadNullEv")) {
      taken[77] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadOptionalPropertyEii")) {
      taken[78] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_LoadPropertyEi")) {
      taken[79] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler37generate_LoadQmlContextPropertyLookupEi")) {
      taken[80] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_LoadRegEi")) {
      taken[81] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadRuntimeStringEi")) {
      taken[82] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_LoadScopedLocalEii")) {
      taken[83] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler29generate_LoadSuperConstructorEv")) {
      taken[84] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_LoadSuperPropertyEi")) {
      taken[85] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadTrueEv")) {
      taken[86] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_LoadUndefinedEv")) {
      taken[87] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_LoadZeroEv")) {
      taken[88] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ModEi")) {
      taken[89] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_MoveConstEii")) {
      taken[90] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler16generate_MoveRegEii")) {
      taken[91] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_MoveRegExpEii")) {
      taken[92] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_MulEi")) {
      taken[93] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_PopContextEv")) {
      taken[94] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PopScriptContextEv")) {
      taken[95] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushBlockContextEi")) {
      taken[96] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_PushCatchContextEii")) {
      taken[97] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler26generate_PushScriptContextEi")) {
      taken[98] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_PushWithContextEv")) {
      taken[99] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_ResumeEi")) {
      taken[100] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_RetEv")) {
      taken[101] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_SetExceptionEv")) {
      taken[102] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_SetLookupEii")) {
      taken[103] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_SetUnwindHandlerEi")) {
      taken[104] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShlEi")) {
      taken[105] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShlConstEi")) {
      taken[106] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_ShrEi")) {
      taken[107] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ShrConstEi")) {
      taken[108] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler21generate_StoreElementEii")) {
      taken[109] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_StoreLocalEi")) {
      taken[110] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameSloppyEi")) {
      taken[111] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler24generate_StoreNameStrictEi")) {
      taken[112] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_StorePropertyEii")) {
      taken[113] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_StoreRegEi")) {
      taken[114] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler25generate_StoreScopedLocalEii")) {
      taken[115] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler27generate_StoreSuperPropertyEi")) {
      taken[116] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler12generate_SubEi")) {
      taken[117] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_TailCallEiiii")) {
      taken[118] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_ThrowExceptionEv")) {
      taken[119] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler31generate_ThrowOnNullOrUndefinedEv")) {
      taken[120] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler17generate_ToObjectEv")) {
      taken[121] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler19generate_TypeofNameEi")) {
      taken[122] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler20generate_TypeofValueEv")) {
      taken[123] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UComplEv")) {
      taken[124] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler15generate_UMinusEv")) {
      taken[125] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UNotEv")) {
      taken[126] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_UPlusEv")) {
      taken[127] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler13generate_UShrEi")) {
      taken[128] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_UShrConstEi")) {
      taken[129] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler23generate_UnwindDispatchEv")) {
      taken[130] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler22generate_UnwindToLabelEii")) {
      taken[131] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler14generate_YieldEv")) {
      taken[132] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN3QV44Moth15ByteCodeHandler18generate_YieldStarEv")) {
      taken[133] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJSStorageInitializer::endInstruction(QV4::Moth::Instr::Type
  //      a0)
  void endInstruction(QV4::Moth::Instr::Type a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall0 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlJSStorageInitializer::endInstruction(a0);
  }

  //  void QQmlJSCompilePass::generate_Add(int a0)
  void generate_Add(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall1 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Add(a0);
  }

  //  void QQmlJSCompilePass::generate_As(int a0)
  void generate_As(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall2 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_As(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAnd(int a0)
  void generate_BitAnd(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall3 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAnd(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAndConst(int a0)
  void generate_BitAndConst(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall4 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAndConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOr(int a0)
  void generate_BitOr(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall5 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOr(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOrConst(int a0)
  void generate_BitOrConst(int a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall6 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXor(int a0)
  void generate_BitXor(int a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall7 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitXor(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXorConst(int a0)
  void generate_BitXorConst(int a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall8 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitXorConst(a0);
  }

  //  void QQmlJSCompilePass::generate_CallGlobalLookup(int a0, int a1, int
  //      a2)
  void generate_CallGlobalLookup(int a0, int a1, int a2) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall9 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall9>(taken[9]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallGlobalLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
  void generate_CallName(int a0, int a1, int a2) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall10 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall10>(taken[10]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallName(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallPossiblyDirectEval(int a0, int
  //      a1)
  void generate_CallPossiblyDirectEval(int a0, int a1) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall11 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall11>(taken[11]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallPossiblyDirectEval(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_CallProperty(int a0, int a1, int a2,
  //      int a3)
  void generate_CallProperty(int a0, int a1, int a2, int a3) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall12 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall12>(taken[12]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallProperty(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CallPropertyLookup(int a0, int a1,
  //      int a2, int a3)
  void generate_CallPropertyLookup(int a0, int a1, int a2, int a3) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall13 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall13>(taken[13]);
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
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall14 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall14>(taken[14]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
  void generate_CallValue(int a0, int a1, int a2) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall15 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall15>(taken[15]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallValue(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallWithReceiver(int a0, int a1, int
  //      a2, int a3)
  void generate_CallWithReceiver(int a0, int a1, int a2, int a3) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall16 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall16>(taken[16]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallWithReceiver(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CallWithSpread(int a0, int a1, int
  //      a2, int a3)
  void generate_CallWithSpread(int a0, int a1, int a2, int a3) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall17 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall17>(taken[17]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallWithSpread(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CheckException()
  void generate_CheckException() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall18 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CheckException();
  }

  //  void QQmlJSCompilePass::generate_CloneBlockContext()
  void generate_CloneBlockContext() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall19 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CloneBlockContext();
  }

  //  void QQmlJSCompilePass::generate_CmpEq(int a0)
  void generate_CmpEq(int a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall20 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEq(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
  void generate_CmpEqInt(int a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall21 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqNull()
  void generate_CmpEqNull() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall22 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqNull();
  }

  //  void QQmlJSCompilePass::generate_CmpGe(int a0)
  void generate_CmpGe(int a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall23 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpGt(int a0)
  void generate_CmpGt(int a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall24 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpIn(int a0)
  void generate_CmpIn(int a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall25 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpIn(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
  void generate_CmpInstanceOf(int a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall26 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpInstanceOf(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLe(int a0)
  void generate_CmpLe(int a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall27 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLt(int a0)
  void generate_CmpLt(int a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall28 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNe(int a0)
  void generate_CmpNe(int a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall29 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
  void generate_CmpNeInt(int a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall30 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeNull()
  void generate_CmpNeNull() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall31 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeNull();
  }

  //  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
  void generate_CmpStrictEqual(int a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall32 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
  void generate_CmpStrictNotEqual(int a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall33 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictNotEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
  void generate_Construct(int a0, int a1, int a2) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall34 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall34>(taken[34]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Construct(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_ConstructWithSpread(int a0, int a1,
  //      int a2)
  void generate_ConstructWithSpread(int a0, int a1, int a2) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall35 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall35>(taken[35]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConstructWithSpread(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_ConvertThisToObject()
  void generate_ConvertThisToObject() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall36 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConvertThisToObject();
  }

  //  void QQmlJSCompilePass::generate_CreateCallContext()
  void generate_CreateCallContext() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall37 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateCallContext();
  }

  //  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
  void generate_CreateClass(int a0, int a1, int a2) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall38 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall38>(taken[38]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateClass(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
  void generate_CreateMappedArgumentsObject() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall39 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateMappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
  void generate_CreateRestParameter(int a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall40 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateRestParameter(a0);
  }

  //  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
  void generate_CreateUnmappedArgumentsObject() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall41 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
  void generate_DeadTemporalZoneCheck(int a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall42 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeadTemporalZoneCheck(a0);
  }

  //  void QQmlJSCompilePass::generate_Debug()
  void generate_Debug() override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall43 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall43>(taken[43]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Debug();
  }

  //  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
  void generate_DeclareVar(int a0, int a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall44 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall44>(taken[44]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeclareVar(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Decrement()
  void generate_Decrement() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall45 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Decrement();
  }

  //  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
  void generate_DefineArray(int a0, int a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall46 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall46>(taken[46]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DefineArray(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_DefineObjectLiteral(int a0, int a1,
  //      int a2)
  void generate_DefineObjectLiteral(int a0, int a1, int a2) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall47 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall47>(taken[47]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DefineObjectLiteral(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_DeleteName(int a0)
  void generate_DeleteName(int a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall48 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall48>(taken[48]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteName(a0);
  }

  //  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
  void generate_DeleteProperty(int a0, int a1) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall49 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall49>(taken[49]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_DestructureRestElement()
  void generate_DestructureRestElement() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall50 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DestructureRestElement();
  }

  //  void QQmlJSCompilePass::generate_Div(int a0)
  void generate_Div(int a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall51 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Div(a0);
  }

  //  void QQmlJSCompilePass::generate_Exp(int a0)
  void generate_Exp(int a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall52 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall52>(taken[52]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Exp(a0);
  }

  //  void QQmlJSCompilePass::generate_GetException()
  void generate_GetException() override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall53 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetException();
  }

  //  void QQmlJSCompilePass::generate_GetIterator(int a0)
  void generate_GetIterator(int a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall54 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetIterator(a0);
  }

  //  void QQmlJSCompilePass::generate_GetLookup(int a0)
  void generate_GetLookup(int a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall55 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
  void generate_GetOptionalLookup(int a0, int a1) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall56 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall56>(taken[56]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetOptionalLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
  void generate_GetTemplateObject(int a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall57 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetTemplateObject(a0);
  }

  //  void QQmlJSCompilePass::generate_Increment()
  void generate_Increment() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall58 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall58>(taken[58]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Increment();
  }

  //  void QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(int
  //      a0, int a1)
  void generate_InitializeBlockDeadTemporalZone(int a0, int a1) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall59 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall59>(taken[59]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_IteratorClose()
  void generate_IteratorClose() override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall60 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall60>(taken[60]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorClose();
  }

  //  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
  void generate_IteratorNext(int a0, int a1) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall61 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall61>(taken[61]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorNext(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_IteratorNextForYieldStar(int a0, int
  //      a1, int a2)
  void generate_IteratorNextForYieldStar(int a0, int a1, int a2) override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall62 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall62>(taken[62]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorNextForYieldStar(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_Jump(int a0)
  void generate_Jump(int a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall63 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Jump(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpFalse(int a0)
  void generate_JumpFalse(int a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall64 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpFalse(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNoException(int a0)
  void generate_JumpNoException(int a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall65 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNoException(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
  void generate_JumpNotUndefined(int a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall66 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall66>(taken[66]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNotUndefined(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpTrue(int a0)
  void generate_JumpTrue(int a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall67 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpTrue(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadClosure(int a0)
  void generate_LoadClosure(int a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall68 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadClosure(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadConst(int a0)
  void generate_LoadConst(int a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall69 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadConst(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadElement(int a0)
  void generate_LoadElement(int a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall70 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall70>(taken[70]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadElement(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadFalse()
  void generate_LoadFalse() override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall71 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall71>(taken[71]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadFalse();
  }

  //  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
  void generate_LoadGlobalLookup(int a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall72 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall72>(taken[72]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadGlobalLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadImport(int a0)
  void generate_LoadImport(int a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall73 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadImport(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadInt(int a0)
  void generate_LoadInt(int a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall74 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadInt(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadLocal(int a0)
  void generate_LoadLocal(int a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall75 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadName(int a0)
  void generate_LoadName(int a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall76 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall76>(taken[76]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadName(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadNull()
  void generate_LoadNull() override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall77 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall77>(taken[77]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadNull();
  }

  //  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
  void generate_LoadOptionalProperty(int a0, int a1) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall78 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall78>(taken[78]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadOptionalProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadProperty(int a0)
  void generate_LoadProperty(int a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall79 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
  void generate_LoadQmlContextPropertyLookup(int a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall80 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadReg(int a0)
  void generate_LoadReg(int a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall81 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadReg(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
  void generate_LoadRuntimeString(int a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall82 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall82>(taken[82]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadRuntimeString(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
  void generate_LoadScopedLocal(int a0, int a1) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall83 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall83>(taken[83]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadSuperConstructor()
  void generate_LoadSuperConstructor() override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall84 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall84>(taken[84]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperConstructor();
  }

  //  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
  void generate_LoadSuperProperty(int a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall85 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadTrue()
  void generate_LoadTrue() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall86 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall86>(taken[86]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadTrue();
  }

  //  void QQmlJSCompilePass::generate_LoadUndefined()
  void generate_LoadUndefined() override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall87 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall87>(taken[87]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadUndefined();
  }

  //  void QQmlJSCompilePass::generate_LoadZero()
  void generate_LoadZero() override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall88 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall88>(taken[88]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadZero();
  }

  //  void QQmlJSCompilePass::generate_Mod(int a0)
  void generate_Mod(int a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall89 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall89>(taken[89]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mod(a0);
  }

  //  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
  void generate_MoveConst(int a0, int a1) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall90 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall90>(taken[90]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveConst(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
  void generate_MoveReg(int a0, int a1) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall91 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall91>(taken[91]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveReg(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
  void generate_MoveRegExp(int a0, int a1) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall92 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall92>(taken[92]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveRegExp(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Mul(int a0)
  void generate_Mul(int a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall93 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall93>(taken[93]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mul(a0);
  }

  //  void QQmlJSCompilePass::generate_PopContext()
  void generate_PopContext() override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall94 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall94>(taken[94]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopContext();
  }

  //  void QQmlJSCompilePass::generate_PopScriptContext()
  void generate_PopScriptContext() override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall95 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall95>(taken[95]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopScriptContext();
  }

  //  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
  void generate_PushBlockContext(int a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall96 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushBlockContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
  void generate_PushCatchContext(int a0, int a1) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall97 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall97>(taken[97]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushCatchContext(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
  void generate_PushScriptContext(int a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall98 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall98>(taken[98]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushScriptContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushWithContext()
  void generate_PushWithContext() override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall99 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall99>(taken[99]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushWithContext();
  }

  //  void QQmlJSCompilePass::generate_Resume(int a0)
  void generate_Resume(int a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall100 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall100>(taken[100]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Resume(a0);
  }

  //  void QQmlJSCompilePass::generate_Ret()
  void generate_Ret() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall101 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Ret();
  }

  //  void QQmlJSCompilePass::generate_SetException()
  void generate_SetException() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall102 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall102>(taken[102]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetException();
  }

  //  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
  void generate_SetLookup(int a0, int a1) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall103 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall103>(taken[103]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
  void generate_SetUnwindHandler(int a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall104 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetUnwindHandler(a0);
  }

  //  void QQmlJSCompilePass::generate_Shl(int a0)
  void generate_Shl(int a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall105 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shl(a0);
  }

  //  void QQmlJSCompilePass::generate_ShlConst(int a0)
  void generate_ShlConst(int a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall106 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShlConst(a0);
  }

  //  void QQmlJSCompilePass::generate_Shr(int a0)
  void generate_Shr(int a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall107 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shr(a0);
  }

  //  void QQmlJSCompilePass::generate_ShrConst(int a0)
  void generate_ShrConst(int a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall108 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
  void generate_StoreElement(int a0, int a1) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall109 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall109>(taken[109]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreElement(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreLocal(int a0)
  void generate_StoreLocal(int a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall110 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
  void generate_StoreNameSloppy(int a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall111 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameSloppy(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
  void generate_StoreNameStrict(int a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall112 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall112>(taken[112]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameStrict(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
  void generate_StoreProperty(int a0, int a1) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall113 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall113>(taken[113]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreReg(int a0)
  void generate_StoreReg(int a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall114 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall114>(taken[114]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreReg(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
  void generate_StoreScopedLocal(int a0, int a1) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall115 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall115>(taken[115]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
  void generate_StoreSuperProperty(int a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall116 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall116>(taken[116]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_Sub(int a0)
  void generate_Sub(int a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall117 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall117>(taken[117]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Sub(a0);
  }

  //  void QQmlJSCompilePass::generate_TailCall(int a0, int a1, int a2, int
  //      a3)
  void generate_TailCall(int a0, int a1, int a2, int a3) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall118 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall118>(taken[118]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TailCall(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_ThrowException()
  void generate_ThrowException() override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall119 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall119>(taken[119]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowException();
  }

  //  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
  void generate_ThrowOnNullOrUndefined() override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall120 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall120>(taken[120]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowOnNullOrUndefined();
  }

  //  void QQmlJSCompilePass::generate_ToObject()
  void generate_ToObject() override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall121 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall121>(taken[121]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ToObject();
  }

  //  void QQmlJSCompilePass::generate_TypeofName(int a0)
  void generate_TypeofName(int a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall122 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall122>(taken[122]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofName(a0);
  }

  //  void QQmlJSCompilePass::generate_TypeofValue()
  void generate_TypeofValue() override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall123 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall123>(taken[123]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofValue();
  }

  //  void QQmlJSCompilePass::generate_UCompl()
  void generate_UCompl() override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall124 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall124>(taken[124]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UCompl();
  }

  //  void QQmlJSCompilePass::generate_UMinus()
  void generate_UMinus() override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall125 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall125>(taken[125]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UMinus();
  }

  //  void QQmlJSCompilePass::generate_UNot()
  void generate_UNot() override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall126 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall126>(taken[126]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UNot();
  }

  //  void QQmlJSCompilePass::generate_UPlus()
  void generate_UPlus() override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall127 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall127>(taken[127]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UPlus();
  }

  //  void QQmlJSCompilePass::generate_UShr(int a0)
  void generate_UShr(int a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall128 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall128>(taken[128]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShr(a0);
  }

  //  void QQmlJSCompilePass::generate_UShrConst(int a0)
  void generate_UShrConst(int a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall129 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_UnwindDispatch()
  void generate_UnwindDispatch() override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall130 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall130>(taken[130]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindDispatch();
  }

  //  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
  void generate_UnwindToLabel(int a0, int a1) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall131 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall131>(taken[131]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindToLabel(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Yield()
  void generate_Yield() override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall132 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall132>(taken[132]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Yield();
  }

  //  void QQmlJSCompilePass::generate_YieldStar()
  void generate_YieldStar() override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSStorageInitializerCall133 call = reinterpret_cast<CuteQQmlJSStorageInitializerCall133>(taken[133]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_YieldStar();
  }
};

//  QQmlJSStorageInitializer::QQmlJSStorageInitializer(const
//      QV4::Compiler::JSUnitGenerator *jsUnitGenerator, const
//      QQmlJSTypeResolver *typeResolver, QQmlJSLogger *logger, const
//      BasicBlocks &basicBlocks, const InstructionAnnotations &annotations)
extern "C" Q_DECL_EXPORT
QQmlJSStorageInitializer *ritual_ZN24QQmlJSStorageInitializerC1EPKN3QV48Compiler15JSUnitGeneratorEPK18QQmlJSTypeResolverP12QQmlJSLoggerRK8QFlatMapIiN17QQmlJSCompilePass10BasicBlockESt4lessIiE5QListIiESF_ISC_EERKSA_IiNSB_21InstructionAnnotationESE_SG_SF_ISL_EE(
    const QV4::Compiler::JSUnitGenerator *jsUnitGenerator,
    const QQmlJSTypeResolver *typeResolver,
    QQmlJSLogger *logger,
    const QQmlJSCompilePass::BasicBlocks *basicBlocks,
    const QQmlJSCompilePass::InstructionAnnotations *annotations) {
  return new CuteQQmlJSStorageInitializer(
      jsUnitGenerator,
      typeResolver,
      logger,
      *basicBlocks,
      *annotations);
}

//  BlocksAndAnnotations QQmlJSStorageInitializer::run(const Function
//      *function)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::BlocksAndAnnotations *ritual_ZN24QQmlJSStorageInitializer3runEPKN17QQmlJSCompilePass8FunctionE(
    QQmlJSStorageInitializer *self,
    const QQmlJSCompilePass::Function *function) {
  return new QQmlJSCompilePass::BlocksAndAnnotations(self->run(function));
}

//  Verdict QQmlJSStorageInitializer::startInstruction(QV4::Moth::Instr::Type
//      a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::ByteCodeHandler::Verdict ritual_ZN24QQmlJSStorageInitializer16startInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSStorageInitializer *self,
    QV4::Moth::Instr::Type a0) {
  return self->startInstruction(a0);
}

//  void QQmlJSStorageInitializer::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlJSStorageInitializer14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSStorageInitializer *self,
    QV4::Moth::Instr::Type a0) {
  self->endInstruction(a0);
}

//  a Python function taken by a CuteQQmlJSStorageInitializer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSStorageInitializer(
    QQmlJSStorageInitializer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSStorageInitializer *>(self)->take(key, call);
}

//  void QQmlJSStorageInitializer::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QQmlJSStorageInitializer14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSStorageInitializer *self,
    QV4::Moth::Instr::Type a0) {
  static_cast<OwnQQmlJSStorageInitializer *>(self)->OwnQQmlJSStorageInitializer::endInstruction(
      a0);
}
