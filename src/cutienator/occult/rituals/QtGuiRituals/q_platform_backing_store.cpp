//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QPlatformBackingStore that Python can take functions over in. Every QPlatformBackingStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQPlatformBackingStoreCall0)(const void *, int *);
typedef void (*CuteQPlatformBackingStoreCall1)(const void *, QWindow *, const QRegion *, const QPoint *, int *);
typedef int (*CuteQPlatformBackingStoreCall2)(const void *, QWindow *, qreal, const QRegion *, const QPoint *, QPlatformTextureList *, bool, qreal, int *);
typedef const QImage * (*CuteQPlatformBackingStoreCall3)(const void *, int *);
typedef void * (*CuteQPlatformBackingStoreCall4)(const void *, QRhiResourceUpdateBatch *, const QRegion *, QPlatformBackingStore::TextureFlags *, int *);
typedef void * (*CuteQPlatformBackingStoreCall5)(const void *, int *);
typedef void (*CuteQPlatformBackingStoreCall6)(const void *, const QSize *, const QRegion *, int *);
typedef bool (*CuteQPlatformBackingStoreCall7)(const void *, const QRegion *, int, int, int *);
typedef void (*CuteQPlatformBackingStoreCall8)(const void *, const QRegion *, int *);
typedef void (*CuteQPlatformBackingStoreCall9)(const void *, int *);
class CuteQPlatformBackingStore : public QPlatformBackingStore {
public:
  using QPlatformBackingStore::QPlatformBackingStore;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore11paintDeviceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore7toImageEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore9toTextureEP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsINS_11TextureFlagEE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore14graphicsBufferEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6scrollERK7QRegionii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore10beginPaintERK7QRegion")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8endPaintEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  QPaintDevice *QPlatformBackingStore::paintDevice()
  QPaintDevice *paintDevice() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall0 call = reinterpret_cast<CuteQPlatformBackingStoreCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return {};
  }

  //  void QPlatformBackingStore::flush(QWindow *window, const QRegion
  //      &region, const QPoint &offset)
  void flush(
      QWindow *window,
      const QRegion &region,
      const QPoint &offset) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall1 call = reinterpret_cast<CuteQPlatformBackingStoreCall1>(taken[1]);
      call(this, window, &region, &offset, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::flush(window, region, offset);
  }

  //  FlushResult QPlatformBackingStore::rhiFlush(QWindow *window, qreal
  //      sourceDevicePixelRatio, const QRegion &region, const QPoint
  //      &offset, QPlatformTextureList *textures, bool
  //      translucentBackground, qreal sourceTransformFactor)
  QPlatformBackingStore::FlushResult rhiFlush(
      QWindow *window,
      qreal sourceDevicePixelRatio,
      const QRegion &region,
      const QPoint &offset,
      QPlatformTextureList *textures,
      bool translucentBackground,
      qreal sourceTransformFactor) override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall2 call = reinterpret_cast<CuteQPlatformBackingStoreCall2>(taken[2]);
      int given = call(this, window, sourceDevicePixelRatio, &region, &offset, textures, translucentBackground, sourceTransformFactor, &handled);
      if (handled) return static_cast<QPlatformBackingStore::FlushResult>(given);
    }
    return QPlatformBackingStore::rhiFlush(window, sourceDevicePixelRatio, region, offset, textures, translucentBackground, sourceTransformFactor);
  }

  //  QImage QPlatformBackingStore::toImage() const
  QImage toImage() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall3 call = reinterpret_cast<CuteQPlatformBackingStoreCall3>(taken[3]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QPlatformBackingStore::toImage();
  }

  //  QRhiTexture *QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch
  //      *resourceUpdates, const QRegion &dirtyRegion, TextureFlags
  //      *flags) const
  QRhiTexture *toTexture(
      QRhiResourceUpdateBatch *resourceUpdates,
      const QRegion &dirtyRegion,
      QPlatformBackingStore::TextureFlags *flags) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall4 call = reinterpret_cast<CuteQPlatformBackingStoreCall4>(taken[4]);
      void * given = call(this, resourceUpdates, &dirtyRegion, flags, &handled);
      if (handled) return static_cast<QRhiTexture *>(given);
    }
    return QPlatformBackingStore::toTexture(resourceUpdates, dirtyRegion, flags);
  }

  //  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer()
  //      const
  QPlatformGraphicsBuffer *graphicsBuffer() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall5 call = reinterpret_cast<CuteQPlatformBackingStoreCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformGraphicsBuffer *>(given);
    }
    return QPlatformBackingStore::graphicsBuffer();
  }

  //  void QPlatformBackingStore::resize(const QSize &size, const QRegion
  //      &staticContents)
  void resize(const QSize &size, const QRegion &staticContents) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall6 call = reinterpret_cast<CuteQPlatformBackingStoreCall6>(taken[6]);
      call(this, &size, &staticContents, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformBackingStore::scroll(const QRegion &area, int dx, int
  //      dy)
  bool scroll(const QRegion &area, int dx, int dy) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall7 call = reinterpret_cast<CuteQPlatformBackingStoreCall7>(taken[7]);
      bool given = call(this, &area, dx, dy, &handled);
      if (handled) return given;
    }
    return QPlatformBackingStore::scroll(area, dx, dy);
  }

  //  void QPlatformBackingStore::beginPaint(const QRegion &a0)
  void beginPaint(const QRegion &a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall8 call = reinterpret_cast<CuteQPlatformBackingStoreCall8>(taken[8]);
      call(this, &a0, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::beginPaint(a0);
  }

  //  void QPlatformBackingStore::endPaint()
  void endPaint() override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformBackingStoreCall9 call = reinterpret_cast<CuteQPlatformBackingStoreCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::endPaint();
  }
};

//  QPlatformBackingStore::QPlatformBackingStore(QWindow *window)
extern "C" Q_DECL_EXPORT
QPlatformBackingStore *ritual_ZN21QPlatformBackingStoreC1EP7QWindow(
    QWindow *window) {
  return new CuteQPlatformBackingStore(window);
}

//  QPlatformBackingStore::~QPlatformBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStoreD1Ev(QPlatformBackingStore *self) {
  delete self;
}

//  QWindow *QPlatformBackingStore::window() const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK21QPlatformBackingStore6windowEv(
    const QPlatformBackingStore *self) {
  return self->window();
}

//  QBackingStore *QPlatformBackingStore::backingStore() const
extern "C" Q_DECL_EXPORT
QBackingStore *ritual_ZNK21QPlatformBackingStore12backingStoreEv(
    const QPlatformBackingStore *self) {
  return self->backingStore();
}

//  QPaintDevice *QPlatformBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZN21QPlatformBackingStore11paintDeviceEv(
    QPlatformBackingStore *self) {
  return self->paintDevice();
}

//  void QPlatformBackingStore::flush(QWindow *window, const QRegion &region,
//      const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QPlatformBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->flush(window, *region, *offset);
}

//  FlushResult QPlatformBackingStore::rhiFlush(QWindow *window, qreal
//      sourceDevicePixelRatio, const QRegion &region, const QPoint &offset,
//      QPlatformTextureList *textures, bool translucentBackground, qreal
//      sourceTransformFactor)
extern "C" Q_DECL_EXPORT
QPlatformBackingStore::FlushResult ritual_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd(
    QPlatformBackingStore *self,
    QWindow *window,
    qreal sourceDevicePixelRatio,
    const QRegion *region,
    const QPoint *offset,
    QPlatformTextureList *textures,
    bool translucentBackground,
    qreal sourceTransformFactor) {
  return self->rhiFlush(
      window,
      sourceDevicePixelRatio,
      *region,
      *offset,
      textures,
      translucentBackground,
      sourceTransformFactor);
}

//  QImage QPlatformBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK21QPlatformBackingStore7toImageEv(
    const QPlatformBackingStore *self) {
  return new QImage(self->toImage());
}

//  QRhiTexture *QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch
//      *resourceUpdates, const QRegion &dirtyRegion, TextureFlags *flags)
//      const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_ZNK21QPlatformBackingStore9toTextureEP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsINS_11TextureFlagEE(
    const QPlatformBackingStore *self,
    QRhiResourceUpdateBatch *resourceUpdates,
    const QRegion *dirtyRegion,
    QPlatformBackingStore::TextureFlags *flags) {
  return self->toTexture(resourceUpdates, *dirtyRegion, flags);
}

//  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer() const
extern "C" Q_DECL_EXPORT
QPlatformGraphicsBuffer *ritual_ZNK21QPlatformBackingStore14graphicsBufferEv(
    const QPlatformBackingStore *self) {
  return self->graphicsBuffer();
}

//  void QPlatformBackingStore::resize(const QSize &size, const QRegion
//      &staticContents)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion(
    QPlatformBackingStore *self,
    const QSize *size,
    const QRegion *staticContents) {
  self->resize(*size, *staticContents);
}

//  bool QPlatformBackingStore::scroll(const QRegion &area, int dx, int dy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QPlatformBackingStore6scrollERK7QRegionii(
    QPlatformBackingStore *self,
    const QRegion *area,
    int dx,
    int dy) {
  return self->scroll(*area, dx, dy);
}

//  void QPlatformBackingStore::beginPaint(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore10beginPaintERK7QRegion(
    QPlatformBackingStore *self,
    const QRegion *a0) {
  self->beginPaint(*a0);
}

//  void QPlatformBackingStore::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore8endPaintEv(
    QPlatformBackingStore *self) {
  self->endPaint();
}

//  void QPlatformBackingStore::createRhi(QWindow *window,
//      QPlatformBackingStoreRhiConfig config)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore9createRhiEP7QWindow30QPlatformBackingStoreRhiConfig(
    QPlatformBackingStore *self,
    QWindow *window,
    const QPlatformBackingStoreRhiConfig *config) {
  self->createRhi(window, *config);
}

//  QRhi *QPlatformBackingStore::rhi(QWindow *window) const
extern "C" Q_DECL_EXPORT
QRhi *ritual_ZNK21QPlatformBackingStore3rhiEP7QWindow(
    const QPlatformBackingStore *self,
    QWindow *window) {
  return self->rhi(window);
}

//  void QPlatformBackingStore::graphicsDeviceReportedLost(QWindow *window)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore26graphicsDeviceReportedLostEP7QWindow(
    QPlatformBackingStore *self,
    QWindow *window) {
  self->graphicsDeviceReportedLost(window);
}

//  void QPlatformBackingStore::setBackingStore(QBackingStore *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPlatformBackingStore15setBackingStoreEP13QBackingStore(
    QPlatformBackingStore *self,
    QBackingStore *a0) {
  self->setBackingStore(a0);
}

//  a Python function taken by a CuteQPlatformBackingStore, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformBackingStore(
    QPlatformBackingStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformBackingStore *>(self)->take(key, call);
}

//  void QPlatformBackingStore::flush(QWindow *window, const QRegion &region,
//      const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QPlatformBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->QPlatformBackingStore::flush(window, *region, *offset);
}

//  FlushResult QPlatformBackingStore::rhiFlush(QWindow *window, qreal
//      sourceDevicePixelRatio, const QRegion &region, const QPoint &offset,
//      QPlatformTextureList *textures, bool translucentBackground, qreal
//      sourceTransformFactor)
extern "C" Q_DECL_EXPORT
QPlatformBackingStore::FlushResult ritual_own_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd(
    QPlatformBackingStore *self,
    QWindow *window,
    qreal sourceDevicePixelRatio,
    const QRegion *region,
    const QPoint *offset,
    QPlatformTextureList *textures,
    bool translucentBackground,
    qreal sourceTransformFactor) {
  return self->QPlatformBackingStore::rhiFlush(
      window,
      sourceDevicePixelRatio,
      *region,
      *offset,
      textures,
      translucentBackground,
      sourceTransformFactor);
}

//  QImage QPlatformBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK21QPlatformBackingStore7toImageEv(
    const QPlatformBackingStore *self) {
  return new QImage(self->QPlatformBackingStore::toImage());
}

//  QRhiTexture *QPlatformBackingStore::toTexture(QRhiResourceUpdateBatch
//      *resourceUpdates, const QRegion &dirtyRegion, TextureFlags *flags)
//      const
extern "C" Q_DECL_EXPORT
QRhiTexture *ritual_own_ZNK21QPlatformBackingStore9toTextureEP23QRhiResourceUpdateBatchRK7QRegionP6QFlagsINS_11TextureFlagEE(
    const QPlatformBackingStore *self,
    QRhiResourceUpdateBatch *resourceUpdates,
    const QRegion *dirtyRegion,
    QPlatformBackingStore::TextureFlags *flags) {
  return self->QPlatformBackingStore::toTexture(
      resourceUpdates,
      *dirtyRegion,
      flags);
}

//  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer() const
extern "C" Q_DECL_EXPORT
QPlatformGraphicsBuffer *ritual_own_ZNK21QPlatformBackingStore14graphicsBufferEv(
    const QPlatformBackingStore *self) {
  return self->QPlatformBackingStore::graphicsBuffer();
}

//  bool QPlatformBackingStore::scroll(const QRegion &area, int dx, int dy)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN21QPlatformBackingStore6scrollERK7QRegionii(
    QPlatformBackingStore *self,
    const QRegion *area,
    int dx,
    int dy) {
  return self->QPlatformBackingStore::scroll(*area, dx, dy);
}

//  void QPlatformBackingStore::beginPaint(const QRegion &a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformBackingStore10beginPaintERK7QRegion(
    QPlatformBackingStore *self,
    const QRegion *a0) {
  self->QPlatformBackingStore::beginPaint(*a0);
}

//  void QPlatformBackingStore::endPaint()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QPlatformBackingStore8endPaintEv(
    QPlatformBackingStore *self) {
  self->QPlatformBackingStore::endPaint();
}
