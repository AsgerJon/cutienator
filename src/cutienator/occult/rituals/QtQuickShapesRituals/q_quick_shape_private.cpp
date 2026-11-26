//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshapesglobal_p.h>
#include <QtQuickShapes/QtQuickShapes>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p.h>
#include <QtQuickShapes/6.12.0/QtQuickShapes/private/qquickshape_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <cstring>

//  A QQuickShapePrivate that Python can take functions over in. Every QQuickShapePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef qreal (*CuteQQuickShapePrivateCall0)(const void *, int *);
typedef qreal (*CuteQQuickShapePrivateCall1)(const void *, int *);
typedef void (*CuteQQuickShapePrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickShapePrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickShapePrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickShapePrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickShapePrivateCall6)(const void *, int, int *);
typedef void (*CuteQQuickShapePrivateCall7)(const void *, int *);
typedef void (*CuteQQuickShapePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickShapePrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickShapePrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickShapePrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickShapePrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickShapePrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickShapePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickShapePrivateCall15)(const void *, int *);
typedef void (*CuteQQuickShapePrivateCall16)(const void *, int *);
typedef void (*CuteQQuickShapePrivateCall17)(const void *, int, int *);
class CuteQQuickShapePrivate : public QQuickShapePrivate {
public:
  using QQuickShapePrivate::QQuickShapePrivate;
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
      CuteQQuickShapePrivateCall0 call = reinterpret_cast<CuteQQuickShapePrivateCall0>(taken[0]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitWidth();
  }

  //  qreal QQuickShapePrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickShapePrivateCall1 call = reinterpret_cast<CuteQQuickShapePrivateCall1>(taken[1]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickShapePrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickShapePrivateCall2 call = reinterpret_cast<CuteQQuickShapePrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickShapePrivateCall3 call = reinterpret_cast<CuteQQuickShapePrivateCall3>(taken[3]);
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
      CuteQQuickShapePrivateCall4 call = reinterpret_cast<CuteQQuickShapePrivateCall4>(taken[4]);
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
      CuteQQuickShapePrivateCall5 call = reinterpret_cast<CuteQQuickShapePrivateCall5>(taken[5]);
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
      CuteQQuickShapePrivateCall6 call = reinterpret_cast<CuteQQuickShapePrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickShapePrivateCall7 call = reinterpret_cast<CuteQQuickShapePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickShapePrivateCall8 call = reinterpret_cast<CuteQQuickShapePrivateCall8>(taken[8]);
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
      CuteQQuickShapePrivateCall9 call = reinterpret_cast<CuteQQuickShapePrivateCall9>(taken[9]);
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
      CuteQQuickShapePrivateCall10 call = reinterpret_cast<CuteQQuickShapePrivateCall10>(taken[10]);
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
      CuteQQuickShapePrivateCall11 call = reinterpret_cast<CuteQQuickShapePrivateCall11>(taken[11]);
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
      CuteQQuickShapePrivateCall12 call = reinterpret_cast<CuteQQuickShapePrivateCall12>(taken[12]);
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
      CuteQQuickShapePrivateCall13 call = reinterpret_cast<CuteQQuickShapePrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickShapePrivateCall14 call = reinterpret_cast<CuteQQuickShapePrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickShapePrivateCall15 call = reinterpret_cast<CuteQQuickShapePrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickShapePrivateCall16 call = reinterpret_cast<CuteQQuickShapePrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickShapePrivateCall17 call = reinterpret_cast<CuteQQuickShapePrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickShape *QQuickShapePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickShape *ritual_ZN18QQuickShapePrivate6q_funcEv(
    QQuickShapePrivate *self) {
  return self->q_func();
}

//  const QQuickShape *QQuickShapePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickShape *ritual_ZNK18QQuickShapePrivate6q_funcEv(
    const QQuickShapePrivate *self) {
  return self->q_func();
}

//  QQuickShapePrivate::QQuickShapePrivate()
extern "C" Q_DECL_EXPORT
QQuickShapePrivate *ritual_ZN18QQuickShapePrivateC1Ev() {
  return new CuteQQuickShapePrivate();
}

//  QQuickShapePrivate::~QQuickShapePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivateD1Ev(QQuickShapePrivate *self) {
  delete self;
}

//  void QQuickShapePrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate4initEv(QQuickShapePrivate *self) {
  self->init();
}

//  QQuickShape::RendererType QQuickShapePrivate::selectRendererType()
extern "C" Q_DECL_EXPORT
QQuickShape::RendererType ritual_ZN18QQuickShapePrivate18selectRendererTypeEv(
    QQuickShapePrivate *self) {
  return self->selectRendererType();
}

//  void QQuickShapePrivate::createRenderer()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate14createRendererEv(
    QQuickShapePrivate *self) {
  self->createRenderer();
}

//  QSGNode *QQuickShapePrivate::createNode()
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN18QQuickShapePrivate10createNodeEv(
    QQuickShapePrivate *self) {
  return self->createNode();
}

//  void QQuickShapePrivate::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate4syncEv(QQuickShapePrivate *self) {
  self->sync();
}

//  void QQuickShapePrivate::_q_shapePathChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate19_q_shapePathChangedEv(
    QQuickShapePrivate *self) {
  self->_q_shapePathChanged();
}

//  void QQuickShapePrivate::setStatus(QQuickShape::Status newStatus)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate9setStatusEN11QQuickShape6StatusE(
    QQuickShapePrivate *self,
    QQuickShape::Status newStatus) {
  self->setStatus(newStatus);
}

//  void QQuickShapePrivate::handleSceneChange(QQuickWindow *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate17handleSceneChangeEP12QQuickWindow(
    QQuickShapePrivate *self,
    QQuickWindow *w) {
  self->handleSceneChange(w);
}

//  QQuickShapePrivate *QQuickShapePrivate::get(QQuickShape *item)
extern "C" Q_DECL_EXPORT
QQuickShapePrivate *ritual_ZN18QQuickShapePrivate3getEP11QQuickShape(
    QQuickShape *item) {
  return QQuickShapePrivate::get(item);
}

//  void QQuickShapePrivate::asyncShapeReady(void *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QQuickShapePrivate15asyncShapeReadyEPv(void *data) {
  QQuickShapePrivate::asyncShapeReady(data);
}

//  qreal QQuickShapePrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickShapePrivate16getImplicitWidthEv(
    const QQuickShapePrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickShapePrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK18QQuickShapePrivate17getImplicitHeightEv(
    const QQuickShapePrivate *self) {
  return self->getImplicitHeight();
}

//  a Python function taken by a CuteQQuickShapePrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickShapePrivate(
    QQuickShapePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickShapePrivate *>(self)->take(key, call);
}

//  qreal QQuickShapePrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK18QQuickShapePrivate16getImplicitWidthEv(
    const QQuickShapePrivate *self) {
  return self->QQuickShapePrivate::getImplicitWidth();
}

//  qreal QQuickShapePrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK18QQuickShapePrivate17getImplicitHeightEv(
    const QQuickShapePrivate *self) {
  return self->QQuickShapePrivate::getImplicitHeight();
}
