//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeocircle.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeocircle.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeocircle.h>
#include <QtPositioning/private/qgeocircle_p.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qnumeric.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtPositioning/private/qdoublevector2d_p.h>
#include <QtPositioning/private/qdoublevector3d_p.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 67, as _ZN10QGeoCircle6d_funcEv
inline QGeoCirclePrivate *QGeoCircle::d_func()
{
    return static_cast<QGeoCirclePrivate *>(d_ptr.data());
}

//  from ../qtpositioning/src/positioning/qgeocircle.cpp, line 72, as _ZNK10QGeoCircle6d_funcEv
inline const QGeoCirclePrivate *QGeoCircle::d_func() const
{
    return static_cast<const QGeoCirclePrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QGeoCircle::QGeoCircle()
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZN10QGeoCircleC1Ev() {
  return new QGeoCircle();
}

//  QGeoCircle::QGeoCircle(const QGeoCoordinate &center, qreal radius)
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZN10QGeoCircleC1ERK14QGeoCoordinated(
    const QGeoCoordinate *center,
    qreal radius) {
  return new QGeoCircle(*center, radius);
}

//  QGeoCircle::QGeoCircle(const QGeoCircle &other)
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZN10QGeoCircleC1ERKS_(const QGeoCircle *other) {
  return new QGeoCircle(*other);
}

//  QGeoCircle::QGeoCircle(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZN10QGeoCircleC1ERK9QGeoShape(const QGeoShape *other) {
  return new QGeoCircle(*other);
}

//  QGeoCircle::~QGeoCircle()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QGeoCircleD1Ev(QGeoCircle *self) {
  delete self;
}

//  QGeoCircle &QGeoCircle::operator=(const QGeoCircle &other)
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZN10QGeoCircleaSERKS_(
    QGeoCircle *self,
    const QGeoCircle *other) {
  return &(self->operator=(*other));
}

//  void QGeoCircle::setCenter(const QGeoCoordinate &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QGeoCircle9setCenterERK14QGeoCoordinate(
    QGeoCircle *self,
    const QGeoCoordinate *center) {
  self->setCenter(*center);
}

//  QGeoCoordinate QGeoCircle::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK10QGeoCircle6centerEv(const QGeoCircle *self) {
  return new QGeoCoordinate(self->center());
}

//  void QGeoCircle::setRadius(qreal radius)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QGeoCircle9setRadiusEd(QGeoCircle *self, qreal radius) {
  self->setRadius(radius);
}

//  qreal QGeoCircle::radius() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK10QGeoCircle6radiusEv(const QGeoCircle *self) {
  return self->radius();
}

//  void QGeoCircle::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QGeoCircle9translateEdd(
    QGeoCircle *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  QGeoCircle QGeoCircle::translated(double degreesLatitude, double
//      degreesLongitude) const
extern "C" Q_DECL_EXPORT
QGeoCircle *ritual_ZNK10QGeoCircle10translatedEdd(
    const QGeoCircle *self,
    double degreesLatitude,
    double degreesLongitude) {
  return new QGeoCircle(self->translated(degreesLatitude, degreesLongitude));
}

//  void QGeoCircle::extendCircle(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QGeoCircle12extendCircleERK14QGeoCoordinate(
    QGeoCircle *self,
    const QGeoCoordinate *coordinate) {
  self->extendCircle(*coordinate);
}

//  QString QGeoCircle::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10QGeoCircle8toStringEv(const QGeoCircle *self) {
  return new QString(self->toString());
}

//  QGeoCirclePrivate *QGeoCircle::d_func()
extern "C" Q_DECL_EXPORT
QGeoCirclePrivate *ritual_ZN10QGeoCircle6d_funcEv(QGeoCircle *self) {
  return self->d_func();
}

//  const QGeoCirclePrivate *QGeoCircle::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoCirclePrivate *ritual_ZNK10QGeoCircle6d_funcEv(
    const QGeoCircle *self) {
  return self->d_func();
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &stream, const QGeoCircle &circle)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK10QGeoCircle(
    QDataStream *stream,
    const QGeoCircle *circle) {
  return &(operator<<(*stream, *circle));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &stream, QGeoCircle &circle)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR10QGeoCircle(
    QDataStream *stream,
    QGeoCircle *circle) {
  return &(operator>>(*stream, *circle));
}
#endif  // !defined(QT_NO_DATASTREAM)
