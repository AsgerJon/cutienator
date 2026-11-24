//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapprotocol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapprotocol_p.h>
#include <QtCoap/private/qcoapinternalrequest_p.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/private/qcoapconnection_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#include <QtCore/qrandom.h>
#include <QtCore/qthread.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qnetworkdatagram.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 93, as _ZN13QCoapProtocolD1Ev
inline QCoapProtocol::~QCoapProtocol()
{
    Q_D(QCoapProtocol);

    // Clear table to avoid double deletion from QObject parenting and QSharedPointer.
    d->exchangeMap.clear();
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 889, as _ZNK13QCoapProtocol10ackTimeoutEv
inline uint QCoapProtocol::ackTimeout() const
{
    Q_D(const QCoapProtocol);
    return d->ackTimeout;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 903, as _ZNK13QCoapProtocol15ackRandomFactorEv
inline double QCoapProtocol::ackRandomFactor() const
{
    Q_D(const QCoapProtocol);
    return d->ackRandomFactor;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 918, as _ZNK13QCoapProtocol22maximumRetransmitCountEv
inline uint QCoapProtocol::maximumRetransmitCount() const
{
    Q_D(const QCoapProtocol);
    return d->maximumRetransmitCount;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 932, as _ZNK13QCoapProtocol9blockSizeEv
inline quint16 QCoapProtocol::blockSize() const
{
    Q_D(const QCoapProtocol);
    return d->blockSize;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 947, as _ZNK13QCoapProtocol19maximumTransmitSpanEv
inline uint QCoapProtocol::maximumTransmitSpan() const
{
    return static_cast<uint>(ackTimeout()
                             * ((1u << maximumRetransmitCount()) - 1)
                             * ackRandomFactor());
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 964, as _ZNK13QCoapProtocol19maximumTransmitWaitEv
inline uint QCoapProtocol::maximumTransmitWait() const
{
    return static_cast<uint>(ackTimeout() * ((1u << (maximumRetransmitCount() + 1)) - 1)
                             * ackRandomFactor());
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 980, as _ZNK13QCoapProtocol14maximumLatencyEv
inline uint QCoapProtocol::maximumLatency() const
{
    return 100 * 1000;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 994, as _ZNK13QCoapProtocol14minimumTimeoutEv
inline uint QCoapProtocol::minimumTimeout() const
{
    Q_D(const QCoapProtocol);
    return d->ackTimeout;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 1007, as _ZNK13QCoapProtocol14maximumTimeoutEv
inline uint QCoapProtocol::maximumTimeout() const
{
    Q_D(const QCoapProtocol);
    return static_cast<uint>(d->ackTimeout * d->ackRandomFactor);
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 1022, as _ZNK13QCoapProtocol18nonConfirmLifetimeEv
inline uint QCoapProtocol::nonConfirmLifetime() const
{
    return maximumTransmitSpan() + maximumLatency();
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 1038, as _ZNK13QCoapProtocol26maximumServerResponseDelayEv
inline uint QCoapProtocol::maximumServerResponseDelay() const
{
    Q_D(const QCoapProtocol);
    return d->maximumServerResponseDelay;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 1056, as _ZN13QCoapProtocol13setAckTimeoutEj
inline void QCoapProtocol::setAckTimeout(uint ackTimeout)
{
    Q_D(QCoapProtocol);
    d->ackTimeout = ackTimeout;
}

//  from ../qtcoap/src/coap/qcoapprotocol.cpp, line 1140, as _ZN13QCoapProtocol29setMaximumServerResponseDelayEj
inline void QCoapProtocol::setMaximumServerResponseDelay(uint responseDelay)
{
    Q_D(QCoapProtocol);
    d->maximumServerResponseDelay = responseDelay;
}
//  -----------------------------------------------------------------------

//  A QCoapProtocol that Python can take functions over in. Every QCoapProtocol
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapProtocolCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQCoapProtocolCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapProtocolCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapProtocolCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapProtocolCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapProtocolCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQCoapProtocolCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQCoapProtocol : public QCoapProtocol {
public:
  using QCoapProtocol::QCoapProtocol;
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
      CuteQCoapProtocolCall0 call = reinterpret_cast<CuteQCoapProtocolCall0>(taken[0]);
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
      CuteQCoapProtocolCall1 call = reinterpret_cast<CuteQCoapProtocolCall1>(taken[1]);
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
      CuteQCoapProtocolCall2 call = reinterpret_cast<CuteQCoapProtocolCall2>(taken[2]);
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
      CuteQCoapProtocolCall3 call = reinterpret_cast<CuteQCoapProtocolCall3>(taken[3]);
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
      CuteQCoapProtocolCall4 call = reinterpret_cast<CuteQCoapProtocolCall4>(taken[4]);
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
      CuteQCoapProtocolCall5 call = reinterpret_cast<CuteQCoapProtocolCall5>(taken[5]);
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
      CuteQCoapProtocolCall6 call = reinterpret_cast<CuteQCoapProtocolCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QCoapProtocol::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QCoapProtocol10metaObjectEv(
    const QCoapProtocol *self) {
  return self->metaObject();
}

//  QCoapProtocol::~QCoapProtocol()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapProtocolD1Ev(QCoapProtocol *self) {
  delete self;
}

//  uint QCoapProtocol::ackTimeout() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol10ackTimeoutEv(const QCoapProtocol *self) {
  return self->ackTimeout();
}

//  double QCoapProtocol::ackRandomFactor() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QCoapProtocol15ackRandomFactorEv(
    const QCoapProtocol *self) {
  return self->ackRandomFactor();
}

//  uint QCoapProtocol::maximumRetransmitCount() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol22maximumRetransmitCountEv(
    const QCoapProtocol *self) {
  return self->maximumRetransmitCount();
}

//  quint16 QCoapProtocol::blockSize() const
extern "C" Q_DECL_EXPORT
quint16 ritual_ZNK13QCoapProtocol9blockSizeEv(const QCoapProtocol *self) {
  return self->blockSize();
}

//  uint QCoapProtocol::maximumTransmitSpan() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol19maximumTransmitSpanEv(
    const QCoapProtocol *self) {
  return self->maximumTransmitSpan();
}

//  uint QCoapProtocol::maximumTransmitWait() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol19maximumTransmitWaitEv(
    const QCoapProtocol *self) {
  return self->maximumTransmitWait();
}

//  uint QCoapProtocol::maximumLatency() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol14maximumLatencyEv(const QCoapProtocol *self) {
  return self->maximumLatency();
}

//  uint QCoapProtocol::minimumTimeout() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol14minimumTimeoutEv(const QCoapProtocol *self) {
  return self->minimumTimeout();
}

//  uint QCoapProtocol::maximumTimeout() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol14maximumTimeoutEv(const QCoapProtocol *self) {
  return self->maximumTimeout();
}

//  uint QCoapProtocol::nonConfirmLifetime() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol18nonConfirmLifetimeEv(
    const QCoapProtocol *self) {
  return self->nonConfirmLifetime();
}

//  uint QCoapProtocol::maximumServerResponseDelay() const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK13QCoapProtocol26maximumServerResponseDelayEv(
    const QCoapProtocol *self) {
  return self->maximumServerResponseDelay();
}

//  void QCoapProtocol::setAckTimeout(uint ackTimeout)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapProtocol13setAckTimeoutEj(
    QCoapProtocol *self,
    uint ackTimeout) {
  self->setAckTimeout(ackTimeout);
}

//  void QCoapProtocol::setMaximumServerResponseDelay(uint responseDelay)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QCoapProtocol29setMaximumServerResponseDelayEj(
    QCoapProtocol *self,
    uint responseDelay) {
  self->setMaximumServerResponseDelay(responseDelay);
}

//  QCoapProtocolPrivate *QCoapProtocol::d_func()
extern "C" Q_DECL_EXPORT
QCoapProtocolPrivate *ritual_ZN13QCoapProtocol6d_funcEv(
    QCoapProtocol *self) {
  return self->d_func();
}

//  const QCoapProtocolPrivate *QCoapProtocol::d_func() const
extern "C" Q_DECL_EXPORT
const QCoapProtocolPrivate *ritual_ZNK13QCoapProtocol6d_funcEv(
    const QCoapProtocol *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQCoapProtocol, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapProtocol(
    QCoapProtocol *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapProtocol *>(self)->take(key, call);
}
