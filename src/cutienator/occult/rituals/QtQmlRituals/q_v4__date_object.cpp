//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dateobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dateobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::DateObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410DateObject10__dataTestEv(QV4::DateObject *self) {
  self->__dataTest();
}

//  QV4::Heap::DateObject *QV4::DateObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZNK3QV410DateObject11d_uncheckedEv(
    const QV4::DateObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DateObject *QV4::DateObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DateObject *ritual_ZNK3QV410DateObject1dEv(
    const QV4::DateObject *self) {
  return self->d();
}

//  QV4::Object *QV4::DateObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV410DateObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::DateObject::defaultPrototype(e);
}

//  double QV4::DateObject::date() const
extern "C" Q_DECL_EXPORT
double ritual_ZNK3QV410DateObject4dateEv(const QV4::DateObject *self) {
  return self->date();
}
