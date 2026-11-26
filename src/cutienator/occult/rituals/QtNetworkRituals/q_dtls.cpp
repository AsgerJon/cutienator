//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdtls.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dtls) && QT_CONFIG(ssl)
#if QT_CONFIG(dtls)
#include <QtNetwork/qdtls.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qsslerror.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QDtls that Python can take functions over in. Every QDtls
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDtlsCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDtlsCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDtls : public QDtls {
public:
  using QDtls::QDtls;
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
      CuteQDtlsCall0 call = reinterpret_cast<CuteQDtlsCall0>(taken[0]);
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
      CuteQDtlsCall1 call = reinterpret_cast<CuteQDtlsCall1>(taken[1]);
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
      CuteQDtlsCall2 call = reinterpret_cast<CuteQDtlsCall2>(taken[2]);
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
      CuteQDtlsCall3 call = reinterpret_cast<CuteQDtlsCall3>(taken[3]);
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
      CuteQDtlsCall4 call = reinterpret_cast<CuteQDtlsCall4>(taken[4]);
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
      CuteQDtlsCall5 call = reinterpret_cast<CuteQDtlsCall5>(taken[5]);
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
      CuteQDtlsCall6 call = reinterpret_cast<CuteQDtlsCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDtls::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK5QDtls10metaObjectEv(const QDtls *self) {
  return self->metaObject();
}

//  void *QDtls::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN5QDtls11qt_metacastEPKc(QDtls *self, const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDtls::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN5QDtls11qt_metacallEN11QMetaObject4CallEiPPv(
    QDtls *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDtls::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN5QDtls2trEPKcS1_i(const char *s, const char *c, int n) {
  return new QString(QDtls::tr(s, c, n));
}

//  QDtls::QDtls(QSslSocket::SslMode mode, QObject *parent)
extern "C" Q_DECL_EXPORT
QDtls *ritual_ZN5QDtlsC1EN10QSslSocket7SslModeEP7QObject(
    QSslSocket::SslMode mode,
    QObject *parent) {
  return new CuteQDtls(mode, parent);
}

//  QDtls::~QDtls()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDtlsD1Ev(QDtls *self) {
  delete self;
}

//  bool QDtls::setPeer(const QHostAddress &address, quint16 port, const
//      QString &verificationName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls7setPeerERK12QHostAddresstRK7QString(
    QDtls *self,
    const QHostAddress *address,
    quint16 port,
    const QString *verificationName) {
  return self->setPeer(*address, port, *verificationName);
}

//  bool QDtls::setPeerVerificationName(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls23setPeerVerificationNameERK7QString(
    QDtls *self,
    const QString *name) {
  return self->setPeerVerificationName(*name);
}

//  QHostAddress QDtls::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK5QDtls11peerAddressEv(const QDtls *self) {
  return new QHostAddress(self->peerAddress());
}

//  quint16 QDtls::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK5QDtls8peerPortEv(const QDtls *self) {
  return self->peerPort();
}

//  QString QDtls::peerVerificationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDtls20peerVerificationNameEv(const QDtls *self) {
  return new QString(self->peerVerificationName());
}

//  QSslSocket::SslMode QDtls::sslMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::SslMode ritual_ZNK5QDtls7sslModeEv(const QDtls *self) {
  return self->sslMode();
}

//  void QDtls::setMtuHint(quint16 mtuHint)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDtls10setMtuHintEt(QDtls *self, quint16 mtuHint) {
  self->setMtuHint(mtuHint);
}

//  quint16 QDtls::mtuHint() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK5QDtls7mtuHintEv(const QDtls *self) {
  return self->mtuHint();
}

//  bool QDtls::setCookieGeneratorParameters(const GeneratorParameters
//      &params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls28setCookieGeneratorParametersERKN19QDtlsClientVerifier19GeneratorParametersE(
    QDtls *self,
    const QDtlsClientVerifier::GeneratorParameters *params) {
  return self->setCookieGeneratorParameters(*params);
}

//  GeneratorParameters QDtls::cookieGeneratorParameters() const
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier::GeneratorParameters *ritual_ZNK5QDtls25cookieGeneratorParametersEv(
    const QDtls *self) {
  return new QDtlsClientVerifier::GeneratorParameters(
      self->cookieGeneratorParameters());
}

//  bool QDtls::setDtlsConfiguration(const QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls20setDtlsConfigurationERK17QSslConfiguration(
    QDtls *self,
    const QSslConfiguration *configuration) {
  return self->setDtlsConfiguration(*configuration);
}

//  QSslConfiguration QDtls::dtlsConfiguration() const
extern "C" Q_DECL_EXPORT
QSslConfiguration *ritual_ZNK5QDtls17dtlsConfigurationEv(const QDtls *self) {
  return new QSslConfiguration(self->dtlsConfiguration());
}

//  HandshakeState QDtls::handshakeState() const
extern "C" Q_DECL_EXPORT
QDtls::HandshakeState ritual_ZNK5QDtls14handshakeStateEv(const QDtls *self) {
  return self->handshakeState();
}

//  bool QDtls::doHandshake(QUdpSocket *socket, const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls11doHandshakeEP10QUdpSocketRK10QByteArray(
    QDtls *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->doHandshake(socket, *dgram);
}

//  bool QDtls::handleTimeout(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls13handleTimeoutEP10QUdpSocket(
    QDtls *self,
    QUdpSocket *socket) {
  return self->handleTimeout(socket);
}

//  bool QDtls::resumeHandshake(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls15resumeHandshakeEP10QUdpSocket(
    QDtls *self,
    QUdpSocket *socket) {
  return self->resumeHandshake(socket);
}

//  bool QDtls::abortHandshake(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls14abortHandshakeEP10QUdpSocket(
    QDtls *self,
    QUdpSocket *socket) {
  return self->abortHandshake(socket);
}

//  bool QDtls::shutdown(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls8shutdownEP10QUdpSocket(
    QDtls *self,
    QUdpSocket *socket) {
  return self->shutdown(socket);
}

//  bool QDtls::isConnectionEncrypted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK5QDtls21isConnectionEncryptedEv(const QDtls *self) {
  return self->isConnectionEncrypted();
}

//  QSslCipher QDtls::sessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK5QDtls13sessionCipherEv(const QDtls *self) {
  return new QSslCipher(self->sessionCipher());
}

//  QSsl::SslProtocol QDtls::sessionProtocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK5QDtls15sessionProtocolEv(const QDtls *self) {
  return self->sessionProtocol();
}

//  qint64 QDtls::writeDatagramEncrypted(QUdpSocket *socket, const QByteArray
//      &dgram)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN5QDtls22writeDatagramEncryptedEP10QUdpSocketRK10QByteArray(
    QDtls *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->writeDatagramEncrypted(socket, *dgram);
}

//  QByteArray QDtls::decryptDatagram(QUdpSocket *socket, const QByteArray
//      &dgram)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN5QDtls15decryptDatagramEP10QUdpSocketRK10QByteArray(
    QDtls *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return new QByteArray(self->decryptDatagram(socket, *dgram));
}

//  QDtlsError QDtls::dtlsError() const
extern "C" Q_DECL_EXPORT
QDtlsError ritual_ZNK5QDtls9dtlsErrorEv(const QDtls *self) {
  return self->dtlsError();
}

//  QString QDtls::dtlsErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK5QDtls15dtlsErrorStringEv(const QDtls *self) {
  return new QString(self->dtlsErrorString());
}

//  QList<QSslError> QDtls::peerVerificationErrors() const
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_ZNK5QDtls22peerVerificationErrorsEv(
    const QDtls *self) {
  return new QList<QSslError>(self->peerVerificationErrors());
}

//  void QDtls::ignoreVerificationErrors(const QList<QSslError>
//      &errorsToIgnore)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDtls24ignoreVerificationErrorsERK5QListI9QSslErrorE(
    QDtls *self,
    const QList<QSslError> *errorsToIgnore) {
  self->ignoreVerificationErrors(*errorsToIgnore);
}

//  void QDtls::pskRequired(QSslPreSharedKeyAuthenticator *authenticator)
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDtls11pskRequiredEP29QSslPreSharedKeyAuthenticator(
    QDtls *self,
    QSslPreSharedKeyAuthenticator *authenticator) {
  self->pskRequired(authenticator);
}

//  void QDtls::handshakeTimeout()
extern "C" Q_DECL_EXPORT
void ritual_ZN5QDtls16handshakeTimeoutEv(QDtls *self) {
  self->handshakeTimeout();
}

//  bool QDtls::startHandshake(QUdpSocket *socket, const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls14startHandshakeEP10QUdpSocketRK10QByteArray(
    QDtls *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->startHandshake(socket, *dgram);
}

//  bool QDtls::continueHandshake(QUdpSocket *socket, const QByteArray
//      &dgram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN5QDtls17continueHandshakeEP10QUdpSocketRK10QByteArray(
    QDtls *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->continueHandshake(socket, *dgram);
}

//  QDtlsPrivate *QDtls::d_func()
extern "C" Q_DECL_EXPORT
QDtlsPrivate *ritual_ZN5QDtls6d_funcEv(QDtls *self) {
  return self->d_func();
}

//  const QDtlsPrivate *QDtls::d_func() const
extern "C" Q_DECL_EXPORT
const QDtlsPrivate *ritual_ZNK5QDtls6d_funcEv(const QDtls *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDtls, for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDtls(QDtls *self, const char *key, void *call) {
  return static_cast<CuteQDtls *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dtls)
#endif  // QT_CONFIG(dtls) && QT_CONFIG(ssl)
