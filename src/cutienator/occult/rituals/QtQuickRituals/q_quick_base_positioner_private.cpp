//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickpositioners_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickpositioners_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickpositioners_p.h>
#include <QtQuick/private/qquickpositioners_p_p.h>
#include <QtQml/qqml.h>
#include <QtQml/qqmlinfo.h>
#include <QtCore/qcoreapplication.h>
#include <QtQuick/private/qquicktransition_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 633, as _ZN27QQuickBasePositionerPrivate9ExtraDataC1Ev
inline QQuickBasePositionerPrivate::ExtraData::ExtraData()
    : padding(0)
    , topPadding(0)
    , leftPadding(0)
    , rightPadding(0)
    , bottomPadding(0)
    , explicitTopPadding(false)
    , explicitLeftPadding(false)
    , explicitRightPadding(false)
    , explicitBottomPadding(false)
{
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 646, as _ZN27QQuickBasePositionerPrivate13setTopPaddingEdb
inline void QQuickBasePositionerPrivate::setTopPadding(qreal value, bool reset)
{
    Q_Q(QQuickBasePositioner);
    qreal oldPadding = q->topPadding();
    if (!reset || extra.isAllocated()) {
        extra.value().topPadding = value;
        extra.value().explicitTopPadding = !reset;
    }
    if ((!reset && !qFuzzyCompare(oldPadding, value)) || (reset && !qFuzzyCompare(oldPadding, padding()))) {
        setPositioningDirty();
        emit q->topPaddingChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 660, as _ZN27QQuickBasePositionerPrivate14setLeftPaddingEdb
inline void QQuickBasePositionerPrivate::setLeftPadding(qreal value, bool reset)
{
    Q_Q(QQuickBasePositioner);
    qreal oldPadding = q->leftPadding();
    if (!reset || extra.isAllocated()) {
        extra.value().leftPadding = value;
        extra.value().explicitLeftPadding = !reset;
    }
    if ((!reset && !qFuzzyCompare(oldPadding, value)) || (reset && !qFuzzyCompare(oldPadding, padding()))) {
        setPositioningDirty();
        emit q->leftPaddingChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 674, as _ZN27QQuickBasePositionerPrivate15setRightPaddingEdb
inline void QQuickBasePositionerPrivate::setRightPadding(qreal value, bool reset)
{
    Q_Q(QQuickBasePositioner);
    qreal oldPadding = q->rightPadding();
    if (!reset || extra.isAllocated()) {
        extra.value().rightPadding = value;
        extra.value().explicitRightPadding = !reset;
    }
    if ((!reset && !qFuzzyCompare(oldPadding, value)) || (reset && !qFuzzyCompare(oldPadding, padding()))) {
        setPositioningDirty();
        emit q->rightPaddingChanged();
    }
}

//  from ../qtdeclarative/src/quick/items/qquickpositioners.cpp, line 688, as _ZN27QQuickBasePositionerPrivate16setBottomPaddingEdb
inline void QQuickBasePositionerPrivate::setBottomPadding(qreal value, bool reset)
{
    Q_Q(QQuickBasePositioner);
    qreal oldPadding = q->bottomPadding();
    if (!reset || extra.isAllocated()) {
        extra.value().bottomPadding = value;
        extra.value().explicitBottomPadding = !reset;
    }
    if ((!reset && !qFuzzyCompare(oldPadding, value)) || (reset && !qFuzzyCompare(oldPadding, padding()))) {
        setPositioningDirty();
        emit q->bottomPaddingChanged();
    }
}
//  -----------------------------------------------------------------------

//  A QQuickBasePositionerPrivate that Python can take functions over in. Every QQuickBasePositionerPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall1)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall2)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall3)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall4)(const void *, QQuickItem *, int *);
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(quick_positioners)
typedef void (*CuteQQuickBasePositionerPrivateCall6)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall7)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickBasePositionerPrivateCall8)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall9)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickBasePositionerPrivateCall10)(const void *, int, int *);
typedef qreal (*CuteQQuickBasePositionerPrivateCall11)(const void *, int *);
typedef qreal (*CuteQQuickBasePositionerPrivateCall12)(const void *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall13)(const void *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall14)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickBasePositionerPrivateCall15)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickBasePositionerPrivateCall16)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickBasePositionerPrivateCall17)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickBasePositionerPrivateCall18)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickBasePositionerPrivateCall19)(const void *, bool, int *);
typedef void * (*CuteQQuickBasePositionerPrivateCall20)(const void *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall21)(const void *, int *);
typedef void (*CuteQQuickBasePositionerPrivateCall22)(const void *, int, int *);
class CuteQQuickBasePositionerPrivate : public QQuickBasePositionerPrivate {
public:
  using QQuickBasePositionerPrivate::QQuickBasePositionerPrivate;
  void *taken[23] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChangedEP10QQuickItem")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN27QQuickBasePositionerPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN27QQuickBasePositionerPrivate21itemVisibilityChangedEP10QQuickItem")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQuickItem")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
#if QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirectionChangeEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_positioners)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[14] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[17] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[22] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall0 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::mirrorChange();
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::itemSiblingOrderChanged(QQuickItem
  //      *other)
  void itemSiblingOrderChanged(QQuickItem *other) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall1 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall1>(taken[1]);
      call(this, other, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::itemSiblingOrderChanged(other);
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::itemGeometryChanged(QQuickItem *a0,
  //      QQuickGeometryChange change, const QRectF &a2)
  void itemGeometryChanged(
      QQuickItem *a0,
      QQuickGeometryChange change,
      const QRectF &a2) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall2 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall2>(taken[2]);
      call(this, a0, &change, &a2, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::itemGeometryChanged(a0, change, a2);
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::itemVisibilityChanged(QQuickItem
  //      *a0)
  void itemVisibilityChanged(QQuickItem *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall3 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::itemVisibilityChanged(a0);
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall4 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall4>(taken[4]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::itemDestroyed(item);
  }
#endif  // QT_CONFIG(quick_positioners)

#if QT_CONFIG(quick_positioners)
  //  void QQuickBasePositionerPrivate::effectiveLayoutDirectionChange()
  void effectiveLayoutDirectionChange() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall5 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickBasePositionerPrivate::effectiveLayoutDirectionChange();
  }
#endif  // QT_CONFIG(quick_positioners)

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall6 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall6>(taken[6]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall7 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall8 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall8>(taken[8]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall9 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall9>(taken[9]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall10 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall10>(taken[10]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall11 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall11>(taken[11]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall12 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall12>(taken[12]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall13 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall13>(taken[13]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall14 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall15 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall15>(taken[15]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall16 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall16>(taken[16]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall17 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall17>(taken[17]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall18 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall18>(taken[18]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall19 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall19>(taken[19]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall20 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall20>(taken[20]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall21 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickBasePositionerPrivateCall22 call = reinterpret_cast<CuteQQuickBasePositionerPrivateCall22>(taken[22]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickBasePositioner *QQuickBasePositionerPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickBasePositioner *ritual_ZN27QQuickBasePositionerPrivate6q_funcEv(
    QQuickBasePositionerPrivate *self) {
  return self->q_func();
}

//  const QQuickBasePositioner *QQuickBasePositionerPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickBasePositioner *ritual_ZNK27QQuickBasePositionerPrivate6q_funcEv(
    const QQuickBasePositionerPrivate *self) {
  return self->q_func();
}

//  QQuickBasePositionerPrivate::QQuickBasePositionerPrivate()
extern "C" Q_DECL_EXPORT
QQuickBasePositionerPrivate *ritual_ZN27QQuickBasePositionerPrivateC1Ev() {
  return new CuteQQuickBasePositionerPrivate();
}

//  void
//      QQuickBasePositionerPrivate::init(QQuickBasePositioner::PositionerTyp
//      e at)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate4initEN20QQuickBasePositioner14PositionerTypeE(
    QQuickBasePositionerPrivate *self,
    QQuickBasePositioner::PositionerType at) {
  self->init(at);
}

//  void QQuickBasePositionerPrivate::setPositioningDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate19setPositioningDirtyEv(
    QQuickBasePositionerPrivate *self) {
  self->setPositioningDirty();
}

//  void QQuickBasePositionerPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate12mirrorChangeEv(
    QQuickBasePositionerPrivate *self) {
  self->mirrorChange();
}

//  bool QQuickBasePositionerPrivate::isLeftToRight() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QQuickBasePositionerPrivate13isLeftToRightEv(
    const QQuickBasePositionerPrivate *self) {
  return self->isLeftToRight();
}

//  void QQuickBasePositionerPrivate::itemSiblingOrderChanged(QQuickItem
//      *other)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *other) {
  self->itemSiblingOrderChanged(other);
}

//  void QQuickBasePositionerPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickBasePositionerPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->itemGeometryChanged(a0, *change, *a2);
}

//  void QQuickBasePositionerPrivate::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *a0) {
  self->itemVisibilityChanged(a0);
}

//  void QQuickBasePositionerPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *item) {
  self->itemDestroyed(item);
}

//  Qt::LayoutDirection QQuickBasePositionerPrivate::getLayoutDirection(const
//      QQuickBasePositioner *positioner)
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZN27QQuickBasePositionerPrivate18getLayoutDirectionEPK20QQuickBasePositioner(
    const QQuickBasePositioner *positioner) {
  return QQuickBasePositionerPrivate::getLayoutDirection(positioner);
}

//  Qt::LayoutDirection
//      QQuickBasePositionerPrivate::getEffectiveLayoutDirection(const
//      QQuickBasePositioner *positioner)
extern "C" Q_DECL_EXPORT
Qt::LayoutDirection ritual_ZN27QQuickBasePositionerPrivate27getEffectiveLayoutDirectionEPK20QQuickBasePositioner(
    const QQuickBasePositioner *positioner) {
  return QQuickBasePositionerPrivate::getEffectiveLayoutDirection(
      positioner);
}

//  void QQuickBasePositionerPrivate::effectiveLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirectionChangeEv(
    QQuickBasePositionerPrivate *self) {
  self->effectiveLayoutDirectionChange();
}

//  qreal QQuickBasePositionerPrivate::padding() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK27QQuickBasePositionerPrivate7paddingEv(
    const QQuickBasePositionerPrivate *self) {
  return self->padding();
}

//  void QQuickBasePositionerPrivate::setTopPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate13setTopPaddingEdb(
    QQuickBasePositionerPrivate *self,
    qreal value,
    bool reset) {
  self->setTopPadding(value, reset);
}

//  void QQuickBasePositionerPrivate::setLeftPadding(qreal value, bool reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate14setLeftPaddingEdb(
    QQuickBasePositionerPrivate *self,
    qreal value,
    bool reset) {
  self->setLeftPadding(value, reset);
}

//  void QQuickBasePositionerPrivate::setRightPadding(qreal value, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate15setRightPaddingEdb(
    QQuickBasePositionerPrivate *self,
    qreal value,
    bool reset) {
  self->setRightPadding(value, reset);
}

//  void QQuickBasePositionerPrivate::setBottomPadding(qreal value, bool
//      reset)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QQuickBasePositionerPrivate16setBottomPaddingEdb(
    QQuickBasePositionerPrivate *self,
    qreal value,
    bool reset) {
  self->setBottomPadding(value, reset);
}

//  a Python function taken by a CuteQQuickBasePositionerPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickBasePositionerPrivate(
    QQuickBasePositionerPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickBasePositionerPrivate *>(self)->take(key, call);
}

//  void QQuickBasePositionerPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate12mirrorChangeEv(
    QQuickBasePositionerPrivate *self) {
  self->QQuickBasePositionerPrivate::mirrorChange();
}

//  void QQuickBasePositionerPrivate::itemSiblingOrderChanged(QQuickItem
//      *other)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate23itemSiblingOrderChangedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *other) {
  self->QQuickBasePositionerPrivate::itemSiblingOrderChanged(other);
}

//  void QQuickBasePositionerPrivate::itemGeometryChanged(QQuickItem *a0,
//      QQuickGeometryChange change, const QRectF &a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickBasePositionerPrivate *self,
    QQuickItem *a0,
    const QQuickGeometryChange *change,
    const QRectF *a2) {
  self->QQuickBasePositionerPrivate::itemGeometryChanged(a0, *change, *a2);
}

//  void QQuickBasePositionerPrivate::itemVisibilityChanged(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate21itemVisibilityChangedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *a0) {
  self->QQuickBasePositionerPrivate::itemVisibilityChanged(a0);
}

//  void QQuickBasePositionerPrivate::itemDestroyed(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate13itemDestroyedEP10QQuickItem(
    QQuickBasePositionerPrivate *self,
    QQuickItem *item) {
  self->QQuickBasePositionerPrivate::itemDestroyed(item);
}

//  void QQuickBasePositionerPrivate::effectiveLayoutDirectionChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN27QQuickBasePositionerPrivate30effectiveLayoutDirectionChangeEv(
    QQuickBasePositionerPrivate *self) {
  self->QQuickBasePositionerPrivate::effectiveLayoutDirectionChange();
}

#endif  // QT_CONFIG(quick_positioners)
#endif  // QT_CONFIG(quick_positioners)
