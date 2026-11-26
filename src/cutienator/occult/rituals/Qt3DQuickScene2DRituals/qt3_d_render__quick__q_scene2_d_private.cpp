//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qscene2d_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qscene2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/qscene2d.h>
#include <Qt3DQuickScene2D/private/qscene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2dmanager_p.h>
#include <Qt3DQuickScene2D/private/scene2devent_p.h>
#include <Qt3DQuickScene2D/qscene2d.h>
#include <Qt3DQuickScene2D/private/qscene2d_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DQuickScene2D/private/scene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2dmanager_p.h>
#include <Qt3DQuickScene2D/private/scene2devent_p.h>
#include <Qt3DCore/qentity.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 19, as local:scene2dmanager.cpp:RenderControl
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
class RenderControl : public QQuickRenderControl
{
public:
    RenderControl(QWindow *w) : m_window(w) { }
    QWindow *renderWindow(QPoint *offset) override;

private:
    QWindow *m_window;
};
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 29, as local:scene2dmanager.cpp:RenderControl::renderWindow
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline QWindow *RenderControl::renderWindow(QPoint *offset)
{
    if (offset)
        *offset = QPoint(0, 0);
    return m_window;
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 224, as _ZN10Qt3DRender5Quick14Scene2DManager7cleanupEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::cleanup()
{
    stopAndClean();
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 40, as _ZN10Qt3DRender5Quick14Scene2DManagerC1EPNS0_15QScene2DPrivateE
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline Scene2DManager::Scene2DManager(QScene2DPrivate *priv)
    : m_rootItem(nullptr)
    , m_item(nullptr)
    , m_priv(priv)
    , m_sharedObject(new Scene2DSharedObject(this))
    , m_renderPolicy(QScene2D::Continuous)
    , m_requested(false)
    , m_initialized(false)
    , m_renderSyncRequested(false)
    , m_backendInitialized(false)
    , m_mouseEnabled(true)
{
    // Create render control
    m_sharedObject->m_renderControl = new RenderControl(nullptr);

    // Create window to render the QML with
    m_sharedObject->m_quickWindow = new QQuickWindow(m_sharedObject->m_renderControl);
    // TODOQT6 see qtdeclarative 0d43e21429ee23442ec3a99f641a5665d66e75e2
    //m_sharedObject->m_quickWindow->setClearBeforeRendering(true);
    m_sharedObject->m_quickWindow->setColor(Qt::transparent);

    connect(m_sharedObject->m_renderControl, &QQuickRenderControl::renderRequested,
            this, &Scene2DManager::requestRender);
    connect(m_sharedObject->m_renderControl, &QQuickRenderControl::sceneChanged,
            this, &Scene2DManager::requestRenderSync);
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 121, as _ZN10Qt3DRender5Quick14Scene2DManager12stopAndCleanEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::stopAndClean()
{
    if (m_sharedObject->isInitialized()) {
        // invalidate render control
        m_sharedObject->m_mutex.lock();
        m_sharedObject->setQuitting();
        m_sharedObject->requestInvalidate();
        m_sharedObject->wait();
        m_sharedObject->m_mutex.unlock();

        // delete QQuick render control and window
        m_sharedObject->cleanup();

        // delete QRhi and OpenGL context
        m_sharedObject->m_mutex.lock();
        m_sharedObject->requestQuit();
        m_sharedObject->wait();
        m_sharedObject->m_mutex.unlock();
    }
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 72, as _ZN10Qt3DRender5Quick14Scene2DManager13requestRenderEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::requestRender()
{
    // Don't request render until the backend is initialized.
    if (m_sharedObject->canRender()) {
        if (!m_requested) {
            m_requested = true;
            QCoreApplication::postEvent(this, new Scene2DEvent(Scene2DEvent::Render));
        }
    }
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 83, as _ZN10Qt3DRender5Quick14Scene2DManager17requestRenderSyncEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::requestRenderSync()
{
    // Don't request render until the backed is initialized.
    if (m_sharedObject->canRender()) {
        if (!m_requested) {
            m_requested = true;
            QCoreApplication::postEvent(this, new Scene2DEvent(Scene2DEvent::RenderSync));
        }
    } else {
        m_renderSyncRequested = true;
    }
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/qscene2d.cpp, line 156, as _ZN10Qt3DRender5Quick15QScene2DPrivateC1Ev
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline QScene2DPrivate::QScene2DPrivate()
    : Qt3DCore::QNodePrivate()
    , m_renderManager(new Scene2DManager(this))
    , m_output(nullptr)
{
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/qscene2d.cpp, line 163, as _ZN10Qt3DRender5Quick15QScene2DPrivateD1Ev
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline QScene2DPrivate::~QScene2DPrivate()
{
    m_renderManager->cleanup();
    delete m_renderManager;
}
}  // namespace Qt3DRender::Quick
//  -----------------------------------------------------------------------

//  A Qt3DRender::Quick::QScene2DPrivate that Python can take functions over in. Every Qt3DRender::Quick::QScene2DPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQt3DRender_Quick_QScene2DPrivateCall0)(const void *, Qt3DCore::QScene *, int *);
typedef void (*CuteQt3DRender_Quick_QScene2DPrivateCall1)(const void *, int *);
class CuteQt3DRender_Quick_QScene2DPrivate : public Qt3DRender::Quick::QScene2DPrivate {
public:
  using Qt3DRender::Quick::QScene2DPrivate::QScene2DPrivate;
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
      CuteQt3DRender_Quick_QScene2DPrivateCall0 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DPrivateCall0>(taken[0]);
      call(this, scene, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::setScene(scene);
  }

  //  void Qt3DCore::QNodePrivate::update()
  void update() override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Quick_QScene2DPrivateCall1 call = reinterpret_cast<CuteQt3DRender_Quick_QScene2DPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    Qt3DCore::QNodePrivate::update();
  }
};

//  QScene2D *Qt3DRender::Quick::QScene2DPrivate::q_func()
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2D *ritual_ZN10Qt3DRender5Quick15QScene2DPrivate6q_funcEv(
    Qt3DRender::Quick::QScene2DPrivate *self) {
  return self->q_func();
}

//  const QScene2D *Qt3DRender::Quick::QScene2DPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const Qt3DRender::Quick::QScene2D *ritual_ZNK10Qt3DRender5Quick15QScene2DPrivate6q_funcEv(
    const Qt3DRender::Quick::QScene2DPrivate *self) {
  return self->q_func();
}

//  Qt3DRender::Quick::QScene2DPrivate::QScene2DPrivate()
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::QScene2DPrivate *ritual_ZN10Qt3DRender5Quick15QScene2DPrivateC1Ev() {
  return new CuteQt3DRender_Quick_QScene2DPrivate();
}

//  Qt3DRender::Quick::QScene2DPrivate::~QScene2DPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick15QScene2DPrivateD1Ev(
    Qt3DRender::Quick::QScene2DPrivate *self) {
  delete self;
}

//  a Python function taken by a CuteQt3DRender_Quick_QScene2DPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Quick_QScene2DPrivate(
    Qt3DRender::Quick::QScene2DPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Quick_QScene2DPrivate *>(self)->take(key, call);
}
