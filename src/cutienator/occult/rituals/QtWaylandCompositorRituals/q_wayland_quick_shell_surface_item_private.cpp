//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.
//  h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandquickshellsurfaceitem.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickshellsurfaceitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QWaylandQuickShellSurfaceItemPrivate that Python can take functions over in. Every QWaylandQuickShellSurfaceItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall0)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall1)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQWaylandQuickShellSurfaceItemPrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQWaylandQuickShellSurfaceItemPrivateCall6)(const void *, int, int *);
typedef qreal (*CuteQWaylandQuickShellSurfaceItemPrivateCall7)(const void *, int *);
typedef qreal (*CuteQWaylandQuickShellSurfaceItemPrivateCall8)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall9)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQWaylandQuickShellSurfaceItemPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQWaylandQuickShellSurfaceItemPrivateCall12)(const void *, QQuickItem *, int *);
typedef bool (*CuteQWaylandQuickShellSurfaceItemPrivateCall13)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQWaylandQuickShellSurfaceItemPrivateCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall15)(const void *, bool, int *);
typedef void * (*CuteQWaylandQuickShellSurfaceItemPrivateCall16)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall17)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall18)(const void *, int *);
typedef void (*CuteQWaylandQuickShellSurfaceItemPrivateCall19)(const void *, int, int *);
class CuteQWaylandQuickShellSurfaceItemPrivate : public QWaylandQuickShellSurfaceItemPrivate {
public:
  using QWaylandQuickShellSurfaceItemPrivate::QWaylandQuickShellSurfaceItemPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN24QWaylandQuickItemPrivate5raiseEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QWaylandQuickItemPrivate5lowerEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[10] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[13] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[19] = call;
      return true;
    }
    return false;
  }

  //  void QWaylandQuickShellSurfaceItemPrivate::raise()
  void raise() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall0 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickShellSurfaceItemPrivate::raise();
  }

  //  void QWaylandQuickShellSurfaceItemPrivate::lower()
  void lower() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall1 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickShellSurfaceItemPrivate::lower();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall2 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall3 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall4 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall4>(taken[4]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall5 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall5>(taken[5]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      reason)
  bool setLastFocusChangeReason(Qt::FocusReason reason) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall6 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall7 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall8 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall9 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall10 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickItemPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall11 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall11>(taken[11]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickItemPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall12 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall12>(taken[12]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall13 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall13>(taken[13]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall14 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall14>(taken[14]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall15 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall16 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[17]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall17 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[18]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall18 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaylandQuickShellSurfaceItemPrivateCall19 call = reinterpret_cast<CuteQWaylandQuickShellSurfaceItemPrivateCall19>(taken[19]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QWaylandQuickShellSurfaceItem
//      *QWaylandQuickShellSurfaceItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItem *ritual_ZN36QWaylandQuickShellSurfaceItemPrivate6q_funcEv(
    QWaylandQuickShellSurfaceItemPrivate *self) {
  return self->q_func();
}

//  const QWaylandQuickShellSurfaceItem
//      *QWaylandQuickShellSurfaceItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQuickShellSurfaceItem *ritual_ZNK36QWaylandQuickShellSurfaceItemPrivate6q_funcEv(
    const QWaylandQuickShellSurfaceItemPrivate *self) {
  return self->q_func();
}

//  void QWaylandQuickShellSurfaceItemPrivate::setShellSurface(QWaylandShellS
//      urface *shellSurface)
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandQuickShellSurfaceItemPrivate15setShellSurfaceEP20QWaylandShellSurface(
    QWaylandQuickShellSurfaceItemPrivate *self,
    QWaylandShellSurface *shellSurface) {
  self->setShellSurface(shellSurface);
}

//  QWaylandQuickShellSurfaceItem *QWaylandQuickShellSurfaceItemPrivate::mayb
//      eCreateAutoPopup(QWaylandShellSurface *shellSurface)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItem *ritual_ZN36QWaylandQuickShellSurfaceItemPrivate20maybeCreateAutoPopupEP20QWaylandShellSurface(
    QWaylandQuickShellSurfaceItemPrivate *self,
    QWaylandShellSurface *shellSurface) {
  return self->maybeCreateAutoPopup(shellSurface);
}

//  QWaylandQuickShellSurfaceItemPrivate
//      *QWaylandQuickShellSurfaceItemPrivate::get(QWaylandQuickShellSurfaceI
//      tem *item)
extern "C" Q_DECL_EXPORT
QWaylandQuickShellSurfaceItemPrivate *ritual_ZN36QWaylandQuickShellSurfaceItemPrivate3getEP29QWaylandQuickShellSurfaceItem(
    QWaylandQuickShellSurfaceItem *item) {
  return QWaylandQuickShellSurfaceItemPrivate::get(item);
}

//  void QWaylandQuickShellSurfaceItemPrivate::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandQuickShellSurfaceItemPrivate5raiseEv(
    QWaylandQuickShellSurfaceItemPrivate *self) {
  self->raise();
}

//  void QWaylandQuickShellSurfaceItemPrivate::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN36QWaylandQuickShellSurfaceItemPrivate5lowerEv(
    QWaylandQuickShellSurfaceItemPrivate *self) {
  self->lower();
}

//  a Python function taken by a CuteQWaylandQuickShellSurfaceItemPrivate,
//      for the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickShellSurfaceItemPrivate(
    QWaylandQuickShellSurfaceItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickShellSurfaceItemPrivate *>(self)->take(key, call);
}

//  void QWaylandQuickShellSurfaceItemPrivate::raise()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QWaylandQuickShellSurfaceItemPrivate5raiseEv(
    QWaylandQuickShellSurfaceItemPrivate *self) {
  self->QWaylandQuickShellSurfaceItemPrivate::raise();
}

//  void QWaylandQuickShellSurfaceItemPrivate::lower()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN36QWaylandQuickShellSurfaceItemPrivate5lowerEv(
    QWaylandQuickShellSurfaceItemPrivate *self) {
  self->QWaylandQuickShellSurfaceItemPrivate::lower();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
