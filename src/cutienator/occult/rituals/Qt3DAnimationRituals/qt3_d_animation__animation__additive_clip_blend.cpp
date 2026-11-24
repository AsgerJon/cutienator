//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/additiveclipblend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/additiveclipblend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DAnimation::Animation::AdditiveClipBlend that Python can take functions over in. Every Qt3DAnimation::Animation::AdditiveClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_AdditiveClipBlendCall0)(const void *, int *);
class CuteQt3DAnimation_Animation_AdditiveClipBlend : public Qt3DAnimation::Animation::AdditiveClipBlend {
public:
  using Qt3DAnimation::Animation::AdditiveClipBlend::AdditiveClipBlend;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_AdditiveClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_AdditiveClipBlendCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::AdditiveClipBlend::duration();
  }
};

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::AdditiveClipBlend::baseClipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend10baseClipIdEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new Qt3DCore::QNodeId(self->baseClipId());
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setBaseClipId(Qt3DCore:
//      :QNodeId baseClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend13setBaseClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const Qt3DCore::QNodeId *baseClipId) {
  self->setBaseClipId(*baseClipId);
}

//  Qt3DCore::QNodeId
//      Qt3DAnimation::Animation::AdditiveClipBlend::additiveClipId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveClipIdEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return new Qt3DCore::QNodeId(self->additiveClipId());
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveClipId(Qt3DC
//      ore::QNodeId additiveClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditiveClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const Qt3DCore::QNodeId *additiveClipId) {
  self->setAdditiveClipId(*additiveClipId);
}

//  float Qt3DAnimation::Animation::AdditiveClipBlend::additiveFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend14additiveFactorEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return self->additiveFactor();
}

//  void Qt3DAnimation::Animation::AdditiveClipBlend::setAdditiveFactor(float
//      additiveFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation17AdditiveClipBlend17setAdditiveFactorEf(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    float additiveFactor) {
  self->setAdditiveFactor(additiveFactor);
}

//  double Qt3DAnimation::Animation::AdditiveClipBlend::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation17AdditiveClipBlend8durationEv(
    const Qt3DAnimation::Animation::AdditiveClipBlend *self) {
  return self->duration();
}

//  a Python function taken by a
//      CuteQt3DAnimation_Animation_AdditiveClipBlend, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_AdditiveClipBlend(
    Qt3DAnimation::Animation::AdditiveClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_AdditiveClipBlend *>(self)->take(key, call);
}
