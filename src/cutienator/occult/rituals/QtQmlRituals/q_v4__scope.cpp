//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Scope::Scope(ExecutionContext *ctx)
extern "C" Q_DECL_EXPORT
QV4::Scope *ritual_ZN3QV45ScopeC1EPNS_16ExecutionContextE(
    QV4::ExecutionContext *ctx) {
  return new QV4::Scope(ctx);
}

//  QV4::Scope::Scope(ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Scope *ritual_ZN3QV45ScopeC1EPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return new QV4::Scope(e);
}

//  QV4::Scope::Scope(const Managed *m)
extern "C" Q_DECL_EXPORT
QV4::Scope *ritual_ZN3QV45ScopeC1EPKNS_7ManagedE(const QV4::Managed *m) {
  return new QV4::Scope(m);
}

//  QV4::Scope::~Scope()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV45ScopeD1Ev(QV4::Scope *self) {
  delete self;
}

//  Value *QV4::Scope::construct(int nValues, const ReturnedValue
//      &initialValue) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV45Scope9constructEiRKy(
    const QV4::Scope *self,
    int nValues,
    QV4::ReturnedValue initialValue) {
  return self->construct(nValues, initialValue);
}

//  Value *QV4::Scope::construct(int nValues, const Value &initialValue)
//      const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV45Scope9constructEiRKNS_5ValueE(
    const QV4::Scope *self,
    int nValues,
    const QV4::Value *initialValue) {
  return self->construct(nValues, *initialValue);
}

//  Value *QV4::Scope::construct(int nValues, Heap::Base *initialValue) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV45Scope9constructEiPNS_4Heap4BaseE(
    const QV4::Scope *self,
    int nValues,
    QV4::Heap::Base *initialValue) {
  return self->construct(nValues, initialValue);
}

//  PropertyKey *QV4::Scope::construct(int nValues, const PropertyKey
//      &initialValue) const
extern "C" Q_DECL_EXPORT
QV4::PropertyKey *ritual_ZNK3QV45Scope9constructEiRKNS_11PropertyKeyE(
    const QV4::Scope *self,
    int nValues,
    const QV4::PropertyKey *initialValue) {
  return self->construct(nValues, *initialValue);
}

//  Value *QV4::Scope::constructUndefined(int nValues) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV45Scope18constructUndefinedEi(
    const QV4::Scope *self,
    int nValues) {
  return self->constructUndefined(nValues);
}

//  bool QV4::Scope::hasException() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV45Scope12hasExceptionEv(const QV4::Scope *self) {
  return self->hasException();
}

//  Value *QV4::Scope::alloc(int nValues) const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV45Scope5allocEi(
    const QV4::Scope *self,
    int nValues) {
  return self->alloc(nValues);
}
