//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/qcoapclient.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtCoap/qcoapclient.h>
#include <QtCore/qstring.h>
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtCore/qvariant.h>
#include <QtNetwork/qnetworkinterface.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QCoapClient that Python can take functions over in. Every QCoapClient
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapClientCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapClientCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapClientCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapClientCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapClientCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapClientCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapClientCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapClient : public QCoapClient {
public:
  using QCoapClient::QCoapClient;
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
      CuteQCoapClientCall0 call = reinterpret_cast<CuteQCoapClientCall0>(taken[0]);
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
      CuteQCoapClientCall1 call = reinterpret_cast<CuteQCoapClientCall1>(taken[1]);
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
      CuteQCoapClientCall2 call = reinterpret_cast<CuteQCoapClientCall2>(taken[2]);
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
      CuteQCoapClientCall3 call = reinterpret_cast<CuteQCoapClientCall3>(taken[3]);
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
      CuteQCoapClientCall4 call = reinterpret_cast<CuteQCoapClientCall4>(taken[4]);
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
      CuteQCoapClientCall5 call = reinterpret_cast<CuteQCoapClientCall5>(taken[5]);
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
      CuteQCoapClientCall6 call = reinterpret_cast<CuteQCoapClientCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapClient::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QCoapClient10metaObjectEv(
    const QCoapClient *self) {
  return self->metaObject();
}

//  QString QCoapClient::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QCoapClient2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QCoapClient::tr(s, c, n));
}

//  QCoapClient::QCoapClient(QtCoap::SecurityMode securityMode, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QCoapClient *ritual_ZN11QCoapClientC1EN6QtCoap12SecurityModeEP7QObject(
    QtCoap::SecurityMode securityMode,
    QObject *parent) {
  return new CuteQCoapClient(securityMode, parent);
}

//  QCoapClient::~QCoapClient()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClientD1Ev(QCoapClient *self) {
  delete self;
}

//  QCoapReply *QCoapClient::get(const QCoapRequest &request)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient3getERK12QCoapRequest(
    QCoapClient *self,
    const QCoapRequest *request) {
  return self->get(*request);
}

//  QCoapReply *QCoapClient::get(const QUrl &url)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient3getERK4QUrl(
    QCoapClient *self,
    const QUrl *url) {
  return self->get(*url);
}

//  QCoapReply *QCoapClient::put(const QCoapRequest &request, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient3putERK12QCoapRequestRK10QByteArray(
    QCoapClient *self,
    const QCoapRequest *request,
    const QByteArray *data) {
  return self->put(*request, *data);
}

//  QCoapReply *QCoapClient::put(const QCoapRequest &request, QIODevice
//      *device)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient3putERK12QCoapRequestP9QIODevice(
    QCoapClient *self,
    const QCoapRequest *request,
    QIODevice *device) {
  return self->put(*request, device);
}

//  QCoapReply *QCoapClient::put(const QUrl &url, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient3putERK4QUrlRK10QByteArray(
    QCoapClient *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->put(*url, *data);
}

//  QCoapReply *QCoapClient::post(const QCoapRequest &request, const
//      QByteArray &data)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient4postERK12QCoapRequestRK10QByteArray(
    QCoapClient *self,
    const QCoapRequest *request,
    const QByteArray *data) {
  return self->post(*request, *data);
}

//  QCoapReply *QCoapClient::post(const QCoapRequest &request, QIODevice
//      *device)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient4postERK12QCoapRequestP9QIODevice(
    QCoapClient *self,
    const QCoapRequest *request,
    QIODevice *device) {
  return self->post(*request, device);
}

//  QCoapReply *QCoapClient::post(const QUrl &url, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient4postERK4QUrlRK10QByteArray(
    QCoapClient *self,
    const QUrl *url,
    const QByteArray *data) {
  return self->post(*url, *data);
}

//  QCoapReply *QCoapClient::deleteResource(const QCoapRequest &request)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient14deleteResourceERK12QCoapRequest(
    QCoapClient *self,
    const QCoapRequest *request) {
  return self->deleteResource(*request);
}

//  QCoapReply *QCoapClient::deleteResource(const QUrl &url)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient14deleteResourceERK4QUrl(
    QCoapClient *self,
    const QUrl *url) {
  return self->deleteResource(*url);
}

//  QCoapReply *QCoapClient::observe(const QCoapRequest &request)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient7observeERK12QCoapRequest(
    QCoapClient *self,
    const QCoapRequest *request) {
  return self->observe(*request);
}

//  QCoapReply *QCoapClient::observe(const QUrl &request)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN11QCoapClient7observeERK4QUrl(
    QCoapClient *self,
    const QUrl *request) {
  return self->observe(*request);
}

//  void QCoapClient::cancelObserve(QCoapReply *notifiedReply)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient13cancelObserveEP10QCoapReply(
    QCoapClient *self,
    QCoapReply *notifiedReply) {
  self->cancelObserve(notifiedReply);
}

//  void QCoapClient::cancelObserve(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient13cancelObserveERK4QUrl(
    QCoapClient *self,
    const QUrl *url) {
  self->cancelObserve(*url);
}

//  void QCoapClient::disconnect()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient10disconnectEv(QCoapClient *self) {
  self->disconnect();
}

//  QCoapResourceDiscoveryReply *QCoapClient::discover(QtCoap::MulticastGroup
//      group, int port, const QString &discoveryPath)
extern "C" Q_DECL_EXPORT
QCoapResourceDiscoveryReply *ritual_ZN11QCoapClient8discoverEN6QtCoap14MulticastGroupEiRK7QString(
    QCoapClient *self,
    QtCoap::MulticastGroup group,
    int port,
    const QString *discoveryPath) {
  return self->discover(group, port, *discoveryPath);
}

//  QCoapResourceDiscoveryReply *QCoapClient::discover(const QUrl &baseUrl,
//      const QString &discoveryPath)
extern "C" Q_DECL_EXPORT
QCoapResourceDiscoveryReply *ritual_ZN11QCoapClient8discoverERK4QUrlRK7QString(
    QCoapClient *self,
    const QUrl *baseUrl,
    const QString *discoveryPath) {
  return self->discover(*baseUrl, *discoveryPath);
}

//  void QCoapClient::setSecurityConfiguration(const
//      QCoapSecurityConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient24setSecurityConfigurationERK26QCoapSecurityConfiguration(
    QCoapClient *self,
    const QCoapSecurityConfiguration *configuration) {
  self->setSecurityConfiguration(*configuration);
}

//  void QCoapClient::setBlockSize(quint16 blockSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient12setBlockSizeEt(
    QCoapClient *self,
    quint16 blockSize) {
  self->setBlockSize(blockSize);
}

//  void QCoapClient::setSocketOption(QAbstractSocket::SocketOption option,
//      const QVariant &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient15setSocketOptionEN15QAbstractSocket12SocketOptionERK8QVariant(
    QCoapClient *self,
    QAbstractSocket::SocketOption option,
    const QVariant *value) {
  self->setSocketOption(option, *value);
}

//  void QCoapClient::setMaximumServerResponseDelay(uint responseDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient29setMaximumServerResponseDelayEj(
    QCoapClient *self,
    uint responseDelay) {
  self->setMaximumServerResponseDelay(responseDelay);
}

//  void QCoapClient::setAckTimeout(uint ackTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient13setAckTimeoutEj(
    QCoapClient *self,
    uint ackTimeout) {
  self->setAckTimeout(ackTimeout);
}

//  void QCoapClient::setAckRandomFactor(double ackRandomFactor)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient18setAckRandomFactorEd(
    QCoapClient *self,
    double ackRandomFactor) {
  self->setAckRandomFactor(ackRandomFactor);
}

//  void QCoapClient::setMaximumRetransmitCount(uint maximumRetransmitCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient25setMaximumRetransmitCountEj(
    QCoapClient *self,
    uint maximumRetransmitCount) {
  self->setMaximumRetransmitCount(maximumRetransmitCount);
}

//  void QCoapClient::setMinimumTokenSize(int tokenSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient19setMinimumTokenSizeEi(
    QCoapClient *self,
    int tokenSize) {
  self->setMinimumTokenSize(tokenSize);
}

#if QT_CONFIG(networkinterface)
//  void QCoapClient::setBindInterface(const QNetworkInterface &iface)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QCoapClient16setBindInterfaceERK17QNetworkInterface(
    QCoapClient *self,
    const QNetworkInterface *iface) {
  self->setBindInterface(*iface);
}
#endif  // QT_CONFIG(networkinterface)

#if QT_CONFIG(networkinterface)
//  QNetworkInterface QCoapClient::bindInterface() const
extern "C" Q_DECL_EXPORT
QNetworkInterface *ritual_ZNK11QCoapClient13bindInterfaceEv(
    const QCoapClient *self) {
  return new QNetworkInterface(self->bindInterface());
}
#endif  // QT_CONFIG(networkinterface)

//  QCoapClientPrivate *QCoapClient::d_func()
extern "C" Q_DECL_EXPORT
QCoapClientPrivate *ritual_ZN11QCoapClient6d_funcEv(QCoapClient *self) {
  return self->d_func();
}

//  const QCoapClientPrivate *QCoapClient::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapClientPrivate *ritual_ZNK11QCoapClient6d_funcEv(
    const QCoapClient *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCoapClient, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapClient(
    QCoapClient *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapClient *>(self)->take(key, call);
}
