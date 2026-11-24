//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickimagebase_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickimagebase_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickimagebase_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickImageBasePrivate that Python can take functions over in. Every QQuickImageBasePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickImageBasePrivateCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickImageBasePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickImageBasePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickImageBasePrivateCall3)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickImageBasePrivateCall4)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickImageBasePrivateCall5)(const void *, int, int *);
typedef qreal (*CuteQQuickImageBasePrivateCall6)(const void *, int *);
typedef qreal (*CuteQQuickImageBasePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickImageBasePrivateCall8)(const void *, int *);
typedef void (*CuteQQuickImageBasePrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickImageBasePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickImageBasePrivateCall11)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickImageBasePrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickImageBasePrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickImageBasePrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickImageBasePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickImageBasePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickImageBasePrivateCall17)(const void *, int *);
typedef void (*CuteQQuickImageBasePrivateCall18)(const void *, int, int *);
class CuteQQuickImageBasePrivate : public QQuickImageBasePrivate {
public:
  using QQuickImageBasePrivate::QQuickImageBasePrivate;
  void *taken[19] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[9] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[12] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[18] = call;
      return true;
    }
    return false;
  }

  //  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
  //      targetDevicePixelRatio)
  bool updateDevicePixelRatio(qreal targetDevicePixelRatio) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall0 call = reinterpret_cast<CuteQQuickImageBasePrivateCall0>(taken[0]);
      bool given = call(this, targetDevicePixelRatio, &handled);
      if (handled) return given;
    }
    return QQuickImageBasePrivate::updateDevicePixelRatio(targetDevicePixelRatio);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall1 call = reinterpret_cast<CuteQQuickImageBasePrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall2 call = reinterpret_cast<CuteQQuickImageBasePrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall3 call = reinterpret_cast<CuteQQuickImageBasePrivateCall3>(taken[3]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall4 call = reinterpret_cast<CuteQQuickImageBasePrivateCall4>(taken[4]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall5 call = reinterpret_cast<CuteQQuickImageBasePrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall6 call = reinterpret_cast<CuteQQuickImageBasePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall7 call = reinterpret_cast<CuteQQuickImageBasePrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall8 call = reinterpret_cast<CuteQQuickImageBasePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall9 call = reinterpret_cast<CuteQQuickImageBasePrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall10 call = reinterpret_cast<CuteQQuickImageBasePrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall11 call = reinterpret_cast<CuteQQuickImageBasePrivateCall11>(taken[11]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall12 call = reinterpret_cast<CuteQQuickImageBasePrivateCall12>(taken[12]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall13 call = reinterpret_cast<CuteQQuickImageBasePrivateCall13>(taken[13]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall14 call = reinterpret_cast<CuteQQuickImageBasePrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall15 call = reinterpret_cast<CuteQQuickImageBasePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall16 call = reinterpret_cast<CuteQQuickImageBasePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall17 call = reinterpret_cast<CuteQQuickImageBasePrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickImageBasePrivateCall18 call = reinterpret_cast<CuteQQuickImageBasePrivateCall18>(taken[18]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickImageBase *QQuickImageBasePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickImageBase *ritual_ZN22QQuickImageBasePrivate6q_funcEv(
    QQuickImageBasePrivate *self) {
  return self->q_func();
}

//  const QQuickImageBase *QQuickImageBasePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickImageBase *ritual_ZNK22QQuickImageBasePrivate6q_funcEv(
    const QQuickImageBasePrivate *self) {
  return self->q_func();
}

//  QQuickImageBasePrivate::QQuickImageBasePrivate()
extern "C" Q_DECL_EXPORT
QQuickImageBasePrivate *ritual_ZN22QQuickImageBasePrivateC1Ev() {
  return new CuteQQuickImageBasePrivate();
}

//  QQuickImageBasePrivate *QQuickImageBasePrivate::get(QQuickImageBase
//      *image)
extern "C" Q_DECL_EXPORT
QQuickImageBasePrivate *ritual_ZN22QQuickImageBasePrivate3getEP15QQuickImageBase(
    QQuickImageBase *image) {
  return QQuickImageBasePrivate::get(image);
}

//  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
//      targetDevicePixelRatio)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd(
    QQuickImageBasePrivate *self,
    qreal targetDevicePixelRatio) {
  return self->updateDevicePixelRatio(targetDevicePixelRatio);
}

//  void QQuickImageBasePrivate::setStatus(QQuickImageBase::Status value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickImageBasePrivate9setStatusEN15QQuickImageBase6StatusE(
    QQuickImageBasePrivate *self,
    QQuickImageBase::Status value) {
  self->setStatus(value);
}

//  void QQuickImageBasePrivate::setProgress(qreal value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickImageBasePrivate11setProgressEd(
    QQuickImageBasePrivate *self,
    qreal value) {
  self->setProgress(value);
}

//  a Python function taken by a CuteQQuickImageBasePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickImageBasePrivate(
    QQuickImageBasePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickImageBasePrivate *>(self)->take(key, call);
}

//  bool QQuickImageBasePrivate::updateDevicePixelRatio(qreal
//      targetDevicePixelRatio)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickImageBasePrivate22updateDevicePixelRatioEd(
    QQuickImageBasePrivate *self,
    qreal targetDevicePixelRatio) {
  return self->QQuickImageBasePrivate::updateDevicePixelRatio(
      targetDevicePixelRatio);
}
