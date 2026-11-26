//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4typedarray_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4typedarray_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4typedarray_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtCore/qatomic.h>
#include <cmath>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4typedarray.cpp, line 409, as _ZN3QV414TypedArrayCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue TypedArrayCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError(QStringLiteral("calling a TypedArray constructor without new is invalid"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::TypedArrayCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414TypedArrayCtor10__dataTestEv(QV4::TypedArrayCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::TypedArrayCtor *QV4::TypedArrayCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArrayCtor *ritual_ZNK3QV414TypedArrayCtor11d_uncheckedEv(
    const QV4::TypedArrayCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::TypedArrayCtor *QV4::TypedArrayCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::TypedArrayCtor *ritual_ZNK3QV414TypedArrayCtor1dEv(
    const QV4::TypedArrayCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::TypedArrayCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV414TypedArrayCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::TypedArrayCtor::virtualCall(f, thisObject, argv, argc);
}
