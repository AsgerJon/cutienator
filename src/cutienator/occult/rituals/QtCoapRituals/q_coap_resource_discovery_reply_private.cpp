//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapresourcediscoveryreply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoapresourcediscoveryreply.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapresourcediscoveryreply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qhostaddress.h>
#include <QtCoap/qcoapmessage.h>
#include <QtCore/qbytearray.h>
#include <QtCoap/qcoapresource.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapreply_p.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapresourcediscoveryreply_p.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 19, as _ZN17QCoapReplyPrivateC2ERK12QCoapRequest
inline QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &req) :
    request(req)
{
}

//  from ../qtcoap/src/coap/qcoapresourcediscoveryreply.cpp, line 23, as _ZN34QCoapResourceDiscoveryReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE
inline void QCoapResourceDiscoveryReplyPrivate::_q_setContent(const QHostAddress &sender,
                                                       const QCoapMessage &msg,
                                                       QtCoap::ResponseCode code)
{
    Q_Q(QCoapResourceDiscoveryReply);

    if (q->isFinished())
        return;

    message = msg;
    responseCode = code;

    if (QtCoap::isError(responseCode)) {
        _q_setError(responseCode);
    } else {
        auto res = QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(sender,
                                                                                 message.payload());
        resources.append(res);
        emit q->discovered(q, res);
    }
}

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

//  from ../qtcoap/src/coap/qcoapresourcediscoveryreply.cpp, line 104, as _ZN34QCoapResourceDiscoveryReplyPrivate25resourcesFromCoreLinkListERK12QHostAddressRK10QByteArray
inline QList<QCoapResource>
QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(const QHostAddress &sender,
                                                              const QByteArray &data)
{
    QList<QCoapResource> resourceList;

    QLatin1String quote = QLatin1String("\"");
    const QList<QByteArray> links = data.split(',');
    for (const QByteArray &link : links) {
        QCoapResource resource;
        resource.setHost(sender);

        const QList<QByteArray> parameterList = link.split(';');
        for (const QByteArray &parameter : parameterList) {
            QString parameterString = QString::fromUtf8(parameter);
            const qsizetype length = parameterString.size();
            if (parameter.startsWith('<') && parameter.endsWith('>'))
                resource.setPath(parameterString.mid(1, length - 2));
            else if (parameter.startsWith("title="))
                resource.setTitle(parameterString.mid(6).remove(quote));
            else if (parameter.startsWith("rt="))
                resource.setResourceType(parameterString.mid(3).remove(quote));
            else if (parameter.startsWith("if="))
                resource.setInterface(parameterString.mid(3).remove(quote));
            else if (parameter.startsWith("sz="))
                resource.setMaximumSize(parameterString.mid(3).remove(quote).toInt());
            else if (parameter.startsWith("ct="))
                resource.setContentFormat(parameterString.mid(3).remove(quote).toUInt());
            else if (parameter == "obs")
                resource.setObservable(true);
        }

        if (!resource.path().isEmpty())
            resourceList.push_back(resource);
    }

    return resourceList;
}
//  -----------------------------------------------------------------------

//  A QCoapResourceDiscoveryReplyPrivate that Python can take functions over in. Every QCoapResourceDiscoveryReplyPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQCoapResourceDiscoveryReplyPrivateCall0)(const void *, const QHostAddress *, const QCoapMessage *, int, int *);
typedef bool (*CuteQCoapResourceDiscoveryReplyPrivateCall1)(const void *, char, int *);
typedef qint64 (*CuteQCoapResourceDiscoveryReplyPrivateCall2)(const void *, char *, qint64, int *);
typedef const QByteArray * (*CuteQCoapResourceDiscoveryReplyPrivateCall3)(const void *, qint64, int *);
class CuteQCoapResourceDiscoveryReplyPrivate : public QCoapResourceDiscoveryReplyPrivate {
public:
  using QCoapResourceDiscoveryReplyPrivate::QCoapResourceDiscoveryReplyPrivate;
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

  //  void QCoapResourceDiscoveryReplyPrivate::_q_setContent(const
  //      QHostAddress &sender, const QCoapMessage &a1,
  //      QtCoap::ResponseCode a2)
  void _q_setContent(
      const QHostAddress &sender,
      const QCoapMessage &a1,
      QtCoap::ResponseCode a2) override {
    if (taken[0]) {
      int handled = 0;
      CuteQCoapResourceDiscoveryReplyPrivateCall0 call = reinterpret_cast<CuteQCoapResourceDiscoveryReplyPrivateCall0>(taken[0]);
      call(this, &sender, &a1, static_cast<int>(a2), &handled);
      if (handled) return;
    }
    QCoapResourceDiscoveryReplyPrivate::_q_setContent(sender, a1, a2);
  }

  //  bool QIODevicePrivate::putCharHelper(char c)
  bool putCharHelper(char c) override {
    if (taken[1]) {
      int handled = 0;
      CuteQCoapResourceDiscoveryReplyPrivateCall1 call = reinterpret_cast<CuteQCoapResourceDiscoveryReplyPrivateCall1>(taken[1]);
      bool given = call(this, c, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::putCharHelper(c);
  }

  //  qint64 QIODevicePrivate::peek(char *data, qint64 maxSize)
  qint64 peek(char *data, qint64 maxSize) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCoapResourceDiscoveryReplyPrivateCall2 call = reinterpret_cast<CuteQCoapResourceDiscoveryReplyPrivateCall2>(taken[2]);
      qint64 given = call(this, data, maxSize, &handled);
      if (handled) return given;
    }
    return QIODevicePrivate::peek(data, maxSize);
  }

  //  QByteArray QIODevicePrivate::peek(qint64 maxSize)
  QByteArray peek(qint64 maxSize) override {
    if (taken[3]) {
      int handled = 0;
      CuteQCoapResourceDiscoveryReplyPrivateCall3 call = reinterpret_cast<CuteQCoapResourceDiscoveryReplyPrivateCall3>(taken[3]);
      const QByteArray * given = call(this, maxSize, &handled);
      if (handled && given) return *given;
    }
    return QIODevicePrivate::peek(maxSize);
  }
};

//  void QCoapResourceDiscoveryReplyPrivate::_q_setContent(const QHostAddress
//      &sender, const QCoapMessage &a1, QtCoap::ResponseCode a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN34QCoapResourceDiscoveryReplyPrivate13_q_setContentERK12QHostAddressRK12QCoapMessageN6QtCoap12ResponseCodeE(
    QCoapResourceDiscoveryReplyPrivate *self,
    const QHostAddress *sender,
    const QCoapMessage *a1,
    QtCoap::ResponseCode a2) {
  self->_q_setContent(*sender, *a1, a2);
}

//  QList<QCoapResource>
//      QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(const
//      QHostAddress &sender, const QByteArray &data)
extern "C" Q_DECL_EXPORT
QList<QCoapResource> *ritual_ZN34QCoapResourceDiscoveryReplyPrivate25resourcesFromCoreLinkListERK12QHostAddressRK10QByteArray(
    const QHostAddress *sender,
    const QByteArray *data) {
  return new QList<QCoapResource>(
      QCoapResourceDiscoveryReplyPrivate::resourcesFromCoreLinkList(
          *sender,
          *data));
}

//  QCoapResourceDiscoveryReply *QCoapResourceDiscoveryReplyPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapResourceDiscoveryReply *ritual_ZN34QCoapResourceDiscoveryReplyPrivate6q_funcEv(
    QCoapResourceDiscoveryReplyPrivate *self) {
  return self->q_func();
}

//  const QCoapResourceDiscoveryReply
//      *QCoapResourceDiscoveryReplyPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapResourceDiscoveryReply *ritual_ZNK34QCoapResourceDiscoveryReplyPrivate6q_funcEv(
    const QCoapResourceDiscoveryReplyPrivate *self) {
  return self->q_func();
}

//  a Python function taken by a CuteQCoapResourceDiscoveryReplyPrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCoapResourceDiscoveryReplyPrivate(
    QCoapResourceDiscoveryReplyPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCoapResourceDiscoveryReplyPrivate *>(self)->take(key, call);
}
