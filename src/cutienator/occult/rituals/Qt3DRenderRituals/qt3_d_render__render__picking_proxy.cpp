//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/pickingproxy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/pickingproxy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DRender::Render::PickingProxy that Python can take functions over in. Every Qt3DRender::Render::PickingProxy
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_PickingProxyCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_PickingProxy : public Qt3DRender::Render::PickingProxy {
public:
  using Qt3DRender::Render::PickingProxy::PickingProxy;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::PickingProxy::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_PickingProxyCall0 call = reinterpret_cast<CuteQt3DRender_Render_PickingProxyCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::PickingProxy::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DCore::QNodeId Qt3DRender::Render::PickingProxy::geometryId() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render12PickingProxy10geometryIdEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return new Qt3DCore::QNodeId(self->geometryId());
}

//  int Qt3DRender::Render::PickingProxy::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy13instanceCountEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->instanceCount();
}

//  int Qt3DRender::Render::PickingProxy::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy11vertexCountEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->vertexCount();
}

//  int Qt3DRender::Render::PickingProxy::indexOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy11indexOffsetEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->indexOffset();
}

//  int Qt3DRender::Render::PickingProxy::firstInstance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy13firstInstanceEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->firstInstance();
}

//  int Qt3DRender::Render::PickingProxy::firstVertex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy11firstVertexEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->firstVertex();
}

//  int Qt3DRender::Render::PickingProxy::indexBufferByteOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy21indexBufferByteOffsetEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->indexBufferByteOffset();
}

//  int Qt3DRender::Render::PickingProxy::restartIndexValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy17restartIndexValueEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->restartIndexValue();
}

//  int Qt3DRender::Render::PickingProxy::verticesPerPatch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render12PickingProxy16verticesPerPatchEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->verticesPerPatch();
}

//  bool Qt3DRender::Render::PickingProxy::primitiveRestartEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12PickingProxy23primitiveRestartEnabledEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->primitiveRestartEnabled();
}

//  Qt3DCore::QGeometryView::PrimitiveType
//      Qt3DRender::Render::PickingProxy::primitiveType() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QGeometryView::PrimitiveType ritual_ZNK10Qt3DRender6Render12PickingProxy13primitiveTypeEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->primitiveType();
}

//  bool Qt3DRender::Render::PickingProxy::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12PickingProxy7isValidEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->isValid();
}

//  bool Qt3DRender::Render::PickingProxy::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12PickingProxy7isDirtyEv(
    const Qt3DRender::Render::PickingProxy *self) {
  return self->isDirty();
}

//  a Python function taken by a CuteQt3DRender_Render_PickingProxy, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_PickingProxy(
    Qt3DRender::Render::PickingProxy *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_PickingProxy *>(self)->take(key, call);
}

//  void Qt3DRender::Render::PickingProxy::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12PickingProxy16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::PickingProxy *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::PickingProxy::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
