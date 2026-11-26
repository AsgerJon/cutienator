//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/framegraphvisitor_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: added by hand, rituals for functions the
//  generator leaves out: 3. Kept as it is when the generator runs again.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/framegraphvisitor_p.h>
#include <vector>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt3DRender::Render::FrameGraphVisitor::FrameGraphVisitor(const
//      FrameGraphManager *nodeManager)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphVisitor *ritual_ZN10Qt3DRender6Render17FrameGraphVisitorC1EPKNS0_17FrameGraphManagerE(
    const Qt3DRender::Render::FrameGraphManager *nodeManager) {
  return new Qt3DRender::Render::FrameGraphVisitor(nodeManager);
}

//  void Qt3DRender::Render::FrameGraphVisitor::visit(Render::FrameGraphNode
//      *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrameGraphVisitor5visitEPNS0_14FrameGraphNodeE(
    Qt3DRender::Render::FrameGraphVisitor *self,
    Qt3DRender::Render::FrameGraphNode *node) {
  self->visit(node);
}

//  Qt3DRender::Render::FrameGraphVisitor::~FrameGraphVisitor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrameGraphVisitorD1Ev(
    Qt3DRender::Render::FrameGraphVisitor *self) {
  delete self;
}

//  std::vector<FrameGraphNode *>
//      &&Qt3DRender::Render::FrameGraphVisitor::traverse(FrameGraphNode
//      *root)
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::FrameGraphNode *> *ritual_ZN10Qt3DRender6Render17FrameGraphVisitor8traverseEPNS0_14FrameGraphNodeE(
    Qt3DRender::Render::FrameGraphVisitor *self,
    Qt3DRender::Render::FrameGraphNode *root) {
  return new std::vector<Qt3DRender::Render::FrameGraphNode *>(
      self->traverse(root));
}

//  std::vector<FrameGraphNode *>
//      &&Qt3DRender::Render::FrameGraphVisitor::takeEnablersToDisable()
extern "C" Q_DECL_EXPORT
std::vector<Qt3DRender::Render::FrameGraphNode *> *ritual_ZN10Qt3DRender6Render17FrameGraphVisitor21takeEnablersToDisableEv(
    Qt3DRender::Render::FrameGraphVisitor *self) {
  return new std::vector<Qt3DRender::Render::FrameGraphNode *>(
      self->takeEnablersToDisable());
}

//  a std::vector<Qt3DRender::Render::FrameGraphNode *> a ritual of
//      Qt3DRender::Render::FrameGraphVisitor gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_FrameGraphVisitor__std_vector_Qt3DRender_Render_FrameGraphNode(
    std::vector<Qt3DRender::Render::FrameGraphNode *> *self) {
  delete self;
}
