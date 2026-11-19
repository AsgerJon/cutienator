//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qlocale.h>

//  const QMetaObject *QValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QValidator10metaObjectEv(
    const QValidator *self) {
  return self->metaObject();
}

//  QString QValidator::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QValidator::tr(s, c, n));
}

//  QValidator::~QValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValidatorD1Ev(QValidator *self) {
  delete self;
}

//  void QValidator::setLocale(const QLocale &locale)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QValidator9setLocaleERK7QLocale(
    QValidator *self,
    const QLocale *locale) {
  self->setLocale(*locale);
}

//  QLocale QValidator::locale() const
extern "C" Q_DECL_EXPORT
QLocale *ritual_ZNK10QValidator6localeEv(const QValidator *self) {
  return new QLocale(self->locale());
}
