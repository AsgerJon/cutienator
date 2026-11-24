//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/clipblendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::Animation::ClipBlendNode that Python can take functions over in. Every Qt3DAnimation::Animation::ClipBlendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef double (*CuteQt3DAnimation_Animation_ClipBlendNodeCall0)(const void *, int *);
typedef void (*CuteQt3DAnimation_Animation_ClipBlendNodeCall1)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DAnimation_Animation_ClipBlendNode : public Qt3DAnimation::Animation::ClipBlendNode {
public:
  using Qt3DAnimation::Animation::ClipBlendNode::ClipBlendNode;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  double Qt3DAnimation::Animation::ClipBlendNode::duration() const
  double duration() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendNodeCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendNodeCall0>(taken[0]);
      double given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_ClipBlendNodeCall1 call = reinterpret_cast<CuteQt3DAnimation_Animation_ClipBlendNodeCall1>(taken[1]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  ClipBlendNodeManager
//      *Qt3DAnimation::Animation::ClipBlendNode::clipBlendNodeManager()
//      const
extern "C" Q_DECL_EXPORT
Qt3DAnimation::Animation::ClipBlendNodeManager *ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode20clipBlendNodeManagerEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return self->clipBlendNodeManager();
}

//  double Qt3DAnimation::Animation::ClipBlendNode::duration() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13Qt3DAnimation9Animation13ClipBlendNode8durationEv(
    const Qt3DAnimation::Animation::ClipBlendNode *self) {
  return self->duration();
}

//  a Python function taken by a CuteQt3DAnimation_Animation_ClipBlendNode,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_ClipBlendNode(
    Qt3DAnimation::Animation::ClipBlendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_ClipBlendNode *>(self)->take(key, call);
}
