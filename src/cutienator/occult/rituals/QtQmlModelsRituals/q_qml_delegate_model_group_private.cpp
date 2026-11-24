//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmldelegatemodel_p_p.h"
#include <QtQml/qqmlinfo.h>
#include <private/qabstractitemmodel_p.h>
#include <private/qcoreapplication_p.h>
#include <private/qjsvalue_p.h>
#include <private/qmetaobjectbuilder_p.h>
#include <private/qqmlabstractdelegatecomponent_p.h>
#include <private/qqmladaptormodel_p.h>
#include <private/qqmlanybinding_p.h>
#include <private/qqmlchangeset_p.h>
#include <private/qqmlcomponent_p.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlpropertytopropertybinding_p.h>
#include <private/qqmltableinstancemodel_p.h>
#include <private/qquickpackage_p.h>
#include <private/qv4functionobject_p.h>
#include <private/qv4objectiterator_p.h>
#include <private/qv4value_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

#endif  // QT_CONFIG(qml_delegate_model)
