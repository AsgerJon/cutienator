//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/ssg/qssgrenderextensions.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSSGRenderExtension that Python can take functions over in. Every QSSGRenderExtension
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSSGRenderExtensionCall0)(const void *, int *);
typedef int (*CuteQSSGRenderExtensionCall1)(const void *, int *);
typedef int (*CuteQSSGRenderExtensionCall2)(const void *, int *);
class CuteQSSGRenderExtension : public QSSGRenderExtension {
public:
  using QSSGRenderExtension::QSSGRenderExtension;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSSGRenderExtension13resetForFrameEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSSGRenderExtension4modeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QSSGRenderExtension5stageEv")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QSSGRenderExtension::resetForFrame()
  void resetForFrame() override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGRenderExtensionCall0 call = reinterpret_cast<CuteQSSGRenderExtensionCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  RenderMode QSSGRenderExtension::mode() const
  QSSGRenderExtension::RenderMode mode() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSSGRenderExtensionCall1 call = reinterpret_cast<CuteQSSGRenderExtensionCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderExtension::RenderMode>(given);
    }
    return {};
  }

  //  RenderStage QSSGRenderExtension::stage() const
  QSSGRenderExtension::RenderStage stage() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSSGRenderExtensionCall2 call = reinterpret_cast<CuteQSSGRenderExtensionCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderExtension::RenderStage>(given);
    }
    return {};
  }
};

//  QSSGRenderExtension::~QSSGRenderExtension()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderExtensionD1Ev(QSSGRenderExtension *self) {
  delete self;
}

//  void QSSGRenderExtension::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QSSGRenderExtension13resetForFrameEv(
    QSSGRenderExtension *self) {
  self->resetForFrame();
}

//  RenderMode QSSGRenderExtension::mode() const
extern "C" Q_DECL_EXPORT
QSSGRenderExtension::RenderMode ritual_ZNK19QSSGRenderExtension4modeEv(
    const QSSGRenderExtension *self) {
  return self->mode();
}

//  RenderStage QSSGRenderExtension::stage() const
extern "C" Q_DECL_EXPORT
QSSGRenderExtension::RenderStage ritual_ZNK19QSSGRenderExtension5stageEv(
    const QSSGRenderExtension *self) {
  return self->stage();
}

//  a Python function taken by a CuteQSSGRenderExtension, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGRenderExtension(
    QSSGRenderExtension *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGRenderExtension *>(self)->take(key, call);
}
