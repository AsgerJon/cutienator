//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmlglobal_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlbuiltinfunctions_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmldebugconnector_p.h>
#include <QtQml/private/qqmldebugserviceinterfaces_p.h>
#include <QtQml/private/qqmldelayedcallqueue_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlloggingcategorybase_p.h>
#include <QtQml/private/qqmlplatform_p.h>
#include <QtQml/private/qqmlstringconverters_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4domerrors_p.h>
#include <QtQml/private/qv4engine_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4include_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4stackframe_p.h>
#include <QtQml/qqmlfile.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qcryptographichash.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qloggingcategory.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvarlengtharray.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 1836, as _ZN3QV419QQmlBindingFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue QQmlBindingFunction::virtualCall(
        const FunctionObject *f, const Value *, const Value *, int)
{
    // Mark this as a callable object, so that we can perform the binding magic on it.
    return f->engine()->throwTypeError(QStringLiteral("Bindings must not be called directly."));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/qml/qqmlbuiltinfunctions.cpp, line 1843, as _ZNK3QV419QQmlBindingFunction15currentLocationEv
namespace QV4 {
inline QQmlSourceLocation QQmlBindingFunction::currentLocation() const
{
    QV4::CppStackFrame *frame = engine()->currentStackFrame;
    if (frame->v4Function) // synchronous loading:
        return QQmlSourceLocation(frame->source(), frame->lineNumber(), 0);
    else // async loading:
        return bindingFunction()->function->sourceLocation();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::QQmlBindingFunction::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV419QQmlBindingFunction10__dataTestEv(
    QV4::QQmlBindingFunction *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlBindingFunction *QV4::QQmlBindingFunction::d_unchecked()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlBindingFunction *ritual_ZNK3QV419QQmlBindingFunction11d_uncheckedEv(
    const QV4::QQmlBindingFunction *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlBindingFunction *QV4::QQmlBindingFunction::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlBindingFunction *ritual_ZNK3QV419QQmlBindingFunction1dEv(
    const QV4::QQmlBindingFunction *self) {
  return self->d();
}

//  ReturnedValue QV4::QQmlBindingFunction::virtualCall(const FunctionObject
//      *f, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV419QQmlBindingFunction11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::QQmlBindingFunction::virtualCall(f, thisObject, argv, argc);
}

//  Heap::JavaScriptFunctionObject
//      *QV4::QQmlBindingFunction::bindingFunction() const
extern "C" Q_DECL_EXPORT
QV4::Heap::JavaScriptFunctionObject *ritual_ZNK3QV419QQmlBindingFunction15bindingFunctionEv(
    const QV4::QQmlBindingFunction *self) {
  return self->bindingFunction();
}

//  QQmlSourceLocation QV4::QQmlBindingFunction::currentLocation() const
extern "C" Q_DECL_EXPORT
QQmlSourceLocation *ritual_ZNK3QV419QQmlBindingFunction15currentLocationEv(
    const QV4::QQmlBindingFunction *self) {
  return new QQmlSourceLocation(self->currentLocation());
}
