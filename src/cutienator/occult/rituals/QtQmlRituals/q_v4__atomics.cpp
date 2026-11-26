//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4atomics_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4atomics_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4typedarray_p.h>
#include <QtQml/private/qv4atomics_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4atomics.cpp, line 138, as _ZN3QV47Atomics17method_isLockFreeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Atomics::method_isLockFree(const FunctionObject *, const Value *, const Value *argv, int argc)
{
    if (!argc)
        return Encode(false);
    double n = argv[0].toInteger();
    if (n == 4.)
        return Encode(true);
    if (n == 2.)
        return Encode(QAtomicOps<unsigned short>::isTestAndSetNative());
#ifdef Q_ATOMIC_INT8_IS_SUPPORTED
    if (n == 1.)
        return Encode(QAtomicOps<unsigned char>::isTestAndSetNative());
#endif
    return Encode(false);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4atomics.cpp, line 208, as _ZN3QV47Atomics11method_waitEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Atomics::method_wait(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4atomics.cpp, line 213, as _ZN3QV47Atomics11method_wakeEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue Atomics::method_wake(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Atomics::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV47Atomics10__dataTestEv(QV4::Atomics *self) {
  self->__dataTest();
}

//  QV4::Heap::Atomics *QV4::Atomics::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Atomics *ritual_ZNK3QV47Atomics11d_uncheckedEv(
    const QV4::Atomics *self) {
  return self->d_unchecked();
}

//  QV4::Heap::Atomics *QV4::Atomics::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::Atomics *ritual_ZNK3QV47Atomics1dEv(const QV4::Atomics *self) {
  return self->d();
}

//  ReturnedValue QV4::Atomics::method_isLockFree(const FunctionObject *a0,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Atomics17method_isLockFreeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::Atomics::method_isLockFree(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::Atomics::method_wait(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Atomics11method_waitEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::Atomics::method_wait(a0, thisObject, argv, argc);
}

//  ReturnedValue QV4::Atomics::method_wake(const FunctionObject *a0, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV47Atomics11method_wakeEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::Atomics::method_wake(a0, thisObject, argv, argc);
}
