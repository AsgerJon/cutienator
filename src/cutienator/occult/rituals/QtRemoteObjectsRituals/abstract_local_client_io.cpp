//  Written by dev_tooling.RitualGenerator from the records of QtRemoteObject
//  s/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtRemoteObjects/qtremoteobjectglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if defined(Q_OS_LINUX)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtRemoteObjects/QtRemoteObjects>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtRemoteObjects/6.12.0/QtRemoteObjects/private/qconnection_local_backend_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qconnection_local_backend_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 9, as _ZN13LocalClientIoC2EP7QObject
inline LocalClientIo::LocalClientIo(QObject *parent)
    : QtROClientIoDevice(parent)
    , m_socket(new QLocalSocket(this))
{
    connect(m_socket, &QLocalSocket::readyRead, this, &QtROClientIoDevice::readyRead);
    connect(m_socket, &QLocalSocket::errorOccurred, this, &LocalClientIo::onError);
    connect(m_socket, &QLocalSocket::stateChanged, this, &LocalClientIo::onStateChanged);
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 18, as _ZN13LocalClientIoD2Ev
inline LocalClientIo::~LocalClientIo()
{
    close();
}

//  from ../qtremoteobjects/src/remoteobjects/qconnection_local_backend.cpp, line 85, as _ZN13LocalClientIo14onStateChangedEN12QLocalSocket16LocalSocketStateE
inline void LocalClientIo::onStateChanged(QLocalSocket::LocalSocketState state)
{
    if (state == QLocalSocket::ClosingState && !isClosing()) {
        m_socket->abort();
        emit shouldReconnect(this);
    }
    if (state == QLocalSocket::ConnectedState)
        initializeDataStream();
}
//  -----------------------------------------------------------------------

#endif  // defined(Q_OS_LINUX)
