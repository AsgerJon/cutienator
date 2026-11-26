//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4promiseobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/QCoreApplication>
#include <QtQml/private/qv4promiseobject_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4jscall_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 338, as _ZN3QV44Heap27CapabilitiesExecutorWrapper4initEv
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::CapabilitiesExecutorWrapper::init()
{
    Heap::FunctionObject::init();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 343, as _ZN3QV44Heap27CapabilitiesExecutorWrapper7destroyEv
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::CapabilitiesExecutorWrapper::destroy()
{
    Heap::FunctionObject::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::CapabilitiesExecutorWrapper::markObjects(Heap::Base *b,
//      MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap27CapabilitiesExecutorWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::CapabilitiesExecutorWrapper::markObjects(b, stack);
}

//  void QV4::Heap::CapabilitiesExecutorWrapper::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap27CapabilitiesExecutorWrapper4initEv(
    QV4::Heap::CapabilitiesExecutorWrapper *self) {
  self->init();
}

//  void QV4::Heap::CapabilitiesExecutorWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap27CapabilitiesExecutorWrapper7destroyEv(
    QV4::Heap::CapabilitiesExecutorWrapper *self) {
  self->destroy();
}

//  QV4::Heap::CapabilitiesExecutorWrapper as the
//      QV4::Heap::CapabilitiesExecutorWrapperData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::CapabilitiesExecutorWrapperData *ritual_cast_QV4_Heap_CapabilitiesExecutorWrapper_QV4_Heap_CapabilitiesExecutorWrapperData(
    QV4::Heap::CapabilitiesExecutorWrapper *self) {
  return static_cast<QV4::Heap::CapabilitiesExecutorWrapperData *>(self);
}
