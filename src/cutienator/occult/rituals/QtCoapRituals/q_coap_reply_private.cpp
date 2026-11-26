//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapreply_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoapreply.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/qcoaprequest.h>
#include <QtCore/qbytearray.h>
#include <QtNetwork/qhostaddress.h>
#include <QtCoap/qcoapmessage.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapreply_p.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 62, as _ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE
inline void QCoapReplyPrivate::_q_setContent(const QHostAddress &, const QCoapMessage &msg,
                                      QtCoap::ResponseCode code)
{
    Q_Q(QCoapReply);

    if (q->isFinished())
        return;

    message = msg;
    responseCode = code;
    seekBuffer(0);

    if (QtCoap::isError(responseCode))
        _q_setError(responseCode);
}

//  from ../qtcoap/src/coap/qcoapnamespace.cpp, line 263, as _ZN6QtCoap20errorForResponseCodeENS_12ResponseCodeE
inline QtCoap::Error QtCoap::errorForResponseCode(QtCoap::ResponseCode code)
{
    if (!isError(code))
        return QtCoap::Error::Ok;

    switch (code) {
#define SINGLE_CASE(name, ignored) case ResponseCode::name: return Error::name;
        FOR_EACH_COAP_ERROR(SINGLE_CASE)
#undef SINGLE_CASE
    default:
        return Error::Unknown;
    }
}

//  from ../qtcoap/src/coap/qcoapnamespace.cpp, line 252, as _ZN6QtCoap7isErrorENS_12ResponseCodeE
inline bool QtCoap::isError(QtCoap::ResponseCode code)
{
    return static_cast<int>(code) >= 0x80;
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 19, as _ZN17QCoapReplyPrivateC1ERK12QCoapRequest
inline QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &req) :
    request(req)
{
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 31, as _ZN17QCoapReplyPrivate13_q_setRunningERK10QByteArrayt
inline void QCoapReplyPrivate::_q_setRunning(const QCoapToken &token, QCoapMessageId messageId)
{
    request.setToken(token);
    request.setMessageId(messageId);
    isRunning = true;
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 85, as _ZN17QCoapReplyPrivate14_q_setNotifiedEv
inline void QCoapReplyPrivate::_q_setNotified()
{
    Q_Q(QCoapReply);

    if (!q->isFinished())
        emit q->notified(q, message);
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 43, as _ZN17QCoapReplyPrivate22_q_setObserveCancelledEv
inline void QCoapReplyPrivate::_q_setObserveCancelled()
{
    Q_Q(QCoapReply);

    bool alreadyFinished = q->isFinished();

    isFinished = true;
    isRunning = false;

    if (!alreadyFinished)
        emit q->finished(q);
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 99, as _ZN17QCoapReplyPrivate14_q_setFinishedEN6QtCoap5ErrorE
inline void QCoapReplyPrivate::_q_setFinished(QtCoap::Error newError)
{
    Q_Q(QCoapReply);

    if (q->isFinished())
        return;

    isFinished = true;
    isRunning = false;

    if (newError != QtCoap::Error::Ok)
        _q_setError(newError);

    emit q->finished(q);
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 137, as _ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap12ResponseCodeE
inline void QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode code)
{
    _q_setError(QtCoap::errorForResponseCode(code));
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 122, as _ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap5ErrorE
inline void QCoapReplyPrivate::_q_setError(QtCoap::Error newError)
{
    Q_Q(QCoapReply);
    if (error == newError)
        return;

    error = newError;
    emit q->error(q, error);
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 399, as _ZN17QCoapReplyPrivate15createCoapReplyERK12QCoapRequestP7QObject
inline QCoapReply *QCoapReplyPrivate::createCoapReply(const QCoapRequest &request, QObject *parent)
{
    return new QCoapReply(*new QCoapReplyPrivate(request), parent);
}
//  -----------------------------------------------------------------------

//  A QCoapReplyPrivate that Python can take functions over in. Every QCoapReplyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCoapReplyPrivateCall0)(const void *, const QHostAddress *, const QCoapMessage *, int, int *);
typedef bool (*CuteQCoapReplyPrivateCall1)(const void *, char, int *);
typedef qint64 (*CuteQCoapReplyPrivateCall2)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQCoapReplyPrivateCall3)(const void *, qint64, int *);
class CuteQCoapReplyPrivate : public QCoapReplyPrivate {
public:
  using QCoapReplyPrivate::QCoapReplyPrivate;
  void *taken[4] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate13putCharHelperEc")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEPcx")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QIODevicePrivate4peekEx")) {
      taken[3] = call;
      return true;
    }
    return false;
  }

  //  void QCoapReplyPrivate::_q_setContent(const QHostAddress &sender,
  //      const QCoapMessage &a1, QtCoap::ResponseCode a2)
  void _q_setContent(
      const QHostAddress &sender,
      const QCoapMessage &a1,
      QtCoap::ResponseCode a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapReplyPrivateCall0 call = reinterpret_cast<CuteQCoapReplyPrivateCall0>(taken[0]);
      call(this, &sender, &a1, static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QCoapReplyPrivate::_q_setContent(sender, a1, a2);
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapReplyPrivateCall1 call = reinterpret_cast<CuteQCoapReplyPrivateCall1>(taken[1]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapReplyPrivateCall2 call = reinterpret_cast<CuteQCoapReplyPrivateCall2>(taken[2]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapReplyPrivateCall3 call = reinterpret_cast<CuteQCoapReplyPrivateCall3>(taken[3]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &request)
extern "C" Q_DECL_EXPORT
QCoapReplyPrivate *ritual_ZN17QCoapReplyPrivateC1ERK12QCoapRequest(
    const QCoapRequest *request) {
  return new CuteQCoapReplyPrivate(*request);
}

//  void QCoapReplyPrivate::_q_setRunning(const QCoapToken &a0,
//      QCoapMessageId a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate13_q_setRunningERK10QByteArrayt(
    QCoapReplyPrivate *self,
    const QByteArray *a0,
    QCoapMessageId a1) {
  self->_q_setRunning(*a0, a1);
}

//  void QCoapReplyPrivate::_q_setContent(const QHostAddress &sender, const
//      QCoapMessage &a1, QtCoap::ResponseCode a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE(
    QCoapReplyPrivate *self,
    const QHostAddress *sender,
    const QCoapMessage *a1,
    QtCoap::ResponseCode a2) {
  self->_q_setContent(*sender, *a1, a2);
}

//  void QCoapReplyPrivate::_q_setNotified()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate14_q_setNotifiedEv(
    QCoapReplyPrivate *self) {
  self->_q_setNotified();
}

//  void QCoapReplyPrivate::_q_setObserveCancelled()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate22_q_setObserveCancelledEv(
    QCoapReplyPrivate *self) {
  self->_q_setObserveCancelled();
}

//  void QCoapReplyPrivate::_q_setFinished(QtCoap::Error a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate14_q_setFinishedEN6QtCoap5ErrorE(
    QCoapReplyPrivate *self,
    QtCoap::Error a0) {
  self->_q_setFinished(a0);
}

//  void QCoapReplyPrivate::_q_setError(QtCoap::ResponseCode code)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap12ResponseCodeE(
    QCoapReplyPrivate *self,
    QtCoap::ResponseCode code) {
  self->_q_setError(code);
}

//  void QCoapReplyPrivate::_q_setError(QtCoap::Error a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QCoapReplyPrivate11_q_setErrorEN6QtCoap5ErrorE(
    QCoapReplyPrivate *self,
    QtCoap::Error a0) {
  self->_q_setError(a0);
}

//  QCoapReply *QCoapReplyPrivate::createCoapReply(const QCoapRequest
//      &request, QObject *parent)
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN17QCoapReplyPrivate15createCoapReplyERK12QCoapRequestP7QObject(
    const QCoapRequest *request,
    QObject *parent) {
  return QCoapReplyPrivate::createCoapReply(*request, parent);
}

//  QCoapReply *QCoapReplyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapReply *ritual_ZN17QCoapReplyPrivate6q_funcEv(QCoapReplyPrivate *self) {
  return self->q_func();
}

//  const QCoapReply *QCoapReplyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapReply *ritual_ZNK17QCoapReplyPrivate6q_funcEv(
    const QCoapReplyPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCoapReplyPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapReplyPrivate(
    QCoapReplyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapReplyPrivate *>(self)->take(key, call);
}

//  void QCoapReplyPrivate::_q_setContent(const QHostAddress &sender, const
//      QCoapMessage &a1, QtCoap::ResponseCode a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QCoapReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE(
    QCoapReplyPrivate *self,
    const QHostAddress *sender,
    const QCoapMessage *a1,
    QtCoap::ResponseCode a2) {
  self->QCoapReplyPrivate::_q_setContent(*sender, *a1, a2);
}
