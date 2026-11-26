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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4functionobject.cpp, line 80, as _ZN3QV44Heap21DynamicFunctionObject4initEPNS_15ExecutionEngineEPNS_6StringEPFyPKNS_14FunctionObjectEPKNS_5ValueESB_iE
namespace QV4 {
inline void Heap::DynamicFunctionObject::init(
        QV4::ExecutionEngine *engine, QV4::String *name, VTable::Call call)
{
    FunctionObject::init(engine, name);
    jsCall = call;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::DynamicFunctionObject::init(ExecutionEngine *engine,
//      QV4::String *name, VTable::Call call)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap21DynamicFunctionObject4initEPNS_15ExecutionEngineEPNS_6StringEPFyPKNS_14FunctionObjectEPKNS_5ValueESB_iE(
    QV4::Heap::DynamicFunctionObject *self,
    QV4::ExecutionEngine *engine,
    QV4::String *name,
    void *call) {
  self->init(engine, name, reinterpret_cast<QV4::VTable::Call>(call));
}

//  QV4::Heap::DynamicFunctionObject as the
//      QV4::Heap::DynamicFunctionObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::DynamicFunctionObjectData *ritual_cast_QV4_Heap_DynamicFunctionObject_QV4_Heap_DynamicFunctionObjectData(
    QV4::Heap::DynamicFunctionObject *self) {
  return static_cast<QV4::Heap::DynamicFunctionObjectData *>(self);
}
