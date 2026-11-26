//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 29, as _ZN3QV44Heap11ErrorObject4initEv
namespace QV4 {
inline void Heap::ErrorObject::init()
{
    Object::init();
    stackTrace = nullptr;

    Scope scope(internalClass->engine);
    Scoped<QV4::ErrorObject> e(scope, this);

    if (internalClass == scope.engine->internalClasses(EngineBase::Class_ErrorProto))
        return;

    setProperty(scope.engine, QV4::ErrorObject::Index_Stack, scope.engine->getStackFunction()->d());
    setProperty(scope.engine, QV4::ErrorObject::Index_StackSetter, Value::undefinedValue());
    setProperty(scope.engine, QV4::ErrorObject::Index_FileName, Value::undefinedValue());
    setProperty(scope.engine, QV4::ErrorObject::Index_LineNumber, Value::undefinedValue());
}
}  // namespace QV4

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 67, as _ZN3QV44Heap11ErrorObject4initERKNS_5ValueERK7QStringiiNS1_9ErrorTypeE
namespace QV4 {
inline void Heap::ErrorObject::init(const Value &message, const QString &fileName, int line, int column, ErrorObject::ErrorType t)
{
    Q_UNUSED(fileName); // ####
    Object::init();
    errorType = t;

    Scope scope(internalClass->engine);
    Scoped<QV4::ErrorObject> e(scope, this);

    setProperty(scope.engine, QV4::ErrorObject::Index_Stack, scope.engine->getStackFunction()->d());
    setProperty(scope.engine, QV4::ErrorObject::Index_StackSetter, Value::undefinedValue());

    e->d()->stackTrace = new StackTrace(scope.engine->stackTrace());
    StackFrame frame;
    frame.source = fileName;
    frame.line = line;
    frame.column = column;
    e->d()->stackTrace->prepend(frame);

    Q_ASSERT(!e->d()->stackTrace->isEmpty());
    setProperty(scope.engine, QV4::ErrorObject::Index_FileName, scope.engine->newString(e->d()->stackTrace->at(0).source));
    setProperty(scope.engine, QV4::ErrorObject::Index_LineNumber, Value::fromInt32(qAbs(e->d()->stackTrace->at(0).line)));

    if (!message.isUndefined())
        setProperty(scope.engine, QV4::ErrorObject::Index_Message, message);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ErrorObject::markObjects(Heap::Base *b, MarkStack *stack)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject11markObjectsEPNS0_4BaseEPNS_9MarkStackE(
    QV4::Heap::Base *b,
    QV4::MarkStack *stack) {
  QV4::Heap::ErrorObject::markObjects(b, stack);
}

//  void QV4::Heap::ErrorObject::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject4initEv(QV4::Heap::ErrorObject *self) {
  self->init();
}

//  void QV4::Heap::ErrorObject::init(const Value &message, ErrorType t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject4initERKNS_5ValueENS1_9ErrorTypeE(
    QV4::Heap::ErrorObject *self,
    const QV4::Value *message,
    QV4::Heap::ErrorObject::ErrorType t) {
  self->init(*message, t);
}

//  void QV4::Heap::ErrorObject::init(const Value &message, const QString
//      &fileName, int line, int column, ErrorType t)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject4initERKNS_5ValueERK7QStringiiNS1_9ErrorTypeE(
    QV4::Heap::ErrorObject *self,
    const QV4::Value *message,
    const QString *fileName,
    int line,
    int column,
    QV4::Heap::ErrorObject::ErrorType t) {
  self->init(*message, *fileName, line, column, t);
}

//  void QV4::Heap::ErrorObject::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap11ErrorObject7destroyEv(
    QV4::Heap::ErrorObject *self) {
  self->destroy();
}

//  QV4::Heap::ErrorObject as the QV4::Heap::ErrorObjectData it is built on
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorObjectData *ritual_cast_QV4_Heap_ErrorObject_QV4_Heap_ErrorObjectData(
    QV4::Heap::ErrorObject *self) {
  return static_cast<QV4::Heap::ErrorObjectData *>(self);
}
