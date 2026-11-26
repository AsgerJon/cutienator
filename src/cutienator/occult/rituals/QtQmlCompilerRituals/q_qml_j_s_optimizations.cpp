//  Written by hand on 2026-11-25 from
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsoptimizations_p.h,
//  Qt 6.12.0, from Qt's source. Kept as it is when the generator runs
//  again.
//  Not written: the constructor, which takes a 'QList' by value (the
//  generator's attempt failed on its type 'InstructionAnnotations',
//  which is 'QQmlJSCompilePass::InstructionAnnotations'), and
//  'removeReadsFromErasedInstructions' and 'eraseDeadStore', whose
//  parameters are iterators of the template 'QFlatMap'.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsoptimizations_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQmlJSOptimizations that Python can take functions over in. Every QQmlJSOptimizations
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSOptimizationsCall0)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall1)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall2)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall3)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall4)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall5)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall6)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall7)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall8)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall9)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall10)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall11)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall12)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall13)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall14)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall15)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall16)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall17)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall18)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall19)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall20)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall21)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall22)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall23)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall24)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall25)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall26)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall27)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall28)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall29)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall30)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall31)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall32)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall33)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall34)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall35)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall36)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall37)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall38)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall39)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall40)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall41)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall42)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall43)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall44)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall45)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall46)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall47)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall48)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall49)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall50)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall51)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall52)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall53)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall54)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall55)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall56)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall57)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall58)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall59)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall60)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall61)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall62)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall63)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall64)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall65)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall66)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall67)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall68)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall69)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall70)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall71)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall72)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall73)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall74)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall75)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall76)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall77)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall78)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall79)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall80)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall81)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall82)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall83)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall84)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall85)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall86)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall87)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall88)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall89)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall90)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall91)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall92)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall93)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall94)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall95)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall96)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall97)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall98)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall99)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall100)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall101)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall102)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall103)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall104)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall105)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall106)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall107)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall108)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall109)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall110)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall111)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall112)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall113)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall114)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall115)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall116)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall117)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall118)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall119)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall120)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall121)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall122)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall123)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall124)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall125)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall126)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall127)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall128)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall129)(const void *, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall130)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall131)(const void *, int, int, int *);
typedef void (*CuteQQmlJSOptimizationsCall132)(const void *, int *);
typedef void (*CuteQQmlJSOptimizationsCall133)(const void *, int *);
class CuteQQmlJSOptimizations : public QQmlJSOptimizations {
public:
  using QQmlJSOptimizations::QQmlJSOptimizations;
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

  //  void QQmlJSOptimizations::endInstruction(QV4::Moth::Instr::Type a0)
  void endInstruction(QV4::Moth::Instr::Type a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall0 call = reinterpret_cast<CuteQQmlJSOptimizationsCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQmlJSOptimizations::endInstruction(a0);
  }

  //  void QQmlJSCompilePass::generate_Add(int a0)
  void generate_Add(int a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall1 call = reinterpret_cast<CuteQQmlJSOptimizationsCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Add(a0);
  }

  //  void QQmlJSCompilePass::generate_As(int a0)
  void generate_As(int a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall2 call = reinterpret_cast<CuteQQmlJSOptimizationsCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_As(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAnd(int a0)
  void generate_BitAnd(int a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall3 call = reinterpret_cast<CuteQQmlJSOptimizationsCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAnd(a0);
  }

  //  void QQmlJSCompilePass::generate_BitAndConst(int a0)
  void generate_BitAndConst(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall4 call = reinterpret_cast<CuteQQmlJSOptimizationsCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitAndConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOr(int a0)
  void generate_BitOr(int a0) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall5 call = reinterpret_cast<CuteQQmlJSOptimizationsCall5>(taken[5]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOr(a0);
  }

  //  void QQmlJSCompilePass::generate_BitOrConst(int a0)
  void generate_BitOrConst(int a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall6 call = reinterpret_cast<CuteQQmlJSOptimizationsCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitOrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXor(int a0)
  void generate_BitXor(int a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall7 call = reinterpret_cast<CuteQQmlJSOptimizationsCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_BitXor(a0);
  }

  //  void QQmlJSCompilePass::generate_BitXorConst(int a0)
  void generate_BitXorConst(int a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall8 call = reinterpret_cast<CuteQQmlJSOptimizationsCall8>(taken[8]);
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
      CuteQQmlJSOptimizationsCall9 call = reinterpret_cast<CuteQQmlJSOptimizationsCall9>(taken[9]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallGlobalLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallName(int a0, int a1, int a2)
  void generate_CallName(int a0, int a1, int a2) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall10 call = reinterpret_cast<CuteQQmlJSOptimizationsCall10>(taken[10]);
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
      CuteQQmlJSOptimizationsCall11 call = reinterpret_cast<CuteQQmlJSOptimizationsCall11>(taken[11]);
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
      CuteQQmlJSOptimizationsCall12 call = reinterpret_cast<CuteQQmlJSOptimizationsCall12>(taken[12]);
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
      CuteQQmlJSOptimizationsCall13 call = reinterpret_cast<CuteQQmlJSOptimizationsCall13>(taken[13]);
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
      CuteQQmlJSOptimizationsCall14 call = reinterpret_cast<CuteQQmlJSOptimizationsCall14>(taken[14]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallQmlContextPropertyLookup(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CallValue(int a0, int a1, int a2)
  void generate_CallValue(int a0, int a1, int a2) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall15 call = reinterpret_cast<CuteQQmlJSOptimizationsCall15>(taken[15]);
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
      CuteQQmlJSOptimizationsCall16 call = reinterpret_cast<CuteQQmlJSOptimizationsCall16>(taken[16]);
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
      CuteQQmlJSOptimizationsCall17 call = reinterpret_cast<CuteQQmlJSOptimizationsCall17>(taken[17]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CallWithSpread(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_CheckException()
  void generate_CheckException() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall18 call = reinterpret_cast<CuteQQmlJSOptimizationsCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CheckException();
  }

  //  void QQmlJSCompilePass::generate_CloneBlockContext()
  void generate_CloneBlockContext() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall19 call = reinterpret_cast<CuteQQmlJSOptimizationsCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CloneBlockContext();
  }

  //  void QQmlJSCompilePass::generate_CmpEq(int a0)
  void generate_CmpEq(int a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall20 call = reinterpret_cast<CuteQQmlJSOptimizationsCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEq(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqInt(int a0)
  void generate_CmpEqInt(int a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall21 call = reinterpret_cast<CuteQQmlJSOptimizationsCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpEqNull()
  void generate_CmpEqNull() override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall22 call = reinterpret_cast<CuteQQmlJSOptimizationsCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpEqNull();
  }

  //  void QQmlJSCompilePass::generate_CmpGe(int a0)
  void generate_CmpGe(int a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall23 call = reinterpret_cast<CuteQQmlJSOptimizationsCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpGt(int a0)
  void generate_CmpGt(int a0) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall24 call = reinterpret_cast<CuteQQmlJSOptimizationsCall24>(taken[24]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpGt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpIn(int a0)
  void generate_CmpIn(int a0) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall25 call = reinterpret_cast<CuteQQmlJSOptimizationsCall25>(taken[25]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpIn(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpInstanceOf(int a0)
  void generate_CmpInstanceOf(int a0) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall26 call = reinterpret_cast<CuteQQmlJSOptimizationsCall26>(taken[26]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpInstanceOf(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLe(int a0)
  void generate_CmpLe(int a0) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall27 call = reinterpret_cast<CuteQQmlJSOptimizationsCall27>(taken[27]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpLt(int a0)
  void generate_CmpLt(int a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall28 call = reinterpret_cast<CuteQQmlJSOptimizationsCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpLt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNe(int a0)
  void generate_CmpNe(int a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall29 call = reinterpret_cast<CuteQQmlJSOptimizationsCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNe(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeInt(int a0)
  void generate_CmpNeInt(int a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall30 call = reinterpret_cast<CuteQQmlJSOptimizationsCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeInt(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpNeNull()
  void generate_CmpNeNull() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall31 call = reinterpret_cast<CuteQQmlJSOptimizationsCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpNeNull();
  }

  //  void QQmlJSCompilePass::generate_CmpStrictEqual(int a0)
  void generate_CmpStrictEqual(int a0) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall32 call = reinterpret_cast<CuteQQmlJSOptimizationsCall32>(taken[32]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_CmpStrictNotEqual(int a0)
  void generate_CmpStrictNotEqual(int a0) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall33 call = reinterpret_cast<CuteQQmlJSOptimizationsCall33>(taken[33]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CmpStrictNotEqual(a0);
  }

  //  void QQmlJSCompilePass::generate_Construct(int a0, int a1, int a2)
  void generate_Construct(int a0, int a1, int a2) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall34 call = reinterpret_cast<CuteQQmlJSOptimizationsCall34>(taken[34]);
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
      CuteQQmlJSOptimizationsCall35 call = reinterpret_cast<CuteQQmlJSOptimizationsCall35>(taken[35]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConstructWithSpread(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_ConvertThisToObject()
  void generate_ConvertThisToObject() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall36 call = reinterpret_cast<CuteQQmlJSOptimizationsCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ConvertThisToObject();
  }

  //  void QQmlJSCompilePass::generate_CreateCallContext()
  void generate_CreateCallContext() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall37 call = reinterpret_cast<CuteQQmlJSOptimizationsCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateCallContext();
  }

  //  void QQmlJSCompilePass::generate_CreateClass(int a0, int a1, int a2)
  void generate_CreateClass(int a0, int a1, int a2) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall38 call = reinterpret_cast<CuteQQmlJSOptimizationsCall38>(taken[38]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateClass(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_CreateMappedArgumentsObject()
  void generate_CreateMappedArgumentsObject() override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall39 call = reinterpret_cast<CuteQQmlJSOptimizationsCall39>(taken[39]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateMappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_CreateRestParameter(int a0)
  void generate_CreateRestParameter(int a0) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall40 call = reinterpret_cast<CuteQQmlJSOptimizationsCall40>(taken[40]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateRestParameter(a0);
  }

  //  void QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject()
  void generate_CreateUnmappedArgumentsObject() override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall41 call = reinterpret_cast<CuteQQmlJSOptimizationsCall41>(taken[41]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_CreateUnmappedArgumentsObject();
  }

  //  void QQmlJSCompilePass::generate_DeadTemporalZoneCheck(int a0)
  void generate_DeadTemporalZoneCheck(int a0) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall42 call = reinterpret_cast<CuteQQmlJSOptimizationsCall42>(taken[42]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeadTemporalZoneCheck(a0);
  }

  //  void QQmlJSCompilePass::generate_Debug()
  void generate_Debug() override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall43 call = reinterpret_cast<CuteQQmlJSOptimizationsCall43>(taken[43]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Debug();
  }

  //  void QQmlJSCompilePass::generate_DeclareVar(int a0, int a1)
  void generate_DeclareVar(int a0, int a1) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall44 call = reinterpret_cast<CuteQQmlJSOptimizationsCall44>(taken[44]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeclareVar(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Decrement()
  void generate_Decrement() override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall45 call = reinterpret_cast<CuteQQmlJSOptimizationsCall45>(taken[45]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Decrement();
  }

  //  void QQmlJSCompilePass::generate_DefineArray(int a0, int a1)
  void generate_DefineArray(int a0, int a1) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall46 call = reinterpret_cast<CuteQQmlJSOptimizationsCall46>(taken[46]);
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
      CuteQQmlJSOptimizationsCall47 call = reinterpret_cast<CuteQQmlJSOptimizationsCall47>(taken[47]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DefineObjectLiteral(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_DeleteName(int a0)
  void generate_DeleteName(int a0) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall48 call = reinterpret_cast<CuteQQmlJSOptimizationsCall48>(taken[48]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteName(a0);
  }

  //  void QQmlJSCompilePass::generate_DeleteProperty(int a0, int a1)
  void generate_DeleteProperty(int a0, int a1) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall49 call = reinterpret_cast<CuteQQmlJSOptimizationsCall49>(taken[49]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DeleteProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_DestructureRestElement()
  void generate_DestructureRestElement() override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall50 call = reinterpret_cast<CuteQQmlJSOptimizationsCall50>(taken[50]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_DestructureRestElement();
  }

  //  void QQmlJSCompilePass::generate_Div(int a0)
  void generate_Div(int a0) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall51 call = reinterpret_cast<CuteQQmlJSOptimizationsCall51>(taken[51]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Div(a0);
  }

  //  void QQmlJSCompilePass::generate_Exp(int a0)
  void generate_Exp(int a0) override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall52 call = reinterpret_cast<CuteQQmlJSOptimizationsCall52>(taken[52]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Exp(a0);
  }

  //  void QQmlJSCompilePass::generate_GetException()
  void generate_GetException() override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall53 call = reinterpret_cast<CuteQQmlJSOptimizationsCall53>(taken[53]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetException();
  }

  //  void QQmlJSCompilePass::generate_GetIterator(int a0)
  void generate_GetIterator(int a0) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall54 call = reinterpret_cast<CuteQQmlJSOptimizationsCall54>(taken[54]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetIterator(a0);
  }

  //  void QQmlJSCompilePass::generate_GetLookup(int a0)
  void generate_GetLookup(int a0) override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall55 call = reinterpret_cast<CuteQQmlJSOptimizationsCall55>(taken[55]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_GetOptionalLookup(int a0, int a1)
  void generate_GetOptionalLookup(int a0, int a1) override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall56 call = reinterpret_cast<CuteQQmlJSOptimizationsCall56>(taken[56]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetOptionalLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_GetTemplateObject(int a0)
  void generate_GetTemplateObject(int a0) override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall57 call = reinterpret_cast<CuteQQmlJSOptimizationsCall57>(taken[57]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_GetTemplateObject(a0);
  }

  //  void QQmlJSCompilePass::generate_Increment()
  void generate_Increment() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall58 call = reinterpret_cast<CuteQQmlJSOptimizationsCall58>(taken[58]);
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
      CuteQQmlJSOptimizationsCall59 call = reinterpret_cast<CuteQQmlJSOptimizationsCall59>(taken[59]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_InitializeBlockDeadTemporalZone(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_IteratorClose()
  void generate_IteratorClose() override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall60 call = reinterpret_cast<CuteQQmlJSOptimizationsCall60>(taken[60]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorClose();
  }

  //  void QQmlJSCompilePass::generate_IteratorNext(int a0, int a1)
  void generate_IteratorNext(int a0, int a1) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall61 call = reinterpret_cast<CuteQQmlJSOptimizationsCall61>(taken[61]);
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
      CuteQQmlJSOptimizationsCall62 call = reinterpret_cast<CuteQQmlJSOptimizationsCall62>(taken[62]);
      call(this, a0, a1, a2, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_IteratorNextForYieldStar(a0, a1, a2);
  }

  //  void QQmlJSCompilePass::generate_Jump(int a0)
  void generate_Jump(int a0) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall63 call = reinterpret_cast<CuteQQmlJSOptimizationsCall63>(taken[63]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Jump(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpFalse(int a0)
  void generate_JumpFalse(int a0) override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall64 call = reinterpret_cast<CuteQQmlJSOptimizationsCall64>(taken[64]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpFalse(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNoException(int a0)
  void generate_JumpNoException(int a0) override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall65 call = reinterpret_cast<CuteQQmlJSOptimizationsCall65>(taken[65]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNoException(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpNotUndefined(int a0)
  void generate_JumpNotUndefined(int a0) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall66 call = reinterpret_cast<CuteQQmlJSOptimizationsCall66>(taken[66]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpNotUndefined(a0);
  }

  //  void QQmlJSCompilePass::generate_JumpTrue(int a0)
  void generate_JumpTrue(int a0) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall67 call = reinterpret_cast<CuteQQmlJSOptimizationsCall67>(taken[67]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_JumpTrue(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadClosure(int a0)
  void generate_LoadClosure(int a0) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall68 call = reinterpret_cast<CuteQQmlJSOptimizationsCall68>(taken[68]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadClosure(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadConst(int a0)
  void generate_LoadConst(int a0) override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall69 call = reinterpret_cast<CuteQQmlJSOptimizationsCall69>(taken[69]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadConst(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadElement(int a0)
  void generate_LoadElement(int a0) override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall70 call = reinterpret_cast<CuteQQmlJSOptimizationsCall70>(taken[70]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadElement(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadFalse()
  void generate_LoadFalse() override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall71 call = reinterpret_cast<CuteQQmlJSOptimizationsCall71>(taken[71]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadFalse();
  }

  //  void QQmlJSCompilePass::generate_LoadGlobalLookup(int a0)
  void generate_LoadGlobalLookup(int a0) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall72 call = reinterpret_cast<CuteQQmlJSOptimizationsCall72>(taken[72]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadGlobalLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadImport(int a0)
  void generate_LoadImport(int a0) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall73 call = reinterpret_cast<CuteQQmlJSOptimizationsCall73>(taken[73]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadImport(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadInt(int a0)
  void generate_LoadInt(int a0) override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall74 call = reinterpret_cast<CuteQQmlJSOptimizationsCall74>(taken[74]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadInt(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadLocal(int a0)
  void generate_LoadLocal(int a0) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall75 call = reinterpret_cast<CuteQQmlJSOptimizationsCall75>(taken[75]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadName(int a0)
  void generate_LoadName(int a0) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall76 call = reinterpret_cast<CuteQQmlJSOptimizationsCall76>(taken[76]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadName(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadNull()
  void generate_LoadNull() override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall77 call = reinterpret_cast<CuteQQmlJSOptimizationsCall77>(taken[77]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadNull();
  }

  //  void QQmlJSCompilePass::generate_LoadOptionalProperty(int a0, int a1)
  void generate_LoadOptionalProperty(int a0, int a1) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall78 call = reinterpret_cast<CuteQQmlJSOptimizationsCall78>(taken[78]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadOptionalProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadProperty(int a0)
  void generate_LoadProperty(int a0) override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall79 call = reinterpret_cast<CuteQQmlJSOptimizationsCall79>(taken[79]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(int a0)
  void generate_LoadQmlContextPropertyLookup(int a0) override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall80 call = reinterpret_cast<CuteQQmlJSOptimizationsCall80>(taken[80]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadQmlContextPropertyLookup(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadReg(int a0)
  void generate_LoadReg(int a0) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall81 call = reinterpret_cast<CuteQQmlJSOptimizationsCall81>(taken[81]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadReg(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadRuntimeString(int a0)
  void generate_LoadRuntimeString(int a0) override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall82 call = reinterpret_cast<CuteQQmlJSOptimizationsCall82>(taken[82]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadRuntimeString(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadScopedLocal(int a0, int a1)
  void generate_LoadScopedLocal(int a0, int a1) override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall83 call = reinterpret_cast<CuteQQmlJSOptimizationsCall83>(taken[83]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_LoadSuperConstructor()
  void generate_LoadSuperConstructor() override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall84 call = reinterpret_cast<CuteQQmlJSOptimizationsCall84>(taken[84]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperConstructor();
  }

  //  void QQmlJSCompilePass::generate_LoadSuperProperty(int a0)
  void generate_LoadSuperProperty(int a0) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall85 call = reinterpret_cast<CuteQQmlJSOptimizationsCall85>(taken[85]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_LoadTrue()
  void generate_LoadTrue() override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall86 call = reinterpret_cast<CuteQQmlJSOptimizationsCall86>(taken[86]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadTrue();
  }

  //  void QQmlJSCompilePass::generate_LoadUndefined()
  void generate_LoadUndefined() override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall87 call = reinterpret_cast<CuteQQmlJSOptimizationsCall87>(taken[87]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadUndefined();
  }

  //  void QQmlJSCompilePass::generate_LoadZero()
  void generate_LoadZero() override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall88 call = reinterpret_cast<CuteQQmlJSOptimizationsCall88>(taken[88]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_LoadZero();
  }

  //  void QQmlJSCompilePass::generate_Mod(int a0)
  void generate_Mod(int a0) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall89 call = reinterpret_cast<CuteQQmlJSOptimizationsCall89>(taken[89]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mod(a0);
  }

  //  void QQmlJSCompilePass::generate_MoveConst(int a0, int a1)
  void generate_MoveConst(int a0, int a1) override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall90 call = reinterpret_cast<CuteQQmlJSOptimizationsCall90>(taken[90]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveConst(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveReg(int a0, int a1)
  void generate_MoveReg(int a0, int a1) override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall91 call = reinterpret_cast<CuteQQmlJSOptimizationsCall91>(taken[91]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveReg(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_MoveRegExp(int a0, int a1)
  void generate_MoveRegExp(int a0, int a1) override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall92 call = reinterpret_cast<CuteQQmlJSOptimizationsCall92>(taken[92]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_MoveRegExp(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Mul(int a0)
  void generate_Mul(int a0) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall93 call = reinterpret_cast<CuteQQmlJSOptimizationsCall93>(taken[93]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Mul(a0);
  }

  //  void QQmlJSCompilePass::generate_PopContext()
  void generate_PopContext() override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall94 call = reinterpret_cast<CuteQQmlJSOptimizationsCall94>(taken[94]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopContext();
  }

  //  void QQmlJSCompilePass::generate_PopScriptContext()
  void generate_PopScriptContext() override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall95 call = reinterpret_cast<CuteQQmlJSOptimizationsCall95>(taken[95]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PopScriptContext();
  }

  //  void QQmlJSCompilePass::generate_PushBlockContext(int a0)
  void generate_PushBlockContext(int a0) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall96 call = reinterpret_cast<CuteQQmlJSOptimizationsCall96>(taken[96]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushBlockContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushCatchContext(int a0, int a1)
  void generate_PushCatchContext(int a0, int a1) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall97 call = reinterpret_cast<CuteQQmlJSOptimizationsCall97>(taken[97]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushCatchContext(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_PushScriptContext(int a0)
  void generate_PushScriptContext(int a0) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall98 call = reinterpret_cast<CuteQQmlJSOptimizationsCall98>(taken[98]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushScriptContext(a0);
  }

  //  void QQmlJSCompilePass::generate_PushWithContext()
  void generate_PushWithContext() override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall99 call = reinterpret_cast<CuteQQmlJSOptimizationsCall99>(taken[99]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_PushWithContext();
  }

  //  void QQmlJSCompilePass::generate_Resume(int a0)
  void generate_Resume(int a0) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall100 call = reinterpret_cast<CuteQQmlJSOptimizationsCall100>(taken[100]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Resume(a0);
  }

  //  void QQmlJSCompilePass::generate_Ret()
  void generate_Ret() override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall101 call = reinterpret_cast<CuteQQmlJSOptimizationsCall101>(taken[101]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Ret();
  }

  //  void QQmlJSCompilePass::generate_SetException()
  void generate_SetException() override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall102 call = reinterpret_cast<CuteQQmlJSOptimizationsCall102>(taken[102]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetException();
  }

  //  void QQmlJSCompilePass::generate_SetLookup(int a0, int a1)
  void generate_SetLookup(int a0, int a1) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall103 call = reinterpret_cast<CuteQQmlJSOptimizationsCall103>(taken[103]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetLookup(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_SetUnwindHandler(int a0)
  void generate_SetUnwindHandler(int a0) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall104 call = reinterpret_cast<CuteQQmlJSOptimizationsCall104>(taken[104]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_SetUnwindHandler(a0);
  }

  //  void QQmlJSCompilePass::generate_Shl(int a0)
  void generate_Shl(int a0) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall105 call = reinterpret_cast<CuteQQmlJSOptimizationsCall105>(taken[105]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shl(a0);
  }

  //  void QQmlJSCompilePass::generate_ShlConst(int a0)
  void generate_ShlConst(int a0) override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall106 call = reinterpret_cast<CuteQQmlJSOptimizationsCall106>(taken[106]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShlConst(a0);
  }

  //  void QQmlJSCompilePass::generate_Shr(int a0)
  void generate_Shr(int a0) override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall107 call = reinterpret_cast<CuteQQmlJSOptimizationsCall107>(taken[107]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Shr(a0);
  }

  //  void QQmlJSCompilePass::generate_ShrConst(int a0)
  void generate_ShrConst(int a0) override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall108 call = reinterpret_cast<CuteQQmlJSOptimizationsCall108>(taken[108]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreElement(int a0, int a1)
  void generate_StoreElement(int a0, int a1) override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall109 call = reinterpret_cast<CuteQQmlJSOptimizationsCall109>(taken[109]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreElement(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreLocal(int a0)
  void generate_StoreLocal(int a0) override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall110 call = reinterpret_cast<CuteQQmlJSOptimizationsCall110>(taken[110]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreLocal(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameSloppy(int a0)
  void generate_StoreNameSloppy(int a0) override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall111 call = reinterpret_cast<CuteQQmlJSOptimizationsCall111>(taken[111]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameSloppy(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreNameStrict(int a0)
  void generate_StoreNameStrict(int a0) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall112 call = reinterpret_cast<CuteQQmlJSOptimizationsCall112>(taken[112]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreNameStrict(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreProperty(int a0, int a1)
  void generate_StoreProperty(int a0, int a1) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall113 call = reinterpret_cast<CuteQQmlJSOptimizationsCall113>(taken[113]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreProperty(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreReg(int a0)
  void generate_StoreReg(int a0) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall114 call = reinterpret_cast<CuteQQmlJSOptimizationsCall114>(taken[114]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreReg(a0);
  }

  //  void QQmlJSCompilePass::generate_StoreScopedLocal(int a0, int a1)
  void generate_StoreScopedLocal(int a0, int a1) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall115 call = reinterpret_cast<CuteQQmlJSOptimizationsCall115>(taken[115]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreScopedLocal(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_StoreSuperProperty(int a0)
  void generate_StoreSuperProperty(int a0) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall116 call = reinterpret_cast<CuteQQmlJSOptimizationsCall116>(taken[116]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_StoreSuperProperty(a0);
  }

  //  void QQmlJSCompilePass::generate_Sub(int a0)
  void generate_Sub(int a0) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall117 call = reinterpret_cast<CuteQQmlJSOptimizationsCall117>(taken[117]);
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
      CuteQQmlJSOptimizationsCall118 call = reinterpret_cast<CuteQQmlJSOptimizationsCall118>(taken[118]);
      call(this, a0, a1, a2, a3, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TailCall(a0, a1, a2, a3);
  }

  //  void QQmlJSCompilePass::generate_ThrowException()
  void generate_ThrowException() override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall119 call = reinterpret_cast<CuteQQmlJSOptimizationsCall119>(taken[119]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowException();
  }

  //  void QQmlJSCompilePass::generate_ThrowOnNullOrUndefined()
  void generate_ThrowOnNullOrUndefined() override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall120 call = reinterpret_cast<CuteQQmlJSOptimizationsCall120>(taken[120]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ThrowOnNullOrUndefined();
  }

  //  void QQmlJSCompilePass::generate_ToObject()
  void generate_ToObject() override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall121 call = reinterpret_cast<CuteQQmlJSOptimizationsCall121>(taken[121]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_ToObject();
  }

  //  void QQmlJSCompilePass::generate_TypeofName(int a0)
  void generate_TypeofName(int a0) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall122 call = reinterpret_cast<CuteQQmlJSOptimizationsCall122>(taken[122]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofName(a0);
  }

  //  void QQmlJSCompilePass::generate_TypeofValue()
  void generate_TypeofValue() override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall123 call = reinterpret_cast<CuteQQmlJSOptimizationsCall123>(taken[123]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_TypeofValue();
  }

  //  void QQmlJSCompilePass::generate_UCompl()
  void generate_UCompl() override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall124 call = reinterpret_cast<CuteQQmlJSOptimizationsCall124>(taken[124]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UCompl();
  }

  //  void QQmlJSCompilePass::generate_UMinus()
  void generate_UMinus() override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall125 call = reinterpret_cast<CuteQQmlJSOptimizationsCall125>(taken[125]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UMinus();
  }

  //  void QQmlJSCompilePass::generate_UNot()
  void generate_UNot() override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall126 call = reinterpret_cast<CuteQQmlJSOptimizationsCall126>(taken[126]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UNot();
  }

  //  void QQmlJSCompilePass::generate_UPlus()
  void generate_UPlus() override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall127 call = reinterpret_cast<CuteQQmlJSOptimizationsCall127>(taken[127]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UPlus();
  }

  //  void QQmlJSCompilePass::generate_UShr(int a0)
  void generate_UShr(int a0) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall128 call = reinterpret_cast<CuteQQmlJSOptimizationsCall128>(taken[128]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShr(a0);
  }

  //  void QQmlJSCompilePass::generate_UShrConst(int a0)
  void generate_UShrConst(int a0) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall129 call = reinterpret_cast<CuteQQmlJSOptimizationsCall129>(taken[129]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UShrConst(a0);
  }

  //  void QQmlJSCompilePass::generate_UnwindDispatch()
  void generate_UnwindDispatch() override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall130 call = reinterpret_cast<CuteQQmlJSOptimizationsCall130>(taken[130]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindDispatch();
  }

  //  void QQmlJSCompilePass::generate_UnwindToLabel(int a0, int a1)
  void generate_UnwindToLabel(int a0, int a1) override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall131 call = reinterpret_cast<CuteQQmlJSOptimizationsCall131>(taken[131]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_UnwindToLabel(a0, a1);
  }

  //  void QQmlJSCompilePass::generate_Yield()
  void generate_Yield() override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall132 call = reinterpret_cast<CuteQQmlJSOptimizationsCall132>(taken[132]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_Yield();
  }

  //  void QQmlJSCompilePass::generate_YieldStar()
  void generate_YieldStar() override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSOptimizationsCall133 call = reinterpret_cast<CuteQQmlJSOptimizationsCall133>(taken[133]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSCompilePass::generate_YieldStar();
  }
};

//  QQmlJSOptimizations::~QQmlJSOptimizations()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizationsD1Ev(QQmlJSOptimizations *self) {
  delete self;
}

//  BlocksAndAnnotations QQmlJSOptimizations::run(const Function *function)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::BlocksAndAnnotations *ritual_ZN19QQmlJSOptimizations3runEPKN17QQmlJSCompilePass8FunctionE(
    QQmlJSOptimizations *self,
    const QQmlJSCompilePass::Function *function) {
  return new QQmlJSCompilePass::BlocksAndAnnotations(self->run(function));
}

//  QV4::Moth::ByteCodeHandler::Verdict
//      QQmlJSOptimizations::startInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
QV4::Moth::ByteCodeHandler::Verdict ritual_ZN19QQmlJSOptimizations16startInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSOptimizations *self,
    QV4::Moth::Instr::Type a0) {
  return self->startInstruction(a0);
}

//  void QQmlJSOptimizations::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSOptimizations *self,
    QV4::Moth::Instr::Type a0) {
  self->endInstruction(a0);
}

//  void QQmlJSOptimizations::populateBasicBlocks()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations19populateBasicBlocksEv(
    QQmlJSOptimizations *self) {
  self->populateBasicBlocks();
}

//  void QQmlJSOptimizations::populateReaderLocationsTrackedTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations35populateReaderLocationsTrackedTypesEv(
    QQmlJSOptimizations *self) {
  self->populateReaderLocationsTrackedTypes();
}

//  void QQmlJSOptimizations::populateReaderLocationsReadersAndConversions()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations44populateReaderLocationsReadersAndConversionsEv(
    QQmlJSOptimizations *self) {
  self->populateReaderLocationsReadersAndConversions();
}

//  void QQmlJSOptimizations::adjustTypes()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations11adjustTypesEv(
    QQmlJSOptimizations *self) {
  self->adjustTypes();
}

//  void QQmlJSOptimizations::removeDeadStoresUntilStable()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQmlJSOptimizations27removeDeadStoresUntilStableEv(
    QQmlJSOptimizations *self) {
  self->removeDeadStoresUntilStable();
}

//  bool QQmlJSOptimizations::canMove(int instructionOffset, const
//      RegisterAccess &access) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QQmlJSOptimizations7canMoveEiRKNS_14RegisterAccessE(
    const QQmlJSOptimizations *self,
    int instructionOffset,
    const QQmlJSOptimizations::RegisterAccess *access) {
  return self->canMove(instructionOffset, *access);
}

//  a Python function taken by a CuteQQmlJSOptimizations, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSOptimizations(
    QQmlJSOptimizations *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSOptimizations *>(self)->take(key, call);
}

//  void QQmlJSOptimizations::endInstruction(QV4::Moth::Instr::Type a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQmlJSOptimizations14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSOptimizations *self,
    QV4::Moth::Instr::Type a0) {
  self->QQmlJSOptimizations::endInstruction(a0);
}
