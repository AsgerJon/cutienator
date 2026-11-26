//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qtextureatlas_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/private/areaallocator_p.h>
#include <QtCore/qglobal.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <Qt3DExtras/private/qtextureatlas_p.h>
#include <Qt3DExtras/private/qtextureatlas_p_p.h>
#include <Qt3DRender/qtexturedata.h>
#include <Qt3DRender/qabstracttextureimage.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/text/areaallocator.cpp, line 66, as _ZN10Qt3DExtras13AreaAllocatorD1Ev
namespace Qt3DExtras {
inline AreaAllocator::~AreaAllocator()
{
    delete m_root;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 85, as _ZN10Qt3DExtras20QTextureAtlasPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasPrivate::QTextureAtlasPrivate()
    : Qt3DRender::QAbstractTexturePrivate()
{
    m_target = Qt3DRender::QAbstractTexture::TargetAutomatic;
    m_format = Qt3DRender::QAbstractTexture::RGBA8_UNorm;
    m_width = 256;
    m_height = 256;
    m_depth = 1;
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/text/qtextureatlas.cpp, line 95, as _ZN10Qt3DExtras20QTextureAtlasPrivateD1Ev
namespace Qt3DExtras {
using namespace Qt3DCore;
inline QTextureAtlasPrivate::~QTextureAtlasPrivate()
{
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QTextureAtlasPrivate that Python can take functions over in. Every Qt3DExtras::QTextureAtlasPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QTextureAtlasPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QTextureAtlasPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QTextureAtlasPrivate : public Qt3DExtras::QTextureAtlasPrivate {
public:
  using Qt3DExtras::QTextureAtlasPrivate::QTextureAtlasPrivate;
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
      CuteQt3DExtras_QTextureAtlasPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QTextureAtlasPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QTextureAtlasPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QTextureAtlasPrivate::QTextureAtlasPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureAtlasPrivate *ritual_ZN10Qt3DExtras20QTextureAtlasPrivateC1Ev() {
  return new CuteQt3DExtras_QTextureAtlasPrivate();
}

//  Qt3DExtras::QTextureAtlasPrivate::~QTextureAtlasPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras20QTextureAtlasPrivateD1Ev(
    Qt3DExtras::QTextureAtlasPrivate *self) {
  delete self;
}

//  QTextureAtlas *Qt3DExtras::QTextureAtlasPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QTextureAtlas *ritual_ZN10Qt3DExtras20QTextureAtlasPrivate6q_funcEv(
    Qt3DExtras::QTextureAtlasPrivate *self) {
  return self->q_func();
}

//  const QTextureAtlas *Qt3DExtras::QTextureAtlasPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QTextureAtlas *ritual_ZNK10Qt3DExtras20QTextureAtlasPrivate6q_funcEv(
    const Qt3DExtras::QTextureAtlasPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QTextureAtlasPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QTextureAtlasPrivate(
    Qt3DExtras::QTextureAtlasPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QTextureAtlasPrivate *>(self)->take(key, call);
}
