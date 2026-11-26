//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomappingmanager_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomappingmanager_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeomappingmanager_p.h>
#include <QtLocation/private/qgeomappingmanager_p_p.h>
#include <QtLocation/private/qgeomappingmanagerengine_p.h>
#include <QtLocation/private/qgeotiledmapreply_p.h>
#include <QtLocation/private/qgeocameracapabilities_p.h>
#include <QtLocation/private/qgeomap_p.h>
#include <QtCore/QTimer>
#include <QtCore/QLocale>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeomappingmanager.cpp, line 142, as _ZN25QGeoMappingManagerPrivateC1Ev
inline QGeoMappingManagerPrivate::QGeoMappingManagerPrivate() = default;

//  from ../qtlocation/src/location/maps/qgeomappingmanager.cpp, line 144, as _ZN25QGeoMappingManagerPrivateD1Ev
inline QGeoMappingManagerPrivate::~QGeoMappingManagerPrivate()
{
    delete engine;
}
//  -----------------------------------------------------------------------

//  QGeoMappingManagerPrivate::QGeoMappingManagerPrivate()
extern "C" Q_DECL_EXPORT
QGeoMappingManagerPrivate *ritual_ZN25QGeoMappingManagerPrivateC1Ev() {
  return new QGeoMappingManagerPrivate();
}

//  QGeoMappingManagerPrivate::~QGeoMappingManagerPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoMappingManagerPrivateD1Ev(
    QGeoMappingManagerPrivate *self) {
  delete self;
}
