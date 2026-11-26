//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 46, as _ZN3QV44Heap11ErrorObject4initERKNS_5ValueENS1_9ErrorTypeE
namespace QV4 {
inline void Heap::ErrorObject::init(const Value &message, ErrorType t)
{
    Object::init();
    errorType = t;

    Scope scope(internalClass->engine);
    Scoped<QV4::ErrorObject> e(scope, this);

    setProperty(scope.engine, QV4::ErrorObject::Index_Stack, scope.engine->getStackFunction()->d());
    setProperty(scope.engine, QV4::ErrorObject::Index_StackSetter, Value::undefinedValue());

    e->d()->stackTrace = new StackTrace(scope.engine->stackTrace());
    if (!e->d()->stackTrace->isEmpty()) {
        setProperty(scope.engine, QV4::ErrorObject::Index_FileName, scope.engine->newString(e->d()->stackTrace->at(0).source));
        setProperty(scope.engine, QV4::ErrorObject::Index_LineNumber, Value::fromInt32(qAbs(e->d()->stackTrace->at(0).line)));
    }

    if (!message.isUndefined())
        setProperty(scope.engine, QV4::ErrorObject::Index_Message, message);
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 173, as _ZN3QV44Heap14URIErrorObject4initERKNS_5ValueE
namespace QV4 {
inline void Heap::URIErrorObject::init(const Value &message)
{
    Heap::ErrorObject::init(message, URIError);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::URIErrorObject::init(const Value &message)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap14URIErrorObject4initERKNS_5ValueE(
    QV4::Heap::URIErrorObject *self,
    const QV4::Value *message) {
  self->init(*message);
}
