//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4errorobject_p.h>
#include <QtCore/qnumeric.h>
#include <QtCore/qmath.h>
#include <QtCore/QDateTime>
#include <QtCore/QStringList>
#include <QtCore/QDebug>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4codegen_p.h>
#ifndef Q_OS_WIN
#  include <time.h>
#  ifndef Q_OS_VXWORKS
#    include <sys/time.h>
#  else
#    include "qplatformdefs.h"
#  endif
#else
#  include <QtCore/qt_windows.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 94, as _ZN3QV411ErrorObject9classNameENS_4Heap11ErrorObject9ErrorTypeE
namespace QV4 {
inline const char *ErrorObject::className(Heap::ErrorObject::ErrorType t)
{
    switch (t) {
    case Heap::ErrorObject::Error:
        return "Error";
    case Heap::ErrorObject::EvalError:
        return "EvalError";
    case Heap::ErrorObject::RangeError:
        return "RangeError";
    case Heap::ErrorObject::ReferenceError:
        return "ReferenceError";
    case Heap::ErrorObject::SyntaxError:
        return "SyntaxError";
    case Heap::ErrorObject::TypeError:
        return "TypeError";
    case Heap::ErrorObject::URIError:
        return "URIError";
    }
    Q_UNREACHABLE();
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 115, as _ZN3QV411ErrorObject16method_get_stackEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ErrorObject::method_get_stack(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const ErrorObject *This = thisObject->as<ErrorObject>();
    if (!This)
        return v4->throwTypeError();
    if (!This->d()->stack) {
        QString trace;
        for (int i = 0; i < This->d()->stackTrace->size(); ++i) {
            if (i > 0)
                trace += QLatin1Char('\n');
            const StackFrame &frame = This->d()->stackTrace->at(i);
            trace += frame.function + QLatin1Char('@') + frame.source;
            if (frame.line >= 0)
                trace += QLatin1Char(':') + QString::number(frame.line);
        }
        This->d()->stack.set(v4, v4->newString(trace));
    }
    return This->d()->stack->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ErrorObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ErrorObject10__dataTestEv(QV4::ErrorObject *self) {
  self->__dataTest();
}

//  QV4::Heap::ErrorObject *QV4::ErrorObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObject *ritual_ZNK3QV411ErrorObject11d_uncheckedEv(
    const QV4::ErrorObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ErrorObject *QV4::ErrorObject::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObject *ritual_ZNK3QV411ErrorObject1dEv(
    const QV4::ErrorObject *self) {
  return self->d();
}

//  Heap::InternalClass
//      *QV4::ErrorObject::defaultInternalClass(QV4::EngineBase *e)
extern "C" Q_DECL_EXPORT
QV4::Heap::InternalClass *ritual_ZN3QV411ErrorObject20defaultInternalClassEPNS_10EngineBaseE(
    QV4::EngineBase *e) {
  return QV4::ErrorObject::defaultInternalClass(e);
}

//  QV4::Object *QV4::ErrorObject::defaultPrototype(QV4::ExecutionEngine *e)
extern "C" Q_DECL_EXPORT
QV4::Object *ritual_ZN3QV411ErrorObject16defaultPrototypeEPNS_15ExecutionEngineE(
    QV4::ExecutionEngine *e) {
  return QV4::ErrorObject::defaultPrototype(e);
}

//  void QV4::ErrorObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV411ErrorObject14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::ErrorObject::virtualDestroy(b);
}

//  SyntaxErrorObject *QV4::ErrorObject::asSyntaxError()
extern "C" Q_DECL_EXPORT
QV4::SyntaxErrorObject *ritual_ZN3QV411ErrorObject13asSyntaxErrorEv(
    QV4::ErrorObject *self) {
  return self->asSyntaxError();
}

//  const char *QV4::ErrorObject::className(Heap::ErrorObject::ErrorType t)
extern "C" Q_DECL_EXPORT
const char *ritual_ZN3QV411ErrorObject9classNameENS_4Heap11ErrorObject9ErrorTypeE(
    QV4::Heap::ErrorObject::ErrorType t) {
  return QV4::ErrorObject::className(t);
}

//  ReturnedValue QV4::ErrorObject::method_get_stack(const FunctionObject
//      *a0, const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV411ErrorObject16method_get_stackEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *a0,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ErrorObject::method_get_stack(a0, thisObject, argv, argc);
}
