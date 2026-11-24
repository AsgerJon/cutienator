//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeorectangle.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/6.12.0/QtPositioning/private/qpositioningglobal_p.h>
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/qgeorectangle.h>
#include <QtPositioning/private/qgeorectangle_p.h>
#include <QtPositioning/private/qwebmercator_p.h>
#include <QtPositioning/private/qdoublevector2d_p.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtCore/qnumeric.h>
#include <QtPositioning/private/qlocationutils_p.h>
#include <QtCore/QList>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 148, as _ZN13QGeoRectangle6d_funcEv
inline QGeoRectanglePrivate *QGeoRectangle::d_func()
{
    return static_cast<QGeoRectanglePrivate *>(d_ptr.data());
}

//  from ../qtpositioning/src/positioning/qgeorectangle.cpp, line 153, as _ZNK13QGeoRectangle6d_funcEv
inline const QGeoRectanglePrivate *QGeoRectangle::d_func() const
{
    return static_cast<const QGeoRectanglePrivate *>(d_ptr.constData());
}
//  -----------------------------------------------------------------------

//  QGeoRectangle::QGeoRectangle()
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1Ev() {
  return new QGeoRectangle();
}

//  QGeoRectangle::QGeoRectangle(const QGeoCoordinate &center, double
//      degreesWidth, double degreesHeight)
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1ERK14QGeoCoordinatedd(
    const QGeoCoordinate *center,
    double degreesWidth,
    double degreesHeight) {
  return new QGeoRectangle(*center, degreesWidth, degreesHeight);
}

//  QGeoRectangle::QGeoRectangle(const QGeoCoordinate &topLeft, const
//      QGeoCoordinate &bottomRight)
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1ERK14QGeoCoordinateS2_(
    const QGeoCoordinate *topLeft,
    const QGeoCoordinate *bottomRight) {
  return new QGeoRectangle(*topLeft, *bottomRight);
}

//  QGeoRectangle::QGeoRectangle(const QList<QGeoCoordinate> &coordinates)
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1ERK5QListI14QGeoCoordinateE(
    const QList<QGeoCoordinate> *coordinates) {
  return new QGeoRectangle(*coordinates);
}

//  QGeoRectangle::QGeoRectangle(const QGeoRectangle &other)
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1ERKS_(const QGeoRectangle *other) {
  return new QGeoRectangle(*other);
}

//  QGeoRectangle::QGeoRectangle(const QGeoShape &other)
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZN13QGeoRectangleC1ERK9QGeoShape(
    const QGeoShape *other) {
  return new QGeoRectangle(*other);
}

//  QGeoRectangle::~QGeoRectangle()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangleD1Ev(QGeoRectangle *self) {
  delete self;
}

//  void QGeoRectangle::setTopLeft(const QGeoCoordinate &topLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle10setTopLeftERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *topLeft) {
  self->setTopLeft(*topLeft);
}

//  QGeoCoordinate QGeoRectangle::topLeft() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK13QGeoRectangle7topLeftEv(
    const QGeoRectangle *self) {
  return new QGeoCoordinate(self->topLeft());
}

//  void QGeoRectangle::setTopRight(const QGeoCoordinate &topRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle11setTopRightERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *topRight) {
  self->setTopRight(*topRight);
}

//  QGeoCoordinate QGeoRectangle::topRight() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK13QGeoRectangle8topRightEv(
    const QGeoRectangle *self) {
  return new QGeoCoordinate(self->topRight());
}

//  void QGeoRectangle::setBottomLeft(const QGeoCoordinate &bottomLeft)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle13setBottomLeftERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *bottomLeft) {
  self->setBottomLeft(*bottomLeft);
}

//  QGeoCoordinate QGeoRectangle::bottomLeft() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK13QGeoRectangle10bottomLeftEv(
    const QGeoRectangle *self) {
  return new QGeoCoordinate(self->bottomLeft());
}

//  void QGeoRectangle::setBottomRight(const QGeoCoordinate &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle14setBottomRightERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *bottomRight) {
  self->setBottomRight(*bottomRight);
}

//  QGeoCoordinate QGeoRectangle::bottomRight() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK13QGeoRectangle11bottomRightEv(
    const QGeoRectangle *self) {
  return new QGeoCoordinate(self->bottomRight());
}

//  void QGeoRectangle::setCenter(const QGeoCoordinate &center)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle9setCenterERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *center) {
  self->setCenter(*center);
}

//  QGeoCoordinate QGeoRectangle::center() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK13QGeoRectangle6centerEv(
    const QGeoRectangle *self) {
  return new QGeoCoordinate(self->center());
}

//  void QGeoRectangle::setWidth(double degreesWidth)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle8setWidthEd(
    QGeoRectangle *self,
    double degreesWidth) {
  self->setWidth(degreesWidth);
}

//  double QGeoRectangle::width() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QGeoRectangle5widthEv(const QGeoRectangle *self) {
  return self->width();
}

//  void QGeoRectangle::setHeight(double degreesHeight)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle9setHeightEd(
    QGeoRectangle *self,
    double degreesHeight) {
  self->setHeight(degreesHeight);
}

//  double QGeoRectangle::height() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK13QGeoRectangle6heightEv(const QGeoRectangle *self) {
  return self->height();
}

//  bool QGeoRectangle::contains(const QGeoRectangle &rectangle) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGeoRectangle8containsERKS_(
    const QGeoRectangle *self,
    const QGeoRectangle *rectangle) {
  return self->contains(*rectangle);
}

//  bool QGeoRectangle::intersects(const QGeoRectangle &rectangle) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QGeoRectangle10intersectsERKS_(
    const QGeoRectangle *self,
    const QGeoRectangle *rectangle) {
  return self->intersects(*rectangle);
}

//  void QGeoRectangle::translate(double degreesLatitude, double
//      degreesLongitude)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle9translateEdd(
    QGeoRectangle *self,
    double degreesLatitude,
    double degreesLongitude) {
  self->translate(degreesLatitude, degreesLongitude);
}

//  QGeoRectangle QGeoRectangle::translated(double degreesLatitude, double
//      degreesLongitude) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK13QGeoRectangle10translatedEdd(
    const QGeoRectangle *self,
    double degreesLatitude,
    double degreesLongitude) {
  return new QGeoRectangle(
      self->translated(
          degreesLatitude,
          degreesLongitude));
}

//  void QGeoRectangle::extendRectangle(const QGeoCoordinate &coordinate)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangle15extendRectangleERK14QGeoCoordinate(
    QGeoRectangle *self,
    const QGeoCoordinate *coordinate) {
  self->extendRectangle(*coordinate);
}

//  QGeoRectangle QGeoRectangle::united(const QGeoRectangle &rectangle) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK13QGeoRectangle6unitedERKS_(
    const QGeoRectangle *self,
    const QGeoRectangle *rectangle) {
  return new QGeoRectangle(self->united(*rectangle));
}

//  QGeoRectangle QGeoRectangle::operator|(const QGeoRectangle &rectangle)
//      const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_ZNK13QGeoRectangleorERKS_(
    const QGeoRectangle *self,
    const QGeoRectangle *rectangle) {
  return new QGeoRectangle(self->operator|(*rectangle));
}

//  QGeoRectangle &QGeoRectangle::operator|=(const QGeoRectangle &rectangle)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QGeoRectangleoRERKS_(
    QGeoRectangle *self,
    const QGeoRectangle *rectangle) {
  self->operator|=(*rectangle);
}

//  QString QGeoRectangle::toString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK13QGeoRectangle8toStringEv(const QGeoRectangle *self) {
  return new QString(self->toString());
}

//  QGeoRectanglePrivate *QGeoRectangle::d_func()
extern "C" Q_DECL_EXPORT
QGeoRectanglePrivate *ritual_ZN13QGeoRectangle6d_funcEv(
    QGeoRectangle *self) {
  return self->d_func();
}

//  const QGeoRectanglePrivate *QGeoRectangle::d_func() const
extern "C" Q_DECL_EXPORT
const QGeoRectanglePrivate *ritual_ZNK13QGeoRectangle6d_funcEv(
    const QGeoRectangle *self) {
  return self->d_func();
}

//  QList<QGeoRectangle>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoRectangle> *ritual_list_make_QGeoRectangle() {
  return new QList<QGeoRectangle>();
}

//  void QList<QGeoRectangle>::append(const QGeoRectangle &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoRectangle(
    QList<QGeoRectangle> *self,
    const QGeoRectangle *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoRectangle>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoRectangle(const QList<QGeoRectangle> *self) {
  return self->size();
}

//  const QGeoRectangle &QList<QGeoRectangle>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoRectangle *ritual_list_at_QGeoRectangle(
    const QList<QGeoRectangle> *self,
    long long index) {
  return new QGeoRectangle(self->at(index));
}

//  QList<QGeoRectangle>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoRectangle(QList<QGeoRectangle> *self) {
  delete self;
}
