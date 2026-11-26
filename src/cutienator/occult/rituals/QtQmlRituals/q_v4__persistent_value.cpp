//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Edited by hand
//  on 2026-11-25: added by hand, instances of templates of the class: 5.
//  Kept as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::PersistentValue::PersistentValue()
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1Ev() {
  return new QV4::PersistentValue();
}

//  QV4::PersistentValue::PersistentValue(const PersistentValue &other)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1ERKS0_(
    const QV4::PersistentValue *other) {
  return new QV4::PersistentValue(*other);
}

//  PersistentValue &QV4::PersistentValue::operator=(const PersistentValue
//      &other)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueaSERKS0_(
    QV4::PersistentValue *self,
    const QV4::PersistentValue *other) {
  return &(self->operator=(*other));
}

//  QV4::PersistentValue::PersistentValue(PersistentValue &&other)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1EOS0_(
    QV4::PersistentValue *other) {
  return new QV4::PersistentValue(std::move(*other));
}

//  void QV4::PersistentValue::swap(PersistentValue &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValue4swapERS0_(
    QV4::PersistentValue *self,
    QV4::PersistentValue *other) {
  self->swap(*other);
}

//  PersistentValue &QV4::PersistentValue::operator=(PersistentValue &&other)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueaSEOS0_(
    QV4::PersistentValue *self,
    QV4::PersistentValue *other) {
  return &(self->operator=(std::move(*other)));
}

//  QV4::PersistentValue::~PersistentValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValueD1Ev(QV4::PersistentValue *self) {
  delete self;
}

//  PersistentValue &QV4::PersistentValue::operator=(const WeakValue &other)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueaSERKNS_9WeakValueE(
    QV4::PersistentValue *self,
    const QV4::WeakValue *other) {
  return &(self->operator=(*other));
}

//  PersistentValue &QV4::PersistentValue::operator=(Object *object)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueaSEPNS_6ObjectE(
    QV4::PersistentValue *self,
    QV4::Object *object) {
  return &(self->operator=(object));
}

//  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, const
//      Value &value)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  return new QV4::PersistentValue(engine, *value);
}

//  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine,
//      ReturnedValue value)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineEy(
    QV4::ExecutionEngine *engine,
    QV4::ReturnedValue value) {
  return new QV4::PersistentValue(engine, value);
}

//  QV4::PersistentValue::PersistentValue(ExecutionEngine *engine, Object
//      *object)
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1EPNS_15ExecutionEngineEPNS_6ObjectE(
    QV4::ExecutionEngine *engine,
    QV4::Object *object) {
  return new QV4::PersistentValue(engine, object);
}

//  void QV4::PersistentValue::set(ExecutionEngine *engine, const Value
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::PersistentValue *self,
    QV4::ExecutionEngine *engine,
    const QV4::Value *value) {
  self->set(engine, *value);
}

//  void QV4::PersistentValue::set(ExecutionEngine *engine, ReturnedValue
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineEy(
    QV4::PersistentValue *self,
    QV4::ExecutionEngine *engine,
    QV4::ReturnedValue value) {
  self->set(engine, value);
}

//  void QV4::PersistentValue::set(ExecutionEngine *engine, Heap::Base *obj)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValue3setEPNS_15ExecutionEngineEPNS_4Heap4BaseE(
    QV4::PersistentValue *self,
    QV4::ExecutionEngine *engine,
    QV4::Heap::Base *obj) {
  self->set(engine, obj);
}

//  ReturnedValue QV4::PersistentValue::value() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV415PersistentValue5valueEv(
    const QV4::PersistentValue *self) {
  return self->value();
}

//  Value *QV4::PersistentValue::valueRef() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV415PersistentValue8valueRefEv(
    const QV4::PersistentValue *self) {
  return self->valueRef();
}

//  Managed *QV4::PersistentValue::asManaged() const
extern "C" Q_DECL_EXPORT
QV4::Managed *ritual_ZNK3QV415PersistentValue9asManagedEv(
    const QV4::PersistentValue *self) {
  return self->asManaged();
}

//  ExecutionEngine *QV4::PersistentValue::engine() const
extern "C" Q_DECL_EXPORT
QV4::ExecutionEngine *ritual_ZNK3QV415PersistentValue6engineEv(
    const QV4::PersistentValue *self) {
  return self->engine();
}

//  bool QV4::PersistentValue::isUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415PersistentValue11isUndefinedEv(
    const QV4::PersistentValue *self) {
  return self->isUndefined();
}

//  bool QV4::PersistentValue::isNullOrUndefined() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV415PersistentValue17isNullOrUndefinedEv(
    const QV4::PersistentValue *self) {
  return self->isNullOrUndefined();
}

//  void QV4::PersistentValue::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValue5clearEv(QV4::PersistentValue *self) {
  self->clear();
}

//  bool QV4::PersistentValue::isEmpty()
extern "C" Q_DECL_EXPORT
bool ritual_ZN3QV415PersistentValue7isEmptyEv(QV4::PersistentValue *self) {
  return self->isEmpty();
}

#include <QtQml/6.12.0/QtQml/private/qv4object_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4string_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>

//  QV4::Object *QV4::PersistentValue::as<QV4::Object>() const
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZNK3QV415PersistentValue2asINS_6ObjectEEEPT_v(
    const QV4::PersistentValue *self) {
  return self->as<QV4::Object>();
}

//  QV4::FunctionObject *QV4::PersistentValue::as<QV4::FunctionObject>()
//      const
extern "C" Q_DECL_EXPORT
QV4::FunctionObject *ritual_ZNK3QV415PersistentValue2asINS_14FunctionObjectEEEPT_v(
    const QV4::PersistentValue *self) {
  return self->as<QV4::FunctionObject>();
}

//  QV4::String *QV4::PersistentValue::as<QV4::String>() const
extern "C" Q_DECL_EXPORT
QV4::String *ritual_ZNK3QV415PersistentValue2asINS_6StringEEEPT_v(
    const QV4::PersistentValue *self) {
  return self->as<QV4::String>();
}

//  QV4::ArrayObject *QV4::PersistentValue::as<QV4::ArrayObject>() const
extern "C" Q_DECL_EXPORT
QV4::ArrayObject *ritual_ZNK3QV415PersistentValue2asINS_11ArrayObjectEEEPT_v(
    const QV4::PersistentValue *self) {
  return self->as<QV4::ArrayObject>();
}

//  QV4::ErrorObject *QV4::PersistentValue::as<QV4::ErrorObject>() const
extern "C" Q_DECL_EXPORT
QV4::ErrorObject *ritual_ZNK3QV415PersistentValue2asINS_11ErrorObjectEEEPT_v(
    const QV4::PersistentValue *self) {
  return self->as<QV4::ErrorObject>();
}
