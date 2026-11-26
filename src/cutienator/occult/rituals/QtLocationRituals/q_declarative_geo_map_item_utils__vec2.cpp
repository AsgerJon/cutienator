//  Written by dev_tooling.RitualGenerator from the records of
//  QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemutils_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtLocation/6.12.0/QtLocation/private/qlocationglobal_p.h>
#include <QtLocation/QtLocation>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtLocation/6.12.0/QtLocation/private/qdeclarativegeomapitemutils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/QtPositioning>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioning/6.12.0/QtPositioning/private/qdoublevector2d_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>

//  QDeclarativeGeoMapItemUtils::vec2::vec2(const QDoubleVector2D &p)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemUtils::vec2 *ritual_ZN27QDeclarativeGeoMapItemUtils4vec2C1ERK15QDoubleVector2D(
    const QDoubleVector2D *p) {
  return new QDeclarativeGeoMapItemUtils::vec2(*p);
}

//  QDeclarativeGeoMapItemUtils::vec2::vec2()
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemUtils::vec2 *ritual_ZN27QDeclarativeGeoMapItemUtils4vec2C1Ev() {
  return new QDeclarativeGeoMapItemUtils::vec2();
}

//  vec2 &QDeclarativeGeoMapItemUtils::vec2::operator=(const QPointF &p)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemUtils::vec2 *ritual_ZN27QDeclarativeGeoMapItemUtils4vec2aSERK7QPointF(
    QDeclarativeGeoMapItemUtils::vec2 *self,
    const QPointF *p) {
  return &(self->operator=(*p));
}

//  vec2 &QDeclarativeGeoMapItemUtils::vec2::operator=(const QDoubleVector2D
//      &p)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoMapItemUtils::vec2 *ritual_ZN27QDeclarativeGeoMapItemUtils4vec2aSERK15QDoubleVector2D(
    QDeclarativeGeoMapItemUtils::vec2 *self,
    const QDoubleVector2D *p) {
  return &(self->operator=(*p));
}

//  QDoubleVector2D QDeclarativeGeoMapItemUtils::vec2::toDoubleVector2D()
//      const
extern "C" Q_DECL_EXPORT
QDoubleVector2D *ritual_ZNK27QDeclarativeGeoMapItemUtils4vec216toDoubleVector2DEv(
    const QDeclarativeGeoMapItemUtils::vec2 *self) {
  return new QDoubleVector2D(self->toDoubleVector2D());
}

//  QDeclarativeGeoMapItemUtils::vec2::~vec2()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QDeclarativeGeoMapItemUtils4vec2D1Ev(
    QDeclarativeGeoMapItemUtils::vec2 *self) {
  delete self;
}
