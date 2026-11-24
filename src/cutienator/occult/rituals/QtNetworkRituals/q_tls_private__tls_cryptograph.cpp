//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qtlsbackend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslerror.h>
#include <QtNetwork/qsslcipher.h>
#include <QtNetwork/qocspresponse.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QTlsPrivate::TlsCryptograph that Python can take functions over in. Every QTlsPrivate::TlsCryptograph
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall0)(const void *, QSslSocket *, QSslSocketPrivate *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall1)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall2)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall3)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall4)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall5)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall6)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall7)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef const QSslCipher * (*CuteQTlsPrivate_TlsCryptographCall8)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef int (*CuteQTlsPrivate_TlsCryptographCall9)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef void (*CuteQTlsPrivate_TlsCryptographCall10)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
typedef bool (*CuteQTlsPrivate_TlsCryptographCall11)(const void *, int *);
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTlsPrivate_TlsCryptographCall12)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQTlsPrivate_TlsCryptographCall13)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsPrivate_TlsCryptographCall14)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsPrivate_TlsCryptographCall15)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsPrivate_TlsCryptographCall16)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsPrivate_TlsCryptographCall17)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQTlsPrivate_TlsCryptographCall18)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQTlsPrivate_TlsCryptograph : public QTlsPrivate::TlsCryptograph {
public:
  using QTlsPrivate::TlsCryptograph::TlsCryptograph;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph4initEP10QSslSocketP17QSslSocketPrivate")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph21startClientEncryptionEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph21startServerEncryptionEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph17continueHandshakeEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeContinuationEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph18disconnectFromHostEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph12disconnectedEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate14TlsCryptograph13sessionCipherEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate14TlsCryptograph15sessionProtocolEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZN11QTlsPrivate14TlsCryptograph8transmitEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if QT_CONFIG(ssl)
    if (!std::strcmp(key, "_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(ssl)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[17] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[18] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::init(QSslSocket *q,
  //      QSslSocketPrivate *d)
  void init(QSslSocket *q, QSslSocketPrivate *d) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall0 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall0>(taken[0]);
      call(this, q, d, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::startClientEncryption()
  void startClientEncryption() override {
    if (taken[1]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall1 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::startServerEncryption()
  void startServerEncryption() override {
    if (taken[2]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall2 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::continueHandshake()
  void continueHandshake() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall3 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::enableHandshakeContinuation()
  void enableHandshakeContinuation() override {
    if (taken[4]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall4 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QTlsPrivate::TlsCryptograph::enableHandshakeContinuation();
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::disconnectFromHost()
  void disconnectFromHost() override {
    if (taken[5]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall5 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::disconnected()
  void disconnected() override {
    if (taken[6]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall6 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::cancelCAFetch()
  void cancelCAFetch() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall7 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QTlsPrivate::TlsCryptograph::cancelCAFetch();
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSslCipher QTlsPrivate::TlsCryptograph::sessionCipher() const
  QSslCipher sessionCipher() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall8 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall8>(taken[8]);
      const QSslCipher * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  QSsl::SslProtocol QTlsPrivate::TlsCryptograph::sessionProtocol()
  //      const
  QSsl::SslProtocol sessionProtocol() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall9 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSsl::SslProtocol>(given);
    }
    return {};
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  void QTlsPrivate::TlsCryptograph::transmit()
  void transmit() override {
    if (taken[10]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall10 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(ssl)

#if QT_CONFIG(ssl)
  //  bool QTlsPrivate::TlsCryptograph::hasUndecryptedData() const
  bool hasUndecryptedData() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall11 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QTlsPrivate::TlsCryptograph::hasUndecryptedData();
  }
#endif  // QT_CONFIG(ssl)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall12 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall13 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall13>(taken[13]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall14 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall15 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall16 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[17]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall17 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall17>(taken[17]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[18]) {
      int handled = 0;
      CuteQTlsPrivate_TlsCryptographCall18 call = reinterpret_cast<CuteQTlsPrivate_TlsCryptographCall18>(taken[18]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  QTlsPrivate::TlsCryptograph::~TlsCryptograph()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptographD1Ev(
    QTlsPrivate::TlsCryptograph *self) {
  delete self;
}

//  void QTlsPrivate::TlsCryptograph::init(QSslSocket *q, QSslSocketPrivate
//      *d)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph4initEP10QSslSocketP17QSslSocketPrivate(
    QTlsPrivate::TlsCryptograph *self,
    QSslSocket *q,
    QSslSocketPrivate *d) {
  self->init(q, d);
}

//  QList<QSslError> QTlsPrivate::TlsCryptograph::tlsErrors() const
extern "C" Q_DECL_EXPORT
QList<QSslError> *ritual_ZNK11QTlsPrivate14TlsCryptograph9tlsErrorsEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return new QList<QSslError>(self->tlsErrors());
}

//  void QTlsPrivate::TlsCryptograph::startClientEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph21startClientEncryptionEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->startClientEncryption();
}

//  void QTlsPrivate::TlsCryptograph::startServerEncryption()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph21startServerEncryptionEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->startServerEncryption();
}

//  void QTlsPrivate::TlsCryptograph::continueHandshake()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph17continueHandshakeEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->continueHandshake();
}

//  void QTlsPrivate::TlsCryptograph::enableHandshakeContinuation()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeContinuationEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->enableHandshakeContinuation();
}

//  void QTlsPrivate::TlsCryptograph::disconnectFromHost()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph18disconnectFromHostEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->disconnectFromHost();
}

//  void QTlsPrivate::TlsCryptograph::disconnected()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph12disconnectedEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->disconnected();
}

//  void QTlsPrivate::TlsCryptograph::cancelCAFetch()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->cancelCAFetch();
}

//  QSslCipher QTlsPrivate::TlsCryptograph::sessionCipher() const
extern "C" Q_DECL_EXPORT
QSslCipher *ritual_ZNK11QTlsPrivate14TlsCryptograph13sessionCipherEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return new QSslCipher(self->sessionCipher());
}

//  QSsl::SslProtocol QTlsPrivate::TlsCryptograph::sessionProtocol() const
extern "C" Q_DECL_EXPORT
QSsl::SslProtocol ritual_ZNK11QTlsPrivate14TlsCryptograph15sessionProtocolEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return self->sessionProtocol();
}

//  void QTlsPrivate::TlsCryptograph::transmit()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTlsPrivate14TlsCryptograph8transmitEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->transmit();
}

//  bool QTlsPrivate::TlsCryptograph::hasUndecryptedData() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return self->hasUndecryptedData();
}

//  QList<QOcspResponse> QTlsPrivate::TlsCryptograph::ocsps() const
extern "C" Q_DECL_EXPORT
QList<QOcspResponse> *ritual_ZNK11QTlsPrivate14TlsCryptograph5ocspsEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return new QList<QOcspResponse>(self->ocsps());
}

//  a Python function taken by a CuteQTlsPrivate_TlsCryptograph, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTlsPrivate_TlsCryptograph(
    QTlsPrivate::TlsCryptograph *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTlsPrivate_TlsCryptograph *>(self)->take(key, call);
}

//  void QTlsPrivate::TlsCryptograph::enableHandshakeContinuation()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTlsPrivate14TlsCryptograph27enableHandshakeContinuationEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->QTlsPrivate::TlsCryptograph::enableHandshakeContinuation();
}

//  void QTlsPrivate::TlsCryptograph::cancelCAFetch()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN11QTlsPrivate14TlsCryptograph13cancelCAFetchEv(
    QTlsPrivate::TlsCryptograph *self) {
  self->QTlsPrivate::TlsCryptograph::cancelCAFetch();
}

//  bool QTlsPrivate::TlsCryptograph::hasUndecryptedData() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK11QTlsPrivate14TlsCryptograph18hasUndecryptedDataEv(
    const QTlsPrivate::TlsCryptograph *self) {
  return self->QTlsPrivate::TlsCryptograph::hasUndecryptedData();
}

#endif  // QT_CONFIG(ssl)
