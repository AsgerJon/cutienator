//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQmlModels/qtqmlmodelsglobal.h>
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#if QT_CONFIG(qml_table_model)
#if QT_CONFIG(qml_table_model)
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmltableinstancemodel_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/private/qqmltableinstancemodel_p.h>
#include <QtQmlModels/private/qqmlabstractdelegatecomponent_p.h>
#include <QtCore/QTimer>
#include <QtQml/private/qqmlincubator_p.h>
#include <QtQmlModels/private/qqmlchangeset_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtCore/qtyperevision.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 933, as local:qqmldelegatemodel.cpp:isDoneIncubating
static bool isDoneIncubating(QQmlIncubator::Status status)
{
     return status == QQmlIncubator::Ready || status == QQmlIncubator::Error;
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 938, as local:qqmldelegatemodel.cpp:RequiredPropertiesInitializer
struct RequiredPropertiesInitializer
{
    Q_DISABLE_COPY_MOVE(RequiredPropertiesInitializer)
public:
    RequiredPropertiesInitializer(
            QQmlEngine *engine, QObject *targetObject, RequiredProperties *requiredProperties,
            QQmlDelegateModel::DelegateModelAccess access)
        : engine(engine)
        , targetObject(targetObject)
        , requiredProperties(requiredProperties)
        , access(access)
    {}

    template<typename ModelObjectType>
    void operator()(const QMetaObject *modelMetaObject, ModelObjectType *modelObject) const
    {
        const int end = modelMetaObject->propertyCount() + modelMetaObject->propertyOffset();
        for (int i = modelMetaObject->propertyOffset(); i < end; ++i) {
            auto prop = modelMetaObject->property(i);
            if (!prop.name())
                continue;
            const QString propName = QString::fromUtf8(prop.name());

            bool wasInRequired = false;
            QQmlProperty targetProp = QQmlComponentPrivate::removePropertyFromRequired(
                    targetObject, propName, requiredProperties,
                    engine, &wasInRequired);
            if (!wasInRequired)
                continue;

            QQmlProperty sourceProp(modelObject, propName);
            QQmlAnyBinding forward = QQmlPropertyToPropertyBinding::create(
                    engine, sourceProp, targetProp);
            if (access != QQmlDelegateModel::Qt5ReadWrite)
                forward.setSticky();
            forward.installOn(targetProp);

            if (access != QQmlDelegateModel::ReadWrite || !sourceProp.isWritable())
                continue;

            QQmlAnyBinding reverse = QQmlPropertyToPropertyBinding::create(
                    engine, targetProp, sourceProp);
            reverse.setSticky();
            if constexpr (std::is_base_of_v<QQmlDelegateModelItem, ModelObjectType>) {
                // Temporarily take away the metaobject so that the property can't actually be
                // written. It shouldn't be written since we've just synchronized it the other way
                // when installing the "forward" binding.
                QQmlDelegateModelReadOnlyMetaObject readonly(modelObject, i);
                reverse.installOn(sourceProp);
            } else {
                // It's only not a QQmlDelegateModelItem if the model is actually an ObjectModel.
                // In that case, we hope that the generic equality check when setting a property
                // is enough to de-bounce it.
                reverse.installOn(sourceProp);
            }
        }
    }

private:
    QQmlEngine *engine = nullptr;
    QObject *targetObject = nullptr;
    RequiredProperties *requiredProperties = nullptr;
    QQmlDelegateModel::DelegateModelAccess access
            = QQmlDelegateModel::DelegateModelAccess::ReadOnly;
};

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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1084, as _ZN18QQDMIncubationTask13statusChangedEN13QQmlIncubator6StatusE
inline void QQDMIncubationTask::statusChanged(Status status)
{
    if (vdm) {
        vdm->incubatorStatusChanged(this, status);
    } else if (isDoneIncubating(status)) {
        Q_ASSERT(incubating);
        // The model was deleted from under our feet, cleanup ourselves
        incubating->destroyObject();
        incubating->deleteLater();
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1227, as _ZN18QQDMIncubationTask15setInitialStateEP7QObject
inline void QQDMIncubationTask::setInitialState(QObject *o)
{
    vdm->setInitialState(this, o);
}

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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1190, as _ZN24QQmlDelegateModelPrivate22incubatorStatusChangedEP18QQDMIncubationTaskN13QQmlIncubator6StatusE
inline void QQmlDelegateModelPrivate::incubatorStatusChanged(QQDMIncubationTask *incubationTask, QQmlIncubator::Status status)
{
    if (!isDoneIncubating(status))
        return;

    const QList<QQmlError> incubationTaskErrors = incubationTask->errors();

    QQmlDelegateModelItem *cacheItem = incubationTask->incubating;
    cacheItem->clearIncubationTask();
    incubationTask->incubating = nullptr;
    releaseIncubator(incubationTask);

    QObject *object = cacheItem->object();
    if (status == QQmlIncubator::Ready) {
        QQmlDelegateModelItem::ObjectReference guard(cacheItem);
        if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object))
            emitCreatedPackage(incubationTask, package);
        else
            emitCreatedItem(incubationTask, object);
    } else if (status == QQmlIncubator::Error) {
        qmlInfo(m_delegate, incubationTaskErrors + m_delegate->errors()) << "Cannot create delegate";
    }

    if (!cacheItem->isObjectReferenced()) {
        if (QQuickPackage *package = qmlobject_cast<QQuickPackage *>(object))
            emitDestroyingPackage(package);
        else
            emitDestroyingItem(object);
        cacheItem->destroyObject();

        if (!cacheItem->isScriptReferenced()) {
            removeCacheItem(cacheItem);
            delete cacheItem;
        }
    }
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
#endif  // QT_CONFIG(qml_table_model)
