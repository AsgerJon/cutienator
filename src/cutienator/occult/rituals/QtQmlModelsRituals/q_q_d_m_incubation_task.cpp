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
#include <cstring>
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
#include <QtQmlModels/private/qqmllistcompositor_p.h>
#include <QtCore/qvarlengtharray.h>
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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 2992, as local:qqmldelegatemodel.cpp:GroupEmitterListIt
typedef QQmlDelegateModelGroupEmitterList::iterator GroupEmitterListIt;

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

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1004, as _ZN18QQDMIncubationTask28initializeRequiredPropertiesEP21QQmlDelegateModelItemP7QObjectN17QQmlDelegateModel19DelegateModelAccessE
inline void QQDMIncubationTask::initializeRequiredProperties(
        QQmlDelegateModelItem *modelItemToIncubate, QObject *object,
        QQmlDelegateModel::DelegateModelAccess access)
{
    // QQmlObjectCreator produces a private internal context.
    // We can always attach the extra object there.
    QQmlData *d = QQmlData::get(object);
    if (auto contextData = d ? d->context : nullptr)
        contextData->setExtraObject(modelItemToIncubate);

    Q_ASSERT(modelItemToIncubate->delegate());
    const bool isBound = QQmlComponentPrivate::get(modelItemToIncubate->delegate())->isBound();

    auto incubatorPriv = QQmlIncubatorPrivate::get(this);
    if (incubatorPriv->hadTopLevelRequiredProperties()) {
        // If we have required properties, we clear the context object
        // so that the model role names are not polluting the context.
        // Unless the context is bound, in which case we have never set the context object.
        if (incubating && !isBound) {
            Q_ASSERT(incubating->contextData());
            incubating->contextData()->setContextObject(nullptr);
        }
        if (proxyContext) {
            proxyContext->setContextObject(nullptr);
        }

        // Retrieve the metaObject before the potential return so that the accessors have a chance
        // to perform some finalization in case they produce a dynamic metaobject. Here we know for
        // sure that we are using required properties.
        const QMetaObject *qmlMetaObject = modelItemToIncubate->metaObject();

        RequiredProperties *requiredProperties = incubatorPriv->requiredProperties();
        if (requiredProperties->empty())
            return;

        const RequiredPropertiesInitializer initializer(
                QQmlEnginePrivate::get(incubatorPriv->enginePriv),
                object, requiredProperties, access);

        // if a required property was not in the model, it might still be a static property of the
        // QQmlDelegateModelItem or one of its derived classes this is the case for index, row,
        // column, model and more
        // the most derived subclasses of QQmlDelegateModelItem are QQmlDMAbstractItemModelData and
        // QQmlDMObjectData at depth 2, so 4 should be plenty

        // we first check the dynamic meta object for properties originating from the model
        // contains abstractitemmodelproperties
        initializer(qmlMetaObject, modelItemToIncubate);

        auto delegateModelItemSubclassMO = qmlMetaObject->superClass();
        initializer(delegateModelItemSubclassMO, modelItemToIncubate);

        while (strcmp(delegateModelItemSubclassMO->className(),
                      modelItemToIncubate->staticMetaObject.className())) {
            delegateModelItemSubclassMO = delegateModelItemSubclassMO->superClass();
            initializer(delegateModelItemSubclassMO, modelItemToIncubate);
        }

        if (proxiedObject)
            initializer(proxiedObject->metaObject(), proxiedObject.data());

    } else {
        // To retain compatibility, we cannot enable structured model data if the data is passed
        // via context properties.
        modelItemToIncubate->disableStructuredModelData();

        if (!isBound)
            modelItemToIncubate->contextData()->setContextObject(modelItemToIncubate);
        if (proxiedObject)
            proxyContext->setContextObject(proxiedObject);

        // Retrieve the metaObject() once so that the accessors have a chance to perform some
        // finalization in case they produce a dynamic metaobject. For example, they might be
        // inclined to create a propertyCache now because there are no required properties and any
        // revisioned properties should be hidden after all. Here is the first time we know for
        // sure whether we are using context properties.
        modelItemToIncubate->metaObject();
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 921, as _ZN24QQmlDelegateModelPrivate15emitInitPackageEP18QQDMIncubationTaskP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitInitPackage(QQDMIncubationTask *incubationTask, QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->initPackage(incubationTask->index[i], package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1180, as _ZN24QQmlDelegateModelPrivate15removeCacheItemEP21QQmlDelegateModelItem
inline void QQmlDelegateModelPrivate::removeCacheItem(QQmlDelegateModelItem *cacheItem)
{
    int cidx = m_cache.lastIndexOf(cacheItem);
    if (cidx >= 0) {
        m_compositor.clearFlags(Compositor::Cache, cidx, 1, Compositor::CacheFlag);
        m_cache.removeAt(cidx);
    }
    Q_ASSERT(m_cache.size() == m_compositor.count(Compositor::Cache));
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 1096, as _ZN24QQmlDelegateModelPrivate16releaseIncubatorEP18QQDMIncubationTask
inline void QQmlDelegateModelPrivate::releaseIncubator(QQDMIncubationTask *incubationTask)
{
    Q_Q(QQmlDelegateModel);
    if (!incubationTask->isError())
        incubationTask->clear();
    m_finishedIncubating.append(incubationTask);
    if (!m_incubatorCleanupScheduled) {
        m_incubatorCleanupScheduled = true;
        QCoreApplication::postEvent(q, new QEvent(QEvent::User));
    }
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 915, as _ZN24QQmlDelegateModelPrivate18emitCreatedPackageEP18QQDMIncubationTaskP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitCreatedPackage(QQDMIncubationTask *incubationTask, QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->createdPackage(incubationTask->index[i], package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 927, as _ZN24QQmlDelegateModelPrivate21emitDestroyingPackageEP13QQuickPackage
inline void QQmlDelegateModelPrivate::emitDestroyingPackage(QQuickPackage *package)
{
    for (int i = 1; i < m_groupCount; ++i)
        QQmlDelegateModelGroupPrivate::get(m_groups[i])->destroyingPackage(package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmldelegatemodel.cpp, line 3000, as _ZN29QQmlDelegateModelGroupPrivate11initPackageEiP13QQuickPackage
inline void QQmlDelegateModelGroupPrivate::initPackage(int index, QQuickPackage *package)
{
    for (GroupEmitterListIt it = emitters.begin(), end = emitters.end(); it != end; ++it)
        it->initPackage(index, package);
}

//  from ../qtdeclarative/src/qmlmodels/qqmllistcompositor.cpp, line 316, as _ZNK18QQmlListCompositor5countENS_5GroupE
inline int QQmlListCompositor::count(Group group) const
{
    return m_end.index[group];
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

//  void QQDMIncubationTask::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQDMIncubationTask13statusChangedEN13QQmlIncubator6StatusE(
    QQDMIncubationTask *self,
    QQmlIncubator::Status a0) {
  self->statusChanged(a0);
}

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

//  void QQDMIncubationTask::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN18QQDMIncubationTask15setInitialStateEP7QObject(
    QQDMIncubationTask *self,
    QObject *a0) {
  self->QQDMIncubationTask::setInitialState(a0);
}

#endif  // QT_CONFIG(qml_delegate_model)
#endif  // QT_CONFIG(qml_delegate_model)
