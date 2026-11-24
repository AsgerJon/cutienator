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
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector3d_p.h>
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

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 847, as _ZN25QGeoProjectionWebMercator5PlaneC1Ev
inline QGeoProjectionWebMercator::Plane::Plane()
{

}

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 855, as _ZNK25QGeoProjectionWebMercator5Plane16lineIntersectionERK15QDoubleVector3DS3_
inline QDoubleVector3D QGeoProjectionWebMercator::Plane::lineIntersection(const QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection) const
{
    double s;
    return lineIntersection(linePoint, lineDirection, s);
}

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 861, as _ZNK25QGeoProjectionWebMercator5Plane16lineIntersectionERK15QDoubleVector3DS3_Rd
inline QDoubleVector3D QGeoProjectionWebMercator::Plane::lineIntersection(const QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection, double &s) const
{
    QDoubleVector3D w = linePoint - m_point;
    // s = -n.dot(w) / n.dot(u).  p = p0 + su; u is lineDirection
    s = QDoubleVector3D::dotProduct(-m_normal, w) / QDoubleVector3D::dotProduct(m_normal, lineDirection);
    return linePoint + lineDirection * s;
}

//  from ../qtlocation/src/location/maps/qgeoprojection.cpp, line 883, as _ZNK25QGeoProjectionWebMercator5Plane7isValidEv
inline bool QGeoProjectionWebMercator::Plane::isValid() const
{
    return (m_normal.length() > 0.5);
}
//  -----------------------------------------------------------------------

//  QGeoProjectionWebMercator::Plane::Plane()
extern "C" Q_DECL_EXPORT
QGeoProjectionWebMercator::Plane *ritual_ZN25QGeoProjectionWebMercator5PlaneC1Ev() {
  return new QGeoProjectionWebMercator::Plane();
}

//  QDoubleVector3D QGeoProjectionWebMercator::Plane::lineIntersection(const
//      QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection)
//      const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK25QGeoProjectionWebMercator5Plane16lineIntersectionERK15QDoubleVector3DS3_(
    const QGeoProjectionWebMercator::Plane *self,
    const QDoubleVector3D *linePoint,
    const QDoubleVector3D *lineDirection) {
  return new QDoubleVector3D(
      self->lineIntersection(
          *linePoint,
          *lineDirection));
}

//  QDoubleVector3D QGeoProjectionWebMercator::Plane::lineIntersection(const
//      QDoubleVector3D &linePoint, const QDoubleVector3D &lineDirection,
//      double &s) const
extern "C" Q_DECL_EXPORT
QDoubleVector3D *ritual_ZNK25QGeoProjectionWebMercator5Plane16lineIntersectionERK15QDoubleVector3DS3_Rd(
    const QGeoProjectionWebMercator::Plane *self,
    const QDoubleVector3D *linePoint,
    const QDoubleVector3D *lineDirection,
    double *s) {
  return new QDoubleVector3D(
      self->lineIntersection(
          *linePoint,
          *lineDirection,
          *s));
}

//  bool QGeoProjectionWebMercator::Plane::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QGeoProjectionWebMercator5Plane7isValidEv(
    const QGeoProjectionWebMercator::Plane *self) {
  return self->isValid();
}

//  QGeoProjectionWebMercator::Plane::~Plane()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QGeoProjectionWebMercator5PlaneD1Ev(
    QGeoProjectionWebMercator::Plane *self) {
  delete self;
}
