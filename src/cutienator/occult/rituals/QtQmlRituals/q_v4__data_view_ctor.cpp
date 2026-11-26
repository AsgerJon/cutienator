//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qv4dataview_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qv4dataview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qv4dataview_p.h>
#include <QtQml/private/qv4arraybuffer_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/qendian.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/jsruntime/qv4dataview.cpp, line 69, as _ZN3QV412DataViewCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i
namespace QV4 {
inline ReturnedValue DataViewCtor::virtualCall(const FunctionObject *f, const Value *, const Value *, int)
{
    return f->engine()->throwTypeError();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::DataViewCtor::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV412DataViewCtor10__dataTestEv(QV4::DataViewCtor *self) {
  self->__dataTest();
}

//  QV4::Heap::DataViewCtor *QV4::DataViewCtor::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DataViewCtor *ritual_ZNK3QV412DataViewCtor11d_uncheckedEv(
    const QV4::DataViewCtor *self) {
  return self->d_unchecked();
}

//  QV4::Heap::DataViewCtor *QV4::DataViewCtor::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::DataViewCtor *ritual_ZNK3QV412DataViewCtor1dEv(
    const QV4::DataViewCtor *self) {
  return self->d();
}

//  ReturnedValue QV4::DataViewCtor::virtualCall(const FunctionObject *f,
//      const Value *thisObject, const Value *argv, int argc)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV412DataViewCtor11virtualCallEPKNS_14FunctionObjectEPKNS_5ValueES6_i(
    const QV4::FunctionObject *f,
    const QV4::Value *thisObject,
    const QV4::Value *argv,
    int argc) {
  return QV4::DataViewCtor::virtualCall(f, thisObject, argv, argc);
}
