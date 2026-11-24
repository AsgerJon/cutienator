//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositorbackingstore_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtOpenGL/qtopenglglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(egl)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpenGL/QtOpenGL>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtOpenGL/6.12.0/QtOpenGL/private/qopenglcompositorbackingstore_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qregion.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <QtGui/qimage.h>
#include <cstring>

//  A QOpenGLCompositorBackingStore that Python can take functions over in. Every QOpenGLCompositorBackingStore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQOpenGLCompositorBackingStoreCall0)(const void *, int *);
typedef void (*CuteQOpenGLCompositorBackingStoreCall1)(const void *, const QRegion *, int *);
typedef void (*CuteQOpenGLCompositorBackingStoreCall2)(const void *, QWindow *, const QRegion *, const QPoint *, int *);
typedef void (*CuteQOpenGLCompositorBackingStoreCall3)(const void *, const QSize *, const QRegion *, int *);
typedef const QImage * (*CuteQOpenGLCompositorBackingStoreCall4)(const void *, int *);
typedef int (*CuteQOpenGLCompositorBackingStoreCall5)(const void *, QWindow *, qreal, const QRegion *, const QPoint *, QPlatformTextureList *, bool, qreal, int *);
typedef void * (*CuteQOpenGLCompositorBackingStoreCall6)(const void *, int *);
typedef bool (*CuteQOpenGLCompositorBackingStoreCall7)(const void *, const QRegion *, int, int, int *);
typedef void (*CuteQOpenGLCompositorBackingStoreCall8)(const void *, int *);
class CuteQOpenGLCompositorBackingStore : public QOpenGLCompositorBackingStore {
public:
  using QOpenGLCompositorBackingStore::QOpenGLCompositorBackingStore;
  CuteQOpenGLCompositorBackingStore(const QOpenGLCompositorBackingStore &other) : QOpenGLCompositorBackingStore(other) {}
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore11paintDeviceEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore10beginPaintERK7QRegion")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore5flushEP7QWindowRK7QRegionRK6QPoint")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6resizeERK5QSizeRK7QRegion")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore7toImageEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QPlatformBackingStore14graphicsBufferEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore6scrollERK7QRegionii")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QPlatformBackingStore8endPaintEv")) {
      taken[8] = call;
      return true;
    }
    return false;
  }

  //  QPaintDevice *QOpenGLCompositorBackingStore::paintDevice()
  QPaintDevice *paintDevice() override {
    if (taken[0]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall0 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPaintDevice *>(given);
    }
    return QOpenGLCompositorBackingStore::paintDevice();
  }

  //  void QOpenGLCompositorBackingStore::beginPaint(const QRegion &region)
  void beginPaint(const QRegion &region) override {
    if (taken[1]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall1 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall1>(taken[1]);
      call(this, &region, &handled);
      if (handled) return;
    }
    QOpenGLCompositorBackingStore::beginPaint(region);
  }

  //  void QOpenGLCompositorBackingStore::flush(QWindow *window, const
  //      QRegion &region, const QPoint &offset)
  void flush(
      QWindow *window,
      const QRegion &region,
      const QPoint &offset) override {
    if (taken[2]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall2 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall2>(taken[2]);
      call(this, window, &region, &offset, &handled);
      if (handled) return;
    }
    QOpenGLCompositorBackingStore::flush(window, region, offset);
  }

  //  void QOpenGLCompositorBackingStore::resize(const QSize &size, const
  //      QRegion &staticContents)
  void resize(const QSize &size, const QRegion &staticContents) override {
    if (taken[3]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall3 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall3>(taken[3]);
      call(this, &size, &staticContents, &handled);
      if (handled) return;
    }
    QOpenGLCompositorBackingStore::resize(size, staticContents);
  }

  //  QImage QOpenGLCompositorBackingStore::toImage() const
  QImage toImage() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall4 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall4>(taken[4]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QOpenGLCompositorBackingStore::toImage();
  }

  //  FlushResult QOpenGLCompositorBackingStore::rhiFlush(QWindow *window,
  //      qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
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
    if (taken[5]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall5 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall5>(taken[5]);
      int given = call(this, window, sourceDevicePixelRatio, &region, &offset, textures, translucentBackground, sourceTransformFactor, &handled);
      if (handled) return static_cast<QPlatformBackingStore::FlushResult>(given);
    }
    return QOpenGLCompositorBackingStore::rhiFlush(window, sourceDevicePixelRatio, region, offset, textures, translucentBackground, sourceTransformFactor);
  }

  //  QPlatformGraphicsBuffer *QPlatformBackingStore::graphicsBuffer()
  //      const
  QPlatformGraphicsBuffer *graphicsBuffer() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall6 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall6>(taken[6]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformGraphicsBuffer *>(given);
    }
    return QPlatformBackingStore::graphicsBuffer();
  }

  //  bool QPlatformBackingStore::scroll(const QRegion &area, int dx, int
  //      dy)
  bool scroll(const QRegion &area, int dx, int dy) override {
    if (taken[7]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall7 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall7>(taken[7]);
      bool given = call(this, &area, dx, dy, &handled);
      if (handled) return given;
    }
    return QPlatformBackingStore::scroll(area, dx, dy);
  }

  //  void QPlatformBackingStore::endPaint()
  void endPaint() override {
    if (taken[8]) {
      int handled = 0;
      CuteQOpenGLCompositorBackingStoreCall8 call = reinterpret_cast<CuteQOpenGLCompositorBackingStoreCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QPlatformBackingStore::endPaint();
  }
};

//  QOpenGLCompositorBackingStore::QOpenGLCompositorBackingStore(QWindow
//      *window)
extern "C" Q_DECL_EXPORT
QOpenGLCompositorBackingStore *ritual_ZN29QOpenGLCompositorBackingStoreC1EP7QWindow(
    QWindow *window) {
  return new CuteQOpenGLCompositorBackingStore(window);
}

//  QOpenGLCompositorBackingStore::~QOpenGLCompositorBackingStore()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStoreD1Ev(
    QOpenGLCompositorBackingStore *self) {
  delete self;
}

//  QPaintDevice *QOpenGLCompositorBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_ZN29QOpenGLCompositorBackingStore11paintDeviceEv(
    QOpenGLCompositorBackingStore *self) {
  return self->paintDevice();
}

//  void QOpenGLCompositorBackingStore::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStore10beginPaintERK7QRegion(
    QOpenGLCompositorBackingStore *self,
    const QRegion *region) {
  self->beginPaint(*region);
}

//  void QOpenGLCompositorBackingStore::flush(QWindow *window, const QRegion
//      &region, const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QOpenGLCompositorBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->flush(window, *region, *offset);
}

//  void QOpenGLCompositorBackingStore::resize(const QSize &size, const
//      QRegion &staticContents)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStore6resizeERK5QSizeRK7QRegion(
    QOpenGLCompositorBackingStore *self,
    const QSize *size,
    const QRegion *staticContents) {
  self->resize(*size, *staticContents);
}

//  QImage QOpenGLCompositorBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_ZNK29QOpenGLCompositorBackingStore7toImageEv(
    const QOpenGLCompositorBackingStore *self) {
  return new QImage(self->toImage());
}

//  FlushResult QOpenGLCompositorBackingStore::rhiFlush(QWindow *window,
//      qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
//      &offset, QPlatformTextureList *textures, bool translucentBackground,
//      qreal sourceTransformFactor)
extern "C" Q_DECL_EXPORT
QPlatformBackingStore::FlushResult ritual_ZN29QOpenGLCompositorBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd(
    QOpenGLCompositorBackingStore *self,
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

//  const QPlatformTextureList *QOpenGLCompositorBackingStore::textures()
//      const
extern "C" Q_DECL_EXPORT
const QPlatformTextureList *ritual_ZNK29QOpenGLCompositorBackingStore8texturesEv(
    const QOpenGLCompositorBackingStore *self) {
  return self->textures();
}

//  void QOpenGLCompositorBackingStore::notifyComposited()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStore16notifyCompositedEv(
    QOpenGLCompositorBackingStore *self) {
  self->notifyComposited();
}

//  void QOpenGLCompositorBackingStore::updateTexture()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QOpenGLCompositorBackingStore13updateTextureEv(
    QOpenGLCompositorBackingStore *self) {
  self->updateTexture();
}

//  a Python function taken by a CuteQOpenGLCompositorBackingStore, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpenGLCompositorBackingStore(
    QOpenGLCompositorBackingStore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpenGLCompositorBackingStore *>(self)->take(key, call);
}

//  QPaintDevice *QOpenGLCompositorBackingStore::paintDevice()
extern "C" Q_DECL_EXPORT
QPaintDevice *ritual_own_ZN29QOpenGLCompositorBackingStore11paintDeviceEv(
    QOpenGLCompositorBackingStore *self) {
  return self->QOpenGLCompositorBackingStore::paintDevice();
}

//  void QOpenGLCompositorBackingStore::beginPaint(const QRegion &region)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QOpenGLCompositorBackingStore10beginPaintERK7QRegion(
    QOpenGLCompositorBackingStore *self,
    const QRegion *region) {
  self->QOpenGLCompositorBackingStore::beginPaint(*region);
}

//  void QOpenGLCompositorBackingStore::flush(QWindow *window, const QRegion
//      &region, const QPoint &offset)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QOpenGLCompositorBackingStore5flushEP7QWindowRK7QRegionRK6QPoint(
    QOpenGLCompositorBackingStore *self,
    QWindow *window,
    const QRegion *region,
    const QPoint *offset) {
  self->QOpenGLCompositorBackingStore::flush(window, *region, *offset);
}

//  void QOpenGLCompositorBackingStore::resize(const QSize &size, const
//      QRegion &staticContents)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QOpenGLCompositorBackingStore6resizeERK5QSizeRK7QRegion(
    QOpenGLCompositorBackingStore *self,
    const QSize *size,
    const QRegion *staticContents) {
  self->QOpenGLCompositorBackingStore::resize(*size, *staticContents);
}

//  QImage QOpenGLCompositorBackingStore::toImage() const
extern "C" Q_DECL_EXPORT
QImage *ritual_own_ZNK29QOpenGLCompositorBackingStore7toImageEv(
    const QOpenGLCompositorBackingStore *self) {
  return new QImage(self->QOpenGLCompositorBackingStore::toImage());
}

//  FlushResult QOpenGLCompositorBackingStore::rhiFlush(QWindow *window,
//      qreal sourceDevicePixelRatio, const QRegion &region, const QPoint
//      &offset, QPlatformTextureList *textures, bool translucentBackground,
//      qreal sourceTransformFactor)
extern "C" Q_DECL_EXPORT
QPlatformBackingStore::FlushResult ritual_own_ZN29QOpenGLCompositorBackingStore8rhiFlushEP7QWindowdRK7QRegionRK6QPointP20QPlatformTextureListbd(
    QOpenGLCompositorBackingStore *self,
    QWindow *window,
    qreal sourceDevicePixelRatio,
    const QRegion *region,
    const QPoint *offset,
    QPlatformTextureList *textures,
    bool translucentBackground,
    qreal sourceTransformFactor) {
  return self->QOpenGLCompositorBackingStore::rhiFlush(
      window,
      sourceDevicePixelRatio,
      *region,
      *offset,
      textures,
      translucentBackground,
      sourceTransformFactor);
}

#endif  // QT_CONFIG(egl)
