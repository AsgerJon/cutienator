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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 273, as _ZN3QV414ErrorPrototype4initEPNS_15ExecutionEngineEPNS_6ObjectES4_NS_4Heap11ErrorObject9ErrorTypeE
namespace QV4 {
inline void ErrorPrototype::init(ExecutionEngine *engine, Object *ctor, Object *obj, Heap::ErrorObject::ErrorType t)
{
    Scope scope(engine);
    ScopedString s(scope);
    ScopedObject o(scope);
    ctor->defineReadonlyProperty(engine->id_prototype(), (o = obj));
    ctor->defineReadonlyConfigurableProperty(engine->id_length(), Value::fromInt32(1));
    obj->setProperty(Index_Constructor, ctor->d());
    obj->setProperty(Index_Message, engine->id_empty()->d());
    obj->setProperty(Index_Name, engine->newString(QString::fromLatin1(ErrorObject::className(t))));
    obj->defineDefaultProperty(engine->id_toString(), method_toString, 0);
}
}  // namespace QV4

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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 286, as _ZN3QV414ErrorPrototype15method_toStringEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ErrorPrototype::method_toString(const FunctionObject *b, const Value *thisObject, const Value *, int)
{
    ExecutionEngine *v4 = b->engine();
    const Object *o = thisObject->as<Object>();
    if (!o)
        return v4->throwTypeError();

    Scope scope(v4);
    ScopedValue name(scope, o->get(scope.engine->id_name()));
    QString qname;
    if (name->isUndefined())
        qname = QStringLiteral("Error");
    else
        qname = name->toQString();

    ScopedString s(scope, scope.engine->newString(QStringLiteral("message")));
    ScopedValue message(scope, o->get(s));
    QString qmessage;
    if (!message->isUndefined())
        qmessage = message->toQString();

    QString str;
    if (qname.isEmpty()) {
        str = qmessage;
    } else if (qmessage.isEmpty()) {
        str = qname;
    } else {
        str = qname + QLatin1String(": ") + qmessage;
    }

    return scope.engine->newString(str)->asReturnedValue();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::TypeErrorPrototype::init(ExecutionEngine *engine, Object *ctor)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV418TypeErrorPrototype4initEPNS_15ExecutionEngineEPNS_6ObjectE(
    QV4::TypeErrorPrototype *self,
    QV4::ExecutionEngine *engine,
    QV4::Object *ctor) {
  self->init(engine, ctor);
}
