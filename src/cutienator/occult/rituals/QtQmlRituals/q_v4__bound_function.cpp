//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::BoundFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV413BoundFunction10__dataTestEv(QV4::BoundFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::BoundFunction *QV4::BoundFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunction *ritual_ZNK3QV413BoundFunction11d_uncheckedEv(
    const QV4::BoundFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::BoundFunction *QV4::BoundFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BoundFunction *ritual_ZNK3QV413BoundFunction1dEv(
    const QV4::BoundFunction *self) {
  return self->d();
}

//  Heap::FunctionObject *QV4::BoundFunction::target() const
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObject *ritual_ZNK3QV413BoundFunction6targetEv(
    const QV4::BoundFunction *self) {
  return self->target();
}

//  Value QV4::BoundFunction::boundThis() const
extern "C" Q_DECL_EXPORT
QV4::Value *ritual_ZNK3QV413BoundFunction9boundThisEv(
    const QV4::BoundFunction *self) {
  return new QV4::Value(self->boundThis());
}

//  Heap::MemberData *QV4::BoundFunction::boundArgs() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MemberData *ritual_ZNK3QV413BoundFunction9boundArgsEv(
    const QV4::BoundFunction *self) {
  return self->boundArgs();
}
