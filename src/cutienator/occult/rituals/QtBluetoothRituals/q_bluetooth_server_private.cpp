//  Written by dev_tooling.RitualGenerator from the records of
//  QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothserver_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtBluetooth/6.12.0/QtBluetooth/private/qtbluetoothglobal_p.h>
#include <QtBluetooth/qbluetoothserver.h>
#include <QtBluetooth/QtBluetooth>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtBluetooth/6.12.0/QtBluetooth/private/qbluetoothserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qbluetoothsocket.h"
#include "qbluetoothsocket_bluez_p.h"
#include "qbluetoothdeviceinfo.h"
#include <QtBluetooth/QBluetoothLocalDevice>
#include <qplatformdefs.h>
#include <QtCore/private/qcore_unix_p.h>
#include <QtCore/QLoggingCategory>
#include <errno.h>
#include <unistd.h>
#include <string.h>
#include <QtCore/QSocketNotifier>
#include "qbluetoothsocketbase_p.h"
#include "qbluetoothserver.h"
#include "qbluetoothserver_p.h"
#include "qbluetoothsocket.h"
#include "qbluetoothsocket_bluez_p.h"
#include "qbluetoothlocaldevice.h"
#include <QtCore/QLoggingCategory>
#include <QtCore/QSocketNotifier>
#include <errno.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocket_bluez.cpp, line 29, as _ZN28QBluetoothSocketPrivateBluezC1Ev
inline QBluetoothSocketPrivateBluez::QBluetoothSocketPrivateBluez()
    : QBluetoothSocketBasePrivate()
{
    secFlags = QBluetooth::Security::Authorization;
}

//  from ../qtconnectivity/src/bluetooth/qbluetoothsocketbase.cpp, line 8, as _ZN27QBluetoothSocketBasePrivateC2EP7QObject
inline QBluetoothSocketBasePrivate::QBluetoothSocketBasePrivate(QObject *parent) : QObject(parent)
{

}

//  from ../qtconnectivity/src/bluetooth/qbluetoothserver_bluez.cpp, line 52, as _ZN23QBluetoothServerPrivate16_q_newConnectionEv
inline void QBluetoothServerPrivate::_q_newConnection()
{
    // disable socket notifier until application calls nextPendingConnection().
    socketNotifier->setEnabled(false);

    emit q_ptr->newConnection();
}
//  -----------------------------------------------------------------------

//  QBluetoothServer *QBluetoothServerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QBluetoothServer *ritual_ZN23QBluetoothServerPrivate6q_funcEv(
    QBluetoothServerPrivate *self) {
  return self->q_func();
}

//  const QBluetoothServer *QBluetoothServerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QBluetoothServer *ritual_ZNK23QBluetoothServerPrivate6q_funcEv(
    const QBluetoothServerPrivate *self) {
  return self->q_func();
}

#if QT_CONFIG(bluez)
//  void QBluetoothServerPrivate::_q_newConnection()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QBluetoothServerPrivate16_q_newConnectionEv(
    QBluetoothServerPrivate *self) {
  self->_q_newConnection();
}
#endif  // QT_CONFIG(bluez)
