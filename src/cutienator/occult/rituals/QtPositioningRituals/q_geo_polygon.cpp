//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeopolygon.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeopolygon.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeopolygon.h"
#include "qgeopolygon_p.h"
#include "qgeopath_p.h"
#include "qgeocircle.h"
#include "qgeocoordinate.h"
#include "qnumeric.h"
#include "qlocationutils_p.h"
#include "qwebmercator_p.h"
#include "qdoublevector2d_p.h"
#include "qdoublevector3d_p.h"
#include "qwebmercator_p.h"
#include <QtCore/qmutex.h>
#include <mutex>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeopolygon.cpp, line 68, as _ZN11QGeoPolygon6d_funcEv
inline QGeoPolygonPrivate *QGeoPolygon::d_func()
{
    return static_cast<QGeoPolygonPrivate *>(d_ptr.data());
}

//  from ../qtpositioning/src/positioning/qgeopolygon.cpp, line 73, as _ZNK11QGeoPolygon6d_funcEv
inline const QGeoPolygonPrivate *QGeoPolygon::d_func() const
{
    return static_cast<const QGeoPolygonPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QGeoPolygon::QGeoPolygon()
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZN11QGeoPolygonC1Ev() {
  return new QGeoPolygon();
}

//  QGeoPolygon::QGeoPolygon(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZN11QGeoPolygonC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *path) {
  return new QGeoPolygon(*path);
}

//  QGeoPolygon::QGeoPolygon(const QGeoPolygon &other)
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZN11QGeoPolygonC1ERKS_(const QGeoPolygon *other) {
  return new QGeoPolygon(*other);
}

//  QGeoPolygon::QGeoPolygon(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZN11QGeoPolygonC1ERK9QGeoShape(const QGeoShape *other) {
  return new QGeoPolygon(*other);
}

//  QGeoPolygon::~QGeoPolygon()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygonD1Ev(QGeoPolygon *self) {
  delete self;
}

//  void QGeoPolygon::setPerimeter(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon12setPerimeterERK5QListI14QGeoCoordinateE(
    QGeoPolygon *self,
    const QList<QGeoCoordinate> *path) {
  self->setPerimeter(*path);
}

//  const QList<QGeoCoordinate> &QGeoPolygon::perimeter() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK11QGeoPolygon9perimeterEv(
    const QGeoPolygon *self) {
  return new QList<QGeoCoordinate>(self->perimeter());
}

//  void QGeoPolygon::addHole(const QVariant &holePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon7addHoleERK8QVariant(
    QGeoPolygon *self,
    const QVariant *holePath) {
  self->addHole(*holePath);
}

//  void QGeoPolygon::addHole(const QList<QGeoCoordinate> &holePath)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon7addHoleERK5QListI14QGeoCoordinateE(
    QGeoPolygon *self,
    const QList<QGeoCoordinate> *holePath) {
  self->addHole(*holePath);
}

//  const QVariantList QGeoPolygon::hole(qsizetype index) const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK11QGeoPolygon4holeEx(
    const QGeoPolygon *self,
    qsizetype index) {
  return new QList<QVariant>(self->hole(index));
}

//  const QList<QGeoCoordinate> QGeoPolygon::holePath(qsizetype index) const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK11QGeoPolygon8holePathEx(
    const QGeoPolygon *self,
    qsizetype index) {
  return new QList<QGeoCoordinate>(self->holePath(index));
}

//  void QGeoPolygon::removeHole(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon10removeHoleEx(
    QGeoPolygon *self,
    qsizetype index) {
  self->removeHole(index);
}

//  qsizetype QGeoPolygon::holesCount() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QGeoPolygon10holesCountEv(const QGeoPolygon *self) {
  return self->holesCount();
}

//  void QGeoPolygon::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon9translateEdd(
    QGeoPolygon *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  QGeoPolygon QGeoPolygon::translated(double degreesLatitude, double
//      degreesLongitude) const
extern "C" Q_DECL_EXPORT
QGeoPolygon *ritual_ZNK11QGeoPolygon10translatedEdd(
    const QGeoPolygon *self,
    double degreesLatitude,
    double degreesLongitude) {
  return new QGeoPolygon(
      self->translated(
          degreesLatitude,
          degreesLongitude));
}

//  double QGeoPolygon::length(qsizetype indexFrom, qsizetype indexTo) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK11QGeoPolygon6lengthExx(
    const QGeoPolygon *self,
    qsizetype indexFrom,
    qsizetype indexTo) {
  return self->length(indexFrom, indexTo);
}

//  qsizetype QGeoPolygon::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK11QGeoPolygon4sizeEv(const QGeoPolygon *self) {
  return self->size();
}

//  void QGeoPolygon::addCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon13addCoordinateERK14QGeoCoordinate(
    QGeoPolygon *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}

//  void QGeoPolygon::insertCoordinate(qsizetype index, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon16insertCoordinateExRK14QGeoCoordinate(
    QGeoPolygon *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->insertCoordinate(index, *coordinate);
}

//  void QGeoPolygon::replaceCoordinate(qsizetype index, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon17replaceCoordinateExRK14QGeoCoordinate(
    QGeoPolygon *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->replaceCoordinate(index, *coordinate);
}

//  QGeoCoordinate QGeoPolygon::coordinateAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK11QGeoPolygon12coordinateAtEx(
    const QGeoPolygon *self,
    qsizetype index) {
  return new QGeoCoordinate(self->coordinateAt(index));
}

//  bool QGeoPolygon::containsCoordinate(const QGeoCoordinate &coordinate)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoPolygon18containsCoordinateERK14QGeoCoordinate(
    const QGeoPolygon *self,
    const QGeoCoordinate *coordinate) {
  return self->containsCoordinate(*coordinate);
}

//  void QGeoPolygon::removeCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon16removeCoordinateERK14QGeoCoordinate(
    QGeoPolygon *self,
    const QGeoCoordinate *coordinate) {
  self->removeCoordinate(*coordinate);
}

//  void QGeoPolygon::removeCoordinate(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoPolygon16removeCoordinateEx(
    QGeoPolygon *self,
    qsizetype index) {
  self->removeCoordinate(index);
}

//  QString QGeoPolygon::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoPolygon8toStringEv(const QGeoPolygon *self) {
  return new QString(self->toString());
}

//  QGeoPolygonPrivate *QGeoPolygon::d_func()
extern "C" Q_DECL_EXPORT
QGeoPolygonPrivate *ritual_ZN11QGeoPolygon6d_funcEv(QGeoPolygon *self) {
  return self->d_func();
}

//  const QGeoPolygonPrivate *QGeoPolygon::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoPolygonPrivate *ritual_ZNK11QGeoPolygon6d_funcEv(
    const QGeoPolygon *self) {
  return self->d_func();
}
