//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::IndexedBuiltinFunction::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV422IndexedBuiltinFunction12staticVTableEv() {
  return QV4::IndexedBuiltinFunction::staticVTable();
}

//  void QV4::IndexedBuiltinFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV422IndexedBuiltinFunction10__dataTestEv(
    QV4::IndexedBuiltinFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::IndexedBuiltinFunction
//      *QV4::IndexedBuiltinFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IndexedBuiltinFunction *ritual_ZNK3QV422IndexedBuiltinFunction11d_uncheckedEv(
    const QV4::IndexedBuiltinFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::IndexedBuiltinFunction *QV4::IndexedBuiltinFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::IndexedBuiltinFunction *ritual_ZNK3QV422IndexedBuiltinFunction1dEv(
    const QV4::IndexedBuiltinFunction *self) {
  return self->d();
}
