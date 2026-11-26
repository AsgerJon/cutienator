//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine *engine,
//      QV4::String *name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14FunctionObject4initEPNS_15ExecutionEngineEPNS_6StringE(
    QV4::Heap::FunctionObject *self,
    QV4::ExecutionEngine *engine,
    QV4::String *name) {
  self->init(engine, name);
}

//  void QV4::Heap::FunctionObject::init(QV4::ExecutionEngine *engine, const
//      QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14FunctionObject4initEPNS_15ExecutionEngineERK7QString(
    QV4::Heap::FunctionObject *self,
    QV4::ExecutionEngine *engine,
    const QString *name) {
  self->init(engine, *name);
}

//  void QV4::Heap::FunctionObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14FunctionObject4initEv(
    QV4::Heap::FunctionObject *self) {
  self->init();
}

//  QV4::Heap::FunctionObject as the QV4::Heap::FunctionObjectData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::FunctionObjectData *ritual_cast_QV4_Heap_FunctionObject_QV4_Heap_FunctionObjectData(
    QV4::Heap::FunctionObject *self) {
  return static_cast<QV4::Heap::FunctionObjectData *>(self);
}
