//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/qpa/qplatformsharedgraphicscache.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformsharedgraphicscache.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/qimage.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QPlatformSharedGraphicsCache that Python can take functions over in. Every QPlatformSharedGraphicsCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQPlatformSharedGraphicsCacheCall0)(const void *, int *);
typedef void (*CuteQPlatformSharedGraphicsCacheCall1)(const void *, const QByteArray *, int, int, int *);
typedef void (*CuteQPlatformSharedGraphicsCacheCall2)(const void *, int *);
typedef bool (*CuteQPlatformSharedGraphicsCacheCall3)(const void *, int *);
typedef uint (*CuteQPlatformSharedGraphicsCacheCall4)(const void *, void *, int *);
typedef void (*CuteQPlatformSharedGraphicsCacheCall5)(const void *, void *, int *);
typedef bool (*CuteQPlatformSharedGraphicsCacheCall6)(const void *, void *, int *);
typedef const QSize * (*CuteQPlatformSharedGraphicsCacheCall7)(const void *, void *, int *);
typedef void * (*CuteQPlatformSharedGraphicsCacheCall8)(const void *, void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformSharedGraphicsCacheCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPlatformSharedGraphicsCacheCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSharedGraphicsCacheCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSharedGraphicsCacheCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSharedGraphicsCacheCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSharedGraphicsCacheCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPlatformSharedGraphicsCacheCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPlatformSharedGraphicsCache : public QPlatformSharedGraphicsCache {
public:
  using QPlatformSharedGraphicsCache::QPlatformSharedGraphicsCache;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache17beginRequestBatchEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache22ensureCacheInitializedERK10QByteArrayNS_10BufferTypeENS_11PixelFormatE")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache15endRequestBatchEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK28QPlatformSharedGraphicsCache19requestBatchStartedEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache18textureIdForBufferEPv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache15referenceBufferEPv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache17dereferenceBufferEPv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache12sizeOfBufferEPv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN28QPlatformSharedGraphicsCache17eglImageForBufferEPv")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QPlatformSharedGraphicsCache::beginRequestBatch()
  void beginRequestBatch() override {
    if (taken[0]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall0 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QPlatformSharedGraphicsCache::ensureCacheInitialized(const
  //      QByteArray &cacheId, BufferType bufferType, PixelFormat
  //      pixelFormat)
  void ensureCacheInitialized(
      const QByteArray &cacheId,
      QPlatformSharedGraphicsCache::BufferType bufferType,
      QPlatformSharedGraphicsCache::PixelFormat pixelFormat) override {
    if (taken[1]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall1 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall1>(taken[1]);
      call(this, &cacheId, static_cast<int>(bufferType), static_cast<int>(pixelFormat), &handled);
      if (handled) return;
    }
  }

  //  void QPlatformSharedGraphicsCache::endRequestBatch()
  void endRequestBatch() override {
    if (taken[2]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall2 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformSharedGraphicsCache::requestBatchStarted() const
  bool requestBatchStarted() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall3 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  uint QPlatformSharedGraphicsCache::textureIdForBuffer(void *bufferId)
  uint textureIdForBuffer(void *bufferId) override {
    if (taken[4]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall4 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall4>(taken[4]);
      uint given = call(this, bufferId, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QPlatformSharedGraphicsCache::referenceBuffer(void *bufferId)
  void referenceBuffer(void *bufferId) override {
    if (taken[5]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall5 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall5>(taken[5]);
      call(this, bufferId, &handled);
      if (handled) return;
    }
  }

  //  bool QPlatformSharedGraphicsCache::dereferenceBuffer(void *bufferId)
  bool dereferenceBuffer(void *bufferId) override {
    if (taken[6]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall6 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall6>(taken[6]);
      bool given = call(this, bufferId, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void *bufferId)
  QSize sizeOfBuffer(void *bufferId) override {
    if (taken[7]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall7 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall7>(taken[7]);
      const QSize * given = call(this, bufferId, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void *QPlatformSharedGraphicsCache::eglImageForBuffer(void *bufferId)
  void *eglImageForBuffer(void *bufferId) override {
    if (taken[8]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall8 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall8>(taken[8]);
      void * given = call(this, bufferId, &handled);
      if (handled) return static_cast<void *>(given);
    }
    return {};
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall9 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall10 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall11 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall12 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall13 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall14 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQPlatformSharedGraphicsCacheCall15 call = reinterpret_cast<CuteQPlatformSharedGraphicsCacheCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPlatformSharedGraphicsCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QPlatformSharedGraphicsCache10metaObjectEv(
    const QPlatformSharedGraphicsCache *self) {
  return self->metaObject();
}

//  void *QPlatformSharedGraphicsCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QPlatformSharedGraphicsCache11qt_metacastEPKc(
    QPlatformSharedGraphicsCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPlatformSharedGraphicsCache::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QPlatformSharedGraphicsCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QPlatformSharedGraphicsCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPlatformSharedGraphicsCache::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QPlatformSharedGraphicsCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPlatformSharedGraphicsCache::tr(s, c, n));
}

//  void QPlatformSharedGraphicsCache::beginRequestBatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache17beginRequestBatchEv(
    QPlatformSharedGraphicsCache *self) {
  self->beginRequestBatch();
}

//  void QPlatformSharedGraphicsCache::ensureCacheInitialized(const
//      QByteArray &cacheId, BufferType bufferType, PixelFormat pixelFormat)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache22ensureCacheInitializedERK10QByteArrayNS_10BufferTypeENS_11PixelFormatE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    QPlatformSharedGraphicsCache::BufferType bufferType,
    QPlatformSharedGraphicsCache::PixelFormat pixelFormat) {
  self->ensureCacheInitialized(*cacheId, bufferType, pixelFormat);
}

//  void QPlatformSharedGraphicsCache::requestItems(const QByteArray
//      &cacheId, const QList<quint32> &itemIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache12requestItemsERK10QByteArrayRK5QListIjE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    const QList<quint32> *itemIds) {
  self->requestItems(*cacheId, *itemIds);
}

//  void QPlatformSharedGraphicsCache::insertItems(const QByteArray &cacheId,
//      const QList<quint32> &itemIds, const QList<QImage> &items)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache11insertItemsERK10QByteArrayRK5QListIjERKS3_I6QImageE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    const QList<quint32> *itemIds,
    const QList<QImage> *items) {
  self->insertItems(*cacheId, *itemIds, *items);
}

//  void QPlatformSharedGraphicsCache::releaseItems(const QByteArray
//      &cacheId, const QList<quint32> &itemIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache12releaseItemsERK10QByteArrayRK5QListIjE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    const QList<quint32> *itemIds) {
  self->releaseItems(*cacheId, *itemIds);
}

//  void QPlatformSharedGraphicsCache::endRequestBatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache15endRequestBatchEv(
    QPlatformSharedGraphicsCache *self) {
  self->endRequestBatch();
}

//  bool QPlatformSharedGraphicsCache::requestBatchStarted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QPlatformSharedGraphicsCache19requestBatchStartedEv(
    const QPlatformSharedGraphicsCache *self) {
  return self->requestBatchStarted();
}

//  uint QPlatformSharedGraphicsCache::textureIdForBuffer(void *bufferId)
extern "C" Q_DECL_EXPORT
uint ritual_ZN28QPlatformSharedGraphicsCache18textureIdForBufferEPv(
    QPlatformSharedGraphicsCache *self,
    void *bufferId) {
  return self->textureIdForBuffer(bufferId);
}

//  void QPlatformSharedGraphicsCache::referenceBuffer(void *bufferId)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache15referenceBufferEPv(
    QPlatformSharedGraphicsCache *self,
    void *bufferId) {
  self->referenceBuffer(bufferId);
}

//  bool QPlatformSharedGraphicsCache::dereferenceBuffer(void *bufferId)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QPlatformSharedGraphicsCache17dereferenceBufferEPv(
    QPlatformSharedGraphicsCache *self,
    void *bufferId) {
  return self->dereferenceBuffer(bufferId);
}

//  QSize QPlatformSharedGraphicsCache::sizeOfBuffer(void *bufferId)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN28QPlatformSharedGraphicsCache12sizeOfBufferEPv(
    QPlatformSharedGraphicsCache *self,
    void *bufferId) {
  return new QSize(self->sizeOfBuffer(bufferId));
}

//  void *QPlatformSharedGraphicsCache::eglImageForBuffer(void *bufferId)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QPlatformSharedGraphicsCache17eglImageForBufferEPv(
    QPlatformSharedGraphicsCache *self,
    void *bufferId) {
  return self->eglImageForBuffer(bufferId);
}

//  void QPlatformSharedGraphicsCache::itemsMissing(const QByteArray
//      &cacheId, const QList<quint32> &itemIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache12itemsMissingERK10QByteArrayRK5QListIjE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    const QList<quint32> *itemIds) {
  self->itemsMissing(*cacheId, *itemIds);
}

//  void QPlatformSharedGraphicsCache::itemsAvailable(const QByteArray
//      &cacheId, void *bufferId, const QList<quint32> &itemIds, const
//      QList<QPoint> &positionsInBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache14itemsAvailableERK10QByteArrayPvRK5QListIjERKS4_I6QPointE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    void *bufferId,
    const QList<quint32> *itemIds,
    const QList<QPoint> *positionsInBuffer) {
  self->itemsAvailable(*cacheId, bufferId, *itemIds, *positionsInBuffer);
}

//  void QPlatformSharedGraphicsCache::itemsInvalidated(const QByteArray
//      &cacheId, const QList<quint32> &itemIds)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache16itemsInvalidatedERK10QByteArrayRK5QListIjE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    const QList<quint32> *itemIds) {
  self->itemsInvalidated(*cacheId, *itemIds);
}

//  void QPlatformSharedGraphicsCache::itemsUpdated(const QByteArray
//      &cacheId, void *bufferId, const QList<quint32> &itemIds, const
//      QList<QPoint> &positionsInBuffer)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QPlatformSharedGraphicsCache12itemsUpdatedERK10QByteArrayPvRK5QListIjERKS4_I6QPointE(
    QPlatformSharedGraphicsCache *self,
    const QByteArray *cacheId,
    void *bufferId,
    const QList<quint32> *itemIds,
    const QList<QPoint> *positionsInBuffer) {
  self->itemsUpdated(*cacheId, bufferId, *itemIds, *positionsInBuffer);
}

//  a Python function taken by a CuteQPlatformSharedGraphicsCache, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPlatformSharedGraphicsCache(
    QPlatformSharedGraphicsCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPlatformSharedGraphicsCache *>(self)->take(key, call);
}
