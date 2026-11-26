//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4objectproto_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4objectproto_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4propertykey_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QStringList>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectproto.cpp, line 28, as _ZN3QV410ObjectCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_
namespace QV4 {
inline ReturnedValue ObjectCtor::virtualCallAsConstructor(const FunctionObject *f, const Value *argv, int argc, const Value *newTarget)
{
    ExecutionEngine *v4 = f->engine();
    const ObjectCtor *nt = static_cast<const ObjectCtor *>(newTarget);
    if (!argc || argv[0].isUndefined() || argv[0].isNull()) {
        Scope scope(v4);
        ScopedObject obj(scope, scope.engine->newObject());
        ScopedObject proto(scope, nt->get(scope.engine->id_prototype()));
        if (!!proto)
            obj->setPrototypeOf(proto);
        return obj.asReturnedValue();
    } else {
        return argv[0].toObject(v4)->asReturnedValue();
    }
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4objectproto.cpp, line 44, as _ZN3QV410ObjectCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ObjectCtor::virtualCall(const FunctionObject *m, const Value *, const Value *argv, int argc)
{
    ExecutionEngine *v4 = m->engine();
    if (!argc || argv[0].isUndefined() || argv[0].isNull()) {
        return v4->newObject()->asReturnedValue();
    } else {
        return argv[0].toObject(v4)->asReturnedValue();
    }
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ObjectCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV410ObjectCtor10__dataTestEv(QV4::ObjectCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::ObjectCtor *QV4::ObjectCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ObjectCtor *ritual_ZNK3QV410ObjectCtor11d_uncheckedEv(
    const QV4::ObjectCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ObjectCtor *QV4::ObjectCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ObjectCtor *ritual_ZNK3QV410ObjectCtor1dEv(
    const QV4::ObjectCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::ObjectCtor::virtualCallAsConstructor(const
//      FunctionObject *f, const Value *argv, int argc, const Value *a3)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410ObjectCtor24virtualCallAsConstructorEPKNS_14FunctionObjectEPKNS_5ValueEiS6_(
    const QV4::FunctionObject *f,
    const QV4::Value *argv,
    int argc,
    const QV4::Value *a3) {
  return QV4::ObjectCtor::virtualCallAsConstructor(f, argv, argc, a3);
}

//  ReturnedValue QV4::ObjectCtor::virtualCall(const FunctionObject *m, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV410ObjectCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *m,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ObjectCtor::virtualCall(m, thisObject, argv, argc);
}
