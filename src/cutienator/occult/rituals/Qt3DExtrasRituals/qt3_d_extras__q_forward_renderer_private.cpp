//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/6.12.0/Qt3DExtras/private/qforwardrenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DExtras/Qt3DExtras>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/6.12.0/Qt3DExtras/private/qforwardrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DExtras/qforwardrenderer.h>
#include <Qt3DExtras/private/qforwardrenderer_p.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DRender/qviewport.h>
#include <Qt3DRender/qcameraselector.h>
#include <Qt3DRender/qclearbuffers.h>
#include <Qt3DRender/qfilterkey.h>
#include <Qt3DRender/qfrustumculling.h>
#include <Qt3DRender/qrendersurfaceselector.h>
#include <Qt3DRender/qdebugoverlay.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/extras/defaults/qforwardrenderer.cpp, line 16, as local:qforwardrenderer.cpp:initResources
static void initResources()
{
#ifdef QT_STATIC
    Q_INIT_RESOURCE(extras);
#endif
}

//  from ../qt3d/src/extras/defaults/qforwardrenderer.cpp, line 29, as _ZN10Qt3DExtras23QForwardRendererPrivateC1Ev
namespace Qt3DExtras {
using namespace Qt3DRender;
inline QForwardRendererPrivate::QForwardRendererPrivate()
    : QTechniqueFilterPrivate()
    , m_surfaceSelector(new QRenderSurfaceSelector)
    , m_viewport(new QViewport())
    , m_cameraSelector(new QCameraSelector())
    , m_clearBuffer(new QClearBuffers())
    , m_frustumCulling(new QFrustumCulling())
    , m_debugOverlay(new QDebugOverlay())
{
}
}  // namespace Qt3DExtras

//  from ../qt3d/src/extras/defaults/qforwardrenderer.cpp, line 40, as _ZN10Qt3DExtras23QForwardRendererPrivate4initEv
namespace Qt3DExtras {
using namespace Qt3DRender;
inline void QForwardRendererPrivate::init()
{
    Q_Q(QForwardRenderer);

    initResources();

    m_debugOverlay->setParent(m_frustumCulling);
    m_debugOverlay->setEnabled(false);
    m_frustumCulling->setParent(m_clearBuffer);
    m_clearBuffer->setParent(m_cameraSelector);
    m_cameraSelector->setParent(m_viewport);
    m_viewport->setParent(m_surfaceSelector);
    m_surfaceSelector->setParent(q);

    m_viewport->setNormalizedRect(QRectF(0.0, 0.0, 1.0, 1.0));
    m_clearBuffer->setClearColor(Qt::white);
    m_clearBuffer->setBuffers(QClearBuffers::ColorDepthBuffer);

    QFilterKey *forwardRenderingStyle = new QFilterKey(q);
    forwardRenderingStyle->setName(QStringLiteral("renderingStyle"));
    forwardRenderingStyle->setValue(QStringLiteral("forward"));
    q->addMatch(forwardRenderingStyle);
}
}  // namespace Qt3DExtras
//  -----------------------------------------------------------------------

//  A Qt3DExtras::QForwardRendererPrivate that Python can take functions over in. Every Qt3DExtras::QForwardRendererPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DExtras_QForwardRendererPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DExtras_QForwardRendererPrivateCall1)(const void *, int *);
class CuteQt3DExtras_QForwardRendererPrivate : public Qt3DExtras::QForwardRendererPrivate {
public:
  using Qt3DExtras::QForwardRendererPrivate::QForwardRendererPrivate;
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
      CuteQt3DExtras_QForwardRendererPrivateCall0 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DExtras_QForwardRendererPrivateCall1 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  Qt3DExtras::QForwardRendererPrivate::QForwardRendererPrivate()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QForwardRendererPrivate *ritual_ZN10Qt3DExtras23QForwardRendererPrivateC1Ev() {
  return new CuteQt3DExtras_QForwardRendererPrivate();
}

//  void Qt3DExtras::QForwardRendererPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras23QForwardRendererPrivate4initEv(
    Qt3DExtras::QForwardRendererPrivate *self) {
  self->init();
}

//  QForwardRenderer *Qt3DExtras::QForwardRendererPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QForwardRenderer *ritual_ZN10Qt3DExtras23QForwardRendererPrivate6q_funcEv(
    Qt3DExtras::QForwardRendererPrivate *self) {
  return self->q_func();
}

//  const QForwardRenderer *Qt3DExtras::QForwardRendererPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QForwardRenderer *ritual_ZNK10Qt3DExtras23QForwardRendererPrivate6q_funcEv(
    const Qt3DExtras::QForwardRendererPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQt3DExtras_QForwardRendererPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QForwardRendererPrivate(
    Qt3DExtras::QForwardRendererPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QForwardRendererPrivate *>(self)->take(key, call);
}
