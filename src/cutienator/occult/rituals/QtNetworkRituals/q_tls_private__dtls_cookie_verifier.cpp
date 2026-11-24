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
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qstring.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/qdtls.h>
#include <cstring>

//  A QTlsPrivate::DtlsCookieVerifier that Python can take functions over in. Every QTlsPrivate::DtlsCookieVerifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCookieVerifierCall0)(const void *, QUdpSocket *, const QByteArray *, const QHostAddress *, quint16, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QByteArray * (*CuteQTlsPrivate_DtlsCookieVerifierCall1)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCookieVerifierCall2)(const void *, int, const QString *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef int (*CuteQTlsPrivate_DtlsCookieVerifierCall3)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef QString * (*CuteQTlsPrivate_DtlsCookieVerifierCall4)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCookieVerifierCall5)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef void (*CuteQTlsPrivate_DtlsCookieVerifierCall6)(const void *, const QSslConfiguration *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QSslConfiguration * (*CuteQTlsPrivate_DtlsCookieVerifierCall7)(const void *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef bool (*CuteQTlsPrivate_DtlsCookieVerifierCall8)(const void *, const QDtlsClientVerifier::GeneratorParameters *, int *);
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
typedef const QDtlsClientVerifier::GeneratorParameters * (*CuteQTlsPrivate_DtlsCookieVerifierCall9)(const void *, int *);
#endif  // QT_CONFIG(dtls)
class CuteQTlsPrivate_DtlsCookieVerifier : public QTlsPrivate::DtlsCookieVerifier {
public:
  using QTlsPrivate::DtlsCookieVerifier::DtlsCookieVerifier;
  void *taken[10] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate18DtlsCookieVerifier12verifyClientEP10QUdpSocketRK10QByteArrayRK12QHostAddresst")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate18DtlsCookieVerifier13verifiedHelloEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase12setDtlsErrorE10QDtlsErrorRK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase5errorEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase11errorStringEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase14clearDtlsErrorEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase16setConfigurationERK17QSslConfiguration")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase13configurationEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZN11QTlsPrivate8DtlsBase28setCookieGeneratorParametersERKN19QDtlsClientVerifier19GeneratorParametersE")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
#if QT_CONFIG(dtls)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate8DtlsBase25cookieGeneratorParametersEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(dtls)
    return false;
  }

#if QT_CONFIG(dtls)
  //  bool QTlsPrivate::DtlsCookieVerifier::verifyClient(QUdpSocket
  //      *socket, const QByteArray &dgram, const QHostAddress &address,
  //      quint16 port)
  bool verifyClient(
      QUdpSocket *socket,
      const QByteArray &dgram,
      const QHostAddress &address,
      quint16 port) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall0 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall0>(taken[0]);
      bool given = call(this, socket, &dgram, &address, port, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QByteArray QTlsPrivate::DtlsCookieVerifier::verifiedHello() const
  QByteArray verifiedHello() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall1 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall1>(taken[1]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setDtlsError(QDtlsError code, const
  //      QString &description)
  void setDtlsError(QDtlsError code, const QString &description) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall2 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall2>(taken[2]);
      call(this, static_cast<int>(code), &description, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QDtlsError QTlsPrivate::DtlsBase::error() const
  QDtlsError error() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall3 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall3>(taken[3]);
      int given = call(this, &handled);
      if (handled) return static_cast<QDtlsError>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QString QTlsPrivate::DtlsBase::errorString() const
  QString errorString() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall4 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall5 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  void QTlsPrivate::DtlsBase::setConfiguration(const QSslConfiguration
  //      &configuration)
  void setConfiguration(const QSslConfiguration &configuration) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall6 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall6>(taken[6]);
      call(this, &configuration, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  QSslConfiguration QTlsPrivate::DtlsBase::configuration() const
  QSslConfiguration configuration() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall7 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall8 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall8>(taken[8]);
      bool given = call(this, &params, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)

#if QT_CONFIG(dtls)
  //  GenParams QTlsPrivate::DtlsBase::cookieGeneratorParameters() const
  QTlsPrivate::DtlsBase::GenParams cookieGeneratorParameters() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsPrivate_DtlsCookieVerifierCall9 call = reinterpret_cast<CuteQTlsPrivate_DtlsCookieVerifierCall9>(taken[9]);
      const QDtlsClientVerifier::GeneratorParameters * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(dtls)
};

//  bool QTlsPrivate::DtlsCookieVerifier::verifyClient(QUdpSocket *socket,
//      const QByteArray &dgram, const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QTlsPrivate18DtlsCookieVerifier12verifyClientEP10QUdpSocketRK10QByteArrayRK12QHostAddresst(
    QTlsPrivate::DtlsCookieVerifier *self,
    QUdpSocket *socket,
    const QByteArray *dgram,
    const QHostAddress *address,
    quint16 port) {
  return self->verifyClient(socket, *dgram, *address, port);
}

//  QByteArray QTlsPrivate::DtlsCookieVerifier::verifiedHello() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK11QTlsPrivate18DtlsCookieVerifier13verifiedHelloEv(
    const QTlsPrivate::DtlsCookieVerifier *self) {
  return new QByteArray(self->verifiedHello());
}

//  a Python function taken by a CuteQTlsPrivate_DtlsCookieVerifier, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_DtlsCookieVerifier(
    QTlsPrivate::DtlsCookieVerifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_DtlsCookieVerifier *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dtls)
