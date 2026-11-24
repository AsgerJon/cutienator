//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/framegraphnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/framegraphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A Qt3DRender::Render::FrameGraphNode that Python can take functions over in. Every Qt3DRender::Render::FrameGraphNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_FrameGraphNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_FrameGraphNode : public Qt3DRender::Render::FrameGraphNode {
public:
  using Qt3DRender::Render::FrameGraphNode::FrameGraphNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_FrameGraphNodeCall0 call = reinterpret_cast<CuteQt3DRender_Render_FrameGraphNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::FrameGraphNode::~FrameGraphNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render14FrameGraphNodeD1Ev(
    Qt3DRender::Render::FrameGraphNode *self) {
  delete self;
}

//  FrameGraphNodeType Qt3DRender::Render::FrameGraphNode::nodeType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphNode::FrameGraphNodeType ritual_ZNK10Qt3DRender6Render14FrameGraphNode8nodeTypeEv(
    const Qt3DRender::Render::FrameGraphNode *self) {
  return self->nodeType();
}

//  a Python function taken by a CuteQt3DRender_Render_FrameGraphNode, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_FrameGraphNode(
    Qt3DRender::Render::FrameGraphNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_FrameGraphNode *>(self)->take(key, call);
}

//  void Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render14FrameGraphNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::FrameGraphNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::FrameGraphNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
