//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeopositioninfo_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeopositioninfo_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeopositioninfo.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeopositioninfo.h"
#include "private/qgeopositioninfo_p.h"
#include <QHash>
#include <QDebug>
#include <QDataStream>
#include <QtCore/QtNumeric>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeopositioninfo.cpp, line 402, as _ZN23QGeoPositionInfoPrivate3getERK16QGeoPositionInfo
inline QGeoPositionInfoPrivate *QGeoPositionInfoPrivate::get(const QGeoPositionInfo &info)
{
    return info.d.data();
}
//  -----------------------------------------------------------------------

//  QGeoPositionInfoPrivate::~QGeoPositionInfoPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QGeoPositionInfoPrivateD1Ev(QGeoPositionInfoPrivate *self) {
  delete self;
}

//  QGeoPositionInfoPrivate *QGeoPositionInfoPrivate::get(const
//      QGeoPositionInfo &info)
extern "C" Q_DECL_EXPORT
QGeoPositionInfoPrivate *ritual_ZN23QGeoPositionInfoPrivate3getERK16QGeoPositionInfo(
    const QGeoPositionInfo *info) {
  return QGeoPositionInfoPrivate::get(*info);
}
