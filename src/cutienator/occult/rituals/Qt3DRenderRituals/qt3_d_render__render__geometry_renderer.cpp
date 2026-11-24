//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/geometryrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>

//  A Qt3DRender::Render::GeometryRenderer that Python can take functions over in. Every Qt3DRender::Render::GeometryRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_GeometryRendererCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_GeometryRenderer : public Qt3DRender::Render::GeometryRenderer {
public:
  using Qt3DRender::Render::GeometryRenderer::GeometryRenderer;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_GeometryRendererCall0 call = reinterpret_cast<CuteQt3DRender_Render_GeometryRendererCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DCore::QNodeId Qt3DRender::Render::GeometryRenderer::geometryId()
//      const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render16GeometryRenderer10geometryIdEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return new Qt3DCore::QNodeId(self->geometryId());
}

//  int Qt3DRender::Render::GeometryRenderer::instanceCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer13instanceCountEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->instanceCount();
}

//  int Qt3DRender::Render::GeometryRenderer::vertexCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer11vertexCountEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->vertexCount();
}

//  int Qt3DRender::Render::GeometryRenderer::indexOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer11indexOffsetEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->indexOffset();
}

//  int Qt3DRender::Render::GeometryRenderer::firstInstance() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer13firstInstanceEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->firstInstance();
}

//  int Qt3DRender::Render::GeometryRenderer::firstVertex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer11firstVertexEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->firstVertex();
}

//  int Qt3DRender::Render::GeometryRenderer::indexBufferByteOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer21indexBufferByteOffsetEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->indexBufferByteOffset();
}

//  int Qt3DRender::Render::GeometryRenderer::restartIndexValue() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer17restartIndexValueEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->restartIndexValue();
}

//  int Qt3DRender::Render::GeometryRenderer::verticesPerPatch() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10Qt3DRender6Render16GeometryRenderer16verticesPerPatchEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->verticesPerPatch();
}

//  bool Qt3DRender::Render::GeometryRenderer::primitiveRestartEnabled()
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16GeometryRenderer23primitiveRestartEnabledEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->primitiveRestartEnabled();
}

//  QGeometryRenderer::PrimitiveType
//      Qt3DRender::Render::GeometryRenderer::primitiveType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QGeometryRenderer::PrimitiveType ritual_ZNK10Qt3DRender6Render16GeometryRenderer13primitiveTypeEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->primitiveType();
}

//  bool Qt3DRender::Render::GeometryRenderer::isDirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16GeometryRenderer7isDirtyEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->isDirty();
}

//  bool Qt3DRender::Render::GeometryRenderer::hasView() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render16GeometryRenderer7hasViewEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->hasView();
}

//  float Qt3DRender::Render::GeometryRenderer::sortIndex() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DRender6Render16GeometryRenderer9sortIndexEv(
    const Qt3DRender::Render::GeometryRenderer *self) {
  return self->sortIndex();
}

//  a Python function taken by a CuteQt3DRender_Render_GeometryRenderer, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_GeometryRenderer(
    Qt3DRender::Render::GeometryRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_GeometryRenderer *>(self)->take(key, call);
}

//  void Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render16GeometryRenderer16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::GeometryRenderer *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::GeometryRenderer::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
