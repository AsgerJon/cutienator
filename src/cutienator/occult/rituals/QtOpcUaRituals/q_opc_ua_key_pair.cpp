//  Written by dev_tooling.RitualGenerator from the records of
//  QtOpcUa/qopcuakeypair.h, Qt 6.12.0.
//  Edited by hand on 2026-11-25: the include of
//  <QtOpcUa/qtopcua-config.h> before the #if, as it defines
//  QT_CONFIG(gds); the long #if line split in two.
//  Kept as it is when the generator runs again.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtOpcUa/qopcuaglobal.h>
#include <QtOpcUa/qtopcua-config.h>
#if QT_CONFIG(gds) && QT_CONFIG(openssl) \
    && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
#include <QtOpcUa/QtOpcUa>
#include <QtOpcUa/qopcuakeypair.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QOpcUaKeyPair that Python can take functions over in. Every QOpcUaKeyPair
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaKeyPairCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQOpcUaKeyPairCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaKeyPairCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaKeyPairCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaKeyPairCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaKeyPairCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQOpcUaKeyPairCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQOpcUaKeyPair : public QOpcUaKeyPair {
public:
  using QOpcUaKeyPair::QOpcUaKeyPair;
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
      CuteQOpcUaKeyPairCall0 call = reinterpret_cast<CuteQOpcUaKeyPairCall0>(taken[0]);
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
      CuteQOpcUaKeyPairCall1 call = reinterpret_cast<CuteQOpcUaKeyPairCall1>(taken[1]);
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
      CuteQOpcUaKeyPairCall2 call = reinterpret_cast<CuteQOpcUaKeyPairCall2>(taken[2]);
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
      CuteQOpcUaKeyPairCall3 call = reinterpret_cast<CuteQOpcUaKeyPairCall3>(taken[3]);
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
      CuteQOpcUaKeyPairCall4 call = reinterpret_cast<CuteQOpcUaKeyPairCall4>(taken[4]);
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
      CuteQOpcUaKeyPairCall5 call = reinterpret_cast<CuteQOpcUaKeyPairCall5>(taken[5]);
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
      CuteQOpcUaKeyPairCall6 call = reinterpret_cast<CuteQOpcUaKeyPairCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QOpcUaKeyPair::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QOpcUaKeyPair10metaObjectEv(
    const QOpcUaKeyPair *self) {
  return self->metaObject();
}

//  void *QOpcUaKeyPair::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QOpcUaKeyPair11qt_metacastEPKc(
    QOpcUaKeyPair *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  QString QOpcUaKeyPair::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QOpcUaKeyPair2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QOpcUaKeyPair::tr(s, c, n));
}

//  QOpcUaKeyPairPrivate *QOpcUaKeyPair::d_func()
extern "C" Q_DECL_EXPORT
QOpcUaKeyPairPrivate *ritual_ZN13QOpcUaKeyPair6d_funcEv(
    QOpcUaKeyPair *self) {
  return self->d_func();
}

//  const QOpcUaKeyPairPrivate *QOpcUaKeyPair::d_func() const
extern "C" Q_DECL_EXPORT
const QOpcUaKeyPairPrivate *ritual_ZNK13QOpcUaKeyPair6d_funcEv(
    const QOpcUaKeyPair *self) {
  return self->d_func();
}

//  QOpcUaKeyPair::QOpcUaKeyPair(QObject *parent)
extern "C" Q_DECL_EXPORT
QOpcUaKeyPair *ritual_ZN13QOpcUaKeyPairC1EP7QObject(QObject *parent) {
  return new CuteQOpcUaKeyPair(parent);
}

//  QOpcUaKeyPair::~QOpcUaKeyPair()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaKeyPairD1Ev(QOpcUaKeyPair *self) {
  delete self;
}

//  bool QOpcUaKeyPair::loadFromPemData(const QByteArray &data)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QOpcUaKeyPair15loadFromPemDataERK10QByteArray(
    QOpcUaKeyPair *self,
    const QByteArray *data) {
  return self->loadFromPemData(*data);
}

//  QByteArray QOpcUaKeyPair::publicKeyToByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QOpcUaKeyPair20publicKeyToByteArrayEv(
    const QOpcUaKeyPair *self) {
  return new QByteArray(self->publicKeyToByteArray());
}

//  QByteArray QOpcUaKeyPair::privateKeyToByteArray(Cipher cipher, const
//      QString &password) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK13QOpcUaKeyPair21privateKeyToByteArrayENS_6CipherERK7QString(
    const QOpcUaKeyPair *self,
    QOpcUaKeyPair::Cipher cipher,
    const QString *password) {
  return new QByteArray(self->privateKeyToByteArray(cipher, *password));
}

//  KeyType QOpcUaKeyPair::type() const
extern "C" Q_DECL_EXPORT
QOpcUaKeyPair::KeyType ritual_ZNK13QOpcUaKeyPair4typeEv(
    const QOpcUaKeyPair *self) {
  return self->type();
}

//  bool QOpcUaKeyPair::hasPrivateKey() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QOpcUaKeyPair13hasPrivateKeyEv(const QOpcUaKeyPair *self) {
  return self->hasPrivateKey();
}

//  void QOpcUaKeyPair::generateRsaKey(QOpcUaKeyPair::RsaKeyStrength
//      strength)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaKeyPair14generateRsaKeyENS_14RsaKeyStrengthE(
    QOpcUaKeyPair *self,
    QOpcUaKeyPair::RsaKeyStrength strength) {
  self->generateRsaKey(strength);
}

//  void QOpcUaKeyPair::passphraseNeeded(QString &passphrase, int
//      maximumLength, bool writeOperation)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QOpcUaKeyPair16passphraseNeededER7QStringib(
    QOpcUaKeyPair *self,
    QString *passphrase,
    int maximumLength,
    bool writeOperation) {
  self->passphraseNeeded(*passphrase, maximumLength, writeOperation);
}

//  a Python function taken by a CuteQOpcUaKeyPair, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QOpcUaKeyPair(
    QOpcUaKeyPair *self,
    const char *key,
    void *call) {
  return static_cast<CuteQOpcUaKeyPair *>(self)->take(key, call);
}

#endif  // QT_CONFIG(gds) && QT_CONFIG(openssl) && !defined(Q_OS_DARWIN) && !defined(Q_OS_WINRT)
