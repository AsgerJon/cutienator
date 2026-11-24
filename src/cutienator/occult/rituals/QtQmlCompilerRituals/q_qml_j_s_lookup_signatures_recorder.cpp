//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslookupsignatures_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslookupsignatures_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QQmlJSLookupSignaturesRecorder::QQmlJSLookupSignaturesRecorder(const
//      QString &currentFilePath, const QQmlJSTypeResolver *typeResolver)
extern "C" Q_DECL_EXPORT
QQmlJSLookupSignaturesRecorder *ritual_ZN30QQmlJSLookupSignaturesRecorderC1ERK7QStringPK18QQmlJSTypeResolver(
    const QString *currentFilePath,
    const QQmlJSTypeResolver *typeResolver) {
  return new QQmlJSLookupSignaturesRecorder(*currentFilePath, typeResolver);
}

//  QString QQmlJSLookupSignaturesRecorder::rejectMessage()
extern "C" Q_DECL_EXPORT
QString *ritual_ZN30QQmlJSLookupSignaturesRecorder13rejectMessageEv(
    QQmlJSLookupSignaturesRecorder *self) {
  return new QString(self->rejectMessage());
}

//  QQmlJSLookupSignaturesRecorder::~QQmlJSLookupSignaturesRecorder()
extern "C" Q_DECL_EXPORT
void ritual_ZN30QQmlJSLookupSignaturesRecorderD1Ev(
    QQmlJSLookupSignaturesRecorder *self) {
  delete self;
}
