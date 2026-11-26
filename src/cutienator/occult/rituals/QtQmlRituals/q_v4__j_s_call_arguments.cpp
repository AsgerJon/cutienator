//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4jscall_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::JSCallArguments::JSCallArguments(const Scope &scope, int argc)
extern "C" Q_DECL_EXPORT
QV4::JSCallArguments *ritual_ZN3QV415JSCallArgumentsC1ERKNS_5ScopeEi(
    const QV4::Scope *scope,
    int argc) {
  return new QV4::JSCallArguments(*scope, argc);
}

//  CallData *QV4::JSCallArguments::callData(const Scope &scope, const
//      FunctionObject *f) const
extern "C" Q_DECL_EXPORT
QV4::CallData *ritual_ZNK3QV415JSCallArguments8callDataERKNS_5ScopeEPKNS_14FunctionObjectE(
    const QV4::JSCallArguments *self,
    const QV4::Scope *scope,
    const QV4::FunctionObject *f) {
  return self->callData(*scope, f);
}

//  QV4::JSCallArguments::~JSCallArguments()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415JSCallArgumentsD1Ev(QV4::JSCallArguments *self) {
  delete self;
}
