//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotiledmapreply_p_p.h>
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeotiledmapreply_p.h>
#include <QtLocation/private/qgeotiledmapreply_p_p.h>
#include <QtCore/qdebug.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeotiledmapreply.cpp, line 249, as _ZN24QGeoTiledMapReplyPrivateC1ERK12QGeoTileSpec
inline QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(const QGeoTileSpec &spec)
    : spec(spec)
{}

//  from ../qtlocation/src/location/maps/qgeotiledmapreply.cpp, line 253, as _ZN24QGeoTiledMapReplyPrivateC1EN17QGeoTiledMapReply5ErrorERK7QString
inline QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(QGeoTiledMapReply::Error error, const QString &errorString)
    : error(error),
      errorString(errorString),
      isFinished(true)
{}
//  -----------------------------------------------------------------------

//  QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(const QGeoTileSpec
//      &spec)
extern "C" Q_DECL_EXPORT
QGeoTiledMapReplyPrivate *ritual_ZN24QGeoTiledMapReplyPrivateC1ERK12QGeoTileSpec(
    const QGeoTileSpec *spec) {
  return new QGeoTiledMapReplyPrivate(*spec);
}

//  QGeoTiledMapReplyPrivate::QGeoTiledMapReplyPrivate(QGeoTiledMapReply::Err
//      or error, const QString &errorString)
extern "C" Q_DECL_EXPORT
QGeoTiledMapReplyPrivate *ritual_ZN24QGeoTiledMapReplyPrivateC1EN17QGeoTiledMapReply5ErrorERK7QString(
    QGeoTiledMapReply::Error error,
    const QString *errorString) {
  return new QGeoTiledMapReplyPrivate(error, *errorString);
}

//  QGeoTiledMapReplyPrivate::~QGeoTiledMapReplyPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoTiledMapReplyPrivateD1Ev(
    QGeoTiledMapReplyPrivate *self) {
  delete self;
}
