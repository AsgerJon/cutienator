//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::ScopedValue::ScopedValue(const ScopedValue &a0)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKS0_(
    const QV4::ScopedValue *a0) {
  return new QV4::ScopedValue(*a0);
}

//  QV4::ScopedValue::ScopedValue(ScopedValue &&a0)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1EOS0_(QV4::ScopedValue *a0) {
  return new QV4::ScopedValue(std::move(*a0));
}

//  QV4::ScopedValue::ScopedValue(const Scope &scope)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKNS_5ScopeE(
    const QV4::Scope *scope) {
  return new QV4::ScopedValue(*scope);
}

//  QV4::ScopedValue::ScopedValue(const Scope &scope, const Value &v)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKNS_5ScopeERKNS_5ValueE(
    const QV4::Scope *scope,
    const QV4::Value *v) {
  return new QV4::ScopedValue(*scope, *v);
}

//  QV4::ScopedValue::ScopedValue(const Scope &scope, Heap::Base *o)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKNS_5ScopeEPNS_4Heap4BaseE(
    const QV4::Scope *scope,
    QV4::Heap::Base *o) {
  return new QV4::ScopedValue(*scope, o);
}

//  QV4::ScopedValue::ScopedValue(const Scope &scope, Managed *m)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKNS_5ScopeEPNS_7ManagedE(
    const QV4::Scope *scope,
    QV4::Managed *m) {
  return new QV4::ScopedValue(*scope, m);
}

//  QV4::ScopedValue::ScopedValue(const Scope &scope, const ReturnedValue &v)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueC1ERKNS_5ScopeERKy(
    const QV4::Scope *scope,
    QV4::ReturnedValue v) {
  return new QV4::ScopedValue(*scope, v);
}

//  ScopedValue &QV4::ScopedValue::operator=(const Value &v)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueaSERKNS_5ValueE(
    QV4::ScopedValue *self,
    const QV4::Value *v) {
  return &(self->operator=(*v));
}

//  ScopedValue &QV4::ScopedValue::operator=(Heap::Base *o)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueaSEPNS_4Heap4BaseE(
    QV4::ScopedValue *self,
    QV4::Heap::Base *o) {
  return &(self->operator=(o));
}

//  ScopedValue &QV4::ScopedValue::operator=(Managed *m)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueaSEPNS_7ManagedE(
    QV4::ScopedValue *self,
    QV4::Managed *m) {
  return &(self->operator=(m));
}

//  ScopedValue &QV4::ScopedValue::operator=(const ReturnedValue &v)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueaSERKy(
    QV4::ScopedValue *self,
    QV4::ReturnedValue v) {
  return &(self->operator=(v));
}

//  ScopedValue &QV4::ScopedValue::operator=(const ScopedValue &other)
extern "C" Q_DECL_EXPORT
QV4::ScopedValue *ritual_ZN3QV411ScopedValueaSERKS0_(
    QV4::ScopedValue *self,
    const QV4::ScopedValue *other) {
  return &(self->operator=(*other));
}

//  Value *QV4::ScopedValue::operator->()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV411ScopedValueptEv(QV4::ScopedValue *self) {
  return self->operator->();
}

//  const Value *QV4::ScopedValue::operator->() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV411ScopedValueptEv(
    const QV4::ScopedValue *self) {
  return self->operator->();
}

//  Value *QV4::ScopedValue::operator QV4::Value *()
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZN3QV411ScopedValuecvPNS_5ValueEEv(
    QV4::ScopedValue *self) {
  return self->operator QV4::Value *();
}

//  const Value &QV4::ScopedValue::operator const QV4::Value &() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV411ScopedValuecvRKNS_5ValueEEv(
    const QV4::ScopedValue *self) {
  return new QV4::Value(self->operator const QV4::Value &());
}

//  QV4::ScopedValue::~ScopedValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ScopedValueD1Ev(QV4::ScopedValue *self) {
  delete self;
}
