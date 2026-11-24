//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectproto_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectproto_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Heap::ArrayObject
//      *QV4::ObjectPrototype::getOwnPropertyNames(ExecutionEngine *v4, const
//      Value &o)
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayObject *ritual_ZN3QV415ObjectPrototype19getOwnPropertyNamesEPNS_15ExecutionEngineERKNS_5ValueE(
    QV4::ExecutionEngine *v4,
    const QV4::Value *o) {
  return QV4::ObjectPrototype::getOwnPropertyNames(v4, *o);
}
