//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSSGRenderTextureProviderExtension that Python can take functions over in. Every QSSGRenderTextureProviderExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSSGRenderTextureProviderExtensionCall0)(const void *, int *);
class CuteQSSGRenderTextureProviderExtension : public QSSGRenderTextureProviderExtension {
public:
  using QSSGRenderTextureProviderExtension::QSSGRenderTextureProviderExtension;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSSGRenderExtension13resetForFrameEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  void QSSGRenderExtension::resetForFrame()
  void resetForFrame() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGRenderTextureProviderExtensionCall0 call = reinterpret_cast<CuteQSSGRenderTextureProviderExtensionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QSSGRenderTextureProviderExtension::~QSSGRenderTextureProviderExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN34QSSGRenderTextureProviderExtensionD1Ev(
    QSSGRenderTextureProviderExtension *self) {
  delete self;
}

//  RenderMode QSSGRenderTextureProviderExtension::mode() const
extern "C" Q_DECL_EXPORT
QSSGRenderExtension::RenderMode ritual_ZNK34QSSGRenderTextureProviderExtension4modeEv(
    const QSSGRenderTextureProviderExtension *self) {
  return self->mode();
}

//  RenderStage QSSGRenderTextureProviderExtension::stage() const
extern "C" Q_DECL_EXPORT
QSSGRenderExtension::RenderStage ritual_ZNK34QSSGRenderTextureProviderExtension5stageEv(
    const QSSGRenderTextureProviderExtension *self) {
  return self->stage();
}

//  a Python function taken by a CuteQSSGRenderTextureProviderExtension, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGRenderTextureProviderExtension(
    QSSGRenderTextureProviderExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGRenderTextureProviderExtension *>(self)->take(key, call);
}
