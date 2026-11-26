//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/renderpass_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/renderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::RenderPass that Python can take functions over in. Every Qt3DRender::Render::RenderPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_RenderPassCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_RenderPass : public Qt3DRender::Render::RenderPass {
public:
  using Qt3DRender::Render::RenderPass::RenderPass;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::RenderPass::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_RenderPassCall0 call = reinterpret_cast<CuteQt3DRender_Render_RenderPassCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::RenderPass::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::RenderPass::RenderPass()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::RenderPass *ritual_ZN10Qt3DRender6Render10RenderPassC1Ev() {
  return new CuteQt3DRender_Render_RenderPass();
}

//  Qt3DRender::Render::RenderPass::~RenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPassD1Ev(
    Qt3DRender::Render::RenderPass *self) {
  delete self;
}

//  void Qt3DRender::Render::RenderPass::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass7cleanupEv(
    Qt3DRender::Render::RenderPass *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::RenderPass::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  Qt3DCore::QNodeId Qt3DRender::Render::RenderPass::shaderProgram() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render10RenderPass13shaderProgramEv(
    const Qt3DRender::Render::RenderPass *self) {
  return new Qt3DCore::QNodeId(self->shaderProgram());
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::RenderPass::filterKeys()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render10RenderPass10filterKeysEv(
    const Qt3DRender::Render::RenderPass *self) {
  return new QList<Qt3DCore::QNodeId>(self->filterKeys());
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::RenderPass::parameters()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render10RenderPass10parametersEv(
    const Qt3DRender::Render::RenderPass *self) {
  return new QList<Qt3DCore::QNodeId>(self->parameters());
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::RenderPass::renderStates()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render10RenderPass12renderStatesEv(
    const Qt3DRender::Render::RenderPass *self) {
  return new QList<Qt3DCore::QNodeId>(self->renderStates());
}

//  bool Qt3DRender::Render::RenderPass::hasRenderStates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render10RenderPass15hasRenderStatesEv(
    const Qt3DRender::Render::RenderPass *self) {
  return self->hasRenderStates();
}

//  void Qt3DRender::Render::RenderPass::appendFilterKey(Qt3DCore::QNodeId
//      filterKeyId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass15appendFilterKeyEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNodeId *filterKeyId) {
  self->appendFilterKey(*filterKeyId);
}

//  void Qt3DRender::Render::RenderPass::removeFilterKey(Qt3DCore::QNodeId
//      filterKeyId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass15removeFilterKeyEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNodeId *filterKeyId) {
  self->removeFilterKey(*filterKeyId);
}

//  void Qt3DRender::Render::RenderPass::addRenderState(Qt3DCore::QNodeId
//      renderStateId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass14addRenderStateEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNodeId *renderStateId) {
  self->addRenderState(*renderStateId);
}

//  void Qt3DRender::Render::RenderPass::removeRenderState(Qt3DCore::QNodeId
//      renderStateId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render10RenderPass17removeRenderStateEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNodeId *renderStateId) {
  self->removeRenderState(*renderStateId);
}

//  a Python function taken by a CuteQt3DRender_Render_RenderPass, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_RenderPass(
    Qt3DRender::Render::RenderPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_RenderPass *>(self)->take(key, call);
}

//  void Qt3DRender::Render::RenderPass::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render10RenderPass16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::RenderPass *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::RenderPass::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::RenderPass
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_RenderPass__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
