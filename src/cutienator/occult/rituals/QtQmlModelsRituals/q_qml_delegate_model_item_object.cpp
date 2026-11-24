//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmldelegatemodel_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtCore/private/qcoreapplication_p.h>
#include <QtQml/private/qjsvalue_p.h>
#include <QtCore/private/qmetaobjectbuilder_p.h>
#include <QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#include <QtQmlModels/private/qqmladaptormodel_p.h>
#include <QtQml/private/qqmlanybinding_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlpropertytopropertybinding_p.h>
#include <QtQmlModels/private/qqmltableinstancemodel_p.h>
#include <QtQmlModels/private/qquickpackage_p.h>
#include <QtQml/private/qv4functionobject_p.h>
#include <QtQml/private/qv4objectiterator_p.h>
#include <QtQml/private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2493, as _ZN3QV44Heap27QQmlDelegateModelItemObject7destroyEv
inline void QV4::Heap::QQmlDelegateModelItemObject::destroy()
{
    // We need to first destroy the reference and then call dispose() because dispose() only
    // does something if the item is not referenced anymore.
    QQmlDelegateModelItem *disposable = item();
    reinterpret_cast<QQmlDelegateModelItem::ScriptReference *>(&ref)->~ScriptReference();
    disposable->dispose();
    Object::destroy();
}
//  -----------------------------------------------------------------------

//  void QQmlDelegateModelItemObject::__dataTest()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlDelegateModelItemObject10__dataTestEv(
    QQmlDelegateModelItemObject *self) {
  self->__dataTest();
}

//  QV4::Heap::QQmlDelegateModelItemObject
//      *QQmlDelegateModelItemObject::d_unchecked() const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlDelegateModelItemObject *ritual_ZNK27QQmlDelegateModelItemObject11d_uncheckedEv(
    const QQmlDelegateModelItemObject *self) {
  return self->d_unchecked();
}

//  QV4::Heap::QQmlDelegateModelItemObject *QQmlDelegateModelItemObject::d()
//      const
extern "C" Q_DECL_EXPORT
QV4::Heap::QQmlDelegateModelItemObject *ritual_ZNK27QQmlDelegateModelItemObject1dEv(
    const QQmlDelegateModelItemObject *self) {
  return self->d();
}

//  void QQmlDelegateModelItemObject::virtualDestroy(QV4::Heap::Base *b)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQmlDelegateModelItemObject14virtualDestroyEPN3QV44Heap4BaseE(
    QV4::Heap::Base *b) {
  QQmlDelegateModelItemObject::virtualDestroy(b);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
