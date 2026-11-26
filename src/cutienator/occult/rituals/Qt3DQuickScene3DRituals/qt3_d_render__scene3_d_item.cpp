//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3ditem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DQuickScene3D/Qt3DQuickScene3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3ditem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qvariant.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/private/scene3ditem_p.h>
#include <Qt3DCore/qt3dcore_global.h>
#include <Qt3DCore/qentity.h>
#include <Qt3DCore/QAspectEngine>
#if QT_CONFIG(qt3d_input)
#include <Qt3DInput/QInputAspect>
#include <Qt3DInput/qinputsettings.h>
#endif
#if QT_CONFIG(qt3d_logic)
#include <Qt3DLogic/qlogicaspect.h>
#endif
#if QT_CONFIG(qt3d_animation)
#include <Qt3DAnimation/qanimationaspect.h>
#endif
#include <Qt3DRender/QRenderAspect>
#include <Qt3DRender/qcamera.h>
#include <Qt3DRender/qrendersurfaceselector.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qoffscreensurface.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQuick/qquickwindow.h>
#include <QtQuick/qquickrendercontrol.h>
#include <Qt3DRender/private/qrendersurfaceselector_p.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DRender/private/rendersettings_p.h>
#include <Qt3DRender/qt3drender-config.h>
#include <Qt3DQuickScene3D/private/scene3dlogging_p.h>
#include <Qt3DQuickScene3D/private/scene3drenderer_p.h>
#include <Qt3DQuickScene3D/private/scene3dsgnode_p.h>
#include <Qt3DCore/private/qaspectengine_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <QtCore/QThread>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 49, as local:scene3ditem.cpp:AspectEngineDestroyer
namespace Qt3DRender {
class AspectEngineDestroyer : public QObject
{
    Q_OBJECT

public:
    AspectEngineDestroyer()
        : QObject()
    {}

    ~AspectEngineDestroyer()
    {
    }

    void reset(int targetCount)
    {
        m_allowed = 0;
        m_targetAllowed = targetCount;
    }

    void allowRelease()
    {
        ++m_allowed;
        if (m_allowed == m_targetAllowed) {
            if (QThread::currentThread() == thread())
                delete this;
            else
                deleteLater();
        }
    }

    void setSGNodeAlive(bool alive) { m_sgNodeAlive = alive; }
    bool sgNodeAlive() const { return m_sgNodeAlive;}

private:
    int m_allowed = 0;
    int m_targetAllowed = 0;
    bool m_sgNodeAlive = false;
};
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 631, as local:scene3ditem.cpp:Scene3DManagerNode
namespace Qt3DRender {
class Scene3DManagerNode : public QSGNode
{
public:
   explicit Scene3DManagerNode(Qt3DCore::QAspectEngine *aspectEngine,
                               AspectEngineDestroyer *destroyer)
        : m_aspectEngine(aspectEngine)
        , m_destroyer(destroyer)
        , m_renderAspect(new QRenderAspect(QRenderAspect::Manual))
        , m_renderer(new Scene3DRenderer())
    {
        m_destroyer->setSGNodeAlive(true);
    }

    ~Scene3DManagerNode()
    {
        // Stop the Qt3D Simulation Loop
        auto engineD = Qt3DCore::QAspectEnginePrivate::get(m_aspectEngine);
        engineD->exitSimulationLoop();

        // Shutdown renderer
        delete m_renderer;

        m_destroyer->setSGNodeAlive(false);

        // Allow AspectEngine destruction
        m_destroyer->allowRelease();
    }

    void init()
    {
        m_aspectEngine->registerAspect(m_renderAspect);
        m_renderer->init(m_aspectEngine, m_renderAspect);
        m_wasInitialized = true;
    }

    inline bool isInitialized() const { return m_wasInitialized; }
    inline QRenderAspect *renderAspect() const { return m_renderAspect; }
    inline Scene3DRenderer *renderer() const { return m_renderer; }
private:
    Qt3DCore::QAspectEngine *m_aspectEngine;
    AspectEngineDestroyer *m_destroyer;
    QRenderAspect *m_renderAspect;
    Scene3DRenderer *m_renderer;
    bool m_wasInitialized = false;
};
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 858, as _ZN10Qt3DRender11Scene3DItem15mousePressEventEP11QMouseEvent
namespace Qt3DRender {
inline void Scene3DItem::mousePressEvent(QMouseEvent *event)
{
    Q_UNUSED(event);
    //Prevent subsequent move and release events being disregarded my the default event->ignore() from QQuickItem
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 174, as _ZN10Qt3DRender11Scene3DItemD1Ev
namespace Qt3DRender {
inline Scene3DItem::~Scene3DItem()
{
    // The SceneGraph is non deterministic in the order in which it will
    // destroy the QSGNode that were created by the item. This unfortunately
    // makes it difficult to know when it is safe to destroy the QAspectEngine.
    // To track this we use the AspectEngineDestroyer. It allows keeping the
    // AspectEngine alive and deleting later when we know that both Scene3DItem
    // and Scene3DRenderer have been destroyed.

    delete m_aspectToDelete;

    if (m_aspectEngineDestroyer)
        m_aspectEngineDestroyer->allowRelease();
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 198, as _ZNK10Qt3DRender11Scene3DItem7aspectsEv
namespace Qt3DRender {
inline QStringList Scene3DItem::aspects() const
{
    return m_aspects;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 210, as _ZNK10Qt3DRender11Scene3DItem6entityEv
namespace Qt3DRender {
inline Qt3DCore::QEntity *Scene3DItem::entity() const
{
    return m_entity;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 613, as _ZNK10Qt3DRender11Scene3DItem11multisampleEv
namespace Qt3DRender {
inline bool Scene3DItem::multisample() const
{
    return m_multisample;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 551, as _ZNK10Qt3DRender11Scene3DItem14isHoverEnabledEv
namespace Qt3DRender {
inline bool Scene3DItem::isHoverEnabled() const
{
    return acceptHoverEvents();
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 340, as _ZNK10Qt3DRender11Scene3DItem21cameraAspectRatioModeEv
namespace Qt3DRender {
inline Scene3DItem::CameraAspectRatioMode Scene3DItem::cameraAspectRatioMode() const
{
    return m_cameraAspectRatioMode;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 345, as _ZNK10Qt3DRender11Scene3DItem15compositingModeEv
namespace Qt3DRender {
inline Scene3DItem::CompositingMode Scene3DItem::compositingMode() const
{
    return m_compositingMode;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 447, as _ZN10Qt3DRender11Scene3DItem16prepareQt3DFrameEv
namespace Qt3DRender {
inline bool Scene3DItem::prepareQt3DFrame()
{
    static bool dontRenderWhenHidden = !qgetenv("QT3D_SCENE3D_STOP_RENDER_HIDDEN").isEmpty();

    // If we are not visible, don't processFrame changes as we would end up
    // waiting forever for the scene to be rendered which won't happen
    // if the Scene3D item is not visible
    if (!isVisible() && dontRenderWhenHidden)
        return false;
    if (!m_aspectEngine)
        return false;
    Q_ASSERT(QThread::currentThread() == thread());

    // Since we are in manual mode, trigger jobs for the next frame
    Qt3DCore::QAspectEnginePrivate *aspectEnginePriv = static_cast<Qt3DCore::QAspectEnginePrivate *>(QObjectPrivate::get(m_aspectEngine));
    if (!aspectEnginePriv->m_initialized)
        return false;

    Q_ASSERT(m_aspectEngine->runMode() == Qt3DCore::QAspectEngine::Manual);
    m_aspectEngine->processFrame();
    // The above essentially sets the number of RV for the RenderQueue and
    // processes the jobs for the frame (it's blocking) When
    // Scene3DRender::updatePaintNode is called, following this step, we know
    // that the RenderQueue target count has been set and that everything
    // should be ready for rendering

    // processFrame() must absolutely be followed by a single call to
    // render
    // At startup, we have no garantee that the QtQuick Render Thread doesn't
    // start rendering before this function has been called
    // We add in a safety to skip such frames as this could otherwise
    // make Qt3D enter a locked state

    // Note: it's too early to request an update at this point as
    // beforeSync() triggered by afterAnimating  is considered
    // to be as being part of the current frame update
    return true;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 511, as _ZN10Qt3DRender11Scene3DItem16setWindowSurfaceEP7QObject
namespace Qt3DRender {
inline void Scene3DItem::setWindowSurface(QObject *rootObject)
{
    Qt3DRender::QRenderSurfaceSelector *surfaceSelector = Qt3DRender::QRenderSurfaceSelectorPrivate::find(rootObject);

    // Set the item's window surface if it appears
    // the surface wasn't set on the surfaceSelector
    if (surfaceSelector && !surfaceSelector->surface()) {
        // We may not have a real, exposed QQuickWindow when the Quick rendering
        // is redirected via QQuickRenderControl (f.ex. QQuickWidget).
        if (QWindow *rw = QQuickRenderControl::renderWindowFor(this->window())) {
            surfaceSelector->setSurface(rw);
        } else {
            surfaceSelector->setSurface(this->window());
        }
    }
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 588, as _ZN10Qt3DRender11Scene3DItem23updateCameraAspectRatioEv
namespace Qt3DRender {
inline void Scene3DItem::updateCameraAspectRatio()
{
    if (m_camera) {
        if (m_compositingMode == FBO)
            m_camera->setAspectRatio(static_cast<float>(width()) /
                                     static_cast<float>(height()));
        else
            m_camera->setAspectRatio(static_cast<float>(window()->width()) /
                                     static_cast<float>(window()->height()));
    }
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 401, as _ZN10Qt3DRender11Scene3DItem11needsRenderEPNS_13QRenderAspectE
namespace Qt3DRender {
inline bool Scene3DItem::needsRender(QRenderAspect *renderAspect)
{
    // We need the dirty flag which is connected to the change arbiter
    // receiving updates to know whether something in the scene has changed

    // Ideally we would use shouldRender() alone but given that it becomes true
    // only after the arbiter has sync the changes and might be reset before
    // process jobs is completed, we cannot fully rely on it. It would require
    // splitting processFrame in 2 parts.

    // We only use it for cases where Qt3D render may require several loops of
    // the simulation to fully process a frame (e.g shaders are loaded in frame
    // n and we can only build render commands for the new shader at frame n +
    // This is where renderer->shouldRender() comes into play as it knows
    // whether some states remain dirty or not (even after processFrame is
    // called)

    auto renderAspectPriv = static_cast<QRenderAspectPrivate*>(QRenderAspectPrivate::get(renderAspect));
    const bool dirty = m_dirty
            || (renderAspectPriv
                && renderAspectPriv->m_renderer
                && renderAspectPriv->m_renderer->shouldRender());

    if (m_dirty) {
        --m_framesToRender;
        if (m_framesToRender <= 0)
            m_dirty = false;
    }
    return dirty || m_framesToRender > 0;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 498, as _ZN10Qt3DRender11Scene3DItem19updateWindowSurfaceEv
namespace Qt3DRender {
inline void Scene3DItem::updateWindowSurface()
{
    if (!m_entity)
        return;
    Qt3DRender::QRenderSurfaceSelector *surfaceSelector =
        Qt3DRender::QRenderSurfaceSelectorPrivate::find(entity());
    if (surfaceSelector) {
        if (QWindow *rw = QQuickRenderControl::renderWindowFor(this->window())) {
            surfaceSelector->setSurface(rw);
        }
    }
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3ditem.cpp, line 215, as _ZN10Qt3DRender11Scene3DItem12applyAspectsEv
namespace Qt3DRender {
inline void Scene3DItem::applyAspects()
{
    if (!m_aspectEngine)
        return;

    // Aspects are owned by the aspect engine
    for (const QString &aspect : std::as_const(m_aspects)) {
        if (aspect == QLatin1String("render")) // This one is hardwired anyway
            continue;
        if (aspect == QLatin1String("input"))  {
#if QT_CONFIG(qt3d_input)
            m_aspectEngine->registerAspect(new Qt3DInput::QInputAspect);
            continue;
#else
            qFatal("Scene3D requested the Qt 3D input aspect but Qt 3D wasn't configured to build the Qt 3D Input aspect");
#endif
        }
        if (aspect == QLatin1String("logic"))  {
#if QT_CONFIG(qt3d_logic)
            m_aspectEngine->registerAspect(new Qt3DLogic::QLogicAspect);
            continue;
#else
            qFatal("Scene3D requested the Qt 3D logic aspect but Qt 3D wasn't configured to build the Qt 3D Logic aspect");
#endif
        }
        if (aspect == QLatin1String("animation"))  {
#if QT_CONFIG(qt3d_animation)
            m_aspectEngine->registerAspect(new Qt3DAnimation::QAnimationAspect);
            continue;
#else
            qFatal("Scene3D requested the Qt 3D animation aspect but Qt 3D wasn't configured to build the Qt 3D Animation aspect");
#endif
        }
        m_aspectEngine->registerAspect(aspect);
    }
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::Scene3DItem that Python can take functions over in. Every Qt3DRender::Scene3DItem
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQt3DRender_Scene3DItemCall0)(const void *, QSGNode *, QQuickItem::UpdatePaintNodeData *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall1)(const void *, QMouseEvent *, int *);
typedef const QRectF * (*CuteQt3DRender_Scene3DItemCall2)(const void *, int *);
typedef const QRectF * (*CuteQt3DRender_Scene3DItemCall3)(const void *, int *);
typedef bool (*CuteQt3DRender_Scene3DItemCall4)(const void *, const QPointF *, int *);
#if QT_CONFIG(im)
typedef const QVariant * (*CuteQt3DRender_Scene3DItemCall5)(const void *, int, int *);
#endif  // QT_CONFIG(im)
typedef bool (*CuteQt3DRender_Scene3DItemCall6)(const void *, int *);
typedef void * (*CuteQt3DRender_Scene3DItemCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Scene3DItemCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall9)(const void *, int, const QQuickItem::ItemChangeData *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall10)(const void *, const QRectF *, const QRectF *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall11)(const void *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall12)(const void *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall13)(const void *, QKeyEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall14)(const void *, QKeyEvent *, int *);
#if QT_CONFIG(im)
typedef void (*CuteQt3DRender_Scene3DItemCall15)(const void *, QInputMethodEvent *, int *);
#endif  // QT_CONFIG(im)
typedef void (*CuteQt3DRender_Scene3DItemCall16)(const void *, QFocusEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall17)(const void *, QFocusEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall20)(const void *, QMouseEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall21)(const void *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall22)(const void *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQt3DRender_Scene3DItemCall23)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQt3DRender_Scene3DItemCall24)(const void *, QTouchEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall25)(const void *, QHoverEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall26)(const void *, QHoverEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall27)(const void *, QHoverEvent *, int *);
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQt3DRender_Scene3DItemCall28)(const void *, QDragEnterEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQt3DRender_Scene3DItemCall29)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQt3DRender_Scene3DItemCall30)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
typedef void (*CuteQt3DRender_Scene3DItemCall31)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(quick_draganddrop)
typedef bool (*CuteQt3DRender_Scene3DItemCall32)(const void *, QQuickItem *, QEvent *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall33)(const void *, int *);
typedef void (*CuteQt3DRender_Scene3DItemCall34)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Scene3DItemCall35)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall36)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall37)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall38)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall39)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DItemCall40)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Scene3DItem : public Qt3DRender::Scene3DItem {
public:
  using Qt3DRender::Scene3DItem::Scene3DItem;
  void *taken[41] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN10QQuickItem15updatePaintNodeEP7QSGNodePNS_19UpdatePaintNodeDataE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15mousePressEventEP11QMouseEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem12boundingRectEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8clipRectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem8containsERK7QPointF")) {
      taken[4] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZNK10QQuickItem17isTextureProviderEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK10QQuickItem15textureProviderEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN10QQuickItem10itemChangeENS_10ItemChangeERKNS_14ItemChangeDataE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14geometryChangeERK6QRectFS2_")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus10classBeginEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QQmlParserStatus17componentCompleteEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13keyPressEventEP9QKeyEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15keyReleaseEventEP9QKeyEvent")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem16inputMethodEventEP17QInputMethodEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(im)
    if (!std::strcmp(key, "_ZN10QQuickItem12focusInEventEP11QFocusEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem13focusOutEventEP11QFocusEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14mouseMoveEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem17mouseReleaseEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16mouseUngrabEventEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16touchUngrabEventEv")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10wheelEventEP11QWheelEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN10QQuickItem10touchEventEP11QTouchEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverEnterEventEP11QHoverEvent")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem14hoverMoveEventEP11QHoverEvent")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem15hoverLeaveEventEP11QHoverEvent")) {
      taken[27] = call;
      return true;
    }
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragEnterEventEP15QDragEnterEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem13dragMoveEventEP14QDragMoveEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem14dragLeaveEventEP15QDragLeaveEvent")) {
      taken[30] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
#if QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem9dropEventEP10QDropEvent")) {
      taken[31] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_draganddrop)
    if (!std::strcmp(key, "_ZN10QQuickItem21childMouseEventFilterEPS_P6QEvent")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem16releaseResourcesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN10QQuickItem12updatePolishEv")) {
      taken[34] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[36] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[37] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[38] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[39] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[40] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QSGNode *Qt3DRender::Scene3DItem::updatePaintNode(QSGNode *node,
  //      UpdatePaintNodeData *nodeData)
  QSGNode *updatePaintNode(
      QSGNode *node,
      QQuickItem::UpdatePaintNodeData *nodeData) override {
    if (taken[0]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall0 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall0>(taken[0]);
      void * given = call(this, node, nodeData, &handled);
      if (handled) return static_cast<QSGNode *>(given);
    }
    return Qt3DRender::Scene3DItem::updatePaintNode(node, nodeData);
  }

  //  void Qt3DRender::Scene3DItem::mousePressEvent(QMouseEvent *event)
  void mousePressEvent(QMouseEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall1 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall1>(taken[1]);
      call(this, event, &handled);
      if (handled) return;
    }
    Qt3DRender::Scene3DItem::mousePressEvent(event);
  }

  //  QRectF QQuickItem::boundingRect() const
  QRectF boundingRect() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall2 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall2>(taken[2]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::boundingRect();
  }

  //  QRectF QQuickItem::clipRect() const
  QRectF clipRect() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall3 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall3>(taken[3]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::clipRect();
  }

  //  bool QQuickItem::contains(const QPointF &point) const
  bool contains(const QPointF &point) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall4 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall4>(taken[4]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickItem::contains(point);
  }

#if QT_CONFIG(im)
  //  QVariant QQuickItem::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall5 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall5>(taken[5]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QQuickItem::inputMethodQuery(query);
  }
#endif  // QT_CONFIG(im)

  //  bool QQuickItem::isTextureProvider() const
  bool isTextureProvider() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall6 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall6>(taken[6]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItem::isTextureProvider();
  }

  //  QSGTextureProvider *QQuickItem::textureProvider() const
  QSGTextureProvider *textureProvider() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall7 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall7>(taken[7]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTextureProvider *>(given);
    }
    return QQuickItem::textureProvider();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QQuickItem::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall8 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall8>(taken[8]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QQuickItem::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QQuickItem::itemChange(ItemChange a0, const ItemChangeData &a1)
  void itemChange(
      QQuickItem::ItemChange a0,
      const QQuickItem::ItemChangeData &a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall9 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall9>(taken[9]);
      call(this, static_cast<int>(a0), &a1, &handled);
      if (handled) return;
    }
    QQuickItem::itemChange(a0, a1);
  }

  //  void QQuickItem::geometryChange(const QRectF &newGeometry, const
  //      QRectF &oldGeometry)
  void geometryChange(
      const QRectF &newGeometry,
      const QRectF &oldGeometry) override {
    if (taken[10]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall10 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall10>(taken[10]);
      call(this, &newGeometry, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickItem::geometryChange(newGeometry, oldGeometry);
  }

  //  void QQuickItem::classBegin()
  void classBegin() override {
    if (taken[11]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall11 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::classBegin();
  }

  //  void QQuickItem::componentComplete()
  void componentComplete() override {
    if (taken[12]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall12 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::componentComplete();
  }

  //  void QQuickItem::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall13 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyPressEvent(event);
  }

  //  void QQuickItem::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall14 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::keyReleaseEvent(event);
  }

#if QT_CONFIG(im)
  //  void QQuickItem::inputMethodEvent(QInputMethodEvent *a0)
  void inputMethodEvent(QInputMethodEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall15 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::inputMethodEvent(a0);
  }
#endif  // QT_CONFIG(im)

  //  void QQuickItem::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall16 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusInEvent(a0);
  }

  //  void QQuickItem::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall17 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::focusOutEvent(a0);
  }

  //  void QQuickItem::mouseMoveEvent(QMouseEvent *event)
  void mouseMoveEvent(QMouseEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall18 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseMoveEvent(event);
  }

  //  void QQuickItem::mouseReleaseEvent(QMouseEvent *event)
  void mouseReleaseEvent(QMouseEvent *event) override {
    if (taken[19]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall19 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall19>(taken[19]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseReleaseEvent(event);
  }

  //  void QQuickItem::mouseDoubleClickEvent(QMouseEvent *event)
  void mouseDoubleClickEvent(QMouseEvent *event) override {
    if (taken[20]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall20 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall20>(taken[20]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::mouseDoubleClickEvent(event);
  }

  //  void QQuickItem::mouseUngrabEvent()
  void mouseUngrabEvent() override {
    if (taken[21]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall21 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::mouseUngrabEvent();
  }

  //  void QQuickItem::touchUngrabEvent()
  void touchUngrabEvent() override {
    if (taken[22]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall22 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall22>(taken[22]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::touchUngrabEvent();
  }

#if QT_CONFIG(wheelevent)
  //  void QQuickItem::wheelEvent(QWheelEvent *event)
  void wheelEvent(QWheelEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall23 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::wheelEvent(event);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QQuickItem::touchEvent(QTouchEvent *event)
  void touchEvent(QTouchEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall24 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::touchEvent(event);
  }

  //  void QQuickItem::hoverEnterEvent(QHoverEvent *event)
  void hoverEnterEvent(QHoverEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall25 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverEnterEvent(event);
  }

  //  void QQuickItem::hoverMoveEvent(QHoverEvent *event)
  void hoverMoveEvent(QHoverEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall26 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverMoveEvent(event);
  }

  //  void QQuickItem::hoverLeaveEvent(QHoverEvent *event)
  void hoverLeaveEvent(QHoverEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall27 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QQuickItem::hoverLeaveEvent(event);
  }

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragEnterEvent(QDragEnterEvent *a0)
  void dragEnterEvent(QDragEnterEvent *a0) override {
    if (taken[28]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall28 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall28>(taken[28]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragEnterEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragMoveEvent(QDragMoveEvent *a0)
  void dragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[29]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall29 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall29>(taken[29]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragMoveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dragLeaveEvent(QDragLeaveEvent *a0)
  void dragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[30]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall30 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall30>(taken[30]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

#if QT_CONFIG(quick_draganddrop)
  //  void QQuickItem::dropEvent(QDropEvent *a0)
  void dropEvent(QDropEvent *a0) override {
    if (taken[31]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall31 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall31>(taken[31]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickItem::dropEvent(a0);
  }
#endif  // QT_CONFIG(quick_draganddrop)

  //  bool QQuickItem::childMouseEventFilter(QQuickItem *a0, QEvent *a1)
  bool childMouseEventFilter(QQuickItem *a0, QEvent *a1) override {
    if (taken[32]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall32 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall32>(taken[32]);
      bool given = call(this, a0, a1, &handled);
      if (handled) return given;
    }
    return QQuickItem::childMouseEventFilter(a0, a1);
  }

  //  void QQuickItem::releaseResources()
  void releaseResources() override {
    if (taken[33]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall33 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::releaseResources();
  }

  //  void QQuickItem::updatePolish()
  void updatePolish() override {
    if (taken[34]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall34 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall34>(taken[34]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItem::updatePolish();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall35 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall35>(taken[35]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[36]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall36 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall36>(taken[36]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[37]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall37 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall37>(taken[37]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[38]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall38 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall38>(taken[38]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[39]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall39 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall39>(taken[39]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[40]) {
      int handled = 0;
      CuteQt3DRender_Scene3DItemCall40 call = reinterpret_cast<CuteQt3DRender_Scene3DItemCall40>(taken[40]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::Scene3DItem::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender11Scene3DItem10metaObjectEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Scene3DItem::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender11Scene3DItem11qt_metacastEPKc(
    Qt3DRender::Scene3DItem *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Scene3DItem::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender11Scene3DItem11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Scene3DItem *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DRender::Scene3DItem::~Scene3DItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItemD1Ev(Qt3DRender::Scene3DItem *self) {
  delete self;
}

//  QStringList Qt3DRender::Scene3DItem::aspects() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender11Scene3DItem7aspectsEv(
    const Qt3DRender::Scene3DItem *self) {
  return new QList<QString>(self->aspects());
}

//  Qt3DCore::QEntity *Qt3DRender::Scene3DItem::entity() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK10Qt3DRender11Scene3DItem6entityEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->entity();
}

//  bool Qt3DRender::Scene3DItem::multisample() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender11Scene3DItem11multisampleEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->multisample();
}

//  void Qt3DRender::Scene3DItem::setItemAreaAndDevicePixelRatio(QSize area,
//      qreal devicePixelRatio)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem30setItemAreaAndDevicePixelRatioE5QSized(
    Qt3DRender::Scene3DItem *self,
    const QSize *area,
    qreal devicePixelRatio) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setItemAreaAndDevicePixelRatio(QSize,qreal)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setItemAreaAndDevicePixelRatio(QSize,qreal)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(area)),
      const_cast<void *>(static_cast<const void *>(&devicePixelRatio)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool Qt3DRender::Scene3DItem::isHoverEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender11Scene3DItem14isHoverEnabledEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->isHoverEnabled();
}

//  CameraAspectRatioMode Qt3DRender::Scene3DItem::cameraAspectRatioMode()
//      const
extern "C" Q_DECL_EXPORT
Qt3DRender::Scene3DItem::CameraAspectRatioMode ritual_ZNK10Qt3DRender11Scene3DItem21cameraAspectRatioModeEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->cameraAspectRatioMode();
}

//  CompositingMode Qt3DRender::Scene3DItem::compositingMode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Scene3DItem::CompositingMode ritual_ZNK10Qt3DRender11Scene3DItem15compositingModeEv(
    const Qt3DRender::Scene3DItem *self) {
  return self->compositingMode();
}

//  void Qt3DRender::Scene3DItem::setAspects(const QStringList &aspects)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem10setAspectsERK5QListI7QStringE(
    Qt3DRender::Scene3DItem *self,
    const QList<QString> *aspects) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setAspects(const QStringList &)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setAspects(const QStringList &)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(aspects)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::setEntity(Qt3DCore::QEntity *entity)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem9setEntityEPN8Qt3DCore7QEntityE(
    Qt3DRender::Scene3DItem *self,
    Qt3DCore::QEntity *entity) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setEntity(Qt3DCore::QEntity *)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setEntity(Qt3DCore::QEntity *)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&entity)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void
//      Qt3DRender::Scene3DItem::setCameraAspectRatioMode(CameraAspectRatioMo
//      de mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem24setCameraAspectRatioModeENS0_21CameraAspectRatioModeE(
    Qt3DRender::Scene3DItem *self,
    Qt3DRender::Scene3DItem::CameraAspectRatioMode mode) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setCameraAspectRatioMode(CameraAspectRatioMode)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setCameraAspectRatioMode(CameraAspectRatioMode)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&mode)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::setHoverEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem15setHoverEnabledEb(
    Qt3DRender::Scene3DItem *self,
    bool enabled) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setHoverEnabled(bool)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setHoverEnabled(bool)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&enabled)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::setCompositingMode(CompositingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem18setCompositingModeENS0_15CompositingModeE(
    Qt3DRender::Scene3DItem *self,
    Qt3DRender::Scene3DItem::CompositingMode mode) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "setCompositingMode(CompositingMode)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "setCompositingMode(CompositingMode)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&mode)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::aspectsChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem14aspectsChangedEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "aspectsChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "aspectsChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::entityChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem13entityChangedEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "entityChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "entityChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::multisampleChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem18multisampleChangedEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "multisampleChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "multisampleChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::cameraAspectRatioModeChanged(CameraAspectRa
//      tioMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem28cameraAspectRatioModeChangedENS0_21CameraAspectRatioModeE(
    Qt3DRender::Scene3DItem *self,
    Qt3DRender::Scene3DItem::CameraAspectRatioMode mode) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "cameraAspectRatioModeChanged(CameraAspectRatioMode)").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "cameraAspectRatioModeChanged(CameraAspectRatioMode)");
  void *arguments[] = {
      nullptr,
      const_cast<void *>(static_cast<const void *>(&mode)),
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::hoverEnabledChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem19hoverEnabledChangedEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "hoverEnabledChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "hoverEnabledChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::compositingModeChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem22compositingModeChangedEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "compositingModeChanged()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "compositingModeChanged()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::applyRootEntityChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem21applyRootEntityChangeEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "applyRootEntityChange()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "applyRootEntityChange()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void Qt3DRender::Scene3DItem::requestUpdate()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem13requestUpdateEv(
    Qt3DRender::Scene3DItem *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DItem")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "requestUpdate()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "requestUpdate()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool Qt3DRender::Scene3DItem::prepareQt3DFrame()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender11Scene3DItem16prepareQt3DFrameEv(
    Qt3DRender::Scene3DItem *self) {
  return self->prepareQt3DFrame();
}

//  QSGNode *Qt3DRender::Scene3DItem::updatePaintNode(QSGNode *node,
//      UpdatePaintNodeData *nodeData)
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN10Qt3DRender11Scene3DItem15updatePaintNodeEP7QSGNodePN10QQuickItem19UpdatePaintNodeDataE(
    Qt3DRender::Scene3DItem *self,
    QSGNode *node,
    QQuickItem::UpdatePaintNodeData *nodeData) {
  return self->updatePaintNode(node, nodeData);
}

//  void Qt3DRender::Scene3DItem::setWindowSurface(QObject *rootObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem16setWindowSurfaceEP7QObject(
    Qt3DRender::Scene3DItem *self,
    QObject *rootObject) {
  self->setWindowSurface(rootObject);
}

//  void Qt3DRender::Scene3DItem::updateCameraAspectRatio()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem23updateCameraAspectRatioEv(
    Qt3DRender::Scene3DItem *self) {
  self->updateCameraAspectRatio();
}

//  void Qt3DRender::Scene3DItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem15mousePressEventEP11QMouseEvent(
    Qt3DRender::Scene3DItem *self,
    QMouseEvent *event) {
  self->mousePressEvent(event);
}

//  bool Qt3DRender::Scene3DItem::needsRender(QRenderAspect *renderAspect)
extern "C" Q_DECL_EXPORT
bool ritual_ZN10Qt3DRender11Scene3DItem11needsRenderEPNS_13QRenderAspectE(
    Qt3DRender::Scene3DItem *self,
    Qt3DRender::QRenderAspect *renderAspect) {
  return self->needsRender(renderAspect);
}

//  void Qt3DRender::Scene3DItem::updateWindowSurface()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem19updateWindowSurfaceEv(
    Qt3DRender::Scene3DItem *self) {
  self->updateWindowSurface();
}

//  void Qt3DRender::Scene3DItem::applyAspects()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender11Scene3DItem12applyAspectsEv(
    Qt3DRender::Scene3DItem *self) {
  self->applyAspects();
}

//  a Python function taken by a CuteQt3DRender_Scene3DItem, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Scene3DItem(
    Qt3DRender::Scene3DItem *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Scene3DItem *>(self)->take(key, call);
}

//  void Qt3DRender::Scene3DItem::mousePressEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN10Qt3DRender11Scene3DItem15mousePressEventEP11QMouseEvent(
    Qt3DRender::Scene3DItem *self,
    QMouseEvent *event) {
  self->Qt3DRender::Scene3DItem::mousePressEvent(event);
}
