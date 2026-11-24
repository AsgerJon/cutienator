//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qquickrhiitem.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qquickrhiitem.h>
#include <cstring>

//  A QQuickRhiItemRenderer that Python can take functions over in. Every QQuickRhiItemRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRhiItemRendererCall0)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQQuickRhiItemRendererCall1)(const void *, QQuickRhiItem *, int *);
typedef void (*CuteQQuickRhiItemRendererCall2)(const void *, QRhiCommandBuffer *, int *);
class CuteQQuickRhiItemRenderer : public QQuickRhiItemRenderer {
public:
  using QQuickRhiItemRenderer::QQuickRhiItemRenderer;
  void *taken[3] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer10initializeEP17QRhiCommandBuffer")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer11synchronizeEP13QQuickRhiItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer6renderEP17QRhiCommandBuffer")) {
      taken[2] = call;
      return true;
    }
    return false;
  }

  //  void QQuickRhiItemRenderer::initialize(QRhiCommandBuffer *cb)
  void initialize(QRhiCommandBuffer *cb) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRhiItemRendererCall0 call = reinterpret_cast<CuteQQuickRhiItemRendererCall0>(taken[0]);
      call(this, cb, &handled);
      if (handled) return;
    }
  }

  //  void QQuickRhiItemRenderer::synchronize(QQuickRhiItem *item)
  void synchronize(QQuickRhiItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRhiItemRendererCall1 call = reinterpret_cast<CuteQQuickRhiItemRendererCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
  }

  //  void QQuickRhiItemRenderer::render(QRhiCommandBuffer *cb)
  void render(QRhiCommandBuffer *cb) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRhiItemRendererCall2 call = reinterpret_cast<CuteQQuickRhiItemRendererCall2>(taken[2]);
      call(this, cb, &handled);
      if (handled) return;
    }
  }
};

//  QQuickRhiItemRenderer::~QQuickRhiItemRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRhiItemRendererD1Ev(QQuickRhiItemRenderer *self) {
  delete self;
}

//  void QQuickRhiItemRenderer::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRhiItemRenderer10initializeEP17QRhiCommandBuffer(
    QQuickRhiItemRenderer *self,
    QRhiCommandBuffer *cb) {
  self->initialize(cb);
}

//  void QQuickRhiItemRenderer::synchronize(QQuickRhiItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRhiItemRenderer11synchronizeEP13QQuickRhiItem(
    QQuickRhiItemRenderer *self,
    QQuickRhiItem *item) {
  self->synchronize(item);
}

//  void QQuickRhiItemRenderer::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRhiItemRenderer6renderEP17QRhiCommandBuffer(
    QQuickRhiItemRenderer *self,
    QRhiCommandBuffer *cb) {
  self->render(cb);
}

//  void QQuickRhiItemRenderer::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRhiItemRenderer6updateEv(QQuickRhiItemRenderer *self) {
  self->update();
}

//  QRhi *QQuickRhiItemRenderer::rhi() const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK21QQuickRhiItemRenderer3rhiEv(
    const QQuickRhiItemRenderer *self) {
  return self->rhi();
}

//  QRhiTexture *QQuickRhiItemRenderer::colorTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QQuickRhiItemRenderer12colorTextureEv(
    const QQuickRhiItemRenderer *self) {
  return self->colorTexture();
}

//  QRhiRenderBuffer *QQuickRhiItemRenderer::msaaColorBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK21QQuickRhiItemRenderer15msaaColorBufferEv(
    const QQuickRhiItemRenderer *self) {
  return self->msaaColorBuffer();
}

//  QRhiTexture *QQuickRhiItemRenderer::resolveTexture() const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QQuickRhiItemRenderer14resolveTextureEv(
    const QQuickRhiItemRenderer *self) {
  return self->resolveTexture();
}

//  QRhiRenderBuffer *QQuickRhiItemRenderer::depthStencilBuffer() const
extern "C" Q_DECL_EXPORT
QRhiRenderBuffer *ritual_ZNK21QQuickRhiItemRenderer18depthStencilBufferEv(
    const QQuickRhiItemRenderer *self) {
  return self->depthStencilBuffer();
}

//  QRhiRenderTarget *QQuickRhiItemRenderer::renderTarget() const
extern "C" Q_DECL_EXPORT
QRhiRenderTarget *ritual_ZNK21QQuickRhiItemRenderer12renderTargetEv(
    const QQuickRhiItemRenderer *self) {
  return self->renderTarget();
}

//  a Python function taken by a CuteQQuickRhiItemRenderer, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRhiItemRenderer(
    QQuickRhiItemRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRhiItemRenderer *>(self)->take(key, call);
}
