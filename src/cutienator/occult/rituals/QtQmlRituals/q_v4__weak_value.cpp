//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 5.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4qobjectwrapper_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::WeakValue::WeakValue()
extern "C" Q_DECL_EXPORT
QV4::WeakValue *ritual_ZN3QV49WeakValueC1Ev() {
  return new QV4::WeakValue();
}

//  QV4::WeakValue::WeakValue(const WeakValue &other)
extern "C" Q_DECL_EXPORT
QV4::WeakValue *ritual_ZN3QV49WeakValueC1ERKS0_(
    const QV4::WeakValue *other) {
  return new QV4::WeakValue(*other);
}

//  QV4::WeakValue::WeakValue(ExecutionEngine *engine, const Value &value)
extern "C" Q_DECL_EXPORT
QV4::WeakValue *ritual_ZN3QV49WeakValueC1EPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  return new QV4::WeakValue(engine, *value);
}

//  WeakValue &QV4::WeakValue::operator=(const WeakValue &other)
extern "C" Q_DECL_EXPORT
QV4::WeakValue *ritual_ZN3QV49WeakValueaSERKS0_(
    QV4::WeakValue *self,
    const QV4::WeakValue *other) {
  return &(self->operator=(*other));
}

//  QV4::WeakValue::~WeakValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValueD1Ev(QV4::WeakValue *self) {
  delete self;
}

//  void QV4::WeakValue::set(ExecutionEngine *engine, const Value &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::WeakValue *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  self->set(engine, *value);
}

//  void QV4::WeakValue::set(ExecutionEngine *engine, ReturnedValue value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineEy(
    QV4::WeakValue *self,
    QV4::ExecutionEngine *engine,
    QV4::ReturnedValue value) {
  self->set(engine, value);
}

//  void QV4::WeakValue::set(ExecutionEngine *engine, Heap::Base *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue3setEPNS_15ExecutionEngineEPNS_4Heap4BaseE(
    QV4::WeakValue *self,
    QV4::ExecutionEngine *engine,
    QV4::Heap::Base *obj) {
  self->set(engine, obj);
}

//  ReturnedValue QV4::WeakValue::value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV49WeakValue5valueEv(
    const QV4::WeakValue *self) {
  return self->value();
}

//  Value *QV4::WeakValue::valueRef() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV49WeakValue8valueRefEv(const QV4::WeakValue *self) {
  return self->valueRef();
}

//  Managed *QV4::WeakValue::asManaged() const
extern "C" Q_DECL_EXPORT
QV4::Managed *ritual_ZNK3QV49WeakValue9asManagedEv(
    const QV4::WeakValue *self) {
  return self->asManaged();
}

//  ExecutionEngine *QV4::WeakValue::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK3QV49WeakValue6engineEv(
    const QV4::WeakValue *self) {
  return self->engine();
}

//  bool QV4::WeakValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49WeakValue11isUndefinedEv(const QV4::WeakValue *self) {
  return self->isUndefined();
}

//  bool QV4::WeakValue::isNullOrUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV49WeakValue17isNullOrUndefinedEv(
    const QV4::WeakValue *self) {
  return self->isNullOrUndefined();
}

//  void QV4::WeakValue::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue5clearEv(QV4::WeakValue *self) {
  self->clear();
}

//  void QV4::WeakValue::markOnce(MarkStack *markStack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue8markOnceEPNS_9MarkStackE(
    QV4::WeakValue *self,
    QV4::MarkStack *markStack) {
  self->markOnce(markStack);
}

//  void QV4::WeakValue::allocVal(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue8allocValEPNS_15ExecutionEngineE(
    QV4::WeakValue *self,
    QV4::ExecutionEngine *engine) {
  self->allocVal(engine);
}

//  void QV4::WeakValue::free()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49WeakValue4freeEv(QV4::WeakValue *self) {
  self->free();
}

//  QV4::Object *QV4::WeakValue::as<QV4::Object>() const
extern "C" Q_DECL_EXPORT
QV4::Object * ritual_ZNK3QV49WeakValue2asINS_6ObjectEEEPT_v(
    const QV4::WeakValue *self) {
  return self->as<QV4::Object>();
}

//  QV4::String *QV4::WeakValue::as<QV4::String>() const
extern "C" Q_DECL_EXPORT
QV4::String * ritual_ZNK3QV49WeakValue2asINS_6StringEEEPT_v(
    const QV4::WeakValue *self) {
  return self->as<QV4::String>();
}

//  QV4::FunctionObject *QV4::WeakValue::as<QV4::FunctionObject>() const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject * ritual_ZNK3QV49WeakValue2asINS_14FunctionObjectEEEPT_v(
    const QV4::WeakValue *self) {
  return self->as<QV4::FunctionObject>();
}

//  QV4::ArrayObject *QV4::WeakValue::as<QV4::ArrayObject>() const
extern "C" Q_DECL_EXPORT
QV4::ArrayObject * ritual_ZNK3QV49WeakValue2asINS_11ArrayObjectEEEPT_v(
    const QV4::WeakValue *self) {
  return self->as<QV4::ArrayObject>();
}

//  QV4::QObjectWrapper *QV4::WeakValue::as<QV4::QObjectWrapper>() const
extern "C" Q_DECL_EXPORT
QV4::QObjectWrapper * ritual_ZNK3QV49WeakValue2asINS_14QObjectWrapperEEEPT_v(
    const QV4::WeakValue *self) {
  return self->as<QV4::QObjectWrapper>();
}
