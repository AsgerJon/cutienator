//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4lookup_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4lookup_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::Lookup::markObjects(MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Lookup11markObjectsEPNS_9MarkStackE(
    QV4::Lookup *self,
    QV4::MarkStack *stack) {
  self->markObjects(stack);
}

//  ReturnedValue QV4::Lookup::contextGetter(ExecutionEngine *engine, Value
//      *base)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup13contextGetterEPNS_15ExecutionEngineEPNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    QV4::Value *base) {
  return self->contextGetter(engine, base);
}

//  ReturnedValue QV4::Lookup::doCallGlobal(Call call, Lookup *lookup,
//      ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup12doCallGlobalENS0_4CallEPS0_PNS_15ExecutionEngineE(
    QV4::Lookup::Call call,
    QV4::Lookup *lookup,
    QV4::ExecutionEngine *engine) {
  return QV4::Lookup::doCallGlobal(call, lookup, engine);
}

//  ReturnedValue QV4::Lookup::globalGetter(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup12globalGetterEPNS_15ExecutionEngineE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine) {
  return self->globalGetter(engine);
}

//  ReturnedValue QV4::Lookup::getter(ExecutionEngine *engine, const Value
//      &object)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV46Lookup6getterEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::Lookup *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *object) {
  return self->getter(engine, *object);
}

//  void QV4::Lookup::releasePropertyCache()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Lookup20releasePropertyCacheEv(QV4::Lookup *self) {
  self->releasePropertyCache();
}

//  QV4::Lookup::~Lookup()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46LookupD1Ev(QV4::Lookup *self) {
  delete self;
}
