//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DExtras/qforwardrenderer.h, Qt 6.12.0. Changes made here are lost.
#include <Qt3DExtras/qforwardrenderer.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A Qt3DExtras::QForwardRenderer that Python can take functions over in. Every Qt3DExtras::QForwardRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QForwardRendererCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQt3DExtras_QForwardRendererCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QForwardRendererCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QForwardRendererCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QForwardRendererCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QForwardRendererCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQt3DExtras_QForwardRendererCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQt3DExtras_QForwardRenderer : public Qt3DExtras::QForwardRenderer {
public:
  using Qt3DExtras::QForwardRenderer::QForwardRenderer;
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
      CuteQt3DExtras_QForwardRendererCall0 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall0>(taken[0]);
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
      CuteQt3DExtras_QForwardRendererCall1 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall1>(taken[1]);
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
      CuteQt3DExtras_QForwardRendererCall2 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall2>(taken[2]);
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
      CuteQt3DExtras_QForwardRendererCall3 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall3>(taken[3]);
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
      CuteQt3DExtras_QForwardRendererCall4 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall4>(taken[4]);
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
      CuteQt3DExtras_QForwardRendererCall5 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall5>(taken[5]);
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
      CuteQt3DExtras_QForwardRendererCall6 call = reinterpret_cast<CuteQt3DExtras_QForwardRendererCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *Qt3DExtras::QForwardRenderer::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10Qt3DExtras16QForwardRenderer10metaObjectEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->metaObject();
}

//  void *Qt3DExtras::QForwardRenderer::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN10Qt3DExtras16QForwardRenderer11qt_metacastEPKc(
    Qt3DExtras::QForwardRenderer *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int Qt3DExtras::QForwardRenderer::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN10Qt3DExtras16QForwardRenderer11qt_metacallEN11QMetaObject4CallEiPPv(
    Qt3DExtras::QForwardRenderer *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString Qt3DExtras::QForwardRenderer::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10Qt3DExtras16QForwardRenderer2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(Qt3DExtras::QForwardRenderer::tr(s, c, n));
}

//  Qt3DExtras::QForwardRenderer::QForwardRenderer(Qt3DCore::QNode *parent)
extern "C" Q_DECL_EXPORT
Qt3DExtras::QForwardRenderer *ritual_ZN10Qt3DExtras16QForwardRendererC1EPN8Qt3DCore5QNodeE(
    Qt3DCore::QNode *parent) {
  return new CuteQt3DExtras_QForwardRenderer(parent);
}

//  Qt3DExtras::QForwardRenderer::~QForwardRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRendererD1Ev(
    Qt3DExtras::QForwardRenderer *self) {
  delete self;
}

//  QRectF Qt3DExtras::QForwardRenderer::viewportRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK10Qt3DExtras16QForwardRenderer12viewportRectEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return new QRectF(self->viewportRect());
}

//  QColor Qt3DExtras::QForwardRenderer::clearColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK10Qt3DExtras16QForwardRenderer10clearColorEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return new QColor(self->clearColor());
}

//  Qt3DRender::QClearBuffers::BufferType
//      Qt3DExtras::QForwardRenderer::buffersToClear() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QClearBuffers::BufferType ritual_ZNK10Qt3DExtras16QForwardRenderer14buffersToClearEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->buffersToClear();
}

//  Qt3DCore::QEntity *Qt3DExtras::QForwardRenderer::camera() const
extern "C" Q_DECL_EXPORT
Qt3DCore::QEntity *ritual_ZNK10Qt3DExtras16QForwardRenderer6cameraEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->camera();
}

//  QObject *Qt3DExtras::QForwardRenderer::surface() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK10Qt3DExtras16QForwardRenderer7surfaceEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->surface();
}

//  QSize Qt3DExtras::QForwardRenderer::externalRenderTargetSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK10Qt3DExtras16QForwardRenderer24externalRenderTargetSizeEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return new QSize(self->externalRenderTargetSize());
}

//  bool Qt3DExtras::QForwardRenderer::isFrustumCullingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras16QForwardRenderer23isFrustumCullingEnabledEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->isFrustumCullingEnabled();
}

//  float Qt3DExtras::QForwardRenderer::gamma() const
extern "C" Q_DECL_EXPORT
float ritual_ZNK10Qt3DExtras16QForwardRenderer5gammaEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->gamma();
}

//  bool Qt3DExtras::QForwardRenderer::showDebugOverlay() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DExtras16QForwardRenderer16showDebugOverlayEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->showDebugOverlay();
}

//  void Qt3DExtras::QForwardRenderer::setViewportRect(const QRectF
//      &viewportRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer15setViewportRectERK6QRectF(
    Qt3DExtras::QForwardRenderer *self,
    const QRectF *viewportRect) {
  self->setViewportRect(*viewportRect);
}

//  void Qt3DExtras::QForwardRenderer::setClearColor(const QColor
//      &clearColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer13setClearColorERK6QColor(
    Qt3DExtras::QForwardRenderer *self,
    const QColor *clearColor) {
  self->setClearColor(*clearColor);
}

//  void Qt3DExtras::QForwardRenderer::setBuffersToClear(Qt3DRender::QClearBu
//      ffers::BufferType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer17setBuffersToClearEN10Qt3DRender13QClearBuffers10BufferTypeE(
    Qt3DExtras::QForwardRenderer *self,
    Qt3DRender::QClearBuffers::BufferType a0) {
  self->setBuffersToClear(a0);
}

//  void Qt3DExtras::QForwardRenderer::setCamera(Qt3DCore::QEntity *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer9setCameraEPN8Qt3DCore7QEntityE(
    Qt3DExtras::QForwardRenderer *self,
    Qt3DCore::QEntity *camera) {
  self->setCamera(camera);
}

//  void Qt3DExtras::QForwardRenderer::setSurface(QObject *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer10setSurfaceEP7QObject(
    Qt3DExtras::QForwardRenderer *self,
    QObject *surface) {
  self->setSurface(surface);
}

//  void Qt3DExtras::QForwardRenderer::setExternalRenderTargetSize(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer27setExternalRenderTargetSizeERK5QSize(
    Qt3DExtras::QForwardRenderer *self,
    const QSize *size) {
  self->setExternalRenderTargetSize(*size);
}

//  void Qt3DExtras::QForwardRenderer::setFrustumCullingEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer24setFrustumCullingEnabledEb(
    Qt3DExtras::QForwardRenderer *self,
    bool enabled) {
  self->setFrustumCullingEnabled(enabled);
}

//  void Qt3DExtras::QForwardRenderer::setGamma(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer8setGammaEf(
    Qt3DExtras::QForwardRenderer *self,
    float gamma) {
  self->setGamma(gamma);
}

//  void Qt3DExtras::QForwardRenderer::setShowDebugOverlay(bool
//      showDebugOverlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer19setShowDebugOverlayEb(
    Qt3DExtras::QForwardRenderer *self,
    bool showDebugOverlay) {
  self->setShowDebugOverlay(showDebugOverlay);
}

//  void Qt3DExtras::QForwardRenderer::viewportRectChanged(const QRectF
//      &viewportRect)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer19viewportRectChangedERK6QRectF(
    Qt3DExtras::QForwardRenderer *self,
    const QRectF *viewportRect) {
  self->viewportRectChanged(*viewportRect);
}

//  void Qt3DExtras::QForwardRenderer::clearColorChanged(const QColor
//      &clearColor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer17clearColorChangedERK6QColor(
    Qt3DExtras::QForwardRenderer *self,
    const QColor *clearColor) {
  self->clearColorChanged(*clearColor);
}

//  void Qt3DExtras::QForwardRenderer::buffersToClearChanged(Qt3DRender::QCle
//      arBuffers::BufferType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer21buffersToClearChangedEN10Qt3DRender13QClearBuffers10BufferTypeE(
    Qt3DExtras::QForwardRenderer *self,
    Qt3DRender::QClearBuffers::BufferType a0) {
  self->buffersToClearChanged(a0);
}

//  void Qt3DExtras::QForwardRenderer::cameraChanged(Qt3DCore::QEntity
//      *camera)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer13cameraChangedEPN8Qt3DCore7QEntityE(
    Qt3DExtras::QForwardRenderer *self,
    Qt3DCore::QEntity *camera) {
  self->cameraChanged(camera);
}

//  void Qt3DExtras::QForwardRenderer::surfaceChanged(QObject *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer14surfaceChangedEP7QObject(
    Qt3DExtras::QForwardRenderer *self,
    QObject *surface) {
  self->surfaceChanged(surface);
}

//  void Qt3DExtras::QForwardRenderer::externalRenderTargetSizeChanged(const
//      QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer31externalRenderTargetSizeChangedERK5QSize(
    Qt3DExtras::QForwardRenderer *self,
    const QSize *size) {
  self->externalRenderTargetSizeChanged(*size);
}

//  void Qt3DExtras::QForwardRenderer::frustumCullingEnabledChanged(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer28frustumCullingEnabledChangedEb(
    Qt3DExtras::QForwardRenderer *self,
    bool enabled) {
  self->frustumCullingEnabledChanged(enabled);
}

//  void Qt3DExtras::QForwardRenderer::gammaChanged(float gamma)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer12gammaChangedEf(
    Qt3DExtras::QForwardRenderer *self,
    float gamma) {
  self->gammaChanged(gamma);
}

//  void Qt3DExtras::QForwardRenderer::showDebugOverlayChanged(bool
//      showDebugOverlay)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DExtras16QForwardRenderer23showDebugOverlayChangedEb(
    Qt3DExtras::QForwardRenderer *self,
    bool showDebugOverlay) {
  self->showDebugOverlayChanged(showDebugOverlay);
}

//  QForwardRendererPrivate *Qt3DExtras::QForwardRenderer::d_func()
extern "C" Q_DECL_EXPORT
Qt3DExtras::QForwardRendererPrivate *ritual_ZN10Qt3DExtras16QForwardRenderer6d_funcEv(
    Qt3DExtras::QForwardRenderer *self) {
  return self->d_func();
}

//  const QForwardRendererPrivate *Qt3DExtras::QForwardRenderer::d_func()
//      const
extern "C" Q_DECL_EXPORT
const Qt3DExtras::QForwardRendererPrivate *ritual_ZNK10Qt3DExtras16QForwardRenderer6d_funcEv(
    const Qt3DExtras::QForwardRenderer *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQt3DExtras_QForwardRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_Qt3DExtras_QForwardRenderer(
    Qt3DExtras::QForwardRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQt3DExtras_QForwardRenderer *>(self)->take(key, call);
}
