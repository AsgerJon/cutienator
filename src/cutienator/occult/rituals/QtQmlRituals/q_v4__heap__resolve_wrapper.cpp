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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4promiseobject.cpp, line 362, as _ZN3QV44Heap14ResolveWrapper4initEv
namespace QV4 {
using namespace QV4::Promise;
inline void Heap::ResolveWrapper::init()
{
    alreadyResolved = false;
    Heap::FunctionObject::init();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ResolveWrapper::markObjects(Heap::Base *b, MarkStack
//      *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14ResolveWrapper11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ResolveWrapper::markObjects(b, stack);
}

//  void QV4::Heap::ResolveWrapper::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14ResolveWrapper4initEv(
    QV4::Heap::ResolveWrapper *self) {
  self->init();
}

//  QV4::Heap::ResolveWrapper as the QV4::Heap::ResolveWrapperData it is
//      built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ResolveWrapperData *ritual_cast_QV4_Heap_ResolveWrapper_QV4_Heap_ResolveWrapperData(
    QV4::Heap::ResolveWrapper *self) {
  return static_cast<QV4::Heap::ResolveWrapperData *>(self);
}
