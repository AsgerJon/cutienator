//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4stringobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4stringobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4stringobject_p.h>
#include <QtQml/private/qv4regexpobject_p.h>
#include <QtQml/private/qv4mm_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4alloca_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4stringiterator_p.h>
#include <QtCore/QDateTime>
#include <QtCore/QDebug>
#include <QtCore/QStringList>
#include <QtQml/private/qv4runtime_p.h>
#include <cassert>
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

using namespace Qt::Literals::StringLiterals;

//  from ../qtdeclarative/src/qml/jsruntime/qv4stringobject.cpp, line 136, as _ZN3QV44Heap10StringCtor4initEPNS_15ExecutionEngineE
namespace QV4 {
using namespace Qt::Literals::StringLiterals;
inline void Heap::StringCtor::init(QV4::ExecutionEngine *engine)
{
    Heap::FunctionObject::init(engine, QStringLiteral("String"));
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::StringCtor::init(QV4::ExecutionEngine *engine)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap10StringCtor4initEPNS_15ExecutionEngineE(
    QV4::Heap::StringCtor *self,
    QV4::ExecutionEngine *engine) {
  self->init(engine);
}
