//  Written by dev_tooling.RitualGenerator from the records of Qt3DQuickExtra
//  s/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/qt3dquickextras_global_p.h>
#include <Qt3DQuickExtras/Qt3DQuickExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/6.12.0/Qt3DQuickExtras/private/quick3dlevelofdetailloader_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickExtras/private/quick3dlevelofdetailloader_p_p.h>
#include <Qt3DRender/qlevelofdetailboundingsphere.h>
#include <Qt3DRender/qcamera.h>
#include <Qt3DQuick/private/quick3dentityloader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dextras/items/quick3dlevelofdetailloader.cpp, line 15, as _ZN10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoaderPrivateC1Ev
namespace Qt3DExtras::Extras::Quick {
inline Quick3DLevelOfDetailLoaderPrivate::Quick3DLevelOfDetailLoaderPrivate()
    : QEntityPrivate()
    , m_loader(new Qt3DCore::Quick::Quick3DEntityLoader)
    , m_lod(new Qt3DRender::QLevelOfDetail)
{
}
}  // namespace Qt3DExtras::Extras::Quick
//  -----------------------------------------------------------------------

//  A Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate that Python can take functions over in. Every Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall1)(const void *, int *);
class CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate : public Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate {
public:
  using Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::Quick3DLevelOfDetailLoaderPrivate;
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
      CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::Quick3DLeve
//      lOfDetailLoaderPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *ritual_ZN10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoaderPrivateC1Ev() {
  return new CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate();
}

//  Quick3DLevelOfDetailLoader
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::q_func
//      ()
extern "C" Q_DECL_EXPORT
Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *ritual_ZN10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoaderPrivate6q_funcEv(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *self) {
  return self->q_func();
}

//  const Quick3DLevelOfDetailLoader
//      *Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate::q_func
//      () const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoader *ritual_ZNK10Qt3DExtras6Extras5Quick33Quick3DLevelOfDetailLoaderPrivate6q_funcEv(
    const Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a
//      CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate(
    Qt3DExtras::Extras::Quick::Quick3DLevelOfDetailLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_Extras_Quick_Quick3DLevelOfDetailLoaderPrivate *>(self)->take(key, call);
}
