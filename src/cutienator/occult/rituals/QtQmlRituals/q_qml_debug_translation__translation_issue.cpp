//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/qtqmlglobal.h>
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#if QT_CONFIG(qml_debug)
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmldebugtranslationprotocol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  bool operator==(const TranslationIssue &first, const TranslationIssue
//      &second)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQmlDebugTranslationeqERKNS_16TranslationIssueES2_(
    const QQmlDebugTranslation::TranslationIssue *first,
    const QQmlDebugTranslation::TranslationIssue *second) {
  return operator==(*first, *second);
}

//  QString QQmlDebugTranslation::TranslationIssue::toDebugString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QQmlDebugTranslation16TranslationIssue13toDebugStringEv(
    const QQmlDebugTranslation::TranslationIssue *self) {
  return new QString(self->toDebugString());
}

//  QQmlDebugTranslation::TranslationIssue::~TranslationIssue()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQmlDebugTranslation16TranslationIssueD1Ev(
    QQmlDebugTranslation::TranslationIssue *self) {
  delete self;
}

#endif  // QT_CONFIG(qml_debug)
