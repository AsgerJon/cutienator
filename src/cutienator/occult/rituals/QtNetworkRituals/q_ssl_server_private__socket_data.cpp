//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/qtnetworkglobal.h>
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#if QT_CONFIG(ssl)
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qobjectdefs.h>

//  QSslServerPrivate::SocketData::SocketData(QMetaObject::Connection
//      readyRead, QMetaObject::Connection destroyed, std::shared_ptr<QTimer>
//      &&timer)
extern "C" Q_DECL_EXPORT
QSslServerPrivate::SocketData *ritual_ZN17QSslServerPrivate10SocketDataC1EN11QMetaObject10ConnectionES2_OSt10shared_ptrI6QTimerE(
    const QMetaObject::Connection *readyRead,
    const QMetaObject::Connection *destroyed,
    std::shared_ptr<QTimer> *timer) {
  return new QSslServerPrivate::SocketData(
      *readyRead,
      *destroyed,
      std::move(*timer));
}

//  void QSslServerPrivate::SocketData::disconnectSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate10SocketData17disconnectSignalsEv(
    QSslServerPrivate::SocketData *self) {
  self->disconnectSignals();
}

//  QSslServerPrivate::SocketData::~SocketData()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSslServerPrivate10SocketDataD1Ev(
    QSslServerPrivate::SocketData *self) {
  delete self;
}

#endif  // QT_CONFIG(ssl)
