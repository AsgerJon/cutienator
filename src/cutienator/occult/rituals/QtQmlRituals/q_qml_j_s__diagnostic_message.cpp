//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool QQmlJS::DiagnosticMessage::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS17DiagnosticMessage7isErrorEv(
    const QQmlJS::DiagnosticMessage *self) {
  return self->isError();
}

//  bool QQmlJS::DiagnosticMessage::isWarning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK6QQmlJS17DiagnosticMessage9isWarningEv(
    const QQmlJS::DiagnosticMessage *self) {
  return self->isWarning();
}

//  QQmlJS::DiagnosticMessage::~DiagnosticMessage()
extern "C" Q_DECL_EXPORT
void ritual_ZN6QQmlJS17DiagnosticMessageD1Ev(
    QQmlJS::DiagnosticMessage *self) {
  delete self;
}
