//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qsortpolicy_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qsortpolicy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/private/qsortpolicy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/framegraph/qsortpolicy.cpp, line 13, as _ZN10Qt3DRender18QSortPolicyPrivateC1Ev
namespace Qt3DRender {
using namespace Qt3DCore;
inline QSortPolicyPrivate::QSortPolicyPrivate()
    : QFrameGraphNodePrivate()
{
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QSortPolicyPrivate that Python can take functions over in. Every Qt3DRender::QSortPolicyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QSortPolicyPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QSortPolicyPrivateCall1)(const void *, int *);
class CuteQt3DRender_QSortPolicyPrivate : public Qt3DRender::QSortPolicyPrivate {
public:
  using Qt3DRender::QSortPolicyPrivate::QSortPolicyPrivate;
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
      CuteQt3DRender_QSortPolicyPrivateCall0 call = reinterpret_cast<CuteQt3DRender_QSortPolicyPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QSortPolicyPrivateCall1 call = reinterpret_cast<CuteQt3DRender_QSortPolicyPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QSortPolicyPrivate::QSortPolicyPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSortPolicyPrivate *ritual_ZN10Qt3DRender18QSortPolicyPrivateC1Ev() {
  return new CuteQt3DRender_QSortPolicyPrivate();
}

//  QSortPolicy *Qt3DRender::QSortPolicyPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QSortPolicy *ritual_ZN10Qt3DRender18QSortPolicyPrivate6q_funcEv(
    Qt3DRender::QSortPolicyPrivate *self) {
  return self->q_func();
}

//  const QSortPolicy *Qt3DRender::QSortPolicyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QSortPolicy *ritual_ZNK10Qt3DRender18QSortPolicyPrivate6q_funcEv(
    const Qt3DRender::QSortPolicyPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QSortPolicyPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QSortPolicyPrivate(
    Qt3DRender::QSortPolicyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QSortPolicyPrivate *>(self)->take(key, call);
}
