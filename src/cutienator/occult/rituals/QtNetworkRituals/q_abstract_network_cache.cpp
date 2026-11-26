//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qabstractnetworkcache.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qabstractnetworkcache.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QAbstractNetworkCache that Python can take functions over in. Every QAbstractNetworkCache
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QNetworkCacheMetaData * (*CuteQAbstractNetworkCacheCall0)(const void *, const QUrl *, int *);
typedef void (*CuteQAbstractNetworkCacheCall1)(const void *, const QNetworkCacheMetaData *, int *);
typedef void * (*CuteQAbstractNetworkCacheCall2)(const void *, const QUrl *, int *);
typedef bool (*CuteQAbstractNetworkCacheCall3)(const void *, const QUrl *, int *);
typedef qint64 (*CuteQAbstractNetworkCacheCall4)(const void *, int *);
typedef void * (*CuteQAbstractNetworkCacheCall5)(const void *, const QNetworkCacheMetaData *, int *);
typedef void (*CuteQAbstractNetworkCacheCall6)(const void *, QIODevice *, int *);
typedef void (*CuteQAbstractNetworkCacheCall7)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractNetworkCacheCall8)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstractNetworkCacheCall9)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractNetworkCacheCall10)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractNetworkCacheCall11)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractNetworkCacheCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractNetworkCacheCall13)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstractNetworkCacheCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstractNetworkCache : public QAbstractNetworkCache {
public:
  using QAbstractNetworkCache::QAbstractNetworkCache;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache8metaDataERK4QUrl")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache14updateMetaDataERK21QNetworkCacheMetaData")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache4dataERK4QUrl")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache6removeERK4QUrl")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK21QAbstractNetworkCache9cacheSizeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache7prepareERK21QNetworkCacheMetaData")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache6insertEP9QIODevice")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN21QAbstractNetworkCache5clearEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QNetworkCacheMetaData QAbstractNetworkCache::metaData(const QUrl
  //      &url)
  QNetworkCacheMetaData metaData(const QUrl &url) override {
    if (taken[0]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall0 call = reinterpret_cast<CuteQAbstractNetworkCacheCall0>(taken[0]);
      const QNetworkCacheMetaData * given = call(this, &url, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QAbstractNetworkCache::updateMetaData(const
  //      QNetworkCacheMetaData &metaData)
  void updateMetaData(const QNetworkCacheMetaData &metaData) override {
    if (taken[1]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall1 call = reinterpret_cast<CuteQAbstractNetworkCacheCall1>(taken[1]);
      call(this, &metaData, &handled);
      if (handled) return;
    }
  }

  //  QIODevice *QAbstractNetworkCache::data(const QUrl &url)
  QIODevice *data(const QUrl &url) override {
    if (taken[2]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall2 call = reinterpret_cast<CuteQAbstractNetworkCacheCall2>(taken[2]);
      void * given = call(this, &url, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  bool QAbstractNetworkCache::remove(const QUrl &url)
  bool remove(const QUrl &url) override {
    if (taken[3]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall3 call = reinterpret_cast<CuteQAbstractNetworkCacheCall3>(taken[3]);
      bool given = call(this, &url, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  qint64 QAbstractNetworkCache::cacheSize() const
  qint64 cacheSize() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall4 call = reinterpret_cast<CuteQAbstractNetworkCacheCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }

  //  QIODevice *QAbstractNetworkCache::prepare(const QNetworkCacheMetaData
  //      &metaData)
  QIODevice *prepare(const QNetworkCacheMetaData &metaData) override {
    if (taken[5]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall5 call = reinterpret_cast<CuteQAbstractNetworkCacheCall5>(taken[5]);
      void * given = call(this, &metaData, &handled);
      if (handled) return static_cast<QIODevice *>(given);
    }
    return {};
  }

  //  void QAbstractNetworkCache::insert(QIODevice *device)
  void insert(QIODevice *device) override {
    if (taken[6]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall6 call = reinterpret_cast<CuteQAbstractNetworkCacheCall6>(taken[6]);
      call(this, device, &handled);
      if (handled) return;
    }
  }

  //  void QAbstractNetworkCache::clear()
  void clear() override {
    if (taken[7]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall7 call = reinterpret_cast<CuteQAbstractNetworkCacheCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall8 call = reinterpret_cast<CuteQAbstractNetworkCacheCall8>(taken[8]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall9 call = reinterpret_cast<CuteQAbstractNetworkCacheCall9>(taken[9]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall10 call = reinterpret_cast<CuteQAbstractNetworkCacheCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall11 call = reinterpret_cast<CuteQAbstractNetworkCacheCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall12 call = reinterpret_cast<CuteQAbstractNetworkCacheCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[13]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall13 call = reinterpret_cast<CuteQAbstractNetworkCacheCall13>(taken[13]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQAbstractNetworkCacheCall14 call = reinterpret_cast<CuteQAbstractNetworkCacheCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstractNetworkCache::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractNetworkCache10metaObjectEv(
    const QAbstractNetworkCache *self) {
  return self->metaObject();
}

//  void *QAbstractNetworkCache::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN21QAbstractNetworkCache11qt_metacastEPKc(
    QAbstractNetworkCache *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QAbstractNetworkCache::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN21QAbstractNetworkCache11qt_metacallEN11QMetaObject4CallEiPPv(
    QAbstractNetworkCache *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QAbstractNetworkCache::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractNetworkCache2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractNetworkCache::tr(s, c, n));
}

//  QAbstractNetworkCache::~QAbstractNetworkCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractNetworkCacheD1Ev(QAbstractNetworkCache *self) {
  delete self;
}

//  QNetworkCacheMetaData QAbstractNetworkCache::metaData(const QUrl &url)
extern "C" Q_DECL_EXPORT
QNetworkCacheMetaData *ritual_ZN21QAbstractNetworkCache8metaDataERK4QUrl(
    QAbstractNetworkCache *self,
    const QUrl *url) {
  return new QNetworkCacheMetaData(self->metaData(*url));
}

//  void QAbstractNetworkCache::updateMetaData(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractNetworkCache14updateMetaDataERK21QNetworkCacheMetaData(
    QAbstractNetworkCache *self,
    const QNetworkCacheMetaData *metaData) {
  self->updateMetaData(*metaData);
}

//  QIODevice *QAbstractNetworkCache::data(const QUrl &url)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN21QAbstractNetworkCache4dataERK4QUrl(
    QAbstractNetworkCache *self,
    const QUrl *url) {
  return self->data(*url);
}

//  bool QAbstractNetworkCache::remove(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractNetworkCache6removeERK4QUrl(
    QAbstractNetworkCache *self,
    const QUrl *url) {
  return self->remove(*url);
}

//  qint64 QAbstractNetworkCache::cacheSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK21QAbstractNetworkCache9cacheSizeEv(
    const QAbstractNetworkCache *self) {
  return self->cacheSize();
}

//  QIODevice *QAbstractNetworkCache::prepare(const QNetworkCacheMetaData
//      &metaData)
extern "C" Q_DECL_EXPORT
QIODevice *ritual_ZN21QAbstractNetworkCache7prepareERK21QNetworkCacheMetaData(
    QAbstractNetworkCache *self,
    const QNetworkCacheMetaData *metaData) {
  return self->prepare(*metaData);
}

//  void QAbstractNetworkCache::insert(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractNetworkCache6insertEP9QIODevice(
    QAbstractNetworkCache *self,
    QIODevice *device) {
  self->insert(device);
}

//  void QAbstractNetworkCache::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractNetworkCache5clearEv(QAbstractNetworkCache *self) {
  self->clear();
}

//  QAbstractNetworkCache::QAbstractNetworkCache(QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractNetworkCache *ritual_ZN21QAbstractNetworkCacheC1EP7QObject(
    QObject *parent) {
  return new CuteQAbstractNetworkCache(parent);
}

//  QAbstractNetworkCache::QAbstractNetworkCache(QAbstractNetworkCachePrivate
//      &dd, QObject *parent)
extern "C" Q_DECL_EXPORT
QAbstractNetworkCache *ritual_ZN21QAbstractNetworkCacheC1ER28QAbstractNetworkCachePrivateP7QObject(
    QAbstractNetworkCachePrivate *dd,
    QObject *parent) {
  return new CuteQAbstractNetworkCache(*dd, parent);
}

//  QAbstractNetworkCachePrivate *QAbstractNetworkCache::d_func()
extern "C" Q_DECL_EXPORT
QAbstractNetworkCachePrivate *ritual_ZN21QAbstractNetworkCache6d_funcEv(
    QAbstractNetworkCache *self) {
  return self->d_func();
}

//  const QAbstractNetworkCachePrivate *QAbstractNetworkCache::d_func() const
extern "C" Q_DECL_EXPORT
const QAbstractNetworkCachePrivate *ritual_ZNK21QAbstractNetworkCache6d_funcEv(
    const QAbstractNetworkCache *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQAbstractNetworkCache, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractNetworkCache(
    QAbstractNetworkCache *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractNetworkCache *>(self)->take(key, call);
}
