//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomaptype_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomaptype_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameracapabilities_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeomaptype_p.h"
#include "qgeomaptype_p_p.h"
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeomaptype.cpp, line 163, as _ZN18QGeoMapTypePrivateC1EN11QGeoMapType8MapStyleERK7QStringS4_bbiRK10QByteArrayRK22QGeoCameraCapabilitiesRK4QMapIS2_8QVariantE
inline QGeoMapTypePrivate::QGeoMapTypePrivate(QGeoMapType::MapStyle style, const QString &name,
                                       const QString &description, bool mobile, bool night,
                                       int mapId, const QByteArray &pluginName,
                                       const QGeoCameraCapabilities &cameraCapabilities,
                                       const QVariantMap &metadata)
:   name_(name), description_(description), pluginName_(pluginName),
    cameraCapabilities_(cameraCapabilities), metadata_(metadata),
    style_(style), mapId_(mapId), mobile_(mobile), night_(night)
{
}
//  -----------------------------------------------------------------------

//  QGeoMapTypePrivate::QGeoMapTypePrivate(QGeoMapType::MapStyle style, const
//      QString &name, const QString &description, bool mobile, bool night,
//      int mapId, const QByteArray &pluginName, const QGeoCameraCapabilities
//      &cameraCapabilities, const QVariantMap &metadata)
extern "C" Q_DECL_EXPORT
QGeoMapTypePrivate *ritual_ZN18QGeoMapTypePrivateC1EN11QGeoMapType8MapStyleERK7QStringS4_bbiRK10QByteArrayRK22QGeoCameraCapabilitiesRK4QMapIS2_8QVariantE(
    QGeoMapType::MapStyle style,
    const QString *name,
    const QString *description,
    bool mobile,
    bool night,
    int mapId,
    const QByteArray *pluginName,
    const QGeoCameraCapabilities *cameraCapabilities,
    const QMap<QString, QVariant> *metadata) {
  return new QGeoMapTypePrivate(
      style,
      *name,
      *description,
      mobile,
      night,
      mapId,
      *pluginName,
      *cameraCapabilities,
      *metadata);
}

//  QGeoMapTypePrivate::~QGeoMapTypePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoMapTypePrivateD1Ev(QGeoMapTypePrivate *self) {
  delete self;
}
