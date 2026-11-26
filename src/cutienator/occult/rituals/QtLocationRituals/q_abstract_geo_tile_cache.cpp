//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qabstractgeotilecache_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qabstractgeotilecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#include <QtCore/QSharedPointer>

//  A QAbstractGeoTileCache that Python can take functions over in. Every QAbstractGeoTileCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQAbstractGeoTileCacheCall0)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall1)(const void *, int *);
typedef int (*CuteQAbstractGeoTileCacheCall2)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall3)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall4)(const void *, int *);
typedef int (*CuteQAbstractGeoTileCacheCall5)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall6)(const void *, int, int *);
typedef void (*CuteQAbstractGeoTileCacheCall7)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall8)(const void *, int *);
typedef int (*CuteQAbstractGeoTileCacheCall9)(const void *, int *);
typedef int (*CuteQAbstractGeoTileCacheCall10)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall11)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall12)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall13)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall14)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall15)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall16)(const void *, int, int *);
typedef int (*CuteQAbstractGeoTileCacheCall17)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall18)(const void *, const QGeoTileSpec *, const QByteArray *, const QString *, int, int *);
typedef void (*CuteQAbstractGeoTileCacheCall19)(const void *, const QGeoTileSpec *, const QString *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall20)(const void *, int *);
typedef void (*CuteQAbstractGeoTileCacheCall21)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractGeoTileCacheCall22)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractGeoTileCacheCall23)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractGeoTileCacheCall24)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractGeoTileCacheCall25)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractGeoTileCacheCall26)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractGeoTileCacheCall27)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractGeoTileCacheCall28)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractGeoTileCache : public QAbstractGeoTileCache {
public:
  using QAbstractGeoTileCache::QAbstractGeoTileCache;
  void *taken[29] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache12maxDiskUsageEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache9diskUsageEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache11memoryUsageEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache18setMinTextureUsageEi")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache20setExtraTextureUsageEi")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache15maxTextureUsageEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache15minTextureUsageEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache12textureUsageEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache8clearAllEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache19setCostStrategyDiskENS_12CostStrategyE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache16costStrategyDiskEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache21setCostStrategyMemoryENS_12CostStrategyE")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache18costStrategyMemoryEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache22setCostStrategyTextureENS_12CostStrategyE")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractGeoTileCache19costStrategyTextureEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache6insertERK12QGeoTileSpecRK10QByteArrayRK7QString6QFlagsINS_9CacheAreaEE")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache4initEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache10printStatsEv")) {
      taken[21] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[22] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[24] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QAbstractGeoTileCache::setMaxDiskUsage(int diskUsage)
  void setMaxDiskUsage(int diskUsage) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall0 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall0>(taken[0]);
      call(this, diskUsage, &handled);
      if (handled) return;
    }
    QAbstractGeoTileCache::setMaxDiskUsage(diskUsage);
  }

  //  int QAbstractGeoTileCache::maxDiskUsage() const
  int maxDiskUsage() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall1 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractGeoTileCache::maxDiskUsage();
  }

  //  int QAbstractGeoTileCache::diskUsage() const
  int diskUsage() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall2 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractGeoTileCache::diskUsage();
  }

  //  void QAbstractGeoTileCache::setMaxMemoryUsage(int memoryUsage)
  void setMaxMemoryUsage(int memoryUsage) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall3 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall3>(taken[3]);
      call(this, memoryUsage, &handled);
      if (handled) return;
    }
    QAbstractGeoTileCache::setMaxMemoryUsage(memoryUsage);
  }

  //  int QAbstractGeoTileCache::maxMemoryUsage() const
  int maxMemoryUsage() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall4 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractGeoTileCache::maxMemoryUsage();
  }

  //  int QAbstractGeoTileCache::memoryUsage() const
  int memoryUsage() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall5 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractGeoTileCache::memoryUsage();
  }

  //  void QAbstractGeoTileCache::setMinTextureUsage(int textureUsage)
  void setMinTextureUsage(int textureUsage) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall6 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall6>(taken[6]);
      call(this, textureUsage, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractGeoTileCache::setExtraTextureUsage(int textureUsage)
  void setExtraTextureUsage(int textureUsage) override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall7 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall7>(taken[7]);
      call(this, textureUsage, &handled);
      if (handled) return;
    }
  }

  //  int QAbstractGeoTileCache::maxTextureUsage() const
  int maxTextureUsage() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall8 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractGeoTileCache::minTextureUsage() const
  int minTextureUsage() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall9 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  int QAbstractGeoTileCache::textureUsage() const
  int textureUsage() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall10 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  void QAbstractGeoTileCache::clearAll()
  void clearAll() override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall11 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractGeoTileCache::setCostStrategyDisk(CostStrategy
  //      costStrategy)
  void setCostStrategyDisk(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall12 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall12>(taken[12]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
  }

  //  CostStrategy QAbstractGeoTileCache::costStrategyDisk() const
  QAbstractGeoTileCache::CostStrategy costStrategyDisk() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall13 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return {};
  }

  //  void QAbstractGeoTileCache::setCostStrategyMemory(CostStrategy
  //      costStrategy)
  void setCostStrategyMemory(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall14 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall14>(taken[14]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
  }

  //  CostStrategy QAbstractGeoTileCache::costStrategyMemory() const
  QAbstractGeoTileCache::CostStrategy costStrategyMemory() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall15 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return {};
  }

  //  void QAbstractGeoTileCache::setCostStrategyTexture(CostStrategy
  //      costStrategy)
  void setCostStrategyTexture(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[16]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall16 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall16>(taken[16]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
  }

  //  CostStrategy QAbstractGeoTileCache::costStrategyTexture() const
  QAbstractGeoTileCache::CostStrategy costStrategyTexture() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall17 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return {};
  }

  //  void QAbstractGeoTileCache::insert(const QGeoTileSpec &spec, const
  //      QByteArray &bytes, const QString &format,
  //      QAbstractGeoTileCache::CacheAreas areas)
  void insert(
      const QGeoTileSpec &spec,
      const QByteArray &bytes,
      const QString &format,
      QAbstractGeoTileCache::CacheAreas areas) override {
    if (taken[18]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall18 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall18>(taken[18]);
      call(this, &spec, &bytes, &format, static_cast<int>(areas.toInt()), &handled);
      if (handled) return;
    }
  }

  //  void QAbstractGeoTileCache::handleError(const QGeoTileSpec &spec,
  //      const QString &errorString)
  void handleError(
      const QGeoTileSpec &spec,
      const QString &errorString) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall19 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall19>(taken[19]);
      call(this, &spec, &errorString, &handled);
      if (handled) return;
    }
    QAbstractGeoTileCache::handleError(spec, errorString);
  }

  //  void QAbstractGeoTileCache::init()
  void init() override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall20 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractGeoTileCache::printStats()
  void printStats() override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall21 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall22 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall22>(taken[22]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall23 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall23>(taken[23]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall24 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall25 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall25>(taken[25]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall26 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall27 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall27>(taken[27]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractGeoTileCacheCall28 call = reinterpret_cast<CuteQAbstractGeoTileCacheCall28>(taken[28]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractGeoTileCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractGeoTileCache10metaObjectEv(
    const QAbstractGeoTileCache *self) {
  return self->metaObject();
}

//  void *QAbstractGeoTileCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QAbstractGeoTileCache11qt_metacastEPKc(
    QAbstractGeoTileCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractGeoTileCache::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QAbstractGeoTileCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractGeoTileCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractGeoTileCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractGeoTileCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractGeoTileCache::tr(s, c, n));
}

//  QAbstractGeoTileCache::~QAbstractGeoTileCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCacheD1Ev(QAbstractGeoTileCache *self) {
  delete self;
}

//  void QAbstractGeoTileCache::setMaxDiskUsage(int diskUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi(
    QAbstractGeoTileCache *self,
    int diskUsage) {
  self->setMaxDiskUsage(diskUsage);
}

//  int QAbstractGeoTileCache::maxDiskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache12maxDiskUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->maxDiskUsage();
}

//  int QAbstractGeoTileCache::diskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache9diskUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->diskUsage();
}

//  void QAbstractGeoTileCache::setMaxMemoryUsage(int memoryUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi(
    QAbstractGeoTileCache *self,
    int memoryUsage) {
  self->setMaxMemoryUsage(memoryUsage);
}

//  int QAbstractGeoTileCache::maxMemoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->maxMemoryUsage();
}

//  int QAbstractGeoTileCache::memoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache11memoryUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->memoryUsage();
}

//  void QAbstractGeoTileCache::setMinTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache18setMinTextureUsageEi(
    QAbstractGeoTileCache *self,
    int textureUsage) {
  self->setMinTextureUsage(textureUsage);
}

//  void QAbstractGeoTileCache::setExtraTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache20setExtraTextureUsageEi(
    QAbstractGeoTileCache *self,
    int textureUsage) {
  self->setExtraTextureUsage(textureUsage);
}

//  int QAbstractGeoTileCache::maxTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache15maxTextureUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->maxTextureUsage();
}

//  int QAbstractGeoTileCache::minTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache15minTextureUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->minTextureUsage();
}

//  int QAbstractGeoTileCache::textureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QAbstractGeoTileCache12textureUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->textureUsage();
}

//  void QAbstractGeoTileCache::clearAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache8clearAllEv(
    QAbstractGeoTileCache *self) {
  self->clearAll();
}

//  void QAbstractGeoTileCache::setCostStrategyDisk(CostStrategy
//      costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache19setCostStrategyDiskENS_12CostStrategyE(
    QAbstractGeoTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyDisk(costStrategy);
}

//  CostStrategy QAbstractGeoTileCache::costStrategyDisk() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK21QAbstractGeoTileCache16costStrategyDiskEv(
    const QAbstractGeoTileCache *self) {
  return self->costStrategyDisk();
}

//  void QAbstractGeoTileCache::setCostStrategyMemory(CostStrategy
//      costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache21setCostStrategyMemoryENS_12CostStrategyE(
    QAbstractGeoTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyMemory(costStrategy);
}

//  CostStrategy QAbstractGeoTileCache::costStrategyMemory() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK21QAbstractGeoTileCache18costStrategyMemoryEv(
    const QAbstractGeoTileCache *self) {
  return self->costStrategyMemory();
}

//  void QAbstractGeoTileCache::setCostStrategyTexture(CostStrategy
//      costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache22setCostStrategyTextureENS_12CostStrategyE(
    QAbstractGeoTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyTexture(costStrategy);
}

//  CostStrategy QAbstractGeoTileCache::costStrategyTexture() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK21QAbstractGeoTileCache19costStrategyTextureEv(
    const QAbstractGeoTileCache *self) {
  return self->costStrategyTexture();
}

//  QSharedPointer<QGeoTileTexture> QAbstractGeoTileCache::get(const
//      QGeoTileSpec &spec)
extern "C" Q_DECL_EXPORT
QSharedPointer<QGeoTileTexture> *ritual_ZN21QAbstractGeoTileCache3getERK12QGeoTileSpec(
    QAbstractGeoTileCache *self,
    const QGeoTileSpec *spec) {
  return new QSharedPointer<QGeoTileTexture>(self->get(*spec));
}

//  void QAbstractGeoTileCache::insert(const QGeoTileSpec &spec, const
//      QByteArray &bytes, const QString &format,
//      QAbstractGeoTileCache::CacheAreas areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache6insertERK12QGeoTileSpecRK10QByteArrayRK7QString6QFlagsINS_9CacheAreaEE(
    QAbstractGeoTileCache *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format,
    int areas) {
  self->insert(
      *spec,
      *bytes,
      *format,
      QFlags<QAbstractGeoTileCache::CacheArea>::fromInt(areas));
}

//  void QAbstractGeoTileCache::handleError(const QGeoTileSpec &spec, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7QString(
    QAbstractGeoTileCache *self,
    const QGeoTileSpec *spec,
    const QString *errorString) {
  self->handleError(*spec, *errorString);
}

//  void QAbstractGeoTileCache::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache4initEv(QAbstractGeoTileCache *self) {
  self->init();
}

//  QString QAbstractGeoTileCache::baseCacheDirectory()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractGeoTileCache18baseCacheDirectoryEv() {
  return new QString(QAbstractGeoTileCache::baseCacheDirectory());
}

//  QString QAbstractGeoTileCache::baseLocationCacheDirectory()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractGeoTileCache26baseLocationCacheDirectoryEv() {
  return new QString(QAbstractGeoTileCache::baseLocationCacheDirectory());
}

//  void QAbstractGeoTileCache::printStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractGeoTileCache10printStatsEv(
    QAbstractGeoTileCache *self) {
  self->printStats();
}

//  a Python function taken by a CuteQAbstractGeoTileCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractGeoTileCache(
    QAbstractGeoTileCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractGeoTileCache *>(self)->take(key, call);
}

//  void QAbstractGeoTileCache::setMaxDiskUsage(int diskUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractGeoTileCache15setMaxDiskUsageEi(
    QAbstractGeoTileCache *self,
    int diskUsage) {
  self->QAbstractGeoTileCache::setMaxDiskUsage(diskUsage);
}

//  int QAbstractGeoTileCache::maxDiskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAbstractGeoTileCache12maxDiskUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->QAbstractGeoTileCache::maxDiskUsage();
}

//  int QAbstractGeoTileCache::diskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAbstractGeoTileCache9diskUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->QAbstractGeoTileCache::diskUsage();
}

//  void QAbstractGeoTileCache::setMaxMemoryUsage(int memoryUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractGeoTileCache17setMaxMemoryUsageEi(
    QAbstractGeoTileCache *self,
    int memoryUsage) {
  self->QAbstractGeoTileCache::setMaxMemoryUsage(memoryUsage);
}

//  int QAbstractGeoTileCache::maxMemoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAbstractGeoTileCache14maxMemoryUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->QAbstractGeoTileCache::maxMemoryUsage();
}

//  int QAbstractGeoTileCache::memoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK21QAbstractGeoTileCache11memoryUsageEv(
    const QAbstractGeoTileCache *self) {
  return self->QAbstractGeoTileCache::memoryUsage();
}

//  void QAbstractGeoTileCache::handleError(const QGeoTileSpec &spec, const
//      QString &errorString)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7QString(
    QAbstractGeoTileCache *self,
    const QGeoTileSpec *spec,
    const QString *errorString) {
  self->QAbstractGeoTileCache::handleError(*spec, *errorString);
}

//  a QSharedPointer<QGeoTileTexture> a ritual of QAbstractGeoTileCache gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QAbstractGeoTileCache__QSharedPointer_QGeoTileTexture(
    QSharedPointer<QGeoTileTexture> *self) {
  delete self;
}
