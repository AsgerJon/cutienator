//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmappingmanagerengine_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmappingmanagerengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGeoTiledMappingManagerEngine may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoTiledMappingManagerEngine : QGeoTiledMappingManagerEngine {
  using QGeoTiledMappingManagerEngine::engineTileFinished;
  using QGeoTiledMappingManagerEngine::engineTileError;
};

//  A QGeoTiledMappingManagerEngine that Python can take functions over in. Every QGeoTiledMappingManagerEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQGeoTiledMappingManagerEngineCall0)(const void *, int *);
typedef void (*CuteQGeoTiledMappingManagerEngineCall1)(const void *, const QGeoTileSpec *, const QByteArray *, const QString *, int *);
typedef void (*CuteQGeoTiledMappingManagerEngineCall2)(const void *, const QGeoTileSpec *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMappingManagerEngineCall3)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoTiledMappingManagerEngineCall4)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMappingManagerEngineCall5)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMappingManagerEngineCall6)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMappingManagerEngineCall7)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMappingManagerEngineCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoTiledMappingManagerEngineCall9)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoTiledMappingManagerEngine : public QGeoTiledMappingManagerEngine {
public:
  using QGeoTiledMappingManagerEngine::QGeoTiledMappingManagerEngine;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QGeoMappingManagerEngine9createMapEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QGeoTiledMappingManagerEngine18engineTileFinishedERK12QGeoTileSpecRK10QByteArrayRK7QString")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK12QGeoTileSpecRK7QString")) {
      taken[2] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QGeoMap *QGeoTiledMappingManagerEngine::createMap()
  QGeoMap *createMap() override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall0 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoMap *>(given);
    }
    return QGeoTiledMappingManagerEngine::createMap();
  }

  //  void QGeoTiledMappingManagerEngine::engineTileFinished(const
  //      QGeoTileSpec &spec, const QByteArray &bytes, const QString
  //      &format)
  void engineTileFinished(
      const QGeoTileSpec &spec,
      const QByteArray &bytes,
      const QString &format) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall1 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall1>(taken[1]);
      call(this, &spec, &bytes, &format, &handled);
      if (handled) return;
    }
    QGeoTiledMappingManagerEngine::engineTileFinished(spec, bytes, format);
  }

  //  void QGeoTiledMappingManagerEngine::engineTileError(const
  //      QGeoTileSpec &spec, const QString &errorString)
  void engineTileError(
      const QGeoTileSpec &spec,
      const QString &errorString) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall2 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall2>(taken[2]);
      call(this, &spec, &errorString, &handled);
      if (handled) return;
    }
    QGeoTiledMappingManagerEngine::engineTileError(spec, errorString);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall3 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall3>(taken[3]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall4 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall4>(taken[4]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall5 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall6 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall7 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall8 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoTiledMappingManagerEngineCall9 call = reinterpret_cast<CuteQGeoTiledMappingManagerEngineCall9>(taken[9]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoTiledMappingManagerEngine::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK29QGeoTiledMappingManagerEngine10metaObjectEv(
    const QGeoTiledMappingManagerEngine *self) {
  return self->metaObject();
}

//  QString QGeoTiledMappingManagerEngine::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN29QGeoTiledMappingManagerEngine2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoTiledMappingManagerEngine::tr(s, c, n));
}

//  QGeoTiledMappingManagerEngine::QGeoTiledMappingManagerEngine(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoTiledMappingManagerEngine *ritual_ZN29QGeoTiledMappingManagerEngineC1EP7QObject(
    QObject *parent) {
  return new CuteQGeoTiledMappingManagerEngine(parent);
}

//  QGeoTiledMappingManagerEngine::~QGeoTiledMappingManagerEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngineD1Ev(
    QGeoTiledMappingManagerEngine *self) {
  delete self;
}

//  QGeoTileFetcher *QGeoTiledMappingManagerEngine::tileFetcher()
extern "C" Q_DECL_EXPORT
QGeoTileFetcher *ritual_ZN29QGeoTiledMappingManagerEngine11tileFetcherEv(
    QGeoTiledMappingManagerEngine *self) {
  return self->tileFetcher();
}

//  QGeoMap *QGeoTiledMappingManagerEngine::createMap()
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_ZN29QGeoTiledMappingManagerEngine9createMapEv(
    QGeoTiledMappingManagerEngine *self) {
  return self->createMap();
}

//  void QGeoTiledMappingManagerEngine::releaseMap(QGeoTiledMap *map)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine10releaseMapEP12QGeoTiledMap(
    QGeoTiledMappingManagerEngine *self,
    QGeoTiledMap *map) {
  self->releaseMap(map);
}

//  QSize QGeoTiledMappingManagerEngine::tileSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK29QGeoTiledMappingManagerEngine8tileSizeEv(
    const QGeoTiledMappingManagerEngine *self) {
  return new QSize(self->tileSize());
}

//  int QGeoTiledMappingManagerEngine::tileVersion() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QGeoTiledMappingManagerEngine11tileVersionEv(
    const QGeoTiledMappingManagerEngine *self) {
  return self->tileVersion();
}

//  QAbstractGeoTileCache *QGeoTiledMappingManagerEngine::tileCache()
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache *ritual_ZN29QGeoTiledMappingManagerEngine9tileCacheEv(
    QGeoTiledMappingManagerEngine *self) {
  return self->tileCache();
}

//  QAbstractGeoTileCache::CacheAreas
//      QGeoTiledMappingManagerEngine::cacheHint() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK29QGeoTiledMappingManagerEngine9cacheHintEv(
    const QGeoTiledMappingManagerEngine *self) {
  return static_cast<int>(self->cacheHint().toInt());
}

//  void QGeoTiledMappingManagerEngine::engineTileFinished(const QGeoTileSpec
//      &spec, const QByteArray &bytes, const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine18engineTileFinishedERK12QGeoTileSpecRK10QByteArrayRK7QString(
    QGeoTiledMappingManagerEngine *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format) {
  self->engineTileFinished(*spec, *bytes, *format);
}

//  void QGeoTiledMappingManagerEngine::engineTileError(const QGeoTileSpec
//      &spec, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK12QGeoTileSpecRK7QString(
    QGeoTiledMappingManagerEngine *self,
    const QGeoTileSpec *spec,
    const QString *errorString) {
  self->engineTileError(*spec, *errorString);
}

//  void QGeoTiledMappingManagerEngine::setTileFetcher(QGeoTileFetcher
//      *fetcher)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine14setTileFetcherEP15QGeoTileFetcher(
    QGeoTiledMappingManagerEngine *self,
    QGeoTileFetcher *fetcher) {
  self->setTileFetcher(fetcher);
}

//  void QGeoTiledMappingManagerEngine::setTileSize(const QSize &tileSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine11setTileSizeERK5QSize(
    QGeoTiledMappingManagerEngine *self,
    const QSize *tileSize) {
  self->setTileSize(*tileSize);
}

//  void QGeoTiledMappingManagerEngine::setTileVersion(int version)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine14setTileVersionEi(
    QGeoTiledMappingManagerEngine *self,
    int version) {
  self->setTileVersion(version);
}

//  void QGeoTiledMappingManagerEngine::setCacheHint(QAbstractGeoTileCache::C
//      acheAreas cacheHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine12setCacheHintE6QFlagsIN21QAbstractGeoTileCache9CacheAreaEE(
    QGeoTiledMappingManagerEngine *self,
    int cacheHint) {
  self->setCacheHint(
      QFlags<QAbstractGeoTileCache::CacheArea>::fromInt(cacheHint));
}

//  void QGeoTiledMappingManagerEngine::setTileCache(QAbstractGeoTileCache
//      *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QGeoTiledMappingManagerEngine12setTileCacheEP21QAbstractGeoTileCache(
    QGeoTiledMappingManagerEngine *self,
    QAbstractGeoTileCache *cache) {
  self->setTileCache(cache);
}

//  QGeoTiledMappingManagerEnginePrivate
//      *QGeoTiledMappingManagerEngine::d_func()
extern "C" Q_DECL_EXPORT
QGeoTiledMappingManagerEnginePrivate *ritual_ZN29QGeoTiledMappingManagerEngine6d_funcEv(
    QGeoTiledMappingManagerEngine *self) {
  return self->d_func();
}

//  const QGeoTiledMappingManagerEnginePrivate
//      *QGeoTiledMappingManagerEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoTiledMappingManagerEnginePrivate *ritual_ZNK29QGeoTiledMappingManagerEngine6d_funcEv(
    const QGeoTiledMappingManagerEngine *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGeoTiledMappingManagerEngine, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoTiledMappingManagerEngine(
    QGeoTiledMappingManagerEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoTiledMappingManagerEngine *>(self)->take(key, call);
}

//  QGeoMap *QGeoTiledMappingManagerEngine::createMap()
extern "C" Q_DECL_EXPORT
QGeoMap *ritual_own_ZN29QGeoTiledMappingManagerEngine9createMapEv(
    QGeoTiledMappingManagerEngine *self) {
  return self->QGeoTiledMappingManagerEngine::createMap();
}

//  void QGeoTiledMappingManagerEngine::engineTileFinished(const QGeoTileSpec
//      &spec, const QByteArray &bytes, const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QGeoTiledMappingManagerEngine18engineTileFinishedERK12QGeoTileSpecRK10QByteArrayRK7QString(
    QGeoTiledMappingManagerEngine *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format) {
  static_cast<OwnQGeoTiledMappingManagerEngine *>(self)->OwnQGeoTiledMappingManagerEngine::engineTileFinished(
      *spec,
      *bytes,
      *format);
}

//  void QGeoTiledMappingManagerEngine::engineTileError(const QGeoTileSpec
//      &spec, const QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN29QGeoTiledMappingManagerEngine15engineTileErrorERK12QGeoTileSpecRK7QString(
    QGeoTiledMappingManagerEngine *self,
    const QGeoTileSpec *spec,
    const QString *errorString) {
  static_cast<OwnQGeoTiledMappingManagerEngine *>(self)->OwnQGeoTiledMappingManagerEngine::engineTileError(
      *spec,
      *errorString);
}
