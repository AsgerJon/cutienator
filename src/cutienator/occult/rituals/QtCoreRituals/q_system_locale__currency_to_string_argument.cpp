//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qlocale_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qlocale_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>

//  QSystemLocale::CurrencyToStringArgument::CurrencyToStringArgument()
extern "C" Q_DECL_EXPORT
QSystemLocale::CurrencyToStringArgument *ritual_ZN13QSystemLocale24CurrencyToStringArgumentC1Ev() {
  return new QSystemLocale::CurrencyToStringArgument();
}

//  QSystemLocale::CurrencyToStringArgument::CurrencyToStringArgument(const
//      QVariant &v, const QString &s)
extern "C" Q_DECL_EXPORT
QSystemLocale::CurrencyToStringArgument *ritual_ZN13QSystemLocale24CurrencyToStringArgumentC1ERK8QVariantRK7QString(
    const QVariant *v,
    const QString *s) {
  return new QSystemLocale::CurrencyToStringArgument(*v, *s);
}

//  QSystemLocale::CurrencyToStringArgument::~CurrencyToStringArgument()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSystemLocale24CurrencyToStringArgumentD1Ev(
    QSystemLocale::CurrencyToStringArgument *self) {
  delete self;
}
