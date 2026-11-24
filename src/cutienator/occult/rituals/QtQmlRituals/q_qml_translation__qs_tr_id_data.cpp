//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltranslation_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltranslation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QQmlTranslation::QsTrIdData::QsTrIdData(const QString &id, int number)
extern "C" Q_DECL_EXPORT
QQmlTranslation::QsTrIdData *ritual_ZN15QQmlTranslation10QsTrIdDataC1ERK7QStringi(
    const QString *id,
    int number) {
  return new QQmlTranslation::QsTrIdData(*id, number);
}

//  QString QQmlTranslation::QsTrIdData::translate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlTranslation10QsTrIdData9translateEv(
    const QQmlTranslation::QsTrIdData *self) {
  return new QString(self->translate());
}

//  QByteArray QQmlTranslation::QsTrIdData::id() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQmlTranslation10QsTrIdData2idEv(
    const QQmlTranslation::QsTrIdData *self) {
  return new QByteArray(self->id());
}

//  int QQmlTranslation::QsTrIdData::number() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlTranslation10QsTrIdData6numberEv(
    const QQmlTranslation::QsTrIdData *self) {
  return self->number();
}

//  QQmlTranslation::QsTrIdData::~QsTrIdData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTranslation10QsTrIdDataD1Ev(
    QQmlTranslation::QsTrIdData *self) {
  delete self;
}
