//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qnetworkaccessmanager.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qnetworkaccessmanager.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtNetwork/qhstspolicy.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QNetworkAccessManager may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQNetworkAccessManager : QNetworkAccessManager {
  using QNetworkAccessManager::createRequest;
};

//  A QNetworkAccessManager that Python can take functions over in. Every QNetworkAccessManager
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void * (*CuteQNetworkAccessManagerCall0)(const void *, int, const QNetworkRequest *, QIODevice *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessManagerCall1)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNetworkAccessManagerCall2)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessManagerCall3)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessManagerCall4)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessManagerCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessManagerCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNetworkAccessManagerCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNetworkAccessManager : public QNetworkAccessManager {
public:
  using QNetworkAccessManager::QNetworkAccessManager;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN21QNetworkAccessManager13createRequestENS_9OperationERK15QNetworkRequestP9QIODevice")) {
      taken[0] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QNetworkReply *QNetworkAccessManager::createRequest(Operation op,
  //      const QNetworkRequest &request, QIODevice *outgoingData)
  QNetworkReply *createRequest(
      QNetworkAccessManager::Operation op,
      const QNetworkRequest &request,
      QIODevice *outgoingData) override {
    if (taken[0]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall0 call = reinterpret_cast<CuteQNetworkAccessManagerCall0>(taken[0]);
      void * given = call(this, static_cast<int>(op), &request, outgoingData, &handled);
      if (handled) return static_cast<QNetworkReply *>(given);
    }
    return QNetworkAccessManager::createRequest(op, request, outgoingData);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall1 call = reinterpret_cast<CuteQNetworkAccessManagerCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall2 call = reinterpret_cast<CuteQNetworkAccessManagerCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall3 call = reinterpret_cast<CuteQNetworkAccessManagerCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall4 call = reinterpret_cast<CuteQNetworkAccessManagerCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall5 call = reinterpret_cast<CuteQNetworkAccessManagerCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall6 call = reinterpret_cast<CuteQNetworkAccessManagerCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNetworkAccessManagerCall7 call = reinterpret_cast<CuteQNetworkAccessManagerCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNetworkAccessManager::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QNetworkAccessManager10metaObjectEv(
    const QNetworkAccessManager *self) {
  return self->metaObject();
}

//  QString QNetworkAccessManager::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QNetworkAccessManager2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNetworkAccessManager::tr(s, c, n));
}

//  QNetworkAccessManager::QNetworkAccessManager(QObject *parent)
extern "C" Q_DECL_EXPORT
QNetworkAccessManager *ritual_ZN21QNetworkAccessManagerC1EP7QObject(
    QObject *parent) {
  return new CuteQNetworkAccessManager(parent);
}

//  QNetworkAccessManager::~QNetworkAccessManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManagerD1Ev(QNetworkAccessManager *self) {
  delete self;
}

//  QStringList QNetworkAccessManager::supportedSchemes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QNetworkAccessManager16supportedSchemesEv(
    const QNetworkAccessManager *self) {
  return new QList<QString>(self->supportedSchemes());
}

//  void QNetworkAccessManager::clearAccessCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager16clearAccessCacheEv(
    QNetworkAccessManager *self) {
  self->clearAccessCache();
}

//  void QNetworkAccessManager::clearConnectionCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager20clearConnectionCacheEv(
    QNetworkAccessManager *self) {
  self->clearConnectionCache();
}

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QNetworkAccessManager::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK21QNetworkAccessManager5proxyEv(
    const QNetworkAccessManager *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QNetworkAccessManager::setProxy(const QNetworkProxy &proxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager8setProxyERK13QNetworkProxy(
    QNetworkAccessManager *self,
    const QNetworkProxy *proxy) {
  self->setProxy(*proxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxyFactory *QNetworkAccessManager::proxyFactory() const
extern "C" Q_DECL_EXPORT
QNetworkProxyFactory *ritual_ZNK21QNetworkAccessManager12proxyFactoryEv(
    const QNetworkAccessManager *self) {
  return self->proxyFactory();
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QNetworkAccessManager::setProxyFactory(QNetworkProxyFactory
//      *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager15setProxyFactoryEP20QNetworkProxyFactory(
    QNetworkAccessManager *self,
    QNetworkProxyFactory *factory) {
  self->setProxyFactory(factory);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  QAbstractNetworkCache *QNetworkAccessManager::cache() const
extern "C" Q_DECL_EXPORT
QAbstractNetworkCache *ritual_ZNK21QNetworkAccessManager5cacheEv(
    const QNetworkAccessManager *self) {
  return self->cache();
}

//  void QNetworkAccessManager::setCache(QAbstractNetworkCache *cache)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager8setCacheEP21QAbstractNetworkCache(
    QNetworkAccessManager *self,
    QAbstractNetworkCache *cache) {
  self->setCache(cache);
}

//  QNetworkCookieJar *QNetworkAccessManager::cookieJar() const
extern "C" Q_DECL_EXPORT
QNetworkCookieJar *ritual_ZNK21QNetworkAccessManager9cookieJarEv(
    const QNetworkAccessManager *self) {
  return self->cookieJar();
}

//  void QNetworkAccessManager::setCookieJar(QNetworkCookieJar *cookieJar)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager12setCookieJarEP17QNetworkCookieJar(
    QNetworkAccessManager *self,
    QNetworkCookieJar *cookieJar) {
  self->setCookieJar(cookieJar);
}

//  void QNetworkAccessManager::setStrictTransportSecurityEnabled(bool
//      enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager33setStrictTransportSecurityEnabledEb(
    QNetworkAccessManager *self,
    bool enabled) {
  self->setStrictTransportSecurityEnabled(enabled);
}

//  bool QNetworkAccessManager::isStrictTransportSecurityEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessManager32isStrictTransportSecurityEnabledEv(
    const QNetworkAccessManager *self) {
  return self->isStrictTransportSecurityEnabled();
}

//  void QNetworkAccessManager::enableStrictTransportSecurityStore(bool
//      enabled, const QString &storeDir)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager34enableStrictTransportSecurityStoreEbRK7QString(
    QNetworkAccessManager *self,
    bool enabled,
    const QString *storeDir) {
  self->enableStrictTransportSecurityStore(enabled, *storeDir);
}

//  bool QNetworkAccessManager::isStrictTransportSecurityStoreEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessManager37isStrictTransportSecurityStoreEnabledEv(
    const QNetworkAccessManager *self) {
  return self->isStrictTransportSecurityStoreEnabled();
}

//  void QNetworkAccessManager::addStrictTransportSecurityHosts(const
//      QList<QHstsPolicy> &knownHosts)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager31addStrictTransportSecurityHostsERK5QListI11QHstsPolicyE(
    QNetworkAccessManager *self,
    const QList<QHstsPolicy> *knownHosts) {
  self->addStrictTransportSecurityHosts(*knownHosts);
}

//  QList<QHstsPolicy> QNetworkAccessManager::strictTransportSecurityHosts()
//      const
extern "C" Q_DECL_EXPORT
QList<QHstsPolicy> *ritual_ZNK21QNetworkAccessManager28strictTransportSecurityHostsEv(
    const QNetworkAccessManager *self) {
  return new QList<QHstsPolicy>(self->strictTransportSecurityHosts());
}

//  QNetworkReply *QNetworkAccessManager::head(const QNetworkRequest
//      &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager4headERK15QNetworkRequest(
    QNetworkAccessManager *self,
    const QNetworkRequest *request) {
  return self->head(*request);
}

//  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequest(
    QNetworkAccessManager *self,
    const QNetworkRequest *request) {
  return self->get(*request);
}

//  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequestP9QIODevice(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->get(*request, data);
}

//  QNetworkReply *QNetworkAccessManager::get(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3getERK15QNetworkRequestRK10QByteArray(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->get(*request, *data);
}

//  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
//      &request, QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestP9QIODevice(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->post(*request, data);
}

//  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
//      &request, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestRK10QByteArray(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->post(*request, *data);
}

//  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest &request,
//      QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestP9QIODevice(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    QIODevice *data) {
  return self->put(*request, data);
}

//  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest &request,
//      const QByteArray &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestRK10QByteArray(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *data) {
  return self->put(*request, *data);
}

//  QNetworkReply *QNetworkAccessManager::deleteResource(const
//      QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager14deleteResourceERK15QNetworkRequest(
    QNetworkAccessManager *self,
    const QNetworkRequest *request) {
  return self->deleteResource(*request);
}

//  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &verb, QIODevice *data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayP9QIODevice(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *verb,
    QIODevice *data) {
  return self->sendCustomRequest(*request, *verb, data);
}

//  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &verb, const QByteArray
//      &data)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayS5_(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *verb,
    const QByteArray *data) {
  return self->sendCustomRequest(*request, *verb, *data);
}

#if QT_CONFIG(http) || defined(Q_OS_WASM)
//  QNetworkReply *QNetworkAccessManager::post(const QNetworkRequest
//      &request, QHttpMultiPart *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager4postERK15QNetworkRequestP14QHttpMultiPart(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *multiPart) {
  return self->post(*request, multiPart);
}
#endif  // QT_CONFIG(http) || defined(Q_OS_WASM)

#if QT_CONFIG(http) || defined(Q_OS_WASM)
//  QNetworkReply *QNetworkAccessManager::put(const QNetworkRequest &request,
//      QHttpMultiPart *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager3putERK15QNetworkRequestP14QHttpMultiPart(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    QHttpMultiPart *multiPart) {
  return self->put(*request, multiPart);
}
#endif  // QT_CONFIG(http) || defined(Q_OS_WASM)

#if QT_CONFIG(http) || defined(Q_OS_WASM)
//  QNetworkReply *QNetworkAccessManager::sendCustomRequest(const
//      QNetworkRequest &request, const QByteArray &verb, QHttpMultiPart
//      *multiPart)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager17sendCustomRequestERK15QNetworkRequestRK10QByteArrayP14QHttpMultiPart(
    QNetworkAccessManager *self,
    const QNetworkRequest *request,
    const QByteArray *verb,
    QHttpMultiPart *multiPart) {
  return self->sendCustomRequest(*request, *verb, multiPart);
}
#endif  // QT_CONFIG(http) || defined(Q_OS_WASM)

#if !defined(QT_NO_SSL)
//  void QNetworkAccessManager::connectToHostEncrypted(const QString
//      &hostName, quint16 port, const QSslConfiguration &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager22connectToHostEncryptedERK7QStringtRK17QSslConfiguration(
    QNetworkAccessManager *self,
    const QString *hostName,
    quint16 port,
    const QSslConfiguration *sslConfiguration) {
  self->connectToHostEncrypted(*hostName, port, *sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QNetworkAccessManager::connectToHostEncrypted(const QString
//      &hostName, quint16 port, const QSslConfiguration &sslConfiguration,
//      const QString &peerName)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager22connectToHostEncryptedERK7QStringtRK17QSslConfigurationS2_(
    QNetworkAccessManager *self,
    const QString *hostName,
    quint16 port,
    const QSslConfiguration *sslConfiguration,
    const QString *peerName) {
  self->connectToHostEncrypted(
      *hostName,
      port,
      *sslConfiguration,
      *peerName);
}
#endif  // !defined(QT_NO_SSL)

//  void QNetworkAccessManager::connectToHost(const QString &hostName,
//      quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager13connectToHostERK7QStringt(
    QNetworkAccessManager *self,
    const QString *hostName,
    quint16 port) {
  self->connectToHost(*hostName, port);
}

//  void
//      QNetworkAccessManager::setRedirectPolicy(QNetworkRequest::RedirectPol
//      icy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager17setRedirectPolicyEN15QNetworkRequest14RedirectPolicyE(
    QNetworkAccessManager *self,
    QNetworkRequest::RedirectPolicy policy) {
  self->setRedirectPolicy(policy);
}

//  QNetworkRequest::RedirectPolicy QNetworkAccessManager::redirectPolicy()
//      const
extern "C" Q_DECL_EXPORT
QNetworkRequest::RedirectPolicy ritual_ZNK21QNetworkAccessManager14redirectPolicyEv(
    const QNetworkAccessManager *self) {
  return self->redirectPolicy();
}

//  bool QNetworkAccessManager::autoDeleteReplies() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QNetworkAccessManager17autoDeleteRepliesEv(
    const QNetworkAccessManager *self) {
  return self->autoDeleteReplies();
}

//  void QNetworkAccessManager::setAutoDeleteReplies(bool autoDelete)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager20setAutoDeleteRepliesEb(
    QNetworkAccessManager *self,
    bool autoDelete) {
  self->setAutoDeleteReplies(autoDelete);
}

//  int QNetworkAccessManager::transferTimeout() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QNetworkAccessManager15transferTimeoutEv(
    const QNetworkAccessManager *self) {
  return self->transferTimeout();
}

//  void QNetworkAccessManager::setTransferTimeout(int timeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QNetworkAccessManager18setTransferTimeoutEi(
    QNetworkAccessManager *self,
    int timeout) {
  self->setTransferTimeout(timeout);
}

//  QNetworkReply *QNetworkAccessManager::createRequest(Operation op, const
//      QNetworkRequest &request, QIODevice *outgoingData)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_ZN21QNetworkAccessManager13createRequestENS_9OperationERK15QNetworkRequestP9QIODevice(
    QNetworkAccessManager *self,
    QNetworkAccessManager::Operation op,
    const QNetworkRequest *request,
    QIODevice *outgoingData) {
  return self->createRequest(op, *request, outgoingData);
}

//  QStringList QNetworkAccessManager::supportedSchemesImplementation() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK21QNetworkAccessManager30supportedSchemesImplementationEv(
    const QNetworkAccessManager *self) {
  return new QList<QString>(self->supportedSchemesImplementation());
}

//  QNetworkAccessManagerPrivate *QNetworkAccessManager::d_func()
extern "C" Q_DECL_EXPORT
QNetworkAccessManagerPrivate *ritual_ZN21QNetworkAccessManager6d_funcEv(
    QNetworkAccessManager *self) {
  return self->d_func();
}

//  const QNetworkAccessManagerPrivate *QNetworkAccessManager::d_func() const
extern "C" Q_DECL_EXPORT
const QNetworkAccessManagerPrivate *ritual_ZNK21QNetworkAccessManager6d_funcEv(
    const QNetworkAccessManager *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQNetworkAccessManager, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNetworkAccessManager(
    QNetworkAccessManager *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNetworkAccessManager *>(self)->take(key, call);
}

//  QNetworkReply *QNetworkAccessManager::createRequest(Operation op, const
//      QNetworkRequest &request, QIODevice *outgoingData)
extern "C" Q_DECL_EXPORT
QNetworkReply *ritual_own_ZN21QNetworkAccessManager13createRequestENS_9OperationERK15QNetworkRequestP9QIODevice(
    QNetworkAccessManager *self,
    QNetworkAccessManager::Operation op,
    const QNetworkRequest *request,
    QIODevice *outgoingData) {
  return static_cast<OwnQNetworkAccessManager *>(self)->OwnQNetworkAccessManager::createRequest(
      op,
      *request,
      outgoingData);
}
