//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Object *QV4::TypeErrorObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV415TypeErrorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::TypeErrorObject::defaultPrototype(e);
}

//  const Data *QV4::TypeErrorObject::d() const
extern "C" Q_DECL_EXPORT
const QV4::TypeErrorObject::Data *ritual_ZNK3QV415TypeErrorObject1dEv(
    const QV4::TypeErrorObject *self) {
  return self->d();
}

//  Data *QV4::TypeErrorObject::d()
extern "C" Q_DECL_EXPORT
QV4::TypeErrorObject::Data *ritual_ZN3QV415TypeErrorObject1dEv(
    QV4::TypeErrorObject *self) {
  return self->d();
}
