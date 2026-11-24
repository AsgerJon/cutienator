//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/qnearfieldtarget.h, Qt 6.12.0. Changes made here are lost.
#include <QtNfc/qnearfieldtarget.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtNfc/qndefmessage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QNearFieldTarget that Python can take functions over in. Every QNearFieldTarget
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNearFieldTarget : public QNearFieldTarget {
public:
  using QNearFieldTarget::QNearFieldTarget;
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
      CuteQNearFieldTargetCall0 call = reinterpret_cast<CuteQNearFieldTargetCall0>(taken[0]);
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
      CuteQNearFieldTargetCall1 call = reinterpret_cast<CuteQNearFieldTargetCall1>(taken[1]);
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
      CuteQNearFieldTargetCall2 call = reinterpret_cast<CuteQNearFieldTargetCall2>(taken[2]);
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
      CuteQNearFieldTargetCall3 call = reinterpret_cast<CuteQNearFieldTargetCall3>(taken[3]);
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
      CuteQNearFieldTargetCall4 call = reinterpret_cast<CuteQNearFieldTargetCall4>(taken[4]);
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
      CuteQNearFieldTargetCall5 call = reinterpret_cast<CuteQNearFieldTargetCall5>(taken[5]);
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
      CuteQNearFieldTargetCall6 call = reinterpret_cast<CuteQNearFieldTargetCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNearFieldTarget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QNearFieldTarget10metaObjectEv(
    const QNearFieldTarget *self) {
  return self->metaObject();
}

//  QString QNearFieldTarget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QNearFieldTarget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QNearFieldTarget::tr(s, c, n));
}

//  QNearFieldTargetPrivate *QNearFieldTarget::d_func()
extern "C" Q_DECL_EXPORT
QNearFieldTargetPrivate *ritual_ZN16QNearFieldTarget6d_funcEv(
    QNearFieldTarget *self) {
  return self->d_func();
}

//  const QNearFieldTargetPrivate *QNearFieldTarget::d_func() const
extern "C" Q_DECL_EXPORT
const QNearFieldTargetPrivate *ritual_ZNK16QNearFieldTarget6d_funcEv(
    const QNearFieldTarget *self) {
  return self->d_func();
}

//  QNearFieldTarget::QNearFieldTarget(QObject *parent)
extern "C" Q_DECL_EXPORT
QNearFieldTarget *ritual_ZN16QNearFieldTargetC1EP7QObject(QObject *parent) {
  return new CuteQNearFieldTarget(parent);
}

//  QNearFieldTarget::~QNearFieldTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QNearFieldTargetD1Ev(QNearFieldTarget *self) {
  delete self;
}

//  QByteArray QNearFieldTarget::uid() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK16QNearFieldTarget3uidEv(
    const QNearFieldTarget *self) {
  return new QByteArray(self->uid());
}

//  Type QNearFieldTarget::type() const
extern "C" Q_DECL_EXPORT
QNearFieldTarget::Type ritual_ZNK16QNearFieldTarget4typeEv(
    const QNearFieldTarget *self) {
  return self->type();
}

//  AccessMethods QNearFieldTarget::accessMethods() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNearFieldTarget13accessMethodsEv(
    const QNearFieldTarget *self) {
  return static_cast<int>(self->accessMethods().toInt());
}

//  bool QNearFieldTarget::disconnect()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QNearFieldTarget10disconnectEv(QNearFieldTarget *self) {
  return self->disconnect();
}

//  bool QNearFieldTarget::hasNdefMessage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QNearFieldTarget14hasNdefMessageEv(QNearFieldTarget *self) {
  return self->hasNdefMessage();
}

//  RequestId QNearFieldTarget::readNdefMessages()
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget16readNdefMessagesEv(
    QNearFieldTarget *self) {
  return new QNearFieldTarget::RequestId(self->readNdefMessages());
}

//  RequestId QNearFieldTarget::writeNdefMessages(const QList<QNdefMessage>
//      &messages)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget17writeNdefMessagesERK5QListI12QNdefMessageE(
    QNearFieldTarget *self,
    const QList<QNdefMessage> *messages) {
  return new QNearFieldTarget::RequestId(self->writeNdefMessages(*messages));
}

//  int QNearFieldTarget::maxCommandLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QNearFieldTarget16maxCommandLengthEv(
    const QNearFieldTarget *self) {
  return self->maxCommandLength();
}

//  RequestId QNearFieldTarget::sendCommand(const QByteArray &command)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN16QNearFieldTarget11sendCommandERK10QByteArray(
    QNearFieldTarget *self,
    const QByteArray *command) {
  return new QNearFieldTarget::RequestId(self->sendCommand(*command));
}

//  bool QNearFieldTarget::waitForRequestCompleted(const RequestId &id, int
//      msecs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QNearFieldTarget23waitForRequestCompletedERKNS_9RequestIdEi(
    QNearFieldTarget *self,
    const QNearFieldTarget::RequestId *id,
    int msecs) {
  return self->waitForRequestCompleted(*id, msecs);
}

//  QVariant QNearFieldTarget::requestResponse(const RequestId &id) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QNearFieldTarget15requestResponseERKNS_9RequestIdE(
    const QNearFieldTarget *self,
    const QNearFieldTarget::RequestId *id) {
  return new QVariant(self->requestResponse(*id));
}

//  QNearFieldTarget::QNearFieldTarget(QNearFieldTargetPrivate *backend,
//      QObject *parent)
extern "C" Q_DECL_EXPORT
QNearFieldTarget *ritual_ZN16QNearFieldTargetC1EP23QNearFieldTargetPrivateP7QObject(
    QNearFieldTargetPrivate *backend,
    QObject *parent) {
  return new CuteQNearFieldTarget(backend, parent);
}

//  a Python function taken by a CuteQNearFieldTarget, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNearFieldTarget(
    QNearFieldTarget *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNearFieldTarget *>(self)->take(key, call);
}
