//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4context_p.h, Qt 6.12.0. Edited by hand on
//  2026-11-25: added by hand, instances of templates of the class: 2. Kept
//  as it is when the generator runs again.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4context_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QString>
#include <QtQml/private/qv4context_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4argumentsobject_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4symbol_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4context.cpp, line 410, as _ZN3QV44Heap11CallContext6setArgEjNS_5ValueE
namespace QV4 {
inline void Heap::CallContext::setArg(uint index, Value v)
{
    locals.set(internalClass->engine, locals.size + index, v);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::CallContext::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::CallContext::markObjects(b, stack);
}

//  void QV4::Heap::CallContext::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext4initEv(QV4::Heap::CallContext *self) {
  self->init();
}

//  int QV4::Heap::CallContext::argc() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK3QV44Heap11CallContext4argcEv(
    const QV4::Heap::CallContext *self) {
  return self->argc();
}

//  const Value *QV4::Heap::CallContext::args() const
extern "C" Q_DECL_EXPORT
const QV4::Value *ritual_ZNK3QV44Heap11CallContext4argsEv(
    const QV4::Heap::CallContext *self) {
  return self->args();
}

//  void QV4::Heap::CallContext::setArg(uint index, Value v)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext6setArgEjNS_5ValueE(
    QV4::Heap::CallContext *self,
    uint index,
    const QV4::Value *v) {
  self->setArg(index, *v);
}

//  QV4::Heap::CallContext as the QV4::Heap::CallContextData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::CallContextData *ritual_cast_QV4_Heap_CallContext_QV4_Heap_CallContextData(
    QV4::Heap::CallContext *self) {
  return static_cast<QV4::Heap::CallContextData *>(self);
}

#include <QtQml/6.12.0/QtQml/private/qv4compileddata_p.h>

//  void QV4::Heap::CallContext::setupLocalTemporalDeadZone<
//      QV4::CompiledData::Function>(QV4::CompiledData::Function *bof)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext26setupLocalTemporalDeadZoneINS_12CompiledData8FunctionEEEvPT_(
    QV4::Heap::CallContext *self, QV4::CompiledData::Function *bof) {
  self->setupLocalTemporalDeadZone<QV4::CompiledData::Function>(bof);
}

//  void QV4::Heap::CallContext::setupLocalTemporalDeadZone<
//      QV4::CompiledData::Block>(QV4::CompiledData::Block *bof)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11CallContext26setupLocalTemporalDeadZoneINS_12CompiledData5BlockEEEvPT_(
    QV4::Heap::CallContext *self, QV4::CompiledData::Block *bof) {
  self->setupLocalTemporalDeadZone<QV4::CompiledData::Block>(bof);
}
