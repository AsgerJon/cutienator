//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolyg
//  onshape_p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolygonshape_p.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickregularpolygonshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickRegularPolygonShapePrivate that Python can take functions over in. Every QQuickRegularPolygonShapePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickRegularPolygonShapePrivateCall0)(const void *, int *);
typedef qreal (*CuteQQuickRegularPolygonShapePrivateCall1)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickRegularPolygonShapePrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickRegularPolygonShapePrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickRegularPolygonShapePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickRegularPolygonShapePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickRegularPolygonShapePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickRegularPolygonShapePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickRegularPolygonShapePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickRegularPolygonShapePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickRegularPolygonShapePrivateCall17)(const void *, int, int *);
class CuteQQuickRegularPolygonShapePrivate : public QQuickRegularPolygonShapePrivate {
public:
  using QQuickRegularPolygonShapePrivate::QQuickRegularPolygonShapePrivate;
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
      CuteQQuickRegularPolygonShapePrivateCall0 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitWidth();
  }

  //  qreal QQuickShapePrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall1 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall2 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall3 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall3>(taken[3]);
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
      CuteQQuickRegularPolygonShapePrivateCall4 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall4>(taken[4]);
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
      CuteQQuickRegularPolygonShapePrivateCall5 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall5>(taken[5]);
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
      CuteQQuickRegularPolygonShapePrivateCall6 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall7 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall8 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall8>(taken[8]);
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
      CuteQQuickRegularPolygonShapePrivateCall9 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall9>(taken[9]);
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
      CuteQQuickRegularPolygonShapePrivateCall10 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall10>(taken[10]);
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
      CuteQQuickRegularPolygonShapePrivateCall11 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall11>(taken[11]);
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
      CuteQQuickRegularPolygonShapePrivateCall12 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall12>(taken[12]);
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
      CuteQQuickRegularPolygonShapePrivateCall13 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall14 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall15 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall16 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickRegularPolygonShapePrivateCall17 call = reinterpret_cast<CuteQQuickRegularPolygonShapePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickRegularPolygonShape *QQuickRegularPolygonShapePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickRegularPolygonShape *ritual_ZN32QQuickRegularPolygonShapePrivate6q_funcEv(
    QQuickRegularPolygonShapePrivate *self) {
  return self->q_func();
}

//  const QQuickRegularPolygonShape
//      *QQuickRegularPolygonShapePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickRegularPolygonShape *ritual_ZNK32QQuickRegularPolygonShapePrivate6q_funcEv(
    const QQuickRegularPolygonShapePrivate *self) {
  return self->q_func();
}

//  QQuickRegularPolygonShapePrivate::QQuickRegularPolygonShapePrivate()
extern "C" Q_DECL_EXPORT
QQuickRegularPolygonShapePrivate *ritual_ZN32QQuickRegularPolygonShapePrivateC1Ev() {
  return new CuteQQuickRegularPolygonShapePrivate();
}

//  QQuickRegularPolygonShapePrivate::~QQuickRegularPolygonShapePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivateD1Ev(
    QQuickRegularPolygonShapePrivate *self) {
  delete self;
}

//  void QQuickRegularPolygonShapePrivate::updatePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivate10updatePathEv(
    QQuickRegularPolygonShapePrivate *self) {
  self->updatePath();
}

//  void QQuickRegularPolygonShapePrivate::updatePoints()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivate12updatePointsEv(
    QQuickRegularPolygonShapePrivate *self) {
  self->updatePoints();
}

//  void QQuickRegularPolygonShapePrivate::updateBisectors()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivate15updateBisectorsEv(
    QQuickRegularPolygonShapePrivate *self) {
  self->updateBisectors();
}

//  void QQuickRegularPolygonShapePrivate::constructPolygonPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivate20constructPolygonPathEv(
    QQuickRegularPolygonShapePrivate *self) {
  self->constructPolygonPath();
}

//  void QQuickRegularPolygonShapePrivate::constructRoundedPolygonPath()
extern "C" Q_DECL_EXPORT
void ritual_ZN32QQuickRegularPolygonShapePrivate27constructRoundedPolygonPathEv(
    QQuickRegularPolygonShapePrivate *self) {
  self->constructRoundedPolygonPath();
}

//  a Python function taken by a CuteQQuickRegularPolygonShapePrivate, for
//      the function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickRegularPolygonShapePrivate(
    QQuickRegularPolygonShapePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickRegularPolygonShapePrivate *>(self)->take(key, call);
}
