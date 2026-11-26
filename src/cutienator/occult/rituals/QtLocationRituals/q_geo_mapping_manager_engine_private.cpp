//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeomappingmanagerengine_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeomappingmanagerengine_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/private/qgeomappingmanagerengine_p.h>
#include <QtLocation/private/qgeomappingmanagerengine_p_p.h>
#include <QtLocation/private/qgeotiledmapreply_p.h>
#include <QtLocation/private/qgeotilespec_p.h>
#include <QtLocation/private/qgeocameracapabilities_p.h>
#include <QtLocation/private/qgeomaptype_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeomappingmanagerengine.cpp, line 180, as _ZN31QGeoMappingManagerEnginePrivateC1Ev
inline QGeoMappingManagerEnginePrivate::QGeoMappingManagerEnginePrivate() = default;

//  from ../qtlocation/src/location/maps/qgeomappingmanagerengine.cpp, line 181, as _ZN31QGeoMappingManagerEnginePrivateD1Ev
inline QGeoMappingManagerEnginePrivate::~QGeoMappingManagerEnginePrivate() = default;
//  -----------------------------------------------------------------------

//  QGeoMappingManagerEnginePrivate::QGeoMappingManagerEnginePrivate()
extern "C" Q_DECL_EXPORT
QGeoMappingManagerEnginePrivate *ritual_ZN31QGeoMappingManagerEnginePrivateC1Ev() {
  return new QGeoMappingManagerEnginePrivate();
}

//  QGeoMappingManagerEnginePrivate::~QGeoMappingManagerEnginePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QGeoMappingManagerEnginePrivateD1Ev(
    QGeoMappingManagerEnginePrivate *self) {
  delete self;
}
