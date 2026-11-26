//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmltypewrapper_p.h>
#include <QtQml/6.12.0/QtQml/private/qqmltype_p.h>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
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

//  from ../qtdeclarative/src/qml/qml/qqmltypewrapper.cpp, line 885, as _ZNK3QV44Heap15QQmlEnumWrapper4typeEv
namespace QV4 {
inline QQmlType Heap::QQmlEnumWrapper::type() const
{
    return QQmlType(typePrivate);
}
}  // namespace QV4
//  -----------------------------------------------------------------------

//  void QV4::Heap::QQmlEnumWrapper::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15QQmlEnumWrapper4initEv(
    QV4::Heap::QQmlEnumWrapper *self) {
  self->init();
}

//  void QV4::Heap::QQmlEnumWrapper::destroy()
extern "C" Q_DECL_EXPORT
void ritual_ZN3QV44Heap15QQmlEnumWrapper7destroyEv(
    QV4::Heap::QQmlEnumWrapper *self) {
  self->destroy();
}

//  QQmlType QV4::Heap::QQmlEnumWrapper::type() const
extern "C" Q_DECL_EXPORT
QQmlType *ritual_ZNK3QV44Heap15QQmlEnumWrapper4typeEv(
    const QV4::Heap::QQmlEnumWrapper *self) {
  return new QQmlType(self->type());
}
