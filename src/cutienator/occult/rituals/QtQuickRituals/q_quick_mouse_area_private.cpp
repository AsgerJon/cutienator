//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquickmousearea_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickmousearea_p.h>
#include <QtQuick/6.12.0/QtQuick/private/qquickmousearea_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qquickmousearea_p.h>
#include <QtQuick/private/qquickmousearea_p_p.h>
#include <QtQuick/qquickwindow.h>
#if QT_CONFIG(quick_draganddrop)
#include <QtQuick/private/qquickdrag_p.h>
#endif
#include <QtQml/private/qqmldata_p.h>
#include <QtQuick/private/qsgadaptationlayer_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qevent.h>
#include <QtGui/qstylehints.h>
#include <float.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 25, as _ZN22QQuickMouseAreaPrivateC1Ev
inline QQuickMouseAreaPrivate::QQuickMouseAreaPrivate()
: enabled(true), hoverEnabled(false), scrollGestureEnabled(true), hovered(false), longPress(false),
  moved(false), stealMouse(false), doubleClick(false), preventStealing(false),
  propagateComposedEvents(false), overThreshold(false),
  pressAndHoldInterval(-1)
#if QT_CONFIG(quick_draganddrop)
  , drag(nullptr)
#endif
#if QT_CONFIG(cursor)
  , cursor(nullptr)
#endif
{
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 39, as _ZN22QQuickMouseAreaPrivateD1Ev
inline QQuickMouseAreaPrivate::~QQuickMouseAreaPrivate()
{
#if QT_CONFIG(quick_draganddrop)
    delete drag;
#endif
#if QT_CONFIG(cursor)
    delete cursor;
#endif
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 60, as _ZN22QQuickMouseAreaPrivate9saveEventEP11QMouseEvent
inline void QQuickMouseAreaPrivate::saveEvent(QMouseEvent *event)
{
    lastPos = event->position();
    lastScenePos = event->scenePosition();
    lastButton = event->button();
    lastButtons = event->buttons();
    lastModifiers = event->modifiers();
    lastFlags = event->flags();
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 96, as _ZN22QQuickMouseAreaPrivate9propagateEP16QQuickMouseEventNS_13PropagateTypeE
inline void QQuickMouseAreaPrivate::propagate(QQuickMouseEvent* event, PropagateType t)
{
    Q_Q(QQuickMouseArea);
    if (!window || !propagateComposedEvents)
        return;
    QPointF scenePos = q->mapToScene(QPointF(event->x(), event->y()));
    propagateHelper(event, window->contentItem(), scenePos, t);
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 105, as _ZN22QQuickMouseAreaPrivate15propagateHelperEP16QQuickMouseEventP10QQuickItemRK7QPointFNS_13PropagateTypeE
inline bool QQuickMouseAreaPrivate::propagateHelper(QQuickMouseEvent *ev, QQuickItem *item,const QPointF &sp, PropagateType sig)
{
    //Based off of QQuickWindow::deliverInitialMousePressEvent
    //But specific to MouseArea, so doesn't belong in window
    Q_Q(const QQuickMouseArea);
    QQuickItemPrivate *itemPrivate = QQuickItemPrivate::get(item);

    if (itemPrivate->effectivelyClipsEventHandlingChildren()) {
        QPointF p = item->mapFromScene(sp);
        if (!item->contains(p))
            return false;
    }

    QList<QQuickItem *> children = itemPrivate->paintOrderChildItems();
    for (int ii = children.size() - 1; ii >= 0; --ii) {
        QQuickItem *child = children.at(ii);
        if (!child->isVisible() || !child->isEnabled())
            continue;
        if (propagateHelper(ev, child, sp, sig))
            return true;
    }

    QQuickMouseArea* ma = qobject_cast<QQuickMouseArea*>(item);
    if (ma && ma != q && ma->isEnabled() && itemPrivate->acceptedMouseButtons() & ev->button()) {
        switch (sig) {
        case Click:
            if (!ma->d_func()->isClickConnected())
                return false;
            break;
        case DoubleClick:
            if (!ma->d_func()->isDoubleClickConnected())
                return false;
            break;
        case PressAndHold:
            if (!ma->d_func()->isPressAndHoldConnected())
                return false;
            break;
        }
        QPointF p = item->mapFromScene(sp);
        if (item->contains(p)) {
            ev->setX(p.x());
            ev->setY(p.y());
            ev->setAccepted(true);//It is connected, they have to explicitly ignore to let it slide
            switch (sig) {
            case Click: emit ma->clicked(ev); break;
            case DoubleClick: emit ma->doubleClicked(ev); break;
            case PressAndHold: emit ma->pressAndHold(ev); break;
            }
            if (ev->isAccepted())
                return true;
        }
    }
    return false;

}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 70, as _ZN22QQuickMouseAreaPrivate23isPressAndHoldConnectedEv
inline bool QQuickMouseAreaPrivate::isPressAndHoldConnected()
{
    Q_Q(QQuickMouseArea);
    IS_SIGNAL_CONNECTED(q, QQuickMouseArea, pressAndHold, (QQuickMouseEvent *));
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 76, as _ZN22QQuickMouseAreaPrivate22isDoubleClickConnectedEv
inline bool QQuickMouseAreaPrivate::isDoubleClickConnected()
{
    Q_Q(QQuickMouseArea);
    IS_SIGNAL_CONNECTED(q, QQuickMouseArea, doubleClicked, (QQuickMouseEvent *));
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 82, as _ZN22QQuickMouseAreaPrivate16isClickConnectedEv
inline bool QQuickMouseAreaPrivate::isClickConnected()
{
    Q_Q(QQuickMouseArea);
    IS_SIGNAL_CONNECTED(q, QQuickMouseArea, clicked, (QQuickMouseEvent *));
}

//  from ../qtdeclarative/src/quick/items/qquickmousearea.cpp, line 89, as _ZN22QQuickMouseAreaPrivate16isWheelConnectedEv
#if QT_CONFIG(wheelevent)
inline bool QQuickMouseAreaPrivate::isWheelConnected()
{
    Q_Q(QQuickMouseArea);
    IS_SIGNAL_CONNECTED(q, QQuickMouseArea, wheel, (QQuickWheelEvent *));
}
#endif  // QT_CONFIG(wheelevent)
//  -----------------------------------------------------------------------

//  A QQuickMouseAreaPrivate that Python can take functions over in. Every QQuickMouseAreaPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickMouseAreaPrivateCall0)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall1)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickMouseAreaPrivateCall2)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall3)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickMouseAreaPrivateCall4)(const void *, int, int *);
typedef qreal (*CuteQQuickMouseAreaPrivateCall5)(const void *, int *);
typedef qreal (*CuteQQuickMouseAreaPrivateCall6)(const void *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall7)(const void *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickMouseAreaPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickMouseAreaPrivateCall10)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickMouseAreaPrivateCall11)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickMouseAreaPrivateCall12)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickMouseAreaPrivateCall13)(const void *, bool, int *);
typedef void * (*CuteQQuickMouseAreaPrivateCall14)(const void *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall15)(const void *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickMouseAreaPrivateCall17)(const void *, int, int *);
class CuteQQuickMouseAreaPrivate : public QQuickMouseAreaPrivate {
public:
  using QQuickMouseAreaPrivate::QQuickMouseAreaPrivate;
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
      CuteQQuickMouseAreaPrivateCall0 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall0>(taken[0]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall1 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall1>(taken[1]);
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
      CuteQQuickMouseAreaPrivateCall2 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall2>(taken[2]);
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
      CuteQQuickMouseAreaPrivateCall3 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall3>(taken[3]);
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
      CuteQQuickMouseAreaPrivateCall4 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall4>(taken[4]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall5 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall6 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall7 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall8 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall8>(taken[8]);
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
      CuteQQuickMouseAreaPrivateCall9 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall9>(taken[9]);
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
      CuteQQuickMouseAreaPrivateCall10 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall10>(taken[10]);
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
      CuteQQuickMouseAreaPrivateCall11 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall11>(taken[11]);
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
      CuteQQuickMouseAreaPrivateCall12 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall12>(taken[12]);
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
      CuteQQuickMouseAreaPrivateCall13 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall13>(taken[13]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall14 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall14>(taken[14]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall15 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall15>(taken[15]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall16 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall16>(taken[16]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickMouseAreaPrivateCall17 call = reinterpret_cast<CuteQQuickMouseAreaPrivateCall17>(taken[17]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickMouseArea *QQuickMouseAreaPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickMouseArea *ritual_ZN22QQuickMouseAreaPrivate6q_funcEv(
    QQuickMouseAreaPrivate *self) {
  return self->q_func();
}

//  const QQuickMouseArea *QQuickMouseAreaPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickMouseArea *ritual_ZNK22QQuickMouseAreaPrivate6q_funcEv(
    const QQuickMouseAreaPrivate *self) {
  return self->q_func();
}

//  QQuickMouseAreaPrivate::QQuickMouseAreaPrivate()
extern "C" Q_DECL_EXPORT
QQuickMouseAreaPrivate *ritual_ZN22QQuickMouseAreaPrivateC1Ev() {
  return new CuteQQuickMouseAreaPrivate();
}

//  QQuickMouseAreaPrivate::~QQuickMouseAreaPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickMouseAreaPrivateD1Ev(QQuickMouseAreaPrivate *self) {
  delete self;
}

//  void QQuickMouseAreaPrivate::saveEvent(QMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickMouseAreaPrivate9saveEventEP11QMouseEvent(
    QQuickMouseAreaPrivate *self,
    QMouseEvent *event) {
  self->saveEvent(event);
}

//  void QQuickMouseAreaPrivate::propagate(QQuickMouseEvent *event,
//      PropagateType a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QQuickMouseAreaPrivate9propagateEP16QQuickMouseEventNS_13PropagateTypeE(
    QQuickMouseAreaPrivate *self,
    QQuickMouseEvent *event,
    QQuickMouseAreaPrivate::PropagateType a1) {
  self->propagate(event, a1);
}

//  bool QQuickMouseAreaPrivate::propagateHelper(QQuickMouseEvent *a0,
//      QQuickItem *a1, const QPointF &a2, PropagateType a3)
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickMouseAreaPrivate15propagateHelperEP16QQuickMouseEventP10QQuickItemRK7QPointFNS_13PropagateTypeE(
    QQuickMouseAreaPrivate *self,
    QQuickMouseEvent *a0,
    QQuickItem *a1,
    const QPointF *a2,
    QQuickMouseAreaPrivate::PropagateType a3) {
  return self->propagateHelper(a0, a1, *a2, a3);
}

//  bool QQuickMouseAreaPrivate::isPressAndHoldConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickMouseAreaPrivate23isPressAndHoldConnectedEv(
    QQuickMouseAreaPrivate *self) {
  return self->isPressAndHoldConnected();
}

//  bool QQuickMouseAreaPrivate::isDoubleClickConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickMouseAreaPrivate22isDoubleClickConnectedEv(
    QQuickMouseAreaPrivate *self) {
  return self->isDoubleClickConnected();
}

//  bool QQuickMouseAreaPrivate::isClickConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickMouseAreaPrivate16isClickConnectedEv(
    QQuickMouseAreaPrivate *self) {
  return self->isClickConnected();
}

#if QT_CONFIG(wheelevent)
//  bool QQuickMouseAreaPrivate::isWheelConnected()
extern "C" Q_DECL_EXPORT
bool ritual_ZN22QQuickMouseAreaPrivate16isWheelConnectedEv(
    QQuickMouseAreaPrivate *self) {
  return self->isWheelConnected();
}
#endif  // QT_CONFIG(wheelevent)

//  a Python function taken by a CuteQQuickMouseAreaPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickMouseAreaPrivate(
    QQuickMouseAreaPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickMouseAreaPrivate *>(self)->take(key, call);
}
