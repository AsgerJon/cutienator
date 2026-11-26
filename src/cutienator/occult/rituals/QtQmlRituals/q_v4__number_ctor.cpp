//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4numberobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4numberobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4numberobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qmath.h>
#include <QtCore/QDebug>
#include <cassert>
#include <limits>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 47, as _ZN3QV410NumberCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue NumberCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    auto v4 = f->engine();
    double dbl = argc ? argv[0].toNumber() : 0.;

    ReturnedValue o = Encode(f->engine()->newNumberObject(dbl));
    if (!newTarget)
        return o;
    Scope scope(v4);
    ScopedObject obj(scope, o);
    obj->setProtoFromNewTarget(newTarget);
    return obj->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4numberobject.cpp, line 61, as _ZN3QV410NumberCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue NumberCtor::virtualCall(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    double dbl = argc ? argv[0].toNumber() : 0.;
    return Encode(dbl);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::NumberCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410NumberCtor10__dataTestEv(QV4::NumberCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::NumberCtor *QV4::NumberCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::NumberCtor *ritual_ZNK3QV410NumberCtor11d_uncheckedEv(
    const QV4::NumberCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::NumberCtor *QV4::NumberCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::NumberCtor *ritual_ZNK3QV410NumberCtor1dEv(
    const QV4::NumberCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::NumberCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410NumberCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::NumberCtor::virtualCallAsConstructor(f, argv, argc, a3);
}

//  ReturnedValue QV4::NumberCtor::virtualCall(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410NumberCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::NumberCtor::virtualCall(a0, thisObject, argv, argc);
}
