//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/lerpclipblend_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/lerpclipblend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DAnimation::Animation::LerpClipBlend that Python can take functions over in. Every Qt3DAnimation::Animation::LerpClipBlend
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_LerpClipBlendCall0)(const void *, int *);
class CuteQt3DAnimation_Animation_LerpClipBlend : public Qt3DAnimation::Animation::LerpClipBlend {
public:
  using Qt3DAnimation::Animation::LerpClipBlend::LerpClipBlend;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::LerpClipBlend::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_LerpClipBlendCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_LerpClipBlendCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return Qt3DAnimation::Animation::LerpClipBlend::duration();
  }
};

//  float Qt3DAnimation::Animation::LerpClipBlend::blendFactor() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11blendFactorEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return self->blendFactor();
}

//  void Qt3DAnimation::Animation::LerpClipBlend::setBlendFactor(float
//      blendFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setBlendFactorEf(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    float blendFactor) {
  self->setBlendFactor(blendFactor);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::LerpClipBlend::startClipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend11startClipIdEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new Qt3DCore::QNodeId(self->startClipId());
}

//  void
//      Qt3DAnimation::Animation::LerpClipBlend::setStartClipId(Qt3DCore::QNo
//      deId startClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend14setStartClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const Qt3DCore::QNodeId *startClipId) {
  self->setStartClipId(*startClipId);
}

//  Qt3DCore::QNodeId Qt3DAnimation::Animation::LerpClipBlend::endClipId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK13Qt3DAnimation9Animation13LerpClipBlend9endClipIdEv(
    const Qt3DAnimation::Animation::LerpClipBlend *self) {
  return new Qt3DCore::QNodeId(self->endClipId());
}

//  void
//      Qt3DAnimation::Animation::LerpClipBlend::setEndClipId(Qt3DCore::QNode
//      Id endClipId)
extern "C" Q_DECL_EXPORT
void ritual_ZN13Qt3DAnimation9Animation13LerpClipBlend12setEndClipIdEN8Qt3DCore7QNodeIdE(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const Qt3DCore::QNodeId *endClipId) {
  self->setEndClipId(*endClipId);
}

//  a Python function taken by a CuteQt3DAnimation_Animation_LerpClipBlend,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_LerpClipBlend(
    Qt3DAnimation::Animation::LerpClipBlend *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_LerpClipBlend *>(self)->take(key, call);
}
