//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkdiskcache.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
#include <QtNetwork/qnetworkdiskcache.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  Only a class built on QNetworkDiskCache may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkDiskCache : QNetworkDiskCache {
  using QNetworkDiskCache::expire;
};

//  A QNetworkDiskCache that Python can take functions over in. Every QNetworkDiskCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(networkdiskcache)
typedef qint64 (*CuteQNetworkDiskCacheCall0)(const void *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef const QNetworkCacheMetaData * (*CuteQNetworkDiskCacheCall1)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef void (*CuteQNetworkDiskCacheCall2)(const void *, const QNetworkCacheMetaData *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef void * (*CuteQNetworkDiskCacheCall3)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef bool (*CuteQNetworkDiskCacheCall4)(const void *, const QUrl *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef void * (*CuteQNetworkDiskCacheCall5)(const void *, const QNetworkCacheMetaData *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef void (*CuteQNetworkDiskCacheCall6)(const void *, QIODevice *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef void (*CuteQNetworkDiskCacheCall7)(const void *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
typedef qint64 (*CuteQNetworkDiskCacheCall8)(const void *, int *);
#endif  // QT_CONFIG(networkdiskcache)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkDiskCacheCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkDiskCacheCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkDiskCacheCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkDiskCacheCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkDiskCacheCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkDiskCacheCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkDiskCacheCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkDiskCache : public QNetworkDiskCache {
public:
  using QNetworkDiskCache::QNetworkDiskCache;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZNK21QAbstractNetworkCache9cacheSizeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache8metaDataERK4QUrl")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache14updateMetaDataERK21QNetworkCacheMetaData")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache4dataERK4QUrl")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache6removeERK4QUrl")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache7prepareERK21QNetworkCacheMetaData")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache6insertEP9QIODevice")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache5clearEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
#if QT_CONFIG(networkdiskcache)
    if (!std::strcmp(key, "_ZN17QNetworkDiskCache6expireEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(networkdiskcache)
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

#if QT_CONFIG(networkdiskcache)
  //  qint64 QNetworkDiskCache::cacheSize() const
  qint64 cacheSize() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall0 call = reinterpret_cast<CuteQNetworkDiskCacheCall0>(taken[0]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkDiskCache::cacheSize();
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  QNetworkCacheMetaData QNetworkDiskCache::metaData(const QUrl &url)
  QNetworkCacheMetaData metaData(const QUrl &url) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall1 call = reinterpret_cast<CuteQNetworkDiskCacheCall1>(taken[1]);
      const QNetworkCacheMetaData * given = call(this, &url, &handled);
      if (handled && given) return *given;
    }
    return QNetworkDiskCache::metaData(url);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  void QNetworkDiskCache::updateMetaData(const QNetworkCacheMetaData
  //      &metaData)
  void updateMetaData(const QNetworkCacheMetaData &metaData) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall2 call = reinterpret_cast<CuteQNetworkDiskCacheCall2>(taken[2]);
      call(this, &metaData, &handled);
      if (handled) return;
    }
    QNetworkDiskCache::updateMetaData(metaData);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  QIODevice *QNetworkDiskCache::data(const QUrl &url)
  QIODevice *data(const QUrl &url) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall3 call = reinterpret_cast<CuteQNetworkDiskCacheCall3>(taken[3]);
      void * given = call(this, &url, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QNetworkDiskCache::data(url);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  bool QNetworkDiskCache::remove(const QUrl &url)
  bool remove(const QUrl &url) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall4 call = reinterpret_cast<CuteQNetworkDiskCacheCall4>(taken[4]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return QNetworkDiskCache::remove(url);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  QIODevice *QNetworkDiskCache::prepare(const QNetworkCacheMetaData
  //      &metaData)
  QIODevice *prepare(const QNetworkCacheMetaData &metaData) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall5 call = reinterpret_cast<CuteQNetworkDiskCacheCall5>(taken[5]);
      void * given = call(this, &metaData, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return QNetworkDiskCache::prepare(metaData);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  void QNetworkDiskCache::insert(QIODevice *device)
  void insert(QIODevice *device) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall6 call = reinterpret_cast<CuteQNetworkDiskCacheCall6>(taken[6]);
      call(this, device, &handled);
      if (handled) return;
    }
    QNetworkDiskCache::insert(device);
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  void QNetworkDiskCache::clear()
  void clear() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall7 call = reinterpret_cast<CuteQNetworkDiskCacheCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QNetworkDiskCache::clear();
  }
#endif  // QT_CONFIG(networkdiskcache)

#if QT_CONFIG(networkdiskcache)
  //  qint64 QNetworkDiskCache::expire()
  qint64 expire() override {
    if (taken[8]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall8 call = reinterpret_cast<CuteQNetworkDiskCacheCall8>(taken[8]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QNetworkDiskCache::expire();
  }
#endif  // QT_CONFIG(networkdiskcache)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNetworkDiskCacheCall9 call = reinterpret_cast<CuteQNetworkDiskCacheCall9>(taken[9]);
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
      CuteQNetworkDiskCacheCall10 call = reinterpret_cast<CuteQNetworkDiskCacheCall10>(taken[10]);
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
      CuteQNetworkDiskCacheCall11 call = reinterpret_cast<CuteQNetworkDiskCacheCall11>(taken[11]);
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
      CuteQNetworkDiskCacheCall12 call = reinterpret_cast<CuteQNetworkDiskCacheCall12>(taken[12]);
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
      CuteQNetworkDiskCacheCall13 call = reinterpret_cast<CuteQNetworkDiskCacheCall13>(taken[13]);
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
      CuteQNetworkDiskCacheCall14 call = reinterpret_cast<CuteQNetworkDiskCacheCall14>(taken[14]);
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
      CuteQNetworkDiskCacheCall15 call = reinterpret_cast<CuteQNetworkDiskCacheCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkDiskCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QNetworkDiskCache10metaObjectEv(
    const QNetworkDiskCache *self) {
  return self->metaObject();
}

//  QString QNetworkDiskCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QNetworkDiskCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkDiskCache::tr(s, c, n));
}

//  QNetworkDiskCache::QNetworkDiskCache(QObject *parent)
extern "C" Q_DECL_EXPORT
QNetworkDiskCache *ritual_ZN17QNetworkDiskCacheC1EP7QObject(
    QObject *parent) {
  return new CuteQNetworkDiskCache(parent);
}

//  QNetworkDiskCache::~QNetworkDiskCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCacheD1Ev(QNetworkDiskCache *self) {
  delete self;
}

//  QString QNetworkDiskCache::cacheDirectory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QNetworkDiskCache14cacheDirectoryEv(
    const QNetworkDiskCache *self) {
  return new QString(self->cacheDirectory());
}

//  void QNetworkDiskCache::setCacheDirectory(const QString &cacheDir)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCache17setCacheDirectoryERK7QString(
    QNetworkDiskCache *self,
    const QString *cacheDir) {
  self->setCacheDirectory(*cacheDir);
}

//  qint64 QNetworkDiskCache::maximumCacheSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QNetworkDiskCache16maximumCacheSizeEv(
    const QNetworkDiskCache *self) {
  return self->maximumCacheSize();
}

//  void QNetworkDiskCache::setMaximumCacheSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCache19setMaximumCacheSizeEx(
    QNetworkDiskCache *self,
    qint64 size) {
  self->setMaximumCacheSize(size);
}

//  qint64 QNetworkDiskCache::cacheSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QNetworkDiskCache9cacheSizeEv(
    const QNetworkDiskCache *self) {
  return self->cacheSize();
}

//  QNetworkCacheMetaData QNetworkDiskCache::metaData(const QUrl &url)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN17QNetworkDiskCache8metaDataERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return new QNetworkCacheMetaData(self->metaData(*url));
}

//  void QNetworkDiskCache::updateMetaData(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCache14updateMetaDataERK21QNetworkCacheMetaData(
    QNetworkDiskCache *self,
    const QNetworkCacheMetaData *metaData) {
  self->updateMetaData(*metaData);
}

//  QIODevice *QNetworkDiskCache::data(const QUrl &url)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN17QNetworkDiskCache4dataERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return self->data(*url);
}

//  bool QNetworkDiskCache::remove(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QNetworkDiskCache6removeERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return self->remove(*url);
}

//  QIODevice *QNetworkDiskCache::prepare(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN17QNetworkDiskCache7prepareERK21QNetworkCacheMetaData(
    QNetworkDiskCache *self,
    const QNetworkCacheMetaData *metaData) {
  return self->prepare(*metaData);
}

//  void QNetworkDiskCache::insert(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCache6insertEP9QIODevice(
    QNetworkDiskCache *self,
    QIODevice *device) {
  self->insert(device);
}

//  QNetworkCacheMetaData QNetworkDiskCache::fileMetaData(const QString
//      &fileName) const
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZNK17QNetworkDiskCache12fileMetaDataERK7QString(
    const QNetworkDiskCache *self,
    const QString *fileName) {
  return new QNetworkCacheMetaData(self->fileMetaData(*fileName));
}

//  void QNetworkDiskCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QNetworkDiskCache5clearEv(QNetworkDiskCache *self) {
  self->clear();
}

//  qint64 QNetworkDiskCache::expire()
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN17QNetworkDiskCache6expireEv(QNetworkDiskCache *self) {
  return self->expire();
}

//  QNetworkDiskCachePrivate *QNetworkDiskCache::d_func()
extern "C" Q_DECL_EXPORT
QNetworkDiskCachePrivate *ritual_ZN17QNetworkDiskCache6d_funcEv(
    QNetworkDiskCache *self) {
  return self->d_func();
}

//  const QNetworkDiskCachePrivate *QNetworkDiskCache::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkDiskCachePrivate *ritual_ZNK17QNetworkDiskCache6d_funcEv(
    const QNetworkDiskCache *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkDiskCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkDiskCache(
    QNetworkDiskCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkDiskCache *>(self)->take(key, call);
}

//  qint64 QNetworkDiskCache::cacheSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK17QNetworkDiskCache9cacheSizeEv(
    const QNetworkDiskCache *self) {
  return self->QNetworkDiskCache::cacheSize();
}

//  QNetworkCacheMetaData QNetworkDiskCache::metaData(const QUrl &url)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_own_ZN17QNetworkDiskCache8metaDataERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return new QNetworkCacheMetaData(self->QNetworkDiskCache::metaData(*url));
}

//  void QNetworkDiskCache::updateMetaData(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkDiskCache14updateMetaDataERK21QNetworkCacheMetaData(
    QNetworkDiskCache *self,
    const QNetworkCacheMetaData *metaData) {
  self->QNetworkDiskCache::updateMetaData(*metaData);
}

//  QIODevice *QNetworkDiskCache::data(const QUrl &url)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZN17QNetworkDiskCache4dataERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return self->QNetworkDiskCache::data(*url);
}

//  bool QNetworkDiskCache::remove(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QNetworkDiskCache6removeERK4QUrl(
    QNetworkDiskCache *self,
    const QUrl *url) {
  return self->QNetworkDiskCache::remove(*url);
}

//  QIODevice *QNetworkDiskCache::prepare(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_own_ZN17QNetworkDiskCache7prepareERK21QNetworkCacheMetaData(
    QNetworkDiskCache *self,
    const QNetworkCacheMetaData *metaData) {
  return self->QNetworkDiskCache::prepare(*metaData);
}

//  void QNetworkDiskCache::insert(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkDiskCache6insertEP9QIODevice(
    QNetworkDiskCache *self,
    QIODevice *device) {
  self->QNetworkDiskCache::insert(device);
}

//  void QNetworkDiskCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QNetworkDiskCache5clearEv(QNetworkDiskCache *self) {
  self->QNetworkDiskCache::clear();
}

//  qint64 QNetworkDiskCache::expire()
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN17QNetworkDiskCache6expireEv(QNetworkDiskCache *self) {
  return static_cast<OwnQNetworkDiskCache *>(self)->OwnQNetworkDiskCache::expire();
}

#endif  // QT_CONFIG(networkdiskcache)
#endif  // QT_CONFIG(networkdiskcache)
