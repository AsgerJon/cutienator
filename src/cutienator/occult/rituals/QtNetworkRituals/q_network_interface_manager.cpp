//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if !defined(QT_NO_NETWORKINTERFACE)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qnetworkinterface_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QSharedDataPointer>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkinterface.h>
#include <QtNetwork/private/qnetworkinterface_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/kernel/qnetworkinterface.cpp, line 17, as local:qnetworkinterface.cpp:postProcess
#if !defined(QT_NO_NETWORKINTERFACE)
inline QT_IMPL_METATYPE_EXTERN(QNetworkAddressEntry)
QT_IMPL_METATYPE_EXTERN(QNetworkInterface)

static QList<QNetworkInterfacePrivate *> postProcess(QList<QNetworkInterfacePrivate *> list)
{
    // Some platforms report a netmask but don't report a broadcast address
    // Go through all available addresses and calculate the broadcast address
    // from the IP and the netmask
    //
    // This is an IPv4-only thing -- IPv6 has no concept of broadcasts
    // The math is:
    //    broadcast = IP | ~netmask

    for (QNetworkInterfacePrivate *iface : list) {
        for (QNetworkAddressEntry &address : iface->addressEntries) {
            if (address.ip().protocol() != QAbstractSocket::IPv4Protocol)
                continue;

            if (!address.netmask().isNull() && address.broadcast().isNull()) {
                QHostAddress bcast = address.ip();
                bcast = QHostAddress(bcast.toIPv4Address() | ~address.netmask().toIPv4Address());
                address.setBroadcast(bcast);
            }
        }
    }

    return list;
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)

//  from src/network/kernel/qnetworkinterface.cpp, line 48, as _ZN24QNetworkInterfaceManagerC1Ev
#if !defined(QT_NO_NETWORKINTERFACE)
inline QNetworkInterfaceManager::QNetworkInterfaceManager()
{
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)

//  from src/network/kernel/qnetworkinterface.cpp, line 52, as _ZN24QNetworkInterfaceManagerD1Ev
#if !defined(QT_NO_NETWORKINTERFACE)
inline QNetworkInterfaceManager::~QNetworkInterfaceManager()
{
}
#endif  // !defined(QT_NO_NETWORKINTERFACE)
//  -----------------------------------------------------------------------

//  QNetworkInterfaceManager::QNetworkInterfaceManager()
extern "C" Q_DECL_EXPORT
QNetworkInterfaceManager *ritual_ZN24QNetworkInterfaceManagerC1Ev() {
  return new QNetworkInterfaceManager();
}

//  QNetworkInterfaceManager::~QNetworkInterfaceManager()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QNetworkInterfaceManagerD1Ev(
    QNetworkInterfaceManager *self) {
  delete self;
}

//  a QSharedDataPointer<QNetworkInterfacePrivate> a ritual of
//      QNetworkInterfaceManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkInterfaceManager__QSharedDataPointer_QNetworkInterfacePrivate(
    QSharedDataPointer<QNetworkInterfacePrivate> *self) {
  delete self;
}

//  a QList<QSharedDataPointer<QNetworkInterfacePrivate>> a ritual of
//      QNetworkInterfaceManager gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QNetworkInterfaceManager__QList_QSharedDataPointer_QNetworkInterfacePrivate(
    QList<QSharedDataPointer<QNetworkInterfacePrivate>> *self) {
  delete self;
}

#endif  // !defined(QT_NO_NETWORKINTERFACE)
