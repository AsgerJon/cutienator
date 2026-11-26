//  Written by dev_tooling.RitualGenerator from the records of
//  QtCoap/6.12.0/QtCoap/private/qcoapclient_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCoap/qcoapclient.h>
#include <QtCoap/QtCoap>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/6.12.0/QtCoap/private/qcoapclient_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCoap/private/qcoapreply_p.h>
#include <QtCoap/private/qcoapinternalreply_p.h>
#include <QtCoap/private/qcoapnamespace_p.h>
#include <QtCore/qmath.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapconnection_p.h>
#include <QtCore/qloggingcategory.h>
#include <QtCoap/private/qcoapclient_p.h>
#include <QtCoap/private/qcoapprotocol_p.h>
#include <QtCoap/qcoapreply.h>
#include <QtCoap/qcoapresourcediscoveryreply.h>
#include <QtCoap/qcoapnamespace.h>
#include <QtCoap/qcoapsecurityconfiguration.h>
#include <QtCoap/private/qcoapqudpconnection_p.h>
#include <QtCoap/private/qcoaprequest_p.h>
#include <QtCoap/private/qcoapreply_p.h>
#include <QtCore/qiodevice.h>
#include <QtCore/qurl.h>
#include <QtCore/qloggingcategory.h>
#include <QtNetwork/qudpsocket.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 399, as _ZN17QCoapReplyPrivate15createCoapReplyERK12QCoapRequestP7QObject
inline QCoapReply *QCoapReplyPrivate::createCoapReply(const QCoapRequest &request, QObject *parent)
{
    return new QCoapReply(*new QCoapReplyPrivate(request), parent);
}

//  from ../qtcoap/src/coap/qcoapconnection.cpp, line 270, as _ZN15QCoapConnection10disconnectEv
inline void QCoapConnection::disconnect()
{
    Q_D(QCoapConnection);

    close();

    d->framesToSend.clear();
    d->state = ConnectionState::Unconnected;
}

//  from ../qtcoap/src/coap/qcoapreply.cpp, line 19, as _ZN17QCoapReplyPrivateC1ERK12QCoapRequest
inline QCoapReplyPrivate::QCoapReplyPrivate(const QCoapRequest &req) :
    request(req)
{
}

//  from ../qtcoap/src/coap/qcoapclient.cpp, line 24, as _ZN18QCoapClientPrivateC1EP13QCoapProtocolP15QCoapConnection
inline QCoapClientPrivate::QCoapClientPrivate(QCoapProtocol *protocol, QCoapConnection *connection)
    : protocol(protocol)
    , connection(connection)
    , workerThread(new QThread)
{
    protocol->moveToThread(workerThread);
    connection->moveToThread(workerThread);
    workerThread->start();
}

//  from ../qtcoap/src/coap/qcoapclient.cpp, line 34, as _ZN18QCoapClientPrivateD1Ev
inline QCoapClientPrivate::~QCoapClientPrivate()
{
    // protocol and connection (and their children, such as the retransmission
    // timers and the UDP socket) live in workerThread. They must be destroyed in
    // that thread, not here.
    protocol->deleteLater();
    connection->deleteLater();
    workerThread->quit();
    workerThread->wait();
    delete workerThread;
}
//  -----------------------------------------------------------------------

//  QCoapClientPrivate::QCoapClientPrivate(QCoapProtocol *protocol,
//      QCoapConnection *connection)
extern "C" Q_DECL_EXPORT
QCoapClientPrivate *ritual_ZN18QCoapClientPrivateC1EP13QCoapProtocolP15QCoapConnection(
    QCoapProtocol *protocol,
    QCoapConnection *connection) {
  return new QCoapClientPrivate(protocol, connection);
}

//  QCoapClientPrivate::~QCoapClientPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCoapClientPrivateD1Ev(QCoapClientPrivate *self) {
  delete self;
}

//  QCoapClient *QCoapClientPrivate::q_func()
extern "C" Q_DECL_EXPORT
QCoapClient *ritual_ZN18QCoapClientPrivate6q_funcEv(
    QCoapClientPrivate *self) {
  return self->q_func();
}

//  const QCoapClient *QCoapClientPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QCoapClient *ritual_ZNK18QCoapClientPrivate6q_funcEv(
    const QCoapClientPrivate *self) {
  return self->q_func();
}
