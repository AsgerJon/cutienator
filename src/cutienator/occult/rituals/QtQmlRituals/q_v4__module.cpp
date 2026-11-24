//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4module_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4module_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::Module::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV46Module12staticVTableEv() {
  return QV4::Module::staticVTable();
}

//  void QV4::Module::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV46Module10__dataTestEv(QV4::Module *self) {
  self->__dataTest();
}

//  QV4::Heap::Module *QV4::Module::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZNK3QV46Module11d_uncheckedEv(
    const QV4::Module *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Module *QV4::Module::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Module *ritual_ZNK3QV46Module1dEv(const QV4::Module *self) {
  return self->d();
}
