//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arraybuffer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4typedarray_p.h>
#include <QtQml/private/qv4dataview_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 30, as _ZN3QV421SharedArrayBufferCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue SharedArrayBufferCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    Scope scope(f);
    if (newTarget->isUndefined())
        return scope.engine->throwTypeError();

    const double len = argc ? argv[0].toInteger() : 0;
    if (scope.hasException())
        return Encode::undefined();
    if (len < 0 || len >= std::numeric_limits<int>::max())
        return scope.engine->throwRangeError(QStringLiteral("SharedArrayBuffer: Invalid length."));

    Scoped<SharedArrayBuffer> a(
                scope, scope.engine->memoryManager->allocate<SharedArrayBuffer>(size_t(len)));
    if (scope.hasException())
        return Encode::undefined();

    return a->asReturnedValue();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 50, as _ZN3QV421SharedArrayBufferCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue SharedArrayBufferCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::SharedArrayBufferCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV421SharedArrayBufferCtor10__dataTestEv(
    QV4::SharedArrayBufferCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::SharedArrayBufferCtor
//      *QV4::SharedArrayBufferCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SharedArrayBufferCtor *ritual_ZNK3QV421SharedArrayBufferCtor11d_uncheckedEv(
    const QV4::SharedArrayBufferCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::SharedArrayBufferCtor *QV4::SharedArrayBufferCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::SharedArrayBufferCtor *ritual_ZNK3QV421SharedArrayBufferCtor1dEv(
    const QV4::SharedArrayBufferCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::SharedArrayBufferCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV421SharedArrayBufferCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::SharedArrayBufferCtor::virtualCallAsConstructor(
      f,
      argv,
      argc,
      a3);
}

//  ReturnedValue QV4::SharedArrayBufferCtor::virtualCall(const
//      FunctionObject *f, const Value *thisObject, const Value *argv, int
//      argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV421SharedArrayBufferCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::SharedArrayBufferCtor::virtualCall(f, thisObject, argv, argc);
}
