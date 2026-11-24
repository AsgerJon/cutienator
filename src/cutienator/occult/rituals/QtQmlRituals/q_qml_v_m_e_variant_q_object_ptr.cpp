//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQml/6.12.0/QtQml/private/qtqmlglobal_p.h>
#include <QtQml/QtQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/6.12.0/QtQml/private/qqmlvmemetaobject_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQml/private/qqmlvmemetaobject_p.h>
#include <QtQml/private/qqmlrefcount_p.h>
#include <QtQml/private/qqmlpropertyvalueinterceptor_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlpropertycachecreator_p.h>
#include <QtQml/private/qqmlpropertycachemethodarguments_p.h>
#include <QtQml/private/qqmlvaluetypewrapper_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4jscall_p.h>
#include <QtQml/private/qv4object_p.h>
#include <QtQml/private/qv4qobjectwrapper_p.h>
#include <QtQml/private/qv4runtime_p.h>
#include <QtQml/private/qv4scopedvalue_p.h>
#include <QtQml/private/qv4sequenceobject_p.h>
#include <QtQml/private/qv4variantassociationobject_p.h>
#include <QtQml/private/qv4variantobject_p.h>
#include <QtCore/qmetasequence.h>
#include <climits> // for CHAR_BIT
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qml/qml/qqmlvmemetaobject.cpp, line 209, as _ZN24QQmlVMEVariantQObjectPtr15setGuardedValueEP7QObjectP17QQmlVMEMetaObjecti
inline void QQmlVMEVariantQObjectPtr::setGuardedValue(QObject *obj, QQmlVMEMetaObject *target, int index)
{
    m_target = target;
    m_index = index;
    setObject(obj);
}
//  -----------------------------------------------------------------------

//  void QQmlVMEVariantQObjectPtr::setGuardedValue(QObject *obj,
//      QQmlVMEMetaObject *target, int index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlVMEVariantQObjectPtr15setGuardedValueEP7QObjectP17QQmlVMEMetaObjecti(
    QQmlVMEVariantQObjectPtr *self,
    QObject *obj,
    QQmlVMEMetaObject *target,
    int index) {
  self->setGuardedValue(obj, target, index);
}

//  QQmlVMEVariantQObjectPtr::~QQmlVMEVariantQObjectPtr()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QQmlVMEVariantQObjectPtrD1Ev(
    QQmlVMEVariantQObjectPtr *self) {
  delete self;
}
