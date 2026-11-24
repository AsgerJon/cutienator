//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendvalue_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendvalue_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DAnimation::Animation::ClipBlendValue that Python can take functions over in. Every Qt3DAnimation::Animation::ClipBlendValue
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_Animation_ClipBlendValueCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
typedef double (*CuteQt3DAnimation_Animation_ClipBlendValueCall1)(const void *, int *);
class CuteQt3DAnimation_Animation_ClipBlendValue : public Qt3DAnimation::Animation::ClipBlendValue {
public:
  using Qt3DAnimation::Animation::ClipBlendValue::ClipBlendValue;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendValueCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendValueCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::ClipBlendValue::syncFromFrontEnd(frontEnd, firstTime);
  }

  //  double Qt3DAnimation::Animation::ClipBlendValue::duration() const
  double duration() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendValueCall1 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendValueCall1>(taken[1]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::ClipBlendValue::duration();
  }
};

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::ClipBlendValue::clipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation14ClipBlendValue6clipIdEv(
    const Qt3DAnimation::Animation::ClipBlendValue *self) {
  return new Qt3DCore::QNodeId(self->clipId());
}

//  void
//      Qt3DAnimation::Animation::ClipBlendValue::setClipId(Qt3DCore::QNodeId
//      clipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation14ClipBlendValue9setClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const Qt3DCore::QNodeId *clipId) {
  self->setClipId(*clipId);
}

//  a Python function taken by a CuteQt3DAnimation_Animation_ClipBlendValue,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_ClipBlendValue(
    Qt3DAnimation::Animation::ClipBlendValue *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_ClipBlendValue *>(self)->take(key, call);
}
