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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmlcontext.cpp, line 37, as _ZN3QV44Heap18QQmlContextWrapper4initE14QQmlRefPointerI15QQmlContextDataEP7QObject
namespace QV4 {
inline void Heap::QQmlContextWrapper::init(QQmlRefPointer<QQmlContextData> context, QObject *scopeObject)
{
    Object::init();
    this->context = context.take();
    this->scopeObject.init(scopeObject);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4qmlcontext.cpp, line 44, as _ZN3QV44Heap18QQmlContextWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlContextWrapper::destroy()
{
    context->release();
    context = nullptr;
    scopeObject.destroy();
    Object::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QQmlContextWrapper::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QQmlContextWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::QQmlContextWrapper::markObjects(b, stack);
}

//  void QV4::Heap::QQmlContextWrapper::init(QQmlRefPointer<QQmlContextData>
//      context, QObject *scopeObject)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QQmlContextWrapper4initE14QQmlRefPointerI15QQmlContextDataEP7QObject(
    QV4::Heap::QQmlContextWrapper *self,
    const QQmlRefPointer<QQmlContextData> *context,
    QObject *scopeObject) {
  self->init(*context, scopeObject);
}

//  void QV4::Heap::QQmlContextWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap18QQmlContextWrapper7destroyEv(
    QV4::Heap::QQmlContextWrapper *self) {
  self->destroy();
}

//  QV4::Heap::QQmlContextWrapper as the QV4::Heap::QQmlContextWrapperData it
//      is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlContextWrapperData *ritual_cast_QV4_Heap_QQmlContextWrapper_QV4_Heap_QQmlContextWrapperData(
    QV4::Heap::QQmlContextWrapper *self) {
  return static_cast<QV4::Heap::QQmlContextWrapperData *>(self);
}
