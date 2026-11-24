//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstypepropagator_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljstypepropagator_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompilepass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsregistercontent_p.h>
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljsmetatypes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QQmlJSTypePropagator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQmlJSTypePropagator : QQmlJSTypePropagator {
  using QQmlJSTypePropagator::handleUnqualifiedAccess;
  using QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties;
  using QQmlJSTypePropagator::handleImportNamespaceLookup;
  using QQmlJSTypePropagator::handleLookupError;
  using QQmlJSTypePropagator::checkForEnumProblems;
  using QQmlJSTypePropagator::warnAboutTypeCoercion;
  using QQmlJSTypePropagator::generate_StoreNameCommon;
  using QQmlJSTypePropagator::propagateTranslationMethod_SAcheck;
  using QQmlJSTypePropagator::propagatePropertyLookup;
};

//  A QQmlJSTypePropagator that Python can take functions over in. Every QQmlJSTypePropagator
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQmlJSTypePropagatorCall0)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall1)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall2)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall3)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall4)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall5)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall6)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall7)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall8)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall9)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall10)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall11)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall12)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall13)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall14)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall15)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall16)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall17)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall18)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall19)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall20)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall21)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall22)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall23)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall24)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall25)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall26)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall27)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall28)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall29)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall30)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall31)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall32)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall33)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall34)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall35)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall36)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall37)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall38)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall39)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall40)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall41)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall42)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall43)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall44)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall45)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall46)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall47)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall48)(const void *, int, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall49)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall50)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall51)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall52)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall53)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall54)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall55)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall56)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall57)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall58)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall59)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall60)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall61)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall62)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall63)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall64)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall65)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall66)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall67)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall68)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall69)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall70)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall71)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall72)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall73)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall74)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall75)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall76)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall77)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall78)(const void *, int, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall79)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall80)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall81)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall82)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall83)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall84)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall85)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall86)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall87)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall88)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall89)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall90)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall91)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall92)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall93)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall94)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall95)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall96)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall97)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall98)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall99)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall100)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall101)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall102)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall103)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall104)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall105)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall106)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall107)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall108)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall109)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall110)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall111)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall112)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall113)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall114)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall115)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall116)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall117)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall118)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall119)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall120)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall121)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall122)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall123)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall124)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall125)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall126)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall127)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall128)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall129)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall130)(const void *, int, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall131)(const void *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall132)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall133)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall134)(const void *, const QString *, bool, int *);
typedef void (*CuteQQmlJSTypePropagatorCall135)(const void *, const QString *, bool, int *);
typedef bool (*CuteQQmlJSTypePropagatorCall136)(const void *, const QString *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall137)(const void *, const QString *, int *);
typedef bool (*CuteQQmlJSTypePropagatorCall138)(const void *, const QQmlJSRegisterContent *, const QString *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall139)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall140)(const void *, int, int *);
typedef void (*CuteQQmlJSTypePropagatorCall141)(const void *, const QString *, int *);
typedef void (*CuteQQmlJSTypePropagatorCall142)(const void *, const QString *, int, int *);
class CuteQQmlJSTypePropagator : public QQmlJSTypePropagator {
public:
  using QQmlJSTypePropagator::QQmlJSTypePropagator;
  void *taken[143] = {};

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
    if (!std::strcmp(key, "_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK7QStringb")) {
      taken[134] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAndContextPropertiesERK7QStringb")) {
      taken[135] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator27handleImportNamespaceLookupERK7QString")) {
      taken[136] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QString")) {
      taken[137] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQmlJSRegisterContentRK7QString")) {
      taken[138] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi")) {
      taken[139] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi")) {
      taken[140] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator34propagateTranslationMethod_SAcheckERK7QString")) {
      taken[141] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7QStringi")) {
      taken[142] = call;
      return true;
    }
    return false;
  }

  //  void QQmlJSTypePropagator::generate_Ret()
  void generate_Ret() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall0 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Ret();
  }

  //  void QQmlJSTypePropagator::generate_Debug()
  void generate_Debug() override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall1 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Debug();
  }

  //  void QQmlJSTypePropagator::generate_LoadConst(int index)
  void generate_LoadConst(int index) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall2 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall2>(taken[2]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadConst(index);
  }

  //  void QQmlJSTypePropagator::generate_LoadZero()
  void generate_LoadZero() override {
    if (taken[3]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall3 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadZero();
  }

  //  void QQmlJSTypePropagator::generate_LoadTrue()
  void generate_LoadTrue() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall4 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadTrue();
  }

  //  void QQmlJSTypePropagator::generate_LoadFalse()
  void generate_LoadFalse() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall5 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadFalse();
  }

  //  void QQmlJSTypePropagator::generate_LoadNull()
  void generate_LoadNull() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall6 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadNull();
  }

  //  void QQmlJSTypePropagator::generate_LoadUndefined()
  void generate_LoadUndefined() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall7 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadUndefined();
  }

  //  void QQmlJSTypePropagator::generate_LoadInt(int value)
  void generate_LoadInt(int value) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall8 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall8>(taken[8]);
      call(this, value, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadInt(value);
  }

  //  void QQmlJSTypePropagator::generate_MoveConst(int constIndex, int
  //      destTemp)
  void generate_MoveConst(int constIndex, int destTemp) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall9 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall9>(taken[9]);
      call(this, constIndex, destTemp, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_MoveConst(constIndex, destTemp);
  }

  //  void QQmlJSTypePropagator::generate_LoadReg(int reg)
  void generate_LoadReg(int reg) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall10 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall10>(taken[10]);
      call(this, reg, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadReg(reg);
  }

  //  void QQmlJSTypePropagator::generate_StoreReg(int reg)
  void generate_StoreReg(int reg) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall11 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall11>(taken[11]);
      call(this, reg, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreReg(reg);
  }

  //  void QQmlJSTypePropagator::generate_MoveReg(int srcReg, int destReg)
  void generate_MoveReg(int srcReg, int destReg) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall12 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall12>(taken[12]);
      call(this, srcReg, destReg, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_MoveReg(srcReg, destReg);
  }

  //  void QQmlJSTypePropagator::generate_LoadImport(int index)
  void generate_LoadImport(int index) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall13 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall13>(taken[13]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadImport(index);
  }

  //  void QQmlJSTypePropagator::generate_LoadLocal(int index)
  void generate_LoadLocal(int index) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall14 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall14>(taken[14]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadLocal(index);
  }

  //  void QQmlJSTypePropagator::generate_StoreLocal(int index)
  void generate_StoreLocal(int index) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall15 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall15>(taken[15]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreLocal(index);
  }

  //  void QQmlJSTypePropagator::generate_LoadScopedLocal(int scope, int
  //      index)
  void generate_LoadScopedLocal(int scope, int index) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall16 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall16>(taken[16]);
      call(this, scope, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadScopedLocal(scope, index);
  }

  //  void QQmlJSTypePropagator::generate_StoreScopedLocal(int scope, int
  //      index)
  void generate_StoreScopedLocal(int scope, int index) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall17 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall17>(taken[17]);
      call(this, scope, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreScopedLocal(scope, index);
  }

  //  void QQmlJSTypePropagator::generate_LoadRuntimeString(int stringId)
  void generate_LoadRuntimeString(int stringId) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall18 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall18>(taken[18]);
      call(this, stringId, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadRuntimeString(stringId);
  }

  //  void QQmlJSTypePropagator::generate_MoveRegExp(int regExpId, int
  //      destReg)
  void generate_MoveRegExp(int regExpId, int destReg) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall19 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall19>(taken[19]);
      call(this, regExpId, destReg, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_MoveRegExp(regExpId, destReg);
  }

  //  void QQmlJSTypePropagator::generate_LoadClosure(int value)
  void generate_LoadClosure(int value) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall20 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall20>(taken[20]);
      call(this, value, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadClosure(value);
  }

  //  void QQmlJSTypePropagator::generate_LoadName(int nameIndex)
  void generate_LoadName(int nameIndex) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall21 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall21>(taken[21]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadName(nameIndex);
  }

  //  void QQmlJSTypePropagator::generate_LoadGlobalLookup(int index)
  void generate_LoadGlobalLookup(int index) override {
    if (taken[22]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall22 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall22>(taken[22]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadGlobalLookup(index);
  }

  //  void QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(int
  //      index)
  void generate_LoadQmlContextPropertyLookup(int index) override {
    if (taken[23]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall23 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall23>(taken[23]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(index);
  }

  //  void QQmlJSTypePropagator::generate_StoreNameSloppy(int nameIndex)
  void generate_StoreNameSloppy(int nameIndex) override {
    if (taken[24]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall24 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall24>(taken[24]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreNameSloppy(nameIndex);
  }

  //  void QQmlJSTypePropagator::generate_StoreNameStrict(int name)
  void generate_StoreNameStrict(int name) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall25 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall25>(taken[25]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreNameStrict(name);
  }

  //  void QQmlJSTypePropagator::generate_LoadElement(int base)
  void generate_LoadElement(int base) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall26 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall26>(taken[26]);
      call(this, base, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadElement(base);
  }

  //  void QQmlJSTypePropagator::generate_StoreElement(int base, int index)
  void generate_StoreElement(int base, int index) override {
    if (taken[27]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall27 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall27>(taken[27]);
      call(this, base, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreElement(base, index);
  }

  //  void QQmlJSTypePropagator::generate_LoadProperty(int nameIndex)
  void generate_LoadProperty(int nameIndex) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall28 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall28>(taken[28]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadProperty(nameIndex);
  }

  //  void QQmlJSTypePropagator::generate_LoadOptionalProperty(int name,
  //      int offset)
  void generate_LoadOptionalProperty(int name, int offset) override {
    if (taken[29]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall29 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall29>(taken[29]);
      call(this, name, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadOptionalProperty(name, offset);
  }

  //  void QQmlJSTypePropagator::generate_GetLookup(int index)
  void generate_GetLookup(int index) override {
    if (taken[30]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall30 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall30>(taken[30]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_GetLookup(index);
  }

  //  void QQmlJSTypePropagator::generate_GetOptionalLookup(int index, int
  //      offset)
  void generate_GetOptionalLookup(int index, int offset) override {
    if (taken[31]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall31 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall31>(taken[31]);
      call(this, index, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_GetOptionalLookup(index, offset);
  }

  //  void QQmlJSTypePropagator::generate_StoreProperty(int name, int base)
  void generate_StoreProperty(int name, int base) override {
    if (taken[32]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall32 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall32>(taken[32]);
      call(this, name, base, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreProperty(name, base);
  }

  //  void QQmlJSTypePropagator::generate_SetLookup(int index, int base)
  void generate_SetLookup(int index, int base) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall33 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall33>(taken[33]);
      call(this, index, base, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_SetLookup(index, base);
  }

  //  void QQmlJSTypePropagator::generate_LoadSuperProperty(int property)
  void generate_LoadSuperProperty(int property) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall34 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall34>(taken[34]);
      call(this, property, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadSuperProperty(property);
  }

  //  void QQmlJSTypePropagator::generate_StoreSuperProperty(int property)
  void generate_StoreSuperProperty(int property) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall35 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall35>(taken[35]);
      call(this, property, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreSuperProperty(property);
  }

  //  void QQmlJSTypePropagator::generate_Yield()
  void generate_Yield() override {
    if (taken[36]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall36 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall36>(taken[36]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Yield();
  }

  //  void QQmlJSTypePropagator::generate_YieldStar()
  void generate_YieldStar() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall37 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall37>(taken[37]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_YieldStar();
  }

  //  void QQmlJSTypePropagator::generate_Resume(int a0)
  void generate_Resume(int a0) override {
    if (taken[38]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall38 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall38>(taken[38]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Resume(a0);
  }

  //  void QQmlJSTypePropagator::generate_CallValue(int name, int argc, int
  //      argv)
  void generate_CallValue(int name, int argc, int argv) override {
    if (taken[39]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall39 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall39>(taken[39]);
      call(this, name, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallValue(name, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallWithReceiver(int name, int
  //      thisObject, int argc, int argv)
  void generate_CallWithReceiver(
      int name,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[40]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall40 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall40>(taken[40]);
      call(this, name, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallWithReceiver(name, thisObject, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallProperty(int name, int base,
  //      int argc, int argv)
  void generate_CallProperty(
      int name,
      int base,
      int argc,
      int argv) override {
    if (taken[41]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall41 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall41>(taken[41]);
      call(this, name, base, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallProperty(name, base, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallPropertyLookup(int
  //      lookupIndex, int base, int argc, int argv)
  void generate_CallPropertyLookup(
      int lookupIndex,
      int base,
      int argc,
      int argv) override {
    if (taken[42]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall42 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall42>(taken[42]);
      call(this, lookupIndex, base, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallPropertyLookup(lookupIndex, base, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallName(int name, int argc, int
  //      argv)
  void generate_CallName(int name, int argc, int argv) override {
    if (taken[43]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall43 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall43>(taken[43]);
      call(this, name, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallName(name, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallPossiblyDirectEval(int argc,
  //      int argv)
  void generate_CallPossiblyDirectEval(int argc, int argv) override {
    if (taken[44]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall44 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall44>(taken[44]);
      call(this, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallPossiblyDirectEval(argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallGlobalLookup(int index, int
  //      argc, int argv)
  void generate_CallGlobalLookup(int index, int argc, int argv) override {
    if (taken[45]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall45 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall45>(taken[45]);
      call(this, index, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallGlobalLookup(index, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(int
  //      index, int argc, int argv)
  void generate_CallQmlContextPropertyLookup(
      int index,
      int argc,
      int argv) override {
    if (taken[46]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall46 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall46>(taken[46]);
      call(this, index, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(index, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_CallWithSpread(int func, int
  //      thisObject, int argc, int argv)
  void generate_CallWithSpread(
      int func,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[47]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall47 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall47>(taken[47]);
      call(this, func, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CallWithSpread(func, thisObject, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_TailCall(int func, int
  //      thisObject, int argc, int argv)
  void generate_TailCall(
      int func,
      int thisObject,
      int argc,
      int argv) override {
    if (taken[48]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall48 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall48>(taken[48]);
      call(this, func, thisObject, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_TailCall(func, thisObject, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_Construct(int func, int argc, int
  //      argv)
  void generate_Construct(int func, int argc, int argv) override {
    if (taken[49]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall49 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall49>(taken[49]);
      call(this, func, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Construct(func, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_ConstructWithSpread(int func, int
  //      argc, int argv)
  void generate_ConstructWithSpread(int func, int argc, int argv) override {
    if (taken[50]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall50 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall50>(taken[50]);
      call(this, func, argc, argv, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ConstructWithSpread(func, argc, argv);
  }

  //  void QQmlJSTypePropagator::generate_SetUnwindHandler(int offset)
  void generate_SetUnwindHandler(int offset) override {
    if (taken[51]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall51 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall51>(taken[51]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_SetUnwindHandler(offset);
  }

  //  void QQmlJSTypePropagator::generate_UnwindDispatch()
  void generate_UnwindDispatch() override {
    if (taken[52]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall52 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall52>(taken[52]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UnwindDispatch();
  }

  //  void QQmlJSTypePropagator::generate_UnwindToLabel(int level, int
  //      offset)
  void generate_UnwindToLabel(int level, int offset) override {
    if (taken[53]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall53 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall53>(taken[53]);
      call(this, level, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UnwindToLabel(level, offset);
  }

  //  void QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(int name)
  void generate_DeadTemporalZoneCheck(int name) override {
    if (taken[54]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall54 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall54>(taken[54]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(name);
  }

  //  void QQmlJSTypePropagator::generate_ThrowException()
  void generate_ThrowException() override {
    if (taken[55]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall55 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall55>(taken[55]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ThrowException();
  }

  //  void QQmlJSTypePropagator::generate_GetException()
  void generate_GetException() override {
    if (taken[56]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall56 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall56>(taken[56]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_GetException();
  }

  //  void QQmlJSTypePropagator::generate_SetException()
  void generate_SetException() override {
    if (taken[57]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall57 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall57>(taken[57]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_SetException();
  }

  //  void QQmlJSTypePropagator::generate_CreateCallContext()
  void generate_CreateCallContext() override {
    if (taken[58]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall58 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall58>(taken[58]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CreateCallContext();
  }

  //  void QQmlJSTypePropagator::generate_PushCatchContext(int index, int
  //      name)
  void generate_PushCatchContext(int index, int name) override {
    if (taken[59]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall59 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall59>(taken[59]);
      call(this, index, name, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PushCatchContext(index, name);
  }

  //  void QQmlJSTypePropagator::generate_PushWithContext()
  void generate_PushWithContext() override {
    if (taken[60]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall60 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall60>(taken[60]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PushWithContext();
  }

  //  void QQmlJSTypePropagator::generate_PushBlockContext(int index)
  void generate_PushBlockContext(int index) override {
    if (taken[61]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall61 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall61>(taken[61]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PushBlockContext(index);
  }

  //  void QQmlJSTypePropagator::generate_CloneBlockContext()
  void generate_CloneBlockContext() override {
    if (taken[62]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall62 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall62>(taken[62]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CloneBlockContext();
  }

  //  void QQmlJSTypePropagator::generate_PushScriptContext(int index)
  void generate_PushScriptContext(int index) override {
    if (taken[63]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall63 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall63>(taken[63]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PushScriptContext(index);
  }

  //  void QQmlJSTypePropagator::generate_PopScriptContext()
  void generate_PopScriptContext() override {
    if (taken[64]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall64 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall64>(taken[64]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PopScriptContext();
  }

  //  void QQmlJSTypePropagator::generate_PopContext()
  void generate_PopContext() override {
    if (taken[65]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall65 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall65>(taken[65]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_PopContext();
  }

  //  void QQmlJSTypePropagator::generate_GetIterator(int iterator)
  void generate_GetIterator(int iterator) override {
    if (taken[66]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall66 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall66>(taken[66]);
      call(this, iterator, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_GetIterator(iterator);
  }

  //  void QQmlJSTypePropagator::generate_IteratorNext(int value, int
  //      offset)
  void generate_IteratorNext(int value, int offset) override {
    if (taken[67]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall67 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall67>(taken[67]);
      call(this, value, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_IteratorNext(value, offset);
  }

  //  void QQmlJSTypePropagator::generate_IteratorNextForYieldStar(int
  //      iterator, int object, int offset)
  void generate_IteratorNextForYieldStar(
      int iterator,
      int object,
      int offset) override {
    if (taken[68]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall68 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall68>(taken[68]);
      call(this, iterator, object, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_IteratorNextForYieldStar(iterator, object, offset);
  }

  //  void QQmlJSTypePropagator::generate_IteratorClose()
  void generate_IteratorClose() override {
    if (taken[69]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall69 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall69>(taken[69]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_IteratorClose();
  }

  //  void QQmlJSTypePropagator::generate_DestructureRestElement()
  void generate_DestructureRestElement() override {
    if (taken[70]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall70 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall70>(taken[70]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DestructureRestElement();
  }

  //  void QQmlJSTypePropagator::generate_DeleteProperty(int base, int
  //      index)
  void generate_DeleteProperty(int base, int index) override {
    if (taken[71]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall71 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall71>(taken[71]);
      call(this, base, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DeleteProperty(base, index);
  }

  //  void QQmlJSTypePropagator::generate_DeleteName(int name)
  void generate_DeleteName(int name) override {
    if (taken[72]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall72 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall72>(taken[72]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DeleteName(name);
  }

  //  void QQmlJSTypePropagator::generate_TypeofName(int name)
  void generate_TypeofName(int name) override {
    if (taken[73]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall73 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall73>(taken[73]);
      call(this, name, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_TypeofName(name);
  }

  //  void QQmlJSTypePropagator::generate_TypeofValue()
  void generate_TypeofValue() override {
    if (taken[74]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall74 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall74>(taken[74]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_TypeofValue();
  }

  //  void QQmlJSTypePropagator::generate_DeclareVar(int varName, int
  //      isDeletable)
  void generate_DeclareVar(int varName, int isDeletable) override {
    if (taken[75]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall75 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall75>(taken[75]);
      call(this, varName, isDeletable, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DeclareVar(varName, isDeletable);
  }

  //  void QQmlJSTypePropagator::generate_DefineArray(int argc, int args)
  void generate_DefineArray(int argc, int args) override {
    if (taken[76]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall76 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall76>(taken[76]);
      call(this, argc, args, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DefineArray(argc, args);
  }

  //  void QQmlJSTypePropagator::generate_DefineObjectLiteral(int
  //      internalClassId, int argc, int args)
  void generate_DefineObjectLiteral(
      int internalClassId,
      int argc,
      int args) override {
    if (taken[77]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall77 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall77>(taken[77]);
      call(this, internalClassId, argc, args, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_DefineObjectLiteral(internalClassId, argc, args);
  }

  //  void QQmlJSTypePropagator::generate_CreateClass(int classIndex, int
  //      heritage, int computedNames)
  void generate_CreateClass(
      int classIndex,
      int heritage,
      int computedNames) override {
    if (taken[78]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall78 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall78>(taken[78]);
      call(this, classIndex, heritage, computedNames, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CreateClass(classIndex, heritage, computedNames);
  }

  //  void QQmlJSTypePropagator::generate_CreateMappedArgumentsObject()
  void generate_CreateMappedArgumentsObject() override {
    if (taken[79]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall79 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall79>(taken[79]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CreateMappedArgumentsObject();
  }

  //  void QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject()
  void generate_CreateUnmappedArgumentsObject() override {
    if (taken[80]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall80 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall80>(taken[80]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject();
  }

  //  void QQmlJSTypePropagator::generate_CreateRestParameter(int argIndex)
  void generate_CreateRestParameter(int argIndex) override {
    if (taken[81]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall81 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall81>(taken[81]);
      call(this, argIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CreateRestParameter(argIndex);
  }

  //  void QQmlJSTypePropagator::generate_ConvertThisToObject()
  void generate_ConvertThisToObject() override {
    if (taken[82]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall82 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall82>(taken[82]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ConvertThisToObject();
  }

  //  void QQmlJSTypePropagator::generate_LoadSuperConstructor()
  void generate_LoadSuperConstructor() override {
    if (taken[83]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall83 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall83>(taken[83]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_LoadSuperConstructor();
  }

  //  void QQmlJSTypePropagator::generate_ToObject()
  void generate_ToObject() override {
    if (taken[84]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall84 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall84>(taken[84]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ToObject();
  }

  //  void QQmlJSTypePropagator::generate_Jump(int offset)
  void generate_Jump(int offset) override {
    if (taken[85]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall85 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall85>(taken[85]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Jump(offset);
  }

  //  void QQmlJSTypePropagator::generate_JumpTrue(int offset)
  void generate_JumpTrue(int offset) override {
    if (taken[86]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall86 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall86>(taken[86]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_JumpTrue(offset);
  }

  //  void QQmlJSTypePropagator::generate_JumpFalse(int offset)
  void generate_JumpFalse(int offset) override {
    if (taken[87]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall87 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall87>(taken[87]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_JumpFalse(offset);
  }

  //  void QQmlJSTypePropagator::generate_JumpNoException(int offset)
  void generate_JumpNoException(int offset) override {
    if (taken[88]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall88 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall88>(taken[88]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_JumpNoException(offset);
  }

  //  void QQmlJSTypePropagator::generate_JumpNotUndefined(int offset)
  void generate_JumpNotUndefined(int offset) override {
    if (taken[89]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall89 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall89>(taken[89]);
      call(this, offset, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_JumpNotUndefined(offset);
  }

  //  void QQmlJSTypePropagator::generate_CheckException()
  void generate_CheckException() override {
    if (taken[90]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall90 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall90>(taken[90]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CheckException();
  }

  //  void QQmlJSTypePropagator::generate_CmpEqNull()
  void generate_CmpEqNull() override {
    if (taken[91]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall91 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall91>(taken[91]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpEqNull();
  }

  //  void QQmlJSTypePropagator::generate_CmpNeNull()
  void generate_CmpNeNull() override {
    if (taken[92]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall92 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall92>(taken[92]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpNeNull();
  }

  //  void QQmlJSTypePropagator::generate_CmpEqInt(int lhsConst)
  void generate_CmpEqInt(int lhsConst) override {
    if (taken[93]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall93 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall93>(taken[93]);
      call(this, lhsConst, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpEqInt(lhsConst);
  }

  //  void QQmlJSTypePropagator::generate_CmpNeInt(int lhs)
  void generate_CmpNeInt(int lhs) override {
    if (taken[94]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall94 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall94>(taken[94]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpNeInt(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpEq(int lhs)
  void generate_CmpEq(int lhs) override {
    if (taken[95]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall95 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall95>(taken[95]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpEq(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpNe(int lhs)
  void generate_CmpNe(int lhs) override {
    if (taken[96]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall96 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall96>(taken[96]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpNe(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpGt(int lhs)
  void generate_CmpGt(int lhs) override {
    if (taken[97]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall97 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall97>(taken[97]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpGt(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpGe(int lhs)
  void generate_CmpGe(int lhs) override {
    if (taken[98]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall98 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall98>(taken[98]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpGe(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpLt(int lhs)
  void generate_CmpLt(int lhs) override {
    if (taken[99]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall99 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall99>(taken[99]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpLt(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpLe(int lhs)
  void generate_CmpLe(int lhs) override {
    if (taken[100]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall100 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall100>(taken[100]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpLe(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpStrictEqual(int lhs)
  void generate_CmpStrictEqual(int lhs) override {
    if (taken[101]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall101 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall101>(taken[101]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpStrictEqual(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpStrictNotEqual(int lhs)
  void generate_CmpStrictNotEqual(int lhs) override {
    if (taken[102]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall102 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall102>(taken[102]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpStrictNotEqual(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpIn(int lhs)
  void generate_CmpIn(int lhs) override {
    if (taken[103]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall103 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall103>(taken[103]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpIn(lhs);
  }

  //  void QQmlJSTypePropagator::generate_CmpInstanceOf(int lhs)
  void generate_CmpInstanceOf(int lhs) override {
    if (taken[104]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall104 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall104>(taken[104]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_CmpInstanceOf(lhs);
  }

  //  void QQmlJSTypePropagator::generate_As(int lhs)
  void generate_As(int lhs) override {
    if (taken[105]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall105 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall105>(taken[105]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_As(lhs);
  }

  //  void QQmlJSTypePropagator::generate_UNot()
  void generate_UNot() override {
    if (taken[106]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall106 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall106>(taken[106]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UNot();
  }

  //  void QQmlJSTypePropagator::generate_UPlus()
  void generate_UPlus() override {
    if (taken[107]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall107 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall107>(taken[107]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UPlus();
  }

  //  void QQmlJSTypePropagator::generate_UMinus()
  void generate_UMinus() override {
    if (taken[108]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall108 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall108>(taken[108]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UMinus();
  }

  //  void QQmlJSTypePropagator::generate_UCompl()
  void generate_UCompl() override {
    if (taken[109]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall109 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall109>(taken[109]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UCompl();
  }

  //  void QQmlJSTypePropagator::generate_Increment()
  void generate_Increment() override {
    if (taken[110]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall110 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall110>(taken[110]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Increment();
  }

  //  void QQmlJSTypePropagator::generate_Decrement()
  void generate_Decrement() override {
    if (taken[111]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall111 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall111>(taken[111]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Decrement();
  }

  //  void QQmlJSTypePropagator::generate_Add(int lhs)
  void generate_Add(int lhs) override {
    if (taken[112]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall112 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall112>(taken[112]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Add(lhs);
  }

  //  void QQmlJSTypePropagator::generate_BitAnd(int lhs)
  void generate_BitAnd(int lhs) override {
    if (taken[113]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall113 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall113>(taken[113]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitAnd(lhs);
  }

  //  void QQmlJSTypePropagator::generate_BitOr(int lhs)
  void generate_BitOr(int lhs) override {
    if (taken[114]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall114 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall114>(taken[114]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitOr(lhs);
  }

  //  void QQmlJSTypePropagator::generate_BitXor(int lhs)
  void generate_BitXor(int lhs) override {
    if (taken[115]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall115 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall115>(taken[115]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitXor(lhs);
  }

  //  void QQmlJSTypePropagator::generate_UShr(int lhs)
  void generate_UShr(int lhs) override {
    if (taken[116]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall116 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall116>(taken[116]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UShr(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Shr(int lhs)
  void generate_Shr(int lhs) override {
    if (taken[117]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall117 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall117>(taken[117]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Shr(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Shl(int lhs)
  void generate_Shl(int lhs) override {
    if (taken[118]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall118 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall118>(taken[118]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Shl(lhs);
  }

  //  void QQmlJSTypePropagator::generate_BitAndConst(int rhsConst)
  void generate_BitAndConst(int rhsConst) override {
    if (taken[119]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall119 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall119>(taken[119]);
      call(this, rhsConst, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitAndConst(rhsConst);
  }

  //  void QQmlJSTypePropagator::generate_BitOrConst(int rhsConst)
  void generate_BitOrConst(int rhsConst) override {
    if (taken[120]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall120 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall120>(taken[120]);
      call(this, rhsConst, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitOrConst(rhsConst);
  }

  //  void QQmlJSTypePropagator::generate_BitXorConst(int rhsConst)
  void generate_BitXorConst(int rhsConst) override {
    if (taken[121]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall121 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall121>(taken[121]);
      call(this, rhsConst, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_BitXorConst(rhsConst);
  }

  //  void QQmlJSTypePropagator::generate_UShrConst(int rhsConst)
  void generate_UShrConst(int rhsConst) override {
    if (taken[122]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall122 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall122>(taken[122]);
      call(this, rhsConst, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_UShrConst(rhsConst);
  }

  //  void QQmlJSTypePropagator::generate_ShrConst(int rhs)
  void generate_ShrConst(int rhs) override {
    if (taken[123]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall123 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall123>(taken[123]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ShrConst(rhs);
  }

  //  void QQmlJSTypePropagator::generate_ShlConst(int rhs)
  void generate_ShlConst(int rhs) override {
    if (taken[124]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall124 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall124>(taken[124]);
      call(this, rhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ShlConst(rhs);
  }

  //  void QQmlJSTypePropagator::generate_Exp(int lhs)
  void generate_Exp(int lhs) override {
    if (taken[125]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall125 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall125>(taken[125]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Exp(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Mul(int lhs)
  void generate_Mul(int lhs) override {
    if (taken[126]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall126 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall126>(taken[126]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Mul(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Div(int lhs)
  void generate_Div(int lhs) override {
    if (taken[127]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall127 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall127>(taken[127]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Div(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Mod(int lhs)
  void generate_Mod(int lhs) override {
    if (taken[128]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall128 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall128>(taken[128]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Mod(lhs);
  }

  //  void QQmlJSTypePropagator::generate_Sub(int lhs)
  void generate_Sub(int lhs) override {
    if (taken[129]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall129 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall129>(taken[129]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_Sub(lhs);
  }

  //  void
  //      QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(in
  //      t firstReg, int count)
  void generate_InitializeBlockDeadTemporalZone(
      int firstReg,
      int count) override {
    if (taken[130]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall130 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall130>(taken[130]);
      call(this, firstReg, count, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(firstReg, count);
  }

  //  void QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined()
  void generate_ThrowOnNullOrUndefined() override {
    if (taken[131]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall131 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall131>(taken[131]);
      call(this, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined();
  }

  //  void QQmlJSTypePropagator::generate_GetTemplateObject(int index)
  void generate_GetTemplateObject(int index) override {
    if (taken[132]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall132 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall132>(taken[132]);
      call(this, index, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_GetTemplateObject(index);
  }

  //  void QQmlJSTypePropagator::endInstruction(QV4::Moth::Instr::Type
  //      instr)
  void endInstruction(QV4::Moth::Instr::Type instr) override {
    if (taken[133]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall133 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall133>(taken[133]);
      call(this, static_cast<int>(instr), &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::endInstruction(instr);
  }

  //  void QQmlJSTypePropagator::handleUnqualifiedAccess(const QString
  //      &name, bool isMethod) const
  void handleUnqualifiedAccess(
      const QString &name,
      bool isMethod) const override {
    if (taken[134]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall134 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall134>(taken[134]);
      call(this, &name, isMethod, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::handleUnqualifiedAccess(name, isMethod);
  }

  //  void QQmlJSTypePropagator::handleUnqualifiedAccessAndContextPropertie
  //      s(const QString &name, bool isMethod) const
  void handleUnqualifiedAccessAndContextProperties(
      const QString &name,
      bool isMethod) const override {
    if (taken[135]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall135 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall135>(taken[135]);
      call(this, &name, isMethod, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(name, isMethod);
  }

  //  bool QQmlJSTypePropagator::handleImportNamespaceLookup(const QString
  //      &propertyName)
  bool handleImportNamespaceLookup(const QString &propertyName) override {
    if (taken[136]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall136 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall136>(taken[136]);
      bool given = call(this, &propertyName, &handled);
      if (handled) return given;
    }
    return QQmlJSTypePropagator::handleImportNamespaceLookup(propertyName);
  }

  //  void QQmlJSTypePropagator::handleLookupError(const QString
  //      &propertyName)
  void handleLookupError(const QString &propertyName) override {
    if (taken[137]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall137 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall137>(taken[137]);
      call(this, &propertyName, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::handleLookupError(propertyName);
  }

  //  bool QQmlJSTypePropagator::checkForEnumProblems(QQmlJSRegisterContent
  //      base, const QString &propertyName)
  bool checkForEnumProblems(
      QQmlJSRegisterContent base,
      const QString &propertyName) override {
    if (taken[138]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall138 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall138>(taken[138]);
      bool given = call(this, &base, &propertyName, &handled);
      if (handled) return given;
    }
    return QQmlJSTypePropagator::checkForEnumProblems(base, propertyName);
  }

  //  void QQmlJSTypePropagator::warnAboutTypeCoercion(int lhs)
  void warnAboutTypeCoercion(int lhs) override {
    if (taken[139]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall139 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall139>(taken[139]);
      call(this, lhs, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::warnAboutTypeCoercion(lhs);
  }

  //  void QQmlJSTypePropagator::generate_StoreNameCommon(int nameIndex)
  void generate_StoreNameCommon(int nameIndex) override {
    if (taken[140]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall140 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall140>(taken[140]);
      call(this, nameIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::generate_StoreNameCommon(nameIndex);
  }

  //  void QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(const
  //      QString &methodName)
  void propagateTranslationMethod_SAcheck(
      const QString &methodName) override {
    if (taken[141]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall141 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall141>(taken[141]);
      call(this, &methodName, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(methodName);
  }

  //  void QQmlJSTypePropagator::propagatePropertyLookup(const QString
  //      &name, int lookupIndex)
  void propagatePropertyLookup(
      const QString &name,
      int lookupIndex) override {
    if (taken[142]) {
      int handled = 0;
      CuteQQmlJSTypePropagatorCall142 call = reinterpret_cast<CuteQQmlJSTypePropagatorCall142>(taken[142]);
      call(this, &name, lookupIndex, &handled);
      if (handled) return;
    }
    QQmlJSTypePropagator::propagatePropertyLookup(name, lookupIndex);
  }
};

//  BlocksAndAnnotations QQmlJSTypePropagator::run(const Function
//      *m_function)
extern "C" Q_DECL_EXPORT
QQmlJSCompilePass::BlocksAndAnnotations *ritual_ZN20QQmlJSTypePropagator3runEPKN17QQmlJSCompilePass8FunctionE(
    QQmlJSTypePropagator *self,
    const QQmlJSCompilePass::Function *m_function) {
  return new QQmlJSCompilePass::BlocksAndAnnotations(self->run(m_function));
}

//  void QQmlJSTypePropagator::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_RetEv(
    QQmlJSTypePropagator *self) {
  self->generate_Ret();
}

//  void QQmlJSTypePropagator::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_DebugEv(
    QQmlJSTypePropagator *self) {
  self->generate_Debug();
}

//  void QQmlJSTypePropagator::generate_LoadConst(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_LoadConstEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_LoadConst(index);
}

//  void QQmlJSTypePropagator::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_LoadZeroEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadZero();
}

//  void QQmlJSTypePropagator::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_LoadTrueEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadTrue();
}

//  void QQmlJSTypePropagator::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_LoadFalseEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadFalse();
}

//  void QQmlJSTypePropagator::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_LoadNullEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadNull();
}

//  void QQmlJSTypePropagator::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22generate_LoadUndefinedEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadUndefined();
}

//  void QQmlJSTypePropagator::generate_LoadInt(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator16generate_LoadIntEi(
    QQmlJSTypePropagator *self,
    int value) {
  self->generate_LoadInt(value);
}

//  void QQmlJSTypePropagator::generate_MoveConst(int constIndex, int
//      destTemp)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_MoveConstEii(
    QQmlJSTypePropagator *self,
    int constIndex,
    int destTemp) {
  self->generate_MoveConst(constIndex, destTemp);
}

//  void QQmlJSTypePropagator::generate_LoadReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator16generate_LoadRegEi(
    QQmlJSTypePropagator *self,
    int reg) {
  self->generate_LoadReg(reg);
}

//  void QQmlJSTypePropagator::generate_StoreReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_StoreRegEi(
    QQmlJSTypePropagator *self,
    int reg) {
  self->generate_StoreReg(reg);
}

//  void QQmlJSTypePropagator::generate_MoveReg(int srcReg, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator16generate_MoveRegEii(
    QQmlJSTypePropagator *self,
    int srcReg,
    int destReg) {
  self->generate_MoveReg(srcReg, destReg);
}

//  void QQmlJSTypePropagator::generate_LoadImport(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_LoadImportEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_LoadImport(index);
}

//  void QQmlJSTypePropagator::generate_LoadLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_LoadLocalEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_LoadLocal(index);
}

//  void QQmlJSTypePropagator::generate_StoreLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_StoreLocalEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_StoreLocal(index);
}

//  void QQmlJSTypePropagator::generate_LoadScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_LoadScopedLocalEii(
    QQmlJSTypePropagator *self,
    int scope,
    int index) {
  self->generate_LoadScopedLocal(scope, index);
}

//  void QQmlJSTypePropagator::generate_StoreScopedLocal(int scope, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_StoreScopedLocalEii(
    QQmlJSTypePropagator *self,
    int scope,
    int index) {
  self->generate_StoreScopedLocal(scope, index);
}

//  void QQmlJSTypePropagator::generate_LoadRuntimeString(int stringId)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_LoadRuntimeStringEi(
    QQmlJSTypePropagator *self,
    int stringId) {
  self->generate_LoadRuntimeString(stringId);
}

//  void QQmlJSTypePropagator::generate_MoveRegExp(int regExpId, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_MoveRegExpEii(
    QQmlJSTypePropagator *self,
    int regExpId,
    int destReg) {
  self->generate_MoveRegExp(regExpId, destReg);
}

//  void QQmlJSTypePropagator::generate_LoadClosure(int value)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_LoadClosureEi(
    QQmlJSTypePropagator *self,
    int value) {
  self->generate_LoadClosure(value);
}

//  void QQmlJSTypePropagator::generate_LoadName(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_LoadNameEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->generate_LoadName(nameIndex);
}

//  void QQmlJSTypePropagator::generate_LoadGlobalLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_LoadGlobalLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_LoadGlobalLookup(index);
}

//  void QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_LoadQmlContextPropertyLookup(index);
}

//  void QQmlJSTypePropagator::generate_StoreNameSloppy(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_StoreNameSloppyEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->generate_StoreNameSloppy(nameIndex);
}

//  void QQmlJSTypePropagator::generate_StoreNameStrict(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_StoreNameStrictEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->generate_StoreNameStrict(name);
}

//  void QQmlJSTypePropagator::generate_LoadElement(int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_LoadElementEi(
    QQmlJSTypePropagator *self,
    int base) {
  self->generate_LoadElement(base);
}

//  void QQmlJSTypePropagator::generate_StoreElement(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_StoreElementEii(
    QQmlJSTypePropagator *self,
    int base,
    int index) {
  self->generate_StoreElement(base, index);
}

//  void QQmlJSTypePropagator::generate_LoadProperty(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_LoadPropertyEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->generate_LoadProperty(nameIndex);
}

//  void QQmlJSTypePropagator::generate_LoadOptionalProperty(int name, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator29generate_LoadOptionalPropertyEii(
    QQmlJSTypePropagator *self,
    int name,
    int offset) {
  self->generate_LoadOptionalProperty(name, offset);
}

//  void QQmlJSTypePropagator::generate_GetLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_GetLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_GetLookup(index);
}

//  void QQmlJSTypePropagator::generate_GetOptionalLookup(int index, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_GetOptionalLookupEii(
    QQmlJSTypePropagator *self,
    int index,
    int offset) {
  self->generate_GetOptionalLookup(index, offset);
}

//  void QQmlJSTypePropagator::generate_StoreProperty(int name, int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22generate_StorePropertyEii(
    QQmlJSTypePropagator *self,
    int name,
    int base) {
  self->generate_StoreProperty(name, base);
}

//  void QQmlJSTypePropagator::generate_SetLookup(int index, int base)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_SetLookupEii(
    QQmlJSTypePropagator *self,
    int index,
    int base) {
  self->generate_SetLookup(index, base);
}

//  void QQmlJSTypePropagator::generate_LoadSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_LoadSuperPropertyEi(
    QQmlJSTypePropagator *self,
    int property) {
  self->generate_LoadSuperProperty(property);
}

//  void QQmlJSTypePropagator::generate_StoreSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator27generate_StoreSuperPropertyEi(
    QQmlJSTypePropagator *self,
    int property) {
  self->generate_StoreSuperProperty(property);
}

//  void QQmlJSTypePropagator::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_YieldEv(
    QQmlJSTypePropagator *self) {
  self->generate_Yield();
}

//  void QQmlJSTypePropagator::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_YieldStarEv(
    QQmlJSTypePropagator *self) {
  self->generate_YieldStar();
}

//  void QQmlJSTypePropagator::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15generate_ResumeEi(
    QQmlJSTypePropagator *self,
    int a0) {
  self->generate_Resume(a0);
}

//  void QQmlJSTypePropagator::generate_CallValue(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_CallValueEiii(
    QQmlJSTypePropagator *self,
    int name,
    int argc,
    int argv) {
  self->generate_CallValue(name, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallWithReceiver(int name, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_CallWithReceiverEiiii(
    QQmlJSTypePropagator *self,
    int name,
    int thisObject,
    int argc,
    int argv) {
  self->generate_CallWithReceiver(name, thisObject, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallProperty(int name, int base, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_CallPropertyEiiii(
    QQmlJSTypePropagator *self,
    int name,
    int base,
    int argc,
    int argv) {
  self->generate_CallProperty(name, base, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallPropertyLookup(int lookupIndex,
//      int base, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator27generate_CallPropertyLookupEiiii(
    QQmlJSTypePropagator *self,
    int lookupIndex,
    int base,
    int argc,
    int argv) {
  self->generate_CallPropertyLookup(lookupIndex, base, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallName(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_CallNameEiii(
    QQmlJSTypePropagator *self,
    int name,
    int argc,
    int argv) {
  self->generate_CallName(name, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallPossiblyDirectEval(int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator31generate_CallPossiblyDirectEvalEii(
    QQmlJSTypePropagator *self,
    int argc,
    int argv) {
  self->generate_CallPossiblyDirectEval(argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallGlobalLookup(int index, int argc,
//      int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_CallGlobalLookupEiii(
    QQmlJSTypePropagator *self,
    int index,
    int argc,
    int argv) {
  self->generate_CallGlobalLookup(index, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(int
//      index, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSTypePropagator *self,
    int index,
    int argc,
    int argv) {
  self->generate_CallQmlContextPropertyLookup(index, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallWithSpread(int func, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_CallWithSpreadEiiii(
    QQmlJSTypePropagator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->generate_CallWithSpread(func, thisObject, argc, argv);
}

//  void QQmlJSTypePropagator::generate_TailCall(int func, int thisObject,
//      int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_TailCallEiiii(
    QQmlJSTypePropagator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->generate_TailCall(func, thisObject, argc, argv);
}

//  void QQmlJSTypePropagator::generate_Construct(int func, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_ConstructEiii(
    QQmlJSTypePropagator *self,
    int func,
    int argc,
    int argv) {
  self->generate_Construct(func, argc, argv);
}

//  void QQmlJSTypePropagator::generate_ConstructWithSpread(int func, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator28generate_ConstructWithSpreadEiii(
    QQmlJSTypePropagator *self,
    int func,
    int argc,
    int argv) {
  self->generate_ConstructWithSpread(func, argc, argv);
}

//  void QQmlJSTypePropagator::generate_SetUnwindHandler(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_SetUnwindHandlerEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_SetUnwindHandler(offset);
}

//  void QQmlJSTypePropagator::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_UnwindDispatchEv(
    QQmlJSTypePropagator *self) {
  self->generate_UnwindDispatch();
}

//  void QQmlJSTypePropagator::generate_UnwindToLabel(int level, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22generate_UnwindToLabelEii(
    QQmlJSTypePropagator *self,
    int level,
    int offset) {
  self->generate_UnwindToLabel(level, offset);
}

//  void QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator30generate_DeadTemporalZoneCheckEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->generate_DeadTemporalZoneCheck(name);
}

//  void QQmlJSTypePropagator::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_ThrowExceptionEv(
    QQmlJSTypePropagator *self) {
  self->generate_ThrowException();
}

//  void QQmlJSTypePropagator::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_GetExceptionEv(
    QQmlJSTypePropagator *self) {
  self->generate_GetException();
}

//  void QQmlJSTypePropagator::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_SetExceptionEv(
    QQmlJSTypePropagator *self) {
  self->generate_SetException();
}

//  void QQmlJSTypePropagator::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_CreateCallContextEv(
    QQmlJSTypePropagator *self) {
  self->generate_CreateCallContext();
}

//  void QQmlJSTypePropagator::generate_PushCatchContext(int index, int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_PushCatchContextEii(
    QQmlJSTypePropagator *self,
    int index,
    int name) {
  self->generate_PushCatchContext(index, name);
}

//  void QQmlJSTypePropagator::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_PushWithContextEv(
    QQmlJSTypePropagator *self) {
  self->generate_PushWithContext();
}

//  void QQmlJSTypePropagator::generate_PushBlockContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_PushBlockContextEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_PushBlockContext(index);
}

//  void QQmlJSTypePropagator::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_CloneBlockContextEv(
    QQmlJSTypePropagator *self) {
  self->generate_CloneBlockContext();
}

//  void QQmlJSTypePropagator::generate_PushScriptContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_PushScriptContextEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_PushScriptContext(index);
}

//  void QQmlJSTypePropagator::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_PopScriptContextEv(
    QQmlJSTypePropagator *self) {
  self->generate_PopScriptContext();
}

//  void QQmlJSTypePropagator::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_PopContextEv(
    QQmlJSTypePropagator *self) {
  self->generate_PopContext();
}

//  void QQmlJSTypePropagator::generate_GetIterator(int iterator)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_GetIteratorEi(
    QQmlJSTypePropagator *self,
    int iterator) {
  self->generate_GetIterator(iterator);
}

//  void QQmlJSTypePropagator::generate_IteratorNext(int value, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21generate_IteratorNextEii(
    QQmlJSTypePropagator *self,
    int value,
    int offset) {
  self->generate_IteratorNext(value, offset);
}

//  void QQmlJSTypePropagator::generate_IteratorNextForYieldStar(int
//      iterator, int object, int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator33generate_IteratorNextForYieldStarEiii(
    QQmlJSTypePropagator *self,
    int iterator,
    int object,
    int offset) {
  self->generate_IteratorNextForYieldStar(iterator, object, offset);
}

//  void QQmlJSTypePropagator::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22generate_IteratorCloseEv(
    QQmlJSTypePropagator *self) {
  self->generate_IteratorClose();
}

//  void QQmlJSTypePropagator::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator31generate_DestructureRestElementEv(
    QQmlJSTypePropagator *self) {
  self->generate_DestructureRestElement();
}

//  void QQmlJSTypePropagator::generate_DeleteProperty(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_DeletePropertyEii(
    QQmlJSTypePropagator *self,
    int base,
    int index) {
  self->generate_DeleteProperty(base, index);
}

//  void QQmlJSTypePropagator::generate_DeleteName(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_DeleteNameEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->generate_DeleteName(name);
}

//  void QQmlJSTypePropagator::generate_TypeofName(int name)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_TypeofNameEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->generate_TypeofName(name);
}

//  void QQmlJSTypePropagator::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_TypeofValueEv(
    QQmlJSTypePropagator *self) {
  self->generate_TypeofValue();
}

//  void QQmlJSTypePropagator::generate_DeclareVar(int varName, int
//      isDeletable)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_DeclareVarEii(
    QQmlJSTypePropagator *self,
    int varName,
    int isDeletable) {
  self->generate_DeclareVar(varName, isDeletable);
}

//  void QQmlJSTypePropagator::generate_DefineArray(int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_DefineArrayEii(
    QQmlJSTypePropagator *self,
    int argc,
    int args) {
  self->generate_DefineArray(argc, args);
}

//  void QQmlJSTypePropagator::generate_DefineObjectLiteral(int
//      internalClassId, int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator28generate_DefineObjectLiteralEiii(
    QQmlJSTypePropagator *self,
    int internalClassId,
    int argc,
    int args) {
  self->generate_DefineObjectLiteral(internalClassId, argc, args);
}

//  void QQmlJSTypePropagator::generate_CreateClass(int classIndex, int
//      heritage, int computedNames)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_CreateClassEiii(
    QQmlJSTypePropagator *self,
    int classIndex,
    int heritage,
    int computedNames) {
  self->generate_CreateClass(classIndex, heritage, computedNames);
}

//  void QQmlJSTypePropagator::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator36generate_CreateMappedArgumentsObjectEv(
    QQmlJSTypePropagator *self) {
  self->generate_CreateMappedArgumentsObject();
}

//  void QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSTypePropagator *self) {
  self->generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSTypePropagator::generate_CreateRestParameter(int argIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator28generate_CreateRestParameterEi(
    QQmlJSTypePropagator *self,
    int argIndex) {
  self->generate_CreateRestParameter(argIndex);
}

//  void QQmlJSTypePropagator::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator28generate_ConvertThisToObjectEv(
    QQmlJSTypePropagator *self) {
  self->generate_ConvertThisToObject();
}

//  void QQmlJSTypePropagator::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator29generate_LoadSuperConstructorEv(
    QQmlJSTypePropagator *self) {
  self->generate_LoadSuperConstructor();
}

//  void QQmlJSTypePropagator::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_ToObjectEv(
    QQmlJSTypePropagator *self) {
  self->generate_ToObject();
}

//  void QQmlJSTypePropagator::generate_Jump(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator13generate_JumpEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_Jump(offset);
}

//  void QQmlJSTypePropagator::generate_JumpTrue(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_JumpTrueEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_JumpTrue(offset);
}

//  void QQmlJSTypePropagator::generate_JumpFalse(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_JumpFalseEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_JumpFalse(offset);
}

//  void QQmlJSTypePropagator::generate_JumpNoException(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_JumpNoExceptionEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_JumpNoException(offset);
}

//  void QQmlJSTypePropagator::generate_JumpNotUndefined(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_JumpNotUndefinedEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->generate_JumpNotUndefined(offset);
}

//  void QQmlJSTypePropagator::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_CheckExceptionEv(
    QQmlJSTypePropagator *self) {
  self->generate_CheckException();
}

//  void QQmlJSTypePropagator::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_CmpEqNullEv(
    QQmlJSTypePropagator *self) {
  self->generate_CmpEqNull();
}

//  void QQmlJSTypePropagator::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_CmpNeNullEv(
    QQmlJSTypePropagator *self) {
  self->generate_CmpNeNull();
}

//  void QQmlJSTypePropagator::generate_CmpEqInt(int lhsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_CmpEqIntEi(
    QQmlJSTypePropagator *self,
    int lhsConst) {
  self->generate_CmpEqInt(lhsConst);
}

//  void QQmlJSTypePropagator::generate_CmpNeInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_CmpNeIntEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpNeInt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpEq(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpEqEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpEq(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpNe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpNeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpNe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpGt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpGtEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpGt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpGe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpGeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpGe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpLt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpLtEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpLt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpLe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpLeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpLe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpStrictEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23generate_CmpStrictEqualEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpStrictEqual(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpStrictNotEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_CmpStrictNotEqualEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpStrictNotEqual(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpIn(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_CmpInEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpIn(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpInstanceOf(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22generate_CmpInstanceOfEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_CmpInstanceOf(lhs);
}

//  void QQmlJSTypePropagator::generate_As(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator11generate_AsEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_As(lhs);
}

//  void QQmlJSTypePropagator::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator13generate_UNotEv(
    QQmlJSTypePropagator *self) {
  self->generate_UNot();
}

//  void QQmlJSTypePropagator::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_UPlusEv(
    QQmlJSTypePropagator *self) {
  self->generate_UPlus();
}

//  void QQmlJSTypePropagator::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15generate_UMinusEv(
    QQmlJSTypePropagator *self) {
  self->generate_UMinus();
}

//  void QQmlJSTypePropagator::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15generate_UComplEv(
    QQmlJSTypePropagator *self) {
  self->generate_UCompl();
}

//  void QQmlJSTypePropagator::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_IncrementEv(
    QQmlJSTypePropagator *self) {
  self->generate_Increment();
}

//  void QQmlJSTypePropagator::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_DecrementEv(
    QQmlJSTypePropagator *self) {
  self->generate_Decrement();
}

//  void QQmlJSTypePropagator::generate_Add(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_AddEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Add(lhs);
}

//  void QQmlJSTypePropagator::generate_BitAnd(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15generate_BitAndEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_BitAnd(lhs);
}

//  void QQmlJSTypePropagator::generate_BitOr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14generate_BitOrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_BitOr(lhs);
}

//  void QQmlJSTypePropagator::generate_BitXor(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15generate_BitXorEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_BitXor(lhs);
}

//  void QQmlJSTypePropagator::generate_UShr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator13generate_UShrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_UShr(lhs);
}

//  void QQmlJSTypePropagator::generate_Shr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_ShrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Shr(lhs);
}

//  void QQmlJSTypePropagator::generate_Shl(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_ShlEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Shl(lhs);
}

//  void QQmlJSTypePropagator::generate_BitAndConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_BitAndConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->generate_BitAndConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_BitOrConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19generate_BitOrConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->generate_BitOrConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_BitXorConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20generate_BitXorConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->generate_BitXorConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_UShrConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18generate_UShrConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->generate_UShrConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_ShrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_ShrConstEi(
    QQmlJSTypePropagator *self,
    int rhs) {
  self->generate_ShrConst(rhs);
}

//  void QQmlJSTypePropagator::generate_ShlConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17generate_ShlConstEi(
    QQmlJSTypePropagator *self,
    int rhs) {
  self->generate_ShlConst(rhs);
}

//  void QQmlJSTypePropagator::generate_Exp(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_ExpEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Exp(lhs);
}

//  void QQmlJSTypePropagator::generate_Mul(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_MulEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Mul(lhs);
}

//  void QQmlJSTypePropagator::generate_Div(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_DivEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Div(lhs);
}

//  void QQmlJSTypePropagator::generate_Mod(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_ModEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Mod(lhs);
}

//  void QQmlJSTypePropagator::generate_Sub(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator12generate_SubEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->generate_Sub(lhs);
}

//  void QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(int
//      firstReg, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSTypePropagator *self,
    int firstReg,
    int count) {
  self->generate_InitializeBlockDeadTemporalZone(firstReg, count);
}

//  void QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSTypePropagator *self) {
  self->generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSTypePropagator::generate_GetTemplateObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_GetTemplateObjectEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->generate_GetTemplateObject(index);
}

//  Verdict QQmlJSTypePropagator::startInstruction(QV4::Moth::Instr::Type
//      instr)
extern "C" Q_DECL_EXPORT
QV4::Moth::ByteCodeHandler::Verdict ritual_ZN20QQmlJSTypePropagator16startInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSTypePropagator *self,
    QV4::Moth::Instr::Type instr) {
  return self->startInstruction(instr);
}

//  void QQmlJSTypePropagator::endInstruction(QV4::Moth::Instr::Type instr)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSTypePropagator *self,
    QV4::Moth::Instr::Type instr) {
  self->endInstruction(instr);
}

//  void QQmlJSTypePropagator::handleUnqualifiedAccess(const QString &name,
//      bool isMethod) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK7QStringb(
    const QQmlJSTypePropagator *self,
    const QString *name,
    bool isMethod) {
  self->handleUnqualifiedAccess(*name, isMethod);
}

//  void
//      QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(con
//      st QString &name, bool isMethod) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAndContextPropertiesERK7QStringb(
    const QQmlJSTypePropagator *self,
    const QString *name,
    bool isMethod) {
  self->handleUnqualifiedAccessAndContextProperties(*name, isMethod);
}

//  bool QQmlJSTypePropagator::handleImportNamespaceLookup(const QString
//      &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator27handleImportNamespaceLookupERK7QString(
    QQmlJSTypePropagator *self,
    const QString *propertyName) {
  return self->handleImportNamespaceLookup(*propertyName);
}

//  void QQmlJSTypePropagator::handleLookupError(const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QString(
    QQmlJSTypePropagator *self,
    const QString *propertyName) {
  self->handleLookupError(*propertyName);
}

//  bool QQmlJSTypePropagator::checkForEnumProblems(QQmlJSRegisterContent
//      base, const QString &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQmlJSRegisterContentRK7QString(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *base,
    const QString *propertyName) {
  return self->checkForEnumProblems(*base, *propertyName);
}

//  void QQmlJSTypePropagator::warnAboutTypeCoercion(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->warnAboutTypeCoercion(lhs);
}

//  void QQmlJSTypePropagator::checkConversion(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15checkConversionE21QQmlJSRegisterContentS0_(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to) {
  self->checkConversion(*from, *to);
}

//  void QQmlJSTypePropagator::generateUnaryArithmeticOperation(QQmlJSTypeRes
//      olver::UnaryOperator op)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator32generateUnaryArithmeticOperationEN18QQmlJSTypeResolver13UnaryOperatorE(
    QQmlJSTypePropagator *self,
    QQmlJSTypeResolver::UnaryOperator op) {
  self->generateUnaryArithmeticOperation(op);
}

//  QQmlJSRegisterContent
//      QQmlJSTypePropagator::propagateBinaryOperation(QSOperator::Op op, int
//      lhs)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN20QQmlJSTypePropagator24propagateBinaryOperationEN10QSOperator2OpEi(
    QQmlJSTypePropagator *self,
    QSOperator::Op op,
    int lhs) {
  return new QQmlJSRegisterContent(self->propagateBinaryOperation(op, lhs));
}

//  void
//      QQmlJSTypePropagator::generateBinaryArithmeticOperation(QSOperator::O
//      p op, int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator33generateBinaryArithmeticOperationEN10QSOperator2OpEi(
    QQmlJSTypePropagator *self,
    QSOperator::Op op,
    int lhs) {
  self->generateBinaryArithmeticOperation(op, lhs);
}

//  void QQmlJSTypePropagator::generateBinaryConstArithmeticOperation(QSOpera
//      tor::Op op)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator38generateBinaryConstArithmeticOperationEN10QSOperator2OpE(
    QQmlJSTypePropagator *self,
    QSOperator::Op op) {
  self->generateBinaryConstArithmeticOperation(op);
}

//  void QQmlJSTypePropagator::generate_StoreNameCommon(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->generate_StoreNameCommon(nameIndex);
}

//  void QQmlJSTypePropagator::propagateCall(const QList<QQmlJSMetaMethod>
//      &methods, int argc, int argv, QQmlJSRegisterContent scope)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator13propagateCallERK5QListI16QQmlJSMetaMethodEii21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    const QList<QQmlJSMetaMethod> *methods,
    int argc,
    int argv,
    const QQmlJSRegisterContent *scope) {
  self->propagateCall(*methods, argc, argv, *scope);
}

//  void QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(const
//      QString &methodName)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator34propagateTranslationMethod_SAcheckERK7QString(
    QQmlJSTypePropagator *self,
    const QString *methodName) {
  self->propagateTranslationMethod_SAcheck(*methodName);
}

//  bool QQmlJSTypePropagator::propagateTranslationMethod(const
//      QList<QQmlJSMetaMethod> &methods, int argc, int argv)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator26propagateTranslationMethodERK5QListI16QQmlJSMetaMethodEii(
    QQmlJSTypePropagator *self,
    const QList<QQmlJSMetaMethod> *methods,
    int argc,
    int argv) {
  return self->propagateTranslationMethod(*methods, argc, argv);
}

//  void QQmlJSTypePropagator::propagateStringArgCall(QQmlJSRegisterContent
//      base, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator22propagateStringArgCallE21QQmlJSRegisterContenti(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *base,
    int argv) {
  self->propagateStringArgCall(*base, argv);
}

//  bool QQmlJSTypePropagator::propagateArrayMethod(const QString &name, int
//      argc, int argv, QQmlJSRegisterContent valueType)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator20propagateArrayMethodERK7QStringii21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    const QString *name,
    int argc,
    int argv,
    const QQmlJSRegisterContent *valueType) {
  return self->propagateArrayMethod(*name, argc, argv, *valueType);
}

//  void QQmlJSTypePropagator::propagatePropertyLookup(const QString &name,
//      int lookupIndex)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7QStringi(
    QQmlJSTypePropagator *self,
    const QString *name,
    int lookupIndex) {
  self->propagatePropertyLookup(*name, lookupIndex);
}

//  void QQmlJSTypePropagator::propagateScopeLookupCall(const QString
//      &functionName, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24propagateScopeLookupCallERK7QStringii(
    QQmlJSTypePropagator *self,
    const QString *functionName,
    int argc,
    int argv) {
  self->propagateScopeLookupCall(*functionName, argc, argv);
}

//  void QQmlJSTypePropagator::saveRegisterStateForJump(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator24saveRegisterStateForJumpEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->saveRegisterStateForJump(offset);
}

//  bool QQmlJSTypePropagator::canConvertFromTo(QQmlJSRegisterContent from,
//      QQmlJSRegisterContent to)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator16canConvertFromToE21QQmlJSRegisterContentS0_(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *from,
    const QQmlJSRegisterContent *to) {
  return self->canConvertFromTo(*from, *to);
}

//  QString QQmlJSTypePropagator::registerName(int registerIndex) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlJSTypePropagator12registerNameEi(
    const QQmlJSTypePropagator *self,
    int registerIndex) {
  return new QString(self->registerName(registerIndex));
}

//  QQmlJSRegisterContent QQmlJSTypePropagator::checkedInputRegister(int reg)
extern "C" Q_DECL_EXPORT
QQmlJSRegisterContent *ritual_ZN20QQmlJSTypePropagator20checkedInputRegisterEi(
    QQmlJSTypePropagator *self,
    int reg) {
  return new QQmlJSRegisterContent(self->checkedInputRegister(reg));
}

//  void QQmlJSTypePropagator::setAccumulator(QQmlJSRegisterContent content)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator14setAccumulatorE21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *content) {
  self->setAccumulator(*content);
}

//  void QQmlJSTypePropagator::setRegister(int index, QQmlJSRegisterContent
//      content)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator11setRegisterEi21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    int index,
    const QQmlJSRegisterContent *content) {
  self->setRegister(index, *content);
}

//  void QQmlJSTypePropagator::mergeRegister(int index, const VirtualRegister
//      &a, const VirtualRegister &b)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator13mergeRegisterEiRKN17QQmlJSCompilePass15VirtualRegisterES3_(
    QQmlJSTypePropagator *self,
    int index,
    const QQmlJSCompilePass::VirtualRegister *a,
    const QQmlJSCompilePass::VirtualRegister *b) {
  self->mergeRegister(index, *a, *b);
}

//  void QQmlJSTypePropagator::addReadRegister(int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15addReadRegisterEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->addReadRegister(index);
}

//  void QQmlJSTypePropagator::addReadRegister(int index,
//      QQmlJSRegisterContent convertTo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator15addReadRegisterEi21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    int index,
    const QQmlJSRegisterContent *convertTo) {
  self->addReadRegister(index, *convertTo);
}

//  void QQmlJSTypePropagator::addReadAccumulator()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18addReadAccumulatorEv(
    QQmlJSTypePropagator *self) {
  self->addReadAccumulator();
}

//  void QQmlJSTypePropagator::addReadAccumulator(QQmlJSRegisterContent
//      convertTo)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator18addReadAccumulatorE21QQmlJSRegisterContent(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *convertTo) {
  self->addReadAccumulator(*convertTo);
}

//  bool QQmlJSTypePropagator::populatesAccumulator(QV4::Moth::Instr::Type
//      instr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlJSTypePropagator20populatesAccumulatorEN3QV44Moth5Instr4TypeE(
    const QQmlJSTypePropagator *self,
    QV4::Moth::Instr::Type instr) {
  return self->populatesAccumulator(instr);
}

//  bool QQmlJSTypePropagator::isNoop(QV4::Moth::Instr::Type instr) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK20QQmlJSTypePropagator6isNoopEN3QV44Moth5Instr4TypeE(
    const QQmlJSTypePropagator *self,
    QV4::Moth::Instr::Type instr) {
  return self->isNoop(instr);
}

//  void QQmlJSTypePropagator::recordEqualsNullType()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator20recordEqualsNullTypeEv(
    QQmlJSTypePropagator *self) {
  self->recordEqualsNullType();
}

//  void QQmlJSTypePropagator::recordEqualsIntType()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator19recordEqualsIntTypeEv(
    QQmlJSTypePropagator *self) {
  self->recordEqualsIntType();
}

//  void QQmlJSTypePropagator::recordEqualsType(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator16recordEqualsTypeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->recordEqualsType(lhs);
}

//  void QQmlJSTypePropagator::recordCompareType(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator17recordCompareTypeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->recordCompareType(lhs);
}

//  void QQmlJSTypePropagator::generate_CallProperty_SCMath(const QString
//      &name, int base, int arcg, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator28generate_CallProperty_SCMathERK7QStringiii(
    QQmlJSTypePropagator *self,
    const QString *name,
    int base,
    int arcg,
    int argv) {
  self->generate_CallProperty_SCMath(*name, base, arcg, argv);
}

//  void QQmlJSTypePropagator::generate_CallProperty_SCconsole(const QString
//      &name, int base, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator31generate_CallProperty_SCconsoleERK7QStringiii(
    QQmlJSTypePropagator *self,
    const QString *name,
    int base,
    int argc,
    int argv) {
  self->generate_CallProperty_SCconsole(*name, base, argc, argv);
}

//  void QQmlJSTypePropagator::generate_Construct_SCDate(const
//      QQmlJSMetaMethod &ctor, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25generate_Construct_SCDateERK16QQmlJSMetaMethodii(
    QQmlJSTypePropagator *self,
    const QQmlJSMetaMethod *ctor,
    int argc,
    int argv) {
  self->generate_Construct_SCDate(*ctor, argc, argv);
}

//  void QQmlJSTypePropagator::generate_Construct_SCArray(const
//      QQmlJSMetaMethod &ctor, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator26generate_Construct_SCArrayERK16QQmlJSMetaMethodii(
    QQmlJSTypePropagator *self,
    const QQmlJSMetaMethod *ctor,
    int argc,
    int argv) {
  self->generate_Construct_SCArray(*ctor, argc, argv);
}

//  bool QQmlJSTypePropagator::isLoggingMethod(const QString &consoleMethod)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlJSTypePropagator15isLoggingMethodERK7QString(
    const QString *consoleMethod) {
  return QQmlJSTypePropagator::isLoggingMethod(*consoleMethod);
}

//  void QQmlJSTypePropagator::addError(const QString &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator8addErrorERK7QString(
    QQmlJSTypePropagator *self,
    const QString *message) {
  self->addError(*message);
}

//  void QQmlJSTypePropagator::setVarAccumulatorAndError()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlJSTypePropagator25setVarAccumulatorAndErrorEv(
    QQmlJSTypePropagator *self) {
  self->setVarAccumulatorAndError();
}

//  a Python function taken by a CuteQQmlJSTypePropagator, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlJSTypePropagator(
    QQmlJSTypePropagator *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlJSTypePropagator *>(self)->take(key, call);
}

//  void QQmlJSTypePropagator::generate_Ret()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_RetEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_Ret();
}

//  void QQmlJSTypePropagator::generate_Debug()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_DebugEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_Debug();
}

//  void QQmlJSTypePropagator::generate_LoadConst(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_LoadConstEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadConst(index);
}

//  void QQmlJSTypePropagator::generate_LoadZero()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_LoadZeroEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadZero();
}

//  void QQmlJSTypePropagator::generate_LoadTrue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_LoadTrueEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadTrue();
}

//  void QQmlJSTypePropagator::generate_LoadFalse()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_LoadFalseEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadFalse();
}

//  void QQmlJSTypePropagator::generate_LoadNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_LoadNullEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadNull();
}

//  void QQmlJSTypePropagator::generate_LoadUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator22generate_LoadUndefinedEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadUndefined();
}

//  void QQmlJSTypePropagator::generate_LoadInt(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator16generate_LoadIntEi(
    QQmlJSTypePropagator *self,
    int value) {
  self->QQmlJSTypePropagator::generate_LoadInt(value);
}

//  void QQmlJSTypePropagator::generate_MoveConst(int constIndex, int
//      destTemp)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_MoveConstEii(
    QQmlJSTypePropagator *self,
    int constIndex,
    int destTemp) {
  self->QQmlJSTypePropagator::generate_MoveConst(constIndex, destTemp);
}

//  void QQmlJSTypePropagator::generate_LoadReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator16generate_LoadRegEi(
    QQmlJSTypePropagator *self,
    int reg) {
  self->QQmlJSTypePropagator::generate_LoadReg(reg);
}

//  void QQmlJSTypePropagator::generate_StoreReg(int reg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_StoreRegEi(
    QQmlJSTypePropagator *self,
    int reg) {
  self->QQmlJSTypePropagator::generate_StoreReg(reg);
}

//  void QQmlJSTypePropagator::generate_MoveReg(int srcReg, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator16generate_MoveRegEii(
    QQmlJSTypePropagator *self,
    int srcReg,
    int destReg) {
  self->QQmlJSTypePropagator::generate_MoveReg(srcReg, destReg);
}

//  void QQmlJSTypePropagator::generate_LoadImport(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_LoadImportEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadImport(index);
}

//  void QQmlJSTypePropagator::generate_LoadLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_LoadLocalEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadLocal(index);
}

//  void QQmlJSTypePropagator::generate_StoreLocal(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_StoreLocalEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_StoreLocal(index);
}

//  void QQmlJSTypePropagator::generate_LoadScopedLocal(int scope, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_LoadScopedLocalEii(
    QQmlJSTypePropagator *self,
    int scope,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadScopedLocal(scope, index);
}

//  void QQmlJSTypePropagator::generate_StoreScopedLocal(int scope, int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_StoreScopedLocalEii(
    QQmlJSTypePropagator *self,
    int scope,
    int index) {
  self->QQmlJSTypePropagator::generate_StoreScopedLocal(scope, index);
}

//  void QQmlJSTypePropagator::generate_LoadRuntimeString(int stringId)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_LoadRuntimeStringEi(
    QQmlJSTypePropagator *self,
    int stringId) {
  self->QQmlJSTypePropagator::generate_LoadRuntimeString(stringId);
}

//  void QQmlJSTypePropagator::generate_MoveRegExp(int regExpId, int destReg)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_MoveRegExpEii(
    QQmlJSTypePropagator *self,
    int regExpId,
    int destReg) {
  self->QQmlJSTypePropagator::generate_MoveRegExp(regExpId, destReg);
}

//  void QQmlJSTypePropagator::generate_LoadClosure(int value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_LoadClosureEi(
    QQmlJSTypePropagator *self,
    int value) {
  self->QQmlJSTypePropagator::generate_LoadClosure(value);
}

//  void QQmlJSTypePropagator::generate_LoadName(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_LoadNameEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->QQmlJSTypePropagator::generate_LoadName(nameIndex);
}

//  void QQmlJSTypePropagator::generate_LoadGlobalLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_LoadGlobalLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadGlobalLookup(index);
}

//  void QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(int
//      index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator37generate_LoadQmlContextPropertyLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_LoadQmlContextPropertyLookup(index);
}

//  void QQmlJSTypePropagator::generate_StoreNameSloppy(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameSloppyEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->QQmlJSTypePropagator::generate_StoreNameSloppy(nameIndex);
}

//  void QQmlJSTypePropagator::generate_StoreNameStrict(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameStrictEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->QQmlJSTypePropagator::generate_StoreNameStrict(name);
}

//  void QQmlJSTypePropagator::generate_LoadElement(int base)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_LoadElementEi(
    QQmlJSTypePropagator *self,
    int base) {
  self->QQmlJSTypePropagator::generate_LoadElement(base);
}

//  void QQmlJSTypePropagator::generate_StoreElement(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_StoreElementEii(
    QQmlJSTypePropagator *self,
    int base,
    int index) {
  self->QQmlJSTypePropagator::generate_StoreElement(base, index);
}

//  void QQmlJSTypePropagator::generate_LoadProperty(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_LoadPropertyEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  self->QQmlJSTypePropagator::generate_LoadProperty(nameIndex);
}

//  void QQmlJSTypePropagator::generate_LoadOptionalProperty(int name, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator29generate_LoadOptionalPropertyEii(
    QQmlJSTypePropagator *self,
    int name,
    int offset) {
  self->QQmlJSTypePropagator::generate_LoadOptionalProperty(name, offset);
}

//  void QQmlJSTypePropagator::generate_GetLookup(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_GetLookupEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_GetLookup(index);
}

//  void QQmlJSTypePropagator::generate_GetOptionalLookup(int index, int
//      offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_GetOptionalLookupEii(
    QQmlJSTypePropagator *self,
    int index,
    int offset) {
  self->QQmlJSTypePropagator::generate_GetOptionalLookup(index, offset);
}

//  void QQmlJSTypePropagator::generate_StoreProperty(int name, int base)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator22generate_StorePropertyEii(
    QQmlJSTypePropagator *self,
    int name,
    int base) {
  self->QQmlJSTypePropagator::generate_StoreProperty(name, base);
}

//  void QQmlJSTypePropagator::generate_SetLookup(int index, int base)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_SetLookupEii(
    QQmlJSTypePropagator *self,
    int index,
    int base) {
  self->QQmlJSTypePropagator::generate_SetLookup(index, base);
}

//  void QQmlJSTypePropagator::generate_LoadSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_LoadSuperPropertyEi(
    QQmlJSTypePropagator *self,
    int property) {
  self->QQmlJSTypePropagator::generate_LoadSuperProperty(property);
}

//  void QQmlJSTypePropagator::generate_StoreSuperProperty(int property)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator27generate_StoreSuperPropertyEi(
    QQmlJSTypePropagator *self,
    int property) {
  self->QQmlJSTypePropagator::generate_StoreSuperProperty(property);
}

//  void QQmlJSTypePropagator::generate_Yield()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_YieldEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_Yield();
}

//  void QQmlJSTypePropagator::generate_YieldStar()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_YieldStarEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_YieldStar();
}

//  void QQmlJSTypePropagator::generate_Resume(int a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator15generate_ResumeEi(
    QQmlJSTypePropagator *self,
    int a0) {
  self->QQmlJSTypePropagator::generate_Resume(a0);
}

//  void QQmlJSTypePropagator::generate_CallValue(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_CallValueEiii(
    QQmlJSTypePropagator *self,
    int name,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallValue(name, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallWithReceiver(int name, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_CallWithReceiverEiiii(
    QQmlJSTypePropagator *self,
    int name,
    int thisObject,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallWithReceiver(
      name,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSTypePropagator::generate_CallProperty(int name, int base, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_CallPropertyEiiii(
    QQmlJSTypePropagator *self,
    int name,
    int base,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallProperty(name, base, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallPropertyLookup(int lookupIndex,
//      int base, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator27generate_CallPropertyLookupEiiii(
    QQmlJSTypePropagator *self,
    int lookupIndex,
    int base,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallPropertyLookup(
      lookupIndex,
      base,
      argc,
      argv);
}

//  void QQmlJSTypePropagator::generate_CallName(int name, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_CallNameEiii(
    QQmlJSTypePropagator *self,
    int name,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallName(name, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallPossiblyDirectEval(int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator31generate_CallPossiblyDirectEvalEii(
    QQmlJSTypePropagator *self,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallPossiblyDirectEval(argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallGlobalLookup(int index, int argc,
//      int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_CallGlobalLookupEiii(
    QQmlJSTypePropagator *self,
    int index,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallGlobalLookup(index, argc, argv);
}

//  void QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(int
//      index, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator37generate_CallQmlContextPropertyLookupEiii(
    QQmlJSTypePropagator *self,
    int index,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallQmlContextPropertyLookup(
      index,
      argc,
      argv);
}

//  void QQmlJSTypePropagator::generate_CallWithSpread(int func, int
//      thisObject, int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_CallWithSpreadEiiii(
    QQmlJSTypePropagator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_CallWithSpread(
      func,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSTypePropagator::generate_TailCall(int func, int thisObject,
//      int argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_TailCallEiiii(
    QQmlJSTypePropagator *self,
    int func,
    int thisObject,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_TailCall(
      func,
      thisObject,
      argc,
      argv);
}

//  void QQmlJSTypePropagator::generate_Construct(int func, int argc, int
//      argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_ConstructEiii(
    QQmlJSTypePropagator *self,
    int func,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_Construct(func, argc, argv);
}

//  void QQmlJSTypePropagator::generate_ConstructWithSpread(int func, int
//      argc, int argv)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator28generate_ConstructWithSpreadEiii(
    QQmlJSTypePropagator *self,
    int func,
    int argc,
    int argv) {
  self->QQmlJSTypePropagator::generate_ConstructWithSpread(func, argc, argv);
}

//  void QQmlJSTypePropagator::generate_SetUnwindHandler(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_SetUnwindHandlerEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_SetUnwindHandler(offset);
}

//  void QQmlJSTypePropagator::generate_UnwindDispatch()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_UnwindDispatchEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_UnwindDispatch();
}

//  void QQmlJSTypePropagator::generate_UnwindToLabel(int level, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator22generate_UnwindToLabelEii(
    QQmlJSTypePropagator *self,
    int level,
    int offset) {
  self->QQmlJSTypePropagator::generate_UnwindToLabel(level, offset);
}

//  void QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator30generate_DeadTemporalZoneCheckEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->QQmlJSTypePropagator::generate_DeadTemporalZoneCheck(name);
}

//  void QQmlJSTypePropagator::generate_ThrowException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_ThrowExceptionEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_ThrowException();
}

//  void QQmlJSTypePropagator::generate_GetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_GetExceptionEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_GetException();
}

//  void QQmlJSTypePropagator::generate_SetException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_SetExceptionEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_SetException();
}

//  void QQmlJSTypePropagator::generate_CreateCallContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_CreateCallContextEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CreateCallContext();
}

//  void QQmlJSTypePropagator::generate_PushCatchContext(int index, int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_PushCatchContextEii(
    QQmlJSTypePropagator *self,
    int index,
    int name) {
  self->QQmlJSTypePropagator::generate_PushCatchContext(index, name);
}

//  void QQmlJSTypePropagator::generate_PushWithContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_PushWithContextEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_PushWithContext();
}

//  void QQmlJSTypePropagator::generate_PushBlockContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_PushBlockContextEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_PushBlockContext(index);
}

//  void QQmlJSTypePropagator::generate_CloneBlockContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_CloneBlockContextEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CloneBlockContext();
}

//  void QQmlJSTypePropagator::generate_PushScriptContext(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_PushScriptContextEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_PushScriptContext(index);
}

//  void QQmlJSTypePropagator::generate_PopScriptContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_PopScriptContextEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_PopScriptContext();
}

//  void QQmlJSTypePropagator::generate_PopContext()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_PopContextEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_PopContext();
}

//  void QQmlJSTypePropagator::generate_GetIterator(int iterator)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_GetIteratorEi(
    QQmlJSTypePropagator *self,
    int iterator) {
  self->QQmlJSTypePropagator::generate_GetIterator(iterator);
}

//  void QQmlJSTypePropagator::generate_IteratorNext(int value, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21generate_IteratorNextEii(
    QQmlJSTypePropagator *self,
    int value,
    int offset) {
  self->QQmlJSTypePropagator::generate_IteratorNext(value, offset);
}

//  void QQmlJSTypePropagator::generate_IteratorNextForYieldStar(int
//      iterator, int object, int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator33generate_IteratorNextForYieldStarEiii(
    QQmlJSTypePropagator *self,
    int iterator,
    int object,
    int offset) {
  self->QQmlJSTypePropagator::generate_IteratorNextForYieldStar(
      iterator,
      object,
      offset);
}

//  void QQmlJSTypePropagator::generate_IteratorClose()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator22generate_IteratorCloseEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_IteratorClose();
}

//  void QQmlJSTypePropagator::generate_DestructureRestElement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator31generate_DestructureRestElementEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_DestructureRestElement();
}

//  void QQmlJSTypePropagator::generate_DeleteProperty(int base, int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_DeletePropertyEii(
    QQmlJSTypePropagator *self,
    int base,
    int index) {
  self->QQmlJSTypePropagator::generate_DeleteProperty(base, index);
}

//  void QQmlJSTypePropagator::generate_DeleteName(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_DeleteNameEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->QQmlJSTypePropagator::generate_DeleteName(name);
}

//  void QQmlJSTypePropagator::generate_TypeofName(int name)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_TypeofNameEi(
    QQmlJSTypePropagator *self,
    int name) {
  self->QQmlJSTypePropagator::generate_TypeofName(name);
}

//  void QQmlJSTypePropagator::generate_TypeofValue()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_TypeofValueEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_TypeofValue();
}

//  void QQmlJSTypePropagator::generate_DeclareVar(int varName, int
//      isDeletable)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_DeclareVarEii(
    QQmlJSTypePropagator *self,
    int varName,
    int isDeletable) {
  self->QQmlJSTypePropagator::generate_DeclareVar(varName, isDeletable);
}

//  void QQmlJSTypePropagator::generate_DefineArray(int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_DefineArrayEii(
    QQmlJSTypePropagator *self,
    int argc,
    int args) {
  self->QQmlJSTypePropagator::generate_DefineArray(argc, args);
}

//  void QQmlJSTypePropagator::generate_DefineObjectLiteral(int
//      internalClassId, int argc, int args)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator28generate_DefineObjectLiteralEiii(
    QQmlJSTypePropagator *self,
    int internalClassId,
    int argc,
    int args) {
  self->QQmlJSTypePropagator::generate_DefineObjectLiteral(
      internalClassId,
      argc,
      args);
}

//  void QQmlJSTypePropagator::generate_CreateClass(int classIndex, int
//      heritage, int computedNames)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_CreateClassEiii(
    QQmlJSTypePropagator *self,
    int classIndex,
    int heritage,
    int computedNames) {
  self->QQmlJSTypePropagator::generate_CreateClass(
      classIndex,
      heritage,
      computedNames);
}

//  void QQmlJSTypePropagator::generate_CreateMappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator36generate_CreateMappedArgumentsObjectEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CreateMappedArgumentsObject();
}

//  void QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator38generate_CreateUnmappedArgumentsObjectEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CreateUnmappedArgumentsObject();
}

//  void QQmlJSTypePropagator::generate_CreateRestParameter(int argIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator28generate_CreateRestParameterEi(
    QQmlJSTypePropagator *self,
    int argIndex) {
  self->QQmlJSTypePropagator::generate_CreateRestParameter(argIndex);
}

//  void QQmlJSTypePropagator::generate_ConvertThisToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator28generate_ConvertThisToObjectEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_ConvertThisToObject();
}

//  void QQmlJSTypePropagator::generate_LoadSuperConstructor()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator29generate_LoadSuperConstructorEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_LoadSuperConstructor();
}

//  void QQmlJSTypePropagator::generate_ToObject()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_ToObjectEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_ToObject();
}

//  void QQmlJSTypePropagator::generate_Jump(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator13generate_JumpEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_Jump(offset);
}

//  void QQmlJSTypePropagator::generate_JumpTrue(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_JumpTrueEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_JumpTrue(offset);
}

//  void QQmlJSTypePropagator::generate_JumpFalse(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_JumpFalseEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_JumpFalse(offset);
}

//  void QQmlJSTypePropagator::generate_JumpNoException(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_JumpNoExceptionEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_JumpNoException(offset);
}

//  void QQmlJSTypePropagator::generate_JumpNotUndefined(int offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator25generate_JumpNotUndefinedEi(
    QQmlJSTypePropagator *self,
    int offset) {
  self->QQmlJSTypePropagator::generate_JumpNotUndefined(offset);
}

//  void QQmlJSTypePropagator::generate_CheckException()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_CheckExceptionEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CheckException();
}

//  void QQmlJSTypePropagator::generate_CmpEqNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_CmpEqNullEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CmpEqNull();
}

//  void QQmlJSTypePropagator::generate_CmpNeNull()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_CmpNeNullEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_CmpNeNull();
}

//  void QQmlJSTypePropagator::generate_CmpEqInt(int lhsConst)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_CmpEqIntEi(
    QQmlJSTypePropagator *self,
    int lhsConst) {
  self->QQmlJSTypePropagator::generate_CmpEqInt(lhsConst);
}

//  void QQmlJSTypePropagator::generate_CmpNeInt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_CmpNeIntEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpNeInt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpEq(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpEqEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpEq(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpNe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpNeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpNe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpGt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpGtEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpGt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpGe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpGeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpGe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpLt(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpLtEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpLt(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpLe(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpLeEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpLe(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpStrictEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23generate_CmpStrictEqualEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpStrictEqual(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpStrictNotEqual(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_CmpStrictNotEqualEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpStrictNotEqual(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpIn(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_CmpInEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpIn(lhs);
}

//  void QQmlJSTypePropagator::generate_CmpInstanceOf(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator22generate_CmpInstanceOfEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_CmpInstanceOf(lhs);
}

//  void QQmlJSTypePropagator::generate_As(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator11generate_AsEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_As(lhs);
}

//  void QQmlJSTypePropagator::generate_UNot()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator13generate_UNotEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_UNot();
}

//  void QQmlJSTypePropagator::generate_UPlus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_UPlusEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_UPlus();
}

//  void QQmlJSTypePropagator::generate_UMinus()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator15generate_UMinusEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_UMinus();
}

//  void QQmlJSTypePropagator::generate_UCompl()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator15generate_UComplEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_UCompl();
}

//  void QQmlJSTypePropagator::generate_Increment()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_IncrementEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_Increment();
}

//  void QQmlJSTypePropagator::generate_Decrement()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_DecrementEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_Decrement();
}

//  void QQmlJSTypePropagator::generate_Add(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_AddEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Add(lhs);
}

//  void QQmlJSTypePropagator::generate_BitAnd(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator15generate_BitAndEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_BitAnd(lhs);
}

//  void QQmlJSTypePropagator::generate_BitOr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14generate_BitOrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_BitOr(lhs);
}

//  void QQmlJSTypePropagator::generate_BitXor(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator15generate_BitXorEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_BitXor(lhs);
}

//  void QQmlJSTypePropagator::generate_UShr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator13generate_UShrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_UShr(lhs);
}

//  void QQmlJSTypePropagator::generate_Shr(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_ShrEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Shr(lhs);
}

//  void QQmlJSTypePropagator::generate_Shl(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_ShlEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Shl(lhs);
}

//  void QQmlJSTypePropagator::generate_BitAndConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_BitAndConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->QQmlJSTypePropagator::generate_BitAndConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_BitOrConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator19generate_BitOrConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->QQmlJSTypePropagator::generate_BitOrConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_BitXorConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator20generate_BitXorConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->QQmlJSTypePropagator::generate_BitXorConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_UShrConst(int rhsConst)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator18generate_UShrConstEi(
    QQmlJSTypePropagator *self,
    int rhsConst) {
  self->QQmlJSTypePropagator::generate_UShrConst(rhsConst);
}

//  void QQmlJSTypePropagator::generate_ShrConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_ShrConstEi(
    QQmlJSTypePropagator *self,
    int rhs) {
  self->QQmlJSTypePropagator::generate_ShrConst(rhs);
}

//  void QQmlJSTypePropagator::generate_ShlConst(int rhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17generate_ShlConstEi(
    QQmlJSTypePropagator *self,
    int rhs) {
  self->QQmlJSTypePropagator::generate_ShlConst(rhs);
}

//  void QQmlJSTypePropagator::generate_Exp(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_ExpEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Exp(lhs);
}

//  void QQmlJSTypePropagator::generate_Mul(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_MulEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Mul(lhs);
}

//  void QQmlJSTypePropagator::generate_Div(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_DivEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Div(lhs);
}

//  void QQmlJSTypePropagator::generate_Mod(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_ModEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Mod(lhs);
}

//  void QQmlJSTypePropagator::generate_Sub(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator12generate_SubEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  self->QQmlJSTypePropagator::generate_Sub(lhs);
}

//  void QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(int
//      firstReg, int count)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator40generate_InitializeBlockDeadTemporalZoneEii(
    QQmlJSTypePropagator *self,
    int firstReg,
    int count) {
  self->QQmlJSTypePropagator::generate_InitializeBlockDeadTemporalZone(
      firstReg,
      count);
}

//  void QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator31generate_ThrowOnNullOrUndefinedEv(
    QQmlJSTypePropagator *self) {
  self->QQmlJSTypePropagator::generate_ThrowOnNullOrUndefined();
}

//  void QQmlJSTypePropagator::generate_GetTemplateObject(int index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator26generate_GetTemplateObjectEi(
    QQmlJSTypePropagator *self,
    int index) {
  self->QQmlJSTypePropagator::generate_GetTemplateObject(index);
}

//  void QQmlJSTypePropagator::endInstruction(QV4::Moth::Instr::Type instr)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator14endInstructionEN3QV44Moth5Instr4TypeE(
    QQmlJSTypePropagator *self,
    QV4::Moth::Instr::Type instr) {
  self->QQmlJSTypePropagator::endInstruction(instr);
}

//  void QQmlJSTypePropagator::handleUnqualifiedAccess(const QString &name,
//      bool isMethod) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QQmlJSTypePropagator23handleUnqualifiedAccessERK7QStringb(
    const QQmlJSTypePropagator *self,
    const QString *name,
    bool isMethod) {
  static_cast<const OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::handleUnqualifiedAccess(
      *name,
      isMethod);
}

//  void
//      QQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(con
//      st QString &name, bool isMethod) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK20QQmlJSTypePropagator43handleUnqualifiedAccessAndContextPropertiesERK7QStringb(
    const QQmlJSTypePropagator *self,
    const QString *name,
    bool isMethod) {
  static_cast<const OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::handleUnqualifiedAccessAndContextProperties(
      *name,
      isMethod);
}

//  bool QQmlJSTypePropagator::handleImportNamespaceLookup(const QString
//      &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQmlJSTypePropagator27handleImportNamespaceLookupERK7QString(
    QQmlJSTypePropagator *self,
    const QString *propertyName) {
  return static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::handleImportNamespaceLookup(
      *propertyName);
}

//  void QQmlJSTypePropagator::handleLookupError(const QString &propertyName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator17handleLookupErrorERK7QString(
    QQmlJSTypePropagator *self,
    const QString *propertyName) {
  static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::handleLookupError(
      *propertyName);
}

//  bool QQmlJSTypePropagator::checkForEnumProblems(QQmlJSRegisterContent
//      base, const QString &propertyName)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN20QQmlJSTypePropagator20checkForEnumProblemsE21QQmlJSRegisterContentRK7QString(
    QQmlJSTypePropagator *self,
    const QQmlJSRegisterContent *base,
    const QString *propertyName) {
  return static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::checkForEnumProblems(
      *base,
      *propertyName);
}

//  void QQmlJSTypePropagator::warnAboutTypeCoercion(int lhs)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator21warnAboutTypeCoercionEi(
    QQmlJSTypePropagator *self,
    int lhs) {
  static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::warnAboutTypeCoercion(
      lhs);
}

//  void QQmlJSTypePropagator::generate_StoreNameCommon(int nameIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator24generate_StoreNameCommonEi(
    QQmlJSTypePropagator *self,
    int nameIndex) {
  static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::generate_StoreNameCommon(
      nameIndex);
}

//  void QQmlJSTypePropagator::propagateTranslationMethod_SAcheck(const
//      QString &methodName)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator34propagateTranslationMethod_SAcheckERK7QString(
    QQmlJSTypePropagator *self,
    const QString *methodName) {
  static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::propagateTranslationMethod_SAcheck(
      *methodName);
}

//  void QQmlJSTypePropagator::propagatePropertyLookup(const QString &name,
//      int lookupIndex)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQmlJSTypePropagator23propagatePropertyLookupERK7QStringi(
    QQmlJSTypePropagator *self,
    const QString *name,
    int lookupIndex) {
  static_cast<OwnQQmlJSTypePropagator *>(self)->OwnQQmlJSTypePropagator::propagatePropertyLookup(
      *name,
      lookupIndex);
}
