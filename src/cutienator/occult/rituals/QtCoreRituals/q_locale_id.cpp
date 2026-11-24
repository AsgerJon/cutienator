//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QLocaleId::operator==(QLocaleId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleIdeqES_(
    const QLocaleId *self,
    const QLocaleId *other) {
  return self->operator==(*other);
}

//  bool QLocaleId::operator!=(QLocaleId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleIdneES_(
    const QLocaleId *self,
    const QLocaleId *other) {
  return self->operator!=(*other);
}

//  bool QLocaleId::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleId7isValidEv(const QLocaleId *self) {
  return self->isValid();
}

//  bool QLocaleId::matchesAll() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleId10matchesAllEv(const QLocaleId *self) {
  return self->matchesAll();
}

//  bool QLocaleId::acceptLanguage(quint16 lang) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleId14acceptLanguageEt(
    const QLocaleId *self,
    quint16 lang) {
  return self->acceptLanguage(lang);
}

//  bool QLocaleId::acceptScriptTerritory(QLocaleId other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QLocaleId21acceptScriptTerritoryES_(
    const QLocaleId *self,
    const QLocaleId *other) {
  return self->acceptScriptTerritory(*other);
}

//  QLocaleId::~QLocaleId()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QLocaleIdD1Ev(QLocaleId *self) {
  delete self;
}
