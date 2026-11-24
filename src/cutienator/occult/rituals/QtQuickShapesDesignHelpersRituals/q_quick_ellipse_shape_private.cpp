//  Written by dev_tooling.RitualGenerator from the records of QtQuickShapesD
//  esignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape
//  _p_p.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickshapesdesignhelpersglobal_p.h>
#include <QtQuickShapesDesignHelpers/QtQuickShapesDesignHelpers>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p.h>
#include <QtQuickShapesDesignHelpers/6.12.0/QtQuickShapesDesignHelpers/private/qquickellipseshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <cstring>

//  A QQuickEllipseShapePrivate that Python can take functions over in. Every QQuickEllipseShapePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickEllipseShapePrivateCall0)(const void *, int *);
typedef qreal (*CuteQQuickEllipseShapePrivateCall1)(const void *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickEllipseShapePrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickEllipseShapePrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickEllipseShapePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickEllipseShapePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickEllipseShapePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickEllipseShapePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickEllipseShapePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickEllipseShapePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickEllipseShapePrivateCall17)(const void *, int, int *);
class CuteQQuickEllipseShapePrivate : public QQuickEllipseShapePrivate {
public:
  using QQuickEllipseShapePrivate::QQuickEllipseShapePrivate;
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
      CuteQQuickEllipseShapePrivateCall0 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitWidth();
  }

  //  qreal QQuickShapePrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall1 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall2 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall3 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall3>(taken[3]);
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
      CuteQQuickEllipseShapePrivateCall4 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall4>(taken[4]);
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
      CuteQQuickEllipseShapePrivateCall5 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall5>(taken[5]);
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
      CuteQQuickEllipseShapePrivateCall6 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall7 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall8 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall8>(taken[8]);
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
      CuteQQuickEllipseShapePrivateCall9 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall9>(taken[9]);
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
      CuteQQuickEllipseShapePrivateCall10 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall10>(taken[10]);
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
      CuteQQuickEllipseShapePrivateCall11 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall11>(taken[11]);
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
      CuteQQuickEllipseShapePrivateCall12 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall12>(taken[12]);
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
      CuteQQuickEllipseShapePrivateCall13 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall14 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall15 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall16 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickEllipseShapePrivateCall17 call = reinterpret_cast<CuteQQuickEllipseShapePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickEllipseShape *QQuickEllipseShapePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickEllipseShape *ritual_ZN25QQuickEllipseShapePrivate6q_funcEv(
    QQuickEllipseShapePrivate *self) {
  return self->q_func();
}

//  const QQuickEllipseShape *QQuickEllipseShapePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickEllipseShape *ritual_ZNK25QQuickEllipseShapePrivate6q_funcEv(
    const QQuickEllipseShapePrivate *self) {
  return self->q_func();
}

//  QQuickEllipseShapePrivate::QQuickEllipseShapePrivate()
extern "C" Q_DECL_EXPORT
QQuickEllipseShapePrivate *ritual_ZN25QQuickEllipseShapePrivateC1Ev() {
  return new CuteQQuickEllipseShapePrivate();
}

//  QQuickEllipseShapePrivate::~QQuickEllipseShapePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivateD1Ev(
    QQuickEllipseShapePrivate *self) {
  delete self;
}

//  void QQuickEllipseShapePrivate::addLine(QVector2D point)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate7addLineE9QVector2D(
    QQuickEllipseShapePrivate *self,
    const QVector2D *point) {
  self->addLine(*point);
}

//  void QQuickEllipseShapePrivate::addArc(QVector2D point, QVector2D
//      arcRadius, QQuickPathArc::ArcDirection dir, bool largeArc)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate6addArcE9QVector2DS0_N13QQuickPathArc12ArcDirectionEb(
    QQuickEllipseShapePrivate *self,
    const QVector2D *point,
    const QVector2D *arcRadius,
    QQuickPathArc::ArcDirection dir,
    bool largeArc) {
  self->addArc(*point, *arcRadius, dir, largeArc);
}

//  qreal QQuickEllipseShapePrivate::getBorderOffset() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK25QQuickEllipseShapePrivate15getBorderOffsetEv(
    const QQuickEllipseShapePrivate *self) {
  return self->getBorderOffset();
}

//  void QQuickEllipseShapePrivate::roundCenter(QVector2D center, QVector2D
//      ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate11roundCenterE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->roundCenter(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::roundBeginEnd(QVector2D center, QVector2D
//      ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate13roundBeginEndE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->roundBeginEnd(*center, *ellipseRadius);
}

//  bool QQuickEllipseShapePrivate::roundOuter(QVector2D center, QVector2D
//      ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
//      RoundedCornerIndex index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickEllipseShapePrivate10roundOuterE9QVector2DS0_dddNS_18RoundedCornerIndexE(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius,
    qreal deg,
    qreal arcAngle1,
    qreal arcAngle2,
    QQuickEllipseShapePrivate::RoundedCornerIndex index) {
  return self->roundOuter(
      *center,
      *ellipseRadius,
      deg,
      arcAngle1,
      arcAngle2,
      index);
}

//  bool QQuickEllipseShapePrivate::roundInner(QVector2D center, QVector2D
//      ellipseRadius, qreal deg, qreal arcAngle1, qreal arcAngle2,
//      RoundedCornerIndex index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQuickEllipseShapePrivate10roundInnerE9QVector2DS0_dddNS_18RoundedCornerIndexE(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius,
    qreal deg,
    qreal arcAngle1,
    qreal arcAngle2,
    QQuickEllipseShapePrivate::RoundedCornerIndex index) {
  return self->roundInner(
      *center,
      *ellipseRadius,
      deg,
      arcAngle1,
      arcAngle2,
      index);
}

//  void QQuickEllipseShapePrivate::drawCenterCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate16drawCenterCornerEv(
    QQuickEllipseShapePrivate *self) {
  self->drawCenterCorner();
}

//  void QQuickEllipseShapePrivate::drawInnerEndCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate18drawInnerEndCornerEv(
    QQuickEllipseShapePrivate *self) {
  self->drawInnerEndCorner();
}

//  void QQuickEllipseShapePrivate::drawInnerBeginCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate20drawInnerBeginCornerEv(
    QQuickEllipseShapePrivate *self) {
  self->drawInnerBeginCorner();
}

//  void QQuickEllipseShapePrivate::drawOuterBeginCorner()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate20drawOuterBeginCornerEv(
    QQuickEllipseShapePrivate *self) {
  self->drawOuterBeginCorner();
}

//  void QQuickEllipseShapePrivate::drawOuterArcRounded(QVector2D center,
//      QVector2D ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate19drawOuterArcRoundedE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawOuterArcRounded(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::drawInnerArcRounded(QVector2D center,
//      QVector2D ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate19drawInnerArcRoundedE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawInnerArcRounded(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::drawOuterArc(QVector2D center, QVector2D
//      ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate12drawOuterArcE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawOuterArc(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::drawFullInnerArc(QVector2D center,
//      QVector2D ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate16drawFullInnerArcE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawFullInnerArc(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::drawWithInnerRadius(QVector2D center,
//      QVector2D ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate19drawWithInnerRadiusE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawWithInnerRadius(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::drawWithoutInnerRadius(QVector2D center,
//      QVector2D ellipseRadius)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate22drawWithoutInnerRadiusE9QVector2DS0_(
    QQuickEllipseShapePrivate *self,
    const QVector2D *center,
    const QVector2D *ellipseRadius) {
  self->drawWithoutInnerRadius(*center, *ellipseRadius);
}

//  void QQuickEllipseShapePrivate::updatePath()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQuickEllipseShapePrivate10updatePathEv(
    QQuickEllipseShapePrivate *self) {
  self->updatePath();
}

//  a Python function taken by a CuteQQuickEllipseShapePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickEllipseShapePrivate(
    QQuickEllipseShapePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickEllipseShapePrivate *>(self)->take(key, call);
}
