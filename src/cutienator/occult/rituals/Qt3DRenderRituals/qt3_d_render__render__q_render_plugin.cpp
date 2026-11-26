//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrenderplugin_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrenderplugin_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobjectdefs.h>
#include <cstring>

//  A Qt3DRender::Render::QRenderPlugin that Python can take functions over in. Every Qt3DRender::Render::QRenderPlugin
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQt3DRender_Render_QRenderPluginCall0)(const void *, Qt3DRender::QRenderAspect *, Qt3DRender::Render::AbstractRenderer *, int *);
typedef bool (*CuteQt3DRender_Render_QRenderPluginCall1)(const void *, Qt3DRender::QRenderAspect *, int *);
class CuteQt3DRender_Render_QRenderPlugin : public Qt3DRender::Render::QRenderPlugin {
public:
  using Qt3DRender::Render::QRenderPlugin::QRenderPlugin;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render13QRenderPlugin20registerBackendTypesEPNS_13QRenderAspectEPNS0_16AbstractRendererE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10Qt3DRender6Render13QRenderPlugin22unregisterBackendTypesEPNS_13QRenderAspectE")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  bool
  //      Qt3DRender::Render::QRenderPlugin::registerBackendTypes(QRenderAs
  //      pect *aspect, AbstractRenderer *renderer)
  bool registerBackendTypes(
      Qt3DRender::QRenderAspect *aspect,
      Qt3DRender::Render::AbstractRenderer *renderer) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Render_QRenderPluginCall0 call = reinterpret_cast<CuteQt3DRender_Render_QRenderPluginCall0>(taken[0]);
      bool given = call(this, aspect, renderer, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  bool Qt3DRender::Render::QRenderPlugin::unregisterBackendTypes(QRende
  //      rAspect *aspect)
  bool unregisterBackendTypes(Qt3DRender::QRenderAspect *aspect) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Render_QRenderPluginCall1 call = reinterpret_cast<CuteQt3DRender_Render_QRenderPluginCall1>(taken[1]);
      bool given = call(this, aspect, &handled);
      if (handled) return given;
    }
    return {};
  }
};

//  bool
//      Qt3DRender::Render::QRenderPlugin::registerBackendTypes(QRenderAspect
//      *aspect, AbstractRenderer *renderer)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render13QRenderPlugin20registerBackendTypesEPNS_13QRenderAspectEPNS0_16AbstractRendererE(
    Qt3DRender::Render::QRenderPlugin *self,
    Qt3DRender::QRenderAspect *aspect,
    Qt3DRender::Render::AbstractRenderer *renderer) {
  return self->registerBackendTypes(aspect, renderer);
}

//  bool
//      Qt3DRender::Render::QRenderPlugin::unregisterBackendTypes(QRenderAspe
//      ct *aspect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender6Render13QRenderPlugin22unregisterBackendTypesEPNS_13QRenderAspectE(
    Qt3DRender::Render::QRenderPlugin *self,
    Qt3DRender::QRenderAspect *aspect) {
  return self->unregisterBackendTypes(aspect);
}

//  void Qt3DRender::Render::QRenderPlugin::registerBackendType(QRenderAspect
//      *aspect, const QMetaObject &obj, const
//      Qt3DCore::QBackendNodeMapperPtr &functor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13QRenderPlugin19registerBackendTypeEPNS_13QRenderAspectERK11QMetaObjectRK14QSharedPointerIN8Qt3DCore18QBackendNodeMapperEE(
    Qt3DRender::Render::QRenderPlugin *self,
    Qt3DRender::QRenderAspect *aspect,
    const QMetaObject *obj,
    const Qt3DCore::QBackendNodeMapperPtr *functor) {
  self->registerBackendType(aspect, *obj, *functor);
}

//  void
//      Qt3DRender::Render::QRenderPlugin::unregisterBackendType(QRenderAspec
//      t *aspect, const QMetaObject &obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender6Render13QRenderPlugin21unregisterBackendTypeEPNS_13QRenderAspectERK11QMetaObject(
    Qt3DRender::Render::QRenderPlugin *self,
    Qt3DRender::QRenderAspect *aspect,
    const QMetaObject *obj) {
  self->unregisterBackendType(aspect, *obj);
}

//  a Python function taken by a CuteQt3DRender_Render_QRenderPlugin, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Render_QRenderPlugin(
    Qt3DRender::Render::QRenderPlugin *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Render_QRenderPlugin *>(self)->take(key, call);
}
