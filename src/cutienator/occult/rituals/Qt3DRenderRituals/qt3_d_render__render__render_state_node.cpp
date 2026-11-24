//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderstatenode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderstatenode_p.h>
#include <Qt3DRender/6.12.0/Qt3DRender/private/statevariant_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::RenderStateNode that Python can take functions over in. Every Qt3DRender::Render::RenderStateNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_RenderStateNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_RenderStateNode : public Qt3DRender::Render::RenderStateNode {
public:
  using Qt3DRender::Render::RenderStateNode::RenderStateNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::RenderStateNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_RenderStateNodeCall0 call = reinterpret_cast<CuteQt3DRender_Render_RenderStateNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::RenderStateNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::RenderStateNode::~RenderStateNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render15RenderStateNodeD1Ev(
    Qt3DRender::Render::RenderStateNode *self) {
  delete self;
}

//  StateMask Qt3DRender::Render::RenderStateNode::type() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateMask ritual_ZNK10Qt3DRender6Render15RenderStateNode4typeEv(
    const Qt3DRender::Render::RenderStateNode *self) {
  return self->type();
}

//  StateVariant Qt3DRender::Render::RenderStateNode::impl() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateVariant *ritual_ZNK10Qt3DRender6Render15RenderStateNode4implEv(
    const Qt3DRender::Render::RenderStateNode *self) {
  return new Qt3DRender::Render::StateVariant(self->impl());
}

//  a Python function taken by a CuteQt3DRender_Render_RenderStateNode, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_RenderStateNode(
    Qt3DRender::Render::RenderStateNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_RenderStateNode *>(self)->take(key, call);
}

//  void Qt3DRender::Render::RenderStateNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render15RenderStateNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderStateNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderStateNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
