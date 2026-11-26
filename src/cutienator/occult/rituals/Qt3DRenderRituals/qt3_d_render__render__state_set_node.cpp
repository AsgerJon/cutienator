//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/statesetnode_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/statesetnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::StateSetNode that Python can take functions over in. Every Qt3DRender::Render::StateSetNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_StateSetNodeCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_StateSetNode : public Qt3DRender::Render::StateSetNode {
public:
  using Qt3DRender::Render::StateSetNode::StateSetNode;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::StateSetNode::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_StateSetNodeCall0 call = reinterpret_cast<CuteQt3DRender_Render_StateSetNodeCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::StateSetNode::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::StateSetNode::StateSetNode()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::StateSetNode *ritual_ZN10Qt3DRender6Render12StateSetNodeC1Ev() {
  return new CuteQt3DRender_Render_StateSetNode();
}

//  Qt3DRender::Render::StateSetNode::~StateSetNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateSetNodeD1Ev(
    Qt3DRender::Render::StateSetNode *self) {
  delete self;
}

//  bool Qt3DRender::Render::StateSetNode::hasRenderStates() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender6Render12StateSetNode15hasRenderStatesEv(
    const Qt3DRender::Render::StateSetNode *self) {
  return self->hasRenderStates();
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::StateSetNode::renderStates()
//      const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render12StateSetNode12renderStatesEv(
    const Qt3DRender::Render::StateSetNode *self) {
  return new QList<Qt3DCore::QNodeId>(self->renderStates());
}

//  void Qt3DRender::Render::StateSetNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateSetNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::StateSetNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::StateSetNode::addRenderState(Qt3DCore::QNodeId
//      renderStateId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateSetNode14addRenderStateEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::StateSetNode *self,
    const Qt3DCore::QNodeId *renderStateId) {
  self->addRenderState(*renderStateId);
}

//  void
//      Qt3DRender::Render::StateSetNode::removeRenderState(Qt3DCore::QNodeId
//      renderStateId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render12StateSetNode17removeRenderStateEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::StateSetNode *self,
    const Qt3DCore::QNodeId *renderStateId) {
  self->removeRenderState(*renderStateId);
}

//  a Python function taken by a CuteQt3DRender_Render_StateSetNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_StateSetNode(
    Qt3DRender::Render::StateSetNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_StateSetNode *>(self)->take(key, call);
}

//  void Qt3DRender::Render::StateSetNode::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render12StateSetNode16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::StateSetNode *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::StateSetNode::syncFromFrontEnd(
      frontEnd,
      firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::StateSetNode
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_StateSetNode__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
