//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/backendnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/backendnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#include <QtCore/QSharedPointer>

//  A Qt3DRender::Render::BackendNode that Python can take functions over in. Every Qt3DRender::Render::BackendNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_BackendNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_BackendNode : public Qt3DRender::Render::BackendNode {
public:
  using Qt3DRender::Render::BackendNode::BackendNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::BackendNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_BackendNodeCall0 call = reinterpret_cast<CuteQt3DRender_Render_BackendNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::BackendNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::BackendNode::BackendNode(Qt3DCore::QBackendNode::Mode
//      mode)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BackendNode *ritual_ZN10Qt3DRender6Render11BackendNodeC1EN8Qt3DCore12QBackendNode4ModeE(
    Qt3DCore::QBackendNode::Mode mode) {
  return new CuteQt3DRender_Render_BackendNode(mode);
}

//  Qt3DRender::Render::BackendNode::~BackendNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11BackendNodeD1Ev(
    Qt3DRender::Render::BackendNode *self) {
  delete self;
}

//  void Qt3DRender::Render::BackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::BackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::BackendNode::setRenderer(AbstractRenderer
//      *renderer)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11BackendNode11setRendererEPNS0_16AbstractRendererE(
    Qt3DRender::Render::BackendNode *self,
    Qt3DRender::Render::AbstractRenderer *renderer) {
  self->setRenderer(renderer);
}

//  AbstractRenderer *Qt3DRender::Render::BackendNode::renderer() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::AbstractRenderer *ritual_ZNK10Qt3DRender6Render11BackendNode8rendererEv(
    const Qt3DRender::Render::BackendNode *self) {
  return self->renderer();
}

//  QSharedPointer<RenderBackendResourceAccessor>
//      Qt3DRender::Render::BackendNode::resourceAccessor() const
extern "C" Q_DECL_EXPORT
QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> *ritual_ZNK10Qt3DRender6Render11BackendNode16resourceAccessorEv(
    const Qt3DRender::Render::BackendNode *self) {
  return new QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor>(
      self->resourceAccessor());
}

//  Qt3DRender::Render::BackendNode::BackendNode(Qt3DCore::QBackendNodePrivat
//      e &dd)
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::BackendNode *ritual_ZN10Qt3DRender6Render11BackendNodeC1ERN8Qt3DCore19QBackendNodePrivateE(
    Qt3DCore::QBackendNodePrivate *dd) {
  return new CuteQt3DRender_Render_BackendNode(*dd);
}

//  void Qt3DRender::Render::BackendNode::markDirty(AbstractRenderer::Backend
//      NodeDirtySet changes)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render11BackendNode9markDirtyE6QFlagsINS0_16AbstractRenderer20BackendNodeDirtyFlagEE(
    Qt3DRender::Render::BackendNode *self,
    int changes) {
  self->markDirty(
      QFlags<Qt3DRender::Render::AbstractRenderer::BackendNodeDirtyFlag>::fromInt(changes));
}

//  a Python function taken by a CuteQt3DRender_Render_BackendNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_BackendNode(
    Qt3DRender::Render::BackendNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_BackendNode *>(self)->take(key, call);
}

//  void Qt3DRender::Render::BackendNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render11BackendNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::BackendNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::BackendNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> a
//      ritual of Qt3DRender::Render::BackendNode gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_BackendNode__QSharedPointer_Qt3DRender_Render_RenderBackendResourceAccessor(
    QSharedPointer<Qt3DRender::Render::RenderBackendResourceAccessor> *self) {
  delete self;
}
