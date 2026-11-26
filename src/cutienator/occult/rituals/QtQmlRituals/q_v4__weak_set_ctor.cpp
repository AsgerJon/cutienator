//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4setobject_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4setobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4setobject_p.h>
#include <QtQml/private/qv4setiterator_p.h>
#include <QtQml/private/qv4estable_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 171, as _ZN3QV44Heap9SetObject4initEv
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::SetObject::init()
{
    Object::init();
    esTable = new ESTable();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 73, as _ZN3QV411WeakSetCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline ReturnedValue WeakSetCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    Scope scope(f);
    return scope.engine->throwTypeError(QString::fromLatin1("Set requires new"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::WeakSetCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411WeakSetCtor10__dataTestEv(QV4::WeakSetCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::WeakSetCtor *QV4::WeakSetCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::WeakSetCtor *ritual_ZNK3QV411WeakSetCtor11d_uncheckedEv(
    const QV4::WeakSetCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::WeakSetCtor *QV4::WeakSetCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::WeakSetCtor *ritual_ZNK3QV411WeakSetCtor1dEv(
    const QV4::WeakSetCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::WeakSetCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411WeakSetCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::WeakSetCtor::virtualCall(f, thisObject, argv, argc);
}
