//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltranslation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltranslation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlTranslation::QQmlTranslation(const Data &d)
extern "C" Q_DECL_EXPORT
QQmlTranslation *ritual_ZN15QQmlTranslationC1ERKSt7variantIJDnNS_8QsTrDataENS_10QsTrIdDataEEE(
    const QQmlTranslation::Data *d) {
  return new QQmlTranslation(*d);
}

//  QQmlTranslation::QQmlTranslation()
extern "C" Q_DECL_EXPORT
QQmlTranslation *ritual_ZN15QQmlTranslationC1Ev() {
  return new QQmlTranslation();
}

//  QString QQmlTranslation::translate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlTranslation9translateEv(
    const QQmlTranslation *self) {
  return new QString(self->translate());
}

//  QString QQmlTranslation::contextFromQmlFilename(const QString
//      &qmlFilename)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QQmlTranslation22contextFromQmlFilenameERK7QString(
    const QString *qmlFilename) {
  return new QString(QQmlTranslation::contextFromQmlFilename(*qmlFilename));
}

//  QQmlTranslation::~QQmlTranslation()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTranslationD1Ev(QQmlTranslation *self) {
  delete self;
}
