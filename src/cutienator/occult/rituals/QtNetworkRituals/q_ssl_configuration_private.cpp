//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/private/qssl_p.h>
#include <QtNetwork/qsslconfiguration.h>
#include <QtNetwork/private/qsslconfiguration_p.h>
#include <QtNetwork/qsslsocket.h>
#include <QtNetwork/private/qsslsocket_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qsslconfiguration.cpp, line 1412, as _ZN24QSslConfigurationPrivate20peerSessionWasSharedERK17QSslConfiguration
inline bool QSslConfigurationPrivate::peerSessionWasShared(const QSslConfiguration &configuration) {
        return configuration.d->peerSessionShared;
    }
//  -----------------------------------------------------------------------

//  bool QSslConfigurationPrivate::peerSessionWasShared(const
//      QSslConfiguration &configuration)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QSslConfigurationPrivate20peerSessionWasSharedERK17QSslConfiguration(
    const QSslConfiguration *configuration) {
  return QSslConfigurationPrivate::peerSessionWasShared(*configuration);
}

//  QSslConfigurationPrivate::~QSslConfigurationPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSslConfigurationPrivateD1Ev(
    QSslConfigurationPrivate *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
