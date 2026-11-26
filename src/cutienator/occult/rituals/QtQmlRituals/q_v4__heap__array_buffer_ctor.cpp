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

//  from ../qtdeclarative/src/qml/jsruntime/qv4arraybuffer.cpp, line 25, as _ZN3QV44Heap15ArrayBufferCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void Heap::ArrayBufferCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("ArrayBuffer"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ArrayBufferCtor::init(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15ArrayBufferCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::ArrayBufferCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}
