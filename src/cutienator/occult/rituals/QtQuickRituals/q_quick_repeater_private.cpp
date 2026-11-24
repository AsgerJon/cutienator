//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrepeater_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_repeater)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrepeater_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickrepeater_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickrepeater_p.h"
#include "qquickrepeater_p_p.h"
#include <private/qqmlglobal_p.h>
#include <private/qqmlchangeset_p.h>
#include <private/qqmldelegatemodel_p.h>
#include <QtQml/QQmlInfo>
#include <QtQml/qqmlcomponent.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickrepeater.cpp, line 17, as _ZN21QQuickRepeaterPrivateC1Ev
inline QQuickRepeaterPrivate::QQuickRepeaterPrivate()
    : model(nullptr)
    , ownModel(false)
    , delegateValidated(false)
    , explicitDelegate(false)
    , explicitDelegateModelAccess(false)
    , itemCount(0)
{
    setTransparentForPositioner(true);
}

//  from ../qtdeclarative/src/quick/items/qquickrepeater.cpp, line 28, as _ZN21QQuickRepeaterPrivateD1Ev
inline QQuickRepeaterPrivate::~QQuickRepeaterPrivate()
{
    if (ownModel)
        delete model;
}

//  from ../qtdeclarative/src/quick/items/qquickrepeater.cpp, line 450, as _ZN21QQuickRepeaterPrivate12requestItemsEv
inline void QQuickRepeaterPrivate::requestItems()
{
    for (int i = 0; i < itemCount; i++) {
        QObject *object = model->object(i, QQmlIncubator::AsynchronousIfNested);
        if (object)
            model->release(object);
    }
}

//  from ../qtdeclarative/src/quick/items/qquickrepeater.cpp, line 459, as _ZN21QQuickRepeaterPrivate12connectModelEP14QQuickRepeaterP24QQmlDelegateModelPointer
inline void QQuickRepeaterPrivate::connectModel(QQuickRepeater *q, QQmlDelegateModelPointer *model)
{
    QQmlInstanceModel *instanceModel = model->instanceModel();
    if (!instanceModel)
        return;

    QObject::connect(instanceModel, &QQmlInstanceModel::modelUpdated,
                     q, &QQuickRepeater::modelUpdated);
    QObject::connect(instanceModel, &QQmlInstanceModel::createdItem,
                     q, &QQuickRepeater::createdItem);
    QObject::connect(instanceModel, &QQmlInstanceModel::initItem,
                     q, &QQuickRepeater::initItem);
    if (QQmlDelegateModel *dataModel = model->delegateModel()) {
        QObjectPrivate::connect(
                dataModel, &QQmlDelegateModel::delegateChanged,
                this, &QQuickRepeaterPrivate::applyDelegateChange);
        QObjectPrivate::connect(
                dataModel, &QQmlDelegateModel::delegateModelAccessChanged,
                this, &QQuickRepeaterPrivate::applyDelegateModelAccessChange);
        if (ownModel) {
            QObject::connect(dataModel, &QQmlDelegateModel::modelChanged,
                             q, &QQuickRepeater::modelChanged);
        }
    }
    q->regenerate();
}

//  from ../qtdeclarative/src/quick/items/qquickrepeater.cpp, line 486, as _ZN21QQuickRepeaterPrivate15disconnectModelEP14QQuickRepeaterP24QQmlDelegateModelPointer
inline void QQuickRepeaterPrivate::disconnectModel(QQuickRepeater *q, QQmlDelegateModelPointer *model)
{
    QQmlInstanceModel *instanceModel = model->instanceModel();
    if (!instanceModel)
        return;

    QObject::disconnect(instanceModel, &QQmlInstanceModel::modelUpdated,
                        q, &QQuickRepeater::modelUpdated);
    QObject::disconnect(instanceModel, &QQmlInstanceModel::createdItem,
                        q, &QQuickRepeater::createdItem);
    QObject::disconnect(instanceModel, &QQmlInstanceModel::initItem,
                        q, &QQuickRepeater::initItem);
    if (QQmlDelegateModel *delegateModel = model->delegateModel()) {
        QObjectPrivate::disconnect(
                delegateModel, &QQmlDelegateModel::delegateChanged,
                this, &QQuickRepeaterPrivate::applyDelegateChange);
        QObjectPrivate::disconnect(
                delegateModel, &QQmlDelegateModel::delegateModelAccessChanged,
                this, &QQuickRepeaterPrivate::applyDelegateModelAccessChange);
        if (ownModel) {
            QObject::disconnect(delegateModel, &QQmlDelegateModel::modelChanged,
                                q, &QQuickRepeater::modelChanged);
        }
    }
}
//  -----------------------------------------------------------------------

//  A QQuickRepeaterPrivate that Python can take functions over in. Every QQuickRepeaterPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRepeaterPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickRepeaterPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickRepeaterPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickRepeaterPrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickRepeaterPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickRepeaterPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickRepeaterPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickRepeaterPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickRepeaterPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickRepeaterPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickRepeaterPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickRepeaterPrivateCall17)(const void *, int, int *);
class CuteQQuickRepeaterPrivate : public QQuickRepeaterPrivate {
public:
  using QQuickRepeaterPrivate::QQuickRepeaterPrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[11] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[17] = call;
      return true;
    }
    return false;
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall0 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall1 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall2 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall2>(taken[2]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall3 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall3>(taken[3]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall4 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall5 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall6 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall7 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall8 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall9 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall10 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall10>(taken[10]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall11 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall11>(taken[11]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall12 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall12>(taken[12]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall13 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall14 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall15 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall16 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRepeaterPrivateCall17 call = reinterpret_cast<CuteQQuickRepeaterPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickRepeater *QQuickRepeaterPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickRepeater *ritual_ZN21QQuickRepeaterPrivate6q_funcEv(
    QQuickRepeaterPrivate *self) {
  return self->q_func();
}

//  const QQuickRepeater *QQuickRepeaterPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickRepeater *ritual_ZNK21QQuickRepeaterPrivate6q_funcEv(
    const QQuickRepeaterPrivate *self) {
  return self->q_func();
}

//  QQuickRepeaterPrivate::QQuickRepeaterPrivate()
extern "C" Q_DECL_EXPORT
QQuickRepeaterPrivate *ritual_ZN21QQuickRepeaterPrivateC1Ev() {
  return new CuteQQuickRepeaterPrivate();
}

//  QQuickRepeaterPrivate::~QQuickRepeaterPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivateD1Ev(QQuickRepeaterPrivate *self) {
  delete self;
}

//  void QQuickRepeaterPrivate::requestItems()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivate12requestItemsEv(
    QQuickRepeaterPrivate *self) {
  self->requestItems();
}

//  void QQuickRepeaterPrivate::applyDelegateChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivate19applyDelegateChangeEv(
    QQuickRepeaterPrivate *self) {
  self->applyDelegateChange();
}

//  void QQuickRepeaterPrivate::applyDelegateModelAccessChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivate30applyDelegateModelAccessChangeEv(
    QQuickRepeaterPrivate *self) {
  self->applyDelegateModelAccessChange();
}

//  void QQuickRepeaterPrivate::connectModel(QQuickRepeater *q,
//      QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivate12connectModelEP14QQuickRepeaterP24QQmlDelegateModelPointer(
    QQuickRepeaterPrivate *self,
    QQuickRepeater *q,
    QQmlDelegateModelPointer *model) {
  self->connectModel(q, model);
}

//  void QQuickRepeaterPrivate::disconnectModel(QQuickRepeater *q,
//      QQmlDelegateModelPointer *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickRepeaterPrivate15disconnectModelEP14QQuickRepeaterP24QQmlDelegateModelPointer(
    QQuickRepeaterPrivate *self,
    QQuickRepeater *q,
    QQmlDelegateModelPointer *model) {
  self->disconnectModel(q, model);
}

//  a Python function taken by a CuteQQuickRepeaterPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRepeaterPrivate(
    QQuickRepeaterPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRepeaterPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_repeater)
