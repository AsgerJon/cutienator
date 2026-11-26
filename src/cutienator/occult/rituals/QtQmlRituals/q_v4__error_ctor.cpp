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

//  from ../qtdeclarative/src/qml/jsruntime/qv4errorobject.cpp, line 202, as _ZN3QV49ErrorCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue ErrorCtor::virtualCall(const FunctionObject *f, const Value *, const Value *argv, int argc)
{
    return f->callAsConstructor(argv, argc);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::ErrorCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV49ErrorCtor10__dataTestEv(QV4::ErrorCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::ErrorCtor *QV4::ErrorCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorCtor *ritual_ZNK3QV49ErrorCtor11d_uncheckedEv(
    const QV4::ErrorCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::ErrorCtor *QV4::ErrorCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::ErrorCtor *ritual_ZNK3QV49ErrorCtor1dEv(
    const QV4::ErrorCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::ErrorCtor::virtualCall(const FunctionObject *f, const
//      Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV49ErrorCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::ErrorCtor::virtualCall(f, thisObject, argv, argc);
}
