//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/technique_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/technique_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::Technique that Python can take functions over in. Every Qt3DRender::Render::Technique
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_TechniqueCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Technique : public Qt3DRender::Render::Technique {
public:
  using Qt3DRender::Render::Technique::Technique;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Technique::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_TechniqueCall0 call = reinterpret_cast<CuteQt3DRender_Render_TechniqueCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Technique::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Technique::Technique()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Technique *ritual_ZN10Qt3DRender6Render9TechniqueC1Ev() {
  return new CuteQt3DRender_Render_Technique();
}

//  Qt3DRender::Render::Technique::~Technique()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9TechniqueD1Ev(
    Qt3DRender::Render::Technique *self) {
  delete self;
}

//  void Qt3DRender::Render::Technique::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique7cleanupEv(
    Qt3DRender::Render::Technique *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Technique::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::Technique::parameters()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render9Technique10parametersEv(
    const Qt3DRender::Render::Technique *self) {
  return new QList<Qt3DCore::QNodeId>(self->parameters());
}

//  void Qt3DRender::Render::Technique::appendRenderPass(Qt3DCore::QNodeId
//      renderPassId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique16appendRenderPassEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNodeId *renderPassId) {
  self->appendRenderPass(*renderPassId);
}

//  void Qt3DRender::Render::Technique::removeRenderPass(Qt3DCore::QNodeId
//      renderPassId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique16removeRenderPassEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNodeId *renderPassId) {
  self->removeRenderPass(*renderPassId);
}

//  void Qt3DRender::Render::Technique::appendFilterKey(Qt3DCore::QNodeId
//      criterionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique15appendFilterKeyEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNodeId *criterionId) {
  self->appendFilterKey(*criterionId);
}

//  void Qt3DRender::Render::Technique::removeFilterKey(Qt3DCore::QNodeId
//      criterionId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique15removeFilterKeyEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNodeId *criterionId) {
  self->removeFilterKey(*criterionId);
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::Technique::filterKeys()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render9Technique10filterKeysEv(
    const Qt3DRender::Render::Technique *self) {
  return new QList<Qt3DCore::QNodeId>(self->filterKeys());
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::Technique::renderPasses()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render9Technique12renderPassesEv(
    const Qt3DRender::Render::Technique *self) {
  return new QList<Qt3DCore::QNodeId>(self->renderPasses());
}

//  const GraphicsApiFilterData
//      *Qt3DRender::Render::Technique::graphicsApiFilter() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::GraphicsApiFilterData *ritual_ZNK10Qt3DRender6Render9Technique17graphicsApiFilterEv(
    const Qt3DRender::Render::Technique *self) {
  return self->graphicsApiFilter();
}

//  bool Qt3DRender::Render::Technique::isCompatibleWithRenderer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render9Technique24isCompatibleWithRendererEv(
    const Qt3DRender::Render::Technique *self) {
  return self->isCompatibleWithRenderer();
}

//  void Qt3DRender::Render::Technique::setCompatibleWithRenderer(bool
//      compatible)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique25setCompatibleWithRendererEb(
    Qt3DRender::Render::Technique *self,
    bool compatible) {
  self->setCompatibleWithRenderer(compatible);
}

//  bool Qt3DRender::Render::Technique::isCompatibleWithFilters(const
//      Qt3DCore::QNodeIdVector &filterKeyIds)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render9Technique23isCompatibleWithFiltersERK5QListIN8Qt3DCore7QNodeIdEE(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNodeIdVector *filterKeyIds) {
  return self->isCompatibleWithFilters(*filterKeyIds);
}

//  void Qt3DRender::Render::Technique::setNodeManager(NodeManagers
//      *nodeManager)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render9Technique14setNodeManagerEPNS0_12NodeManagersE(
    Qt3DRender::Render::Technique *self,
    Qt3DRender::Render::NodeManagers *nodeManager) {
  self->setNodeManager(nodeManager);
}

//  NodeManagers *Qt3DRender::Render::Technique::nodeManager() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::NodeManagers *ritual_ZNK10Qt3DRender6Render9Technique11nodeManagerEv(
    const Qt3DRender::Render::Technique *self) {
  return self->nodeManager();
}

//  a Python function taken by a CuteQt3DRender_Render_Technique, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Technique(
    Qt3DRender::Render::Technique *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Technique *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Technique::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render9Technique16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Technique *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Technique::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::Technique gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Technique__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
