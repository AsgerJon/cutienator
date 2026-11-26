//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/6.12.0/QtQml/private/qv4propertykey_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtQml/private/qqmlcontext_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlmetaobject_p.h>
#include <QtQml/private/qqmltypedata_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4dateobject_p.h>
#include <QtQml/private/qv4identifiertable_p.h>
#include <QtQml/private/qv4lookup_p.h>
#include <QtQml/private/qv4objectproto_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4symbol_p.h>
#include <QtQml/private/qv4urlobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 878, as _ZN3QV44Heap15QQmlEnumWrapper7destroyEv
namespace QV4 {
inline void Heap::QQmlEnumWrapper::destroy()
{
    QQmlType::derefHandle(typePrivate);
    typePrivate = nullptr;
    Object::destroy();
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  const QV4::VTable *QV4::QQmlEnumWrapper::staticVTable()
extern "C" Q_DECL_EXPORT
const QV4::VTable *ritual_ZN3QV415QQmlEnumWrapper12staticVTableEv() {
  return QV4::QQmlEnumWrapper::staticVTable();
}

//  void QV4::QQmlEnumWrapper::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlEnumWrapper10__dataTestEv(
    QV4::QQmlEnumWrapper *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlEnumWrapper *QV4::QQmlEnumWrapper::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlEnumWrapper *ritual_ZNK3QV415QQmlEnumWrapper11d_uncheckedEv(
    const QV4::QQmlEnumWrapper *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlEnumWrapper *QV4::QQmlEnumWrapper::d() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlEnumWrapper *ritual_ZNK3QV415QQmlEnumWrapper1dEv(
    const QV4::QQmlEnumWrapper *self) {
  return self->d();
}

//  void QV4::QQmlEnumWrapper::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV415QQmlEnumWrapper14virtualDestroyEPNS_4Heap4BaseE(
    QV4::Heap::Base *b) {
  QV4::QQmlEnumWrapper::virtualDestroy(b);
}

//  ReturnedValue QV4::QQmlEnumWrapper::virtualGet(const Managed *m,
//      PropertyKey id, const Value *receiver, bool *hasProperty)
extern "C" Q_DECL_EXPORT
QV4::ReturnedValue ritual_ZN3QV415QQmlEnumWrapper10virtualGetEPKNS_7ManagedENS_11PropertyKeyEPKNS_5ValueEPb(
    const QV4::Managed *m,
    const QV4::PropertyKey *id,
    const QV4::Value *receiver,
    bool *hasProperty) {
  return QV4::QQmlEnumWrapper::virtualGet(m, *id, receiver, hasProperty);
}
