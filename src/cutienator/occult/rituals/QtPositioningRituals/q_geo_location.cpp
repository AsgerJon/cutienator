//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeolocation.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeolocation.h>
#include <QtPositioning/qgeoaddress.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  QGeoLocation::QGeoLocation()
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZN12QGeoLocationC1Ev() {
  return new QGeoLocation();
}

//  QGeoLocation::QGeoLocation(const QGeoLocation &other)
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZN12QGeoLocationC1ERKS_(const QGeoLocation *other) {
  return new QGeoLocation(*other);
}

//  QGeoLocation::~QGeoLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocationD1Ev(QGeoLocation *self) {
  delete self;
}

//  bool operator==(const QGeoLocation &lhs, const QGeoLocation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK12QGeoLocationS1_(
    const QGeoLocation *lhs,
    const QGeoLocation *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoLocation &lhs, const QGeoLocation &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK12QGeoLocationS1_(
    const QGeoLocation *lhs,
    const QGeoLocation *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QGeoAddress QGeoLocation::address() const
extern "C" Q_DECL_EXPORT
QGeoAddress *ritual_ZNK12QGeoLocation7addressEv(const QGeoLocation *self) {
  return new QGeoAddress(self->address());
}

//  void QGeoLocation::setAddress(const QGeoAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocation10setAddressERK11QGeoAddress(
    QGeoLocation *self,
    const QGeoAddress *address) {
  self->setAddress(*address);
}

//  QGeoCoordinate QGeoLocation::coordinate() const
extern "C" Q_DECL_EXPORT
QGeoCoordinate *ritual_ZNK12QGeoLocation10coordinateEv(
    const QGeoLocation *self) {
  return new QGeoCoordinate(self->coordinate());
}

//  void QGeoLocation::setCoordinate(const QGeoCoordinate &position)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocation13setCoordinateERK14QGeoCoordinate(
    QGeoLocation *self,
    const QGeoCoordinate *position) {
  self->setCoordinate(*position);
}

//  QGeoShape QGeoLocation::boundingShape() const
extern "C" Q_DECL_EXPORT
QGeoShape *ritual_ZNK12QGeoLocation13boundingShapeEv(
    const QGeoLocation *self) {
  return new QGeoShape(self->boundingShape());
}

//  void QGeoLocation::setBoundingShape(const QGeoShape &shape)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocation16setBoundingShapeERK9QGeoShape(
    QGeoLocation *self,
    const QGeoShape *shape) {
  self->setBoundingShape(*shape);
}

//  QVariantMap QGeoLocation::extendedAttributes() const
extern "C" Q_DECL_EXPORT
QMap<QString, QVariant> *ritual_ZNK12QGeoLocation18extendedAttributesEv(
    const QGeoLocation *self) {
  return new QMap<QString, QVariant>(self->extendedAttributes());
}

//  void QGeoLocation::setExtendedAttributes(const QVariantMap &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocation21setExtendedAttributesERK4QMapI7QString8QVariantE(
    QGeoLocation *self,
    const QMap<QString, QVariant> *data) {
  self->setExtendedAttributes(*data);
}

//  bool QGeoLocation::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QGeoLocation7isEmptyEv(const QGeoLocation *self) {
  return self->isEmpty();
}

//  bool QGeoLocation::equals(const QGeoLocation &lhs, const QGeoLocation
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QGeoLocation6equalsERKS_S1_(
    const QGeoLocation *lhs,
    const QGeoLocation *rhs) {
  return QGeoLocation::equals(*lhs, *rhs);
}
