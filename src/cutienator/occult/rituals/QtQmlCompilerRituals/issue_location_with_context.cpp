//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljslogger_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstringview.h>
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljssourcelocation_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  IssueLocationWithContext::IssueLocationWithContext(QStringView code,
//      const QQmlJS::SourceLocation &location)
extern "C" Q_DECL_EXPORT
IssueLocationWithContext *ritual_ZN24IssueLocationWithContextC1E11QStringViewRKN6QQmlJS14SourceLocationE(
    const QString *code,
    const QQmlJS::SourceLocation *location) {
  return new IssueLocationWithContext(QStringView(*code), *location);
}

//  QStringView IssueLocationWithContext::beforeText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24IssueLocationWithContext10beforeTextEv(
    const IssueLocationWithContext *self) {
  return new QString(self->beforeText().toString());
}

//  QStringView IssueLocationWithContext::issueText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24IssueLocationWithContext9issueTextEv(
    const IssueLocationWithContext *self) {
  return new QString(self->issueText().toString());
}

//  QStringView IssueLocationWithContext::afterText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24IssueLocationWithContext9afterTextEv(
    const IssueLocationWithContext *self) {
  return new QString(self->afterText().toString());
}

//  IssueLocationWithContext::~IssueLocationWithContext()
extern "C" Q_DECL_EXPORT
void ritual_ZN24IssueLocationWithContextD1Ev(
    IssueLocationWithContext *self) {
  delete self;
}
