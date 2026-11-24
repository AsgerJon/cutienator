//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeosatelliteinfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeosatelliteinfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeosatelliteinfo.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeosatelliteinfo.h"
#include "private/qgeosatelliteinfo_p.h"
#include <QHash>
#include <QDebug>
#include <QDataStream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeosatelliteinfo.cpp, line 397, as _ZN24QGeoSatelliteInfoPrivate3getERK17QGeoSatelliteInfo
inline QGeoSatelliteInfoPrivate *QGeoSatelliteInfoPrivate::get(const QGeoSatelliteInfo &info)
{
    return info.d.data();
}
//  -----------------------------------------------------------------------

//  QGeoSatelliteInfoPrivate::~QGeoSatelliteInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QGeoSatelliteInfoPrivateD1Ev(
    QGeoSatelliteInfoPrivate *self) {
  delete self;
}

//  QGeoSatelliteInfoPrivate *QGeoSatelliteInfoPrivate::get(const
//      QGeoSatelliteInfo &info)
extern "C" Q_DECL_EXPORT
QGeoSatelliteInfoPrivate *ritual_ZN24QGeoSatelliteInfoPrivate3getERK17QGeoSatelliteInfo(
    const QGeoSatelliteInfo *info) {
  return QGeoSatelliteInfoPrivate::get(*info);
}
