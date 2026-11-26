//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4booleanobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4booleanobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4booleanobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4booleanobject.cpp, line 17, as _ZN3QV411BooleanCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue BooleanCtor::virtualCallAsConstructor(const FunctionObject *that, const Value *argv, int argc, const Value *newTarget)
{
    auto v4 = that->engine();
    bool n = argc ? argv[0].toBoolean() : false;

    ReturnedValue o = Encode(v4->newBooleanObject(n));
    if (!newTarget)
        return o;
    Scope scope(v4);
    ScopedObject obj(scope, o);
    obj->setProtoFromNewTarget(newTarget);
    return obj->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4booleanobject.cpp, line 31, as _ZN3QV411BooleanCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue BooleanCtor::virtualCall(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    bool value = argc ? argv[0].toBoolean() : 0;
    return Encode(value);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::BooleanCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411BooleanCtor10__dataTestEv(QV4::BooleanCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::BooleanCtor *QV4::BooleanCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BooleanCtor *ritual_ZNK3QV411BooleanCtor11d_uncheckedEv(
    const QV4::BooleanCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::BooleanCtor *QV4::BooleanCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::BooleanCtor *ritual_ZNK3QV411BooleanCtor1dEv(
    const QV4::BooleanCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::BooleanCtor::virtualCallAsConstructor(const
//      FunctionObject *a0, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411BooleanCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *a0,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::BooleanCtor::virtualCallAsConstructor(a0, argv, argc, a3);
}

//  ReturnedValue QV4::BooleanCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411BooleanCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::BooleanCtor::virtualCall(f, thisObject, argv, argc);
}
