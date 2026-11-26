//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4arrayobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4arrayobject_p.h>
#include <QtQml/private/qv4arrayiterator_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/qscopedvaluerollback.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4arrayobject.cpp, line 18, as _ZN3QV44Heap9ArrayCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void Heap::ArrayCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("Array"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ArrayCtor::init(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ArrayCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::ArrayCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}
