//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qscopedvaluerollback.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arrayobject.cpp, line 23, as _ZN3QV49ArrayCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue ArrayCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = static_cast<const ArrayCtor *>(f)->engine();
    Scope scope(v4);
    ScopedArrayObject a(scope, v4->newArrayObject());
    if (newTarget)
        a->setProtoFromNewTarget(newTarget);
    uint len;
    if (argc == 1 && argv[0].isNumber()) {
        bool ok;
        len = argv[0].asArrayLength(&ok);

        if (!ok)
            return v4->throwRangeError(argv[0]);

        if (len < 0x1000)
            a->arrayReserve(len);
    } else {
        len = argc;
        a->arrayReserve(len);
        a->arrayPut(0, argv, len);
    }
    a->setArrayLengthUnchecked(len);

    return a.asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arrayobject.cpp, line 50, as _ZN3QV49ArrayCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ArrayCtor::virtualCall(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    return virtualCallAsConstructor(f, argv, argc, f);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ArrayCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ArrayCtor10__dataTestEv(QV4::ArrayCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::ArrayCtor *QV4::ArrayCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayCtor *ritual_ZNK3QV49ArrayCtor11d_uncheckedEv(
    const QV4::ArrayCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ArrayCtor *QV4::ArrayCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ArrayCtor *ritual_ZNK3QV49ArrayCtor1dEv(
    const QV4::ArrayCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::ArrayCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value
//      *newTarget)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV49ArrayCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *newTarget) {
  return QV4::ArrayCtor::virtualCallAsConstructor(f, argv, argc, newTarget);
}

//  ReturnedValue QV4::ArrayCtor::virtualCall(const FunctionObject *f, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV49ArrayCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ArrayCtor::virtualCall(f, thisObject, argv, argc);
}
