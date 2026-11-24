//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4persistent_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4persistent_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::PersistentValue::PersistentValue()
extern "C" Q_DECL_EXPORT
QV4::PersistentValue *ritual_ZN3QV415PersistentValueC1Ev() {
  return new QV4::PersistentValue();
}

//  QV4::PersistentValue::~PersistentValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415PersistentValueD1Ev(QV4::PersistentValue *self) {
  delete self;
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
