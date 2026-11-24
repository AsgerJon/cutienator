//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(dtls)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qdtls.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTlsPrivate::DtlsCryptograph that Python can take functions over in. Every QTlsPrivate::DtlsCryptograph
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsCryptographCall0)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall1)(const void *, const QHostAddress *, quint16, const QString *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QHostAddress * (*CuteQTlsPrivate_DtlsCryptographCall2)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef quint16 (*CuteQTlsPrivate_DtlsCryptographCall3)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall4)(const void *, const QString *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef QString * (*CuteQTlsPrivate_DtlsCryptographCall5)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall6)(const void *, quint16, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef quint16 (*CuteQTlsPrivate_DtlsCryptographCall7)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsCryptographCall8)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall9)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall10)(const void *, QUdpSocket *, const QByteArray *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall11)(const void *, QUdpSocket *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall12)(const void *, QUdpSocket *, const QByteArray *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall13)(const void *, QUdpSocket *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall14)(const void *, QUdpSocket *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall15)(const void *, QUdpSocket *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QSslCipher * (*CuteQTlsPrivate_DtlsCryptographCall16)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsCryptographCall17)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef qint64 (*CuteQTlsPrivate_DtlsCryptographCall18)(const void *, QUdpSocket *, const QByteArray *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QByteArray * (*CuteQTlsPrivate_DtlsCryptographCall19)(const void *, QUdpSocket *, const QByteArray *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall20)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsCryptographCall21)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef QString * (*CuteQTlsPrivate_DtlsCryptographCall22)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall23)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCryptographCall24)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QSslConfiguration * (*CuteQTlsPrivate_DtlsCryptographCall25)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCryptographCall26)(const void *, const QDtlsClientVerifier::GeneratorParameters *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QDtlsClientVerifier::GeneratorParameters * (*CuteQTlsPrivate_DtlsCryptographCall27)(const void *, int *);
#endif  // QT_CONFIG(dtls)
class CuteQTlsPrivate_DtlsCryptograph : public QTlsPrivate::DtlsCryptograph {
public:
  using QTlsPrivate::DtlsCryptograph::DtlsCryptograph;
  void *taken[28] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph15cryptographModeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph7setPeerERK12QHostAddresstRK7QString")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph11peerAddressEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph8peerPortEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph23setPeerVerificationNameERK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph20peerVerificationNameEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph14setDtlsMtuHintEt")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph11dtlsMtuHintEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph5stateEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph21isConnectionEncryptedEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph14startHandshakeEP10QUdpSocketRK10QByteArray")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph13handleTimeoutEP10QUdpSocket")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph17continueHandshakeEP10QUdpSocketRK10QByteArray")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph15resumeHandshakeEP10QUdpSocket")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph14abortHandshakeEP10QUdpSocket")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph17sendShutdownAlertEP10QUdpSocket")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph17dtlsSessionCipherEv")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate15DtlsCryptograph19dtlsSessionProtocolEv")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph22writeDatagramEncryptedEP10QUdpSocketRK10QByteArray")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate15DtlsCryptograph15decryptDatagramEP10QUdpSocketRK10QByteArray")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase12setDtlsErrorE10QDtlsErrorRK7QString")) {
      taken[20] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase5errorEv")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase11errorStringEv")) {
      taken[22] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfiguration")) {
      taken[24] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase13configurationEv")) {
      taken[25] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN19QDtlsClientVerifier19GeneratorParametersE")) {
      taken[26] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv")) {
      taken[27] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
    return false;
  }

#if QT_CONFIG(dtls)
  //  QSslSocket::SslMode QTlsPrivate::DtlsCryptograph::cryptographMode()
  //      const
  QSslSocket::SslMode cryptographMode() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall0 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSslSocket::SslMode>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsCryptograph::setPeer(const QHostAddress &addr,
  //      quint16 port, const QString &name)
  void setPeer(
      const QHostAddress &addr,
      quint16 port,
      const QString &name) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall1 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall1>(taken[1]);
      call(this, &addr, port, &name, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QHostAddress QTlsPrivate::DtlsCryptograph::peerAddress() const
  QHostAddress peerAddress() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall2 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall2>(taken[2]);
      const QHostAddress * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  quint16 QTlsPrivate::DtlsCryptograph::peerPort() const
  quint16 peerPort() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall3 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall3>(taken[3]);
      quint16 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsCryptograph::setPeerVerificationName(const
  //      QString &name)
  void setPeerVerificationName(const QString &name) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall4 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall4>(taken[4]);
      call(this, &name, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QString QTlsPrivate::DtlsCryptograph::peerVerificationName() const
  QString peerVerificationName() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall5 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall5>(taken[5]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsCryptograph::setDtlsMtuHint(quint16 mtu)
  void setDtlsMtuHint(quint16 mtu) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall6 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall6>(taken[6]);
      call(this, mtu, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  quint16 QTlsPrivate::DtlsCryptograph::dtlsMtuHint() const
  quint16 dtlsMtuHint() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall7 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall7>(taken[7]);
      quint16 given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QDtls::HandshakeState QTlsPrivate::DtlsCryptograph::state() const
  QDtls::HandshakeState state() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall8 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDtls::HandshakeState>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCryptograph::isConnectionEncrypted() const
  bool isConnectionEncrypted() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall9 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall9>(taken[9]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCryptograph::startHandshake(QUdpSocket *socket,
  //      const QByteArray &dgram)
  bool startHandshake(QUdpSocket *socket, const QByteArray &dgram) override {
    if (taken[10]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall10 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall10>(taken[10]);
      bool given = call(this, socket, &dgram, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCryptograph::handleTimeout(QUdpSocket *socket)
  bool handleTimeout(QUdpSocket *socket) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall11 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall11>(taken[11]);
      bool given = call(this, socket, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCryptograph::continueHandshake(QUdpSocket
  //      *socket, const QByteArray &dgram)
  bool continueHandshake(
      QUdpSocket *socket,
      const QByteArray &dgram) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall12 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall12>(taken[12]);
      bool given = call(this, socket, &dgram, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCryptograph::resumeHandshake(QUdpSocket
  //      *socket)
  bool resumeHandshake(QUdpSocket *socket) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall13 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall13>(taken[13]);
      bool given = call(this, socket, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsCryptograph::abortHandshake(QUdpSocket *socket)
  void abortHandshake(QUdpSocket *socket) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall14 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall14>(taken[14]);
      call(this, socket, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsCryptograph::sendShutdownAlert(QUdpSocket
  //      *socket)
  void sendShutdownAlert(QUdpSocket *socket) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall15 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall15>(taken[15]);
      call(this, socket, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QSslCipher QTlsPrivate::DtlsCryptograph::dtlsSessionCipher() const
  QSslCipher dtlsSessionCipher() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall16 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall16>(taken[16]);
      const QSslCipher * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QSsl::SslProtocol QTlsPrivate::DtlsCryptograph::dtlsSessionProtocol()
  //      const
  QSsl::SslProtocol dtlsSessionProtocol() const override {
    if (taken[17]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall17 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall17>(taken[17]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSsl::SslProtocol>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  qint64
  //      QTlsPrivate::DtlsCryptograph::writeDatagramEncrypted(QUdpSocket
  //      *socket, const QByteArray &dgram)
  qint64 writeDatagramEncrypted(
      QUdpSocket *socket,
      const QByteArray &dgram) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall18 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall18>(taken[18]);
      qint64 given = call(this, socket, &dgram, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QByteArray QTlsPrivate::DtlsCryptograph::decryptDatagram(QUdpSocket
  //      *socket, const QByteArray &dgram)
  QByteArray decryptDatagram(
      QUdpSocket *socket,
      const QByteArray &dgram) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall19 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall19>(taken[19]);
      const QByteArray * given = call(this, socket, &dgram, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const
  //      QString &description)
  void setDtlsError(QDtlsError code, const QString &description) override {
    if (taken[20]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall20 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall20>(taken[20]);
      call(this, static_cast<int>(code), &description, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QDtlsError QTlsPrivate::DtlsBase::error() const
  QDtlsError error() const override {
    if (taken[21]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall21 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall21>(taken[21]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDtlsError>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QString QTlsPrivate::DtlsBase::errorString() const
  QString errorString() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall22 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall22>(taken[22]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::clearDtlsError()
  void clearDtlsError() override {
    if (taken[23]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall23 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall23>(taken[23]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setConfiguration(const QSslConfiguration
  //      &configuration)
  void setConfiguration(const QSslConfiguration &configuration) override {
    if (taken[24]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall24 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall24>(taken[24]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QSslConfiguration QTlsPrivate::DtlsBase::configuration() const
  QSslConfiguration configuration() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall25 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall25>(taken[25]);
      const QSslConfiguration * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsBase::setCookieGeneratorParameters(const
  //      GenParams &params)
  bool setCookieGeneratorParameters(
      const QTlsPrivate::DtlsBase::GenParams &params) override {
    if (taken[26]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall26 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall26>(taken[26]);
      bool given = call(this, &params, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters() const
  QTlsPrivate::DtlsBase::GenParams cookieGeneratorParameters() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCryptographCall27 call = reinterpret_cast<CuteQTlsPrivate_DtlsCryptographCall27>(taken[27]);
      const QDtlsClientVerifier::GeneratorParameters * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)
};

//  QSslSocket::SslMode QTlsPrivate::DtlsCryptograph::cryptographMode() const
extern "C" Q_DECL_EXPORT
QSslSocket::SslMode ritual_ZNK11QTlsPrivate15DtlsCryptograph15cryptographModeEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->cryptographMode();
}

//  void QTlsPrivate::DtlsCryptograph::setPeer(const QHostAddress &addr,
//      quint16 port, const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph7setPeerERK12QHostAddresstRK7QString(
    QTlsPrivate::DtlsCryptograph *self,
    const QHostAddress *addr,
    quint16 port,
    const QString *name) {
  self->setPeer(*addr, port, *name);
}

//  QHostAddress QTlsPrivate::DtlsCryptograph::peerAddress() const
extern "C" Q_DECL_EXPORT
QHostAddress *ritual_ZNK11QTlsPrivate15DtlsCryptograph11peerAddressEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return new QHostAddress(self->peerAddress());
}

//  quint16 QTlsPrivate::DtlsCryptograph::peerPort() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK11QTlsPrivate15DtlsCryptograph8peerPortEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->peerPort();
}

//  void QTlsPrivate::DtlsCryptograph::setPeerVerificationName(const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph23setPeerVerificationNameERK7QString(
    QTlsPrivate::DtlsCryptograph *self,
    const QString *name) {
  self->setPeerVerificationName(*name);
}

//  QString QTlsPrivate::DtlsCryptograph::peerVerificationName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QTlsPrivate15DtlsCryptograph20peerVerificationNameEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return new QString(self->peerVerificationName());
}

//  void QTlsPrivate::DtlsCryptograph::setDtlsMtuHint(quint16 mtu)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph14setDtlsMtuHintEt(
    QTlsPrivate::DtlsCryptograph *self,
    quint16 mtu) {
  self->setDtlsMtuHint(mtu);
}

//  quint16 QTlsPrivate::DtlsCryptograph::dtlsMtuHint() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK11QTlsPrivate15DtlsCryptograph11dtlsMtuHintEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->dtlsMtuHint();
}

//  QDtls::HandshakeState QTlsPrivate::DtlsCryptograph::state() const
extern "C" Q_DECL_EXPORT
QDtls::HandshakeState ritual_ZNK11QTlsPrivate15DtlsCryptograph5stateEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->state();
}

//  bool QTlsPrivate::DtlsCryptograph::isConnectionEncrypted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate15DtlsCryptograph21isConnectionEncryptedEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->isConnectionEncrypted();
}

//  bool QTlsPrivate::DtlsCryptograph::startHandshake(QUdpSocket *socket,
//      const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate15DtlsCryptograph14startHandshakeEP10QUdpSocketRK10QByteArray(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->startHandshake(socket, *dgram);
}

//  bool QTlsPrivate::DtlsCryptograph::handleTimeout(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate15DtlsCryptograph13handleTimeoutEP10QUdpSocket(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket) {
  return self->handleTimeout(socket);
}

//  bool QTlsPrivate::DtlsCryptograph::continueHandshake(QUdpSocket *socket,
//      const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate15DtlsCryptograph17continueHandshakeEP10QUdpSocketRK10QByteArray(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->continueHandshake(socket, *dgram);
}

//  bool QTlsPrivate::DtlsCryptograph::resumeHandshake(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate15DtlsCryptograph15resumeHandshakeEP10QUdpSocket(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket) {
  return self->resumeHandshake(socket);
}

//  void QTlsPrivate::DtlsCryptograph::abortHandshake(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph14abortHandshakeEP10QUdpSocket(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket) {
  self->abortHandshake(socket);
}

//  void QTlsPrivate::DtlsCryptograph::sendShutdownAlert(QUdpSocket *socket)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph17sendShutdownAlertEP10QUdpSocket(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket) {
  self->sendShutdownAlert(socket);
}

//  QList<QSslError> QTlsPrivate::DtlsCryptograph::peerVerificationErrors()
//      const
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_ZNK11QTlsPrivate15DtlsCryptograph22peerVerificationErrorsEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return new QList<QSslError>(self->peerVerificationErrors());
}

//  void QTlsPrivate::DtlsCryptograph::ignoreVerificationErrors(const
//      QList<QSslError> &errorsToIgnore)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate15DtlsCryptograph24ignoreVerificationErrorsERK5QListI9QSslErrorE(
    QTlsPrivate::DtlsCryptograph *self,
    const QList<QSslError> *errorsToIgnore) {
  self->ignoreVerificationErrors(*errorsToIgnore);
}

//  QSslCipher QTlsPrivate::DtlsCryptograph::dtlsSessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK11QTlsPrivate15DtlsCryptograph17dtlsSessionCipherEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return new QSslCipher(self->dtlsSessionCipher());
}

//  QSsl::SslProtocol QTlsPrivate::DtlsCryptograph::dtlsSessionProtocol()
//      const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK11QTlsPrivate15DtlsCryptograph19dtlsSessionProtocolEv(
    const QTlsPrivate::DtlsCryptograph *self) {
  return self->dtlsSessionProtocol();
}

//  qint64 QTlsPrivate::DtlsCryptograph::writeDatagramEncrypted(QUdpSocket
//      *socket, const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN11QTlsPrivate15DtlsCryptograph22writeDatagramEncryptedEP10QUdpSocketRK10QByteArray(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return self->writeDatagramEncrypted(socket, *dgram);
}

//  QByteArray QTlsPrivate::DtlsCryptograph::decryptDatagram(QUdpSocket
//      *socket, const QByteArray &dgram)
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN11QTlsPrivate15DtlsCryptograph15decryptDatagramEP10QUdpSocketRK10QByteArray(
    QTlsPrivate::DtlsCryptograph *self,
    QUdpSocket *socket,
    const QByteArray *dgram) {
  return new QByteArray(self->decryptDatagram(socket, *dgram));
}

//  a Python function taken by a CuteQTlsPrivate_DtlsCryptograph, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_DtlsCryptograph(
    QTlsPrivate::DtlsCryptograph *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_DtlsCryptograph *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dtls)
