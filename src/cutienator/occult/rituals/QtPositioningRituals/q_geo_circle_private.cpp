//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/6.12.0/QtPositioning/private/qgeocircle_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qgeocircle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeorectangle.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeoshape.h"
#include "qgeoshape_p.h"
#include "qgeorectangle.h"
#include "qgeocircle.h"
#include "qgeopath.h"
#include "qgeopolygon.h"
#ifndef QT_NO_DEBUG_STREAM
#include <QtCore/QDebug>
#endif
#ifndef QT_NO_DATASTREAM
#include <QtCore/QDataStream>
#endif
#include "qgeocircle.h"
#include "qgeocircle_p.h"
#include "qgeocoordinate.h"
#include "qnumeric.h"
#include "qlocationutils_p.h"
#include "qdoublevector2d_p.h"
#include "qdoublevector3d_p.h"
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 25, as _ZN16QGeoShapePrivateC2EN9QGeoShape9ShapeTypeE
inline QGeoShapePrivate::QGeoShapePrivate(QGeoShape::ShapeType type)
:   type(type)
{
}

//  from ../qtpositioning/src/positioning/qgeoshape.cpp, line 30, as _ZN16QGeoShapePrivateD2Ev
inline QGeoShapePrivate::~QGeoShapePrivate()
{
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 129, as _ZNK17QGeoCirclePrivate7isValidEv
inline bool QGeoCirclePrivate::isValid() const
{
    return m_center.isValid() && !qIsNaN(m_radius) && m_radius >= -1e-7;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 134, as _ZNK17QGeoCirclePrivate7isEmptyEv
inline bool QGeoCirclePrivate::isEmpty() const
{
    return !isValid() || m_radius <= 1e-7;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 179, as _ZNK17QGeoCirclePrivate8containsERK14QGeoCoordinate
inline bool QGeoCirclePrivate::contains(const QGeoCoordinate &coordinate) const
{
    if (!isValid() || !coordinate.isValid())
        return false;

    // see QTBUG-41447 for details
    qreal distance = m_center.distanceTo(coordinate);
    if (distance <= m_radius || QtPrivate::fuzzyCompare(distance, m_radius))
        return true;

    return false;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 192, as _ZNK17QGeoCirclePrivate6centerEv
inline QGeoCoordinate QGeoCirclePrivate::center() const
{
    return m_center;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 197, as _ZNK17QGeoCirclePrivate20boundingGeoRectangleEv
inline QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle() const
{
    return m_bbox;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 276, as _ZNK17QGeoCirclePrivate14crossNorthPoleEv
inline bool QGeoCirclePrivate::crossNorthPole() const
{
    const QGeoCoordinate northPole(90.0, m_center.longitude());
    qreal distanceToPole = m_center.distanceTo(northPole);
    if (distanceToPole < m_radius)
        return true;
    return false;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 285, as _ZNK17QGeoCirclePrivate14crossSouthPoleEv
inline bool QGeoCirclePrivate::crossSouthPole() const
{
    const QGeoCoordinate southPole(-90.0, m_center.longitude());
    qreal distanceToPole = m_center.distanceTo(southPole);
    if (distanceToPole < m_radius)
        return true;
    return false;
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 202, as _ZN17QGeoCirclePrivate17updateBoundingBoxEv
inline void QGeoCirclePrivate::updateBoundingBox()
{
    if (isEmpty()) {
        if (m_center.isValid()) {
            m_bbox.setTopLeft(m_center);
            m_bbox.setBottomRight(m_center);
        }
        return;
    }

    bool crossNorth = crossNorthPole();
    bool crossSouth = crossSouthPole();

    if (crossNorth && crossSouth) {
        // Circle crossing both poles fills the whole map
        m_bbox = QGeoRectangle(QGeoCoordinate(90.0, -180.0), QGeoCoordinate(-90.0, 180.0));
    } else if (crossNorth) {
        // Circle crossing one pole fills the map in the longitudinal direction
        m_bbox = QGeoRectangle(QGeoCoordinate(90.0, -180.0), QGeoCoordinate(m_center.atDistanceAndAzimuth(m_radius, 180.0).latitude(), 180.0));
    } else if (crossSouth) {
        m_bbox = QGeoRectangle(QGeoCoordinate(m_center.atDistanceAndAzimuth(m_radius, 0.0).latitude(), -180.0), QGeoCoordinate(-90, 180.0));
    } else {
        // Regular circle not crossing anything

        // Calculate geo bounding box of the circle
        //
        // A circle tangential point with a meridian, together with pole and
        // the circle center create a spherical triangle.
        // Finding the tangential point with the spherical law of sines:
        //
        // * lon_delta_in_rad : delta between the circle center and a tangential
        //   point (absolute value).
        // * r_in_rad : angular radius of the circle
        // * lat_in_rad : latitude of the circle center
        // * alpha_in_rad : angle between meridian and radius of the circle.
        //   At the tangential point, sin(alpha_in_rad) == 1.
        // * lat_delta_in_rad - absolute delta of latitudes between the circle center and
        //   any of the two points where the great circle going through the circle
        //   center and the pole crosses the circle. In other words, the points
        //   on the circle with azimuth 0 or 180.
        //
        //  Using:
        //  sin(lon_delta_in_rad)/sin(r_in_rad) = sin(alpha_in_rad)/sin(pi/2 - lat_in_rad)

        double r_in_rad = m_radius / QLocationUtils::earthMeanRadius(); // angular r
        double lat_delta_in_deg = QLocationUtils::degrees(r_in_rad);
        double lon_delta_in_deg = QLocationUtils::degrees(std::asin(
               std::sin(r_in_rad) /
               std::cos(QLocationUtils::radians(m_center.latitude()))
            ));

        QGeoCoordinate topLeft;
        topLeft.setLatitude(QLocationUtils::clipLat(m_center.latitude() + lat_delta_in_deg));
        topLeft.setLongitude(QLocationUtils::wrapLong(m_center.longitude() - lon_delta_in_deg));
        QGeoCoordinate bottomRight;
        bottomRight.setLatitude(QLocationUtils::clipLat(m_center.latitude() - lat_delta_in_deg));
        bottomRight.setLongitude(QLocationUtils::wrapLong(m_center.longitude() + lon_delta_in_deg));

        m_bbox = QGeoRectangle(topLeft, bottomRight);
    }
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 264, as _ZN17QGeoCirclePrivate9setCenterERK14QGeoCoordinate
inline void QGeoCirclePrivate::setCenter(const QGeoCoordinate &c)
{
    m_center = c;
    updateBoundingBox();
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 270, as _ZN17QGeoCirclePrivate9setRadiusEd
inline void QGeoCirclePrivate::setRadius(const qreal r)
{
    m_radius = r;
    updateBoundingBox();
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 297, as _ZN17QGeoCirclePrivate12extendCircleERK14QGeoCoordinate
inline void QGeoCirclePrivate::extendCircle(const QGeoCoordinate &coordinate)
{
    if (!isValid() || !coordinate.isValid() || contains(coordinate))
        return;

    setRadius(m_center.distanceTo(coordinate));
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 412, as _ZNK17QGeoCirclePrivate5cloneEv
inline QGeoShapePrivate *QGeoCirclePrivate::clone() const
{
    return new QGeoCirclePrivate(*this);
}
//  -----------------------------------------------------------------------

//  A QGeoCirclePrivate that Python can take functions over in. Every QGeoCirclePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQGeoCirclePrivateCall0)(const void *, int *);
typedef bool (*CuteQGeoCirclePrivateCall1)(const void *, int *);
typedef bool (*CuteQGeoCirclePrivateCall2)(const void *, const QGeoCoordinate *, int *);
typedef const QGeoCoordinate * (*CuteQGeoCirclePrivateCall3)(const void *, int *);
typedef const QGeoRectangle * (*CuteQGeoCirclePrivateCall4)(const void *, int *);
typedef void * (*CuteQGeoCirclePrivateCall5)(const void *, int *);
class CuteQGeoCirclePrivate : public QGeoCirclePrivate {
public:
  using QGeoCirclePrivate::QGeoCirclePrivate;
  CuteQGeoCirclePrivate(const QGeoCirclePrivate &other) : QGeoCirclePrivate(other) {}
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isValidEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate7isEmptyEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate8containsERK14QGeoCoordinate")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate6centerEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate20boundingGeoRectangleEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QGeoShapePrivate5cloneEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  bool QGeoCirclePrivate::isValid() const
  bool isValid() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall0 call = reinterpret_cast<CuteQGeoCirclePrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoCirclePrivate::isValid();
  }

  //  bool QGeoCirclePrivate::isEmpty() const
  bool isEmpty() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall1 call = reinterpret_cast<CuteQGeoCirclePrivateCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGeoCirclePrivate::isEmpty();
  }

  //  bool QGeoCirclePrivate::contains(const QGeoCoordinate &coordinate)
  //      const
  bool contains(const QGeoCoordinate &coordinate) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall2 call = reinterpret_cast<CuteQGeoCirclePrivateCall2>(taken[2]);
      bool given = call(this, &coordinate, &handled);
      if (handled) return given;
    }
    return QGeoCirclePrivate::contains(coordinate);
  }

  //  QGeoCoordinate QGeoCirclePrivate::center() const
  QGeoCoordinate center() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall3 call = reinterpret_cast<CuteQGeoCirclePrivateCall3>(taken[3]);
      const QGeoCoordinate * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoCirclePrivate::center();
  }

  //  QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle() const
  QGeoRectangle boundingGeoRectangle() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall4 call = reinterpret_cast<CuteQGeoCirclePrivateCall4>(taken[4]);
      const QGeoRectangle * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QGeoCirclePrivate::boundingGeoRectangle();
  }

  //  QGeoShapePrivate *QGeoCirclePrivate::clone() const
  QGeoShapePrivate *clone() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGeoCirclePrivateCall5 call = reinterpret_cast<CuteQGeoCirclePrivateCall5>(taken[5]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QGeoShapePrivate *>(given);
    }
    return QGeoCirclePrivate::clone();
  }
};

//  bool QGeoCirclePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoCirclePrivate7isValidEv(const QGeoCirclePrivate *self) {
  return self->isValid();
}

//  bool QGeoCirclePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoCirclePrivate7isEmptyEv(const QGeoCirclePrivate *self) {
  return self->isEmpty();
}

//  bool QGeoCirclePrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoCirclePrivate8containsERK14QGeoCoordinate(
    const QGeoCirclePrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->contains(*coordinate);
}

//  QGeoCoordinate QGeoCirclePrivate::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK17QGeoCirclePrivate6centerEv(
    const QGeoCirclePrivate *self) {
  return new QGeoCoordinate(self->center());
}

//  QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK17QGeoCirclePrivate20boundingGeoRectangleEv(
    const QGeoCirclePrivate *self) {
  return new QGeoRectangle(self->boundingGeoRectangle());
}

//  bool QGeoCirclePrivate::crossNorthPole() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoCirclePrivate14crossNorthPoleEv(
    const QGeoCirclePrivate *self) {
  return self->crossNorthPole();
}

//  bool QGeoCirclePrivate::crossSouthPole() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QGeoCirclePrivate14crossSouthPoleEv(
    const QGeoCirclePrivate *self) {
  return self->crossSouthPole();
}

//  void QGeoCirclePrivate::updateBoundingBox()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCirclePrivate17updateBoundingBoxEv(
    QGeoCirclePrivate *self) {
  self->updateBoundingBox();
}

//  void QGeoCirclePrivate::setCenter(const QGeoCoordinate &c)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCirclePrivate9setCenterERK14QGeoCoordinate(
    QGeoCirclePrivate *self,
    const QGeoCoordinate *c) {
  self->setCenter(*c);
}

//  void QGeoCirclePrivate::setRadius(const qreal r)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCirclePrivate9setRadiusEd(
    QGeoCirclePrivate *self,
    qreal r) {
  self->setRadius(r);
}

//  void QGeoCirclePrivate::extendCircle(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QGeoCirclePrivate12extendCircleERK14QGeoCoordinate(
    QGeoCirclePrivate *self,
    const QGeoCoordinate *coordinate) {
  self->extendCircle(*coordinate);
}

//  QGeoShapePrivate *QGeoCirclePrivate::clone() const
extern "C" Q_DECL_EXPORT
QGeoShapePrivate *ritual_ZNK17QGeoCirclePrivate5cloneEv(
    const QGeoCirclePrivate *self) {
  return self->clone();
}

//  a Python function taken by a CuteQGeoCirclePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGeoCirclePrivate(
    QGeoCirclePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGeoCirclePrivate *>(self)->take(key, call);
}

//  bool QGeoCirclePrivate::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGeoCirclePrivate7isValidEv(
    const QGeoCirclePrivate *self) {
  return self->QGeoCirclePrivate::isValid();
}

//  bool QGeoCirclePrivate::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGeoCirclePrivate7isEmptyEv(
    const QGeoCirclePrivate *self) {
  return self->QGeoCirclePrivate::isEmpty();
}

//  bool QGeoCirclePrivate::contains(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK17QGeoCirclePrivate8containsERK14QGeoCoordinate(
    const QGeoCirclePrivate *self,
    const QGeoCoordinate *coordinate) {
  return self->QGeoCirclePrivate::contains(*coordinate);
}

//  QGeoCoordinate QGeoCirclePrivate::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_own_ZNK17QGeoCirclePrivate6centerEv(
    const QGeoCirclePrivate *self) {
  return new QGeoCoordinate(self->QGeoCirclePrivate::center());
}

//  QGeoRectangle QGeoCirclePrivate::boundingGeoRectangle() const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_own_ZNK17QGeoCirclePrivate20boundingGeoRectangleEv(
    const QGeoCirclePrivate *self) {
  return new QGeoRectangle(self->QGeoCirclePrivate::boundingGeoRectangle());
}
