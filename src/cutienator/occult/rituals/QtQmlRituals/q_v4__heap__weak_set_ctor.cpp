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

//  from ../qtdeclarative/src/qml/jsruntime/qv4setobject.cpp, line 18, as _ZN3QV44Heap11WeakSetCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::WeakSetCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("WeakSet"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::WeakSetCtor::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11WeakSetCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::WeakSetCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}
