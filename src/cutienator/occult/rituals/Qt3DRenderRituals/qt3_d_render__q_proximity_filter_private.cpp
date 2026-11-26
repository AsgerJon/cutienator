//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qproximityfilter_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <QtSensors/qproximitysensor.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qproximityfilter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qproximityfilter.h>
#include <Qt3DRender/private/qproximityfilter_p.h>
#include <Qt3DCore/qentity.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qproximityfilter.cpp, line 12, as _ZN10Qt3DRender23QProximityFilterPrivateC1Ev
namespace Qt3DRender {
inline QProximityFilterPrivate::QProximityFilterPrivate()
    : QFrameGraphNodePrivate()
    , m_entity(nullptr)
    , m_distanceThreshold(0.0f)
{
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QProximityFilterPrivate that Python can take functions over in. Every Qt3DRender::QProximityFilterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QProximityFilterPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QProximityFilterPrivateCall1)(const void *, int *);
class CuteQt3DRender_QProximityFilterPrivate : public Qt3DRender::QProximityFilterPrivate {
public:
  using Qt3DRender::QProximityFilterPrivate::QProximityFilterPrivate;
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
      CuteQt3DRender_QProximityFilterPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QProximityFilterPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QProximityFilterPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QProximityFilterPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QProximityFilterPrivate::QProximityFilterPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QProximityFilterPrivate *ritual_ZN10Qt3DRender23QProximityFilterPrivateC1Ev() {
  return new CuteQt3DRender_QProximityFilterPrivate();
}

//  QProximityFilter *Qt3DRender::QProximityFilterPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QProximityFilter *ritual_ZN10Qt3DRender23QProximityFilterPrivate6q_funcEv(
    Qt3DRender::QProximityFilterPrivate *self) {
  return self->q_func();
}

//  const QProximityFilter *Qt3DRender::QProximityFilterPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QProximityFilter *ritual_ZNK10Qt3DRender23QProximityFilterPrivate6q_funcEv(
    const Qt3DRender::QProximityFilterPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QProximityFilterPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QProximityFilterPrivate(
    Qt3DRender::QProximityFilterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QProximityFilterPrivate *>(self)->take(key, call);
}
