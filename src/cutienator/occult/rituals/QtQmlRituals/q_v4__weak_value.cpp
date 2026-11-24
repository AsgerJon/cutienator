//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::WeakValue::WeakValue()
extern "C" Q_DECL_EXPORT
QV4::WeakValue *ritual_ZN3QV49WeakValueC1Ev() {
  return new QV4::WeakValue();
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
