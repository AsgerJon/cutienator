//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickspritesequence_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickSpriteSequencePrivate that Python can take functions over in. Every QQuickSpriteSequencePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickSpriteSequencePrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickSpriteSequencePrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickSpriteSequencePrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickSpriteSequencePrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickSpriteSequencePrivateCall6)(const void *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSpriteSequencePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickSpriteSequencePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickSpriteSequencePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickSpriteSequencePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickSpriteSequencePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickSpriteSequencePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickSpriteSequencePrivateCall17)(const void *, int, int *);
class CuteQQuickSpriteSequencePrivate : public QQuickSpriteSequencePrivate {
public:
  using QQuickSpriteSequencePrivate::QQuickSpriteSequencePrivate;
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
      CuteQQuickSpriteSequencePrivateCall0 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall1 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall1>(taken[1]);
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
      CuteQQuickSpriteSequencePrivateCall2 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall2>(taken[2]);
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
      CuteQQuickSpriteSequencePrivateCall3 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall3>(taken[3]);
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
      CuteQQuickSpriteSequencePrivateCall4 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall5 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall6 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall7 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall8 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall8>(taken[8]);
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
      CuteQQuickSpriteSequencePrivateCall9 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall9>(taken[9]);
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
      CuteQQuickSpriteSequencePrivateCall10 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall10>(taken[10]);
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
      CuteQQuickSpriteSequencePrivateCall11 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall11>(taken[11]);
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
      CuteQQuickSpriteSequencePrivateCall12 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall12>(taken[12]);
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
      CuteQQuickSpriteSequencePrivateCall13 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall14 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall15 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall16 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSpriteSequencePrivateCall17 call = reinterpret_cast<CuteQQuickSpriteSequencePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickSpriteSequence *QQuickSpriteSequencePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSpriteSequence *ritual_ZN27QQuickSpriteSequencePrivate6q_funcEv(
    QQuickSpriteSequencePrivate *self) {
  return self->q_func();
}

//  const QQuickSpriteSequence *QQuickSpriteSequencePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickSpriteSequence *ritual_ZNK27QQuickSpriteSequencePrivate6q_funcEv(
    const QQuickSpriteSequencePrivate *self) {
  return self->q_func();
}

//  QQuickSpriteSequencePrivate::QQuickSpriteSequencePrivate()
extern "C" Q_DECL_EXPORT
QQuickSpriteSequencePrivate *ritual_ZN27QQuickSpriteSequencePrivateC1Ev() {
  return new CuteQQuickSpriteSequencePrivate();
}

//  a Python function taken by a CuteQQuickSpriteSequencePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSpriteSequencePrivate(
    QQuickSpriteSequencePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSpriteSequencePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_sprite)
