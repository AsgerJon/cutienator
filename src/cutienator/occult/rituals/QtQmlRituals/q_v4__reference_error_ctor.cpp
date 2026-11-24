//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::ReferenceErrorCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418ReferenceErrorCtor10__dataTestEv(
    QV4::ReferenceErrorCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::ReferenceErrorCtor *QV4::ReferenceErrorCtor::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceErrorCtor *ritual_ZNK3QV418ReferenceErrorCtor11d_uncheckedEv(
    const QV4::ReferenceErrorCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ReferenceErrorCtor *QV4::ReferenceErrorCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ReferenceErrorCtor *ritual_ZNK3QV418ReferenceErrorCtor1dEv(
    const QV4::ReferenceErrorCtor *self) {
  return self->d();
}

//  QV4::Object
//      *QV4::ReferenceErrorCtor::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV418ReferenceErrorCtor16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ReferenceErrorCtor::defaultPrototype(e);
}
