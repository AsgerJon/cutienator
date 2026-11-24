//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickrectangle_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickrectangle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickrectangle_p.h"
#include "qquickrectangle_p_p.h"
#include <QtQml/qqmlinfo.h>
#include <QtQuick/private/qsgcontext_p.h>
#include <private/qsgadaptationlayer_p.h>
#include <private/qqmlmetatype_p.h>
#include <QtGui/qpixmapcache.h>
#include <QtCore/qmath.h>
#include <QtCore/qmetaobject.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickrectangle.cpp, line 269, as _ZN22QQuickRectanglePrivate28maybeSetImplicitAntialiasingEv
inline void QQuickRectanglePrivate::maybeSetImplicitAntialiasing()
{
    bool implicitAA = (radius > 0);
    if (extraRectangle.isAllocated() && !implicitAA) {
        const auto &extra = extraRectangle.value();
        implicitAA = (extra.isTopLeftRadiusSet && extra.topLeftRadius > 0)
            || (extra.isTopRightRadiusSet && extra.topRightRadius > 0)
            || (extra.isBottomLeftRadiusSet && extra.bottomLeftRadius > 0)
            || (extra.isBottomRightRadiusSet && extra.bottomRightRadius > 0);
    }
    setImplicitAntialiasing(implicitAA);
}
//  -----------------------------------------------------------------------

//  A QQuickRectanglePrivate that Python can take functions over in. Every QQuickRectanglePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickRectanglePrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickRectanglePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickRectanglePrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickRectanglePrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickRectanglePrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickRectanglePrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickRectanglePrivateCall6)(const void *, int *);
typedef void (*CuteQQuickRectanglePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickRectanglePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickRectanglePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickRectanglePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickRectanglePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickRectanglePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickRectanglePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickRectanglePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickRectanglePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickRectanglePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickRectanglePrivateCall17)(const void *, int, int *);
class CuteQQuickRectanglePrivate : public QQuickRectanglePrivate {
public:
  using QQuickRectanglePrivate::QQuickRectanglePrivate;
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
      CuteQQuickRectanglePrivateCall0 call = reinterpret_cast<CuteQQuickRectanglePrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall1 call = reinterpret_cast<CuteQQuickRectanglePrivateCall1>(taken[1]);
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
      CuteQQuickRectanglePrivateCall2 call = reinterpret_cast<CuteQQuickRectanglePrivateCall2>(taken[2]);
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
      CuteQQuickRectanglePrivateCall3 call = reinterpret_cast<CuteQQuickRectanglePrivateCall3>(taken[3]);
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
      CuteQQuickRectanglePrivateCall4 call = reinterpret_cast<CuteQQuickRectanglePrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall5 call = reinterpret_cast<CuteQQuickRectanglePrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall6 call = reinterpret_cast<CuteQQuickRectanglePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall7 call = reinterpret_cast<CuteQQuickRectanglePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall8 call = reinterpret_cast<CuteQQuickRectanglePrivateCall8>(taken[8]);
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
      CuteQQuickRectanglePrivateCall9 call = reinterpret_cast<CuteQQuickRectanglePrivateCall9>(taken[9]);
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
      CuteQQuickRectanglePrivateCall10 call = reinterpret_cast<CuteQQuickRectanglePrivateCall10>(taken[10]);
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
      CuteQQuickRectanglePrivateCall11 call = reinterpret_cast<CuteQQuickRectanglePrivateCall11>(taken[11]);
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
      CuteQQuickRectanglePrivateCall12 call = reinterpret_cast<CuteQQuickRectanglePrivateCall12>(taken[12]);
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
      CuteQQuickRectanglePrivateCall13 call = reinterpret_cast<CuteQQuickRectanglePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall14 call = reinterpret_cast<CuteQQuickRectanglePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall15 call = reinterpret_cast<CuteQQuickRectanglePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall16 call = reinterpret_cast<CuteQQuickRectanglePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRectanglePrivateCall17 call = reinterpret_cast<CuteQQuickRectanglePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickRectangle *QQuickRectanglePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickRectangle *ritual_ZN22QQuickRectanglePrivate6q_funcEv(
    QQuickRectanglePrivate *self) {
  return self->q_func();
}

//  const QQuickRectangle *QQuickRectanglePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickRectangle *ritual_ZNK22QQuickRectanglePrivate6q_funcEv(
    const QQuickRectanglePrivate *self) {
  return self->q_func();
}

//  QQuickRectanglePrivate::QQuickRectanglePrivate()
extern "C" Q_DECL_EXPORT
QQuickRectanglePrivate *ritual_ZN22QQuickRectanglePrivateC1Ev() {
  return new CuteQQuickRectanglePrivate();
}

//  QQuickRectanglePrivate::~QQuickRectanglePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickRectanglePrivateD1Ev(QQuickRectanglePrivate *self) {
  delete self;
}

//  void QQuickRectanglePrivate::maybeSetImplicitAntialiasing()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickRectanglePrivate28maybeSetImplicitAntialiasingEv(
    QQuickRectanglePrivate *self) {
  self->maybeSetImplicitAntialiasing();
}

//  a Python function taken by a CuteQQuickRectanglePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRectanglePrivate(
    QQuickRectanglePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRectanglePrivate *>(self)->take(key, call);
}
