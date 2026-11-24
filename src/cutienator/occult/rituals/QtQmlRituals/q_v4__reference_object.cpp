//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4referenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ReferenceObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ReferenceObject10__dataTestEv(
    QV4::ReferenceObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObject *ritual_ZNK3QV415ReferenceObject11d_uncheckedEv(
    const QV4::ReferenceObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ReferenceObject *QV4::ReferenceObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceObject *ritual_ZNK3QV415ReferenceObject1dEv(
    const QV4::ReferenceObject *self) {
  return self->d();
}

//  void QV4::ReferenceObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415ReferenceObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ReferenceObject::virtualDestroy(b);
}
