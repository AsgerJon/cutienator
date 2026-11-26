//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4errorobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4errorobject_p.h>
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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 186, as _ZN3QV44Heap9ErrorCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
inline void Heap::ErrorCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("Error"));
}
}  // namespace QV4

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 191, as _ZN3QV44Heap9ErrorCtor4initEPNS_15ExecutionEngineERK7QString
namespace QV4 {
inline void Heap::ErrorCtor::init(QV4::ExecutionEngine *engine, const QString &name)
{
    Heap::FunctionObject::init(engine, name);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::ErrorCtor::init(ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ErrorCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::ErrorCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}

//  void QV4::Heap::ErrorCtor::init(ExecutionEngine *engine, const QString
//      &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap9ErrorCtor4initEPNS_15ExecutionEngineERK7QString(
    QV4::Heap::ErrorCtor *self,
    QV4::ExecutionEngine *engine,
    const QString *name) {
  self->init(engine, *name);
}
