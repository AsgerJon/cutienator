//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/qhttpserverwebsocketupgraderesponse.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/qhttpserverwebsocketupgraderesponse.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qhttpserverwebsocketupgraderesponse.h>
#include <QtCore/QString>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverwebsocketupgraderesponse.cpp, line 52, as _ZN35QHttpServerWebSocketUpgradeResponseC1ENS_12ResponseTypeEi10QByteArray
inline QHttpServerWebSocketUpgradeResponse::QHttpServerWebSocketUpgradeResponse(ResponseType type,
                                                                         int status,
                                                                         QByteArray message)
    : responseType(type), errorStatus(status), errorMessage(message), reserved(nullptr)
{
}
//  -----------------------------------------------------------------------

//  QHttpServerWebSocketUpgradeResponse::QHttpServerWebSocketUpgradeResponse(
//      const QHttpServerWebSocketUpgradeResponse &other)
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponseC1ERKS_(
    const QHttpServerWebSocketUpgradeResponse *other) {
  return new QHttpServerWebSocketUpgradeResponse(*other);
}

//  QHttpServerWebSocketUpgradeResponse::~QHttpServerWebSocketUpgradeResponse
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QHttpServerWebSocketUpgradeResponseD1Ev(
    QHttpServerWebSocketUpgradeResponse *self) {
  delete self;
}

//  ResponseType QHttpServerWebSocketUpgradeResponse::type() const
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse::ResponseType ritual_ZNK35QHttpServerWebSocketUpgradeResponse4typeEv(
    const QHttpServerWebSocketUpgradeResponse *self) {
  return self->type();
}

//  int QHttpServerWebSocketUpgradeResponse::denyStatus() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK35QHttpServerWebSocketUpgradeResponse10denyStatusEv(
    const QHttpServerWebSocketUpgradeResponse *self) {
  return self->denyStatus();
}

//  const QByteArray &QHttpServerWebSocketUpgradeResponse::denyMessage()
//      const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNKR35QHttpServerWebSocketUpgradeResponse11denyMessageEv(
    const QHttpServerWebSocketUpgradeResponse *self) {
  return new QByteArray(self->denyMessage());
}

//  QHttpServerWebSocketUpgradeResponse
//      QHttpServerWebSocketUpgradeResponse::accept()
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponse6acceptEv() {
  return new QHttpServerWebSocketUpgradeResponse(
      QHttpServerWebSocketUpgradeResponse::accept());
}

//  QHttpServerWebSocketUpgradeResponse
//      QHttpServerWebSocketUpgradeResponse::deny()
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponse4denyEv() {
  return new QHttpServerWebSocketUpgradeResponse(
      QHttpServerWebSocketUpgradeResponse::deny());
}

//  QHttpServerWebSocketUpgradeResponse
//      QHttpServerWebSocketUpgradeResponse::deny(int status, QByteArray
//      message)
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponse4denyEi10QByteArray(
    int status,
    const QByteArray *message) {
  return new QHttpServerWebSocketUpgradeResponse(
      QHttpServerWebSocketUpgradeResponse::deny(
          status,
          *message));
}

//  QHttpServerWebSocketUpgradeResponse
//      QHttpServerWebSocketUpgradeResponse::passToNext()
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponse10passToNextEv() {
  return new QHttpServerWebSocketUpgradeResponse(
      QHttpServerWebSocketUpgradeResponse::passToNext());
}

//  QHttpServerWebSocketUpgradeResponse::QHttpServerWebSocketUpgradeResponse(
//      ResponseType type, int status, QByteArray message)
extern "C" Q_DECL_EXPORT
QHttpServerWebSocketUpgradeResponse *ritual_ZN35QHttpServerWebSocketUpgradeResponseC1ENS_12ResponseTypeEi10QByteArray(
    QHttpServerWebSocketUpgradeResponse::ResponseType type,
    int status,
    const QByteArray *message) {
  return new QHttpServerWebSocketUpgradeResponse(type, status, *message);
}
