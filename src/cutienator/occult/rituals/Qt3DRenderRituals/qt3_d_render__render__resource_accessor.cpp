//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/resourceaccessor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/resourceaccessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::ResourceAccessor::ResourceAccessor(AbstractRenderer
//      *renderer, NodeManagers *mgr)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::ResourceAccessor *ritual_ZN10Qt3DRender6Render16ResourceAccessorC1EPNS0_16AbstractRendererEPNS0_12NodeManagersE(
    Qt3DRender::Render::AbstractRenderer *renderer,
    Qt3DRender::Render::NodeManagers *mgr) {
  return new Qt3DRender::Render::ResourceAccessor(renderer, mgr);
}

//  bool Qt3DRender::Render::ResourceAccessor::accessResource(ResourceType
//      type, Qt3DCore::QNodeId nodeId, void **handle, QMutex **lock)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render16ResourceAccessor14accessResourceENS0_29RenderBackendResourceAccessor12ResourceTypeEN8Qt3DCore7QNodeIdEPPvPP6QMutex(
    Qt3DRender::Render::ResourceAccessor *self,
    Qt3DRender::Render::RenderBackendResourceAccessor::ResourceType type,
    const Qt3DCore::QNodeId *nodeId,
    void **handle,
    QMutex **lock) {
  return self->accessResource(type, *nodeId, handle, lock);
}

//  Qt3DRender::Render::ResourceAccessor::~ResourceAccessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render16ResourceAccessorD1Ev(
    Qt3DRender::Render::ResourceAccessor *self) {
  delete self;
}
