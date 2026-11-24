//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4compilercontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Compiler::Context::KeyValuePair::KeyValuePair()
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context::KeyValuePair *ritual_ZN3QV48Compiler7Context12KeyValuePairC1Ev() {
  return new QV4::Compiler::Context::KeyValuePair();
}

//  QV4::Compiler::Context::KeyValuePair::KeyValuePair(quint32 key, quint32
//      value)
extern "C" Q_DECL_EXPORT
QV4::Compiler::Context::KeyValuePair *ritual_ZN3QV48Compiler7Context12KeyValuePairC1Ejj(
    quint32 key,
    quint32 value) {
  return new QV4::Compiler::Context::KeyValuePair(key, value);
}

//  quint32 QV4::Compiler::Context::KeyValuePair::key() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV48Compiler7Context12KeyValuePair3keyEv(
    const QV4::Compiler::Context::KeyValuePair *self) {
  return self->key();
}

//  quint32 QV4::Compiler::Context::KeyValuePair::value() const
extern "C" Q_DECL_EXPORT
quint32 ritual_ZNK3QV48Compiler7Context12KeyValuePair5valueEv(
    const QV4::Compiler::Context::KeyValuePair *self) {
  return self->value();
}

//  QV4::Compiler::Context::KeyValuePair::~KeyValuePair()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Compiler7Context12KeyValuePairD1Ev(
    QV4::Compiler::Context::KeyValuePair *self) {
  delete self;
}
