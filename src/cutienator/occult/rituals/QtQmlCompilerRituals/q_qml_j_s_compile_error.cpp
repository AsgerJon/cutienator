//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtQmlCompiler/QtQmlCompiler>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlCompiler/6.12.0/QtQmlCompiler/private/qqmljscompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmljsdiagnosticmessage_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QQmlJSCompileError::print()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSCompileError5printEv(QQmlJSCompileError *self) {
  self->print();
}

//  QQmlJSCompileError QQmlJSCompileError::augment(const QString
//      &contextErrorMessage) const
extern "C" Q_DECL_EXPORT
QQmlJSCompileError *ritual_ZNK18QQmlJSCompileError7augmentERK7QString(
    const QQmlJSCompileError *self,
    const QString *contextErrorMessage) {
  return new QQmlJSCompileError(self->augment(*contextErrorMessage));
}

//  void QQmlJSCompileError::appendDiagnostic(const QString &inputFileName,
//      const QQmlJS::DiagnosticMessage &diagnostic)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSCompileError16appendDiagnosticERK7QStringRKN6QQmlJS17DiagnosticMessageE(
    QQmlJSCompileError *self,
    const QString *inputFileName,
    const QQmlJS::DiagnosticMessage *diagnostic) {
  self->appendDiagnostic(*inputFileName, *diagnostic);
}

//  QQmlJSCompileError::~QQmlJSCompileError()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQmlJSCompileErrorD1Ev(QQmlJSCompileError *self) {
  delete self;
}
