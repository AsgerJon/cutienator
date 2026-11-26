//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick3D/6.12.0/QtQuick3D/private/qtquick3dglobal_p.h>
#include <QtQuick3D/QtQuick3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/6.12.0/QtQuick3D/private/qquick3dscenerenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick3D/private/qquick3dcubemaptexture_p.h>
#include <QtQuick3D/private/qquick3dscenerenderer_p.h>
#include <QtQuick3D/private/qquick3dsceneenvironment_p.h>
#include <QtQuick3D/private/qquick3dobject_p.h>
#include <QtQuick3D/private/qquick3dnode_p.h>
#include <QtQuick3D/private/qquick3dscenemanager_p.h>
#include <QtQuick3D/private/qquick3dtexture_p.h>
#include <QtQuick3D/private/qquick3dcamera_p.h>
#include <QtQuick3D/private/qquick3dpickresult_p.h>
#include <QtQuick3D/private/qquick3dmodel_p.h>
#include <QtQuick3D/private/qquick3drenderstats_p.h>
#include <QtQuick3D/private/qquick3ddebugsettings_p.h>
#include <QtQuick3D/private/qquick3dskymaterial_p.h>
#include <QtQuick3DUtils/private/qquick3dprofiler_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendererutil_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderer_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#include <QtQuick/private/qsgdefaultrendercontext_p.h>
#include <QtQuick/private/qsgtexture_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#include <QtQuick/private/qsgrendernode_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendereffect_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhieffectsystem_p.h>
#include <QtQuick3DRuntimeRender/private/qssglayerrenderdata_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhiquadrenderer_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrhicontext_p.h>
#include <QtQuick3DRuntimeRender/private/qssgcputonemapper_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderroot_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderskymaterial_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrenderuserpass_p.h>
#include <QtQuick3DRuntimeRender/private/qssgrendercommands_p.h>
#include <QtQuick3DUtils/private/qssgutils_p.h>
#include <QtQuick3DUtils/private/qssgassert_p.h>
#include <QtCore/QObject>
#include <QtCore/qqueue.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 143, as local:qquick3dscenerenderer.cpp:requestFullUpdate
static void requestFullUpdate(QQuickWindow *window)
{
    if (QThread::currentThread() == QCoreApplication::instance()->thread())
        window->update();
    else
        QCoreApplication::postEvent(window, new QEvent(QEvent::Type(QQuickWindowPrivate::FullUpdateRequest)));
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1691, as local:qquick3dscenerenderer.cpp:queryMainRenderPassDescriptorAndCommandBuffer
namespace {
inline void queryMainRenderPassDescriptorAndCommandBuffer(QQuickWindow *window, QSSGRhiContext *rhiCtx)
{
    if (rhiCtx->isValid()) {
        QSSGRhiContextPrivate *rhiCtxD = QSSGRhiContextPrivate::get(rhiCtx);
        // Query from the rif because that is available in the sync
        // phase (updatePaintNode) already.  QSGDefaultRenderContext's
        // copies of the rp and cb are not there until the render
        // phase of the scenegraph.
        int sampleCount = 1;
        int viewCount = 1;
        QRhiSwapChain *swapchain = window->swapChain();
        if (swapchain) {
            rhiCtxD->setMainRenderPassDescriptor(swapchain->renderPassDescriptor());
            rhiCtxD->setCommandBuffer(swapchain->currentFrameCommandBuffer());
            rhiCtxD->setRenderTarget(swapchain->currentFrameRenderTarget());
            sampleCount = swapchain->sampleCount();
        } else {
            QSGRendererInterface *rif = window->rendererInterface();
            // no swapchain when using a QQuickRenderControl (redirecting to a texture etc.)
            QRhiCommandBuffer *cb = static_cast<QRhiCommandBuffer *>(
                rif->getResource(window, QSGRendererInterface::RhiRedirectCommandBuffer));
            QRhiTextureRenderTarget *rt = static_cast<QRhiTextureRenderTarget *>(
                rif->getResource(window, QSGRendererInterface::RhiRedirectRenderTarget));
            if (cb && rt) {
                rhiCtxD->setMainRenderPassDescriptor(rt->renderPassDescriptor());
                rhiCtxD->setCommandBuffer(cb);
                rhiCtxD->setRenderTarget(rt);
                const auto descr = rt->description();
                const QRhiColorAttachment *color0 = descr.cbeginColorAttachments();
                if (color0 && color0->texture()) {
                    sampleCount = color0->texture()->sampleCount();
                    if (rt->resourceType() == QRhiResource::TextureRenderTarget) {
                        const QRhiTextureRenderTargetDescription desc = static_cast<QRhiTextureRenderTarget *>(rt)->description();
                        for (auto it = desc.cbeginColorAttachments(), end = desc.cendColorAttachments(); it != end; ++it) {
                            if (it->multiViewCount() >= 2) {
                                viewCount = it->multiViewCount();
                                break;
                            }
                        }
                    }
                }
            } else {
                qWarning("Neither swapchain nor redirected command buffer and render target are available.");
            }
        }

        // MSAA is out of our control on this path: it is up to the
        // QQuickWindow and the scenegraph to set up the swapchain based on the
        // QSurfaceFormat's samples(). The only thing we need to do here is to
        // pass the sample count to the renderer because it is needed when
        // creating graphics pipelines.
        rhiCtxD->setMainPassSampleCount(sampleCount);

        // The "direct renderer", i.e. the Underlay and Overlay modes are the
        // only ones that support multiview rendering. This becomes active when
        // the QQuickWindow is redirected into a texture array, typically with
        // an array size of 2 (2 views, for the left and right eye). Otherwise,
        // when targeting a window or redirected to a 2D texture, this is not
        // applicable and the view count is 1.
        rhiCtxD->setMainPassViewCount(viewCount);
    }
}
}  // namespace

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 206, as _ZN21QQuick3DSceneRendererD1Ev
inline QQuick3DSceneRenderer::~QQuick3DSceneRenderer()
{
    const auto &rhiCtx = m_sgContext->rhiContext();
    auto *rhi = rhiCtx->rhi();
    rhi->finish(); // finish active readbacks
    QSSGRhiContextStats::get(*rhiCtx).cleanupLayerInfo(m_layer);
    m_sgContext->bufferManager()->releaseResourcesForLayer(m_layer);

    if (m_layer) {
        // The scene root is created by the scene manager and released by the normal cleanup of
        // scene nodes. Since we delete the layer at a later point, detach the scene root from the
        // layer now. QSSGRenderNode::removeChild() ignores a node that is no longer a child of
        // the layer, so this is safe even if the scene manager has already cleaned up (and
        // unlinked) the scene root.
        if (m_sceneRootNode)
            removeNodeFromLayer(m_sceneRootNode);
        m_sceneRootNode = nullptr;

        // There might be nodes queued for cleanup that still reference the layer,
        // so we schedule the layer for cleanup so that it is deleted after the nodes
        // have been cleaned up.
        if (winAttacment)
            winAttacment->queueForCleanup(m_layer);
        else
            delete m_layer;
        m_layer = nullptr;
    }

    delete m_texture;

    releaseAaDependentRhiResources();
    delete m_effectSystem;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1847, as _ZN24QQuick3DSGDirectRendererD1Ev
inline QQuick3DSGDirectRenderer::~QQuick3DSGDirectRenderer()
{
    delete m_renderer;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1852, as _ZN24QQuick3DSGDirectRenderer11setViewportERK6QRectF
inline void QQuick3DSGDirectRenderer::setViewport(const QRectF &viewport)
{
    m_viewport = viewport;
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1865, as _ZN24QQuick3DSGDirectRenderer13requestRenderEv
inline void QQuick3DSGDirectRenderer::requestRender()
{
    renderPending = true;
    requestFullUpdate(m_window);
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1857, as _ZN24QQuick3DSGDirectRenderer13setVisibilityEb
inline void QQuick3DSGDirectRenderer::setVisibility(bool visible)
{
    if (m_isVisible == visible)
        return;
    m_isVisible = visible;
    m_window->update();
}

//  from ../qtquick3d/src/quick3d/qquick3dscenerenderer.cpp, line 1871, as _ZN24QQuick3DSGDirectRenderer14preSynchronizeEv
inline void QQuick3DSGDirectRenderer::preSynchronize()
{
    // This is called from the QQuick3DViewport's updatePaintNode(), before
    // QQuick3DSceneRenderer::synchronize(). It is essential to query things
    // such as the view count already here, so that synchronize() can rely on
    // mainPassViewCount() for instance. prepare() is too late as that is only
    // called on beforeRendering (so after the scenegraph sync phase).
    if (m_renderer->m_sgContext->rhiContext()->isValid())
        queryMainRenderPassDescriptorAndCommandBuffer(m_window, m_renderer->m_sgContext->rhiContext().get());
}
//  -----------------------------------------------------------------------

//  A QQuick3DSGDirectRenderer that Python can take functions over in. Every QQuick3DSGDirectRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSGDirectRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQQuick3DSGDirectRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSGDirectRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSGDirectRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSGDirectRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSGDirectRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQQuick3DSGDirectRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQQuick3DSGDirectRenderer : public QQuick3DSGDirectRenderer {
public:
  using QQuick3DSGDirectRenderer::QQuick3DSGDirectRenderer;
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
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuick3DSGDirectRendererCall0 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuick3DSGDirectRendererCall1 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall1>(taken[1]);
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
      CuteQQuick3DSGDirectRendererCall2 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall2>(taken[2]);
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
      CuteQQuick3DSGDirectRendererCall3 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall3>(taken[3]);
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
      CuteQQuick3DSGDirectRendererCall4 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall4>(taken[4]);
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
      CuteQQuick3DSGDirectRendererCall5 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall5>(taken[5]);
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
      CuteQQuick3DSGDirectRendererCall6 call = reinterpret_cast<CuteQQuick3DSGDirectRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QQuick3DSGDirectRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK24QQuick3DSGDirectRenderer10metaObjectEv(
    const QQuick3DSGDirectRenderer *self) {
  return self->metaObject();
}

//  void *QQuick3DSGDirectRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN24QQuick3DSGDirectRenderer11qt_metacastEPKc(
    QQuick3DSGDirectRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QQuick3DSGDirectRenderer::qt_metacall(QMetaObject::Call a0, int a1,
//      void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN24QQuick3DSGDirectRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    QQuick3DSGDirectRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QQuick3DSGDirectRenderer::~QQuick3DSGDirectRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRendererD1Ev(
    QQuick3DSGDirectRenderer *self) {
  delete self;
}

//  QQuick3DSceneRenderer *QQuick3DSGDirectRenderer::renderer()
extern "C" Q_DECL_EXPORT
QQuick3DSceneRenderer *ritual_ZN24QQuick3DSGDirectRenderer8rendererEv(
    QQuick3DSGDirectRenderer *self) {
  return self->renderer();
}

//  void QQuick3DSGDirectRenderer::setViewport(const QRectF &viewport)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer11setViewportERK6QRectF(
    QQuick3DSGDirectRenderer *self,
    const QRectF *viewport) {
  self->setViewport(*viewport);
}

//  void QQuick3DSGDirectRenderer::requestRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer13requestRenderEv(
    QQuick3DSGDirectRenderer *self) {
  self->requestRender();
}

//  void QQuick3DSGDirectRenderer::setVisibility(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer13setVisibilityEb(
    QQuick3DSGDirectRenderer *self,
    bool visible) {
  self->setVisibility(visible);
}

//  void QQuick3DSGDirectRenderer::preSynchronize()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer14preSynchronizeEv(
    QQuick3DSGDirectRenderer *self) {
  self->preSynchronize();
}

//  void QQuick3DSGDirectRenderer::prepare()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer7prepareEv(
    QQuick3DSGDirectRenderer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSGDirectRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "prepare()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "prepare()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  void QQuick3DSGDirectRenderer::render()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQuick3DSGDirectRenderer6renderEv(
    QQuick3DSGDirectRenderer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QQuick3DSGDirectRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "render()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "render()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQQuick3DSGDirectRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuick3DSGDirectRenderer(
    QQuick3DSGDirectRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuick3DSGDirectRenderer *>(self)->take(key, call);
}
