//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4value_p.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::OptionalReturnedValue::OptionalReturnedValue()
extern "C" Q_DECL_EXPORT
QV4::OptionalReturnedValue *ritual_ZN3QV421OptionalReturnedValueC1Ev() {
  return new QV4::OptionalReturnedValue();
}

//  QV4::OptionalReturnedValue::OptionalReturnedValue(ReturnedValue v)
extern "C" Q_DECL_EXPORT
QV4::OptionalReturnedValue *ritual_ZN3QV421OptionalReturnedValueC1Ey(
    QV4::ReturnedValue v) {
  return new QV4::OptionalReturnedValue(v);
}

//  ReturnedValue QV4::OptionalReturnedValue::operator->() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV421OptionalReturnedValueptEv(
    const QV4::OptionalReturnedValue *self) {
  return self->operator->();
}

//  ReturnedValue QV4::OptionalReturnedValue::operator*() const
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZNK3QV421OptionalReturnedValuedeEv(
    const QV4::OptionalReturnedValue *self) {
  return self->operator*();
}

//  bool QV4::OptionalReturnedValue::operator bool() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK3QV421OptionalReturnedValuecvbEv(
    const QV4::OptionalReturnedValue *self) {
  return self->operator bool();
}

//  QV4::OptionalReturnedValue::~OptionalReturnedValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421OptionalReturnedValueD1Ev(
    QV4::OptionalReturnedValue *self) {
  delete self;
}
