//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_delegate_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmldelegatemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1237, as _ZN24QQmlDelegateModelPrivate15setInitialStateEP18QQDMIncubationTaskP7QObject
inline void QQmlDelegateModelPrivate::setInitialState(QQDMIncubationTask *incubationTask, QObject *o)
{
    QQmlDelegateModelItem *cacheItem = incubationTask->incubating;
    incubationTask->initializeRequiredProperties(
            incubationTask->incubating, o, m_adaptorModel.delegateModelAccess);
    cacheItem->setObject(o);

    if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(o))
        emitInitPackage(incubationTask, package);
    else
        emitInitItem(incubationTask, o);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 921, as _ZN24QQmlDelegateModelPrivate15emitInitPackageEP18QQDMIncubationTaskP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitInitPackage(QQDMIncubationTask *incubationTask, QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->initPackage(incubationTask->index[i], package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1227, as _ZN18QQDMIncubationTask15setInitialStateEP7QObject
inline void QQDMIncubationTask::setInitialState(QObject *o)
{
    vdm->setInitialState(this, o);
}
//  -----------------------------------------------------------------------

//  A QQDMIncubationTask that Python can take functions over in. Every QQDMIncubationTask
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQDMIncubationTaskCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
typedef void (*CuteQQDMIncubationTaskCall1)(const void *, QObject *, int *);
#endif  // QT_CONFIG(qml_delegate_model)
class CuteQQDMIncubationTask : public QQDMIncubationTask {
public:
  using QQDMIncubationTask::QQDMIncubationTask;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQmlIncubator13statusChangedENS_6StatusE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
#if QT_CONFIG(qml_delegate_model)
    if (!std::strcmp(key, "_ZN13QQmlIncubator15setInitialStateEP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_delegate_model)
    return false;
  }

#if QT_CONFIG(qml_delegate_model)
  //  void QQDMIncubationTask::statusChanged(Status a0)
  void statusChanged(QQmlIncubator::Status a0) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQDMIncubationTaskCall0 call = reinterpret_cast<CuteQQDMIncubationTaskCall0>(taken[0]);
      call(this, static_cast<int>(a0), &handled);
      if (handled) return;
    }
    QQDMIncubationTask::statusChanged(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)

#if QT_CONFIG(qml_delegate_model)
  //  void QQDMIncubationTask::setInitialState(QObject *a0)
  void setInitialState(QObject *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQDMIncubationTaskCall1 call = reinterpret_cast<CuteQQDMIncubationTaskCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQDMIncubationTask::setInitialState(a0);
  }
#endif  // QT_CONFIG(qml_delegate_model)
};

//  void QQDMIncubationTask::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQDMIncubationTask15setInitialStateEP7QObject(
    QQDMIncubationTask *self,
    QObject *a0) {
  self->setInitialState(a0);
}

//  a Python function taken by a CuteQQDMIncubationTask, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQDMIncubationTask(
    QQDMIncubationTask *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQDMIncubationTask *>(self)->take(key, call);
}

#endif  // QT_CONFIG(qml_delegate_model)
