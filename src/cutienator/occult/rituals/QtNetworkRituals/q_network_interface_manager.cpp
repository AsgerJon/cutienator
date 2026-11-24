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
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qnetworkinterface.h>
#include <QtNetwork/private/qnetworkinterface_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qtools_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

#endif  // !defined(QT_NO_NETWORKINTERFACE)
