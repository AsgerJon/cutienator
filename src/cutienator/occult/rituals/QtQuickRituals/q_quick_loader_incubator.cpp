//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickloader_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQml/private/qqmlengine_p.h>
#include <QtQml/private/qqmlglobal_p.h>
#include <QtQml/private/qqmlcomponent_p.h>
#include <QtQml/private/qqmlincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 18, as local:qquickloader.cpp:watchedChanges
static const QQuickItemPrivate::ChangeTypes watchedChanges
    = QQuickItemPrivate::Geometry | QQuickItemPrivate::ImplicitWidth | QQuickItemPrivate::ImplicitHeight;

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 657, as _ZN21QQuickLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE
inline void QQuickLoaderIncubator::statusChanged(Status status)
{
    loader->incubatorStateChanged(status);
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 615, as _ZN21QQuickLoaderIncubator15setInitialStateEP7QObject
inline void QQuickLoaderIncubator::setInitialState(QObject *o)
{
    loader->setInitialState(o);
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 620, as _ZN19QQuickLoaderPrivate15setInitialStateEP7QObject
inline void QQuickLoaderPrivate::setInitialState(QObject *obj)
{
    Q_Q(QQuickLoader);

    QQuickItem *item = qmlobject_cast<QQuickItem*>(obj);
    if (item) {
        // If the item doesn't have an explicit size, but the Loader
        // does, then set the item's size now before bindings are
        // evaluated, otherwise we will end up resizing the item
        // later and triggering any affected bindings/anchors.
        if (widthValid() && !QQuickItemPrivate::get(item)->widthValid())
            item->setWidth(q->width());
        if (heightValid() && !QQuickItemPrivate::get(item)->heightValid())
            item->setHeight(q->height());
        item->setParentItem(q);
    }
    if (obj) {
        if (itemContext)
            QQml_setParent_noEvent(itemContext, obj);
        QQml_setParent_noEvent(obj, q);
        itemContext = nullptr;
    }

    if (initialPropertyValues.isUndefined())
        return;

    QQmlComponentPrivate *d = QQmlComponentPrivate::get(component);
    Q_ASSERT(d && d->engine());
    QV4::ExecutionEngine *v4 = d->engine()->handle();
    Q_ASSERT(v4);
    QV4::Scope scope(v4);
    QV4::ScopedValue ipv(scope, initialPropertyValues.value());
    QV4::Scoped<QV4::QmlContext> qmlContext(scope, qmlCallingContext.value());
    auto incubatorPriv = QQmlIncubatorPrivate::get(incubator);
    d->initializeObjectWithInitialProperties(qmlContext, ipv, obj, incubatorPriv->requiredProperties());
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 662, as _ZN19QQuickLoaderPrivate21incubatorStateChangedEN13QQmlIncubator6StatusE
inline void QQuickLoaderPrivate::incubatorStateChanged(QQmlIncubator::Status status)
{
    Q_Q(QQuickLoader);
    if (status == QQmlIncubator::Loading || status == QQmlIncubator::Null)
        return;

    if (status == QQmlIncubator::Ready) {
        object = incubator->object();
        item = qmlobject_cast<QQuickItem*>(object);
        emit q->itemChanged();
        initResize();
        incubator->clear();
    } else if (status == QQmlIncubator::Error) {
        if (!incubator->errors().isEmpty())
            QQmlEnginePrivate::warning(qmlEngine(q), incubator->errors());
        delete itemContext;
        itemContext = nullptr;
        delete incubator->object();
        source = QUrl();
        emit q->itemChanged();
    }
    if (loadingFromSource)
        emit q->sourceChanged();
    else
        emit q->sourceComponentChanged();
    updateStatus();
    emit q->progressChanged();
    if (status == QQmlIncubator::Ready)
        emit q->loaded();
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 101, as _ZN19QQuickLoaderPrivate10initResizeEv
inline void QQuickLoaderPrivate::initResize()
{
    if (!item)
        return;
    QQuickItemPrivate *p = QQuickItemPrivate::get(item);
    p->addItemChangeListener(this, watchedChanges);
    _q_updateSize();
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 994, as _ZN19QQuickLoaderPrivate12updateStatusEv
inline void QQuickLoaderPrivate::updateStatus()
{
    Q_Q(QQuickLoader);
    auto newStatus = computeStatus();
    if (status != newStatus) {
        status = newStatus;
        emit q->statusChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 900, as _ZN19QQuickLoaderPrivate13_q_updateSizeEb
inline void QQuickLoaderPrivate::_q_updateSize(bool loaderGeometryChanged)
{
    Q_Q(QQuickLoader);
    if (!item)
        return;

    const bool needToUpdateWidth = loaderGeometryChanged && q->widthValid();
    const bool needToUpdateHeight = loaderGeometryChanged && q->heightValid();

    if (needToUpdateWidth && needToUpdateHeight) {
        /* setSize keeps bindings intact (for backwards compatibility reasons),
           but here we actually want the loader to control the size, so any
           prexisting bindings ought to be removed
        */
        auto *itemPriv = QQuickItemPrivate::get(item);
        // takeBinding  would work without the check, but this is more efficient
        // for the common case where we don't have a binding
        if (itemPriv->width.hasBinding())
            itemPriv->width.takeBinding();
        if (itemPriv->height.hasBinding())
            itemPriv->height.takeBinding();
        item->setSize(QSizeF(q->width(), q->height()));
    } else if (needToUpdateWidth) {
        item->setWidth(q->width());
    } else if (needToUpdateHeight) {
        item->setHeight(q->height());
    }

    if (updatingSize)
        return;

    updatingSize = true;

    q->setImplicitSize(getImplicitWidth(), getImplicitHeight());

    updatingSize = false;
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 959, as _ZNK19QQuickLoaderPrivate13computeStatusEv
inline QQuickLoader::Status QQuickLoaderPrivate::computeStatus() const
{
    if (!active)
        return QQuickLoader::Status::Null;

    if (component) {
        switch (component->status()) {
        case QQmlComponent::Loading:
            return QQuickLoader::Status::Loading;
        case QQmlComponent::Error:
            return QQuickLoader::Status::Error;
        case QQmlComponent::Null:
            return QQuickLoader::Status::Null;
        default:
            break;
        }
    }

    if (incubator) {
        switch (incubator->status()) {
        case QQmlIncubator::Loading:
            return QQuickLoader::Status::Loading;
        case QQmlIncubator::Error:
            return QQuickLoader::Status::Error;
        default:
            break;
        }
    }

    if (object)
        return QQuickLoader::Status::Ready;

    return source.isEmpty() ? QQuickLoader::Status::Null : QQuickLoader::Status::Error;
}
//  -----------------------------------------------------------------------

//  Only a class built on QQuickLoaderIncubator may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQQuickLoaderIncubator : QQuickLoaderIncubator {
  using QQuickLoaderIncubator::statusChanged;
  using QQuickLoaderIncubator::setInitialState;
};

//  QQuickLoaderIncubator::QQuickLoaderIncubator(QQuickLoaderPrivate *l,
//      IncubationMode mode)
extern "C" Q_DECL_EXPORT
QQuickLoaderIncubator *ritual_ZN21QQuickLoaderIncubatorC1EP19QQuickLoaderPrivateN13QQmlIncubator14IncubationModeE(
    QQuickLoaderPrivate *l,
    QQmlIncubator::IncubationMode mode) {
  return new QQuickLoaderIncubator(l, mode);
}

//  void QQuickLoaderIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuickLoaderIncubator *self,
    QQmlIncubator::Status a0) {
  self->statusChanged(a0);
}

//  void QQuickLoaderIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickLoaderIncubator15setInitialStateEP7QObject(
    QQuickLoaderIncubator *self,
    QObject *a0) {
  self->setInitialState(a0);
}

//  void QQuickLoaderIncubator::statusChanged(Status a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickLoaderIncubator13statusChangedEN13QQmlIncubator6StatusE(
    QQuickLoaderIncubator *self,
    QQmlIncubator::Status a0) {
  static_cast<OwnQQuickLoaderIncubator *>(self)->OwnQQuickLoaderIncubator::statusChanged(
      a0);
}

//  void QQuickLoaderIncubator::setInitialState(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN21QQuickLoaderIncubator15setInitialStateEP7QObject(
    QQuickLoaderIncubator *self,
    QObject *a0) {
  static_cast<OwnQQuickLoaderIncubator *>(self)->OwnQQuickLoaderIncubator::setInitialState(
      a0);
}
