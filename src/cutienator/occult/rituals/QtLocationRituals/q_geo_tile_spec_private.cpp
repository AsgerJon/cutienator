//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeotilespec_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeotilespec_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeotilespec_p.h>
#include <QtLocation/private/qgeotilespec_p_p.h>
#include <QtCore/QDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeotilespec.cpp, line 113, as _ZNK19QGeoTileSpecPrivateltERKS_
inline bool QGeoTileSpecPrivate::operator<(const QGeoTileSpecPrivate &rhs) const
{
    if (plugin_ < rhs.plugin_)
        return true;
    if (plugin_ > rhs.plugin_)
        return false;

    if (mapId_ < rhs.mapId_)
        return true;
    if (mapId_ > rhs.mapId_)
        return false;

    if (zoom_ < rhs.zoom_)
        return true;
    if (zoom_ > rhs.zoom_)
        return false;

    if (x_ < rhs.x_)
        return true;
    if (x_ > rhs.x_)
        return false;

    if (y_ < rhs.y_)
        return true;
    if (y_ > rhs.y_)
        return false;

    return (version_ < rhs.version_);
}
//  -----------------------------------------------------------------------

//  QGeoTileSpecPrivate::QGeoTileSpecPrivate(const QString &plugin, int
//      mapId, int zoom, int x, int y, int version)
extern "C" Q_DECL_EXPORT
QGeoTileSpecPrivate *ritual_ZN19QGeoTileSpecPrivateC1ERK7QStringiiiii(
    const QString *plugin,
    int mapId,
    int zoom,
    int x,
    int y,
    int version) {
  return new QGeoTileSpecPrivate(*plugin, mapId, zoom, x, y, version);
}

//  size_t QGeoTileSpecPrivate::hash(size_t seed) const
extern "C" Q_DECL_EXPORT
size_t ritual_ZNK19QGeoTileSpecPrivate4hashEm(
    const QGeoTileSpecPrivate *self,
    size_t seed) {
  return self->hash(seed);
}

//  bool QGeoTileSpecPrivate::operator==(const QGeoTileSpecPrivate &rhs)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoTileSpecPrivateeqERKS_(
    const QGeoTileSpecPrivate *self,
    const QGeoTileSpecPrivate *rhs) {
  return self->operator==(*rhs);
}

//  bool QGeoTileSpecPrivate::operator<(const QGeoTileSpecPrivate &rhs) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QGeoTileSpecPrivateltERKS_(
    const QGeoTileSpecPrivate *self,
    const QGeoTileSpecPrivate *rhs) {
  return self->operator<(*rhs);
}

//  QGeoTileSpecPrivate::~QGeoTileSpecPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QGeoTileSpecPrivateD1Ev(QGeoTileSpecPrivate *self) {
  delete self;
}
