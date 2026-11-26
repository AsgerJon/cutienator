//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qwaitfence_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qwaitfence_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qwaitfence.h>
#include <Qt3DRender/private/qwaitfence_p.h>
#include <Qt3DRender/private/qframegraphnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qwaitfence.cpp, line 12, as _ZN10Qt3DRender17QWaitFencePrivateC1Ev
namespace Qt3DRender {
inline QWaitFencePrivate::QWaitFencePrivate()
    : QFrameGraphNodePrivate()
    , m_handleType(QWaitFence::NoHandle)
    , m_handle(QVariant())
    , m_waitOnCPU(false)
    , m_timeout(std::numeric_limits<quint64>::max())
{
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QWaitFencePrivate that Python can take functions over in. Every Qt3DRender::QWaitFencePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QWaitFencePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QWaitFencePrivateCall1)(const void *, int *);
class CuteQt3DRender_QWaitFencePrivate : public Qt3DRender::QWaitFencePrivate {
public:
  using Qt3DRender::QWaitFencePrivate::QWaitFencePrivate;
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
      CuteQt3DRender_QWaitFencePrivateCall0 call = reinterpret_cast<CuteQt3DRender_QWaitFencePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QWaitFencePrivateCall1 call = reinterpret_cast<CuteQt3DRender_QWaitFencePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QWaitFencePrivate::QWaitFencePrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QWaitFencePrivate *ritual_ZN10Qt3DRender17QWaitFencePrivateC1Ev() {
  return new CuteQt3DRender_QWaitFencePrivate();
}

//  a Python function taken by a CuteQt3DRender_QWaitFencePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QWaitFencePrivate(
    Qt3DRender::QWaitFencePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QWaitFencePrivate *>(self)->take(key, call);
}
