//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeolocation.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeolocation.h>
#include <QtPositioning/qgeoaddress.h>
#include <QtPositioning/qgeocoordinate.h>
#include <QtPositioning/qgeoshape.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
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

//  QGeoLocation::QGeoLocation(QGeoLocation &&other)
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZN12QGeoLocationC1EOS_(QGeoLocation *other) {
  return new QGeoLocation(std::move(*other));
}

//  QGeoLocation::~QGeoLocation()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocationD1Ev(QGeoLocation *self) {
  delete self;
}

//  QGeoLocation &QGeoLocation::operator=(const QGeoLocation &other)
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZN12QGeoLocationaSERKS_(
    QGeoLocation *self,
    const QGeoLocation *other) {
  return &(self->operator=(*other));
}

//  QGeoLocation &QGeoLocation::operator=(QGeoLocation &&other)
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_ZN12QGeoLocationaSEOS_(
    QGeoLocation *self,
    QGeoLocation *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QGeoLocation::swap(QGeoLocation &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QGeoLocation4swapERS_(
    QGeoLocation *self,
    QGeoLocation *other) {
  self->swap(*other);
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

//  QList<QGeoLocation>::QList()
extern "C" Q_DECL_EXPORT
QList<QGeoLocation> *ritual_list_make_QGeoLocation() {
  return new QList<QGeoLocation>();
}

//  void QList<QGeoLocation>::append(const QGeoLocation &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QGeoLocation(
    QList<QGeoLocation> *self,
    const QGeoLocation *element) {
  self->append(*element);
}

//  qsizetype QList<QGeoLocation>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QGeoLocation(const QList<QGeoLocation> *self) {
  return self->size();
}

//  const QGeoLocation &QList<QGeoLocation>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QGeoLocation *ritual_list_at_QGeoLocation(
    const QList<QGeoLocation> *self,
    long long index) {
  return new QGeoLocation(self->at(index));
}

//  QList<QGeoLocation>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QGeoLocation(QList<QGeoLocation> *self) {
  delete self;
}
