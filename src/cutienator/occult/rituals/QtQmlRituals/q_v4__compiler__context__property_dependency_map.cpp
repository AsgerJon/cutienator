//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Compiler::Context::PropertyDependencyMap::insert(quint32 key,
//      quint32 value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context21PropertyDependencyMap6insertEjj(
    QV4::Compiler::Context::PropertyDependencyMap *self,
    quint32 key,
    quint32 value) {
  self->insert(key, value);
}

//  QV4::Compiler::Context::PropertyDependencyMap::~PropertyDependencyMap()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context21PropertyDependencyMapD1Ev(
    QV4::Compiler::Context::PropertyDependencyMap *self) {
  delete self;
}
