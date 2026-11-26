//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/managers_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::FrameGraphManager::FrameGraphManager()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphManager *ritual_ZN10Qt3DRender6Render17FrameGraphManagerC1Ev() {
  return new Qt3DRender::Render::FrameGraphManager();
}

//  Qt3DRender::Render::FrameGraphManager::~FrameGraphManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrameGraphManagerD1Ev(
    Qt3DRender::Render::FrameGraphManager *self) {
  delete self;
}

//  bool
//      Qt3DRender::Render::FrameGraphManager::containsNode(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render17FrameGraphManager12containsNodeEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::FrameGraphManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->containsNode(*id);
}

//  void Qt3DRender::Render::FrameGraphManager::appendNode(Qt3DCore::QNodeId
//      id, FrameGraphNode *node)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrameGraphManager10appendNodeEN8Qt3DCore7QNodeIdEPNS0_14FrameGraphNodeE(
    Qt3DRender::Render::FrameGraphManager *self,
    const Qt3DCore::QNodeId *id,
    Qt3DRender::Render::FrameGraphNode *node) {
  self->appendNode(*id, node);
}

//  FrameGraphNode
//      *Qt3DRender::Render::FrameGraphManager::lookupNode(Qt3DCore::QNodeId
//      id) const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::FrameGraphNode *ritual_ZNK10Qt3DRender6Render17FrameGraphManager10lookupNodeEN8Qt3DCore7QNodeIdE(
    const Qt3DRender::Render::FrameGraphManager *self,
    const Qt3DCore::QNodeId *id) {
  return self->lookupNode(*id);
}

//  void Qt3DRender::Render::FrameGraphManager::releaseNode(Qt3DCore::QNodeId
//      id)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render17FrameGraphManager11releaseNodeEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::FrameGraphManager *self,
    const Qt3DCore::QNodeId *id) {
  self->releaseNode(*id);
}
