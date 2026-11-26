//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/resourceaccessor_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/resourceaccessor_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>

//  Qt3DRender::Render::RenderBackendResourceAccessor::~RenderBackendResource
//      Accessor()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render29RenderBackendResourceAccessorD1Ev(
    Qt3DRender::Render::RenderBackendResourceAccessor *self) {
  delete self;
}

//  bool Qt3DRender::Render::RenderBackendResourceAccessor::accessResource(Re
//      sourceType type, Qt3DCore::QNodeId nodeId, void **handle, QMutex
//      **lock)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render29RenderBackendResourceAccessor14accessResourceENS1_12ResourceTypeEN8Qt3DCore7QNodeIdEPPvPP6QMutex(
    Qt3DRender::Render::RenderBackendResourceAccessor *self,
    Qt3DRender::Render::RenderBackendResourceAccessor::ResourceType type,
    const Qt3DCore::QNodeId *nodeId,
    void **handle,
    QMutex **lock) {
  return self->accessResource(type, *nodeId, handle, lock);
}
