//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qfontdatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qfontdatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QtFontFoundry::QtFontFoundry(const QString &n)
extern "C" Q_DECL_EXPORT
QtFontFoundry *ritual_ZN13QtFontFoundryC1ERK7QString(const QString *n) {
  return new QtFontFoundry(*n);
}

//  QtFontFoundry::~QtFontFoundry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QtFontFoundryD1Ev(QtFontFoundry *self) {
  delete self;
}

//  QtFontStyle *QtFontFoundry::style(const QtFontStyle::Key &a0, const
//      QString &a1, StyleRetrievalFlags flags)
extern "C" Q_DECL_EXPORT
QtFontStyle *ritual_ZN13QtFontFoundry5styleERKN11QtFontStyle3KeyERK7QStringNS_19StyleRetrievalFlagsE(
    QtFontFoundry *self,
    const QtFontStyle::Key *a0,
    const QString *a1,
    QtFontFoundry::StyleRetrievalFlags flags) {
  return self->style(*a0, *a1, flags);
}
