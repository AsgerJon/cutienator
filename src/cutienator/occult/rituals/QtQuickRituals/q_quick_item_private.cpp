//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickitem_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#include <QtQuick/qquickitem.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickanchors_p_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qtransform.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qeventpoint.h>
#include <QtGui/qcursor.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qlayoutpolicy_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#include <cstring>

//  A QQuickItemPrivate that Python can take functions over in. Every QQuickItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickItemPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickItemPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickItemPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickItemPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickItemPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickItemPrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickItemPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickItemPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickItemPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickItemPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickItemPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickItemPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickItemPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickItemPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickItemPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickItemPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickItemPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickItemPrivateCall17)(const void *, int, int *);
class CuteQQuickItemPrivate : public QQuickItemPrivate {
public:
  using QQuickItemPrivate::QQuickItemPrivate;
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
      CuteQQuickItemPrivateCall0 call = reinterpret_cast<CuteQQuickItemPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickItemPrivateCall1 call = reinterpret_cast<CuteQQuickItemPrivateCall1>(taken[1]);
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
      CuteQQuickItemPrivateCall2 call = reinterpret_cast<CuteQQuickItemPrivateCall2>(taken[2]);
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
      CuteQQuickItemPrivateCall3 call = reinterpret_cast<CuteQQuickItemPrivateCall3>(taken[3]);
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
      CuteQQuickItemPrivateCall4 call = reinterpret_cast<CuteQQuickItemPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickItemPrivateCall5 call = reinterpret_cast<CuteQQuickItemPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickItemPrivateCall6 call = reinterpret_cast<CuteQQuickItemPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickItemPrivateCall7 call = reinterpret_cast<CuteQQuickItemPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickItemPrivateCall8 call = reinterpret_cast<CuteQQuickItemPrivateCall8>(taken[8]);
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
      CuteQQuickItemPrivateCall9 call = reinterpret_cast<CuteQQuickItemPrivateCall9>(taken[9]);
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
      CuteQQuickItemPrivateCall10 call = reinterpret_cast<CuteQQuickItemPrivateCall10>(taken[10]);
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
      CuteQQuickItemPrivateCall11 call = reinterpret_cast<CuteQQuickItemPrivateCall11>(taken[11]);
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
      CuteQQuickItemPrivateCall12 call = reinterpret_cast<CuteQQuickItemPrivateCall12>(taken[12]);
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
      CuteQQuickItemPrivateCall13 call = reinterpret_cast<CuteQQuickItemPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickItemPrivateCall14 call = reinterpret_cast<CuteQQuickItemPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickItemPrivateCall15 call = reinterpret_cast<CuteQQuickItemPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickItemPrivateCall16 call = reinterpret_cast<CuteQQuickItemPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickItemPrivateCall17 call = reinterpret_cast<CuteQQuickItemPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickItem *QQuickItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickItemPrivate6q_funcEv(QQuickItemPrivate *self) {
  return self->q_func();
}

//  const QQuickItem *QQuickItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickItem *ritual_ZNK17QQuickItemPrivate6q_funcEv(
    const QQuickItemPrivate *self) {
  return self->q_func();
}

//  QQuickItemPrivate *QQuickItemPrivate::get(QQuickItem *item)
extern "C" Q_DECL_EXPORT
QQuickItemPrivate *ritual_ZN17QQuickItemPrivate3getEP10QQuickItem(
    QQuickItem *item) {
  return QQuickItemPrivate::get(item);
}

//  const QQuickItemPrivate *QQuickItemPrivate::get(const QQuickItem *item)
extern "C" Q_DECL_EXPORT
const QQuickItemPrivate *ritual_ZN17QQuickItemPrivate3getEPK10QQuickItem(
    const QQuickItem *item) {
  return QQuickItemPrivate::get(item);
}

//  QQuickItemPrivate::QQuickItemPrivate()
extern "C" Q_DECL_EXPORT
QQuickItemPrivate *ritual_ZN17QQuickItemPrivateC1Ev() {
  return new CuteQQuickItemPrivate();
}

//  QQuickItemPrivate::~QQuickItemPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivateD1Ev(QQuickItemPrivate *self) {
  delete self;
}

//  void QQuickItemPrivate::init(QQuickItem *parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate4initEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *parent) {
  self->init(parent);
}

//  QString QQuickItemPrivate::state() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickItemPrivate5stateEv(
    const QQuickItemPrivate *self) {
  return new QString(self->state());
}

//  void QQuickItemPrivate::setState(const QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate8setStateERK7QString(
    QQuickItemPrivate *self,
    const QString *a0) {
  self->setState(*a0);
}

//  QQuickAnchorLine QQuickItemPrivate::left() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate4leftEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->left());
}

//  QQuickAnchorLine QQuickItemPrivate::right() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate5rightEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->right());
}

//  QQuickAnchorLine QQuickItemPrivate::horizontalCenter() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate16horizontalCenterEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->horizontalCenter());
}

//  QQuickAnchorLine QQuickItemPrivate::top() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate3topEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->top());
}

//  QQuickAnchorLine QQuickItemPrivate::bottom() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate6bottomEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->bottom());
}

//  QQuickAnchorLine QQuickItemPrivate::verticalCenter() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate14verticalCenterEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->verticalCenter());
}

//  QQuickAnchorLine QQuickItemPrivate::baseline() const
extern "C" Q_DECL_EXPORT
QQuickAnchorLine *ritual_ZNK17QQuickItemPrivate8baselineEv(
    const QQuickItemPrivate *self) {
  return new QQuickAnchorLine(self->baseline());
}

#if QT_CONFIG(quick_shadereffect)
//  QQuickItemLayer *QQuickItemPrivate::layer() const
extern "C" Q_DECL_EXPORT
QQuickItemLayer *ritual_ZNK17QQuickItemPrivate5layerEv(
    const QQuickItemPrivate *self) {
  return self->layer();
}
#endif  // QT_CONFIG(quick_shadereffect)

//  void QQuickItemPrivate::localizedTouchEvent(const QTouchEvent *event,
//      bool isFiltering, QMutableTouchEvent *localized)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19localizedTouchEventEPK11QTouchEventbP18QMutableTouchEvent(
    QQuickItemPrivate *self,
    const QTouchEvent *event,
    bool isFiltering,
    QMutableTouchEvent *localized) {
  self->localizedTouchEvent(event, isFiltering, localized);
}

//  bool QQuickItemPrivate::hasPointerHandlers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate18hasPointerHandlersEv(
    const QQuickItemPrivate *self) {
  return self->hasPointerHandlers();
}

//  bool QQuickItemPrivate::hasEnabledHoverHandlers() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate23hasEnabledHoverHandlersEv(
    const QQuickItemPrivate *self) {
  return self->hasEnabledHoverHandlers();
}

//  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler(
    QQuickItemPrivate *self,
    QQuickPointerHandler *h) {
  self->addPointerHandler(h);
}

//  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler(
    QQuickItemPrivate *self,
    QQuickPointerHandler *h) {
  self->removePointerHandler(h);
}

//  QObject *QQuickItemPrivate::setContextMenu(QObject *menu)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN17QQuickItemPrivate14setContextMenuEP7QObject(
    QQuickItemPrivate *self,
    QObject *menu) {
  return self->setContextMenu(menu);
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
//      QMetaObject *attachedType)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject(
    QQuickItemPrivate *self,
    const QMetaObject *attachedType) {
  return self->attachedPropertyPropagator_parent(attachedType);
}

//  void QQuickItemPrivate::_q_resourceObjectDeleted(QObject *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate24_q_resourceObjectDeletedEP7QObject(
    QQuickItemPrivate *self,
    QObject *a0) {
  self->_q_resourceObjectDeleted(a0);
}

//  quint64 QQuickItemPrivate::_q_createJSWrapper(QQmlV4ExecutionEnginePtr
//      engine)
extern "C" Q_DECL_EXPORT
quint64 ritual_ZN17QQuickItemPrivate18_q_createJSWrapperEPN3QV415ExecutionEngineE(
    QQuickItemPrivate *self,
    QQmlV4ExecutionEnginePtr engine) {
  return self->_q_createJSWrapper(engine);
}

//  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0, bool
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb(
    QQuickItemPrivate *self,
    QQuickItem *a0,
    bool a1) {
  self->registerAsContainmentMask(a0, a1);
}

//  QQuickAnchors *QQuickItemPrivate::anchors() const
extern "C" Q_DECL_EXPORT
QQuickAnchors *ritual_ZNK17QQuickItemPrivate7anchorsEv(
    const QQuickItemPrivate *self) {
  return self->anchors();
}

//  Qt::MouseButtons QQuickItemPrivate::acceptedMouseButtons() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QQuickItemPrivate20acceptedMouseButtonsEv(
    const QQuickItemPrivate *self) {
  return static_cast<int>(self->acceptedMouseButtons().toInt());
}

//  void QQuickItemPrivate::addItemChangeListener(QQuickItemChangeListener
//      *listener, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate21addItemChangeListenerEP24QQuickItemChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuickItemPrivate *self,
    QQuickItemChangeListener *listener,
    int types) {
  self->addItemChangeListener(
      listener,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(types));
}

//  void
//      QQuickItemPrivate::updateOrAddItemChangeListener(QQuickItemChangeList
//      ener *listener, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate29updateOrAddItemChangeListenerEP24QQuickItemChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuickItemPrivate *self,
    QQuickItemChangeListener *listener,
    int types) {
  self->updateOrAddItemChangeListener(
      listener,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(types));
}

//  void QQuickItemPrivate::removeItemChangeListener(QQuickItemChangeListener
//      *a0, ChangeTypes types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate24removeItemChangeListenerEP24QQuickItemChangeListener6QFlagsINS_10ChangeTypeEE(
    QQuickItemPrivate *self,
    QQuickItemChangeListener *a0,
    int types) {
  self->removeItemChangeListener(
      a0,
      QFlags<QQuickItemPrivate::ChangeType>::fromInt(types));
}

//  void QQuickItemPrivate::updateOrAddGeometryChangeListener(QQuickItemChang
//      eListener *listener, QQuickGeometryChange types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate33updateOrAddGeometryChangeListenerEP24QQuickItemChangeListener20QQuickGeometryChange(
    QQuickItemPrivate *self,
    QQuickItemChangeListener *listener,
    const QQuickGeometryChange *types) {
  self->updateOrAddGeometryChangeListener(listener, *types);
}

//  void QQuickItemPrivate::updateOrRemoveGeometryChangeListener(QQuickItemCh
//      angeListener *listener, QQuickGeometryChange types)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate36updateOrRemoveGeometryChangeListenerEP24QQuickItemChangeListener20QQuickGeometryChange(
    QQuickItemPrivate *self,
    QQuickItemChangeListener *listener,
    const QQuickGeometryChange *types) {
  self->updateOrRemoveGeometryChangeListener(listener, *types);
}

//  QQuickStateGroup *QQuickItemPrivate::_states()
extern "C" Q_DECL_EXPORT
QQuickStateGroup *ritual_ZN17QQuickItemPrivate7_statesEv(
    QQuickItemPrivate *self) {
  return self->_states();
}

//  QQuickItem::TransformOrigin QQuickItemPrivate::origin() const
extern "C" Q_DECL_EXPORT
QQuickItem::TransformOrigin ritual_ZNK17QQuickItemPrivate6originEv(
    const QQuickItemPrivate *self) {
  return self->origin();
}

//  void QQuickItemPrivate::requestCustomOverlay()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate20requestCustomOverlayEv(
    QQuickItemPrivate *self) {
  self->requestCustomOverlay();
}

//  QString QQuickItemPrivate::dirtyToString() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QQuickItemPrivate13dirtyToStringEv(
    const QQuickItemPrivate *self) {
  return new QString(self->dirtyToString());
}

//  void QQuickItemPrivate::dirty(DirtyType a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate5dirtyENS_9DirtyTypeE(
    QQuickItemPrivate *self,
    QQuickItemPrivate::DirtyType a0) {
  self->dirty(a0);
}

//  void QQuickItemPrivate::addToDirtyList()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate14addToDirtyListEv(
    QQuickItemPrivate *self) {
  self->addToDirtyList();
}

//  void QQuickItemPrivate::removeFromDirtyList()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19removeFromDirtyListEv(
    QQuickItemPrivate *self) {
  self->removeFromDirtyList();
}

//  void QQuickItemPrivate::setCulled(bool a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate9setCulledEb(
    QQuickItemPrivate *self,
    bool a0) {
  self->setCulled(a0);
}

//  QWindow *QQuickItemPrivate::renderWindow(QPoint *offset) const
extern "C" Q_DECL_EXPORT
QWindow *ritual_ZNK17QQuickItemPrivate12renderWindowEP6QPoint(
    const QQuickItemPrivate *self,
    QPoint *offset) {
  return self->renderWindow(offset);
}

//  QSGContext *QQuickItemPrivate::sceneGraphContext() const
extern "C" Q_DECL_EXPORT
QSGContext *ritual_ZNK17QQuickItemPrivate17sceneGraphContextEv(
    const QQuickItemPrivate *self) {
  return self->sceneGraphContext();
}

//  QSGRenderContext *QQuickItemPrivate::sceneGraphRenderContext() const
extern "C" Q_DECL_EXPORT
QSGRenderContext *ritual_ZNK17QQuickItemPrivate23sceneGraphRenderContextEv(
    const QQuickItemPrivate *self) {
  return self->sceneGraphRenderContext();
}

//  QList<QQuickItem *> QQuickItemPrivate::paintOrderChildItems() const
extern "C" Q_DECL_EXPORT
QList<QQuickItem *> *ritual_ZNK17QQuickItemPrivate20paintOrderChildItemsEv(
    const QQuickItemPrivate *self) {
  return new QList<QQuickItem *>(self->paintOrderChildItems());
}

//  void QQuickItemPrivate::addChild(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate8addChildEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *a0) {
  self->addChild(a0);
}

//  void QQuickItemPrivate::removeChild(QQuickItem *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate11removeChildEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *a0) {
  self->removeChild(a0);
}

//  void QQuickItemPrivate::siblingOrderChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19siblingOrderChangedEv(
    QQuickItemPrivate *self) {
  self->siblingOrderChanged();
}

//  void QQuickItemPrivate::markSortedChildrenDirty(QQuickItem *child)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23markSortedChildrenDirtyEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *child) {
  self->markSortedChildrenDirty(child);
}

//  void QQuickItemPrivate::refWindow(QQuickWindow *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate9refWindowEP12QQuickWindow(
    QQuickItemPrivate *self,
    QQuickWindow *a0) {
  self->refWindow(a0);
}

//  void QQuickItemPrivate::derefWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate11derefWindowEv(QQuickItemPrivate *self) {
  self->derefWindow();
}

//  qreal QQuickItemPrivate::effectiveDevicePixelRatio() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate25effectiveDevicePixelRatioEv(
    const QQuickItemPrivate *self) {
  return self->effectiveDevicePixelRatio();
}

//  void QQuickItemPrivate::updateSubFocusItem(QQuickItem *scope, bool focus)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate18updateSubFocusItemEP10QQuickItemb(
    QQuickItemPrivate *self,
    QQuickItem *scope,
    bool focus) {
  self->updateSubFocusItem(scope, focus);
}

//  bool QQuickItemPrivate::setFocusIfNeeded(QEvent::Type a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate16setFocusIfNeededEN6QEvent4TypeE(
    QQuickItemPrivate *self,
    QEvent::Type a0) {
  return self->setFocusIfNeeded(a0);
}

//  Qt::FocusReason QQuickItemPrivate::lastFocusChangeReason() const
extern "C" Q_DECL_EXPORT
Qt::FocusReason ritual_ZNK17QQuickItemPrivate21lastFocusChangeReasonEv(
    const QQuickItemPrivate *self) {
  return self->lastFocusChangeReason();
}

//  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickItemPrivate *self,
    Qt::FocusReason reason) {
  return self->setLastFocusChangeReason(reason);
}

//  QTransform QQuickItemPrivate::windowToItemTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QQuickItemPrivate21windowToItemTransformEv(
    const QQuickItemPrivate *self) {
  return new QTransform(self->windowToItemTransform());
}

//  QTransform QQuickItemPrivate::itemToWindowTransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QQuickItemPrivate21itemToWindowTransformEv(
    const QQuickItemPrivate *self) {
  return new QTransform(self->itemToWindowTransform());
}

//  void QQuickItemPrivate::itemToParentTransform(QTransform *a0) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQuickItemPrivate21itemToParentTransformEP10QTransform(
    const QQuickItemPrivate *self,
    QTransform *a0) {
  self->itemToParentTransform(a0);
}

//  bool QQuickItemPrivate::focusNextPrev(QQuickItem *item, bool forward)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate13focusNextPrevEP10QQuickItemb(
    QQuickItem *item,
    bool forward) {
  return QQuickItemPrivate::focusNextPrev(item, forward);
}

//  QQuickItem *QQuickItemPrivate::nextTabChildItem(const QQuickItem *item,
//      int start)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickItemPrivate16nextTabChildItemEPK10QQuickItemi(
    const QQuickItem *item,
    int start) {
  return QQuickItemPrivate::nextTabChildItem(item, start);
}

//  QQuickItem *QQuickItemPrivate::prevTabChildItem(const QQuickItem *item,
//      int start)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickItemPrivate16prevTabChildItemEPK10QQuickItemi(
    const QQuickItem *item,
    int start) {
  return QQuickItemPrivate::prevTabChildItem(item, start);
}

//  QQuickItem *QQuickItemPrivate::nextPrevItemInTabFocusChain(QQuickItem
//      *item, bool forward, bool wrap)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN17QQuickItemPrivate27nextPrevItemInTabFocusChainEP10QQuickItembb(
    QQuickItem *item,
    bool forward,
    bool wrap) {
  return QQuickItemPrivate::nextPrevItemInTabFocusChain(item, forward, wrap);
}

//  bool QQuickItemPrivate::canAcceptTabFocus(QQuickItem *item)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate17canAcceptTabFocusEP10QQuickItem(
    QQuickItem *item) {
  return QQuickItemPrivate::canAcceptTabFocus(item);
}

//  void QQuickItemPrivate::setX(qreal x)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate4setXEd(QQuickItemPrivate *self, qreal x) {
  self->setX(x);
}

//  void QQuickItemPrivate::xChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate8xChangedEv(QQuickItemPrivate *self) {
  self->xChanged();
}

//  void QQuickItemPrivate::setY(qreal y)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate4setYEd(QQuickItemPrivate *self, qreal y) {
  self->setY(y);
}

//  void QQuickItemPrivate::yChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate8yChangedEv(QQuickItemPrivate *self) {
  self->yChanged();
}

//  void QQuickItemPrivate::setWidth(qreal width)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate8setWidthEd(
    QQuickItemPrivate *self,
    qreal width) {
  self->setWidth(width);
}

//  void QQuickItemPrivate::widthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate12widthChangedEv(QQuickItemPrivate *self) {
  self->widthChanged();
}

//  void QQuickItemPrivate::setHeight(qreal height)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate9setHeightEd(
    QQuickItemPrivate *self,
    qreal height) {
  self->setHeight(height);
}

//  void QQuickItemPrivate::heightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate13heightChangedEv(QQuickItemPrivate *self) {
  self->heightChanged();
}

//  bool QQuickItemPrivate::widthValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate10widthValidEv(
    const QQuickItemPrivate *self) {
  return self->widthValid();
}

//  bool QQuickItemPrivate::heightValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate11heightValidEv(
    const QQuickItemPrivate *self) {
  return self->heightValid();
}

//  qreal QQuickItemPrivate::z() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate1zEv(const QQuickItemPrivate *self) {
  return self->z();
}

//  qreal QQuickItemPrivate::scale() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate5scaleEv(const QQuickItemPrivate *self) {
  return self->scale();
}

//  qreal QQuickItemPrivate::rotation() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate8rotationEv(
    const QQuickItemPrivate *self) {
  return self->rotation();
}

//  qreal QQuickItemPrivate::opacity() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate7opacityEv(
    const QQuickItemPrivate *self) {
  return self->opacity();
}

//  void QQuickItemPrivate::setAccessible()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate13setAccessibleEv(QQuickItemPrivate *self) {
  self->setAccessible();
}

//  qreal QQuickItemPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate16getImplicitWidthEv(
    const QQuickItemPrivate *self) {
  return self->getImplicitWidth();
}

//  qreal QQuickItemPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate17getImplicitHeightEv(
    const QQuickItemPrivate *self) {
  return self->getImplicitHeight();
}

//  void QQuickItemPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate20implicitWidthChangedEv(
    QQuickItemPrivate *self) {
  self->implicitWidthChanged();
}

//  void QQuickItemPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate21implicitHeightChangedEv(
    QQuickItemPrivate *self) {
  self->implicitHeightChanged();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickItemPrivate::effectiveAccessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickItemPrivate23effectiveAccessibleRoleEv(
    const QQuickItemPrivate *self) {
  return self->effectiveAccessibleRole();
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickItemPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_ZNK17QQuickItemPrivate14accessibleRoleEv(
    const QQuickItemPrivate *self) {
  return self->accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  void QQuickItemPrivate::setImplicitAntialiasing(bool antialiasing)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23setImplicitAntialiasingEb(
    QQuickItemPrivate *self,
    bool antialiasing) {
  self->setImplicitAntialiasing(antialiasing);
}

//  void QQuickItemPrivate::resolveLayoutMirror()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19resolveLayoutMirrorEv(
    QQuickItemPrivate *self) {
  self->resolveLayoutMirror();
}

//  void QQuickItemPrivate::setImplicitLayoutMirror(bool mirror, bool
//      inherit)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23setImplicitLayoutMirrorEbb(
    QQuickItemPrivate *self,
    bool mirror,
    bool inherit) {
  self->setImplicitLayoutMirror(mirror, inherit);
}

//  void QQuickItemPrivate::setLayoutMirror(bool mirror)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate15setLayoutMirrorEb(
    QQuickItemPrivate *self,
    bool mirror) {
  self->setLayoutMirror(mirror);
}

//  bool QQuickItemPrivate::isMirrored() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate10isMirroredEv(
    const QQuickItemPrivate *self) {
  return self->isMirrored();
}

//  void QQuickItemPrivate::emitChildrenRectChanged(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23emitChildrenRectChangedERK6QRectF(
    QQuickItemPrivate *self,
    const QRectF *rect) {
  self->emitChildrenRectChanged(*rect);
}

//  QPointF QQuickItemPrivate::computeTransformOrigin() const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK17QQuickItemPrivate22computeTransformOriginEv(
    const QQuickItemPrivate *self) {
  return new QPointF(self->computeTransformOrigin());
}

//  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *transformedItem) {
  return self->transformChanged(transformedItem);
}

//  QPointF QQuickItemPrivate::adjustedPosForTransform(const QPointF
//      &centroid, const QPointF &startPos, const QVector2D
//      &activeTranslatation, qreal startScale, qreal activeScale, qreal
//      startRotation, qreal activeRotation)
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZN17QQuickItemPrivate23adjustedPosForTransformERK7QPointFS2_RK9QVector2Ddddd(
    QQuickItemPrivate *self,
    const QPointF *centroid,
    const QPointF *startPos,
    const QVector2D *activeTranslatation,
    qreal startScale,
    qreal activeScale,
    qreal startRotation,
    qreal activeRotation) {
  return new QPointF(
      self->adjustedPosForTransform(
          *centroid,
          *startPos,
          *activeTranslatation,
          startScale,
          activeScale,
          startRotation,
          activeRotation));
}

//  QQuickDeliveryAgent *QQuickItemPrivate::deliveryAgent()
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent *ritual_ZN17QQuickItemPrivate13deliveryAgentEv(
    QQuickItemPrivate *self) {
  return self->deliveryAgent();
}

//  QQuickDeliveryAgentPrivate *QQuickItemPrivate::deliveryAgentPrivate()
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgentPrivate *ritual_ZN17QQuickItemPrivate20deliveryAgentPrivateEv(
    QQuickItemPrivate *self) {
  return self->deliveryAgentPrivate();
}

//  QQuickDeliveryAgent *QQuickItemPrivate::ensureSubsceneDeliveryAgent()
extern "C" Q_DECL_EXPORT
QQuickDeliveryAgent *ritual_ZN17QQuickItemPrivate27ensureSubsceneDeliveryAgentEv(
    QQuickItemPrivate *self) {
  return self->ensureSubsceneDeliveryAgent();
}

//  void QQuickItemPrivate::deliverKeyEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate15deliverKeyEventEP9QKeyEvent(
    QQuickItemPrivate *self,
    QKeyEvent *a0) {
  self->deliverKeyEvent(a0);
}

//  bool QQuickItemPrivate::filterKeyEvent(QKeyEvent *a0, bool post)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate14filterKeyEventEP9QKeyEventb(
    QQuickItemPrivate *self,
    QKeyEvent *a0,
    bool post) {
  return self->filterKeyEvent(a0, post);
}

#if QT_CONFIG(im)
//  void QQuickItemPrivate::deliverInputMethodEvent(QInputMethodEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23deliverInputMethodEventEP17QInputMethodEvent(
    QQuickItemPrivate *self,
    QInputMethodEvent *a0) {
  self->deliverInputMethodEvent(a0);
}
#endif  // QT_CONFIG(im)

//  void QQuickItemPrivate::deliverShortcutOverrideEvent(QKeyEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate28deliverShortcutOverrideEventEP9QKeyEvent(
    QQuickItemPrivate *self,
    QKeyEvent *a0) {
  self->deliverShortcutOverrideEvent(a0);
}

//  void QQuickItemPrivate::deliverPointerEvent(QEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19deliverPointerEventEP6QEvent(
    QQuickItemPrivate *self,
    QEvent *a0) {
  self->deliverPointerEvent(a0);
}

//  bool QQuickItemPrivate::anyPointerHandlerWants(const QPointerEvent
//      *event, const QEventPoint &point) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate22anyPointerHandlerWantsEPK13QPointerEventRK11QEventPoint(
    const QQuickItemPrivate *self,
    const QPointerEvent *event,
    const QEventPoint *point) {
  return self->anyPointerHandlerWants(event, *point);
}

//  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
//      avoidGrabbers)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb(
    QQuickItemPrivate *self,
    QPointerEvent *a0,
    bool avoidGrabbers) {
  return self->handlePointerEvent(a0, avoidGrabbers);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickItemPrivate *self,
    QContextMenuEvent *event) {
  return self->handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickItemPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate10setVisibleEb(
    QQuickItemPrivate *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QQuickItemPrivate::isTransparentForPositioner() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate26isTransparentForPositionerEv(
    const QQuickItemPrivate *self) {
  return self->isTransparentForPositioner();
}

//  void QQuickItemPrivate::setTransparentForPositioner(bool trans)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate27setTransparentForPositionerEb(
    QQuickItemPrivate *self,
    bool trans) {
  self->setTransparentForPositioner(trans);
}

//  bool QQuickItemPrivate::calcEffectiveVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate20calcEffectiveVisibleEv(
    const QQuickItemPrivate *self) {
  return self->calcEffectiveVisible();
}

//  bool QQuickItemPrivate::setEffectiveVisibleRecur(bool a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QQuickItemPrivate24setEffectiveVisibleRecurEb(
    QQuickItemPrivate *self,
    bool a0) {
  return self->setEffectiveVisibleRecur(a0);
}

//  bool QQuickItemPrivate::calcEffectiveEnable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate19calcEffectiveEnableEv(
    const QQuickItemPrivate *self) {
  return self->calcEffectiveEnable();
}

//  void QQuickItemPrivate::setEffectiveEnableRecur(QQuickItem *scope, bool
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate23setEffectiveEnableRecurEP10QQuickItemb(
    QQuickItemPrivate *self,
    QQuickItem *scope,
    bool a1) {
  self->setEffectiveEnableRecur(scope, a1);
}

//  qreal QQuickItemPrivate::biggestPointerHandlerMargin() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK17QQuickItemPrivate27biggestPointerHandlerMarginEv(
    const QQuickItemPrivate *self) {
  return self->biggestPointerHandlerMargin();
}

//  QRectF QQuickItemPrivate::eventHandlingBounds(qreal margin) const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK17QQuickItemPrivate19eventHandlingBoundsEd(
    const QQuickItemPrivate *self,
    qreal margin) {
  return new QRectF(self->eventHandlingBounds(margin));
}

//  bool QQuickItemPrivate::parentFullyContains() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate19parentFullyContainsEv(
    const QQuickItemPrivate *self) {
  return self->parentFullyContains();
}

//  bool QQuickItemPrivate::effectivelyClipsEventHandlingChildren() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QQuickItemPrivate37effectivelyClipsEventHandlingChildrenEv(
    const QQuickItemPrivate *self) {
  return self->effectivelyClipsEventHandlingChildren();
}

//  QSGTransformNode *QQuickItemPrivate::itemNode()
extern "C" Q_DECL_EXPORT
QSGTransformNode *ritual_ZN17QQuickItemPrivate8itemNodeEv(
    QQuickItemPrivate *self) {
  return self->itemNode();
}

//  QSGNode *QQuickItemPrivate::childContainerNode()
extern "C" Q_DECL_EXPORT
QSGNode *ritual_ZN17QQuickItemPrivate18childContainerNodeEv(
    QQuickItemPrivate *self) {
  return self->childContainerNode();
}

//  QSGOpacityNode *QQuickItemPrivate::opacityNode() const
extern "C" Q_DECL_EXPORT
QSGOpacityNode *ritual_ZNK17QQuickItemPrivate11opacityNodeEv(
    const QQuickItemPrivate *self) {
  return self->opacityNode();
}

//  QQuickDefaultClipNode *QQuickItemPrivate::clipNode() const
extern "C" Q_DECL_EXPORT
QQuickDefaultClipNode *ritual_ZNK17QQuickItemPrivate8clipNodeEv(
    const QQuickItemPrivate *self) {
  return self->clipNode();
}

//  QSGRootNode *QQuickItemPrivate::rootNode() const
extern "C" Q_DECL_EXPORT
QSGRootNode *ritual_ZNK17QQuickItemPrivate8rootNodeEv(
    const QQuickItemPrivate *self) {
  return self->rootNode();
}

//  QSGTransformNode *QQuickItemPrivate::createTransformNode()
extern "C" Q_DECL_EXPORT
QSGTransformNode *ritual_ZN17QQuickItemPrivate19createTransformNodeEv(
    QQuickItemPrivate *self) {
  return self->createTransformNode();
}

//  void QQuickItemPrivate::refFromEffectItem(bool hide)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate17refFromEffectItemEb(
    QQuickItemPrivate *self,
    bool hide) {
  self->refFromEffectItem(hide);
}

//  void QQuickItemPrivate::recursiveRefFromEffectItem(int refs)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate26recursiveRefFromEffectItemEi(
    QQuickItemPrivate *self,
    int refs) {
  self->recursiveRefFromEffectItem(refs);
}

//  void QQuickItemPrivate::derefFromEffectItem(bool unhide)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19derefFromEffectItemEb(
    QQuickItemPrivate *self,
    bool unhide) {
  self->derefFromEffectItem(unhide);
}

//  void QQuickItemPrivate::itemChange(QQuickItem::ItemChange a0, const
//      QQuickItem::ItemChangeData &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate10itemChangeEN10QQuickItem10ItemChangeERKNS0_14ItemChangeDataE(
    QQuickItemPrivate *self,
    QQuickItem::ItemChange a0,
    const QQuickItem::ItemChangeData *a1) {
  self->itemChange(a0, *a1);
}

//  void
//      QQuickItemPrivate::enableSubtreeChangeNotificationsForParentHierachy(
//      )
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate49enableSubtreeChangeNotificationsForParentHierachyEv(
    QQuickItemPrivate *self) {
  self->enableSubtreeChangeNotificationsForParentHierachy();
}

//  void QQuickItemPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate12mirrorChangeEv(QQuickItemPrivate *self) {
  self->mirrorChange();
}

//  void QQuickItemPrivate::setHasCursorInChild(bool hasCursor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate19setHasCursorInChildEb(
    QQuickItemPrivate *self,
    bool hasCursor) {
  self->setHasCursorInChild(hasCursor);
}

//  void QQuickItemPrivate::setHasHoverInChild(bool hasHover)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate18setHasHoverInChildEb(
    QQuickItemPrivate *self,
    bool hasHover) {
  self->setHasHoverInChild(hasHover);
}

#if QT_CONFIG(cursor)
//  QCursor QQuickItemPrivate::effectiveCursor(const QQuickPointerHandler
//      *handler) const
extern "C" Q_DECL_EXPORT
QCursor *ritual_ZNK17QQuickItemPrivate15effectiveCursorEPK20QQuickPointerHandler(
    const QQuickItemPrivate *self,
    const QQuickPointerHandler *handler) {
  return new QCursor(self->effectiveCursor(handler));
}
#endif  // QT_CONFIG(cursor)

#if QT_CONFIG(cursor)
//  QQuickPointerHandler *QQuickItemPrivate::effectiveCursorHandler() const
extern "C" Q_DECL_EXPORT
QQuickPointerHandler *ritual_ZNK17QQuickItemPrivate22effectiveCursorHandlerEv(
    const QQuickItemPrivate *self) {
  return self->effectiveCursorHandler();
}
#endif  // QT_CONFIG(cursor)

//  void QQuickItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QQuickItemPrivate12updatePolishEv(QQuickItemPrivate *self) {
  self->updatePolish();
}

//  void QQuickItemPrivate::dumpItemTree(int indent) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QQuickItemPrivate12dumpItemTreeEi(
    const QQuickItemPrivate *self,
    int indent) {
  self->dumpItemTree(indent);
}

//  QLayoutPolicy QQuickItemPrivate::sizePolicy() const
extern "C" Q_DECL_EXPORT
QLayoutPolicy *ritual_ZNK17QQuickItemPrivate10sizePolicyEv(
    const QQuickItemPrivate *self) {
  return new QLayoutPolicy(self->sizePolicy());
}

//  a Python function taken by a CuteQQuickItemPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickItemPrivate(
    QQuickItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickItemPrivate *>(self)->take(key, call);
}

//  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler(
    QQuickItemPrivate *self,
    QQuickPointerHandler *h) {
  self->QQuickItemPrivate::addPointerHandler(h);
}

//  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler(
    QQuickItemPrivate *self,
    QQuickPointerHandler *h) {
  self->QQuickItemPrivate::removePointerHandler(h);
}

//  QtPrivate::QQuickAttachedPropertyPropagator
//      *QQuickItemPrivate::attachedPropertyPropagator_parent(const
//      QMetaObject *attachedType)
extern "C" Q_DECL_EXPORT
QtPrivate::QQuickAttachedPropertyPropagator *ritual_own_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject(
    QQuickItemPrivate *self,
    const QMetaObject *attachedType) {
  return self->QQuickItemPrivate::attachedPropertyPropagator_parent(
      attachedType);
}

//  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0, bool
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb(
    QQuickItemPrivate *self,
    QQuickItem *a0,
    bool a1) {
  self->QQuickItemPrivate::registerAsContainmentMask(a0, a1);
}

//  bool QQuickItemPrivate::setLastFocusChangeReason(Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE(
    QQuickItemPrivate *self,
    Qt::FocusReason reason) {
  return self->QQuickItemPrivate::setLastFocusChangeReason(reason);
}

//  qreal QQuickItemPrivate::getImplicitWidth() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickItemPrivate16getImplicitWidthEv(
    const QQuickItemPrivate *self) {
  return self->QQuickItemPrivate::getImplicitWidth();
}

//  qreal QQuickItemPrivate::getImplicitHeight() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK17QQuickItemPrivate17getImplicitHeightEv(
    const QQuickItemPrivate *self) {
  return self->QQuickItemPrivate::getImplicitHeight();
}

//  void QQuickItemPrivate::implicitWidthChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate20implicitWidthChangedEv(
    QQuickItemPrivate *self) {
  self->QQuickItemPrivate::implicitWidthChanged();
}

//  void QQuickItemPrivate::implicitHeightChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate21implicitHeightChangedEv(
    QQuickItemPrivate *self) {
  self->QQuickItemPrivate::implicitHeightChanged();
}

#if QT_CONFIG(accessibility)
//  QAccessible::Role QQuickItemPrivate::accessibleRole() const
extern "C" Q_DECL_EXPORT
QAccessible::Role ritual_own_ZNK17QQuickItemPrivate14accessibleRoleEv(
    const QQuickItemPrivate *self) {
  return self->QQuickItemPrivate::accessibleRole();
}
#endif  // QT_CONFIG(accessibility)

//  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem(
    QQuickItemPrivate *self,
    QQuickItem *transformedItem) {
  return self->QQuickItemPrivate::transformChanged(transformedItem);
}

//  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
//      avoidGrabbers)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb(
    QQuickItemPrivate *self,
    QPointerEvent *a0,
    bool avoidGrabbers) {
  return self->QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent(
    QQuickItemPrivate *self,
    QContextMenuEvent *event) {
  return self->QQuickItemPrivate::handleContextMenuEvent(event);
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  void QQuickItemPrivate::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate10setVisibleEb(
    QQuickItemPrivate *self,
    bool visible) {
  self->QQuickItemPrivate::setVisible(visible);
}

//  QSGTransformNode *QQuickItemPrivate::createTransformNode()
extern "C" Q_DECL_EXPORT
QSGTransformNode *ritual_own_ZN17QQuickItemPrivate19createTransformNodeEv(
    QQuickItemPrivate *self) {
  return self->QQuickItemPrivate::createTransformNode();
}

//  void QQuickItemPrivate::mirrorChange()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate12mirrorChangeEv(
    QQuickItemPrivate *self) {
  self->QQuickItemPrivate::mirrorChange();
}

//  void QQuickItemPrivate::updatePolish()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QQuickItemPrivate12updatePolishEv(
    QQuickItemPrivate *self) {
  self->QQuickItemPrivate::updatePolish();
}

//  void QQuickItemPrivate::dumpItemTree(int indent) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK17QQuickItemPrivate12dumpItemTreeEi(
    const QQuickItemPrivate *self,
    int indent) {
  self->QQuickItemPrivate::dumpItemTree(indent);
}
