//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qabstractsocketengine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qabstractsocketengine_p.h>
#include <QtNetwork/private/qnativesocketengine_p.h>
#include <QtCore/qmutex.h>
#include <QtNetwork/qnetworkproxy.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/socket/qabstractsocketengine.cpp, line 40, as _ZN28QAbstractSocketEnginePrivateC1Ev
inline QAbstractSocketEnginePrivate::QAbstractSocketEnginePrivate()
    : socketError(QAbstractSocket::UnknownSocketError)
    , hasSetSocketError(false)
    , socketErrorString(QLatin1StringView(QT_TRANSLATE_NOOP(QSocketLayer, "Unknown error")))
    , socketState(QAbstractSocket::UnconnectedState)
    , socketType(QAbstractSocket::UnknownSocketType)
    , socketProtocol(QAbstractSocket::UnknownNetworkLayerProtocol)
    , localPort(0)
    , peerPort(0)
    , inboundStreamCount(0)
    , outboundStreamCount(0)
    , receiver(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QAbstractSocketEngine *QAbstractSocketEnginePrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractSocketEngine *ritual_ZN28QAbstractSocketEnginePrivate6q_funcEv(
    QAbstractSocketEnginePrivate *self) {
  return self->q_func();
}

//  const QAbstractSocketEngine *QAbstractSocketEnginePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractSocketEngine *ritual_ZNK28QAbstractSocketEnginePrivate6q_funcEv(
    const QAbstractSocketEnginePrivate *self) {
  return self->q_func();
}

//  QAbstractSocketEnginePrivate::QAbstractSocketEnginePrivate()
extern "C" Q_DECL_EXPORT
QAbstractSocketEnginePrivate *ritual_ZN28QAbstractSocketEnginePrivateC1Ev() {
  return new QAbstractSocketEnginePrivate();
}
