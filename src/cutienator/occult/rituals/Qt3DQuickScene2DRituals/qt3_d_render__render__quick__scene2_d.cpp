//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <Qt3DRender/Qt3DRender>

//  A Qt3DRender::Render::Quick::Scene2D that Python can take functions over in. Every Qt3DRender::Render::Quick::Scene2D
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_Quick_Scene2DCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Quick_Scene2D : public Qt3DRender::Render::Quick::Scene2D {
public:
  using Qt3DRender::Render::Quick::Scene2D::Scene2D;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_Quick_Scene2DCall0 call = reinterpret_cast<CuteQt3DRender_Render_Quick_Scene2DCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Quick::Scene2D::Scene2D()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Quick::Scene2D *ritual_ZN10Qt3DRender6Render5Quick7Scene2DC1Ev() {
  return new CuteQt3DRender_Render_Quick_Scene2D();
}

//  Qt3DRender::Render::Quick::Scene2D::~Scene2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2DD1Ev(
    Qt3DRender::Render::Quick::Scene2D *self) {
  delete self;
}

//  void Qt3DRender::Render::Quick::Scene2D::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D6renderEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->render();
}

//  void Qt3DRender::Render::Quick::Scene2D::initializeRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D16initializeRenderEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->initializeRender();
}

//  void Qt3DRender::Render::Quick::Scene2D::setSharedObject(Qt3DRender::Quic
//      k::Scene2DSharedObjectPtr sharedObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D15setSharedObjectE14QSharedPointerINS_5Quick19Scene2DSharedObjectEE(
    Qt3DRender::Render::Quick::Scene2D *self,
    const Qt3DRender::Quick::Scene2DSharedObjectPtr *sharedObject) {
  self->setSharedObject(*sharedObject);
}

//  void Qt3DRender::Render::Quick::Scene2D::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D10invalidateEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->invalidate();
}

//  void Qt3DRender::Render::Quick::Scene2D::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D7cleanupEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Quick::Scene2D::setOutput(Qt3DCore::QNodeId
//      outputId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D9setOutputEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Quick::Scene2D *self,
    const Qt3DCore::QNodeId *outputId) {
  self->setOutput(*outputId);
}

//  void Qt3DRender::Render::Quick::Scene2D::initializeSharedObject()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D22initializeSharedObjectEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->initializeSharedObject();
}

//  void Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Quick::Scene2D *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  void Qt3DRender::Render::Quick::Scene2D::syncRenderControl()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D17syncRenderControlEv(
    Qt3DRender::Render::Quick::Scene2D *self) {
  self->syncRenderControl();
}

//  bool Qt3DRender::Render::Quick::Scene2D::registerObjectPickerEvents(Qt3DC
//      ore::QEntity *qentity)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render5Quick7Scene2D26registerObjectPickerEventsEPN8Qt3DCore7QEntityE(
    Qt3DRender::Render::Quick::Scene2D *self,
    Qt3DCore::QEntity *qentity) {
  return self->registerObjectPickerEvents(qentity);
}

//  void Qt3DRender::Render::Quick::Scene2D::unregisterObjectPickerEvents(Qt3
//      DCore::QNodeId entityId)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D28unregisterObjectPickerEventsEN8Qt3DCore7QNodeIdE(
    Qt3DRender::Render::Quick::Scene2D *self,
    const Qt3DCore::QNodeId *entityId) {
  self->unregisterObjectPickerEvents(*entityId);
}

//  void Qt3DRender::Render::Quick::Scene2D::handlePickEvent(int type, const
//      QPickEvent *ev)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render5Quick7Scene2D15handlePickEventEiPKNS_10QPickEventE(
    Qt3DRender::Render::Quick::Scene2D *self,
    int type,
    const Qt3DRender::QPickEvent *ev) {
  self->handlePickEvent(type, ev);
}

//  a Python function taken by a CuteQt3DRender_Render_Quick_Scene2D, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Quick_Scene2D(
    Qt3DRender::Render::Quick::Scene2D *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Quick_Scene2D *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(const
//      Qt3DCore::QNode *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render5Quick7Scene2D16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Quick::Scene2D *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Quick::Scene2D::syncFromFrontEnd(
      frontEnd,
      firstTime);
}
