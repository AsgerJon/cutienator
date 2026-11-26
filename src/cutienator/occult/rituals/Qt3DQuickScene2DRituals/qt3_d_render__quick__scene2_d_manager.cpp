//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dmanager_p.h, Qt
//  6.12.0.
//  Edited by hand on 2026-11-26: moc's output for
//  'Qt3DRender::Quick::Scene2DManager' is pasted in, cut from what the moc
//  of Qt 6.12.0 writes for its header: Qt's library keeps it to itself;
//  added are 2 rituals that lean on what moc writes for a class of the part
//  Qt keeps to itself, whose ritual file carries moc's output, drafted by a
//  copy of the generator that lets those names through. A copy of a meta-
//  object is a second one: 'qobject_cast' between it and Qt's own does not
//  match. Kept as it is when the generator runs again.
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/qt3dquickscene2d_global_p.h>
#include <Qt3DQuickScene2D/Qt3DQuickScene2D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene2D/6.12.0/Qt3DQuickScene2D/private/scene2dmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetatype.h>
#include <QtCore/qtmochelpers.h>
#include <memory>
#include <QtCore/qxptype_traits.h>
#include <Qt3DQuickScene2D/qscene2d.h>
#include <Qt3DQuickScene2D/private/qscene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2d_p.h>
#include <Qt3DQuickScene2D/private/scene2dmanager_p.h>
#include <Qt3DQuickScene2D/private/scene2devent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
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

//  from Qt3DQuickScene2D__Qt3DRender_Quick_Scene2DManager.cpp, line 1, as moc:Qt3DRender::Quick::Scene2DManager
#ifndef Q_CONSTINIT
#define Q_CONSTINIT
#endif
QT_WARNING_PUSH
QT_WARNING_DISABLE_DEPRECATED
namespace {
struct qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t {};
} // unnamed namespace

template <> constexpr inline auto Qt3DRender::Quick::Scene2DManager::qt_create_metaobjectdata<qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>()
{
    namespace QMC = QtMocConstants;
    QtMocHelpers::StringRefStorage qt_stringData {
        "Qt3DRender::Quick::Scene2DManager"
    };

    QtMocHelpers::UintData qt_methods {
    };
    QtMocHelpers::UintData qt_properties {
    };
    QtMocHelpers::UintData qt_enums {
    };
    return QtMocHelpers::metaObjectData<Scene2DManager, qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>(QMC::MetaObjectFlag{}, qt_stringData,
            qt_methods, qt_properties, qt_enums);
}
Q_CONSTINIT const QMetaObject Qt3DRender::Quick::Scene2DManager::staticMetaObject = { {
    QMetaObject::SuperData::link<QObject::staticMetaObject>(),
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>.stringdata,
    qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>.data,
    qt_static_metacall,
    nullptr,
    qt_staticMetaObjectRelocatingContent<qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>.metaTypes,
    nullptr
} };

void Qt3DRender::Quick::Scene2DManager::qt_static_metacall(QObject *_o, QMetaObject::Call _c, int _id, void **_a)
{
    auto *_t = static_cast<Scene2DManager *>(_o);
    (void)_t;
    (void)_c;
    (void)_id;
    (void)_a;
}

const QMetaObject *Qt3DRender::Quick::Scene2DManager::metaObject() const
{
    return QObject::d_ptr->metaObject ? QObject::d_ptr->dynamicMetaObject() : &staticMetaObject;
}

void *Qt3DRender::Quick::Scene2DManager::qt_metacast(const char *_clname)
{
    if (!_clname) return nullptr;
    if (!strcmp(_clname, qt_staticMetaObjectStaticContent<qt_meta_tag_ZN10Qt3DRender5Quick14Scene2DManagerE_t>.strings))
        return static_cast<void*>(this);
    return QObject::qt_metacast(_clname);
}

int Qt3DRender::Quick::Scene2DManager::qt_metacall(QMetaObject::Call _c, int _id, void **_a)
{
    _id = QObject::qt_metacall(_c, _id, _a);
    return _id;
}
QT_WARNING_POP

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 159, as _ZN10Qt3DRender5Quick14Scene2DManager5eventEP6QEvent
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline bool Scene2DManager::event(QEvent *e)
{
    switch (static_cast<Scene2DEvent::Type>(e->type())) {

    case Scene2DEvent::Render: {
        // just render request, don't need to call sync in render thread
        QMutexLocker lock(&m_sharedObject->m_mutex);
        m_sharedObject->requestRender(false);
        m_requested = false;
        return true;
    }

    case Scene2DEvent::RenderSync: {
        // sync and render request, main and render threads must be synchronized
        if (!m_sharedObject->isQuitting())
            doRenderSync();
        m_requested = false;
        return true;
    }

    case Scene2DEvent::Prepare: {
        m_sharedObject->m_renderControl->prepareThread(m_sharedObject->m_renderThread);
        m_sharedObject->setPrepared();

        if (m_renderSyncRequested) {
            if (!m_requested) {
                m_requested = true;
                QCoreApplication::postEvent(this, new Scene2DEvent(Scene2DEvent::RenderSync));
            }
            m_renderSyncRequested = false;
        }
        return true;
    }

    case Scene2DEvent::Initialized: {
        // backend is initialized, start the qml
        m_backendInitialized = true;
        startIfInitialized();
        return true;
    }

    case Scene2DEvent::Rendered: {
        // render is done, excellent, now clean anything not needed anymore.
        stopAndClean();
        return true;
    }

    default:
        break;
    }
    return QObject::event(e);
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

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 67, as _ZN10Qt3DRender5Quick14Scene2DManagerD1Ev
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline Scene2DManager::~Scene2DManager()
{
    m_sharedObject = nullptr;
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

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 212, as _ZN10Qt3DRender5Quick14Scene2DManager12doRenderSyncEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::doRenderSync()
{
    QMutexLocker lock(&m_sharedObject->m_mutex);

    m_sharedObject->requestRender(true);
    m_sharedObject->m_renderControl->polishItems();

    // begin waiting render thread
    m_sharedObject->wait();
    m_requested = false;
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 96, as _ZN10Qt3DRender5Quick14Scene2DManager18startIfInitializedEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::startIfInitialized()
{
    if (!m_initialized && m_backendInitialized && m_item != nullptr) {
        m_rootItem = m_item;

        // Associate root item with the window.
        m_rootItem->setParentItem(m_sharedObject->m_quickWindow->contentItem());

        // Update window size.
        updateSizes();

        m_initialized = true;
        m_sharedObject->setInitialized();

        // Request render if we have already been requested and preparation has already been done
        if (m_sharedObject->isPrepared() && m_renderSyncRequested) {
            if (!m_requested) {
                m_requested = true;
                QCoreApplication::postEvent(this, new Scene2DEvent(Scene2DEvent::RenderSync));
            }
            m_renderSyncRequested = false;
        }
    }
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

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 142, as _ZN10Qt3DRender5Quick14Scene2DManager11updateSizesEv
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::updateSizes()
{
    const int width = m_rootItem->width();
    const int height = m_rootItem->height();
    if (width == 0 || height == 0) {
        qWarning() << "QScene2D: Root item size not set.";
        return;
    }
    m_sharedObject->m_quickWindow->setGeometry(0, 0, width, height);
}
}  // namespace Qt3DRender::Quick

//  from ../qt3d/src/quick3d/quick3dscene2d/items/scene2dmanager.cpp, line 153, as _ZN10Qt3DRender5Quick14Scene2DManager7setItemEP10QQuickItem
namespace Qt3DRender::Quick {
using namespace Qt3DCore;
inline void Scene2DManager::setItem(QQuickItem *item)
{
    m_item = item;
    startIfInitialized();
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
//  -----------------------------------------------------------------------

//  A Qt3DRender::Quick::Scene2DManager that Python can take functions over in. Every Qt3DRender::Quick::Scene2DManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Quick_Scene2DManagerCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Quick_Scene2DManagerCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_Scene2DManagerCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_Scene2DManagerCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_Scene2DManagerCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_Scene2DManagerCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Quick_Scene2DManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Quick_Scene2DManager : public Qt3DRender::Quick::Scene2DManager {
public:
  using Qt3DRender::Quick::Scene2DManager::Scene2DManager;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool Qt3DRender::Quick::Scene2DManager::event(QEvent *e)
  bool event(QEvent *e) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall0 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall0>(taken[0]);
      bool given = call(this, e, &handled);
      if (handled) return given;
    }
    return Qt3DRender::Quick::Scene2DManager::event(e);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall1 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall2 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall3 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall4 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall5 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_Quick_Scene2DManagerCall6 call = reinterpret_cast<CuteQt3DRender_Quick_Scene2DManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::Quick::Scene2DManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender5Quick14Scene2DManager10metaObjectEv(
    const Qt3DRender::Quick::Scene2DManager *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Quick::Scene2DManager::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender5Quick14Scene2DManager11qt_metacastEPKc(
    Qt3DRender::Quick::Scene2DManager *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Quick::Scene2DManager::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender5Quick14Scene2DManager11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Quick::Scene2DManager *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DRender::Quick::Scene2DManager::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DRender5Quick14Scene2DManager2trEPKcS3_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DRender::Quick::Scene2DManager::tr(s, c, n));
}

//  Qt3DRender::Quick::Scene2DManager::Scene2DManager(QScene2DPrivate *priv)
extern "C" Q_DECL_EXPORT
Qt3DRender::Quick::Scene2DManager *ritual_ZN10Qt3DRender5Quick14Scene2DManagerC1EPNS0_15QScene2DPrivateE(
    Qt3DRender::Quick::QScene2DPrivate *priv) {
  return new CuteQt3DRender_Quick_Scene2DManager(priv);
}

//  Qt3DRender::Quick::Scene2DManager::~Scene2DManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManagerD1Ev(
    Qt3DRender::Quick::Scene2DManager *self) {
  delete self;
}

//  void Qt3DRender::Quick::Scene2DManager::requestRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager13requestRenderEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->requestRender();
}

//  void Qt3DRender::Quick::Scene2DManager::requestRenderSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager17requestRenderSyncEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->requestRenderSync();
}

//  void Qt3DRender::Quick::Scene2DManager::doRenderSync()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager12doRenderSyncEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->doRenderSync();
}

//  void Qt3DRender::Quick::Scene2DManager::startIfInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager18startIfInitializedEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->startIfInitialized();
}

//  void Qt3DRender::Quick::Scene2DManager::stopAndClean()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager12stopAndCleanEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->stopAndClean();
}

//  void Qt3DRender::Quick::Scene2DManager::updateSizes()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager11updateSizesEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->updateSizes();
}

//  void Qt3DRender::Quick::Scene2DManager::setItem(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager7setItemEP10QQuickItem(
    Qt3DRender::Quick::Scene2DManager *self,
    QQuickItem *item) {
  self->setItem(item);
}

//  bool Qt3DRender::Quick::Scene2DManager::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender5Quick14Scene2DManager5eventEP6QEvent(
    Qt3DRender::Quick::Scene2DManager *self,
    QEvent *e) {
  return self->event(e);
}

//  void Qt3DRender::Quick::Scene2DManager::cleanup()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender5Quick14Scene2DManager7cleanupEv(
    Qt3DRender::Quick::Scene2DManager *self) {
  self->cleanup();
}

//  a Python function taken by a CuteQt3DRender_Quick_Scene2DManager, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Quick_Scene2DManager(
    Qt3DRender::Quick::Scene2DManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Quick_Scene2DManager *>(self)->take(key, call);
}

//  bool Qt3DRender::Quick::Scene2DManager::event(QEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN10Qt3DRender5Quick14Scene2DManager5eventEP6QEvent(
    Qt3DRender::Quick::Scene2DManager *self,
    QEvent *e) {
  return self->Qt3DRender::Quick::Scene2DManager::event(e);
}
