//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickoverlay_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickpopup_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickcontrol_p_p.h>
#include <QtQuickTemplates2/private/qquickoverlay_p.h>
#include <QtQuickTemplates2/private/qquickoverlay_p_p.h>
#include <QtQuickTemplates2/private/qquickpopupitem_p_p.h>
#include <QtQuickTemplates2/private/qquickpopup_p_p.h>
#include <QtQuickTemplates2/private/qquickdrawer_p.h>
#include <QtQuickTemplates2/private/qquickdrawer_p_p.h>
#include <QtQuickTemplates2/private/qquickapplicationwindow_p.h>
#include <QtGui/qpainterpath.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlproperty.h>
#include <QtQml/qqmlcomponent.h>
#if QT_CONFIG(quick_shadereffect)
#include <QtQuick/private/qquickshadereffectsource_p.h>
#endif
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 190, as local:qquickoverlay.cpp:canCascadeCloseOnOutsidePress
static bool canCascadeCloseOnOutsidePress(const QQuickPopup *popup)
{
    static const QQuickPopup::ClosePolicy outsideFlags = QQuickPopup::CloseOnPressOutside
            | QQuickPopup::CloseOnReleaseOutside
            | QQuickPopup::CloseOnPressOutsideParent
            | QQuickPopup::CloseOnReleaseOutsideParent;
    return popup->closePolicy().testAnyFlags(outsideFlags);
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 208, as local:qquickoverlay.cpp:closedItselfViaCloseMultiple
static bool closedItselfViaCloseMultiple(const QQuickPopup *popup, bool wasOpened)
{
    return wasOpened && !popup->isOpened() && canCascadeCloseOnOutsidePress(popup)
            && popup->closePolicy().testFlag(QQuickPopup::CloseMultiple);
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 276, as _ZN20QQuickOverlayPrivate13handleReleaseEP10QQuickItemP6QEventP11QQuickPopup
inline bool QQuickOverlayPrivate::handleRelease(QQuickItem *source, QEvent *event, QQuickPopup *target)
{
    if (target) {
        const bool wasOpened = target->isOpened();
        setMouseGrabberPopup(nullptr);
        if (target->overlayEvent(source, event)) {
            setMouseGrabberPopup(nullptr);
            if (!closedItselfViaCloseMultiple(target, wasOpened))
                return true;
        }
    } else if (!closeCascadeStopped) {
        const auto popups = stackingOrderPopups();
        for (QQuickPopup *popup : popups) {
            if (popup->overlayEvent(source, event))
                return true;
            if (!canCascadeCloseOnOutsidePress(popup))
                continue;
            if (!popup->closePolicy().testFlag(QQuickPopup::CloseMultiple)) {
                closeCascadeStopped = true;
                break;
            }
        }
    }
    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 69, as _ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF
inline void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem *, QQuickGeometryChange, const QRectF &)
{
    updateGeometry();
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 74, as _ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem
inline void QQuickOverlayPrivate::itemRotationChanged(QQuickItem *)
{
    updateGeometry();
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 83, as _ZN20QQuickOverlayPrivate24eatEventIfBlockedByModalEP13QPointerEvent
#if QT_CONFIG(tabletevent) || QT_CONFIG(wheelevent)
inline bool QQuickOverlayPrivate::eatEventIfBlockedByModal(QPointerEvent *event)
{
    Q_Q(QQuickOverlay);
    const QList<QQuickItem *> targetItems = deliveryAgentPrivate()->pointerTargets(
            window->contentItem(), event, event->point(0), false, false);
    if (targetItems.isEmpty())
        return false;

    QQuickItem *const topItem = targetItems.first();
    QQuickItem *const dimmerItem = q->property("_q_dimmerItem").value<QQuickItem *>();
    // Find the QQuickPopupItem that contains topItem, if any.
    QQuickItem *item = qobject_cast<QQuickPopupItem *>(topItem) ? topItem : nullptr;

    if (!item) {
        item = topItem;
        while ((item = item->parentItem())) {
            if (qobject_cast<QQuickPopupItem *>(item))
                break;
        }
    }

#if QT_CONFIG(quick_shadereffect)
    // topItem may be a QQuickShaderEffectSource created for a popup's drop shadow layer.
    // It is a direct child of the overlay (not of the popup item), so the parent walk above
    // misses it. Resolve it to the popup item it renders so the loop below handles it correctly.
    if (!item && dimmerItem != topItem && q->isAncestorOf(topItem)) {
        if (auto *shaderEffect = qobject_cast<QQuickShaderEffectSource *>(topItem)) {
            if (auto *pi = qobject_cast<QQuickPopupItem *>(shaderEffect->sourceItem()))
                item = pi;
        }
        if (!item)
            return false;
    }
#endif

    // Iterate popups front-to-back. Block the event if topItem is not inside a popup
    // that sits above the first modal popup in stacking order.
    for (const auto &popup : stackingOrderPopups()) {
        const QQuickItem *popupItem = popup->popupItem();
        if (!popupItem)
            continue;
        if (popupItem == item) {
            if (topItem != item && popup->isModal()
                && !item->contains(item->mapFromScene(event->point(0).scenePosition()))) {
                // topItem is the popup's shader effect source (drop shadow), not the popup item
                // itself — the event landed in the shadow area outside the popup's bounds.
                // Eat it for modal popups to prevent it reaching items behind the shadow.
                event->accept();
                return true;
            }
            // The event landed inside the popup. Tablet events must be filtered here
            // because, unlike wheel and mouse events, no standard item
            // accepts tablet events — so the delivery agent would otherwise continue
            // past the popup to a TapHandler behind it.
            // Intentionally not calling event->accept() so Qt synthesizes a mouse event,
            // which the overlay's mouse press handler delivers to popup content normally.
#if QT_CONFIG(tabletevent)
            if (QQuickDeliveryAgentPrivate::isTabletEvent(event))
                return true;
#endif
            break;
        }
        // topItem is outside this popup — let the popup decide whether to block.
        if (popup->overlayEvent(topItem, event))
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(tabletevent) || QT_CONFIG(wheelevent)

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 153, as _ZN20QQuickOverlayPrivate9startDragEP6QEventRK7QPointF
inline bool QQuickOverlayPrivate::startDrag(QEvent *event, const QPointF &pos)
{
    Q_Q(QQuickOverlay);
    if (allDrawers.isEmpty())
        return false;

    // don't start dragging a drawer if a modal popup overlay is blocking (QTBUG-60602)
    QQuickItem *item = q->childAt(pos.x(), pos.y());
    if (item) {
        const auto popups = stackingOrderPopups();
        for (QQuickPopup *popup : popups) {
            QQuickPopupPrivate *p = QQuickPopupPrivate::get(popup);
            if (p->dimmer == item && popup->isVisible() && popup->isModal())
                return false;
        }
    }

    const QList<QQuickPopup *> drawers = stackingOrderDrawers();
    for (QQuickPopup *popup : drawers) {
        QQuickDrawer *drawer = qobject_cast<QQuickDrawer *>(popup);
        Q_ASSERT(drawer);
        QQuickDrawerPrivate *p = QQuickDrawerPrivate::get(drawer);
        if (p->startDrag(event)) {
            setMouseGrabberPopup(drawer);
            return true;
        }
    }

    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 214, as _ZN20QQuickOverlayPrivate11handlePressEP10QQuickItemP6QEventP11QQuickPopup
inline bool QQuickOverlayPrivate::handlePress(QQuickItem *source, QEvent *event, QQuickPopup *target)
{
    if (target) {
        const bool wasOpened = target->isOpened();
        if (target->overlayEvent(source, event)) {
            if (closedItselfViaCloseMultiple(target, wasOpened))
                return false;
            setMouseGrabberPopup(target);
            return true;
        }
        return false;
    }

    switch (event->type()) {
    default: {
        if (mouseGrabberPopup)
            break;
#if QT_CONFIG(quicktemplates2_multitouch)
        Q_FALLTHROUGH();
    case QEvent::TouchBegin:
    case QEvent::TouchUpdate:
    case QEvent::TouchEnd:
#endif
        // allow non-modal popups to close themselves,
        // and non-dimming modal popups to block the event
        if (closeCascadeStopped)
            break;
        const auto popups = stackingOrderPopups();
        bool passedWithCloseMultiple = false;
        for (QQuickPopup *popup : popups) {
            if (popup->overlayEvent(source, event)) {
                // Don't grab a deeper popup as the mouse grabber when we've
                // already iterated past a higher popup via CloseMultiple. The
                // release loop's CloseMultiple logic will handle closing the
                // higher popup correctly without a grabbed target.
                if (!passedWithCloseMultiple)
                    setMouseGrabberPopup(popup);
                return true;
            }
            if (!canCascadeCloseOnOutsidePress(popup))
                continue;
            if (!popup->closePolicy().testFlag(QQuickPopup::CloseMultiple)) {
                closeCascadeStopped = true;
                break;
            }
            passedWithCloseMultiple = true;
        }
        break;
    }
    }

    event->ignore();
    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 269, as _ZN20QQuickOverlayPrivate10handleMoveEP10QQuickItemP6QEventP11QQuickPopup
inline bool QQuickOverlayPrivate::handleMove(QQuickItem *source, QEvent *event, QQuickPopup *target)
{
    if (target)
        return target->overlayEvent(source, event);
    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 302, as _ZN20QQuickOverlayPrivate16handleMouseEventEP10QQuickItemP11QMouseEventP11QQuickPopup
inline bool QQuickOverlayPrivate::handleMouseEvent(QQuickItem *source, QMouseEvent *event, QQuickPopup *target)
{
    switch (event->type()) {
    case QEvent::MouseButtonPress:
        if (!target && startDrag(event, event->scenePosition()))
            return true;
        return handlePress(source, event, target);
    case QEvent::MouseMove:
        return handleMove(source, event, target ? target : mouseGrabberPopup.data());
    case QEvent::MouseButtonRelease:
        return handleRelease(source, event, target ? target : mouseGrabberPopup.data());
    default:
        break;
    }
    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 319, as _ZN20QQuickOverlayPrivate16handleHoverEventEP10QQuickItemP11QHoverEventP11QQuickPopup
inline bool QQuickOverlayPrivate::handleHoverEvent(QQuickItem *source, QHoverEvent *event, QQuickPopup *target)
{
    switch (event->type()) {
    case QEvent::HoverEnter:
    case QEvent::HoverMove:
    case QEvent::HoverLeave:
        if (target)
            return target->overlayEvent(source, event);
        return false;
    default:
        Q_UNREACHABLE(); // function must only be called on hover events
        break;
    }
    return false;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 336, as _ZN20QQuickOverlayPrivate16handleTouchEventEP10QQuickItemP11QTouchEventP11QQuickPopup
#if QT_CONFIG(quicktemplates2_multitouch)
inline bool QQuickOverlayPrivate::handleTouchEvent(QQuickItem *source, QTouchEvent *event, QQuickPopup *target)
{
    bool handled = false;
    switch (event->type()) {
    case QEvent::TouchBegin:
    case QEvent::TouchUpdate:
    case QEvent::TouchEnd:
        for (const QTouchEvent::TouchPoint &point : event->points()) {
            switch (point.state()) {
            case QEventPoint::Pressed:
                if (!target && startDrag(event, point.scenePosition()))
                    handled = true;
                else
                    handled |= handlePress(source, event, target);
                break;
            case QEventPoint::Updated:
                handled |= handleMove(source, event, target ? target : mouseGrabberPopup.data());
                break;
            case QEventPoint::Released:
                handled |= handleRelease(source, event, target ? target : mouseGrabberPopup.data());
                break;
            default:
                break;
            }
        }
        break;

    default:
        break;
    }

    return handled;
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 371, as _ZN20QQuickOverlayPrivate8addPopupEP11QQuickPopup
inline void QQuickOverlayPrivate::addPopup(QQuickPopup *popup)
{
    Q_Q(QQuickOverlay);
    allPopups += popup;
    if (QQuickDrawer *drawer = qobject_cast<QQuickDrawer *>(popup)) {
        allDrawers += drawer;
        q->setVisible(!allDrawers.isEmpty() || !q->childItems().isEmpty());
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 381, as _ZN20QQuickOverlayPrivate11removePopupEP11QQuickPopup
inline void QQuickOverlayPrivate::removePopup(QQuickPopup *popup)
{
    Q_Q(QQuickOverlay);
    allPopups.removeOne(popup);
    if (allDrawers.removeOne(popup))
        q->setVisible(!allDrawers.isEmpty() || !q->childItems().isEmpty());
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 389, as _ZN20QQuickOverlayPrivate20setMouseGrabberPopupEP11QQuickPopup
inline void QQuickOverlayPrivate::setMouseGrabberPopup(QQuickPopup *popup)
{
    if (popup && !popup->isVisible())
        popup = nullptr;
    mouseGrabberPopup = popup;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 44, as _ZNK20QQuickOverlayPrivate19stackingOrderPopupsEv
inline QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderPopups() const
{
    const QList<QQuickItem *> children = paintOrderChildItems();

    QList<QQuickPopup *> popups;
    popups.reserve(children.size());

    for (auto it = children.crbegin(), end = children.crend(); it != end; ++it) {
        QQuickPopup *popup = qobject_cast<QQuickPopup *>((*it)->parent());
        if (popup)
            popups += popup;
    }

    return popups;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 60, as _ZNK20QQuickOverlayPrivate20stackingOrderDrawersEv
inline QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderDrawers() const
{
    QList<QQuickPopup *> sorted(allDrawers);
    std::sort(sorted.begin(), sorted.end(), [](const QQuickPopup *one, const QQuickPopup *another) {
        return one->z() > another->z();
    });
    return sorted;
}

//  from ../qtdeclarative/src/quicktemplates/qquickoverlay.cpp, line 396, as _ZN20QQuickOverlayPrivate14updateGeometryEv
inline void QQuickOverlayPrivate::updateGeometry()
{
    Q_Q(QQuickOverlay);
    if (!window || !window->contentItem())
        return;

    const QSizeF size = window->contentItem()->size();
    const QPointF pos(-(size.width() - window->size().width()) / 2,
                      -(size.height() - window->size().height()) / 2);

    q->setSize(size);
    q->setPosition(pos);
}
//  -----------------------------------------------------------------------

//  A QQuickOverlayPrivate that Python can take functions over in. Every QQuickOverlayPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQQuickOverlayPrivateCall0)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickOverlayPrivateCall1)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickOverlayPrivateCall2)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickOverlayPrivateCall3)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickOverlayPrivateCall4)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickOverlayPrivateCall5)(const void *, QQuickItem *, bool, int *);
typedef bool (*CuteQQuickOverlayPrivateCall6)(const void *, int, int *);
typedef qreal (*CuteQQuickOverlayPrivateCall7)(const void *, int *);
typedef qreal (*CuteQQuickOverlayPrivateCall8)(const void *, int *);
typedef void (*CuteQQuickOverlayPrivateCall9)(const void *, int *);
typedef void (*CuteQQuickOverlayPrivateCall10)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickOverlayPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef bool (*CuteQQuickOverlayPrivateCall12)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickOverlayPrivateCall13)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickOverlayPrivateCall14)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickOverlayPrivateCall15)(const void *, bool, int *);
typedef void * (*CuteQQuickOverlayPrivateCall16)(const void *, int *);
typedef void (*CuteQQuickOverlayPrivateCall17)(const void *, int *);
typedef void (*CuteQQuickOverlayPrivateCall18)(const void *, int *);
typedef void (*CuteQQuickOverlayPrivateCall19)(const void *, int, int *);
class CuteQQuickOverlayPrivate : public QQuickOverlayPrivate {
public:
  using QQuickOverlayPrivate::QQuickOverlayPrivate;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem")) {
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

  //  void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall0 call = reinterpret_cast<CuteQQuickOverlayPrivateCall0>(taken[0]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickOverlayPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickOverlayPrivate::itemRotationChanged(QQuickItem *item)
  void itemRotationChanged(QQuickItem *item) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall1 call = reinterpret_cast<CuteQQuickOverlayPrivateCall1>(taken[1]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickOverlayPrivate::itemRotationChanged(item);
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall2 call = reinterpret_cast<CuteQQuickOverlayPrivateCall2>(taken[2]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall3 call = reinterpret_cast<CuteQQuickOverlayPrivateCall3>(taken[3]);
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
      CuteQQuickOverlayPrivateCall4 call = reinterpret_cast<CuteQQuickOverlayPrivateCall4>(taken[4]);
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
      CuteQQuickOverlayPrivateCall5 call = reinterpret_cast<CuteQQuickOverlayPrivateCall5>(taken[5]);
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
      CuteQQuickOverlayPrivateCall6 call = reinterpret_cast<CuteQQuickOverlayPrivateCall6>(taken[6]);
      bool given = call(this, static_cast<int>(reason), &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::setLastFocusChangeReason(reason);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall7 call = reinterpret_cast<CuteQQuickOverlayPrivateCall7>(taken[7]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall8 call = reinterpret_cast<CuteQQuickOverlayPrivateCall8>(taken[8]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall9 call = reinterpret_cast<CuteQQuickOverlayPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall10 call = reinterpret_cast<CuteQQuickOverlayPrivateCall10>(taken[10]);
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
      CuteQQuickOverlayPrivateCall11 call = reinterpret_cast<CuteQQuickOverlayPrivateCall11>(taken[11]);
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
      CuteQQuickOverlayPrivateCall12 call = reinterpret_cast<CuteQQuickOverlayPrivateCall12>(taken[12]);
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
      CuteQQuickOverlayPrivateCall13 call = reinterpret_cast<CuteQQuickOverlayPrivateCall13>(taken[13]);
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
      CuteQQuickOverlayPrivateCall14 call = reinterpret_cast<CuteQQuickOverlayPrivateCall14>(taken[14]);
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
      CuteQQuickOverlayPrivateCall15 call = reinterpret_cast<CuteQQuickOverlayPrivateCall15>(taken[15]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall16 call = reinterpret_cast<CuteQQuickOverlayPrivateCall16>(taken[16]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall17 call = reinterpret_cast<CuteQQuickOverlayPrivateCall17>(taken[17]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::mirrorChange();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall18 call = reinterpret_cast<CuteQQuickOverlayPrivateCall18>(taken[18]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickOverlayPrivateCall19 call = reinterpret_cast<CuteQQuickOverlayPrivateCall19>(taken[19]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickOverlay *QQuickOverlayPrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickOverlay *ritual_ZN20QQuickOverlayPrivate6q_funcEv(
    QQuickOverlayPrivate *self) {
  return self->q_func();
}

//  const QQuickOverlay *QQuickOverlayPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QQuickOverlay *ritual_ZNK20QQuickOverlayPrivate6q_funcEv(
    const QQuickOverlayPrivate *self) {
  return self->q_func();
}

//  QQuickOverlayPrivate *QQuickOverlayPrivate::get(QQuickOverlay *overlay)
extern "C" Q_DECL_EXPORT
QQuickOverlayPrivate *ritual_ZN20QQuickOverlayPrivate3getEP13QQuickOverlay(
    QQuickOverlay *overlay) {
  return QQuickOverlayPrivate::get(overlay);
}

#if QT_CONFIG(tabletevent) || QT_CONFIG(wheelevent)
//  bool QQuickOverlayPrivate::eatEventIfBlockedByModal(QPointerEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate24eatEventIfBlockedByModalEP13QPointerEvent(
    QQuickOverlayPrivate *self,
    QPointerEvent *event) {
  return self->eatEventIfBlockedByModal(event);
}
#endif  // QT_CONFIG(tabletevent) || QT_CONFIG(wheelevent)

//  bool QQuickOverlayPrivate::startDrag(QEvent *event, const QPointF &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate9startDragEP6QEventRK7QPointF(
    QQuickOverlayPrivate *self,
    QEvent *event,
    const QPointF *pos) {
  return self->startDrag(event, *pos);
}

//  bool QQuickOverlayPrivate::handlePress(QQuickItem *source, QEvent *event,
//      QQuickPopup *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate11handlePressEP10QQuickItemP6QEventP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickItem *source,
    QEvent *event,
    QQuickPopup *target) {
  return self->handlePress(source, event, target);
}

//  bool QQuickOverlayPrivate::handleMove(QQuickItem *source, QEvent *event,
//      QQuickPopup *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate10handleMoveEP10QQuickItemP6QEventP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickItem *source,
    QEvent *event,
    QQuickPopup *target) {
  return self->handleMove(source, event, target);
}

//  bool QQuickOverlayPrivate::handleMouseEvent(QQuickItem *source,
//      QMouseEvent *event, QQuickPopup *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate16handleMouseEventEP10QQuickItemP11QMouseEventP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickItem *source,
    QMouseEvent *event,
    QQuickPopup *target) {
  return self->handleMouseEvent(source, event, target);
}

//  bool QQuickOverlayPrivate::handleHoverEvent(QQuickItem *source,
//      QHoverEvent *event, QQuickPopup *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate16handleHoverEventEP10QQuickItemP11QHoverEventP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickItem *source,
    QHoverEvent *event,
    QQuickPopup *target) {
  return self->handleHoverEvent(source, event, target);
}

#if QT_CONFIG(quicktemplates2_multitouch)
//  bool QQuickOverlayPrivate::handleTouchEvent(QQuickItem *source,
//      QTouchEvent *event, QQuickPopup *target)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QQuickOverlayPrivate16handleTouchEventEP10QQuickItemP11QTouchEventP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickItem *source,
    QTouchEvent *event,
    QQuickPopup *target) {
  return self->handleTouchEvent(source, event, target);
}
#endif  // QT_CONFIG(quicktemplates2_multitouch)

//  void QQuickOverlayPrivate::addPopup(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate8addPopupEP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickPopup *popup) {
  self->addPopup(popup);
}

//  void QQuickOverlayPrivate::removePopup(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate11removePopupEP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickPopup *popup) {
  self->removePopup(popup);
}

//  void QQuickOverlayPrivate::setMouseGrabberPopup(QQuickPopup *popup)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate20setMouseGrabberPopupEP11QQuickPopup(
    QQuickOverlayPrivate *self,
    QQuickPopup *popup) {
  self->setMouseGrabberPopup(popup);
}

//  QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderPopups() const
extern "C" Q_DECL_EXPORT
QList<QQuickPopup *> *ritual_ZNK20QQuickOverlayPrivate19stackingOrderPopupsEv(
    const QQuickOverlayPrivate *self) {
  return new QList<QQuickPopup *>(self->stackingOrderPopups());
}

//  QList<QQuickPopup *> QQuickOverlayPrivate::stackingOrderDrawers() const
extern "C" Q_DECL_EXPORT
QList<QQuickPopup *> *ritual_ZNK20QQuickOverlayPrivate20stackingOrderDrawersEv(
    const QQuickOverlayPrivate *self) {
  return new QList<QQuickPopup *>(self->stackingOrderDrawers());
}

//  void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickOverlayPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->itemGeometryChanged(item, *change, *diff);
}

//  void QQuickOverlayPrivate::itemRotationChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem(
    QQuickOverlayPrivate *self,
    QQuickItem *item) {
  self->itemRotationChanged(item);
}

//  void QQuickOverlayPrivate::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QQuickOverlayPrivate14updateGeometryEv(
    QQuickOverlayPrivate *self) {
  self->updateGeometry();
}

//  a Python function taken by a CuteQQuickOverlayPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickOverlayPrivate(
    QQuickOverlayPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickOverlayPrivate *>(self)->take(key, call);
}

//  void QQuickOverlayPrivate::itemGeometryChanged(QQuickItem *item,
//      QQuickGeometryChange change, const QRectF &diff)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickOverlayPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF(
    QQuickOverlayPrivate *self,
    QQuickItem *item,
    const QQuickGeometryChange *change,
    const QRectF *diff) {
  self->QQuickOverlayPrivate::itemGeometryChanged(item, *change, *diff);
}

//  void QQuickOverlayPrivate::itemRotationChanged(QQuickItem *item)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN20QQuickOverlayPrivate19itemRotationChangedEP10QQuickItem(
    QQuickOverlayPrivate *self,
    QQuickItem *item) {
  self->QQuickOverlayPrivate::itemRotationChanged(item);
}
