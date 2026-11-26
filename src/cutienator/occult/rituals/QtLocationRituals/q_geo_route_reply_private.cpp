//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoroutereply_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoroutereply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeorouterequest.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/qgeoroutereply.h>
#include <QtLocation/private/qgeoroutereply_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeoroutereply.cpp, line 233, as _ZN21QGeoRouteReplyPrivateC1ERK16QGeoRouteRequest
inline QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(const QGeoRouteRequest &request)
    : request(request)
{}

//  from ../qtlocation/src/location/maps/qgeoroutereply.cpp, line 237, as _ZN21QGeoRouteReplyPrivateC1EN14QGeoRouteReply5ErrorE7QString
inline QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(QGeoRouteReply::Error error, QString errorString)
    : error(error),
      errorString(errorString),
      isFinished(true)
{}
//  -----------------------------------------------------------------------

//  QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(const QGeoRouteRequest
//      &request)
extern "C" Q_DECL_EXPORT
QGeoRouteReplyPrivate *ritual_ZN21QGeoRouteReplyPrivateC1ERK16QGeoRouteRequest(
    const QGeoRouteRequest *request) {
  return new QGeoRouteReplyPrivate(*request);
}

//  QGeoRouteReplyPrivate::QGeoRouteReplyPrivate(QGeoRouteReply::Error error,
//      QString errorString)
extern "C" Q_DECL_EXPORT
QGeoRouteReplyPrivate *ritual_ZN21QGeoRouteReplyPrivateC1EN14QGeoRouteReply5ErrorE7QString(
    QGeoRouteReply::Error error,
    const QString *errorString) {
  return new QGeoRouteReplyPrivate(error, *errorString);
}
