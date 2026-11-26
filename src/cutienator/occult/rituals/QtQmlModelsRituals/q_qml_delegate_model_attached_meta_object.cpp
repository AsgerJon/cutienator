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
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1473, as _ZN24QQmlDelegateModelPrivate12removeGroupsEN18QQmlListCompositor8iteratorEiNS0_5GroupEi
inline void QQmlDelegateModelPrivate::removeGroups(
        Compositor::iterator from, int count, Compositor::Group group, int groupFlags)
{
    QList<Compositor::Remove> removes;
    m_compositor.clearFlags(from, count, group, groupFlags, &removes);
    itemsRemoved(removes);
    emitChanges();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1464, as _ZN24QQmlDelegateModelPrivate9addGroupsEN18QQmlListCompositor8iteratorEiNS0_5GroupEi
inline void QQmlDelegateModelPrivate::addGroups(
        Compositor::iterator from, int count, Compositor::Group group, int groupFlags)
{
    QList<Compositor::Insert> inserts;
    m_compositor.setFlags(from, count, group, groupFlags, &inserts);
    itemsInserted(inserts);
    emitChanges();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2657, as _ZN35QQmlDelegateModelAttachedMetaObjectD1Ev
inline QQmlDelegateModelAttachedMetaObject::~QQmlDelegateModelAttachedMetaObject()
{
    ::free(metaObject);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2662, as _ZN35QQmlDelegateModelAttachedMetaObject15objectDestroyedEP7QObject
inline void QQmlDelegateModelAttachedMetaObject::objectDestroyed(QObject *)
{
    release();
}
//  -----------------------------------------------------------------------

//  QQmlDelegateModelAttachedMetaObject::~QQmlDelegateModelAttachedMetaObject
//      ()
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQmlDelegateModelAttachedMetaObjectD1Ev(
    QQmlDelegateModelAttachedMetaObject *self) {
  delete self;
}

//  void QQmlDelegateModelAttachedMetaObject::objectDestroyed(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN35QQmlDelegateModelAttachedMetaObject15objectDestroyedEP7QObject(
    QQmlDelegateModelAttachedMetaObject *self,
    QObject *a0) {
  self->objectDestroyed(a0);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
