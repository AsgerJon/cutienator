//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeopath.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeopath.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qgeopath.h"
#include "qgeopolygon.h"
#include "qgeopath_p.h"
#include "qgeocoordinate.h"
#include "qnumeric.h"
#include "qlocationutils_p.h"
#include "qwebmercator_p.h"
#include "qdoublevector2d_p.h"
#include <QtCore/qmutex.h>
#include <mutex>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeopath.cpp, line 65, as _ZN8QGeoPath6d_funcEv
inline QGeoPathPrivate *QGeoPath::d_func()
{
    return static_cast<QGeoPathPrivate *>(d_ptr.data());
}

//  from ../qtpositioning/src/positioning/qgeopath.cpp, line 70, as _ZNK8QGeoPath6d_funcEv
inline const QGeoPathPrivate *QGeoPath::d_func() const
{
    return static_cast<const QGeoPathPrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QGeoPath::QGeoPath()
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZN8QGeoPathC1Ev() {
  return new QGeoPath();
}

//  QGeoPath::QGeoPath(const QList<QGeoCoordinate> &path, const qreal &width)
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZN8QGeoPathC1ERK5QListI14QGeoCoordinateERKd(
    const QList<QGeoCoordinate> *path,
    qreal width) {
  return new QGeoPath(*path, width);
}

//  QGeoPath::QGeoPath(const QGeoPath &other)
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZN8QGeoPathC1ERKS_(const QGeoPath *other) {
  return new QGeoPath(*other);
}

//  QGeoPath::QGeoPath(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZN8QGeoPathC1ERK9QGeoShape(const QGeoShape *other) {
  return new QGeoPath(*other);
}

//  QGeoPath::~QGeoPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPathD1Ev(QGeoPath *self) {
  delete self;
}

//  void QGeoPath::setPath(const QList<QGeoCoordinate> &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath7setPathERK5QListI14QGeoCoordinateE(
    QGeoPath *self,
    const QList<QGeoCoordinate> *path) {
  self->setPath(*path);
}

//  const QList<QGeoCoordinate> &QGeoPath::path() const
extern "C" Q_DECL_EXPORT
QList<QGeoCoordinate> *ritual_ZNK8QGeoPath4pathEv(const QGeoPath *self) {
  return new QList<QGeoCoordinate>(self->path());
}

//  void QGeoPath::clearPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath9clearPathEv(QGeoPath *self) {
  self->clearPath();
}

//  void QGeoPath::setVariantPath(const QVariantList &path)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath14setVariantPathERK5QListI8QVariantE(
    QGeoPath *self,
    const QList<QVariant> *path) {
  self->setVariantPath(*path);
}

//  QVariantList QGeoPath::variantPath() const
extern "C" Q_DECL_EXPORT
QList<QVariant> *ritual_ZNK8QGeoPath11variantPathEv(const QGeoPath *self) {
  return new QList<QVariant>(self->variantPath());
}

//  void QGeoPath::setWidth(const qreal &width)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath8setWidthERKd(QGeoPath *self, qreal width) {
  self->setWidth(width);
}

//  qreal QGeoPath::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK8QGeoPath5widthEv(const QGeoPath *self) {
  return self->width();
}

//  void QGeoPath::translate(double degreesLatitude, double degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath9translateEdd(
    QGeoPath *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  QGeoPath QGeoPath::translated(double degreesLatitude, double
//      degreesLongitude) const
extern "C" Q_DECL_EXPORT
QGeoPath *ritual_ZNK8QGeoPath10translatedEdd(
    const QGeoPath *self,
    double degreesLatitude,
    double degreesLongitude) {
  return new QGeoPath(self->translated(degreesLatitude, degreesLongitude));
}

//  double QGeoPath::length(qsizetype indexFrom, qsizetype indexTo) const
extern "C" Q_DECL_EXPORT
double ritual_ZNK8QGeoPath6lengthExx(
    const QGeoPath *self,
    qsizetype indexFrom,
    qsizetype indexTo) {
  return self->length(indexFrom, indexTo);
}

//  qsizetype QGeoPath::size() const
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZNK8QGeoPath4sizeEv(const QGeoPath *self) {
  return self->size();
}

//  void QGeoPath::addCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath13addCoordinateERK14QGeoCoordinate(
    QGeoPath *self,
    const QGeoCoordinate *coordinate) {
  self->addCoordinate(*coordinate);
}

//  void QGeoPath::insertCoordinate(qsizetype index, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath16insertCoordinateExRK14QGeoCoordinate(
    QGeoPath *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->insertCoordinate(index, *coordinate);
}

//  void QGeoPath::replaceCoordinate(qsizetype index, const QGeoCoordinate
//      &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath17replaceCoordinateExRK14QGeoCoordinate(
    QGeoPath *self,
    qsizetype index,
    const QGeoCoordinate *coordinate) {
  self->replaceCoordinate(index, *coordinate);
}

//  QGeoCoordinate QGeoPath::coordinateAt(qsizetype index) const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK8QGeoPath12coordinateAtEx(
    const QGeoPath *self,
    qsizetype index) {
  return new QGeoCoordinate(self->coordinateAt(index));
}

//  bool QGeoPath::containsCoordinate(const QGeoCoordinate &coordinate) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QGeoPath18containsCoordinateERK14QGeoCoordinate(
    const QGeoPath *self,
    const QGeoCoordinate *coordinate) {
  return self->containsCoordinate(*coordinate);
}

//  void QGeoPath::removeCoordinate(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath16removeCoordinateERK14QGeoCoordinate(
    QGeoPath *self,
    const QGeoCoordinate *coordinate) {
  self->removeCoordinate(*coordinate);
}

//  void QGeoPath::removeCoordinate(qsizetype index)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QGeoPath16removeCoordinateEx(
    QGeoPath *self,
    qsizetype index) {
  self->removeCoordinate(index);
}

//  QString QGeoPath::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QGeoPath8toStringEv(const QGeoPath *self) {
  return new QString(self->toString());
}

//  QGeoPathPrivate *QGeoPath::d_func()
extern "C" Q_DECL_EXPORT
QGeoPathPrivate *ritual_ZN8QGeoPath6d_funcEv(QGeoPath *self) {
  return self->d_func();
}

//  const QGeoPathPrivate *QGeoPath::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoPathPrivate *ritual_ZNK8QGeoPath6d_funcEv(const QGeoPath *self) {
  return self->d_func();
}
