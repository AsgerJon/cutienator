//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4iterator_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4iterator_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4iterator_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4engine_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4iterator.cpp, line 10, as _ZN3QV417IteratorPrototype4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void IteratorPrototype::init(ExecutionEngine *engine)
{
    defineDefaultProperty(engine->symbol_iterator(), method_iterator, 0);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4iterator.cpp, line 15, as _ZN3QV417IteratorPrototype15method_iteratorEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue IteratorPrototype::method_iterator(const FunctionObject *, const Value *thisObject, const Value *, int)
{
    return thisObject->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4iterator.cpp, line 21, as _ZN3QV417IteratorPrototype22createIterResultObjectEPNS_15ExecutionEngineERKNS_5ValueEb
namespace QV4 {
inline ReturnedValue IteratorPrototype::createIterResultObject(ExecutionEngine *engine, const Value &value, bool done)
{
    Scope scope(engine);
    ScopedObject obj(scope, engine->newObject());
    obj->set(ScopedString(scope, engine->newString(QStringLiteral("value"))), value, Object::DoNotThrow);
    obj->set(ScopedString(scope, engine->newString(QStringLiteral("done"))), Value::fromBoolean(done), Object::DoNotThrow);
    return obj->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::IteratorPrototype::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV417IteratorPrototype4initEPNS_15ExecutionEngineE(
    QV4::IteratorPrototype *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}

//  ReturnedValue QV4::IteratorPrototype::method_iterator(const
//      FunctionObject *b, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417IteratorPrototype15method_iteratorEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *b,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::IteratorPrototype::method_iterator(b, thisObject, argv, argc);
}

//  ReturnedValue
//      QV4::IteratorPrototype::createIterResultObject(ExecutionEngine
//      *engine, const Value &value, bool done)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV417IteratorPrototype22createIterResultObjectEPNS_15ExecutionEngineERKNS_5ValueEb(
    QV4::ExecutionEngine *engine,
    const QV4::Value *value,
    bool done) {
  return QV4::IteratorPrototype::createIterResultObject(
      engine,
      *value,
      done);
}
