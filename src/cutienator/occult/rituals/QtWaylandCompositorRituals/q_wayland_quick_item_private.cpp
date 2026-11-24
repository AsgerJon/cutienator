//  Written by dev_tooling.RitualGenerator from the records of QtWaylandCompo
//  sitor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qtwaylandcompositorglobal_p.h>
#include <QtWaylandCompositor/qwaylandquickitem.h>
#include <QtWaylandCompositor/QtWaylandCompositor>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWaylandCompositor/6.12.0/QtWaylandCompositor/private/qwaylandquickitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qwaylandquickitem.h"
#include "qwaylandquickitem_p.h"
#include "qwaylandquicksurface.h"
#include "qwaylandinputmethodcontrol.h"
#include "qwaylandtextinput.h"
#include "qwaylandtextinputv3.h"
#include "qwaylandqttextinputmethod.h"
#include "qwaylandquickoutput.h"
#include <QtWaylandCompositor/qwaylandcompositor.h>
#include <QtWaylandCompositor/qwaylandseat.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#if QT_CONFIG(draganddrop)
#include <QtWaylandCompositor/QWaylandDrag>
#endif
#include <QtWaylandCompositor/private/qwlclientbufferintegration_p.h>
#if QT_CONFIG(opengl)
#  include <QtOpenGL/QOpenGLTexture>
#  include <QtGui/QOpenGLFunctions>
#endif
#include <QtGui/QKeyEvent>
#include <QtGui/QGuiApplication>
#include <QtGui/QScreen>
#include <QtQuick/QSGSimpleTextureNode>
#include <QtQuick/QQuickWindow>
#include <QtQuick/qsgtexture.h>
#include <QtCore/QFile>
#include <QtCore/QMutexLocker>
#include <QtCore/QMutex>
#include <wayland-server-core.h>
#include <QThread>
#if QT_CONFIG(opengl)
#include <QtGui/private/qshaderdescription_p.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1700, as _ZN24QWaylandQuickItemPrivate5lowerEv
inline void QWaylandQuickItemPrivate::lower()
{
    Q_Q(QWaylandQuickItem);
    QQuickItem *parent = q->parentItem();
    Q_ASSERT(parent);
    QQuickItem *bottom = parent->childItems().constFirst();
    if (q != bottom)
        q->stackBefore(bottom);
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1716, as _ZN24QWaylandQuickItemPrivate5raiseEv
inline void QWaylandQuickItemPrivate::raise()
{
    Q_Q(QWaylandQuickItem);
    QQuickItem *parent = q->parentItem();
    Q_ASSERT(parent);
    QQuickItem *top = parent->childItems().constLast();
    if (q != top)
        q->stackAfter(top);
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 467, as _ZN24QWaylandQuickItemPrivate15handleDragEndedEP12QWaylandSeat
inline void QWaylandQuickItemPrivate::handleDragEnded(QWaylandSeat *seat)
{
#if QT_CONFIG(draganddrop)
    isDragging = false;
    seat->drag()->drop();
#else
    Q_UNUSED(seat);
#endif // QT_CONFIG(draganddrop)
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 448, as _ZN24QWaylandQuickItemPrivate16handleDragUpdateEP12QWaylandSeatRK7QPointF
inline void QWaylandQuickItemPrivate::handleDragUpdate(QWaylandSeat *seat, const QPointF &globalPosition)
{
#if QT_CONFIG(draganddrop)
    Q_Q(QWaylandQuickItem);
    QWaylandQuickOutput *currentOutput = qobject_cast<QWaylandQuickOutput *>(q->view()->output());
    //TODO: also check if dragging onto other outputs
    QWaylandQuickItem *targetItem = qobject_cast<QWaylandQuickItem *>(currentOutput->pickClickableItem(q->mapToScene(globalPosition)));
    QWaylandSurface *targetSurface = targetItem ? targetItem->surface() : nullptr;
    if (targetSurface) {
        QPointF position = q->mapToItem(targetItem, globalPosition);
        QPointF surfacePosition = targetItem->mapToSurface(position);
        seat->drag()->dragMove(targetSurface, surfacePosition);
    }
#else
    Q_UNUSED(seat);
    Q_UNUSED(globalPosition);
#endif // QT_CONFIG(draganddrop)
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1760, as _ZNK24QWaylandQuickItemPrivate11scaleFactorEv
inline qreal QWaylandQuickItemPrivate::scaleFactor() const
{
    qreal f = view->output() ? view->output()->scaleFactor() : 1;
#if !defined(Q_OS_MACOS)
    if (window)
        f /= window->devicePixelRatio();
#endif
    return f;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1770, as _ZNK24QWaylandQuickItemPrivate11findSiblingEP15QWaylandSurface
inline QWaylandQuickItem *QWaylandQuickItemPrivate::findSibling(QWaylandSurface *surface) const
{
    Q_Q(const QWaylandQuickItem);
    auto *parent = q->parentItem();
    if (!parent)
        return nullptr;

    const auto siblings = q->parentItem()->childItems();
    for (auto *sibling : siblings) {
        auto *waylandItem = qobject_cast<QWaylandQuickItem *>(sibling);
        if (waylandItem && waylandItem->surface() == surface)
            return waylandItem;
    }
    return nullptr;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1786, as _ZN24QWaylandQuickItemPrivate17placeAboveSiblingEP17QWaylandQuickItem
inline void QWaylandQuickItemPrivate::placeAboveSibling(QWaylandQuickItem *sibling)
{
    Q_Q(QWaylandQuickItem);
    q->stackAfter(sibling);
    q->setZ(sibling->z());
    belowParent = sibling->d_func()->belowParent;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1794, as _ZN24QWaylandQuickItemPrivate17placeBelowSiblingEP17QWaylandQuickItem
inline void QWaylandQuickItemPrivate::placeBelowSibling(QWaylandQuickItem *sibling)
{
    Q_Q(QWaylandQuickItem);
    q->stackBefore(sibling);
    q->setZ(sibling->z());
    belowParent = sibling->d_func()->belowParent;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1803, as _ZN24QWaylandQuickItemPrivate16placeAboveParentEv
inline void QWaylandQuickItemPrivate::placeAboveParent()
{
    Q_Q(QWaylandQuickItem);
    const auto siblings = q->parentItem()->childItems();

    // Stack below first (bottom) sibling above parent
    bool foundSibling = false;
    for (auto it = siblings.cbegin(); it != siblings.cend(); ++it) {
        QWaylandQuickItem *sibling = qobject_cast<QWaylandQuickItem*>(*it);
        if (sibling && !sibling->d_func()->belowParent) {
            q->stackBefore(sibling);
            foundSibling = true;
            break;
        }
    }

    // No other subsurfaces above parent
    if (!foundSibling && siblings.last() != q)
        q->stackAfter(siblings.last());

    q->setZ(q->parentItem()->z());
    belowParent = false;
}

//  from ../qtwayland/src/compositor/compositor_api/qwaylandquickitem.cpp, line 1828, as _ZN24QWaylandQuickItemPrivate16placeBelowParentEv
inline void QWaylandQuickItemPrivate::placeBelowParent()
{
    Q_Q(QWaylandQuickItem);
    const auto siblings = q->parentItem()->childItems();

    // Stack above last (top) sibling below parent
    bool foundSibling = false;
    for (auto it = siblings.crbegin(); it != siblings.crend(); ++it) {
        QWaylandQuickItem *sibling = qobject_cast<QWaylandQuickItem*>(*it);
        if (sibling && sibling->d_func()->belowParent) {
            q->stackAfter(sibling);
            foundSibling = true;
            break;
        }
    }

    // No other subsurfaces below parent
    if (!foundSibling && siblings.first() != q)
        q->stackBefore(siblings.first());

    q->setZ(q->parentItem()->z() - 1.0);
    belowParent = true;
}
//  -----------------------------------------------------------------------

//  A QWaylandQuickItemPrivate that Python can take functions over in. Every QWaylandQuickItemPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandQuickItemPrivateCall0)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall1)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQWaylandQuickItemPrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQWaylandQuickItemPrivateCall6)(const void *, int, int *);
typedef qreal (*CuteQWaylandQuickItemPrivateCall7)(const void *, int *);
typedef qreal (*CuteQWaylandQuickItemPrivateCall8)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall9)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQWaylandQuickItemPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQWaylandQuickItemPrivateCall12)(const void *, QQuickItem *, int *);
typedef bool (*CuteQWaylandQuickItemPrivateCall13)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQWaylandQuickItemPrivateCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQWaylandQuickItemPrivateCall15)(const void *, bool, int *);
typedef void * (*CuteQWaylandQuickItemPrivateCall16)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall17)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall18)(const void *, int *);
typedef void (*CuteQWaylandQuickItemPrivateCall19)(const void *, int, int *);
class CuteQWaylandQuickItemPrivate : public QWaylandQuickItemPrivate {
public:
  using QWaylandQuickItemPrivate::QWaylandQuickItemPrivate;
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

  //  void QWaylandQuickItemPrivate::raise()
  void raise() override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall0 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall0>(taken[0]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickItemPrivate::raise();
  }

  //  void QWaylandQuickItemPrivate::lower()
  void lower() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall1 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall1>(taken[1]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandQuickItemPrivate::lower();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall2 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall3 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall3>(taken[3]);
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
      CuteQWaylandQuickItemPrivateCall4 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall4>(taken[4]);
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
      CuteQWaylandQuickItemPrivateCall5 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall5>(taken[5]);
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
      CuteQWaylandQuickItemPrivateCall6 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall7 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall8 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall9 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall10 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall10>(taken[10]);
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
      CuteQWaylandQuickItemPrivateCall11 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall11>(taken[11]);
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
      CuteQWaylandQuickItemPrivateCall12 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall12>(taken[12]);
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
      CuteQWaylandQuickItemPrivateCall13 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall13>(taken[13]);
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
      CuteQWaylandQuickItemPrivateCall14 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall14>(taken[14]);
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
      CuteQWaylandQuickItemPrivateCall15 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall16 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[17]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall17 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[18]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall18 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQWaylandQuickItemPrivateCall19 call = reinterpret_cast<CuteQWaylandQuickItemPrivateCall19>(taken[19]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QWaylandQuickItem *QWaylandQuickItemPrivate::q_func()
extern "C" Q_DECL_EXPORT
QWaylandQuickItem *ritual_ZN24QWaylandQuickItemPrivate6q_funcEv(
    QWaylandQuickItemPrivate *self) {
  return self->q_func();
}

//  const QWaylandQuickItem *QWaylandQuickItemPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QWaylandQuickItem *ritual_ZNK24QWaylandQuickItemPrivate6q_funcEv(
    const QWaylandQuickItemPrivate *self) {
  return self->q_func();
}

//  const QWaylandQuickItemPrivate *QWaylandQuickItemPrivate::get(const
//      QWaylandQuickItem *item)
extern "C" Q_DECL_EXPORT
const QWaylandQuickItemPrivate *ritual_ZN24QWaylandQuickItemPrivate3getEPK17QWaylandQuickItem(
    const QWaylandQuickItem *item) {
  return QWaylandQuickItemPrivate::get(item);
}

//  void QWaylandQuickItemPrivate::setInputEventsEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate21setInputEventsEnabledEb(
    QWaylandQuickItemPrivate *self,
    bool enable) {
  self->setInputEventsEnabled(enable);
}

//  void QWaylandQuickItemPrivate::handleDragEnded(QWaylandSeat *seat)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate15handleDragEndedEP12QWaylandSeat(
    QWaylandQuickItemPrivate *self,
    QWaylandSeat *seat) {
  self->handleDragEnded(seat);
}

//  void QWaylandQuickItemPrivate::handleDragUpdate(QWaylandSeat *seat, const
//      QPointF &globalPosition)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate16handleDragUpdateEP12QWaylandSeatRK7QPointF(
    QWaylandQuickItemPrivate *self,
    QWaylandSeat *seat,
    const QPointF *globalPosition) {
  self->handleDragUpdate(seat, *globalPosition);
}

//  bool QWaylandQuickItemPrivate::shouldSendInputEvents() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QWaylandQuickItemPrivate21shouldSendInputEventsEv(
    const QWaylandQuickItemPrivate *self) {
  return self->shouldSendInputEvents();
}

//  qreal QWaylandQuickItemPrivate::scaleFactor() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK24QWaylandQuickItemPrivate11scaleFactorEv(
    const QWaylandQuickItemPrivate *self) {
  return self->scaleFactor();
}

//  QWaylandQuickItem *QWaylandQuickItemPrivate::findSibling(QWaylandSurface
//      *surface) const
extern "C" Q_DECL_EXPORT
QWaylandQuickItem *ritual_ZNK24QWaylandQuickItemPrivate11findSiblingEP15QWaylandSurface(
    const QWaylandQuickItemPrivate *self,
    QWaylandSurface *surface) {
  return self->findSibling(surface);
}

//  void QWaylandQuickItemPrivate::placeAboveSibling(QWaylandQuickItem
//      *sibling)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate17placeAboveSiblingEP17QWaylandQuickItem(
    QWaylandQuickItemPrivate *self,
    QWaylandQuickItem *sibling) {
  self->placeAboveSibling(sibling);
}

//  void QWaylandQuickItemPrivate::placeBelowSibling(QWaylandQuickItem
//      *sibling)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate17placeBelowSiblingEP17QWaylandQuickItem(
    QWaylandQuickItemPrivate *self,
    QWaylandQuickItem *sibling) {
  self->placeBelowSibling(sibling);
}

//  void QWaylandQuickItemPrivate::placeAboveParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate16placeAboveParentEv(
    QWaylandQuickItemPrivate *self) {
  self->placeAboveParent();
}

//  void QWaylandQuickItemPrivate::placeBelowParent()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate16placeBelowParentEv(
    QWaylandQuickItemPrivate *self) {
  self->placeBelowParent();
}

//  void QWaylandQuickItemPrivate::raise()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate5raiseEv(
    QWaylandQuickItemPrivate *self) {
  self->raise();
}

//  void QWaylandQuickItemPrivate::lower()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QWaylandQuickItemPrivate5lowerEv(
    QWaylandQuickItemPrivate *self) {
  self->lower();
}

//  a Python function taken by a CuteQWaylandQuickItemPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandQuickItemPrivate(
    QWaylandQuickItemPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandQuickItemPrivate *>(self)->take(key, call);
}

//  void QWaylandQuickItemPrivate::raise()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandQuickItemPrivate5raiseEv(
    QWaylandQuickItemPrivate *self) {
  self->QWaylandQuickItemPrivate::raise();
}

//  void QWaylandQuickItemPrivate::lower()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QWaylandQuickItemPrivate5lowerEv(
    QWaylandQuickItemPrivate *self) {
  self->QWaylandQuickItemPrivate::lower();
}

#endif  // QT_CONFIG(wayland_compositor_quick)
