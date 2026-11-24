//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QV4::MapObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49MapObject10__dataTestEv(QV4::MapObject *self) {
  self->__dataTest();
}

//  QV4::Heap::MapObject *QV4::MapObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapObject *ritual_ZNK3QV49MapObject11d_uncheckedEv(
    const QV4::MapObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::MapObject *QV4::MapObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::MapObject *ritual_ZNK3QV49MapObject1dEv(
    const QV4::MapObject *self) {
  return self->d();
}

//  QV4::Object *QV4::MapObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV49MapObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::MapObject::defaultPrototype(e);
}
