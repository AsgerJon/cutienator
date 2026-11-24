//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qgeoprojection_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeoprojection_p.h"
#include <QSize>
#include <QtGui/QMatrix4x4>
#include <QtPositioning/QGeoPolygon>
#include <QtPositioning/QGeoRectangle>
#include <QtPositioning/private/qwebmercator_p.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtPositioning/private/qclipperutils_p.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 825, as _ZN25QGeoProjectionWebMercator6Line2DC1Ev
inline QGeoProjectionWebMercator::Line2D::Line2D()
{

}

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 830, as _ZN25QGeoProjectionWebMercator6Line2DC1ERK15QDoubleVector2DS3_
inline QGeoProjectionWebMercator::Line2D::Line2D(const QDoubleVector2D &linePoint, const QDoubleVector2D &lineDirection)
    :   m_point(linePoint), m_direction(lineDirection.normalized())
{

}

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 836, as _ZNK25QGeoProjectionWebMercator6Line2D7isValidEv
inline bool QGeoProjectionWebMercator::Line2D::isValid() const
{
    return (m_direction.length() > 0.5);
}
//  -----------------------------------------------------------------------

//  QGeoProjectionWebMercator::Line2D::Line2D()
extern "C" Q_DECL_EXPORT
QGeoProjectionWebMercator::Line2D *ritual_ZN25QGeoProjectionWebMercator6Line2DC1Ev() {
  return new QGeoProjectionWebMercator::Line2D();
}

//  QGeoProjectionWebMercator::Line2D::Line2D(const QDoubleVector2D
//      &linePoint, const QDoubleVector2D &lineDirection)
extern "C" Q_DECL_EXPORT
QGeoProjectionWebMercator::Line2D *ritual_ZN25QGeoProjectionWebMercator6Line2DC1ERK15QDoubleVector2DS3_(
    const QDoubleVector2D *linePoint,
    const QDoubleVector2D *lineDirection) {
  return new QGeoProjectionWebMercator::Line2D(*linePoint, *lineDirection);
}

//  bool QGeoProjectionWebMercator::Line2D::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QGeoProjectionWebMercator6Line2D7isValidEv(
    const QGeoProjectionWebMercator::Line2D *self) {
  return self->isValid();
}

//  QGeoProjectionWebMercator::Line2D::~Line2D()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator6Line2DD1Ev(
    QGeoProjectionWebMercator::Line2D *self) {
  delete self;
}
