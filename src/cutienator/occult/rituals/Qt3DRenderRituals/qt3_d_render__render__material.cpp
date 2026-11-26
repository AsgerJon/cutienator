//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/material_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/material_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DCore/qnodeid.h>
#include <cstring>
#include <QtCore/QList>
#include <Qt3DCore/Qt3DCore>

//  A Qt3DRender::Render::Material that Python can take functions over in. Every Qt3DRender::Render::Material
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Render_MaterialCall0)(const void *, const Qt3DCore::QNode *, bool, int *);
class CuteQt3DRender_Render_Material : public Qt3DRender::Render::Material {
public:
  using Qt3DRender::Render::Material::Material;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QBackendNode16syncFromFrontEndEPKNS_5QNodeEb")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DRender::Render::Material::syncFromFrontEnd(const
  //      Qt3DCore::QNode *frontEnd, bool firstTime)
  void syncFromFrontEnd(
      const Qt3DCore::QNode *frontEnd,
      bool firstTime) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_MaterialCall0 call = reinterpret_cast<CuteQt3DRender_Render_MaterialCall0>(taken[0]);
      call(this, frontEnd, firstTime, &handled);
      if (handled) return;
    }
    Qt3DRender::Render::Material::syncFromFrontEnd(frontEnd, firstTime);
  }
};

//  Qt3DRender::Render::Material::Material()
extern "C" Q_DECL_EXPORT
Qt3DRender::Render::Material *ritual_ZN10Qt3DRender6Render8MaterialC1Ev() {
  return new CuteQt3DRender_Render_Material();
}

//  Qt3DRender::Render::Material::~Material()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8MaterialD1Ev(
    Qt3DRender::Render::Material *self) {
  delete self;
}

//  void Qt3DRender::Render::Material::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Material7cleanupEv(
    Qt3DRender::Render::Material *self) {
  self->cleanup();
}

//  void Qt3DRender::Render::Material::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render8Material16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Material *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->syncFromFrontEnd(frontEnd, firstTime);
}

//  QList<Qt3DCore::QNodeId> Qt3DRender::Render::Material::parameters() const
extern "C" Q_DECL_EXPORT
QList<Qt3DCore::QNodeId> *ritual_ZNK10Qt3DRender6Render8Material10parametersEv(
    const Qt3DRender::Render::Material *self) {
  return new QList<Qt3DCore::QNodeId>(self->parameters());
}

//  Qt3DCore::QNodeId Qt3DRender::Render::Material::effect() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QNodeId *ritual_ZNK10Qt3DRender6Render8Material6effectEv(
    const Qt3DRender::Render::Material *self) {
  return new Qt3DCore::QNodeId(self->effect());
}

//  a Python function taken by a CuteQt3DRender_Render_Material, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_Material(
    Qt3DRender::Render::Material *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_Material *>(self)->take(key, call);
}

//  void Qt3DRender::Render::Material::syncFromFrontEnd(const Qt3DCore::QNode
//      *frontEnd, bool firstTime)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender6Render8Material16syncFromFrontEndEPKN8Qt3DCore5QNodeEb(
    Qt3DRender::Render::Material *self,
    const Qt3DCore::QNode *frontEnd,
    bool firstTime) {
  self->Qt3DRender::Render::Material::syncFromFrontEnd(frontEnd, firstTime);
}

//  a QList<Qt3DCore::QNodeId> a ritual of Qt3DRender::Render::Material gave
extern "C" Q_DECL_EXPORT
void ritual_drop_Qt3DRender_Render_Material__QList_Qt3DCore_QNodeId(
    QList<Qt3DCore::QNodeId> *self) {
  delete self;
}
