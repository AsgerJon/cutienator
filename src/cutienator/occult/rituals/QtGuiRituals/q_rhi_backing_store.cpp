//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrhibackingstore_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_DARWIN)) || (defined(Q_OS_QNX)) || (defined(Q_OS_ANDROID)) || (defined(Q_OS_HARMONY))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrhibackingstore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QRhiBackingStore that Python can take functions over in. Every QRhiBackingStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRhiBackingStoreCall0)(const void *, QWindow *, const QRegion *, const QPoint *, int *);
typedef int (*CuteQRhiBackingStoreCall1)(const void *, int *);
typedef void (*CuteQRhiBackingStoreCall2)(const void *, const QSize *, const QRegion *, int *);
typedef bool (*CuteQRhiBackingStoreCall3)(const void *, const QRegion *, int, int, int *);
typedef void (*CuteQRhiBackingStoreCall4)(const void *, const QRegion *, int *);
typedef void * (*CuteQRhiBackingStoreCall5)(const void *, int *);
typedef const QImage * (*CuteQRhiBackingStoreCall6)(const void *, int *);
typedef int (*CuteQRhiBackingStoreCall7)(const void *, QWindow *, qreal, const QRegion *, const QPoint *, QPlatformTextureList *, bool, qreal, int *);
typedef void * (*CuteQRhiBackingStoreCall8)(const void *, int *);
typedef void (*CuteQRhiBackingStoreCall9)(const void *, int *);
class CuteQRhiBackingStore : public QRhiBackingStore {
public:
  using QRhiBackingStore::QRhiBackingStore;
  CuteQRhiBackingStore(const QRhiBackingStore &other) : QRhiBackingStore(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QRasterBackingStore6formatEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6scrollERK7QRegionii")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore10beginPaintERK7QRegion")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore11paintDeviceEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore7toImageEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore14graphicsBufferEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8endPaintEv")) {
      taken[9] = call;
      return true;
    }
    return false;
  }

  //  void QRhiBackingStore::flush(QWindow *window, const QRegion &region,
  //      const QPoint &offset)
  void flush(
      QWindow *window,
      const QRegion &region,
      const QPoint &offset) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRhiBackingStoreCall0 call = reinterpret_cast<CuteQRhiBackingStoreCall0>(taken[0]);
      call(this, window, &region, &offset, &handled);
      if (handled) return;
    }
    QRhiBackingStore::flush(window, region, offset);
  }

  //  QImage::Format QRhiBackingStore::format() const
  QImage::Format format() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQRhiBackingStoreCall1 call = reinterpret_cast<CuteQRhiBackingStoreCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QImage::Format>(given);
    }
    return QRhiBackingStore::format();
  }

  //  void QRasterBackingStore::resize(const QSize &size, const QRegion
  //      &staticContents)
  void resize(const QSize &size, const QRegion &staticContents) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRhiBackingStoreCall2 call = reinterpret_cast<CuteQRhiBackingStoreCall2>(taken[2]);
      call(this, &size, &staticContents, &handled);
      if (handled) return;
    }
    QRasterBackingStore::resize(size, staticContents);
  }

  //  bool QRasterBackingStore::scroll(const QRegion &area, int dx, int dy)
  bool scroll(const QRegion &area, int dx, int dy) override {
    if (taken[3]) {
      int handled = 0;
      CuteQRhiBackingStoreCall3 call = reinterpret_cast<CuteQRhiBackingStoreCall3>(taken[3]);
      bool given = call(this, &area, dx, dy, &handled);
      if (handled) return given;
    }
    return QRasterBackingStore::scroll(area, dx, dy);
  }

  //  void QRasterBackingStore::beginPaint(const QRegion &region)
  void beginPaint(const QRegion &region) override {
    if (taken[4]) {
      int handled = 0;
      CuteQRhiBackingStoreCall4 call = reinterpret_cast<CuteQRhiBackingStoreCall4>(taken[4]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QRasterBackingStore::beginPaint(region);
  }

  //  QPaintDevice *QRasterBackingStore::paintDevice()
  QPaintDevice *paintDevice() override {
    if (taken[5]) {
      int handled = 0;
      CuteQRhiBackingStoreCall5 call = reinterpret_cast<CuteQRhiBackingStoreCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QRasterBackingStore::paintDevice();
  }

  //  QImage QRasterBackingStore::toImage() const
  QImage toImage() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQRhiBackingStoreCall6 call = reinterpret_cast<CuteQRhiBackingStoreCall6>(taken[6]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRasterBackingStore::toImage();
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
    if (taken[7]) {
      int handled = 0;
      CuteQRhiBackingStoreCall7 call = reinterpret_cast<CuteQRhiBackingStoreCall7>(taken[7]);
      int given = call(this, window, sourceDevicePixelRatio, &region, &offset, textures, translucentBackground, sourceTransformFactor, &handled);
      if (handled) return static_cast<QPlatformBackingStore::FlushResult>(given);
    }
    return QPlatformBackingStore::rhiFlush(window, sourceDevicePixelRatio, region, offset, textures, translucentBackground, sourceTransformFactor);
  }

  //  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer()
  //      const
  QPlatformGraphicsBuffer *graphicsBuffer() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQRhiBackingStoreCall8 call = reinterpret_cast<CuteQRhiBackingStoreCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformGraphicsBuffer *>(given);
    }
    return QPlatformBackingStore::graphicsBuffer();
  }

  //  void QPlatformBackingStore::endPaint()
  void endPaint() override {
    if (taken[9]) {
      int handled = 0;
      CuteQRhiBackingStoreCall9 call = reinterpret_cast<CuteQRhiBackingStoreCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::endPaint();
  }
};

//  QRhiBackingStore::QRhiBackingStore(QWindow *window)
extern "C" Q_DECL_EXPORT
QRhiBackingStore *ritual_ZN16QRhiBackingStoreC1EP7QWindow(QWindow *window) {
  return new CuteQRhiBackingStore(window);
}

//  QRhiBackingStore::~QRhiBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiBackingStoreD1Ev(QRhiBackingStore *self) {
  delete self;
}

//  void QRhiBackingStore::flush(QWindow *window, const QRegion &region,
//      const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QRhiBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QRhiBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->flush(window, *region, *offset);
}

//  QImage::Format QRhiBackingStore::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK16QRhiBackingStore6formatEv(
    const QRhiBackingStore *self) {
  return self->format();
}

//  a Python function taken by a CuteQRhiBackingStore, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRhiBackingStore(
    QRhiBackingStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRhiBackingStore *>(self)->take(key, call);
}

//  void QRhiBackingStore::flush(QWindow *window, const QRegion &region,
//      const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QRhiBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QRhiBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->QRhiBackingStore::flush(window, *region, *offset);
}

//  QImage::Format QRhiBackingStore::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_own_ZNK16QRhiBackingStore6formatEv(
    const QRhiBackingStore *self) {
  return self->QRhiBackingStore::format();
}

#endif  // (defined(Q_OS_DARWIN)) || (defined(Q_OS_QNX)) || (defined(Q_OS_ANDROID)) || (defined(Q_OS_HARMONY))
