//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QGeoFileTileCache may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGeoFileTileCache : QGeoFileTileCache {
  using QGeoFileTileCache::init;
  using QGeoFileTileCache::printStats;
  using QGeoFileTileCache::isTileBogus;
  using QGeoFileTileCache::tileSpecToFilename;
  using QGeoFileTileCache::filenameToTileSpec;
};

//  A QGeoFileTileCache that Python can take functions over in. Every QGeoFileTileCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQGeoFileTileCacheCall0)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall1)(const void *, int *);
typedef int (*CuteQGeoFileTileCacheCall2)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall3)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall4)(const void *, int *);
typedef int (*CuteQGeoFileTileCacheCall5)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall6)(const void *, int, int *);
typedef void (*CuteQGeoFileTileCacheCall7)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall8)(const void *, int *);
typedef int (*CuteQGeoFileTileCacheCall9)(const void *, int *);
typedef int (*CuteQGeoFileTileCacheCall10)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall11)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall12)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall13)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall14)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall15)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall16)(const void *, int, int *);
typedef int (*CuteQGeoFileTileCacheCall17)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall18)(const void *, const QGeoTileSpec *, const QByteArray *, const QString *, int, int *);
typedef void (*CuteQGeoFileTileCacheCall19)(const void *, int *);
typedef void (*CuteQGeoFileTileCacheCall20)(const void *, int *);
typedef bool (*CuteQGeoFileTileCacheCall21)(const void *, const QByteArray *, int *);
typedef QString * (*CuteQGeoFileTileCacheCall22)(const void *, const QGeoTileSpec *, const QString *, const QString *, int *);
typedef const QGeoTileSpec * (*CuteQGeoFileTileCacheCall23)(const void *, const QString *, int *);
typedef void (*CuteQGeoFileTileCacheCall24)(const void *, const QGeoTileSpec *, const QString *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoFileTileCacheCall25)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQGeoFileTileCacheCall26)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoFileTileCacheCall27)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoFileTileCacheCall28)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoFileTileCacheCall29)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoFileTileCacheCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQGeoFileTileCacheCall31)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQGeoFileTileCache : public QGeoFileTileCache {
public:
  using QGeoFileTileCache::QGeoFileTileCache;
  void *taken[32] = {};

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
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache4initEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache10printStatsEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTileSpecRK7QStringS5_")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractGeoTileCache11handleErrorERK12QGeoTileSpecRK7QString")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[31] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QGeoFileTileCache::setMaxDiskUsage(int diskUsage)
  void setMaxDiskUsage(int diskUsage) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall0 call = reinterpret_cast<CuteQGeoFileTileCacheCall0>(taken[0]);
      call(this, diskUsage, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setMaxDiskUsage(diskUsage);
  }

  //  int QGeoFileTileCache::maxDiskUsage() const
  int maxDiskUsage() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall1 call = reinterpret_cast<CuteQGeoFileTileCacheCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::maxDiskUsage();
  }

  //  int QGeoFileTileCache::diskUsage() const
  int diskUsage() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall2 call = reinterpret_cast<CuteQGeoFileTileCacheCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::diskUsage();
  }

  //  void QGeoFileTileCache::setMaxMemoryUsage(int memoryUsage)
  void setMaxMemoryUsage(int memoryUsage) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall3 call = reinterpret_cast<CuteQGeoFileTileCacheCall3>(taken[3]);
      call(this, memoryUsage, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setMaxMemoryUsage(memoryUsage);
  }

  //  int QGeoFileTileCache::maxMemoryUsage() const
  int maxMemoryUsage() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall4 call = reinterpret_cast<CuteQGeoFileTileCacheCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::maxMemoryUsage();
  }

  //  int QGeoFileTileCache::memoryUsage() const
  int memoryUsage() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall5 call = reinterpret_cast<CuteQGeoFileTileCacheCall5>(taken[5]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::memoryUsage();
  }

  //  void QGeoFileTileCache::setMinTextureUsage(int textureUsage)
  void setMinTextureUsage(int textureUsage) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall6 call = reinterpret_cast<CuteQGeoFileTileCacheCall6>(taken[6]);
      call(this, textureUsage, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setMinTextureUsage(textureUsage);
  }

  //  void QGeoFileTileCache::setExtraTextureUsage(int textureUsage)
  void setExtraTextureUsage(int textureUsage) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall7 call = reinterpret_cast<CuteQGeoFileTileCacheCall7>(taken[7]);
      call(this, textureUsage, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setExtraTextureUsage(textureUsage);
  }

  //  int QGeoFileTileCache::maxTextureUsage() const
  int maxTextureUsage() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall8 call = reinterpret_cast<CuteQGeoFileTileCacheCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::maxTextureUsage();
  }

  //  int QGeoFileTileCache::minTextureUsage() const
  int minTextureUsage() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall9 call = reinterpret_cast<CuteQGeoFileTileCacheCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::minTextureUsage();
  }

  //  int QGeoFileTileCache::textureUsage() const
  int textureUsage() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall10 call = reinterpret_cast<CuteQGeoFileTileCacheCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::textureUsage();
  }

  //  void QGeoFileTileCache::clearAll()
  void clearAll() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall11 call = reinterpret_cast<CuteQGeoFileTileCacheCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::clearAll();
  }

  //  void QGeoFileTileCache::setCostStrategyDisk(CostStrategy
  //      costStrategy)
  void setCostStrategyDisk(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall12 call = reinterpret_cast<CuteQGeoFileTileCacheCall12>(taken[12]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setCostStrategyDisk(costStrategy);
  }

  //  CostStrategy QGeoFileTileCache::costStrategyDisk() const
  QAbstractGeoTileCache::CostStrategy costStrategyDisk() const override {
    if (taken[13]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall13 call = reinterpret_cast<CuteQGeoFileTileCacheCall13>(taken[13]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return QGeoFileTileCache::costStrategyDisk();
  }

  //  void QGeoFileTileCache::setCostStrategyMemory(CostStrategy
  //      costStrategy)
  void setCostStrategyMemory(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall14 call = reinterpret_cast<CuteQGeoFileTileCacheCall14>(taken[14]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setCostStrategyMemory(costStrategy);
  }

  //  CostStrategy QGeoFileTileCache::costStrategyMemory() const
  QAbstractGeoTileCache::CostStrategy costStrategyMemory() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall15 call = reinterpret_cast<CuteQGeoFileTileCacheCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return QGeoFileTileCache::costStrategyMemory();
  }

  //  void QGeoFileTileCache::setCostStrategyTexture(CostStrategy
  //      costStrategy)
  void setCostStrategyTexture(
      QAbstractGeoTileCache::CostStrategy costStrategy) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall16 call = reinterpret_cast<CuteQGeoFileTileCacheCall16>(taken[16]);
      call(this, static_cast<int>(costStrategy), &handled);
      if (handled) return;
    }
    QGeoFileTileCache::setCostStrategyTexture(costStrategy);
  }

  //  CostStrategy QGeoFileTileCache::costStrategyTexture() const
  QAbstractGeoTileCache::CostStrategy costStrategyTexture() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall17 call = reinterpret_cast<CuteQGeoFileTileCacheCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAbstractGeoTileCache::CostStrategy>(given);
    }
    return QGeoFileTileCache::costStrategyTexture();
  }

  //  void QGeoFileTileCache::insert(const QGeoTileSpec &spec, const
  //      QByteArray &bytes, const QString &format,
  //      QAbstractGeoTileCache::CacheAreas areas)
  void insert(
      const QGeoTileSpec &spec,
      const QByteArray &bytes,
      const QString &format,
      QAbstractGeoTileCache::CacheAreas areas) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall18 call = reinterpret_cast<CuteQGeoFileTileCacheCall18>(taken[18]);
      call(this, &spec, &bytes, &format, static_cast<int>(areas.toInt()), &handled);
      if (handled) return;
    }
    QGeoFileTileCache::insert(spec, bytes, format, areas);
  }

  //  void QGeoFileTileCache::init()
  void init() override {
    if (taken[19]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall19 call = reinterpret_cast<CuteQGeoFileTileCacheCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::init();
  }

  //  void QGeoFileTileCache::printStats()
  void printStats() override {
    if (taken[20]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall20 call = reinterpret_cast<CuteQGeoFileTileCacheCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QGeoFileTileCache::printStats();
  }

  //  bool QGeoFileTileCache::isTileBogus(const QByteArray &bytes) const
  bool isTileBogus(const QByteArray &bytes) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall21 call = reinterpret_cast<CuteQGeoFileTileCacheCall21>(taken[21]);
      bool given = call(this, &bytes, &handled);
      if (handled) return given;
    }
    return QGeoFileTileCache::isTileBogus(bytes);
  }

  //  QString QGeoFileTileCache::tileSpecToFilename(const QGeoTileSpec
  //      &spec, const QString &format, const QString &directory) const
  QString tileSpecToFilename(
      const QGeoTileSpec &spec,
      const QString &format,
      const QString &directory) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall22 call = reinterpret_cast<CuteQGeoFileTileCacheCall22>(taken[22]);
      QString * given = call(this, &spec, &format, &directory, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QGeoFileTileCache::tileSpecToFilename(spec, format, directory);
  }

  //  QGeoTileSpec QGeoFileTileCache::filenameToTileSpec(const QString
  //      &filename) const
  QGeoTileSpec filenameToTileSpec(const QString &filename) const override {
    if (taken[23]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall23 call = reinterpret_cast<CuteQGeoFileTileCacheCall23>(taken[23]);
      const QGeoTileSpec * given = call(this, &filename, &handled);
      if (handled && given) return *given;
    }
    return QGeoFileTileCache::filenameToTileSpec(filename);
  }

  //  void QAbstractGeoTileCache::handleError(const QGeoTileSpec &spec,
  //      const QString &errorString)
  void handleError(
      const QGeoTileSpec &spec,
      const QString &errorString) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall24 call = reinterpret_cast<CuteQGeoFileTileCacheCall24>(taken[24]);
      call(this, &spec, &errorString, &handled);
      if (handled) return;
    }
    QAbstractGeoTileCache::handleError(spec, errorString);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall25 call = reinterpret_cast<CuteQGeoFileTileCacheCall25>(taken[25]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall26 call = reinterpret_cast<CuteQGeoFileTileCacheCall26>(taken[26]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall27 call = reinterpret_cast<CuteQGeoFileTileCacheCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall28 call = reinterpret_cast<CuteQGeoFileTileCacheCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[29]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall29 call = reinterpret_cast<CuteQGeoFileTileCacheCall29>(taken[29]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall30 call = reinterpret_cast<CuteQGeoFileTileCacheCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[31]) {
      int handled = 0;
      CuteQGeoFileTileCacheCall31 call = reinterpret_cast<CuteQGeoFileTileCacheCall31>(taken[31]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QGeoFileTileCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QGeoFileTileCache10metaObjectEv(
    const QGeoFileTileCache *self) {
  return self->metaObject();
}

//  QString QGeoFileTileCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGeoFileTileCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGeoFileTileCache::tr(s, c, n));
}

//  QGeoFileTileCache::QGeoFileTileCache(const QString &directory, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QGeoFileTileCache *ritual_ZN17QGeoFileTileCacheC1ERK7QStringP7QObject(
    const QString *directory,
    QObject *parent) {
  return new CuteQGeoFileTileCache(*directory, parent);
}

//  QGeoFileTileCache::~QGeoFileTileCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCacheD1Ev(QGeoFileTileCache *self) {
  delete self;
}

//  void QGeoFileTileCache::setMaxDiskUsage(int diskUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache15setMaxDiskUsageEi(
    QGeoFileTileCache *self,
    int diskUsage) {
  self->setMaxDiskUsage(diskUsage);
}

//  int QGeoFileTileCache::maxDiskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache12maxDiskUsageEv(
    const QGeoFileTileCache *self) {
  return self->maxDiskUsage();
}

//  int QGeoFileTileCache::diskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache9diskUsageEv(
    const QGeoFileTileCache *self) {
  return self->diskUsage();
}

//  void QGeoFileTileCache::setMaxMemoryUsage(int memoryUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache17setMaxMemoryUsageEi(
    QGeoFileTileCache *self,
    int memoryUsage) {
  self->setMaxMemoryUsage(memoryUsage);
}

//  int QGeoFileTileCache::maxMemoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache14maxMemoryUsageEv(
    const QGeoFileTileCache *self) {
  return self->maxMemoryUsage();
}

//  int QGeoFileTileCache::memoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache11memoryUsageEv(
    const QGeoFileTileCache *self) {
  return self->memoryUsage();
}

//  void QGeoFileTileCache::setMinTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache18setMinTextureUsageEi(
    QGeoFileTileCache *self,
    int textureUsage) {
  self->setMinTextureUsage(textureUsage);
}

//  void QGeoFileTileCache::setExtraTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache20setExtraTextureUsageEi(
    QGeoFileTileCache *self,
    int textureUsage) {
  self->setExtraTextureUsage(textureUsage);
}

//  int QGeoFileTileCache::maxTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache15maxTextureUsageEv(
    const QGeoFileTileCache *self) {
  return self->maxTextureUsage();
}

//  int QGeoFileTileCache::minTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache15minTextureUsageEv(
    const QGeoFileTileCache *self) {
  return self->minTextureUsage();
}

//  int QGeoFileTileCache::textureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QGeoFileTileCache12textureUsageEv(
    const QGeoFileTileCache *self) {
  return self->textureUsage();
}

//  void QGeoFileTileCache::clearAll()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache8clearAllEv(QGeoFileTileCache *self) {
  self->clearAll();
}

//  void QGeoFileTileCache::clearMapId(int mapId)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache10clearMapIdEi(
    QGeoFileTileCache *self,
    int mapId) {
  self->clearMapId(mapId);
}

//  void QGeoFileTileCache::setCostStrategyDisk(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache19setCostStrategyDiskEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyDisk(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyDisk() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK17QGeoFileTileCache16costStrategyDiskEv(
    const QGeoFileTileCache *self) {
  return self->costStrategyDisk();
}

//  void QGeoFileTileCache::setCostStrategyMemory(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache21setCostStrategyMemoryEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyMemory(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyMemory() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK17QGeoFileTileCache18costStrategyMemoryEv(
    const QGeoFileTileCache *self) {
  return self->costStrategyMemory();
}

//  void QGeoFileTileCache::setCostStrategyTexture(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache22setCostStrategyTextureEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->setCostStrategyTexture(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyTexture() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_ZNK17QGeoFileTileCache19costStrategyTextureEv(
    const QGeoFileTileCache *self) {
  return self->costStrategyTexture();
}

//  void QGeoFileTileCache::evictFromDiskCache(QGeoCachedTileDisk *td)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache18evictFromDiskCacheEP18QGeoCachedTileDisk(
    QGeoCachedTileDisk *td) {
  QGeoFileTileCache::evictFromDiskCache(td);
}

//  void QGeoFileTileCache::insert(const QGeoTileSpec &spec, const QByteArray
//      &bytes, const QString &format, QAbstractGeoTileCache::CacheAreas
//      areas)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache6insertERK12QGeoTileSpecRK10QByteArrayRK7QString6QFlagsIN21QAbstractGeoTileCache9CacheAreaEE(
    QGeoFileTileCache *self,
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

//  QString QGeoFileTileCache::tileSpecToFilenameDefault(const QGeoTileSpec
//      &spec, const QString &format, const QString &directory)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QGeoFileTileCache25tileSpecToFilenameDefaultERK12QGeoTileSpecRK7QStringS5_(
    const QGeoTileSpec *spec,
    const QString *format,
    const QString *directory) {
  return new QString(
      QGeoFileTileCache::tileSpecToFilenameDefault(
          *spec,
          *format,
          *directory));
}

//  QGeoTileSpec QGeoFileTileCache::filenameToTileSpecDefault(const QString
//      &filename)
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZN17QGeoFileTileCache25filenameToTileSpecDefaultERK7QString(
    const QString *filename) {
  return new QGeoTileSpec(
      QGeoFileTileCache::filenameToTileSpecDefault(
          *filename));
}

//  void QGeoFileTileCache::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache4initEv(QGeoFileTileCache *self) {
  self->init();
}

//  void QGeoFileTileCache::printStats()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache10printStatsEv(QGeoFileTileCache *self) {
  self->printStats();
}

//  void QGeoFileTileCache::loadTiles()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache9loadTilesEv(QGeoFileTileCache *self) {
  self->loadTiles();
}

//  QString QGeoFileTileCache::directory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGeoFileTileCache9directoryEv(
    const QGeoFileTileCache *self) {
  return new QString(self->directory());
}

//  bool QGeoFileTileCache::addToDiskCache(const QGeoTileSpec &spec, const
//      QString &filename, const QByteArray &bytes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QGeoFileTileCache14addToDiskCacheERK12QGeoTileSpecRK7QStringRK10QByteArray(
    QGeoFileTileCache *self,
    const QGeoTileSpec *spec,
    const QString *filename,
    const QByteArray *bytes) {
  return self->addToDiskCache(*spec, *filename, *bytes);
}

//  void QGeoFileTileCache::addToMemoryCache(const QGeoTileSpec &spec, const
//      QByteArray &bytes, const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoFileTileCache16addToMemoryCacheERK12QGeoTileSpecRK10QByteArrayRK7QString(
    QGeoFileTileCache *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format) {
  self->addToMemoryCache(*spec, *bytes, *format);
}

//  bool QGeoFileTileCache::isTileBogus(const QByteArray &bytes) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray(
    const QGeoFileTileCache *self,
    const QByteArray *bytes) {
  return self->isTileBogus(*bytes);
}

//  QString QGeoFileTileCache::tileSpecToFilename(const QGeoTileSpec &spec,
//      const QString &format, const QString &directory) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTileSpecRK7QStringS5_(
    const QGeoFileTileCache *self,
    const QGeoTileSpec *spec,
    const QString *format,
    const QString *directory) {
  return new QString(self->tileSpecToFilename(*spec, *format, *directory));
}

//  QGeoTileSpec QGeoFileTileCache::filenameToTileSpec(const QString
//      &filename) const
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString(
    const QGeoFileTileCache *self,
    const QString *filename) {
  return new QGeoTileSpec(self->filenameToTileSpec(*filename));
}

//  a Python function taken by a CuteQGeoFileTileCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoFileTileCache(
    QGeoFileTileCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoFileTileCache *>(self)->take(key, call);
}

//  void QGeoFileTileCache::setMaxDiskUsage(int diskUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache15setMaxDiskUsageEi(
    QGeoFileTileCache *self,
    int diskUsage) {
  self->QGeoFileTileCache::setMaxDiskUsage(diskUsage);
}

//  int QGeoFileTileCache::maxDiskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache12maxDiskUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::maxDiskUsage();
}

//  int QGeoFileTileCache::diskUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache9diskUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::diskUsage();
}

//  void QGeoFileTileCache::setMaxMemoryUsage(int memoryUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache17setMaxMemoryUsageEi(
    QGeoFileTileCache *self,
    int memoryUsage) {
  self->QGeoFileTileCache::setMaxMemoryUsage(memoryUsage);
}

//  int QGeoFileTileCache::maxMemoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache14maxMemoryUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::maxMemoryUsage();
}

//  int QGeoFileTileCache::memoryUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache11memoryUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::memoryUsage();
}

//  void QGeoFileTileCache::setMinTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache18setMinTextureUsageEi(
    QGeoFileTileCache *self,
    int textureUsage) {
  self->QGeoFileTileCache::setMinTextureUsage(textureUsage);
}

//  void QGeoFileTileCache::setExtraTextureUsage(int textureUsage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache20setExtraTextureUsageEi(
    QGeoFileTileCache *self,
    int textureUsage) {
  self->QGeoFileTileCache::setExtraTextureUsage(textureUsage);
}

//  int QGeoFileTileCache::maxTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache15maxTextureUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::maxTextureUsage();
}

//  int QGeoFileTileCache::minTextureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache15minTextureUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::minTextureUsage();
}

//  int QGeoFileTileCache::textureUsage() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QGeoFileTileCache12textureUsageEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::textureUsage();
}

//  void QGeoFileTileCache::clearAll()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache8clearAllEv(QGeoFileTileCache *self) {
  self->QGeoFileTileCache::clearAll();
}

//  void QGeoFileTileCache::setCostStrategyDisk(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache19setCostStrategyDiskEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->QGeoFileTileCache::setCostStrategyDisk(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyDisk() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_own_ZNK17QGeoFileTileCache16costStrategyDiskEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::costStrategyDisk();
}

//  void QGeoFileTileCache::setCostStrategyMemory(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache21setCostStrategyMemoryEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->QGeoFileTileCache::setCostStrategyMemory(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyMemory() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_own_ZNK17QGeoFileTileCache18costStrategyMemoryEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::costStrategyMemory();
}

//  void QGeoFileTileCache::setCostStrategyTexture(CostStrategy costStrategy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache22setCostStrategyTextureEN21QAbstractGeoTileCache12CostStrategyE(
    QGeoFileTileCache *self,
    QAbstractGeoTileCache::CostStrategy costStrategy) {
  self->QGeoFileTileCache::setCostStrategyTexture(costStrategy);
}

//  CostStrategy QGeoFileTileCache::costStrategyTexture() const
extern "C" Q_DECL_EXPORT
QAbstractGeoTileCache::CostStrategy ritual_own_ZNK17QGeoFileTileCache19costStrategyTextureEv(
    const QGeoFileTileCache *self) {
  return self->QGeoFileTileCache::costStrategyTexture();
}

//  void QGeoFileTileCache::insert(const QGeoTileSpec &spec, const QByteArray
//      &bytes, const QString &format, QAbstractGeoTileCache::CacheAreas
//      areas)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache6insertERK12QGeoTileSpecRK10QByteArrayRK7QString6QFlagsIN21QAbstractGeoTileCache9CacheAreaEE(
    QGeoFileTileCache *self,
    const QGeoTileSpec *spec,
    const QByteArray *bytes,
    const QString *format,
    int areas) {
  self->QGeoFileTileCache::insert(
      *spec,
      *bytes,
      *format,
      QFlags<QAbstractGeoTileCache::CacheArea>::fromInt(areas));
}

//  void QGeoFileTileCache::init()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache4initEv(QGeoFileTileCache *self) {
  static_cast<OwnQGeoFileTileCache *>(self)->OwnQGeoFileTileCache::init();
}

//  void QGeoFileTileCache::printStats()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QGeoFileTileCache10printStatsEv(
    QGeoFileTileCache *self) {
  static_cast<OwnQGeoFileTileCache *>(self)->OwnQGeoFileTileCache::printStats();
}

//  bool QGeoFileTileCache::isTileBogus(const QByteArray &bytes) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGeoFileTileCache11isTileBogusERK10QByteArray(
    const QGeoFileTileCache *self,
    const QByteArray *bytes) {
  return static_cast<const OwnQGeoFileTileCache *>(self)->OwnQGeoFileTileCache::isTileBogus(
      *bytes);
}

//  QString QGeoFileTileCache::tileSpecToFilename(const QGeoTileSpec &spec,
//      const QString &format, const QString &directory) const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK17QGeoFileTileCache18tileSpecToFilenameERK12QGeoTileSpecRK7QStringS5_(
    const QGeoFileTileCache *self,
    const QGeoTileSpec *spec,
    const QString *format,
    const QString *directory) {
  return new QString(
      static_cast<const OwnQGeoFileTileCache *>(self)->OwnQGeoFileTileCache::tileSpecToFilename(
          *spec,
          *format,
          *directory));
}

//  QGeoTileSpec QGeoFileTileCache::filenameToTileSpec(const QString
//      &filename) const
extern "C" Q_DECL_EXPORT
QGeoTileSpec *ritual_own_ZNK17QGeoFileTileCache18filenameToTileSpecERK7QString(
    const QGeoFileTileCache *self,
    const QString *filename) {
  return new QGeoTileSpec(
      static_cast<const OwnQGeoFileTileCache *>(self)->OwnQGeoFileTileCache::filenameToTileSpec(
          *filename));
}
