//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::StringObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412StringObject10__dataTestEv(QV4::StringObject *self) {
  self->__dataTest();
}

//  QV4::Heap::StringObject *QV4::StringObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObject *ritual_ZNK3QV412StringObject11d_uncheckedEv(
    const QV4::StringObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::StringObject *QV4::StringObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::StringObject *ritual_ZNK3QV412StringObject1dEv(
    const QV4::StringObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::StringObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV412StringObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::StringObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::StringObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV412StringObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::StringObject::defaultPrototype(e);
}
