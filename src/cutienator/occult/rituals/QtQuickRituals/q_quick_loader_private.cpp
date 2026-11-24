//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickloader_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickloader_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickloader_p_p.h"
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <private/qqmlengine_p.h>
#include <private/qqmlglobal_p.h>
#include <private/qqmlcomponent_p.h>
#include <private/qqmlincubator_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 21, as _ZN19QQuickLoaderPrivateC1Ev
inline QQuickLoaderPrivate::QQuickLoaderPrivate()
    : item(nullptr), object(nullptr), itemContext(nullptr), incubator(nullptr), updatingSize(false),
      active(true), loadingFromSource(false), asynchronous(false), status(computeStatus())
{
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 27, as _ZN19QQuickLoaderPrivateD1Ev
inline QQuickLoaderPrivate::~QQuickLoaderPrivate()
{
    delete itemContext;
    itemContext = nullptr;
    delete incubator;
    disposeInitialPropertyValues();
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 35, as _ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem *resizeItem, QQuickGeometryChange change,
                                              const QRectF &oldGeometry)
{
    if (resizeItem == item)
        _q_updateSize(false);
    QQuickItemChangeListener::itemGeometryChanged(resizeItem, change, oldGeometry);
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 43, as _ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuickItem
inline void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem *)
{
    Q_Q(QQuickLoader);
    q->setImplicitWidth(getImplicitWidth());
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 49, as _ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuickItem
inline void QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *)
{
    Q_Q(QQuickLoader);
    q->setImplicitHeight(getImplicitHeight());
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

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 586, as _ZN19QQuickLoaderPrivate28disposeInitialPropertyValuesEv
inline void QQuickLoaderPrivate::disposeInitialPropertyValues()
{
    initialPropertyValues.clear();
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

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 1004, as _ZN19QQuickLoaderPrivate15createComponentEv
inline void QQuickLoaderPrivate::createComponent()
{
    Q_Q(QQuickLoader);
    const QQmlComponent::CompilationMode mode = asynchronous
            ? QQmlComponent::Asynchronous
            : QQmlComponent::PreferSynchronous;
    if (QQmlContext *context = qmlContext(q)) {
        if (QQmlEngine *engine = context->engine()) {
            component.setObject(new QQmlComponent(
                                    engine, context->resolvedUrl(source), mode, q), q);
            return;
        }
    }

    qmlWarning(q) << "createComponent: Cannot find a QML engine.";
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 110, as _ZNK19QQuickLoaderPrivate16getImplicitWidthEv
inline qreal QQuickLoaderPrivate::getImplicitWidth() const
{
    Q_Q(const QQuickLoader);
    // If the Loader has a valid width then Loader has set an explicit width on the
    // item, and we want the item's implicitWidth.  If the Loader's width has
    // not been set then its implicitWidth is the width of the item.
    if (item)
        return q->widthValid() ? item->implicitWidth() : item->width();
    return QQuickImplicitSizeItemPrivate::getImplicitWidth();
}

//  from ../qtdeclarative/src/quick/items/qquickloader.cpp, line 121, as _ZNK19QQuickLoaderPrivate17getImplicitHeightEv
inline qreal QQuickLoaderPrivate::getImplicitHeight() const
{
    Q_Q(const QQuickLoader);
    // If the Loader has a valid height then Loader has set an explicit height on the
    // item, and we want the item's implicitHeight.  If the Loader's height has
    // not been set then its implicitHeight is the height of the item.
    if (item)
        return q->heightValid() ? item->implicitHeight() : item->height();
    return QQuickImplicitSizeItemPrivate::getImplicitHeight();
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
//  -----------------------------------------------------------------------

//  A QQuickLoaderPrivate that Python can take functions over in. Every QQuickLoaderPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickLoaderPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickLoaderPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickLoaderPrivateCall2)(const void *, QQuickItem *, int *);
typedef qreal (*CuteQQuickLoaderPrivateCall3)(const void *, int *);
typedef qreal (*CuteQQuickLoaderPrivateCall4)(const void *, int *);
typedef void (*CuteQQuickLoaderPrivateCall5)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickLoaderPrivateCall6)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickLoaderPrivateCall7)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickLoaderPrivateCall8)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickLoaderPrivateCall9)(const void *, int, int *);
typedef void (*CuteQQuickLoaderPrivateCall10)(const void *, int *);
typedef void (*CuteQQuickLoaderPrivateCall11)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickLoaderPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickLoaderPrivateCall13)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickLoaderPrivateCall14)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickLoaderPrivateCall15)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickLoaderPrivateCall16)(const void *, bool, int *);
typedef void * (*CuteQQuickLoaderPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickLoaderPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickLoaderPrivateCall19)(const void *, int *);
typedef void (*CuteQQuickLoaderPrivateCall20)(const void *, int, int *);
class CuteQQuickLoaderPrivate : public QQuickLoaderPrivate {
public:
  using QQuickLoaderPrivate::QQuickLoaderPrivate;
  void *taken[21] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[11] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[14] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[20] = call;
      return true;
    }
    return false;
  }

  //  void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &oldGeometry)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &oldGeometry) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall0 call = reinterpret_cast<CuteQQuickLoaderPrivateCall0>(taken[0]);
      call(this, item, &change, &oldGeometry, &handled);
      if (handled) return;
    }
    QQuickLoaderPrivate::itemGeometryChanged(item, change, oldGeometry);
  }

  //  void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem *a0)
  void itemImplicitWidthChanged(QQuickItem *a0) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall1 call = reinterpret_cast<CuteQQuickLoaderPrivateCall1>(taken[1]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickLoaderPrivate::itemImplicitWidthChanged(a0);
  }

  //  void QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *a0)
  void itemImplicitHeightChanged(QQuickItem *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall2 call = reinterpret_cast<CuteQQuickLoaderPrivateCall2>(taken[2]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickLoaderPrivate::itemImplicitHeightChanged(a0);
  }

  //  qreal QQuickLoaderPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall3 call = reinterpret_cast<CuteQQuickLoaderPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickLoaderPrivate::getImplicitWidth();
  }

  //  qreal QQuickLoaderPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall4 call = reinterpret_cast<CuteQQuickLoaderPrivateCall4>(taken[4]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickLoaderPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall5 call = reinterpret_cast<CuteQQuickLoaderPrivateCall5>(taken[5]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall6 call = reinterpret_cast<CuteQQuickLoaderPrivateCall6>(taken[6]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::removePointerHandler(h);
  }

  //  QtPrivate::QQuickAttachedPropertyPropagator
  //      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
  //      QMetaObject *attachedType)
  QtPrivate::QQuickAttachedPropertyPropagator *attachedPropertyPropagator_parent(
      const QMetaObject *attachedType) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall7 call = reinterpret_cast<CuteQQuickLoaderPrivateCall7>(taken[7]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall8 call = reinterpret_cast<CuteQQuickLoaderPrivateCall8>(taken[8]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall9 call = reinterpret_cast<CuteQQuickLoaderPrivateCall9>(taken[9]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall10 call = reinterpret_cast<CuteQQuickLoaderPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall11 call = reinterpret_cast<CuteQQuickLoaderPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall12 call = reinterpret_cast<CuteQQuickLoaderPrivateCall12>(taken[12]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall13 call = reinterpret_cast<CuteQQuickLoaderPrivateCall13>(taken[13]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall14 call = reinterpret_cast<CuteQQuickLoaderPrivateCall14>(taken[14]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall15 call = reinterpret_cast<CuteQQuickLoaderPrivateCall15>(taken[15]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall16 call = reinterpret_cast<CuteQQuickLoaderPrivateCall16>(taken[16]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall17 call = reinterpret_cast<CuteQQuickLoaderPrivateCall17>(taken[17]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall18 call = reinterpret_cast<CuteQQuickLoaderPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall19 call = reinterpret_cast<CuteQQuickLoaderPrivateCall19>(taken[19]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickLoaderPrivateCall20 call = reinterpret_cast<CuteQQuickLoaderPrivateCall20>(taken[20]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickLoader *QQuickLoaderPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickLoader *ritual_ZN19QQuickLoaderPrivate6q_funcEv(
    QQuickLoaderPrivate *self) {
  return self->q_func();
}

//  const QQuickLoader *QQuickLoaderPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickLoader *ritual_ZNK19QQuickLoaderPrivate6q_funcEv(
    const QQuickLoaderPrivate *self) {
  return self->q_func();
}

//  QQuickLoaderPrivate::QQuickLoaderPrivate()
extern "C" Q_DECL_EXPORT
QQuickLoaderPrivate *ritual_ZN19QQuickLoaderPrivateC1Ev() {
  return new CuteQQuickLoaderPrivate();
}

//  QQuickLoaderPrivate::~QQuickLoaderPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivateD1Ev(QQuickLoaderPrivate *self) {
  delete self;
}

//  void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickLoaderPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *oldGeometry) {
  self->itemGeometryChanged(item, *change, *oldGeometry);
}

//  void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLoaderPrivate *self,
    QQuickItem *a0) {
  self->itemImplicitWidthChanged(a0);
}

//  void QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLoaderPrivate *self,
    QQuickItem *a0) {
  self->itemImplicitHeightChanged(a0);
}

//  void QQuickLoaderPrivate::setInitialState(QObject *o)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate15setInitialStateEP7QObject(
    QQuickLoaderPrivate *self,
    QObject *o) {
  self->setInitialState(o);
}

//  void QQuickLoaderPrivate::disposeInitialPropertyValues()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate28disposeInitialPropertyValuesEv(
    QQuickLoaderPrivate *self) {
  self->disposeInitialPropertyValues();
}

//  QQuickLoader::Status QQuickLoaderPrivate::computeStatus() const
extern "C" Q_DECL_EXPORT
QQuickLoader::Status ritual_ZNK19QQuickLoaderPrivate13computeStatusEv(
    const QQuickLoaderPrivate *self) {
  return self->computeStatus();
}

//  void QQuickLoaderPrivate::updateStatus()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate12updateStatusEv(
    QQuickLoaderPrivate *self) {
  self->updateStatus();
}

//  void QQuickLoaderPrivate::createComponent()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate15createComponentEv(
    QQuickLoaderPrivate *self) {
  self->createComponent();
}

//  qreal QQuickLoaderPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickLoaderPrivate16getImplicitWidthEv(
    const QQuickLoaderPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickLoaderPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK19QQuickLoaderPrivate17getImplicitHeightEv(
    const QQuickLoaderPrivate *self) {
  return self->getImplicitHeight();
}

//  void QQuickLoaderPrivate::_q_updateSize(bool loaderGeometryChanged)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QQuickLoaderPrivate13_q_updateSizeEb(
    QQuickLoaderPrivate *self,
    bool loaderGeometryChanged) {
  self->_q_updateSize(loaderGeometryChanged);
}

//  a Python function taken by a CuteQQuickLoaderPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickLoaderPrivate(
    QQuickLoaderPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickLoaderPrivate *>(self)->take(key, call);
}

//  void QQuickLoaderPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &oldGeometry)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickLoaderPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickLoaderPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *oldGeometry) {
  self->QQuickLoaderPrivate::itemGeometryChanged(
      item,
      *change,
      *oldGeometry);
}

//  void QQuickLoaderPrivate::itemImplicitWidthChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickLoaderPrivate24itemImplicitWidthChangedEP10QQuickItem(
    QQuickLoaderPrivate *self,
    QQuickItem *a0) {
  self->QQuickLoaderPrivate::itemImplicitWidthChanged(a0);
}

//  void QQuickLoaderPrivate::itemImplicitHeightChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QQuickLoaderPrivate25itemImplicitHeightChangedEP10QQuickItem(
    QQuickLoaderPrivate *self,
    QQuickItem *a0) {
  self->QQuickLoaderPrivate::itemImplicitHeightChanged(a0);
}

//  qreal QQuickLoaderPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK19QQuickLoaderPrivate16getImplicitWidthEv(
    const QQuickLoaderPrivate *self) {
  return self->QQuickLoaderPrivate::getImplicitWidth();
}

//  qreal QQuickLoaderPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK19QQuickLoaderPrivate17getImplicitHeightEv(
    const QQuickLoaderPrivate *self) {
  return self->QQuickLoaderPrivate::getImplicitHeight();
}
