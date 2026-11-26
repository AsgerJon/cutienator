//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/qdtls.h, Qt 6.12.0. Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#if QT_CONFIG(dtls) && QT_CONFIG(ssl)
#if QT_CONFIG(dtls)
#include <QtNetwork/qdtls.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QDtlsClientVerifier that Python can take functions over in. Every QDtlsClientVerifier
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDtlsClientVerifierCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQDtlsClientVerifierCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsClientVerifierCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsClientVerifierCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsClientVerifierCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsClientVerifierCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQDtlsClientVerifierCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQDtlsClientVerifier : public QDtlsClientVerifier {
public:
  using QDtlsClientVerifier::QDtlsClientVerifier;
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
      CuteQDtlsClientVerifierCall0 call = reinterpret_cast<CuteQDtlsClientVerifierCall0>(taken[0]);
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
      CuteQDtlsClientVerifierCall1 call = reinterpret_cast<CuteQDtlsClientVerifierCall1>(taken[1]);
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
      CuteQDtlsClientVerifierCall2 call = reinterpret_cast<CuteQDtlsClientVerifierCall2>(taken[2]);
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
      CuteQDtlsClientVerifierCall3 call = reinterpret_cast<CuteQDtlsClientVerifierCall3>(taken[3]);
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
      CuteQDtlsClientVerifierCall4 call = reinterpret_cast<CuteQDtlsClientVerifierCall4>(taken[4]);
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
      CuteQDtlsClientVerifierCall5 call = reinterpret_cast<CuteQDtlsClientVerifierCall5>(taken[5]);
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
      CuteQDtlsClientVerifierCall6 call = reinterpret_cast<CuteQDtlsClientVerifierCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QDtlsClientVerifier::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QDtlsClientVerifier10metaObjectEv(
    const QDtlsClientVerifier *self) {
  return self->metaObject();
}

//  void *QDtlsClientVerifier::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QDtlsClientVerifier11qt_metacastEPKc(
    QDtlsClientVerifier *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QDtlsClientVerifier::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QDtlsClientVerifier11qt_metacallEN11QMetaObject4CallEiPPv(
    QDtlsClientVerifier *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QDtlsClientVerifier::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QDtlsClientVerifier2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDtlsClientVerifier::tr(s, c, n));
}

//  QDtlsClientVerifier::QDtlsClientVerifier(QObject *parent)
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier *ritual_ZN19QDtlsClientVerifierC1EP7QObject(
    QObject *parent) {
  return new CuteQDtlsClientVerifier(parent);
}

//  QDtlsClientVerifier::~QDtlsClientVerifier()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QDtlsClientVerifierD1Ev(QDtlsClientVerifier *self) {
  delete self;
}

//  bool QDtlsClientVerifier::setCookieGeneratorParameters(const
//      GeneratorParameters &params)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QDtlsClientVerifier28setCookieGeneratorParametersERKNS_19GeneratorParametersE(
    QDtlsClientVerifier *self,
    const QDtlsClientVerifier::GeneratorParameters *params) {
  return self->setCookieGeneratorParameters(*params);
}

//  GeneratorParameters QDtlsClientVerifier::cookieGeneratorParameters()
//      const
extern "C" Q_DECL_EXPORT
QDtlsClientVerifier::GeneratorParameters *ritual_ZNK19QDtlsClientVerifier25cookieGeneratorParametersEv(
    const QDtlsClientVerifier *self) {
  return new QDtlsClientVerifier::GeneratorParameters(
      self->cookieGeneratorParameters());
}

//  bool QDtlsClientVerifier::verifyClient(QUdpSocket *socket, const
//      QByteArray &dgram, const QHostAddress &address, quint16 port)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QDtlsClientVerifier12verifyClientEP10QUdpSocketRK10QByteArrayRK12QHostAddresst(
    QDtlsClientVerifier *self,
    QUdpSocket *socket,
    const QByteArray *dgram,
    const QHostAddress *address,
    quint16 port) {
  return self->verifyClient(socket, *dgram, *address, port);
}

//  QByteArray QDtlsClientVerifier::verifiedHello() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK19QDtlsClientVerifier13verifiedHelloEv(
    const QDtlsClientVerifier *self) {
  return new QByteArray(self->verifiedHello());
}

//  QDtlsError QDtlsClientVerifier::dtlsError() const
extern "C" Q_DECL_EXPORT
QDtlsError ritual_ZNK19QDtlsClientVerifier9dtlsErrorEv(
    const QDtlsClientVerifier *self) {
  return self->dtlsError();
}

//  QString QDtlsClientVerifier::dtlsErrorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QDtlsClientVerifier15dtlsErrorStringEv(
    const QDtlsClientVerifier *self) {
  return new QString(self->dtlsErrorString());
}

//  QDtlsClientVerifierPrivate *QDtlsClientVerifier::d_func()
extern "C" Q_DECL_EXPORT
QDtlsClientVerifierPrivate *ritual_ZN19QDtlsClientVerifier6d_funcEv(
    QDtlsClientVerifier *self) {
  return self->d_func();
}

//  const QDtlsClientVerifierPrivate *QDtlsClientVerifier::d_func() const
extern "C" Q_DECL_EXPORT
const QDtlsClientVerifierPrivate *ritual_ZNK19QDtlsClientVerifier6d_funcEv(
    const QDtlsClientVerifier *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQDtlsClientVerifier, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QDtlsClientVerifier(
    QDtlsClientVerifier *self,
    const char *key,
    void *call) {
  return static_cast<CuteQDtlsClientVerifier *>(self)->take(key, call);
}

#endif  // QT_CONFIG(dtls)
#endif  // QT_CONFIG(dtls) && QT_CONFIG(ssl)
