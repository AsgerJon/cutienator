//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 1 rituals whose code, copied from
//  Qt's source, reads constant data Qt keeps to itself
//  ('QSslConfigurationPrivate::defaultSslOptions'), copied with it 'inline'
//  from Qt's source, drafted by a copy of the generator that takes it along.
//  Kept as it is when the generator runs again.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslconfiguration_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/qsslconfiguration.h>

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/network/ssl/qsslconfiguration.cpp, line 18, as _ZN24QSslConfigurationPrivate17defaultSslOptionsE
inline const QSsl::SslOptions QSslConfigurationPrivate::defaultSslOptions = QSsl::SslOptionDisableEmptyFragments
                                                                    |QSsl::SslOptionDisableLegacyRenegotiation
                                                                    |QSsl::SslOptionDisableCompression
                                                                    |QSsl::SslOptionDisableSessionPersistence;

//  from src/network/ssl/qsslconfiguration.cpp, line 1412, as _ZN24QSslConfigurationPrivate20peerSessionWasSharedERK17QSslConfiguration
inline bool QSslConfigurationPrivate::peerSessionWasShared(const QSslConfiguration &configuration) {
        return configuration.d->peerSessionShared;
    }
//  -----------------------------------------------------------------------

//  QSslConfigurationPrivate::QSslConfigurationPrivate()
extern "C" Q_DECL_EXPORT
QSslConfigurationPrivate *ritual_ZN24QSslConfigurationPrivateC1Ev() {
  return new QSslConfigurationPrivate();
}

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
