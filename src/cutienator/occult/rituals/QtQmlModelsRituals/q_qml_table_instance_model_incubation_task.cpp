//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qqmltableinstancemodel_p.h"
#include "qqmlabstractdelegatecomponent_p.h"
#include <QtCore/QTimer>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtCore/qtyperevision.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/qmlmodels/qqmltableinstancemodel.cpp, line 659, as _ZN36QQmlTableInstanceModelIncubationTask13statusChangedEN13QQmlIncubator6StatusE
inline void QQmlTableInstanceModelIncubationTask::statusChanged(QQmlIncubator::Status status)
{
    if (!QQmlTableInstanceModel::isDoneIncubating(modelItemToIncubate))
        return;

    // We require the view to cancel any ongoing load
    // requests before the tableInstanceModel is destructed.
    Q_ASSERT(tableInstanceModel);

    tableInstanceModel->incubatorStatusChanged(this, status);
}

//  from ../qtdeclarative/src/qmlmodels/qqmltableinstancemodel.cpp, line 644, as _ZN36QQmlTableInstanceModelIncubationTask15setInitialStateEP7QObject
inline void QQmlTableInstanceModelIncubationTask::setInitialState(QObject *object)
{
    initializeRequiredProperties(
            modelItemToIncubate, object, tableInstanceModel->delegateModelAccess());
    modelItemToIncubate->setObject(object);

    const bool init = true;
    const int flatIndex = modelItemToIncubate->modelIndex();
    emit tableInstanceModel->initItem(flatIndex, object);
    emit tableInstanceModel->updateItemProperties(flatIndex, object, init);

    if (!QQmlIncubatorPrivate::get(this)->requiredProperties()->empty())
        modelItemToIncubate->destroyObjectLater();
}
//  -----------------------------------------------------------------------

//  A QQmlTableInstanceModelIncubationTask that Python can take functions over in. Every QQmlTableInstanceModelIncubationTask
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableInstanceModelIncubationTaskCall0)(const void *, int, int *);
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
typedef void (*CuteQQmlTableInstanceModelIncubationTaskCall1)(const void *, QObject *, int *);
#endif  // QT_CONFIG(qml_table_model)
class CuteQQmlTableInstanceModelIncubationTask : public QQmlTableInstanceModelIncubationTask {
public:
  using QQmlTableInstanceModelIncubationTask::QQmlTableInstanceModelIncubationTask;
  void *taken[2] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN13QQmlIncubator13statusChangedENS_6StatusE")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
    if (!std::strcmp(key, "_ZN13QQmlIncubator15setInitialStateEP7QObject")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(qml_table_model)
    return false;
  }

#if QT_CONFIG(qml_table_model)
  //  void QQmlTableInstanceModelIncubationTask::statusChanged(Status
  //      status)
  void statusChanged(QQmlIncubator::Status status) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQmlTableInstanceModelIncubationTaskCall0 call = reinterpret_cast<CuteQQmlTableInstanceModelIncubationTaskCall0>(taken[0]);
      call(this, static_cast<int>(status), &handled);
      if (handled) return;
    }
    QQmlTableInstanceModelIncubationTask::statusChanged(status);
  }
#endif  // QT_CONFIG(qml_table_model)

#if QT_CONFIG(qml_table_model)
  //  void QQmlTableInstanceModelIncubationTask::setInitialState(QObject
  //      *object)
  void setInitialState(QObject *object) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQmlTableInstanceModelIncubationTaskCall1 call = reinterpret_cast<CuteQQmlTableInstanceModelIncubationTaskCall1>(taken[1]);
      call(this, object, &handled);
      if (handled) return;
    }
    QQmlTableInstanceModelIncubationTask::setInitialState(object);
  }
#endif  // QT_CONFIG(qml_table_model)
};

//  void QQmlTableInstanceModelIncubationTask::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQmlTableInstanceModelIncubationTask13statusChangedEN13QQmlIncubator6StatusE(
    QQmlTableInstanceModelIncubationTask *self,
    QQmlIncubator::Status status) {
  self->statusChanged(status);
}

//  void QQmlTableInstanceModelIncubationTask::setInitialState(QObject
//      *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QQmlTableInstanceModelIncubationTask15setInitialStateEP7QObject(
    QQmlTableInstanceModelIncubationTask *self,
    QObject *object) {
  self->setInitialState(object);
}

//  a Python function taken by a CuteQQmlTableInstanceModelIncubationTask,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQmlTableInstanceModelIncubationTask(
    QQmlTableInstanceModelIncubationTask *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQmlTableInstanceModelIncubationTask *>(self)->take(key, call);
}

//  void QQmlTableInstanceModelIncubationTask::statusChanged(Status status)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QQmlTableInstanceModelIncubationTask13statusChangedEN13QQmlIncubator6StatusE(
    QQmlTableInstanceModelIncubationTask *self,
    QQmlIncubator::Status status) {
  self->QQmlTableInstanceModelIncubationTask::statusChanged(status);
}

#endif  // QT_CONFIG(qml_table_model)
