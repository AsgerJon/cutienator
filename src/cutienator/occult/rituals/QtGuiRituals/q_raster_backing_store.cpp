//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qrasterbackingstore_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#if (defined(Q_OS_DARWIN)) || (defined(Q_OS_QNX)) || (defined(Q_OS_ANDROID)) || (defined(Q_OS_HARMONY))
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qrasterbackingstore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtGui/qregion.h>
#include <QtGui/qimage.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  Only a class built on QRasterBackingStore may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQRasterBackingStore : QRasterBackingStore {
  using QRasterBackingStore::format;
};

//  A QRasterBackingStore that Python can take functions over in. Every QRasterBackingStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQRasterBackingStoreCall0)(const void *, const QSize *, const QRegion *, int *);
typedef bool (*CuteQRasterBackingStoreCall1)(const void *, const QRegion *, int, int, int *);
typedef void (*CuteQRasterBackingStoreCall2)(const void *, const QRegion *, int *);
typedef void * (*CuteQRasterBackingStoreCall3)(const void *, int *);
typedef const QImage * (*CuteQRasterBackingStoreCall4)(const void *, int *);
typedef int (*CuteQRasterBackingStoreCall5)(const void *, int *);
typedef void (*CuteQRasterBackingStoreCall6)(const void *, QWindow *, const QRegion *, const QPoint *, int *);
typedef int (*CuteQRasterBackingStoreCall7)(const void *, QWindow *, qreal, const QRegion *, const QPoint *, QPlatformTextureList *, bool, qreal, int *);
typedef void * (*CuteQRasterBackingStoreCall8)(const void *, int *);
typedef void (*CuteQRasterBackingStoreCall9)(const void *, int *);
class CuteQRasterBackingStore : public QRasterBackingStore {
public:
  using QRasterBackingStore::QRasterBackingStore;
  CuteQRasterBackingStore(const QRasterBackingStore &other) : QRasterBackingStore(other) {}
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6scrollERK7QRegionii")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore10beginPaintERK7QRegion")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore11paintDeviceEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore7toImageEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QRasterBackingStore6formatEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint")) {
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

  //  void QRasterBackingStore::resize(const QSize &size, const QRegion
  //      &staticContents)
  void resize(const QSize &size, const QRegion &staticContents) override {
    if (taken[0]) {
      int handled = 0;
      CuteQRasterBackingStoreCall0 call = reinterpret_cast<CuteQRasterBackingStoreCall0>(taken[0]);
      call(this, &size, &staticContents, &handled);
      if (handled) return;
    }
    QRasterBackingStore::resize(size, staticContents);
  }

  //  bool QRasterBackingStore::scroll(const QRegion &area, int dx, int dy)
  bool scroll(const QRegion &area, int dx, int dy) override {
    if (taken[1]) {
      int handled = 0;
      CuteQRasterBackingStoreCall1 call = reinterpret_cast<CuteQRasterBackingStoreCall1>(taken[1]);
      bool given = call(this, &area, dx, dy, &handled);
      if (handled) return given;
    }
    return QRasterBackingStore::scroll(area, dx, dy);
  }

  //  void QRasterBackingStore::beginPaint(const QRegion &region)
  void beginPaint(const QRegion &region) override {
    if (taken[2]) {
      int handled = 0;
      CuteQRasterBackingStoreCall2 call = reinterpret_cast<CuteQRasterBackingStoreCall2>(taken[2]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QRasterBackingStore::beginPaint(region);
  }

  //  QPaintDevice *QRasterBackingStore::paintDevice()
  QPaintDevice *paintDevice() override {
    if (taken[3]) {
      int handled = 0;
      CuteQRasterBackingStoreCall3 call = reinterpret_cast<CuteQRasterBackingStoreCall3>(taken[3]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QRasterBackingStore::paintDevice();
  }

  //  QImage QRasterBackingStore::toImage() const
  QImage toImage() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQRasterBackingStoreCall4 call = reinterpret_cast<CuteQRasterBackingStoreCall4>(taken[4]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QRasterBackingStore::toImage();
  }

  //  QImage::Format QRasterBackingStore::format() const
  QImage::Format format() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQRasterBackingStoreCall5 call = reinterpret_cast<CuteQRasterBackingStoreCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return static_cast<QImage::Format>(given);
    }
    return QRasterBackingStore::format();
  }

  //  void QPlatformBackingStore::flush(QWindow *window, const QRegion
  //      &region, const QPoint &offset)
  void flush(
      QWindow *window,
      const QRegion &region,
      const QPoint &offset) override {
    if (taken[6]) {
      int handled = 0;
      CuteQRasterBackingStoreCall6 call = reinterpret_cast<CuteQRasterBackingStoreCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQRasterBackingStoreCall7 call = reinterpret_cast<CuteQRasterBackingStoreCall7>(taken[7]);
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
      CuteQRasterBackingStoreCall8 call = reinterpret_cast<CuteQRasterBackingStoreCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformGraphicsBuffer *>(given);
    }
    return QPlatformBackingStore::graphicsBuffer();
  }

  //  void QPlatformBackingStore::endPaint()
  void endPaint() override {
    if (taken[9]) {
      int handled = 0;
      CuteQRasterBackingStoreCall9 call = reinterpret_cast<CuteQRasterBackingStoreCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::endPaint();
  }
};

//  QRasterBackingStore::QRasterBackingStore(QWindow *window)
extern "C" Q_DECL_EXPORT
QRasterBackingStore *ritual_ZN19QRasterBackingStoreC1EP7QWindow(
    QWindow *window) {
  return new CuteQRasterBackingStore(window);
}

//  QRasterBackingStore::~QRasterBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRasterBackingStoreD1Ev(QRasterBackingStore *self) {
  delete self;
}

//  void QRasterBackingStore::resize(const QSize &size, const QRegion
//      &staticContents)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRasterBackingStore6resizeERK5QSizeRK7QRegion(
    QRasterBackingStore *self,
    const QSize *size,
    const QRegion *staticContents) {
  self->resize(*size, *staticContents);
}

//  bool QRasterBackingStore::scroll(const QRegion &area, int dx, int dy)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRasterBackingStore6scrollERK7QRegionii(
    QRasterBackingStore *self,
    const QRegion *area,
    int dx,
    int dy) {
  return self->scroll(*area, dx, dy);
}

//  void QRasterBackingStore::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRasterBackingStore10beginPaintERK7QRegion(
    QRasterBackingStore *self,
    const QRegion *region) {
  self->beginPaint(*region);
}

//  QPaintDevice *QRasterBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZN19QRasterBackingStore11paintDeviceEv(
    QRasterBackingStore *self) {
  return self->paintDevice();
}

//  QImage QRasterBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK19QRasterBackingStore7toImageEv(
    const QRasterBackingStore *self) {
  return new QImage(self->toImage());
}

//  QImage::Format QRasterBackingStore::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_ZNK19QRasterBackingStore6formatEv(
    const QRasterBackingStore *self) {
  return self->format();
}

//  a Python function taken by a CuteQRasterBackingStore, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QRasterBackingStore(
    QRasterBackingStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQRasterBackingStore *>(self)->take(key, call);
}

//  void QRasterBackingStore::resize(const QSize &size, const QRegion
//      &staticContents)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QRasterBackingStore6resizeERK5QSizeRK7QRegion(
    QRasterBackingStore *self,
    const QSize *size,
    const QRegion *staticContents) {
  self->QRasterBackingStore::resize(*size, *staticContents);
}

//  bool QRasterBackingStore::scroll(const QRegion &area, int dx, int dy)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QRasterBackingStore6scrollERK7QRegionii(
    QRasterBackingStore *self,
    const QRegion *area,
    int dx,
    int dy) {
  return self->QRasterBackingStore::scroll(*area, dx, dy);
}

//  void QRasterBackingStore::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QRasterBackingStore10beginPaintERK7QRegion(
    QRasterBackingStore *self,
    const QRegion *region) {
  self->QRasterBackingStore::beginPaint(*region);
}

//  QPaintDevice *QRasterBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZN19QRasterBackingStore11paintDeviceEv(
    QRasterBackingStore *self) {
  return self->QRasterBackingStore::paintDevice();
}

//  QImage QRasterBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK19QRasterBackingStore7toImageEv(
    const QRasterBackingStore *self) {
  return new QImage(self->QRasterBackingStore::toImage());
}

//  QImage::Format QRasterBackingStore::format() const
extern "C" Q_DECL_EXPORT
QImage::Format ritual_own_ZNK19QRasterBackingStore6formatEv(
    const QRasterBackingStore *self) {
  return static_cast<const OwnQRasterBackingStore *>(self)->OwnQRasterBackingStore::format();
}

#endif  // (defined(Q_OS_DARWIN)) || (defined(Q_OS_QNX)) || (defined(Q_OS_ANDROID)) || (defined(Q_OS_HARMONY))
