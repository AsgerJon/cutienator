//  Written by dev_tooling.RitualGenerator from the records of
//  QtSerialBus/qmodbusreply.h, Qt 6.12.0. Changes made here are lost.
#include <QtSerialBus/qmodbusreply.h>
#include <QtCore/qstring.h>
#include <QtSerialBus/qmodbusdataunit.h>
#include <QtSerialBus/qmodbuspdu.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QModbusReply that Python can take functions over in. Every QModbusReply
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusReplyCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQModbusReplyCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusReplyCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusReplyCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusReplyCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusReplyCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQModbusReplyCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQModbusReply : public QModbusReply {
public:
  using QModbusReply::QModbusReply;
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
      CuteQModbusReplyCall0 call = reinterpret_cast<CuteQModbusReplyCall0>(taken[0]);
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
      CuteQModbusReplyCall1 call = reinterpret_cast<CuteQModbusReplyCall1>(taken[1]);
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
      CuteQModbusReplyCall2 call = reinterpret_cast<CuteQModbusReplyCall2>(taken[2]);
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
      CuteQModbusReplyCall3 call = reinterpret_cast<CuteQModbusReplyCall3>(taken[3]);
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
      CuteQModbusReplyCall4 call = reinterpret_cast<CuteQModbusReplyCall4>(taken[4]);
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
      CuteQModbusReplyCall5 call = reinterpret_cast<CuteQModbusReplyCall5>(taken[5]);
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
      CuteQModbusReplyCall6 call = reinterpret_cast<CuteQModbusReplyCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QModbusReply::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QModbusReply10metaObjectEv(
    const QModbusReply *self) {
  return self->metaObject();
}

//  QString QModbusReply::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QModbusReply2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QModbusReply::tr(s, c, n));
}

//  QModbusReply::QModbusReply(ReplyType type, int serverAddress, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QModbusReply *ritual_ZN12QModbusReplyC1ENS_9ReplyTypeEiP7QObject(
    QModbusReply::ReplyType type,
    int serverAddress,
    QObject *parent) {
  return new CuteQModbusReply(type, serverAddress, parent);
}

//  ReplyType QModbusReply::type() const
extern "C" Q_DECL_EXPORT
QModbusReply::ReplyType ritual_ZNK12QModbusReply4typeEv(
    const QModbusReply *self) {
  return self->type();
}

//  int QModbusReply::serverAddress() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QModbusReply13serverAddressEv(const QModbusReply *self) {
  return self->serverAddress();
}

//  bool QModbusReply::isFinished() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QModbusReply10isFinishedEv(const QModbusReply *self) {
  return self->isFinished();
}

//  QModbusDataUnit QModbusReply::result() const
extern "C" Q_DECL_EXPORT
QModbusDataUnit *ritual_ZNK12QModbusReply6resultEv(
    const QModbusReply *self) {
  return new QModbusDataUnit(self->result());
}

//  QModbusResponse QModbusReply::rawResult() const
extern "C" Q_DECL_EXPORT
QModbusResponse *ritual_ZNK12QModbusReply9rawResultEv(
    const QModbusReply *self) {
  return new QModbusResponse(self->rawResult());
}

//  QString QModbusReply::errorString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QModbusReply11errorStringEv(const QModbusReply *self) {
  return new QString(self->errorString());
}

//  QModbusDevice::Error QModbusReply::error() const
extern "C" Q_DECL_EXPORT
QModbusDevice::Error ritual_ZNK12QModbusReply5errorEv(
    const QModbusReply *self) {
  return self->error();
}

//  void QModbusReply::setResult(const QModbusDataUnit &unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QModbusReply9setResultERK15QModbusDataUnit(
    QModbusReply *self,
    const QModbusDataUnit *unit) {
  self->setResult(*unit);
}

//  void QModbusReply::setRawResult(const QModbusResponse &unit)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QModbusReply12setRawResultERK15QModbusResponse(
    QModbusReply *self,
    const QModbusResponse *unit) {
  self->setRawResult(*unit);
}

//  void QModbusReply::setFinished(bool isFinished)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QModbusReply11setFinishedEb(
    QModbusReply *self,
    bool isFinished) {
  self->setFinished(isFinished);
}

//  void QModbusReply::setError(QModbusDevice::Error error, const QString
//      &errorText)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QModbusReply8setErrorEN13QModbusDevice5ErrorERK7QString(
    QModbusReply *self,
    QModbusDevice::Error error,
    const QString *errorText) {
  self->setError(error, *errorText);
}

//  void QModbusReply::addIntermediateError(QModbusDevice::IntermediateError
//      error)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QModbusReply20addIntermediateErrorEN13QModbusDevice17IntermediateErrorE(
    QModbusReply *self,
    QModbusDevice::IntermediateError error) {
  self->addIntermediateError(error);
}

//  a Python function taken by a CuteQModbusReply, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QModbusReply(
    QModbusReply *self,
    const char *key,
    void *call) {
  return static_cast<CuteQModbusReply *>(self)->take(key, call);
}
