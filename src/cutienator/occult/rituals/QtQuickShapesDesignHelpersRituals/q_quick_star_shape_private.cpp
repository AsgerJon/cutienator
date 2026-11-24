//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p_
//  p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickstarshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickStarShapePrivate that Python can take functions over in. Every QQuickStarShapePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickStarShapePrivateCall0)(const void *, int *);
typedef qreal (*CuteQQuickStarShapePrivateCall1)(const void *, int *);
typedef void (*CuteQQuickStarShapePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickStarShapePrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickStarShapePrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickStarShapePrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickStarShapePrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickStarShapePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickStarShapePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickStarShapePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickStarShapePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickStarShapePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickStarShapePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickStarShapePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickStarShapePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickStarShapePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickStarShapePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickStarShapePrivateCall17)(const void *, int, int *);
class CuteQQuickStarShapePrivate : public QQuickStarShapePrivate {
public:
  using QQuickStarShapePrivate::QQuickStarShapePrivate;
  void *taken[18] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
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

  //  qreal QQuickShapePrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall0 call = reinterpret_cast<CuteQQuickStarShapePrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitWidth();
  }

  //  qreal QQuickShapePrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall1 call = reinterpret_cast<CuteQQuickStarShapePrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall2 call = reinterpret_cast<CuteQQuickStarShapePrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall3 call = reinterpret_cast<CuteQQuickStarShapePrivateCall3>(taken[3]);
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
      CuteQQuickStarShapePrivateCall4 call = reinterpret_cast<CuteQQuickStarShapePrivateCall4>(taken[4]);
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
      CuteQQuickStarShapePrivateCall5 call = reinterpret_cast<CuteQQuickStarShapePrivateCall5>(taken[5]);
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
      CuteQQuickStarShapePrivateCall6 call = reinterpret_cast<CuteQQuickStarShapePrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall7 call = reinterpret_cast<CuteQQuickStarShapePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall8 call = reinterpret_cast<CuteQQuickStarShapePrivateCall8>(taken[8]);
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
      CuteQQuickStarShapePrivateCall9 call = reinterpret_cast<CuteQQuickStarShapePrivateCall9>(taken[9]);
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
      CuteQQuickStarShapePrivateCall10 call = reinterpret_cast<CuteQQuickStarShapePrivateCall10>(taken[10]);
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
      CuteQQuickStarShapePrivateCall11 call = reinterpret_cast<CuteQQuickStarShapePrivateCall11>(taken[11]);
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
      CuteQQuickStarShapePrivateCall12 call = reinterpret_cast<CuteQQuickStarShapePrivateCall12>(taken[12]);
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
      CuteQQuickStarShapePrivateCall13 call = reinterpret_cast<CuteQQuickStarShapePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall14 call = reinterpret_cast<CuteQQuickStarShapePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall15 call = reinterpret_cast<CuteQQuickStarShapePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall16 call = reinterpret_cast<CuteQQuickStarShapePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickStarShapePrivateCall17 call = reinterpret_cast<CuteQQuickStarShapePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickStarShape *QQuickStarShapePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickStarShape *ritual_ZN22QQuickStarShapePrivate6q_funcEv(
    QQuickStarShapePrivate *self) {
  return self->q_func();
}

//  const QQuickStarShape *QQuickStarShapePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickStarShape *ritual_ZNK22QQuickStarShapePrivate6q_funcEv(
    const QQuickStarShapePrivate *self) {
  return self->q_func();
}

//  QQuickStarShapePrivate::QQuickStarShapePrivate()
extern "C" Q_DECL_EXPORT
QQuickStarShapePrivate *ritual_ZN22QQuickStarShapePrivateC1Ev() {
  return new CuteQQuickStarShapePrivate();
}

//  QQuickStarShapePrivate::~QQuickStarShapePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStarShapePrivateD1Ev(QQuickStarShapePrivate *self) {
  delete self;
}

//  void QQuickStarShapePrivate::updatePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStarShapePrivate10updatePathEv(
    QQuickStarShapePrivate *self) {
  self->updatePath();
}

//  void QQuickStarShapePrivate::updatePoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStarShapePrivate12updatePointsEv(
    QQuickStarShapePrivate *self) {
  self->updatePoints();
}

//  void QQuickStarShapePrivate::constructPolygonPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStarShapePrivate20constructPolygonPathEv(
    QQuickStarShapePrivate *self) {
  self->constructPolygonPath();
}

//  void QQuickStarShapePrivate::constructRoundedPolygonPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickStarShapePrivate27constructRoundedPolygonPathEv(
    QQuickStarShapePrivate *self) {
  self->constructRoundedPolygonPath();
}

//  a Python function taken by a CuteQQuickStarShapePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickStarShapePrivate(
    QQuickStarShapePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickStarShapePrivate *>(self)->take(key, call);
}
