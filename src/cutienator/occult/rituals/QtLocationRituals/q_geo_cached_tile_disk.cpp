//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeofiletilecache_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeofiletilecache_p.h>
#include <QtLocation/private/qgeotilespec_p.h>
#include <QtLocation/private/qgeomappingmanager_p.h>
#include <QtCore/QDir>
#include <QtCore/QStandardPaths>
#include <QtCore/QMetaType>
#include <QtGui/QPixmap>
#include <QtCore/QDebug>
#include <QtCore/qsavefile.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeofiletilecache.cpp, line 51, as _ZN18QGeoCachedTileDiskD1Ev
inline QGeoCachedTileDisk::~QGeoCachedTileDisk()
{
    if (cache)
        cache->evictFromDiskCache(this);
}
//  -----------------------------------------------------------------------

//  QGeoCachedTileDisk::~QGeoCachedTileDisk()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QGeoCachedTileDiskD1Ev(QGeoCachedTileDisk *self) {
  delete self;
}
