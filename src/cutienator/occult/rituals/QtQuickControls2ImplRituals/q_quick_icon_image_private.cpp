//  Written by dev_tooling.RitualGenerator from the records of QtQuickControl
//  s2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qtquickcontrols2implglobal_p.h>
#include <QtQuickControls2Impl/QtQuickControls2Impl>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p.h>
#include <QtQuickControls2Impl/6.12.0/QtQuickControls2Impl/private/qquickiconimage_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickIconImagePrivate that Python can take functions over in. Every QQuickIconImagePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQQuickIconImagePrivateCall0)(const void *, qreal, int *);
typedef void (*CuteQQuickIconImagePrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickIconImagePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickIconImagePrivateCall3)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickIconImagePrivateCall4)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickIconImagePrivateCall5)(const void *, int, int *);
typedef qreal (*CuteQQuickIconImagePrivateCall6)(const void *, int *);
typedef qreal (*CuteQQuickIconImagePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickIconImagePrivateCall8)(const void *, int *);
typedef void (*CuteQQuickIconImagePrivateCall9)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickIconImagePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickIconImagePrivateCall11)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickIconImagePrivateCall12)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickIconImagePrivateCall13)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickIconImagePrivateCall14)(const void *, bool, int *);
typedef void * (*CuteQQuickIconImagePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickIconImagePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickIconImagePrivateCall17)(const void *, int *);
typedef void (*CuteQQuickIconImagePrivateCall18)(const void *, int, int *);
class CuteQQuickIconImagePrivate : public QQuickIconImagePrivate {
public:
  using QQuickIconImagePrivate::QQuickIconImagePrivate;
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

  //  bool QQuickIconImagePrivate::updateDevicePixelRatio(qreal
  //      targetDevicePixelRatio)
  bool updateDevicePixelRatio(qreal targetDevicePixelRatio) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall0 call = reinterpret_cast<CuteQQuickIconImagePrivateCall0>(taken[0]);
      bool given = call(this, targetDevicePixelRatio, &handled);
      if (handled) return given;
    }
    return QQuickIconImagePrivate::updateDevicePixelRatio(targetDevicePixelRatio);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall1 call = reinterpret_cast<CuteQQuickIconImagePrivateCall1>(taken[1]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall2 call = reinterpret_cast<CuteQQuickIconImagePrivateCall2>(taken[2]);
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
      CuteQQuickIconImagePrivateCall3 call = reinterpret_cast<CuteQQuickIconImagePrivateCall3>(taken[3]);
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
      CuteQQuickIconImagePrivateCall4 call = reinterpret_cast<CuteQQuickIconImagePrivateCall4>(taken[4]);
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
      CuteQQuickIconImagePrivateCall5 call = reinterpret_cast<CuteQQuickIconImagePrivateCall5>(taken[5]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall6 call = reinterpret_cast<CuteQQuickIconImagePrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall7 call = reinterpret_cast<CuteQQuickIconImagePrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall8 call = reinterpret_cast<CuteQQuickIconImagePrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall9 call = reinterpret_cast<CuteQQuickIconImagePrivateCall9>(taken[9]);
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
      CuteQQuickIconImagePrivateCall10 call = reinterpret_cast<CuteQQuickIconImagePrivateCall10>(taken[10]);
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
      CuteQQuickIconImagePrivateCall11 call = reinterpret_cast<CuteQQuickIconImagePrivateCall11>(taken[11]);
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
      CuteQQuickIconImagePrivateCall12 call = reinterpret_cast<CuteQQuickIconImagePrivateCall12>(taken[12]);
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
      CuteQQuickIconImagePrivateCall13 call = reinterpret_cast<CuteQQuickIconImagePrivateCall13>(taken[13]);
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
      CuteQQuickIconImagePrivateCall14 call = reinterpret_cast<CuteQQuickIconImagePrivateCall14>(taken[14]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall15 call = reinterpret_cast<CuteQQuickIconImagePrivateCall15>(taken[15]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall16 call = reinterpret_cast<CuteQQuickIconImagePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall17 call = reinterpret_cast<CuteQQuickIconImagePrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickIconImagePrivateCall18 call = reinterpret_cast<CuteQQuickIconImagePrivateCall18>(taken[18]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickIconImage *QQuickIconImagePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickIconImage *ritual_ZN22QQuickIconImagePrivate6q_funcEv(
    QQuickIconImagePrivate *self) {
  return self->q_func();
}

//  const QQuickIconImage *QQuickIconImagePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickIconImage *ritual_ZNK22QQuickIconImagePrivate6q_funcEv(
    const QQuickIconImagePrivate *self) {
  return self->q_func();
}

//  QQuickIconImagePrivate::~QQuickIconImagePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconImagePrivateD1Ev(QQuickIconImagePrivate *self) {
  delete self;
}

//  void QQuickIconImagePrivate::updateFillMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickIconImagePrivate14updateFillModeEv(
    QQuickIconImagePrivate *self) {
  self->updateFillMode();
}

//  bool QQuickIconImagePrivate::updateDevicePixelRatio(qreal
//      targetDevicePixelRatio)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickIconImagePrivate22updateDevicePixelRatioEd(
    QQuickIconImagePrivate *self,
    qreal targetDevicePixelRatio) {
  return self->updateDevicePixelRatio(targetDevicePixelRatio);
}

//  a Python function taken by a CuteQQuickIconImagePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickIconImagePrivate(
    QQuickIconImagePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickIconImagePrivate *>(self)->take(key, call);
}

//  bool QQuickIconImagePrivate::updateDevicePixelRatio(qreal
//      targetDevicePixelRatio)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN22QQuickIconImagePrivate22updateDevicePixelRatioEd(
    QQuickIconImagePrivate *self,
    qreal targetDevicePixelRatio) {
  return self->QQuickIconImagePrivate::updateDevicePixelRatio(
      targetDevicePixelRatio);
}
