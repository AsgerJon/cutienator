//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvaspainteritemrenderer.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCanvasPainter/qtcanvaspainterglobal.h>
#if 1
#include <QtCanvasPainter/QtCanvasPainter>
#include <QtCanvasPainter/qcanvaspainteritemrenderer.h>
#include <QtGui/qcolor.h>
#include <QtCanvasPainter/qcanvasoffscreencanvas.h>
#include <cstring>

//  Only a class built on QCanvasPainterItemRenderer may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQCanvasPainterItemRenderer : QCanvasPainterItemRenderer {
  using QCanvasPainterItemRenderer::initializeResources;
  using QCanvasPainterItemRenderer::prePaint;
  using QCanvasPainterItemRenderer::paint;
  using QCanvasPainterItemRenderer::synchronizeData;
  using QCanvasPainterItemRenderer::initialize;
  using QCanvasPainterItemRenderer::render;
  using QCanvasPainterItemRenderer::synchronize;
};

//  A QCanvasPainterItemRenderer that Python can take functions over in. Every QCanvasPainterItemRenderer
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCanvasPainterItemRendererCall0)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall1)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall2)(const void *, QCanvasPainter *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall3)(const void *, QCanvasPainterItem *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall4)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall5)(const void *, QRhiCommandBuffer *, int *);
typedef void (*CuteQCanvasPainterItemRendererCall6)(const void *, QQuickRhiItem *, int *);
class CuteQCanvasPainterItemRenderer : public QCanvasPainterItemRenderer {
public:
  using QCanvasPainterItemRenderer::QCanvasPainterItemRenderer;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN26QCanvasPainterItemRenderer19initializeResourcesEP14QCanvasPainter")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPainter")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainter")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QCanvasPainterItem")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer10initializeEP17QRhiCommandBuffer")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer6renderEP17QRhiCommandBuffer")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QQuickRhiItemRenderer11synchronizeEP13QQuickRhiItem")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  void QCanvasPainterItemRenderer::initializeResources(QCanvasPainter
  //      *painter)
  void initializeResources(QCanvasPainter *painter) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall0 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall0>(taken[0]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::initializeResources(painter);
  }

  //  void QCanvasPainterItemRenderer::prePaint(QCanvasPainter *painter)
  void prePaint(QCanvasPainter *painter) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall1 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall1>(taken[1]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::prePaint(painter);
  }

  //  void QCanvasPainterItemRenderer::paint(QCanvasPainter *painter)
  void paint(QCanvasPainter *painter) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall2 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall2>(taken[2]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::paint(painter);
  }

  //  void QCanvasPainterItemRenderer::synchronizeData(QCanvasPainterItem
  //      *item)
  void synchronizeData(QCanvasPainterItem *item) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall3 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall3>(taken[3]);
      call(this, item, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::synchronizeData(item);
  }

  //  void QCanvasPainterItemRenderer::initialize(QRhiCommandBuffer *cb)
  void initialize(QRhiCommandBuffer *cb) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall4 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall4>(taken[4]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::initialize(cb);
  }

  //  void QCanvasPainterItemRenderer::render(QRhiCommandBuffer *cb)
  void render(QRhiCommandBuffer *cb) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall5 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall5>(taken[5]);
      call(this, cb, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::render(cb);
  }

  //  void QCanvasPainterItemRenderer::synchronize(QQuickRhiItem *item)
  void synchronize(QQuickRhiItem *item) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCanvasPainterItemRendererCall6 call = reinterpret_cast<CuteQCanvasPainterItemRendererCall6>(taken[6]);
      call(this, item, &handled);
      if (handled) return;
    }
    QCanvasPainterItemRenderer::synchronize(item);
  }
};

//  QCanvasPainterItemRenderer::QCanvasPainterItemRenderer()
extern "C" Q_DECL_EXPORT
QCanvasPainterItemRenderer *ritual_ZN26QCanvasPainterItemRendererC1Ev() {
  return new CuteQCanvasPainterItemRenderer();
}

//  QCanvasPainterItemRenderer::~QCanvasPainterItemRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRendererD1Ev(
    QCanvasPainterItemRenderer *self) {
  delete self;
}

//  QColor QCanvasPainterItemRenderer::fillColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK26QCanvasPainterItemRenderer9fillColorEv(
    const QCanvasPainterItemRenderer *self) {
  return new QColor(self->fillColor());
}

//  QCanvasPainter *QCanvasPainterItemRenderer::painter() const
extern "C" Q_DECL_EXPORT
QCanvasPainter *ritual_ZNK26QCanvasPainterItemRenderer7painterEv(
    const QCanvasPainterItemRenderer *self) {
  return self->painter();
}

//  qreal QCanvasPainterItemRenderer::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QCanvasPainterItemRenderer5widthEv(
    const QCanvasPainterItemRenderer *self) {
  return self->width();
}

//  qreal QCanvasPainterItemRenderer::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK26QCanvasPainterItemRenderer6heightEv(
    const QCanvasPainterItemRenderer *self) {
  return self->height();
}

//  bool QCanvasPainterItemRenderer::hasSharedPainter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK26QCanvasPainterItemRenderer16hasSharedPainterEv(
    const QCanvasPainterItemRenderer *self) {
  return self->hasSharedPainter();
}

//  void QCanvasPainterItemRenderer::setSharedPainter(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer16setSharedPainterEb(
    QCanvasPainterItemRenderer *self,
    bool enable) {
  self->setSharedPainter(enable);
}

//  void QCanvasPainterItemRenderer::initializeResources(QCanvasPainter
//      *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer19initializeResourcesEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  self->initializeResources(painter);
}

//  void QCanvasPainterItemRenderer::prePaint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  self->prePaint(painter);
}

//  void QCanvasPainterItemRenderer::paint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  self->paint(painter);
}

//  void QCanvasPainterItemRenderer::synchronizeData(QCanvasPainterItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QCanvasPainterItem(
    QCanvasPainterItemRenderer *self,
    QCanvasPainterItem *item) {
  self->synchronizeData(item);
}

//  void QCanvasPainterItemRenderer::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer10initializeEP17QRhiCommandBuffer(
    QCanvasPainterItemRenderer *self,
    QRhiCommandBuffer *cb) {
  self->initialize(cb);
}

//  void QCanvasPainterItemRenderer::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer6renderEP17QRhiCommandBuffer(
    QCanvasPainterItemRenderer *self,
    QRhiCommandBuffer *cb) {
  self->render(cb);
}

//  void QCanvasPainterItemRenderer::synchronize(QQuickRhiItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer11synchronizeEP13QQuickRhiItem(
    QCanvasPainterItemRenderer *self,
    QQuickRhiItem *item) {
  self->synchronize(item);
}

//  void QCanvasPainterItemRenderer::endCanvasPainting()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer17endCanvasPaintingEv(
    QCanvasPainterItemRenderer *self) {
  self->endCanvasPainting();
}

//  void QCanvasPainterItemRenderer::grabCanvasImpl(const
//      QCanvasOffscreenCanvas &canvas, const QObject *context,
//      QtPrivate::QSlotObjectBase *slotObj)
extern "C" Q_DECL_EXPORT
void ritual_ZN26QCanvasPainterItemRenderer14grabCanvasImplERK22QCanvasOffscreenCanvasPK7QObjectPN9QtPrivate15QSlotObjectBaseE(
    QCanvasPainterItemRenderer *self,
    const QCanvasOffscreenCanvas *canvas,
    const QObject *context,
    QtPrivate::QSlotObjectBase *slotObj) {
  self->grabCanvasImpl(*canvas, context, slotObj);
}

//  a Python function taken by a CuteQCanvasPainterItemRenderer, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCanvasPainterItemRenderer(
    QCanvasPainterItemRenderer *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCanvasPainterItemRenderer *>(self)->take(key, call);
}

//  void QCanvasPainterItemRenderer::initializeResources(QCanvasPainter
//      *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer19initializeResourcesEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::initializeResources(
      painter);
}

//  void QCanvasPainterItemRenderer::prePaint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer8prePaintEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::prePaint(
      painter);
}

//  void QCanvasPainterItemRenderer::paint(QCanvasPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer5paintEP14QCanvasPainter(
    QCanvasPainterItemRenderer *self,
    QCanvasPainter *painter) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::paint(
      painter);
}

//  void QCanvasPainterItemRenderer::synchronizeData(QCanvasPainterItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer15synchronizeDataEP18QCanvasPainterItem(
    QCanvasPainterItemRenderer *self,
    QCanvasPainterItem *item) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::synchronizeData(
      item);
}

//  void QCanvasPainterItemRenderer::initialize(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer10initializeEP17QRhiCommandBuffer(
    QCanvasPainterItemRenderer *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::initialize(
      cb);
}

//  void QCanvasPainterItemRenderer::render(QRhiCommandBuffer *cb)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer6renderEP17QRhiCommandBuffer(
    QCanvasPainterItemRenderer *self,
    QRhiCommandBuffer *cb) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::render(
      cb);
}

//  void QCanvasPainterItemRenderer::synchronize(QQuickRhiItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN26QCanvasPainterItemRenderer11synchronizeEP13QQuickRhiItem(
    QCanvasPainterItemRenderer *self,
    QQuickRhiItem *item) {
  static_cast<OwnQCanvasPainterItemRenderer *>(self)->OwnQCanvasPainterItemRenderer::synchronize(
      item);
}

#endif  // 1
