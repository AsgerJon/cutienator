//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QV4::Object *QV4::URIErrorObject::defaultPrototype(QV4::ExecutionEngine
//      *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV414URIErrorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::URIErrorObject::defaultPrototype(e);
}

//  const Data *QV4::URIErrorObject::d() const
extern "C" Q_DECL_EXPORT
const QV4::URIErrorObject::Data *ritual_ZNK3QV414URIErrorObject1dEv(
    const QV4::URIErrorObject *self) {
  return self->d();
}

//  Data *QV4::URIErrorObject::d()
extern "C" Q_DECL_EXPORT
QV4::URIErrorObject::Data *ritual_ZN3QV414URIErrorObject1dEv(
    QV4::URIErrorObject *self) {
  return self->d();
}
