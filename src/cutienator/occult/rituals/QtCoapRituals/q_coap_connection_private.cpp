//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapconnection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapconnection_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 223, as _ZN15QCoapConnection18startToSendRequestEv
inline void QCoapConnection::startToSendRequest()
{
    Q_D(QCoapConnection);

    Q_ASSERT(!d->framesToSend.isEmpty());
    while (!d->framesToSend.isEmpty()) {
        const CoapFrame frame = d->framesToSend.dequeue();
        writeData(frame.currentPdu, frame.host, frame.port);
    }
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 119, as _ZN22QCoapConnectionPrivateC1EN6QtCoap12SecurityModeE
inline QCoapConnectionPrivate::QCoapConnectionPrivate(QtCoap::SecurityMode security)
    : securityMode(security)
    , state(QCoapConnection::ConnectionState::Unconnected)
{}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 170, as _ZN22QCoapConnectionPrivate11sendRequestERK10QByteArrayRK7QStringt
inline void
QCoapConnectionPrivate::sendRequest(const QByteArray &request, const QString &host, quint16 port)
{
    Q_Q(QCoapConnection);

    CoapFrame frame(request, host, port);
    framesToSend.enqueue(frame);

    if (state == QCoapConnection::ConnectionState::Unconnected)
        q->bind(host, port);
    else
        q->startToSendRequest();
}
//  -----------------------------------------------------------------------

//  QCoapConnectionPrivate::QCoapConnectionPrivate(QtCoap::SecurityMode
//      security)
extern "C" Q_DECL_EXPORT
QCoapConnectionPrivate *ritual_ZN22QCoapConnectionPrivateC1EN6QtCoap12SecurityModeE(
    QtCoap::SecurityMode security) {
  return new QCoapConnectionPrivate(security);
}

//  QCoapConnectionPrivate::~QCoapConnectionPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCoapConnectionPrivateD1Ev(QCoapConnectionPrivate *self) {
  delete self;
}

//  void QCoapConnectionPrivate::sendRequest(const QByteArray &request, const
//      QString &host, quint16 port)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QCoapConnectionPrivate11sendRequestERK10QByteArrayRK7QStringt(
    QCoapConnectionPrivate *self,
    const QByteArray *request,
    const QString *host,
    quint16 port) {
  self->sendRequest(*request, *host, port);
}

//  QCoapConnection *QCoapConnectionPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapConnection *ritual_ZN22QCoapConnectionPrivate6q_funcEv(
    QCoapConnectionPrivate *self) {
  return self->q_func();
}

//  const QCoapConnection *QCoapConnectionPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapConnection *ritual_ZNK22QCoapConnectionPrivate6q_funcEv(
    const QCoapConnectionPrivate *self) {
  return self->q_func();
}
