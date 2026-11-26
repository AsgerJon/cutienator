//  Written by dev_tooling.RitualGenerator from the records of
//  QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtMultimedia/6.12.0/QtMultimedia/private/qtmultimediaglobal_p.h>
#include <QtMultimedia/QtMultimedia>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtMultimedia/6.12.0/QtMultimedia/private/qsamplecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QFuture>
#include <QtCore/QUrl>
#include <optional>
#include <QtCore/QSpan>
#include <variant>
#include <QtCore/QByteArray>

//  A QSampleCache that Python can take functions over in. Every QSampleCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSampleCacheCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQSampleCacheCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSampleCacheCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSampleCacheCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSampleCacheCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSampleCacheCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQSampleCacheCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQSampleCache : public QSampleCache {
public:
  using QSampleCache::QSampleCache;
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
      CuteQSampleCacheCall0 call = reinterpret_cast<CuteQSampleCacheCall0>(taken[0]);
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
      CuteQSampleCacheCall1 call = reinterpret_cast<CuteQSampleCacheCall1>(taken[1]);
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
      CuteQSampleCacheCall2 call = reinterpret_cast<CuteQSampleCacheCall2>(taken[2]);
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
      CuteQSampleCacheCall3 call = reinterpret_cast<CuteQSampleCacheCall3>(taken[3]);
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
      CuteQSampleCacheCall4 call = reinterpret_cast<CuteQSampleCacheCall4>(taken[4]);
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
      CuteQSampleCacheCall5 call = reinterpret_cast<CuteQSampleCacheCall5>(taken[5]);
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
      CuteQSampleCacheCall6 call = reinterpret_cast<CuteQSampleCacheCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QSampleCache *QSampleCache::instance()
extern "C" Q_DECL_EXPORT
QSampleCache *ritual_ZN12QSampleCache8instanceEv() {
  return QSampleCache::instance();
}

//  QSampleCache::QSampleCache(QObject *parent)
extern "C" Q_DECL_EXPORT
QSampleCache *ritual_ZN12QSampleCacheC1EP7QObject(QObject *parent) {
  return new CuteQSampleCache(parent);
}

//  QSampleCache::~QSampleCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSampleCacheD1Ev(QSampleCache *self) {
  delete self;
}

//  QFuture<SharedSamplePtr> QSampleCache::requestSampleFuture(const QUrl
//      &a0, std::optional<int> targetSampleRate,
//      std::optional<SampleSourceType> forceSourceType)
extern "C" Q_DECL_EXPORT
QFuture<SharedSamplePtr> *ritual_ZN12QSampleCache19requestSampleFutureERK4QUrlSt8optionalIiES3_INS_16SampleSourceTypeEE(
    QSampleCache *self,
    const QUrl *a0,
    const std::optional<int> *targetSampleRate,
    const std::optional<QSampleCache::SampleSourceType> *forceSourceType) {
  return new QFuture<SharedSamplePtr>(
      self->requestSampleFuture(
          *a0,
          *targetSampleRate,
          *forceSourceType));
}

//  bool QSampleCache::isCached(const QUrl &url, std::optional<int>
//      targetSampleRate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QSampleCache8isCachedERK4QUrlSt8optionalIiE(
    const QSampleCache *self,
    const QUrl *url,
    const std::optional<int> *targetSampleRate) {
  return self->isCached(*url, *targetSampleRate);
}

//  SampleLoadResult QSampleCache::loadSample(QSpan<const char> a0)
extern "C" Q_DECL_EXPORT
QSampleCache::SampleLoadResult *ritual_ZN12QSampleCache10loadSampleE5QSpanIKcLm18446744073709551615EE(
    const QSpan<const char> *a0) {
  return new QSampleCache::SampleLoadResult(QSampleCache::loadSample(*a0));
}

//  SampleLoadResult QSampleCache::loadSampleViaDecoder(std::variant<QUrl,
//      QByteArray> a0)
extern "C" Q_DECL_EXPORT
QSampleCache::SampleLoadResult *ritual_ZN12QSampleCache20loadSampleViaDecoderESt7variantIJ4QUrl10QByteArrayEE(
    const std::variant<QUrl, QByteArray> *a0) {
  return new QSampleCache::SampleLoadResult(
      QSampleCache::loadSampleViaDecoder(
          *a0));
}

//  QFuture<SampleLoadResult>
//      QSampleCache::loadSampleAsyncViaDecoder(QByteArray a0)
extern "C" Q_DECL_EXPORT
QFuture<QSampleCache::SampleLoadResult> *ritual_ZN12QSampleCache25loadSampleAsyncViaDecoderE10QByteArray(
    const QByteArray *a0) {
  return new QFuture<QSampleCache::SampleLoadResult>(
      QSampleCache::loadSampleAsyncViaDecoder(
          *a0));
}

#if QT_CONFIG(thread)
//  QThreadPool *QSampleCache::threadPool()
extern "C" Q_DECL_EXPORT
QThreadPool *ritual_ZN12QSampleCache10threadPoolEv(QSampleCache *self) {
  return self->threadPool();
}
#endif  // QT_CONFIG(thread)

//  void QSampleCache::removeUnreferencedSample(const QUrl &a0,
//      std::optional<SampleRate> targetSampleRate)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSampleCache24removeUnreferencedSampleERK4QUrlSt8optionalIN19QtMultimediaPrivate10SampleRateEE(
    QSampleCache *self,
    const QUrl *a0,
    const std::optional<QSampleCache::SampleRate> *targetSampleRate) {
  self->removeUnreferencedSample(*a0, *targetSampleRate);
}

#if QT_CONFIG(thread)
//  SampleLoadResult QSampleCache::loadSample(const QUrl &a0,
//      std::optional<SampleSourceType> a1)
extern "C" Q_DECL_EXPORT
QSampleCache::SampleLoadResult *ritual_ZN12QSampleCache10loadSampleERK4QUrlSt8optionalINS_16SampleSourceTypeEE(
    const QUrl *a0,
    const std::optional<QSampleCache::SampleSourceType> *a1) {
  return new QSampleCache::SampleLoadResult(
      QSampleCache::loadSample(
          *a0,
          *a1));
}
#endif  // QT_CONFIG(thread)

//  QFuture<SampleLoadResult> QSampleCache::loadSampleAsync(const QUrl &a0,
//      std::optional<SampleSourceType> a1)
extern "C" Q_DECL_EXPORT
QFuture<QSampleCache::SampleLoadResult> *ritual_ZN12QSampleCache15loadSampleAsyncERK4QUrlSt8optionalINS_16SampleSourceTypeEE(
    QSampleCache *self,
    const QUrl *a0,
    const std::optional<QSampleCache::SampleSourceType> *a1) {
  return new QFuture<QSampleCache::SampleLoadResult>(
      self->loadSampleAsync(
          *a0,
          *a1));
}

//  a Python function taken by a CuteQSampleCache, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSampleCache(
    QSampleCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSampleCache *>(self)->take(key, call);
}

//  a QFuture<SharedSamplePtr> a ritual of QSampleCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSampleCache__QFuture_SharedSamplePtr(
    QFuture<SharedSamplePtr> *self) {
  delete self;
}

//  a QSampleCache::SampleLoadResult a ritual of QSampleCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSampleCache__QSampleCache_SampleLoadResult(
    QSampleCache::SampleLoadResult *self) {
  delete self;
}

//  a QFuture<QSampleCache::SampleLoadResult> a ritual of QSampleCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QSampleCache__QFuture_QSampleCache_SampleLoadResult(
    QFuture<QSampleCache::SampleLoadResult> *self) {
  delete self;
}
