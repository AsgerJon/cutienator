//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4functionobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4functionobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qqmljsengine_p.h>
#include <QtQml/private/qqmljsast_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qv4runtimecodegen_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4vme_moth_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtCore/QDebug>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 592, as _ZNK3QV414ScriptFunction19classForConstructorEv
namespace QV4 {
inline Heap::InternalClass *ScriptFunction::classForConstructor() const
{
    Scope scope(engine());
    ScopedValue o(scope, protoProperty());
    if (d()->cachedClassForConstructor && d()->cachedClassForConstructor->prototype == o->heapObject())
        return d()->cachedClassForConstructor;

    Scoped<InternalClass> ic(scope, engine()->internalClasses(EngineBase::Class_Object));
    ScopedObject p(scope, o);
    if (p)
        ic = ic->changePrototype(p->d());
    d()->cachedClassForConstructor.set(scope.engine, ic->d());

    return ic->d();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ScriptFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV414ScriptFunction10__dataTestEv(QV4::ScriptFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::ScriptFunction *QV4::ScriptFunction::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ScriptFunction *ritual_ZNK3QV414ScriptFunction11d_uncheckedEv(
    const QV4::ScriptFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ScriptFunction *QV4::ScriptFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ScriptFunction *ritual_ZNK3QV414ScriptFunction1dEv(
    const QV4::ScriptFunction *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ScriptFunction::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV414ScriptFunction20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ScriptFunction::defaultInternalClass(e);
}

//  Heap::InternalClass *QV4::ScriptFunction::classForConstructor() const
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZNK3QV414ScriptFunction19classForConstructorEv(
    const QV4::ScriptFunction *self) {
  return self->classForConstructor();
}
