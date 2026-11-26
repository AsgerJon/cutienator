//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3drenderer_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <Qt3DQuickScene3D/Qt3DQuickScene3D>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/6.12.0/Qt3DQuickScene3D/private/scene3drenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DQuickScene3D/private/scene3drenderer_p.h>
#include <Qt3DCore/qaspectengine.h>
#include <Qt3DRender/qrenderaspect.h>
#include <QtCore/qthread.h>
#include <QtGui/qopenglcontext.h>
#include <qopenglframebufferobject.h>
#include <QtQuick/qquickwindow.h>
#include <QtGui/rhi/qrhi.h>
#include <Qt3DRender/private/qrenderaspect_p.h>
#include <Qt3DRender/private/abstractrenderer_p.h>
#include <Qt3DCore/private/qaspectengine_p.h>
#include <Qt3DCore/private/qaspectmanager_p.h>
#include <Qt3DCore/private/qchangearbiter_p.h>
#include <Qt3DCore/private/qservicelocator_p.h>
#include <Qt3DQuickScene3D/private/scene3ditem_p.h>
#include <Qt3DQuickScene3D/private/scene3dlogging_p.h>
#include <Qt3DQuickScene3D/private/scene3dsgnode_p.h>
#include <QtQuick/private/qquickwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 594, as _ZN10Qt3DRender15Scene3DRenderer13QuickRendererC2Ev
namespace Qt3DRender {
inline Scene3DRenderer::QuickRenderer::QuickRenderer() {}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 171, as _ZN10Qt3DRender15Scene3DRenderer8shutdownEv
namespace Qt3DRender {
inline void Scene3DRenderer::shutdown()
{
    if (!m_needsShutdown)
        return;
    m_needsShutdown = false;

    m_quickRenderer->shutdown(this);
    delete m_quickRenderer;
    m_quickRenderer = nullptr;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 154, as _ZN10Qt3DRender15Scene3DRendererD1Ev
namespace Qt3DRender {
inline Scene3DRenderer::~Scene3DRenderer()
{
    qCDebug(Scene3D) << Q_FUNC_INFO << QThread::currentThread();
    shutdown();
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 160, as _ZNK10Qt3DRender15Scene3DRenderer6sgNodeEv
namespace Qt3DRender {
inline Scene3DSGNode *Scene3DRenderer::sgNode() const
{
    return m_node;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 188, as _ZN10Qt3DRender15Scene3DRenderer11allowRenderEv
namespace Qt3DRender {
inline void Scene3DRenderer::allowRender()
{
    m_allowRendering.release(1);
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 193, as _ZN10Qt3DRender15Scene3DRenderer18setCompositingModeENS_11Scene3DItem15CompositingModeE
namespace Qt3DRender {
inline void Scene3DRenderer::setCompositingMode(Scene3DItem::CompositingMode mode)
{
    m_compositingMode = mode;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 198, as _ZN10Qt3DRender15Scene3DRenderer12setSkipFrameEb
namespace Qt3DRender {
inline void Scene3DRenderer::setSkipFrame(bool skip)
{
    m_skipFrame = skip;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 203, as _ZN10Qt3DRender15Scene3DRenderer14setMultisampleEb
namespace Qt3DRender {
inline void Scene3DRenderer::setMultisample(bool multisample)
{
    m_multisample = multisample;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 208, as _ZN10Qt3DRender15Scene3DRenderer15setBoundingSizeERK5QSize
namespace Qt3DRender {
inline void Scene3DRenderer::setBoundingSize(const QSize &size)
{
    m_boundingRectSize = size;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 165, as _ZNK10Qt3DRender15Scene3DRenderer5isYUpEv
namespace Qt3DRender {
inline bool Scene3DRenderer::isYUp() const
{
    return m_quickRenderer ? m_quickRenderer->isYUp() : true;
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 183, as _ZN10Qt3DRender15Scene3DRenderer17beforeSynchronizeEv
namespace Qt3DRender {
inline void Scene3DRenderer::beforeSynchronize()
{
    m_quickRenderer->beforeSynchronize(this);
}
}  // namespace Qt3DRender

//  from ../qt3d/src/quick3d/quick3dscene3d/scene3drenderer.cpp, line 136, as _ZN10Qt3DRender15Scene3DRenderer9setWindowEP12QQuickWindow
namespace Qt3DRender {
inline void Scene3DRenderer::setWindow(QQuickWindow *window)
{
    if (window == m_window)
        return;

    QObject::disconnect(m_window);
    m_window = window;

    if (m_window) {
        QObject::connect(m_window, &QQuickWindow::beforeRendering, this,
                         [this] () { m_quickRenderer->beforeRendering(this); }, Qt::DirectConnection);
        QObject::connect(m_window, &QQuickWindow::beforeRenderPassRecording, this,
                         [this] () { m_quickRenderer->beforeRenderPassRecording(this); }, Qt::DirectConnection);
    } else {
        shutdown();
    }
}
}  // namespace Qt3DRender
//  -----------------------------------------------------------------------

//  A Qt3DRender::Scene3DRenderer that Python can take functions over in. Every Qt3DRender::Scene3DRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Scene3DRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DRender_Scene3DRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DRender_Scene3DRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DRender_Scene3DRenderer : public Qt3DRender::Scene3DRenderer {
public:
  using Qt3DRender::Scene3DRenderer::Scene3DRenderer;
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
      CuteQt3DRender_Scene3DRendererCall0 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall0>(taken[0]);
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
      CuteQt3DRender_Scene3DRendererCall1 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall1>(taken[1]);
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
      CuteQt3DRender_Scene3DRendererCall2 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall2>(taken[2]);
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
      CuteQt3DRender_Scene3DRendererCall3 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall3>(taken[3]);
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
      CuteQt3DRender_Scene3DRendererCall4 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall4>(taken[4]);
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
      CuteQt3DRender_Scene3DRendererCall5 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall5>(taken[5]);
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
      CuteQt3DRender_Scene3DRendererCall6 call = reinterpret_cast<CuteQt3DRender_Scene3DRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DRender::Scene3DRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DRender15Scene3DRenderer10metaObjectEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->metaObject();
}

//  void *Qt3DRender::Scene3DRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DRender15Scene3DRenderer11qt_metacastEPKc(
    Qt3DRender::Scene3DRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DRender::Scene3DRenderer::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DRender15Scene3DRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DRender::Scene3DRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  Qt3DRender::Scene3DRenderer::~Scene3DRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRendererD1Ev(
    Qt3DRender::Scene3DRenderer *self) {
  delete self;
}

//  Scene3DSGNode *Qt3DRender::Scene3DRenderer::sgNode() const
extern "C" Q_DECL_EXPORT
Qt3DRender::Scene3DSGNode *ritual_ZNK10Qt3DRender15Scene3DRenderer6sgNodeEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->sgNode();
}

//  void Qt3DRender::Scene3DRenderer::allowRender()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer11allowRenderEv(
    Qt3DRender::Scene3DRenderer *self) {
  self->allowRender();
}

//  void Qt3DRender::Scene3DRenderer::setCompositingMode(Scene3DItem::Composi
//      tingMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer18setCompositingModeENS_11Scene3DItem15CompositingModeE(
    Qt3DRender::Scene3DRenderer *self,
    Qt3DRender::Scene3DItem::CompositingMode mode) {
  self->setCompositingMode(mode);
}

//  void Qt3DRender::Scene3DRenderer::setSkipFrame(bool skip)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer12setSkipFrameEb(
    Qt3DRender::Scene3DRenderer *self,
    bool skip) {
  self->setSkipFrame(skip);
}

//  void Qt3DRender::Scene3DRenderer::setMultisample(bool multisample)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer14setMultisampleEb(
    Qt3DRender::Scene3DRenderer *self,
    bool multisample) {
  self->setMultisample(multisample);
}

//  void Qt3DRender::Scene3DRenderer::setBoundingSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer15setBoundingSizeERK5QSize(
    Qt3DRender::Scene3DRenderer *self,
    const QSize *size) {
  self->setBoundingSize(*size);
}

//  bool Qt3DRender::Scene3DRenderer::multisample() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender15Scene3DRenderer11multisampleEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->multisample();
}

//  QSize Qt3DRender::Scene3DRenderer::boundingSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DRender15Scene3DRenderer12boundingSizeEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return new QSize(self->boundingSize());
}

//  bool Qt3DRender::Scene3DRenderer::isYUp() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender15Scene3DRenderer5isYUpEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->isYUp();
}

//  void Qt3DRender::Scene3DRenderer::beforeSynchronize()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer17beforeSynchronizeEv(
    Qt3DRender::Scene3DRenderer *self) {
  self->beforeSynchronize();
}

//  void Qt3DRender::Scene3DRenderer::setWindow(QQuickWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer9setWindowEP12QQuickWindow(
    Qt3DRender::Scene3DRenderer *self,
    QQuickWindow *window) {
  self->setWindow(window);
}

//  bool Qt3DRender::Scene3DRenderer::hasShutdown() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender15Scene3DRenderer11hasShutdownEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->hasShutdown();
}

//  QRenderAspect *Qt3DRender::Scene3DRenderer::renderAspect() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QRenderAspect *ritual_ZNK10Qt3DRender15Scene3DRenderer12renderAspectEv(
    const Qt3DRender::Scene3DRenderer *self) {
  return self->renderAspect();
}

//  void Qt3DRender::Scene3DRenderer::shutdown()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender15Scene3DRenderer8shutdownEv(
    Qt3DRender::Scene3DRenderer *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "Qt3DRender::Scene3DRenderer")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "shutdown()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "shutdown()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  a Python function taken by a CuteQt3DRender_Scene3DRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DRender_Scene3DRenderer(
    Qt3DRender::Scene3DRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DRender_Scene3DRenderer *>(self)->take(key, call);
}
