//  Written by dev_tooling.RitualGenerator from the records of
//  QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtNfc/6.12.0/QtNfc/private/qtnfcglobal_p.h>
#include <QtNfc/QtNfc>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNfc/6.12.0/QtNfc/private/qnearfieldtarget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtNfc/qnearfieldtarget.h>
#include <QtNfc/qndefmessage.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qnearfieldtarget_p.h"
#include <QtCore/QCoreApplication>
#include <QtCore/QElapsedTimer>
#include <QtCore/QPointer>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 34, as _ZN23QNearFieldTargetPrivate10disconnectEv
inline bool QNearFieldTargetPrivate::disconnect()
{
    return false;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 19, as _ZNK23QNearFieldTargetPrivate3uidEv
inline QByteArray QNearFieldTargetPrivate::uid() const
{
    return QByteArray();
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 24, as _ZNK23QNearFieldTargetPrivate4typeEv
inline QNearFieldTarget::Type QNearFieldTargetPrivate::type() const
{
    return QNearFieldTarget::Type::ProprietaryTag;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 29, as _ZNK23QNearFieldTargetPrivate13accessMethodsEv
inline QNearFieldTarget::AccessMethods QNearFieldTargetPrivate::accessMethods() const
{
    return QNearFieldTarget::AccessMethod::UnknownAccess;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 40, as _ZN23QNearFieldTargetPrivate14hasNdefMessageEv
inline bool QNearFieldTargetPrivate::hasNdefMessage()
{
    return false;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 45, as _ZN23QNearFieldTargetPrivate16readNdefMessagesEv
inline QNearFieldTarget::RequestId QNearFieldTargetPrivate::readNdefMessages()
{
    const QNearFieldTarget::RequestId id;
    Q_EMIT error(QNearFieldTarget::UnsupportedError, id);
    return id;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 63, as _ZNK23QNearFieldTargetPrivate16maxCommandLengthEv
inline int QNearFieldTargetPrivate::maxCommandLength() const
{
    return 0;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 68, as _ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray
inline QNearFieldTarget::RequestId QNearFieldTargetPrivate::sendCommand(const QByteArray &command)
{
    Q_UNUSED(command);

    const QNearFieldTarget::RequestId id;
    Q_EMIT error(QNearFieldTarget::UnsupportedError, id);
    return id;
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 105, as _ZN23QNearFieldTargetPrivate21setResponseForRequestERKN16QNearFieldTarget9RequestIdERK8QVariantb
inline void QNearFieldTargetPrivate::setResponseForRequest(const QNearFieldTarget::RequestId &id,
                                                    const QVariant &response,
                                                    bool emitRequestCompleted)
{
    for (auto i = m_decodedResponses.begin(), end = m_decodedResponses.end(); i != end; /* erasing */) {
        // no more external references
        if (i.key().refCount() == 1)
            i = m_decodedResponses.erase(i);
        else
            ++i;
    }

    m_decodedResponses.insert(id, response);

    if (emitRequestCompleted)
        Q_EMIT requestCompleted(id);
}

//  from ../qtconnectivity/src/nfc/qnearfieldtarget_p.cpp, line 100, as _ZNK23QNearFieldTargetPrivate15requestResponseERKN16QNearFieldTarget9RequestIdE
inline QVariant QNearFieldTargetPrivate::requestResponse(const QNearFieldTarget::RequestId &id) const
{
    return m_decodedResponses.value(id);
}
//  -----------------------------------------------------------------------

//  A QNearFieldTargetPrivate that Python can take functions over in. Every QNearFieldTargetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QByteArray * (*CuteQNearFieldTargetPrivateCall0)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateCall1)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateCall2)(const void *, int *);
typedef bool (*CuteQNearFieldTargetPrivateCall3)(const void *, int *);
typedef bool (*CuteQNearFieldTargetPrivateCall4)(const void *, int *);
typedef const QNearFieldTarget::RequestId * (*CuteQNearFieldTargetPrivateCall5)(const void *, int *);
typedef int (*CuteQNearFieldTargetPrivateCall6)(const void *, int *);
typedef const QNearFieldTarget::RequestId * (*CuteQNearFieldTargetPrivateCall7)(const void *, const QByteArray *, int *);
typedef void (*CuteQNearFieldTargetPrivateCall8)(const void *, const QNearFieldTarget::RequestId *, const QVariant *, bool, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetPrivateCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQNearFieldTargetPrivateCall10)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateCall11)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateCall12)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateCall13)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateCall14)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQNearFieldTargetPrivateCall15)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQNearFieldTargetPrivate : public QNearFieldTargetPrivate {
public:
  using QNearFieldTargetPrivate::QNearFieldTargetPrivate;
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
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate14hasNdefMessageEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate16readNdefMessagesEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray")) {
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

  //  QByteArray QNearFieldTargetPrivate::uid() const
  QByteArray uid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall0 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall0>(taken[0]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivate::uid();
  }

  //  QNearFieldTarget::Type QNearFieldTargetPrivate::type() const
  QNearFieldTarget::Type type() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall1 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall1>(taken[1]);
      int given = call(this, &handled);
      if (handled) return static_cast<QNearFieldTarget::Type>(given);
    }
    return QNearFieldTargetPrivate::type();
  }

  //  QNearFieldTarget::AccessMethods
  //      QNearFieldTargetPrivate::accessMethods() const
  QNearFieldTarget::AccessMethods accessMethods() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall2 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall2>(taken[2]);
      int given = call(this, &handled);
      if (handled) return QFlags<QNearFieldTarget::AccessMethod>::fromInt(given);
    }
    return QNearFieldTargetPrivate::accessMethods();
  }

  //  bool QNearFieldTargetPrivate::disconnect()
  bool disconnect() override {
    if (taken[3]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall3 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall3>(taken[3]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivate::disconnect();
  }

  //  bool QNearFieldTargetPrivate::hasNdefMessage()
  bool hasNdefMessage() override {
    if (taken[4]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall4 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivate::hasNdefMessage();
  }

  //  QNearFieldTarget::RequestId
  //      QNearFieldTargetPrivate::readNdefMessages()
  QNearFieldTarget::RequestId readNdefMessages() override {
    if (taken[5]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall5 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall5>(taken[5]);
      const QNearFieldTarget::RequestId * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivate::readNdefMessages();
  }

  //  int QNearFieldTargetPrivate::maxCommandLength() const
  int maxCommandLength() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall6 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall6>(taken[6]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QNearFieldTargetPrivate::maxCommandLength();
  }

  //  QNearFieldTarget::RequestId
  //      QNearFieldTargetPrivate::sendCommand(const QByteArray &command)
  QNearFieldTarget::RequestId sendCommand(
      const QByteArray &command) override {
    if (taken[7]) {
      int handled = 0;
      CuteQNearFieldTargetPrivateCall7 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall7>(taken[7]);
      const QNearFieldTarget::RequestId * given = call(this, &command, &handled);
      if (handled && given) return *given;
    }
    return QNearFieldTargetPrivate::sendCommand(command);
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
      CuteQNearFieldTargetPrivateCall8 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall8>(taken[8]);
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
      CuteQNearFieldTargetPrivateCall9 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall9>(taken[9]);
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
      CuteQNearFieldTargetPrivateCall10 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall10>(taken[10]);
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
      CuteQNearFieldTargetPrivateCall11 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall11>(taken[11]);
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
      CuteQNearFieldTargetPrivateCall12 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall12>(taken[12]);
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
      CuteQNearFieldTargetPrivateCall13 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall13>(taken[13]);
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
      CuteQNearFieldTargetPrivateCall14 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall14>(taken[14]);
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
      CuteQNearFieldTargetPrivateCall15 call = reinterpret_cast<CuteQNearFieldTargetPrivateCall15>(taken[15]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QNearFieldTargetPrivate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK23QNearFieldTargetPrivate10metaObjectEv(
    const QNearFieldTargetPrivate *self) {
  return self->metaObject();
}

//  QNearFieldTargetPrivate::~QNearFieldTargetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNearFieldTargetPrivateD1Ev(QNearFieldTargetPrivate *self) {
  delete self;
}

//  QByteArray QNearFieldTargetPrivate::uid() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK23QNearFieldTargetPrivate3uidEv(
    const QNearFieldTargetPrivate *self) {
  return new QByteArray(self->uid());
}

//  QNearFieldTarget::Type QNearFieldTargetPrivate::type() const
extern "C" Q_DECL_EXPORT
QNearFieldTarget::Type ritual_ZNK23QNearFieldTargetPrivate4typeEv(
    const QNearFieldTargetPrivate *self) {
  return self->type();
}

//  QNearFieldTarget::AccessMethods QNearFieldTargetPrivate::accessMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QNearFieldTargetPrivate13accessMethodsEv(
    const QNearFieldTargetPrivate *self) {
  return static_cast<int>(self->accessMethods().toInt());
}

//  bool QNearFieldTargetPrivate::disconnect()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QNearFieldTargetPrivate10disconnectEv(
    QNearFieldTargetPrivate *self) {
  return self->disconnect();
}

//  bool QNearFieldTargetPrivate::hasNdefMessage()
extern "C" Q_DECL_EXPORT
bool ritual_ZN23QNearFieldTargetPrivate14hasNdefMessageEv(
    QNearFieldTargetPrivate *self) {
  return self->hasNdefMessage();
}

//  QNearFieldTarget::RequestId QNearFieldTargetPrivate::readNdefMessages()
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN23QNearFieldTargetPrivate16readNdefMessagesEv(
    QNearFieldTargetPrivate *self) {
  return new QNearFieldTarget::RequestId(self->readNdefMessages());
}

//  QNearFieldTarget::RequestId
//      QNearFieldTargetPrivate::writeNdefMessages(const QList<QNdefMessage>
//      &messages)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN23QNearFieldTargetPrivate17writeNdefMessagesERK5QListI12QNdefMessageE(
    QNearFieldTargetPrivate *self,
    const QList<QNdefMessage> *messages) {
  return new QNearFieldTarget::RequestId(self->writeNdefMessages(*messages));
}

//  int QNearFieldTargetPrivate::maxCommandLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv(
    const QNearFieldTargetPrivate *self) {
  return self->maxCommandLength();
}

//  QNearFieldTarget::RequestId QNearFieldTargetPrivate::sendCommand(const
//      QByteArray &command)
extern "C" Q_DECL_EXPORT
QNearFieldTarget::RequestId *ritual_ZN23QNearFieldTargetPrivate11sendCommandERK10QByteArray(
    QNearFieldTargetPrivate *self,
    const QByteArray *command) {
  return new QNearFieldTarget::RequestId(self->sendCommand(*command));
}

//  QVariant QNearFieldTargetPrivate::requestResponse(const
//      QNearFieldTarget::RequestId &id) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK23QNearFieldTargetPrivate15requestResponseERKN16QNearFieldTarget9RequestIdE(
    const QNearFieldTargetPrivate *self,
    const QNearFieldTarget::RequestId *id) {
  return new QVariant(self->requestResponse(*id));
}

//  void QNearFieldTargetPrivate::setResponseForRequest(const
//      QNearFieldTarget::RequestId &id, const QVariant &response, bool
//      emitRequestCompleted)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QNearFieldTargetPrivate21setResponseForRequestERKN16QNearFieldTarget9RequestIdERK8QVariantb(
    QNearFieldTargetPrivate *self,
    const QNearFieldTarget::RequestId *id,
    const QVariant *response,
    bool emitRequestCompleted) {
  self->setResponseForRequest(*id, *response, emitRequestCompleted);
}

//  a Python function taken by a CuteQNearFieldTargetPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QNearFieldTargetPrivate(
    QNearFieldTargetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQNearFieldTargetPrivate *>(self)->take(key, call);
}

//  QByteArray QNearFieldTargetPrivate::uid() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_own_ZNK23QNearFieldTargetPrivate3uidEv(
    const QNearFieldTargetPrivate *self) {
  return new QByteArray(self->QNearFieldTargetPrivate::uid());
}

//  QNearFieldTarget::Type QNearFieldTargetPrivate::type() const
extern "C" Q_DECL_EXPORT
QNearFieldTarget::Type ritual_own_ZNK23QNearFieldTargetPrivate4typeEv(
    const QNearFieldTargetPrivate *self) {
  return self->QNearFieldTargetPrivate::type();
}

//  QNearFieldTarget::AccessMethods QNearFieldTargetPrivate::accessMethods()
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QNearFieldTargetPrivate13accessMethodsEv(
    const QNearFieldTargetPrivate *self) {
  return static_cast<int>(
      self->QNearFieldTargetPrivate::accessMethods().toInt());
}

//  bool QNearFieldTargetPrivate::disconnect()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QNearFieldTargetPrivate10disconnectEv(
    QNearFieldTargetPrivate *self) {
  return self->QNearFieldTargetPrivate::disconnect();
}

//  bool QNearFieldTargetPrivate::hasNdefMessage()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN23QNearFieldTargetPrivate14hasNdefMessageEv(
    QNearFieldTargetPrivate *self) {
  return self->QNearFieldTargetPrivate::hasNdefMessage();
}

//  int QNearFieldTargetPrivate::maxCommandLength() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK23QNearFieldTargetPrivate16maxCommandLengthEv(
    const QNearFieldTargetPrivate *self) {
  return self->QNearFieldTargetPrivate::maxCommandLength();
}
