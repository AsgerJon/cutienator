//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DAnimation/6.12.0/Qt3DAnimation/private/backendnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/qt3danimation_global_p.h>
#include <Qt3DAnimation/Qt3DAnimation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DAnimation/6.12.0/Qt3DAnimation/private/backendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DAnimation::Animation::BackendNode that Python can take functions over in. Every Qt3DAnimation::Animation::BackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DAnimation_Animation_BackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DAnimation_Animation_BackendNode : public Qt3DAnimation::Animation::BackendNode {
public:
  using Qt3DAnimation::Animation::BackendNode::BackendNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DAnimation_Animation_BackendNodeCall0 call = reinterpret_cast<CuteQt3DAnimation_Animation_BackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DAnimation::Animation::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  a Python function taken by a CuteQt3DAnimation_Animation_BackendNode, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DAnimation_Animation_BackendNode(
    Qt3DAnimation::Animation::BackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DAnimation_Animation_BackendNode *>(self)->take(key, call);
}
