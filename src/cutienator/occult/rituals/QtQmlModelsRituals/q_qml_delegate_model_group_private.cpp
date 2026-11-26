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
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2992, as local:qqmldelegatemodel.cpp:GroupEmitterListIt
typedef QQmlDelegateModelGroupEmitterList::iterator GroupEmitterListIt;

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2959, as _ZN29QQmlDelegateModelGroupPrivate8setModelEP17QQmlDelegateModelN18QQmlListCompositor5GroupE
inline void QQmlDelegateModelGroupPrivate::setModel(QQmlDelegateModel *m, Compositor::Group g)
{
    Q_ASSERT(!model);
    model = m;
    group = g;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2966, as _ZN29QQmlDelegateModelGroupPrivate18isChangedConnectedEv
inline bool QQmlDelegateModelGroupPrivate::isChangedConnected()
{
    Q_Q(QQmlDelegateModelGroup);
    IS_SIGNAL_CONNECTED(q, QQmlDelegateModelGroup, changed, (const QJSValue &,const QJSValue &));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2985, as _ZN29QQmlDelegateModelGroupPrivate16emitModelUpdatedEb
inline void QQmlDelegateModelGroupPrivate::emitModelUpdated(bool reset)
{
    for (QQmlDelegateModelGroupEmitterList::iterator it = emitters.begin(); it != emitters.end(); ++it)
        it->emitModelUpdated(changeSet, reset);
    changeSet.clear();
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2994, as _ZN29QQmlDelegateModelGroupPrivate14createdPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupPrivate::createdPackage(int index, QQuickPackage *package)
{
    for (GroupEmitterListIt it = emitters.begin(), end = emitters.end(); it != end; ++it)
        it->createdPackage(index, package);
}
//  -----------------------------------------------------------------------

//  QQmlDelegateModelGroup *QQmlDelegateModelGroupPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroup *ritual_ZN29QQmlDelegateModelGroupPrivate6q_funcEv(
    QQmlDelegateModelGroupPrivate *self) {
  return self->q_func();
}

//  const QQmlDelegateModelGroup *QQmlDelegateModelGroupPrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQmlDelegateModelGroup *ritual_ZNK29QQmlDelegateModelGroupPrivate6q_funcEv(
    const QQmlDelegateModelGroupPrivate *self) {
  return self->q_func();
}

//  QQmlDelegateModelGroupPrivate::QQmlDelegateModelGroupPrivate()
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroupPrivate *ritual_ZN29QQmlDelegateModelGroupPrivateC1Ev() {
  return new QQmlDelegateModelGroupPrivate();
}

//  QQmlDelegateModelGroupPrivate
//      *QQmlDelegateModelGroupPrivate::get(QQmlDelegateModelGroup *group)
extern "C" Q_DECL_EXPORT
QQmlDelegateModelGroupPrivate *ritual_ZN29QQmlDelegateModelGroupPrivate3getEP22QQmlDelegateModelGroup(
    QQmlDelegateModelGroup *group) {
  return QQmlDelegateModelGroupPrivate::get(group);
}

//  void QQmlDelegateModelGroupPrivate::setModel(QQmlDelegateModel *model,
//      Compositor::Group group)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupPrivate8setModelEP17QQmlDelegateModelN18QQmlListCompositor5GroupE(
    QQmlDelegateModelGroupPrivate *self,
    QQmlDelegateModel *model,
    const Compositor::Group *group) {
  self->setModel(model, *group);
}

//  bool QQmlDelegateModelGroupPrivate::isChangedConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN29QQmlDelegateModelGroupPrivate18isChangedConnectedEv(
    QQmlDelegateModelGroupPrivate *self) {
  return self->isChangedConnected();
}

//  void QQmlDelegateModelGroupPrivate::emitModelUpdated(bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupPrivate16emitModelUpdatedEb(
    QQmlDelegateModelGroupPrivate *self,
    bool reset) {
  self->emitModelUpdated(reset);
}

//  void QQmlDelegateModelGroupPrivate::createdPackage(int index,
//      QQuickPackage *package)
extern "C" Q_DECL_EXPORT
void ritual_ZN29QQmlDelegateModelGroupPrivate14createdPackageEiP13QQuickPackage(
    QQmlDelegateModelGroupPrivate *self,
    int index,
    QQuickPackage *package) {
  self->createdPackage(index, package);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
