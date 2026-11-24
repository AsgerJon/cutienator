//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QtFontFamily::QtFontFamily(const QString &n)
extern "C" Q_DECL_EXPORT
QtFontFamily *ritual_ZN12QtFontFamilyC1ERK7QString(const QString *n) {
  return new QtFontFamily(*n);
}

//  QtFontFamily::~QtFontFamily()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QtFontFamilyD1Ev(QtFontFamily *self) {
  delete self;
}

//  bool QtFontFamily::matchesFamilyName(const QString &familyName) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QtFontFamily17matchesFamilyNameERK7QString(
    const QtFontFamily *self,
    const QString *familyName) {
  return self->matchesFamilyName(*familyName);
}

//  QtFontFoundry *QtFontFamily::foundry(const QString &f, bool a1)
extern "C" Q_DECL_EXPORT
QtFontFoundry *ritual_ZN12QtFontFamily7foundryERK7QStringb(
    QtFontFamily *self,
    const QString *f,
    bool a1) {
  return self->foundry(*f, a1);
}

//  bool QtFontFamily::ensurePopulated()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QtFontFamily15ensurePopulatedEv(QtFontFamily *self) {
  return self->ensurePopulated();
}
