//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4qmlcontext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4qmlcontext_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmljavascriptexpression_p.h>
#include <QtQml/private/qqmllistwrapper_p.h>
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qv4compileddata_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4function_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4module_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/private/qv4value_p.h>
#include <QtCore/qloggingcategory.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmlcontext.cpp, line 825, as _ZN3QV44Heap10QmlContext4initEPNS_16ExecutionContextEPNS_18QQmlContextWrapperE
namespace QV4 {
inline void Heap::QmlContext::init(QV4::ExecutionContext *outerContext, QV4::QQmlContextWrapper *qml)
{
    Heap::ExecutionContext::init(Heap::ExecutionContext::Type_QmlContext);
    outer.set(internalClass->engine, outerContext->d());

    this->activation.set(internalClass->engine, qml->d());
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QmlContext::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10QmlContext11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QmlContext::markObjects(b, stack);
}

//  QQmlContextWrapper *QV4::Heap::QmlContext::qml()
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapper *ritual_ZN3QV44Heap10QmlContext3qmlEv(
    QV4::Heap::QmlContext *self) {
  return self->qml();
}

//  void QV4::Heap::QmlContext::init(QV4::ExecutionContext *outerContext,
//      QV4::QQmlContextWrapper *qml)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10QmlContext4initEPNS_16ExecutionContextEPNS_18QQmlContextWrapperE(
    QV4::Heap::QmlContext *self,
    QV4::ExecutionContext *outerContext,
    QV4::QQmlContextWrapper *qml) {
  self->init(outerContext, qml);
}

//  QV4::Heap::QmlContext as the QV4::Heap::QmlContextData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QmlContextData *ritual_cast_QV4_Heap_QmlContext_QV4_Heap_QmlContextData(
    QV4::Heap::QmlContext *self) {
  return static_cast<QV4::Heap::QmlContextData *>(self);
}
