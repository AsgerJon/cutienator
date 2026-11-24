//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslsocket_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/qsslsocket.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslsocket_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qsslellipticcurve.h>
#include <QtNetwork/qsslcertificate.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qnetworkproxy.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QSslSocketPrivate that Python can take functions over in. Every QSslSocketPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQSslSocketPrivateCall0)(const void *, const QHostAddress *, quint16, int, const QNetworkInterface *, int *);
typedef const QByteArray * (*CuteQSslSocketPrivateCall1)(const void *, qint64, int *);
typedef bool (*CuteQSslSocketPrivateCall2)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall3)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall4)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall5)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall6)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall7)(const void *, int *);
#if !defined(QT_NO_NETWORKPROXY)
typedef void (*CuteQSslSocketPrivateCall8)(const void *, const QNetworkProxy *, QAuthenticator *, int *);
#endif  // !defined(QT_NO_NETWORKPROXY)
typedef bool (*CuteQSslSocketPrivateCall9)(const void *, int *);
typedef void (*CuteQSslSocketPrivateCall10)(const void *, int *);
typedef bool (*CuteQSslSocketPrivateCall11)(const void *, int *);
typedef bool (*CuteQSslSocketPrivateCall12)(const void *, char, int *);
class CuteQSslSocketPrivate : public QSslSocketPrivate {
public:
  using QSslSocketPrivate::QSslSocketPrivate;
  void *taken[13] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate5flushEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver16readNotificationEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17writeNotificationEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver21exceptionNotificationEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver17closeNotificationEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver22connectionNotificationEv")) {
      taken[7] = call;
      return true;
    }
#if !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN29QAbstractSocketEngineReceiver27proxyAuthenticationRequiredERK13QNetworkProxyP14QAuthenticator")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_NETWORKPROXY)
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate19canReadNotificationEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate22configureCreatedSocketEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN22QAbstractSocketPrivate13writeToSocketEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[12] = call;
      return true;
    }
    return false;
  }

  //  bool QSslSocketPrivate::bind(const QHostAddress &address, quint16 a1,
  //      QAbstractSocket::BindMode a2, const QNetworkInterface *iface)
  bool bind(
      const QHostAddress &address,
      quint16 a1,
      QAbstractSocket::BindMode a2,
      const QNetworkInterface *iface) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSslSocketPrivateCall0 call = reinterpret_cast<CuteQSslSocketPrivateCall0>(taken[0]);
      bool given = call(this, &address, a1, static_cast<int>(a2.toInt()), iface, &handled);
      if (handled) return given;
    }
    return QSslSocketPrivate::bind(address, a1, a2, iface);
  }

  //  QByteArray QSslSocketPrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSslSocketPrivateCall1 call = reinterpret_cast<CuteQSslSocketPrivateCall1>(taken[1]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QSslSocketPrivate::peek(maxSize);
  }

  //  bool QSslSocketPrivate::flush()
  bool flush() override {
    if (taken[2]) {
      int handled = 0;
      CuteQSslSocketPrivateCall2 call = reinterpret_cast<CuteQSslSocketPrivateCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSslSocketPrivate::flush();
  }

  //  void QAbstractSocketPrivate::readNotification()
  void readNotification() override {
    if (taken[3]) {
      int handled = 0;
      CuteQSslSocketPrivateCall3 call = reinterpret_cast<CuteQSslSocketPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::readNotification();
  }

  //  void QAbstractSocketPrivate::writeNotification()
  void writeNotification() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSslSocketPrivateCall4 call = reinterpret_cast<CuteQSslSocketPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::writeNotification();
  }

  //  void QAbstractSocketPrivate::exceptionNotification()
  void exceptionNotification() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSslSocketPrivateCall5 call = reinterpret_cast<CuteQSslSocketPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::exceptionNotification();
  }

  //  void QAbstractSocketPrivate::closeNotification()
  void closeNotification() override {
    if (taken[6]) {
      int handled = 0;
      CuteQSslSocketPrivateCall6 call = reinterpret_cast<CuteQSslSocketPrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::closeNotification();
  }

  //  void QAbstractSocketPrivate::connectionNotification()
  void connectionNotification() override {
    if (taken[7]) {
      int handled = 0;
      CuteQSslSocketPrivateCall7 call = reinterpret_cast<CuteQSslSocketPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::connectionNotification();
  }

#if !defined(QT_NO_NETWORKPROXY)
  //  void QAbstractSocketPrivate::proxyAuthenticationRequired(const
  //      QNetworkProxy &proxy, QAuthenticator *authenticator)
  void proxyAuthenticationRequired(
      const QNetworkProxy &proxy,
      QAuthenticator *authenticator) override {
    if (taken[8]) {
      int handled = 0;
      CuteQSslSocketPrivateCall8 call = reinterpret_cast<CuteQSslSocketPrivateCall8>(taken[8]);
      call(this, &proxy, authenticator, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::proxyAuthenticationRequired(proxy, authenticator);
  }
#endif  // !defined(QT_NO_NETWORKPROXY)

  //  bool QAbstractSocketPrivate::canReadNotification()
  bool canReadNotification() override {
    if (taken[9]) {
      int handled = 0;
      CuteQSslSocketPrivateCall9 call = reinterpret_cast<CuteQSslSocketPrivateCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::canReadNotification();
  }

  //  void QAbstractSocketPrivate::configureCreatedSocket()
  void configureCreatedSocket() override {
    if (taken[10]) {
      int handled = 0;
      CuteQSslSocketPrivateCall10 call = reinterpret_cast<CuteQSslSocketPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractSocketPrivate::configureCreatedSocket();
  }

  //  bool QAbstractSocketPrivate::writeToSocket()
  bool writeToSocket() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSslSocketPrivateCall11 call = reinterpret_cast<CuteQSslSocketPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractSocketPrivate::writeToSocket();
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[12]) {
      int handled = 0;
      CuteQSslSocketPrivateCall12 call = reinterpret_cast<CuteQSslSocketPrivateCall12>(taken[12]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }
};

//  QSslSocket *QSslSocketPrivate::q_func()
extern "C" Q_DECL_EXPORT
QSslSocket *ritual_ZN17QSslSocketPrivate6q_funcEv(QSslSocketPrivate *self) {
  return self->q_func();
}

//  const QSslSocket *QSslSocketPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QSslSocket *ritual_ZNK17QSslSocketPrivate6q_funcEv(
    const QSslSocketPrivate *self) {
  return self->q_func();
}

//  QSslSocketPrivate::QSslSocketPrivate()
extern "C" Q_DECL_EXPORT
QSslSocketPrivate *ritual_ZN17QSslSocketPrivateC1Ev() {
  return new CuteQSslSocketPrivate();
}

//  QSslSocketPrivate::~QSslSocketPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivateD1Ev(QSslSocketPrivate *self) {
  delete self;
}

//  void QSslSocketPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate4initEv(QSslSocketPrivate *self) {
  self->init();
}

//  bool QSslSocketPrivate::verifyProtocolSupported(const char *where)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate23verifyProtocolSupportedEPKc(
    QSslSocketPrivate *self,
    const char *where) {
  return self->verifyProtocolSupported(where);
}

//  bool QSslSocketPrivate::supportsSsl()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate11supportsSslEv() {
  return QSslSocketPrivate::supportsSsl();
}

//  void QSslSocketPrivate::ensureInitialized()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate17ensureInitializedEv() {
  QSslSocketPrivate::ensureInitialized();
}

//  QList<QSslCipher> QSslSocketPrivate::defaultCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN17QSslSocketPrivate14defaultCiphersEv() {
  return new QList<QSslCipher>(QSslSocketPrivate::defaultCiphers());
}

//  QList<QSslCipher> QSslSocketPrivate::defaultDtlsCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN17QSslSocketPrivate18defaultDtlsCiphersEv() {
  return new QList<QSslCipher>(QSslSocketPrivate::defaultDtlsCiphers());
}

//  QList<QSslCipher> QSslSocketPrivate::supportedCiphers()
extern "C" Q_DECL_EXPORT
QList<QSslCipher> *ritual_ZN17QSslSocketPrivate16supportedCiphersEv() {
  return new QList<QSslCipher>(QSslSocketPrivate::supportedCiphers());
}

//  void QSslSocketPrivate::setDefaultCiphers(const QList<QSslCipher>
//      &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate17setDefaultCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QSslSocketPrivate::setDefaultCiphers(*ciphers);
}

//  void QSslSocketPrivate::setDefaultDtlsCiphers(const QList<QSslCipher>
//      &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate21setDefaultDtlsCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QSslSocketPrivate::setDefaultDtlsCiphers(*ciphers);
}

//  void QSslSocketPrivate::setDefaultSupportedCiphers(const
//      QList<QSslCipher> &ciphers)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate26setDefaultSupportedCiphersERK5QListI10QSslCipherE(
    const QList<QSslCipher> *ciphers) {
  QSslSocketPrivate::setDefaultSupportedCiphers(*ciphers);
}

//  QList<QSslEllipticCurve> QSslSocketPrivate::supportedEllipticCurves()
extern "C" Q_DECL_EXPORT
QList<QSslEllipticCurve> *ritual_ZN17QSslSocketPrivate23supportedEllipticCurvesEv() {
  return new QList<QSslEllipticCurve>(
      QSslSocketPrivate::supportedEllipticCurves());
}

//  void QSslSocketPrivate::setDefaultSupportedEllipticCurves(const
//      QList<QSslEllipticCurve> &curves)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate33setDefaultSupportedEllipticCurvesERK5QListI17QSslEllipticCurveE(
    const QList<QSslEllipticCurve> *curves) {
  QSslSocketPrivate::setDefaultSupportedEllipticCurves(*curves);
}

//  void QSslSocketPrivate::resetDefaultEllipticCurves()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate26resetDefaultEllipticCurvesEv() {
  QSslSocketPrivate::resetDefaultEllipticCurves();
}

//  QList<QSslCertificate> QSslSocketPrivate::defaultCaCertificates()
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN17QSslSocketPrivate21defaultCaCertificatesEv() {
  return new QList<QSslCertificate>(
      QSslSocketPrivate::defaultCaCertificates());
}

//  QList<QSslCertificate> QSslSocketPrivate::systemCaCertificates()
extern "C" Q_DECL_EXPORT
QList<QSslCertificate> *ritual_ZN17QSslSocketPrivate20systemCaCertificatesEv() {
  return new QList<QSslCertificate>(
      QSslSocketPrivate::systemCaCertificates());
}

//  void QSslSocketPrivate::setDefaultCaCertificates(const
//      QList<QSslCertificate> &certs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate24setDefaultCaCertificatesERK5QListI15QSslCertificateE(
    const QList<QSslCertificate> *certs) {
  QSslSocketPrivate::setDefaultCaCertificates(*certs);
}

//  void QSslSocketPrivate::addDefaultCaCertificate(const QSslCertificate
//      &cert)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate23addDefaultCaCertificateERK15QSslCertificate(
    const QSslCertificate *cert) {
  QSslSocketPrivate::addDefaultCaCertificate(*cert);
}

//  void QSslSocketPrivate::addDefaultCaCertificates(const
//      QList<QSslCertificate> &certs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate24addDefaultCaCertificatesERK5QListI15QSslCertificateE(
    const QList<QSslCertificate> *certs) {
  QSslSocketPrivate::addDefaultCaCertificates(*certs);
}

//  bool QSslSocketPrivate::isMatchingHostname(const QSslCertificate &cert,
//      const QString &peerName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate18isMatchingHostnameERK15QSslCertificateRK7QString(
    const QSslCertificate *cert,
    const QString *peerName) {
  return QSslSocketPrivate::isMatchingHostname(*cert, *peerName);
}

//  bool QSslSocketPrivate::isMatchingHostname(const QString &cn, const
//      QString &hostname)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate18isMatchingHostnameERK7QStringS2_(
    const QString *cn,
    const QString *hostname) {
  return QSslSocketPrivate::isMatchingHostname(*cn, *hostname);
}

//  void QSslSocketPrivate::createPlainSocket(QIODevice::OpenMode openMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate17createPlainSocketE6QFlagsIN13QIODeviceBase12OpenModeFlagEE(
    QSslSocketPrivate *self,
    int openMode) {
  self->createPlainSocket(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(openMode));
}

//  void QSslSocketPrivate::pauseSocketNotifiers(QSslSocket *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate20pauseSocketNotifiersEP10QSslSocket(
    QSslSocket *a0) {
  QSslSocketPrivate::pauseSocketNotifiers(a0);
}

//  void QSslSocketPrivate::resumeSocketNotifiers(QSslSocket *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate21resumeSocketNotifiersEP10QSslSocket(
    QSslSocket *a0) {
  QSslSocketPrivate::resumeSocketNotifiers(a0);
}

//  bool QSslSocketPrivate::isPaused() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslSocketPrivate8isPausedEv(
    const QSslSocketPrivate *self) {
  return self->isPaused();
}

//  void QSslSocketPrivate::setPaused(bool p)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate9setPausedEb(
    QSslSocketPrivate *self,
    bool p) {
  self->setPaused(p);
}

//  bool QSslSocketPrivate::bind(const QHostAddress &address, quint16 a1,
//      QAbstractSocket::BindMode a2, const QNetworkInterface *iface)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface(
    QSslSocketPrivate *self,
    const QHostAddress *address,
    quint16 a1,
    int a2,
    const QNetworkInterface *iface) {
  return self->bind(
      *address,
      a1,
      QFlags<QAbstractSocket::BindFlag>::fromInt(a2),
      iface);
}

//  void QSslSocketPrivate::_q_connectedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate16_q_connectedSlotEv(
    QSslSocketPrivate *self) {
  self->_q_connectedSlot();
}

//  void QSslSocketPrivate::_q_hostFoundSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate16_q_hostFoundSlotEv(
    QSslSocketPrivate *self) {
  self->_q_hostFoundSlot();
}

//  void QSslSocketPrivate::_q_disconnectedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate19_q_disconnectedSlotEv(
    QSslSocketPrivate *self) {
  self->_q_disconnectedSlot();
}

//  void QSslSocketPrivate::_q_stateChangedSlot(QAbstractSocket::SocketState
//      a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate19_q_stateChangedSlotEN15QAbstractSocket11SocketStateE(
    QSslSocketPrivate *self,
    QAbstractSocket::SocketState a0) {
  self->_q_stateChangedSlot(a0);
}

//  void QSslSocketPrivate::_q_errorSlot(QAbstractSocket::SocketError a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate12_q_errorSlotEN15QAbstractSocket11SocketErrorE(
    QSslSocketPrivate *self,
    QAbstractSocket::SocketError a0) {
  self->_q_errorSlot(a0);
}

//  void QSslSocketPrivate::_q_readyReadSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate16_q_readyReadSlotEv(
    QSslSocketPrivate *self) {
  self->_q_readyReadSlot();
}

//  void QSslSocketPrivate::_q_channelReadyReadSlot(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate23_q_channelReadyReadSlotEi(
    QSslSocketPrivate *self,
    int a0) {
  self->_q_channelReadyReadSlot(a0);
}

//  void QSslSocketPrivate::_q_bytesWrittenSlot(qint64 a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate19_q_bytesWrittenSlotEx(
    QSslSocketPrivate *self,
    qint64 a0) {
  self->_q_bytesWrittenSlot(a0);
}

//  void QSslSocketPrivate::_q_channelBytesWrittenSlot(int a0, qint64 a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate26_q_channelBytesWrittenSlotEix(
    QSslSocketPrivate *self,
    int a0,
    qint64 a1) {
  self->_q_channelBytesWrittenSlot(a0, a1);
}

//  void QSslSocketPrivate::_q_readChannelFinishedSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate26_q_readChannelFinishedSlotEv(
    QSslSocketPrivate *self) {
  self->_q_readChannelFinishedSlot();
}

//  void QSslSocketPrivate::_q_flushWriteBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate19_q_flushWriteBufferEv(
    QSslSocketPrivate *self) {
  self->_q_flushWriteBuffer();
}

//  void QSslSocketPrivate::_q_flushReadBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate18_q_flushReadBufferEv(
    QSslSocketPrivate *self) {
  self->_q_flushReadBuffer();
}

//  void QSslSocketPrivate::_q_resumeImplementation()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate23_q_resumeImplementationEv(
    QSslSocketPrivate *self) {
  self->_q_resumeImplementation();
}

//  QList<QByteArray> QSslSocketPrivate::unixRootCertDirectories()
extern "C" Q_DECL_EXPORT
QList<QByteArray> *ritual_ZN17QSslSocketPrivate23unixRootCertDirectoriesEv() {
  return new QList<QByteArray>(QSslSocketPrivate::unixRootCertDirectories());
}

//  QByteArray QSslSocketPrivate::peek(qint64 maxSize)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN17QSslSocketPrivate4peekEx(
    QSslSocketPrivate *self,
    qint64 maxSize) {
  return new QByteArray(self->peek(maxSize));
}

//  bool QSslSocketPrivate::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate5flushEv(QSslSocketPrivate *self) {
  return self->flush();
}

//  void QSslSocketPrivate::startClientEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate21startClientEncryptionEv(
    QSslSocketPrivate *self) {
  self->startClientEncryption();
}

//  void QSslSocketPrivate::startServerEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate21startServerEncryptionEv(
    QSslSocketPrivate *self) {
  self->startServerEncryption();
}

//  void QSslSocketPrivate::transmit()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate8transmitEv(QSslSocketPrivate *self) {
  self->transmit();
}

//  void QSslSocketPrivate::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate18disconnectFromHostEv(
    QSslSocketPrivate *self) {
  self->disconnectFromHost();
}

//  void QSslSocketPrivate::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate12disconnectedEv(QSslSocketPrivate *self) {
  self->disconnected();
}

//  QSslCipher QSslSocketPrivate::sessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK17QSslSocketPrivate13sessionCipherEv(
    const QSslSocketPrivate *self) {
  return new QSslCipher(self->sessionCipher());
}

//  QSsl::SslProtocol QSslSocketPrivate::sessionProtocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK17QSslSocketPrivate15sessionProtocolEv(
    const QSslSocketPrivate *self) {
  return self->sessionProtocol();
}

//  void QSslSocketPrivate::continueHandshake()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate17continueHandshakeEv(
    QSslSocketPrivate *self) {
  self->continueHandshake();
}

//  bool QSslSocketPrivate::rootCertOnDemandLoadingSupported()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate32rootCertOnDemandLoadingSupportedEv() {
  return QSslSocketPrivate::rootCertOnDemandLoadingSupported();
}

//  void QSslSocketPrivate::setRootCertOnDemandLoadingSupported(bool
//      supported)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate35setRootCertOnDemandLoadingSupportedEb(
    bool supported) {
  QSslSocketPrivate::setRootCertOnDemandLoadingSupported(supported);
}

//  QTlsBackend *QSslSocketPrivate::tlsBackendInUse()
extern "C" Q_DECL_EXPORT
QTlsBackend *ritual_ZN17QSslSocketPrivate15tlsBackendInUseEv() {
  return QSslSocketPrivate::tlsBackendInUse();
}

//  QSslSocket::SslMode QSslSocketPrivate::tlsMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::SslMode ritual_ZNK17QSslSocketPrivate7tlsModeEv(
    const QSslSocketPrivate *self) {
  return self->tlsMode();
}

//  bool QSslSocketPrivate::isRootsOnDemandAllowed() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslSocketPrivate22isRootsOnDemandAllowedEv(
    const QSslSocketPrivate *self) {
  return self->isRootsOnDemandAllowed();
}

//  QString QSslSocketPrivate::verificationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSslSocketPrivate16verificationNameEv(
    const QSslSocketPrivate *self) {
  return new QString(self->verificationName());
}

//  QString QSslSocketPrivate::tlsHostName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSslSocketPrivate11tlsHostNameEv(
    const QSslSocketPrivate *self) {
  return new QString(self->tlsHostName());
}

//  QTcpSocket *QSslSocketPrivate::plainTcpSocket() const
extern "C" Q_DECL_EXPORT
QTcpSocket *ritual_ZNK17QSslSocketPrivate14plainTcpSocketEv(
    const QSslSocketPrivate *self) {
  return self->plainTcpSocket();
}

//  bool QSslSocketPrivate::verifyErrorsHaveBeenIgnored()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QSslSocketPrivate27verifyErrorsHaveBeenIgnoredEv(
    QSslSocketPrivate *self) {
  return self->verifyErrorsHaveBeenIgnored();
}

//  bool QSslSocketPrivate::isAutoStartingHandshake() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslSocketPrivate23isAutoStartingHandshakeEv(
    const QSslSocketPrivate *self) {
  return self->isAutoStartingHandshake();
}

//  bool QSslSocketPrivate::isPendingClose() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslSocketPrivate14isPendingCloseEv(
    const QSslSocketPrivate *self) {
  return self->isPendingClose();
}

//  void QSslSocketPrivate::setPendingClose(bool pc)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate15setPendingCloseEb(
    QSslSocketPrivate *self,
    bool pc) {
  self->setPendingClose(pc);
}

//  qint64 QSslSocketPrivate::maxReadBufferSize() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK17QSslSocketPrivate17maxReadBufferSizeEv(
    const QSslSocketPrivate *self) {
  return self->maxReadBufferSize();
}

//  void QSslSocketPrivate::setMaxReadBufferSize(qint64 maxSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate20setMaxReadBufferSizeEx(
    QSslSocketPrivate *self,
    qint64 maxSize) {
  self->setMaxReadBufferSize(maxSize);
}

//  void QSslSocketPrivate::setEncrypted(bool enc)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslSocketPrivate12setEncryptedEb(
    QSslSocketPrivate *self,
    bool enc) {
  self->setEncrypted(enc);
}

//  bool QSslSocketPrivate::hasUndecryptedData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSslSocketPrivate18hasUndecryptedDataEv(
    const QSslSocketPrivate *self) {
  return self->hasUndecryptedData();
}

//  a Python function taken by a CuteQSslSocketPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSslSocketPrivate(
    QSslSocketPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSslSocketPrivate *>(self)->take(key, call);
}

//  bool QSslSocketPrivate::bind(const QHostAddress &address, quint16 a1,
//      QAbstractSocket::BindMode a2, const QNetworkInterface *iface)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QSslSocketPrivate4bindERK12QHostAddresst6QFlagsIN15QAbstractSocket8BindFlagEEPK17QNetworkInterface(
    QSslSocketPrivate *self,
    const QHostAddress *address,
    quint16 a1,
    int a2,
    const QNetworkInterface *iface) {
  return self->QSslSocketPrivate::bind(
      *address,
      a1,
      QFlags<QAbstractSocket::BindFlag>::fromInt(a2),
      iface);
}

//  QByteArray QSslSocketPrivate::peek(qint64 maxSize)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZN17QSslSocketPrivate4peekEx(
    QSslSocketPrivate *self,
    qint64 maxSize) {
  return new QByteArray(self->QSslSocketPrivate::peek(maxSize));
}

//  bool QSslSocketPrivate::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QSslSocketPrivate5flushEv(QSslSocketPrivate *self) {
  return self->QSslSocketPrivate::flush();
}

#endif  // QT_CONFIG(ssl)
