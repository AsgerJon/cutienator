//  Written by dev_tooling.RitualGenerator from the records of
//  QtPositioning/qgeoaddress.h, Qt 6.12.0. Changes made here are lost.
#include <QtPositioning/qgeoaddress.h>
#include <QtCore/qstring.h>

//  QGeoAddress::QGeoAddress()
extern "C" Q_DECL_EXPORT
QGeoAddress *ritual_ZN11QGeoAddressC1Ev() {
  return new QGeoAddress();
}

//  QGeoAddress::QGeoAddress(const QGeoAddress &other)
extern "C" Q_DECL_EXPORT
QGeoAddress *ritual_ZN11QGeoAddressC1ERKS_(const QGeoAddress *other) {
  return new QGeoAddress(*other);
}

//  QGeoAddress::~QGeoAddress()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddressD1Ev(QGeoAddress *self) {
  delete self;
}

//  bool operator==(const QGeoAddress &lhs, const QGeoAddress &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QGeoAddressS1_(
    const QGeoAddress *lhs,
    const QGeoAddress *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QGeoAddress &lhs, const QGeoAddress &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QGeoAddressS1_(
    const QGeoAddress *lhs,
    const QGeoAddress *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QString QGeoAddress::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress4textEv(const QGeoAddress *self) {
  return new QString(self->text());
}

//  void QGeoAddress::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress7setTextERK7QString(
    QGeoAddress *self,
    const QString *text) {
  self->setText(*text);
}

//  QString QGeoAddress::country() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress7countryEv(const QGeoAddress *self) {
  return new QString(self->country());
}

//  void QGeoAddress::setCountry(const QString &country)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress10setCountryERK7QString(
    QGeoAddress *self,
    const QString *country) {
  self->setCountry(*country);
}

//  QString QGeoAddress::countryCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress11countryCodeEv(const QGeoAddress *self) {
  return new QString(self->countryCode());
}

//  void QGeoAddress::setCountryCode(const QString &countryCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress14setCountryCodeERK7QString(
    QGeoAddress *self,
    const QString *countryCode) {
  self->setCountryCode(*countryCode);
}

//  QString QGeoAddress::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress5stateEv(const QGeoAddress *self) {
  return new QString(self->state());
}

//  void QGeoAddress::setState(const QString &state)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress8setStateERK7QString(
    QGeoAddress *self,
    const QString *state) {
  self->setState(*state);
}

//  QString QGeoAddress::county() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress6countyEv(const QGeoAddress *self) {
  return new QString(self->county());
}

//  void QGeoAddress::setCounty(const QString &county)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress9setCountyERK7QString(
    QGeoAddress *self,
    const QString *county) {
  self->setCounty(*county);
}

//  QString QGeoAddress::city() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress4cityEv(const QGeoAddress *self) {
  return new QString(self->city());
}

//  void QGeoAddress::setCity(const QString &city)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress7setCityERK7QString(
    QGeoAddress *self,
    const QString *city) {
  self->setCity(*city);
}

//  QString QGeoAddress::district() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress8districtEv(const QGeoAddress *self) {
  return new QString(self->district());
}

//  void QGeoAddress::setDistrict(const QString &district)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress11setDistrictERK7QString(
    QGeoAddress *self,
    const QString *district) {
  self->setDistrict(*district);
}

//  QString QGeoAddress::postalCode() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress10postalCodeEv(const QGeoAddress *self) {
  return new QString(self->postalCode());
}

//  void QGeoAddress::setPostalCode(const QString &postalCode)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress13setPostalCodeERK7QString(
    QGeoAddress *self,
    const QString *postalCode) {
  self->setPostalCode(*postalCode);
}

//  QString QGeoAddress::street() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress6streetEv(const QGeoAddress *self) {
  return new QString(self->street());
}

//  void QGeoAddress::setStreet(const QString &street)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress9setStreetERK7QString(
    QGeoAddress *self,
    const QString *street) {
  self->setStreet(*street);
}

//  QString QGeoAddress::streetNumber() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK11QGeoAddress12streetNumberEv(const QGeoAddress *self) {
  return new QString(self->streetNumber());
}

//  void QGeoAddress::setStreetNumber(const QString &streetNumber)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress15setStreetNumberERK7QString(
    QGeoAddress *self,
    const QString *streetNumber) {
  self->setStreetNumber(*streetNumber);
}

//  bool QGeoAddress::isEmpty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoAddress7isEmptyEv(const QGeoAddress *self) {
  return self->isEmpty();
}

//  void QGeoAddress::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QGeoAddress5clearEv(QGeoAddress *self) {
  self->clear();
}

//  bool QGeoAddress::isTextGenerated() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QGeoAddress15isTextGeneratedEv(const QGeoAddress *self) {
  return self->isTextGenerated();
}

//  bool QGeoAddress::equals(const QGeoAddress &lhs, const QGeoAddress &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QGeoAddress6equalsERKS_S1_(
    const QGeoAddress *lhs,
    const QGeoAddress *rhs) {
  return QGeoAddress::equals(*lhs, *rhs);
}
