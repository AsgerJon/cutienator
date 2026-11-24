//  Written by dev_tooling.RitualGenerator from the records of QtPositioningQ
//  uick/6.12.0/QtPositioningQuick/private/qdeclarativegeoaddress_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qpositioningquickglobal_p.h>
#include <QtPositioningQuick/QtPositioningQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtPositioningQuick/6.12.0/QtPositioningQuick/private/qdeclarativegeoaddress_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtPositioning/qgeoaddress.h>

//  const QMetaObject *QDeclarativeGeoAddress::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK22QDeclarativeGeoAddress10metaObjectEv(
    const QDeclarativeGeoAddress *self) {
  return self->metaObject();
}

//  QString QDeclarativeGeoAddress::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN22QDeclarativeGeoAddress2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QDeclarativeGeoAddress::tr(s, c, n));
}

//  QDeclarativeGeoAddress::QDeclarativeGeoAddress(QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoAddress *ritual_ZN22QDeclarativeGeoAddressC1EP7QObject(
    QObject *parent) {
  return new QDeclarativeGeoAddress(parent);
}

//  QDeclarativeGeoAddress::QDeclarativeGeoAddress(const QGeoAddress
//      &address, QObject *parent)
extern "C" Q_DECL_EXPORT
QDeclarativeGeoAddress *ritual_ZN22QDeclarativeGeoAddressC1ERK11QGeoAddressP7QObject(
    const QGeoAddress *address,
    QObject *parent) {
  return new QDeclarativeGeoAddress(*address, parent);
}

//  QGeoAddress QDeclarativeGeoAddress::address() const
extern "C" Q_DECL_EXPORT
QGeoAddress *ritual_ZNK22QDeclarativeGeoAddress7addressEv(
    const QDeclarativeGeoAddress *self) {
  return new QGeoAddress(self->address());
}

//  void QDeclarativeGeoAddress::setAddress(const QGeoAddress &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress10setAddressERK11QGeoAddress(
    QDeclarativeGeoAddress *self,
    const QGeoAddress *address) {
  self->setAddress(*address);
}

//  QString QDeclarativeGeoAddress::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress4textEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->text());
}

//  void QDeclarativeGeoAddress::setText(const QString &address)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress7setTextERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *address) {
  self->setText(*address);
}

//  QString QDeclarativeGeoAddress::country() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress7countryEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->country());
}

//  void QDeclarativeGeoAddress::setCountry(const QString &country)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress10setCountryERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *country) {
  self->setCountry(*country);
}

//  QString QDeclarativeGeoAddress::countryCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress11countryCodeEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->countryCode());
}

//  void QDeclarativeGeoAddress::setCountryCode(const QString &countryCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress14setCountryCodeERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *countryCode) {
  self->setCountryCode(*countryCode);
}

//  QString QDeclarativeGeoAddress::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress5stateEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->state());
}

//  void QDeclarativeGeoAddress::setState(const QString &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress8setStateERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *state) {
  self->setState(*state);
}

//  QString QDeclarativeGeoAddress::county() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress6countyEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->county());
}

//  void QDeclarativeGeoAddress::setCounty(const QString &county)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress9setCountyERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *county) {
  self->setCounty(*county);
}

//  QString QDeclarativeGeoAddress::city() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress4cityEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->city());
}

//  void QDeclarativeGeoAddress::setCity(const QString &city)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress7setCityERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *city) {
  self->setCity(*city);
}

//  QString QDeclarativeGeoAddress::district() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress8districtEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->district());
}

//  void QDeclarativeGeoAddress::setDistrict(const QString &district)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress11setDistrictERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *district) {
  self->setDistrict(*district);
}

//  QString QDeclarativeGeoAddress::street() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress6streetEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->street());
}

//  void QDeclarativeGeoAddress::setStreet(const QString &street)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress9setStreetERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *street) {
  self->setStreet(*street);
}

//  QString QDeclarativeGeoAddress::streetNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress12streetNumberEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->streetNumber());
}

//  void QDeclarativeGeoAddress::setStreetNumber(const QString &streetNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress15setStreetNumberERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *streetNumber) {
  self->setStreetNumber(*streetNumber);
}

//  QString QDeclarativeGeoAddress::postalCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK22QDeclarativeGeoAddress10postalCodeEv(
    const QDeclarativeGeoAddress *self) {
  return new QString(self->postalCode());
}

//  void QDeclarativeGeoAddress::setPostalCode(const QString &postalCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QDeclarativeGeoAddress13setPostalCodeERK7QString(
    QDeclarativeGeoAddress *self,
    const QString *postalCode) {
  self->setPostalCode(*postalCode);
}

//  bool QDeclarativeGeoAddress::isTextGenerated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QDeclarativeGeoAddress15isTextGeneratedEv(
    const QDeclarativeGeoAddress *self) {
  return self->isTextGenerated();
}
