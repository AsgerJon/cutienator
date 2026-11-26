//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qrenderstateset_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qrenderstateset_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qrenderstateset.h>
#include <Qt3DRender/private/qrenderstateset_p.h>
#include <Qt3DRender/qrenderstate.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qrenderstateset.cpp, line 16, as _ZN10Qt3DRender22QRenderStateSetPrivateC1Ev
namespace Qt3DRender {
using namespace Qt3DCore;
inline QRenderStateSetPrivate::QRenderStateSetPrivate()
    : QFrameGraphNodePrivate()
{
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QRenderStateSetPrivate that Python can take functions over in. Every Qt3DRender::QRenderStateSetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QRenderStateSetPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QRenderStateSetPrivateCall1)(const void *, int *);
class CuteQt3DRender_QRenderStateSetPrivate : public Qt3DRender::QRenderStateSetPrivate {
public:
  using Qt3DRender::QRenderStateSetPrivate::QRenderStateSetPrivate;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate8setSceneEPNS_6QSceneE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN8Qt3DCore12QNodePrivate6updateEv")) {
      taken[1] = call;
      return true;
    }
    return false;
  }

  //  void Qt3DCore::QNodePrivate::setScene(QScene *scene)
  void setScene(Qt3DCore::QScene *scene) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_QRenderStateSetPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QRenderStateSetPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QRenderStateSetPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QRenderStateSetPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QRenderStateSetPrivate::QRenderStateSetPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderStateSetPrivate *ritual_ZN10Qt3DRender22QRenderStateSetPrivateC1Ev() {
  return new CuteQt3DRender_QRenderStateSetPrivate();
}

//  QRenderStateSet *Qt3DRender::QRenderStateSetPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderStateSet *ritual_ZN10Qt3DRender22QRenderStateSetPrivate6q_funcEv(
    Qt3DRender::QRenderStateSetPrivate *self) {
  return self->q_func();
}

//  const QRenderStateSet *Qt3DRender::QRenderStateSetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QRenderStateSet *ritual_ZNK10Qt3DRender22QRenderStateSetPrivate6q_funcEv(
    const Qt3DRender::QRenderStateSetPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QRenderStateSetPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QRenderStateSetPrivate(
    Qt3DRender::QRenderStateSetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QRenderStateSetPrivate *>(self)->take(key, call);
}
