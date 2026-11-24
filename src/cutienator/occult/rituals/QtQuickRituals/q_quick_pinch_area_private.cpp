//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpincharea_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpincharea_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickpincharea_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qquickpincharea_p_p.h"
#include "qquickwindow.h"
#include <QtCore/qmath.h>
#include <QtGui/qevent.h>
#include <QtGui/qguiapplication.h>
#include <QtGui/qstylehints.h>
#include <qpa/qplatformintegration.h>
#include <qpa/qplatformnativeinterface.h>
#include <private/qguiapplication_p.h>
#include <QVariant>
#include <float.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickpincharea.cpp, line 126, as _ZN22QQuickPinchAreaPrivateD1Ev
inline QQuickPinchAreaPrivate::~QQuickPinchAreaPrivate()
{
    delete pinch;
}
//  -----------------------------------------------------------------------

//  A QQuickPinchAreaPrivate that Python can take functions over in. Every QQuickPinchAreaPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickPinchAreaPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickPinchAreaPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickPinchAreaPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickPinchAreaPrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickPinchAreaPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickPinchAreaPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickPinchAreaPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickPinchAreaPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickPinchAreaPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickPinchAreaPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickPinchAreaPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickPinchAreaPrivateCall17)(const void *, int, int *);
class CuteQQuickPinchAreaPrivate : public QQuickPinchAreaPrivate {
public:
  using QQuickPinchAreaPrivate::QQuickPinchAreaPrivate;
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
      CuteQQuickPinchAreaPrivateCall0 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall1 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall1>(taken[1]);
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
      CuteQQuickPinchAreaPrivateCall2 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall2>(taken[2]);
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
      CuteQQuickPinchAreaPrivateCall3 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall3>(taken[3]);
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
      CuteQQuickPinchAreaPrivateCall4 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall5 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall6 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall7 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall8 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall8>(taken[8]);
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
      CuteQQuickPinchAreaPrivateCall9 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall9>(taken[9]);
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
      CuteQQuickPinchAreaPrivateCall10 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall10>(taken[10]);
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
      CuteQQuickPinchAreaPrivateCall11 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall11>(taken[11]);
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
      CuteQQuickPinchAreaPrivateCall12 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall12>(taken[12]);
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
      CuteQQuickPinchAreaPrivateCall13 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall14 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall15 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall16 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickPinchAreaPrivateCall17 call = reinterpret_cast<CuteQQuickPinchAreaPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickPinchArea *QQuickPinchAreaPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickPinchArea *ritual_ZN22QQuickPinchAreaPrivate6q_funcEv(
    QQuickPinchAreaPrivate *self) {
  return self->q_func();
}

//  const QQuickPinchArea *QQuickPinchAreaPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickPinchArea *ritual_ZNK22QQuickPinchAreaPrivate6q_funcEv(
    const QQuickPinchAreaPrivate *self) {
  return self->q_func();
}

//  QQuickPinchAreaPrivate::QQuickPinchAreaPrivate()
extern "C" Q_DECL_EXPORT
QQuickPinchAreaPrivate *ritual_ZN22QQuickPinchAreaPrivateC1Ev() {
  return new CuteQQuickPinchAreaPrivate();
}

//  QQuickPinchAreaPrivate::~QQuickPinchAreaPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPinchAreaPrivateD1Ev(QQuickPinchAreaPrivate *self) {
  delete self;
}

//  void QQuickPinchAreaPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickPinchAreaPrivate4initEv(QQuickPinchAreaPrivate *self) {
  self->init();
}

//  a Python function taken by a CuteQQuickPinchAreaPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickPinchAreaPrivate(
    QQuickPinchAreaPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickPinchAreaPrivate *>(self)->take(key, call);
}
