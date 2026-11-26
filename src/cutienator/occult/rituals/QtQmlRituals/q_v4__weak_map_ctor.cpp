//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4mapobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4mapobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4mapobject_p.h>
#include <QtQml/private/qv4mapiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 149, as _ZN3QV44Heap9MapObject4initEv
namespace QV4 {
inline void Heap::MapObject::init()
{
    Object::init();
    esTable = new ESTable();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4mapobject.cpp, line 90, as _ZN3QV411WeakMapCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue WeakMapCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    Scope scope(f);
    return scope.engine->throwTypeError(QString::fromLatin1("(Weak)Map requires new"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::WeakMapCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411WeakMapCtor10__dataTestEv(QV4::WeakMapCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::WeakMapCtor *QV4::WeakMapCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::WeakMapCtor *ritual_ZNK3QV411WeakMapCtor11d_uncheckedEv(
    const QV4::WeakMapCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::WeakMapCtor *QV4::WeakMapCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::WeakMapCtor *ritual_ZNK3QV411WeakMapCtor1dEv(
    const QV4::WeakMapCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::WeakMapCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411WeakMapCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::WeakMapCtor::virtualCall(f, thisObject, argv, argc);
}
