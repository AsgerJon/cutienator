//  Written by dev_tooling.RitualGenerator from the records of
//  QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponse_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtHttpServer/QtHttpServer>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/6.12.0/QtHttpServer/private/qhttpserverresponse_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/QHttpServerResponse>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtHttpServer/qhttpserverresponse.h>
#include <QtHttpServer/private/qhttpserverliterals_p.h>
#include <QtHttpServer/private/qhttpserverresponse_p.h>
#include <QtHttpServer/private/qhttpserverresponder_p.h>
#include <QtCore/qfile.h>
#include <QtCore/qjsondocument.h>
#include <QtCore/qjsonobject.h>
#include <QtCore/qmimedatabase.h>
#include <QtNetwork/qtcpsocket.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qthttpserver/src/httpserver/qhttpserverresponse.cpp, line 36, as _ZN26QHttpServerResponsePrivateC1EO10QByteArrayN20QHttpServerResponder10StatusCodeE
inline QHttpServerResponsePrivate::QHttpServerResponsePrivate(
        QByteArray &&d, const QHttpServerResponse::StatusCode sc)
    : data(std::move(d)),
      statusCode(sc)
{ }

//  from ../qthttpserver/src/httpserver/qhttpserverresponse.cpp, line 45, as _ZN26QHttpServerResponsePrivateC1EN20QHttpServerResponder10StatusCodeE
inline QHttpServerResponsePrivate::QHttpServerResponsePrivate(const QHttpServerResponse::StatusCode sc)
    : statusCode(sc)
{ }
//  -----------------------------------------------------------------------

//  QHttpServerResponsePrivate::QHttpServerResponsePrivate(QByteArray &&d,
//      const QHttpServerResponse::StatusCode sc)
extern "C" Q_DECL_EXPORT
QHttpServerResponsePrivate *ritual_ZN26QHttpServerResponsePrivateC1EO10QByteArrayN20QHttpServerResponder10StatusCodeE(
    QByteArray *d,
    const QHttpServerResponse::StatusCode *sc) {
  return new QHttpServerResponsePrivate(std::move(*d), *sc);
}

//  QHttpServerResponsePrivate::QHttpServerResponsePrivate(const
//      QHttpServerResponse::StatusCode sc)
extern "C" Q_DECL_EXPORT
QHttpServerResponsePrivate *ritual_ZN26QHttpServerResponsePrivateC1EN20QHttpServerResponder10StatusCodeE(
    const QHttpServerResponse::StatusCode *sc) {
  return new QHttpServerResponsePrivate(*sc);
}

//  QHttpServerResponsePrivate::~QHttpServerResponsePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN26QHttpServerResponsePrivateD1Ev(
    QHttpServerResponsePrivate *self) {
  delete self;
}
