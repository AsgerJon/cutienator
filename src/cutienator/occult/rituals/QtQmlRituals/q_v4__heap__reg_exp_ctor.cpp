//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4regexpobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/private/qlocale_tools_p.h>
#include <QtCore/QDebug>
#if QT_CONFIG(regularexpression)
#include <QtCore/qregularexpression.h>
#endif
#include <cassert>
#include <typeinfo>
#include <iostream>
#include <QtQml/private/qv4alloca_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 200, as _ZN3QV44Heap10RegExpCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void Heap::RegExpCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("RegExp"));
    clearLastMatch();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4regexpobject.cpp, line 206, as _ZN3QV44Heap10RegExpCtor14clearLastMatchEv
namespace QV4 {
inline void Heap::RegExpCtor::clearLastMatch()
{
    lastMatch.set(internalClass->engine, Value::nullValue());
    lastInput.set(internalClass->engine, internalClass->engine->id_empty()->d());
    lastMatchStart = 0;
    lastMatchEnd = 0;
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::RegExpCtor::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10RegExpCtor11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::RegExpCtor::markObjects(b, stack);
}

//  void QV4::Heap::RegExpCtor::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10RegExpCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::RegExpCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}

//  void QV4::Heap::RegExpCtor::clearLastMatch()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10RegExpCtor14clearLastMatchEv(
    QV4::Heap::RegExpCtor *self) {
  self->clearLastMatch();
}

//  QV4::Heap::RegExpCtor as the QV4::Heap::RegExpCtorData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::RegExpCtorData *ritual_cast_QV4_Heap_RegExpCtor_QV4_Heap_RegExpCtorData(
    QV4::Heap::RegExpCtor *self) {
  return static_cast<QV4::Heap::RegExpCtorData *>(self);
}
