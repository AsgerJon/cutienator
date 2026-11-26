//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshaderimage_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshaderimage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/qshaderimage.h>
#include <Qt3DRender/private/qshaderimage_p.h>
#include <Qt3DRender/qabstracttexture.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/render/materialsystem/qshaderimage.cpp, line 12, as _ZN10Qt3DRender19QShaderImagePrivateC1Ev
namespace Qt3DRender {
inline QShaderImagePrivate::QShaderImagePrivate()
    : Qt3DCore::QNodePrivate()
    , m_texture(nullptr)
    , m_mipLevel(0)
    , m_layer(0)
    , m_access(QShaderImage::ReadWrite)
    , m_format(QShaderImage::Automatic)
    , m_layered(false)
{
}
}  // namespace Qt3DRender

//  from ../qt3d/src/render/materialsystem/qshaderimage.cpp, line 23, as _ZN10Qt3DRender19QShaderImagePrivateD1Ev
namespace Qt3DRender {
inline QShaderImagePrivate::~QShaderImagePrivate()
{
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::QShaderImagePrivate that Python can take functions over in. Every Qt3DRender::QShaderImagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_QShaderImagePrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_QShaderImagePrivateCall1)(const void *, int *);
class CuteQt3DRender_QShaderImagePrivate : public Qt3DRender::QShaderImagePrivate {
public:
  using Qt3DRender::QShaderImagePrivate::QShaderImagePrivate;
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
      CuteQt3DRender_QShaderImagePrivateCall0 call = reinterpret_cast<CuteQt3DRender_QShaderImagePrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_QShaderImagePrivateCall1 call = reinterpret_cast<CuteQt3DRender_QShaderImagePrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DRender::QShaderImagePrivate::QShaderImagePrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImagePrivate *ritual_ZN10Qt3DRender19QShaderImagePrivateC1Ev() {
  return new CuteQt3DRender_QShaderImagePrivate();
}

//  Qt3DRender::QShaderImagePrivate::~QShaderImagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender19QShaderImagePrivateD1Ev(
    Qt3DRender::QShaderImagePrivate *self) {
  delete self;
}

//  QShaderImage *Qt3DRender::QShaderImagePrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderImage *ritual_ZN10Qt3DRender19QShaderImagePrivate6q_funcEv(
    Qt3DRender::QShaderImagePrivate *self) {
  return self->q_func();
}

//  const QShaderImage *Qt3DRender::QShaderImagePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::QShaderImage *ritual_ZNK10Qt3DRender19QShaderImagePrivate6q_funcEv(
    const Qt3DRender::QShaderImagePrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DRender_QShaderImagePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_QShaderImagePrivate(
    Qt3DRender::QShaderImagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_QShaderImagePrivate *>(self)->take(key, call);
}
