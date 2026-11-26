//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4globalobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4globalobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4globalobject_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4codegen_p.h>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4script_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4string_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qstring.h>
#include <iostream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4globalobject.cpp, line 294, as _ZN3QV44Heap12EvalFunction4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void Heap::EvalFunction::init(QV4::ExecutionEngine *engine)
{
    Scope s(engine);
    Heap::FunctionObject::init(engine, s.engine->id_eval());
    ScopedFunctionObject f(s, this);
    f->defineReadonlyConfigurableProperty(s.engine->id_length(), Value::fromInt32(1));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::EvalFunction::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap12EvalFunction4initEPNS_15ExecutionEngineE(
    QV4::Heap::EvalFunction *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}
