//  Written by dev_tooling.RitualGenerator from the records of QtQuick3DRunti
//  meRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qtquick3druntimerenderglobal_p.h>
#include <QtQuick3DRuntimeRender/QtQuick3DRuntimeRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3DRuntimeRender/6.12.0/QtQuick3DRuntimeRender/private/qssgrenderpass_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QSSGRenderPass that Python can take functions over in. Every QSSGRenderPass
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSSGRenderPassCall0)(const void *, int *);
typedef void (*CuteQSSGRenderPassCall1)(const void *, int *);
class CuteQSSGRenderPass : public QSSGRenderPass {
public:
  using QSSGRenderPass::QSSGRenderPass;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QSSGRenderPass8passTypeEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QSSGRenderPass13resetForFrameEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  Type QSSGRenderPass::passType() const
  QSSGRenderPass::Type passType() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSSGRenderPassCall0 call = reinterpret_cast<CuteQSSGRenderPassCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSSGRenderPass::Type>(given);
    }
    return {};
  }

  //  void QSSGRenderPass::resetForFrame()
  void resetForFrame() override {
    if (taken[1]) {
      int handled = 0;
      CuteQSSGRenderPassCall1 call = reinterpret_cast<CuteQSSGRenderPassCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
};

//  QSSGRenderPass::~QSSGRenderPass()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderPassD1Ev(QSSGRenderPass *self) {
  delete self;
}

//  Type QSSGRenderPass::passType() const
extern "C" Q_DECL_EXPORT
QSSGRenderPass::Type ritual_ZNK14QSSGRenderPass8passTypeEv(
    const QSSGRenderPass *self) {
  return self->passType();
}

//  void QSSGRenderPass::resetForFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSSGRenderPass13resetForFrameEv(QSSGRenderPass *self) {
  self->resetForFrame();
}

//  a Python function taken by a CuteQSSGRenderPass, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSSGRenderPass(
    QSSGRenderPass *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSSGRenderPass *>(self)->take(key, call);
}
