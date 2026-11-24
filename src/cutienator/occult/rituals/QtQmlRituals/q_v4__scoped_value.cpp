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
