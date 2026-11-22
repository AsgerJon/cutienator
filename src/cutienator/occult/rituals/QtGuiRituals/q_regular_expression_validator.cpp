//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qvalidator.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qvalidator.h>
#include <QtCore/qstring.h>
#include <QtCore/qregularexpression.h>

//  const QMetaObject *QRegularExpressionValidator::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK27QRegularExpressionValidator10metaObjectEv(
    const QRegularExpressionValidator *self) {
  return self->metaObject();
}

//  QString QRegularExpressionValidator::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN27QRegularExpressionValidator2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRegularExpressionValidator::tr(s, c, n));
}

//  QRegularExpressionValidator::QRegularExpressionValidator(QObject *parent)
extern "C" Q_DECL_EXPORT
QRegularExpressionValidator *ritual_ZN27QRegularExpressionValidatorC1EP7QObject(
    QObject *parent) {
  return new QRegularExpressionValidator(parent);
}

//  QRegularExpressionValidator::QRegularExpressionValidator(const
//      QRegularExpression &re, QObject *parent)
extern "C" Q_DECL_EXPORT
QRegularExpressionValidator *ritual_ZN27QRegularExpressionValidatorC1ERK18QRegularExpressionP7QObject(
    const QRegularExpression *re,
    QObject *parent) {
  return new QRegularExpressionValidator(*re, parent);
}

//  QRegularExpressionValidator::~QRegularExpressionValidator()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRegularExpressionValidatorD1Ev(
    QRegularExpressionValidator *self) {
  delete self;
}

//  QRegularExpression QRegularExpressionValidator::regularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK27QRegularExpressionValidator17regularExpressionEv(
    const QRegularExpressionValidator *self) {
  return new QRegularExpression(self->regularExpression());
}

//  void QRegularExpressionValidator::setRegularExpression(const
//      QRegularExpression &re)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QRegularExpressionValidator20setRegularExpressionERK18QRegularExpression(
    QRegularExpressionValidator *self,
    const QRegularExpression *re) {
  self->setRegularExpression(*re);
}
