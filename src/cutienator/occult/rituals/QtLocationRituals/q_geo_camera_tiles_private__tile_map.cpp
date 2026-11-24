//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeocameratiles_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeocameratiles_p.h>
#include <QtLocation/private/qgeocameratiles_p_p.h>
#include <QtLocation/private/qgeocameradata_p.h>
#include <QtLocation/private/qgeotilespec_p.h>
#include <QtLocation/private/qgeomaptype_p.h>
#include <QtGui/QMatrix4x4>
#include <QtCore/QList>
#include <QtCore/QMap>
#include <QtCore/QPair>
#include <QtCore/QSet>
#include <QtCore/QSize>
#include <QtPositioning/private/qwebmercator_p.h>
#include <QtPositioning/private/qdoublevector2d_p.h>
#include <QtPositioning/private/qdoublevector3d_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <cmath>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeocameratiles.cpp, line 810, as _ZN22QGeoCameraTilesPrivate7TileMap3addEii
inline void QGeoCameraTilesPrivate::TileMap::add(int tileX, int tileY)
{
    if (data.contains(tileY)) {
        int oldMinX = data.value(tileY).first;
        int oldMaxX = data.value(tileY).second;
        data.insert(tileY, QPair<int, int>(qMin(tileX, oldMinX), qMax(tileX, oldMaxX)));
    } else {
        data.insert(tileY, QPair<int, int>(tileX, tileX));
    }
}
//  -----------------------------------------------------------------------

//  void QGeoCameraTilesPrivate::TileMap::add(int tileX, int tileY)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivate7TileMap3addEii(
    QGeoCameraTilesPrivate::TileMap *self,
    int tileX,
    int tileY) {
  self->add(tileX, tileY);
}

//  QGeoCameraTilesPrivate::TileMap::~TileMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGeoCameraTilesPrivate7TileMapD1Ev(
    QGeoCameraTilesPrivate::TileMap *self) {
  delete self;
}
