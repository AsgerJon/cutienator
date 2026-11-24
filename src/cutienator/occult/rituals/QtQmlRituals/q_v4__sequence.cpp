//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4sequenceobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  const QV4::VTable *QV4::Sequence::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV48Sequence12staticVTableEv() {
  return QV4::Sequence::staticVTable();
}

//  void QV4::Sequence::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV48Sequence10__dataTestEv(QV4::Sequence *self) {
  self->__dataTest();
}

//  QV4::Heap::Sequence *QV4::Sequence::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Sequence *ritual_ZNK3QV48Sequence11d_uncheckedEv(
    const QV4::Sequence *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Sequence *QV4::Sequence::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Sequence *ritual_ZNK3QV48Sequence1dEv(const QV4::Sequence *self) {
  return self->d();
}

//  QV4::Object *QV4::Sequence::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV48Sequence16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::Sequence::defaultPrototype(e);
}
