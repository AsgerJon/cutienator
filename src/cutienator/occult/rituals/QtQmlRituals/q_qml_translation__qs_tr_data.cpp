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

//  QQmlTranslation::QsTrData::QsTrData(const QString &fileNameForContext,
//      const QString &text, const QString &comment, int number)
extern "C" Q_DECL_EXPORT
QQmlTranslation::QsTrData *ritual_ZN15QQmlTranslation8QsTrDataC1ERK7QStringS3_S3_i(
    const QString *fileNameForContext,
    const QString *text,
    const QString *comment,
    int number) {
  return new QQmlTranslation::QsTrData(
      *fileNameForContext,
      *text,
      *comment,
      number);
}

//  QString QQmlTranslation::QsTrData::translate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QQmlTranslation8QsTrData9translateEv(
    const QQmlTranslation::QsTrData *self) {
  return new QString(self->translate());
}

//  QByteArray QQmlTranslation::QsTrData::context() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQmlTranslation8QsTrData7contextEv(
    const QQmlTranslation::QsTrData *self) {
  return new QByteArray(self->context());
}

//  QByteArray QQmlTranslation::QsTrData::text() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQmlTranslation8QsTrData4textEv(
    const QQmlTranslation::QsTrData *self) {
  return new QByteArray(self->text());
}

//  QByteArray QQmlTranslation::QsTrData::comment() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QQmlTranslation8QsTrData7commentEv(
    const QQmlTranslation::QsTrData *self) {
  return new QByteArray(self->comment());
}

//  int QQmlTranslation::QsTrData::number() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK15QQmlTranslation8QsTrData6numberEv(
    const QQmlTranslation::QsTrData *self) {
  return self->number();
}

//  QQmlTranslation::QsTrData::~QsTrData()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QQmlTranslation8QsTrDataD1Ev(
    QQmlTranslation::QsTrData *self) {
  delete self;
}
