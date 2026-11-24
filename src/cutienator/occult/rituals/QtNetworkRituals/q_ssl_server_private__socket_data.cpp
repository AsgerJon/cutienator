//  Written by dev_tooling.RitualGenerator from the records of
//  QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtNetwork/6.12.0/QtNetwork/private/qtnetworkglobal_p.h>
#include <QtNetwork/QtNetwork>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtNetwork/6.12.0/QtNetwork/private/qsslserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

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
