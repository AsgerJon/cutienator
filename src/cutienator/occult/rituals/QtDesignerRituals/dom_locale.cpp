//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/ui4_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/ui4_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  DomLocale::DomLocale()
extern "C" Q_DECL_EXPORT
DomLocale *ritual_ZN9DomLocaleC1Ev() {
  return new DomLocale();
}

//  DomLocale::~DomLocale()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomLocaleD1Ev(DomLocale *self) {
  delete self;
}

//  bool DomLocale::hasAttributeLanguage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomLocale20hasAttributeLanguageEv(const DomLocale *self) {
  return self->hasAttributeLanguage();
}

//  QString DomLocale::attributeLanguage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomLocale17attributeLanguageEv(const DomLocale *self) {
  return new QString(self->attributeLanguage());
}

//  void DomLocale::setAttributeLanguage(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomLocale20setAttributeLanguageERK7QString(
    DomLocale *self,
    const QString *a) {
  self->setAttributeLanguage(*a);
}

//  void DomLocale::clearAttributeLanguage()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomLocale22clearAttributeLanguageEv(DomLocale *self) {
  self->clearAttributeLanguage();
}

//  bool DomLocale::hasAttributeCountry() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9DomLocale19hasAttributeCountryEv(const DomLocale *self) {
  return self->hasAttributeCountry();
}

//  QString DomLocale::attributeCountry() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9DomLocale16attributeCountryEv(const DomLocale *self) {
  return new QString(self->attributeCountry());
}

//  void DomLocale::setAttributeCountry(const QString &a)
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomLocale19setAttributeCountryERK7QString(
    DomLocale *self,
    const QString *a) {
  self->setAttributeCountry(*a);
}

//  void DomLocale::clearAttributeCountry()
extern "C" Q_DECL_EXPORT
void ritual_ZN9DomLocale21clearAttributeCountryEv(DomLocale *self) {
  self->clearAttributeCountry();
}
