//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4script_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4script_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QV4::Script::Script(ExecutionContext *scope, QV4::Compiler::ContextType
//      mode, const QString &sourceCode, const QString &source, int line)
extern "C" Q_DECL_EXPORT
QV4::Script *ritual_ZN3QV46ScriptC1EPNS_16ExecutionContextENS_8Compiler11ContextTypeERK7QStringS7_i(
    QV4::ExecutionContext *scope,
    QV4::Compiler::ContextType mode,
    const QString *sourceCode,
    const QString *source,
    int line) {
  return new QV4::Script(scope, mode, *sourceCode, *source, line);
}

//  QV4::Script::Script(ExecutionEngine *engine, QmlContext *qml, bool
//      parseAsBinding, const QString &sourceCode, const QString &source, int
//      line)
extern "C" Q_DECL_EXPORT
QV4::Script *ritual_ZN3QV46ScriptC1EPNS_15ExecutionEngineEPNS_10QmlContextEbRK7QStringS7_i(
    QV4::ExecutionEngine *engine,
    QV4::QmlContext *qml,
    bool parseAsBinding,
    const QString *sourceCode,
    const QString *source,
    int line) {
  return new QV4::Script(
      engine,
      qml,
      parseAsBinding,
      *sourceCode,
      *source,
      line);
}

//  void QV4::Script::setStrictMode(bool strictMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script13setStrictModeEb(
    QV4::Script *self,
    bool strictMode) {
  self->setStrictMode(strictMode);
}

//  void QV4::Script::setInheritContext(bool inheritContext)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script17setInheritContextEb(
    QV4::Script *self,
    bool inheritContext) {
  self->setInheritContext(inheritContext);
}

//  void QV4::Script::setParseAsBinding(bool parseAsBinding)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Script17setParseAsBindingEb(
    QV4::Script *self,
    bool parseAsBinding) {
  self->setParseAsBinding(parseAsBinding);
}
