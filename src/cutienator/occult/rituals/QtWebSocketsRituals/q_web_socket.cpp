//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebSockets/qwebsocket.h, Qt 6.12.0. Changes made here are lost.
#include <QtWebSockets/qwebsocket.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qurl.h>
#include <QtNetwork/qnetworkrequest.h>
#include <QtWebSockets/qwebsockethandshakeoptions.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWebSocket that Python can take functions over in. Every QWebSocket
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebSocketCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebSocketCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebSocket : public QWebSocket {
public:
  using QWebSocket::QWebSocket;
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
      CuteQWebSocketCall0 call = reinterpret_cast<CuteQWebSocketCall0>(taken[0]);
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
      CuteQWebSocketCall1 call = reinterpret_cast<CuteQWebSocketCall1>(taken[1]);
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
      CuteQWebSocketCall2 call = reinterpret_cast<CuteQWebSocketCall2>(taken[2]);
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
      CuteQWebSocketCall3 call = reinterpret_cast<CuteQWebSocketCall3>(taken[3]);
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
      CuteQWebSocketCall4 call = reinterpret_cast<CuteQWebSocketCall4>(taken[4]);
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
      CuteQWebSocketCall5 call = reinterpret_cast<CuteQWebSocketCall5>(taken[5]);
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
      CuteQWebSocketCall6 call = reinterpret_cast<CuteQWebSocketCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebSocket::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QWebSocket10metaObjectEv(
    const QWebSocket *self) {
  return self->metaObject();
}

//  QString QWebSocket::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QWebSocket2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebSocket::tr(s, c, n));
}

//  QWebSocketPrivate *QWebSocket::d_func()
extern "C" Q_DECL_EXPORT
QWebSocketPrivate *ritual_ZN10QWebSocket6d_funcEv(QWebSocket *self) {
  return self->d_func();
}

//  const QWebSocketPrivate *QWebSocket::d_func() const
extern "C" Q_DECL_EXPORT
const QWebSocketPrivate *ritual_ZNK10QWebSocket6d_funcEv(
    const QWebSocket *self) {
  return self->d_func();
}

//  QWebSocket::QWebSocket(const QString &origin, QWebSocketProtocol::Version
//      version, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN10QWebSocketC1ERK7QStringN18QWebSocketProtocol7VersionEP7QObject(
    const QString *origin,
    QWebSocketProtocol::Version version,
    QObject *parent) {
  return new CuteQWebSocket(*origin, version, parent);
}

//  QWebSocket::~QWebSocket()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocketD1Ev(QWebSocket *self) {
  delete self;
}

//  void QWebSocket::abort()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket5abortEv(QWebSocket *self) {
  self->abort();
}

//  QString QWebSocket::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket11errorStringEv(const QWebSocket *self) {
  return new QString(self->errorString());
}

//  bool QWebSocket::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN10QWebSocket5flushEv(QWebSocket *self) {
  return self->flush();
}

//  bool QWebSocket::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10QWebSocket7isValidEv(const QWebSocket *self) {
  return self->isValid();
}

//  QHostAddress QWebSocket::localAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK10QWebSocket12localAddressEv(
    const QWebSocket *self) {
  return new QHostAddress(self->localAddress());
}

//  quint16 QWebSocket::localPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK10QWebSocket9localPortEv(const QWebSocket *self) {
  return self->localPort();
}

//  QAbstractSocket::PauseModes QWebSocket::pauseMode() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QWebSocket9pauseModeEv(const QWebSocket *self) {
  return static_cast<int>(self->pauseMode().toInt());
}

//  QHostAddress QWebSocket::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK10QWebSocket11peerAddressEv(const QWebSocket *self) {
  return new QHostAddress(self->peerAddress());
}

//  QString QWebSocket::peerName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket8peerNameEv(const QWebSocket *self) {
  return new QString(self->peerName());
}

//  quint16 QWebSocket::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK10QWebSocket8peerPortEv(const QWebSocket *self) {
  return self->peerPort();
}

#if !defined(QT_NO_NETWORKPROXY)
//  QNetworkProxy QWebSocket::proxy() const
extern "C" Q_DECL_EXPORT
QNetworkProxy *ritual_ZNK10QWebSocket5proxyEv(const QWebSocket *self) {
  return new QNetworkProxy(self->proxy());
}
#endif  // !defined(QT_NO_NETWORKPROXY)

#if !defined(QT_NO_NETWORKPROXY)
//  void QWebSocket::setProxy(const QNetworkProxy &networkProxy)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket8setProxyERK13QNetworkProxy(
    QWebSocket *self,
    const QNetworkProxy *networkProxy) {
  self->setProxy(*networkProxy);
}
#endif  // !defined(QT_NO_NETWORKPROXY)

//  void QWebSocket::setMaskGenerator(const QMaskGenerator *maskGenerator)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket16setMaskGeneratorEPK14QMaskGenerator(
    QWebSocket *self,
    const QMaskGenerator *maskGenerator) {
  self->setMaskGenerator(maskGenerator);
}

//  const QMaskGenerator *QWebSocket::maskGenerator() const
extern "C" Q_DECL_EXPORT
const QMaskGenerator *ritual_ZNK10QWebSocket13maskGeneratorEv(
    const QWebSocket *self) {
  return self->maskGenerator();
}

//  qint64 QWebSocket::readBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QWebSocket14readBufferSizeEv(const QWebSocket *self) {
  return self->readBufferSize();
}

//  void QWebSocket::setReadBufferSize(qint64 size)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket17setReadBufferSizeEx(
    QWebSocket *self,
    qint64 size) {
  self->setReadBufferSize(size);
}

//  void QWebSocket::resume()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket6resumeEv(QWebSocket *self) {
  self->resume();
}

//  void QWebSocket::setPauseMode(QAbstractSocket::PauseModes pauseMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket12setPauseModeE6QFlagsIN15QAbstractSocket9PauseModeEE(
    QWebSocket *self,
    int pauseMode) {
  self->setPauseMode(QFlags<QAbstractSocket::PauseMode>::fromInt(pauseMode));
}

//  QAbstractSocket::SocketState QWebSocket::state() const
extern "C" Q_DECL_EXPORT
QAbstractSocket::SocketState ritual_ZNK10QWebSocket5stateEv(
    const QWebSocket *self) {
  return self->state();
}

//  QWebSocketProtocol::Version QWebSocket::version() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::Version ritual_ZNK10QWebSocket7versionEv(
    const QWebSocket *self) {
  return self->version();
}

//  QString QWebSocket::resourceName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket12resourceNameEv(const QWebSocket *self) {
  return new QString(self->resourceName());
}

//  QUrl QWebSocket::requestUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK10QWebSocket10requestUrlEv(const QWebSocket *self) {
  return new QUrl(self->requestUrl());
}

//  QNetworkRequest QWebSocket::request() const
extern "C" Q_DECL_EXPORT
QNetworkRequest *ritual_ZNK10QWebSocket7requestEv(const QWebSocket *self) {
  return new QNetworkRequest(self->request());
}

//  QWebSocketHandshakeOptions QWebSocket::handshakeOptions() const
extern "C" Q_DECL_EXPORT
QWebSocketHandshakeOptions *ritual_ZNK10QWebSocket16handshakeOptionsEv(
    const QWebSocket *self) {
  return new QWebSocketHandshakeOptions(self->handshakeOptions());
}

//  QString QWebSocket::origin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket6originEv(const QWebSocket *self) {
  return new QString(self->origin());
}

//  QString QWebSocket::subprotocol() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket11subprotocolEv(const QWebSocket *self) {
  return new QString(self->subprotocol());
}

//  QWebSocketProtocol::CloseCode QWebSocket::closeCode() const
extern "C" Q_DECL_EXPORT
QWebSocketProtocol::CloseCode ritual_ZNK10QWebSocket9closeCodeEv(
    const QWebSocket *self) {
  return self->closeCode();
}

//  QString QWebSocket::closeReason() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QWebSocket11closeReasonEv(const QWebSocket *self) {
  return new QString(self->closeReason());
}

//  qint64 QWebSocket::sendTextMessage(const QString &message)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QWebSocket15sendTextMessageERK7QString(
    QWebSocket *self,
    const QString *message) {
  return self->sendTextMessage(*message);
}

//  qint64 QWebSocket::sendBinaryMessage(const QByteArray &data)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN10QWebSocket17sendBinaryMessageERK10QByteArray(
    QWebSocket *self,
    const QByteArray *data) {
  return self->sendBinaryMessage(*data);
}

#if !defined(QT_NO_SSL)
//  void QWebSocket::ignoreSslErrors(const QList<QSslError> &errors)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket15ignoreSslErrorsERK5QListI9QSslErrorE(
    QWebSocket *self,
    const QList<QSslError> *errors) {
  self->ignoreSslErrors(*errors);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocket::continueInterruptedHandshake()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket28continueInterruptedHandshakeEv(
    QWebSocket *self) {
  self->continueInterruptedHandshake();
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  void QWebSocket::setSslConfiguration(const QSslConfiguration
//      &sslConfiguration)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket19setSslConfigurationERK17QSslConfiguration(
    QWebSocket *self,
    const QSslConfiguration *sslConfiguration) {
  self->setSslConfiguration(*sslConfiguration);
}
#endif  // !defined(QT_NO_SSL)

#if !defined(QT_NO_SSL)
//  QSslConfiguration QWebSocket::sslConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK10QWebSocket16sslConfigurationEv(
    const QWebSocket *self) {
  return new QSslConfiguration(self->sslConfiguration());
}
#endif  // !defined(QT_NO_SSL)

//  qint64 QWebSocket::bytesToWrite() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK10QWebSocket12bytesToWriteEv(const QWebSocket *self) {
  return self->bytesToWrite();
}

//  void QWebSocket::setMaxAllowedIncomingFrameSize(quint64
//      maxAllowedIncomingFrameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket30setMaxAllowedIncomingFrameSizeEy(
    QWebSocket *self,
    quint64 maxAllowedIncomingFrameSize) {
  self->setMaxAllowedIncomingFrameSize(maxAllowedIncomingFrameSize);
}

//  quint64 QWebSocket::maxAllowedIncomingFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK10QWebSocket27maxAllowedIncomingFrameSizeEv(
    const QWebSocket *self) {
  return self->maxAllowedIncomingFrameSize();
}

//  void QWebSocket::setMaxAllowedIncomingMessageSize(quint64
//      maxAllowedIncomingMessageSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket32setMaxAllowedIncomingMessageSizeEy(
    QWebSocket *self,
    quint64 maxAllowedIncomingMessageSize) {
  self->setMaxAllowedIncomingMessageSize(maxAllowedIncomingMessageSize);
}

//  quint64 QWebSocket::maxAllowedIncomingMessageSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK10QWebSocket29maxAllowedIncomingMessageSizeEv(
    const QWebSocket *self) {
  return self->maxAllowedIncomingMessageSize();
}

//  quint64 QWebSocket::maxIncomingMessageSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN10QWebSocket22maxIncomingMessageSizeEv() {
  return QWebSocket::maxIncomingMessageSize();
}

//  quint64 QWebSocket::maxIncomingFrameSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN10QWebSocket20maxIncomingFrameSizeEv() {
  return QWebSocket::maxIncomingFrameSize();
}

//  void QWebSocket::setOutgoingFrameSize(quint64 outgoingFrameSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket20setOutgoingFrameSizeEy(
    QWebSocket *self,
    quint64 outgoingFrameSize) {
  self->setOutgoingFrameSize(outgoingFrameSize);
}

//  quint64 QWebSocket::outgoingFrameSize() const
extern "C" Q_DECL_EXPORT
quint64 ritual_ZNK10QWebSocket17outgoingFrameSizeEv(const QWebSocket *self) {
  return self->outgoingFrameSize();
}

//  quint64 QWebSocket::maxOutgoingFrameSize()
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN10QWebSocket20maxOutgoingFrameSizeEv() {
  return QWebSocket::maxOutgoingFrameSize();
}

//  void QWebSocket::close(QWebSocketProtocol::CloseCode closeCode, const
//      QString &reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket5closeEN18QWebSocketProtocol9CloseCodeERK7QString(
    QWebSocket *self,
    QWebSocketProtocol::CloseCode closeCode,
    const QString *reason) {
  self->close(closeCode, *reason);
}

//  void QWebSocket::open(const QUrl &url)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket4openERK4QUrl(QWebSocket *self, const QUrl *url) {
  self->open(*url);
}

//  void QWebSocket::open(const QNetworkRequest &request)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket4openERK15QNetworkRequest(
    QWebSocket *self,
    const QNetworkRequest *request) {
  self->open(*request);
}

//  void QWebSocket::open(const QUrl &url, const QWebSocketHandshakeOptions
//      &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket4openERK4QUrlRK26QWebSocketHandshakeOptions(
    QWebSocket *self,
    const QUrl *url,
    const QWebSocketHandshakeOptions *options) {
  self->open(*url, *options);
}

//  void QWebSocket::open(const QNetworkRequest &request, const
//      QWebSocketHandshakeOptions &options)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket4openERK15QNetworkRequestRK26QWebSocketHandshakeOptions(
    QWebSocket *self,
    const QNetworkRequest *request,
    const QWebSocketHandshakeOptions *options) {
  self->open(*request, *options);
}

//  void QWebSocket::ping(const QByteArray &payload)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket4pingERK10QByteArray(
    QWebSocket *self,
    const QByteArray *payload) {
  self->ping(*payload);
}

#if !defined(QT_NO_SSL)
//  void QWebSocket::ignoreSslErrors()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QWebSocket15ignoreSslErrorsEv(QWebSocket *self) {
  self->ignoreSslErrors();
}
#endif  // !defined(QT_NO_SSL)

//  QWebSocket::QWebSocket(QTcpSocket *pTcpSocket,
//      QWebSocketProtocol::Version version, QObject *parent)
extern "C" Q_DECL_EXPORT
QWebSocket *ritual_ZN10QWebSocketC1EP10QTcpSocketN18QWebSocketProtocol7VersionEP7QObject(
    QTcpSocket *pTcpSocket,
    QWebSocketProtocol::Version version,
    QObject *parent) {
  return new CuteQWebSocket(pTcpSocket, version, parent);
}

//  a Python function taken by a CuteQWebSocket, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebSocket(QWebSocket *self, const char *key, void *call) {
  return static_cast<CuteQWebSocket *>(self)->take(key, call);
}
