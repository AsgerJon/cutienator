//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_pcsc_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_pcsc_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNfc/qnearfieldtarget.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QNearFieldTargetPrivateImpl that Python can take functions over in. Every QNearFieldTargetPrivateImpl
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QByteArray * (*CuteQNearFieldTargetPrivateImplCall0)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateImplCall1)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateImplCall2)(const void *, int *);
typedef bool (*CuteQNearFieldTargetPrivateImplCall3)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateImplCall4)(const void *, int *);
typedef const QNearFieldTarget::RequestId * (*CuteQNearFieldTargetPrivateImplCall5)(const void *, const QByteArray *, int *);
typedef const QNearFieldTarget::RequestId * (*CuteQNearFieldTargetPrivateImplCall6)(const void *, int *);
typedef bool (*CuteQNearFieldTargetPrivateImplCall7)(const void *, int *);
typedef void (*CuteQNearFieldTargetPrivateImplCall8)(const void *, const QNearFieldTarget::RequestId *, const QVariant *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetPrivateImplCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetPrivateImplCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateImplCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateImplCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateImplCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateImplCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateImplCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNearFieldTargetPrivateImpl : public QNearFieldTargetPrivateImpl {
public:
  using QNearFieldTargetPrivateImpl::QNearFieldTargetPrivateImpl;
  void *taken[16] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK23QNearFieldTargetPrivate3uidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QNearFieldTargetPrivate4typeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QNearFieldTargetPrivate13accessMethodsEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate10disconnectEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate16readNdefMessagesEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate14hasNdefMessageEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate21setResponseForRequestERKN16QNearFieldTarget9RequestIdERK8QVariantb")) {
      taken[8] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[14] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[15] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  QByteArray QNearFieldTargetPrivateImpl::uid() const
  QByteArray uid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall0 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivateImpl::uid();
  }

  //  QNearFieldTarget::Type QNearFieldTargetPrivateImpl::type() const
  QNearFieldTarget::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall1 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QNearFieldTarget::Type>(given);
    }
    return QNearFieldTargetPrivateImpl::type();
  }

  //  QNearFieldTarget::AccessMethods
  //      QNearFieldTargetPrivateImpl::accessMethods() const
  QNearFieldTarget::AccessMethods accessMethods() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall2 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QNearFieldTarget::AccessMethod>::fromInt(given);
    }
    return QNearFieldTargetPrivateImpl::accessMethods();
  }

  //  bool QNearFieldTargetPrivateImpl::disconnect()
  bool disconnect() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall3 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivateImpl::disconnect();
  }

  //  int QNearFieldTargetPrivateImpl::maxCommandLength() const
  int maxCommandLength() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall4 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivateImpl::maxCommandLength();
  }

  //  QNearFieldTarget::RequestId
  //      QNearFieldTargetPrivateImpl::sendCommand(const QByteArray
  //      &command)
  QNearFieldTarget::RequestId sendCommand(
      const QByteArray &command) override {
    if (taken[5]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall5 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall5>(taken[5]);
      const QNearFieldTarget::RequestId * given = call(this, &command, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivateImpl::sendCommand(command);
  }

  //  QNearFieldTarget::RequestId
  //      QNearFieldTargetPrivateImpl::readNdefMessages()
  QNearFieldTarget::RequestId readNdefMessages() override {
    if (taken[6]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall6 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall6>(taken[6]);
      const QNearFieldTarget::RequestId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivateImpl::readNdefMessages();
  }

  //  bool QNearFieldTargetPrivate::hasNdefMessage()
  bool hasNdefMessage() override {
    if (taken[7]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall7 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall7>(taken[7]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivate::hasNdefMessage();
  }

  //  void QNearFieldTargetPrivate::setResponseForRequest(const
  //      QNearFieldTarget::RequestId &id, const QVariant &response, bool
  //      emitRequestCompleted)
  void setResponseForRequest(
      const QNearFieldTarget::RequestId &id,
      const QVariant &response,
      bool emitRequestCompleted) override {
    if (taken[8]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall8 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall8>(taken[8]);
      call(this, &id, &response, emitRequestCompleted, &handled);
      if (handled) return;
    }
    QNearFieldTargetPrivate::setResponseForRequest(id, response, emitRequestCompleted);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall9 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall9>(taken[9]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall10 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall10>(taken[10]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall11 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall12 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall13 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[14]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall14 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall14>(taken[14]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[15]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateImplCall15 call = reinterpret_cast<CuteQNearFieldTargetPrivateImplCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNearFieldTargetPrivateImpl::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QNearFieldTargetPrivateImpl10metaObjectEv(
    const QNearFieldTargetPrivateImpl *self) {
  return self->metaObject();
}

//  a Python function taken by a CuteQNearFieldTargetPrivateImpl, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNearFieldTargetPrivateImpl(
    QNearFieldTargetPrivateImpl *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNearFieldTargetPrivateImpl *>(self)->take(key, call);
}
