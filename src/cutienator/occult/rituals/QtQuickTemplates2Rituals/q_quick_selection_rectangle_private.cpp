//  Written by dev_tooling.RitualGenerator from the records of QtQuickTemplat
//  es2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p_p.h, Qt
//  6.12.0. Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtGui/qtguiglobal.h>
#include <QtQuickTemplates2/qtquicktemplates2exports.h>
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qtquicktemplates2global_p.h>
#if QT_CONFIG(quick_tableview)
#include <QtQuickTemplates2/QtQuickTemplates2>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/6.12.0/QtQuickTemplates2/private/qquickselectionrectangle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qeventpoint.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquickitemchangelistener_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpalette.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuickTemplates2/private/qquickselectionrectangle_p.h>
#include <QtQuickTemplates2/private/qquickselectionrectangle_p_p.h>
#include <QtQml/qqmlinfo.h>
#include <QtQml/qqmlcomponent.h>
#include <QtQuick/private/qquickdraghandler_p.h>
#include <QtQuick/private/qquickhoverhandler_p.h>
#include <QtQuick/private/qquicktableview_p_p.h>
#include <QtQuickTemplates2/private/qquickscrollview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 171, as _ZN31QQuickSelectionRectanglePrivateC1Ev
inline QQuickSelectionRectanglePrivate::QQuickSelectionRectanglePrivate()
    : QQuickControlPrivate()
{
    m_tapHandler = new QQuickTapHandler();
    m_dragHandler = new QQuickDragHandler();
    m_dragHandler->setTarget(nullptr);

    // QObject::connect() calls in this constructor cannot use `q` as context,
    // because at this point the public class constructor hasn't finished yet

    QObject::connect(&m_scrollTimer, &QTimer::timeout, &m_scrollTimer, [&]{
        if (m_topLeftHandle && m_draggedHandle == m_topLeftHandle.data())
            m_selectable->setSelectionStartPos(m_scrollToPoint);
        else
            m_selectable->setSelectionEndPos(m_scrollToPoint);
        updateHandles();
        const QSizeF dist = m_selectable->scrollTowardsPoint(m_scrollToPoint, m_scrollSpeed);
        m_scrollToPoint.rx() += dist.width() > 0 ? m_scrollSpeed.width() : -m_scrollSpeed.width();
        m_scrollToPoint.ry() += dist.height() > 0 ? m_scrollSpeed.height() : -m_scrollSpeed.height();
        m_scrollSpeed = QSizeF(qAbs(dist.width() * 0.007), qAbs(dist.height() * 0.007));
    });

    QObject::connect(m_tapHandler, &QQuickTapHandler::pressedChanged, m_tapHandler, [this]() {
        Q_Q(QQuickSelectionRectangle);

        if (!m_tapHandler->isPressed()) {
            // Deactivate the selection rectangle when the tap handler
            // is released and there's no selection
            if (q->active() && !m_selectable->hasSelection())
                updateActiveState(false);
            return;
        }
        if (m_effectiveSelectionMode != QQuickSelectionRectangle::Drag)
            return;

        const QPointF pos = m_tapHandler->point().pressPosition();
        const auto modifiers = m_tapHandler->point().modifiers();
        if (modifiers & ~(Qt::ControlModifier | Qt::ShiftModifier))
            return;

        // A selection rectangle is not valid when its width or height is 0
        const auto isSelectionRectValid = [](const QRectF &selectionRect) -> bool {
            return ((selectionRect.width() != 0) || (selectionRect.height() != 0));
        };

        if (modifiers & Qt::ShiftModifier) {
            // Extend the selection towards the pressed cell. If there is no
            // existing selection, start a new selection from the current item
            // to the pressed item.
            if (!m_active) {
                if (!m_selectable->startSelection(pos, modifiers))
                    return;
                m_selectable->setSelectionStartPos(QPoint{-1, -1});
            }
            m_selectable->setSelectionEndPos(pos);
            // Don't update and activate the selection handlers when
            // the size of m_selectable's selection rectangle is 0.
            if (!isSelectionRectValid(m_selectable->selectionRectangle()))
                return;
            updateHandles();
            updateActiveState(true);
        } else if (modifiers & Qt::ControlModifier) {
            // Select a single cell, but keep the old selection (unless
            // m_selectable->startSelection(pos. modifiers) returns false, which
            // it will if selectionMode only allows a single selection).
            if (handleUnderPos(pos) != nullptr) {
                // Don't allow press'n'hold to start a new
                // selection if it started on top of a handle.
                return;
            }

            if (!m_selectable->startSelection(pos, modifiers))
                return;
            m_selectable->setSelectionStartPos(pos);
            m_selectable->setSelectionEndPos(pos);
            // Don't update and activate the selection handlers when
            // the size of m_selectable's selection rectangle is 0.
            if (!isSelectionRectValid(m_selectable->selectionRectangle()))
                return;
            updateHandles();
            updateActiveState(true);
        }
    });

    QObject::connect(m_tapHandler, &QQuickTapHandler::longPressed, m_tapHandler, [this]() {
        if (m_tapHandler->point().device()->type() == QInputDevice::DeviceType::TouchScreen &&
            m_selectionMode == QQuickSelectionRectangle::Auto) {
            const QQuickTableView *tableview = qobject_cast<QQuickTableView *>(m_target);
            if (tableview && !tableview->isInteractive())
                return; // you can select by touch drag, so don't allow touch long-press
            // otherwise, touch long-press is allowed
        } else if (m_effectiveSelectionMode != QQuickSelectionRectangle::PressAndHold) {
            return;
        }

        const QPointF pos = m_tapHandler->point().pressPosition();
        const auto modifiers = m_tapHandler->point().modifiers();
        if (handleUnderPos(pos) != nullptr) {
            // Don't allow press'n'hold to start a new
            // selection if it started on top of a handle.
            return;
        }

        // A selection rectangle is not valid when its width or height is 0
        const auto isSelectionRectValid = [](const QRectF &selectionRect) -> bool {
            return ((selectionRect.width() != 0) || (selectionRect.height() != 0));
        };

        if (modifiers == Qt::ShiftModifier) {
            // Extend the selection towards the pressed cell. If there is no
            // existing selection, start a new selection from the current item
            // to the pressed item.
            if (!m_active) {
                if (!m_selectable->startSelection(pos, modifiers))
                    return;
                m_selectable->setSelectionStartPos(QPoint{-1, -1});
            }
            m_selectable->setSelectionEndPos(pos);
            if (!isSelectionRectValid(m_selectable->selectionRectangle()))
                return;
            updateHandles();
            updateActiveState(true);
        } else {
            // Select a single cell. m_selectable->startSelection() will decide
            // if the existing selection should also be cleared.
            if (!m_selectable->startSelection(pos, modifiers))
                return;
            m_selectable->setSelectionStartPos(pos);
            m_selectable->setSelectionEndPos(pos);
            if (!isSelectionRectValid(m_selectable->selectionRectangle()))
                return;
            updateHandles();
            updateActiveState(true);
        }
    });

    QObject::connect(m_dragHandler, &QQuickDragHandler::activeChanged, m_dragHandler, [this]() {
        Q_ASSERT(m_effectiveSelectionMode == QQuickSelectionRectangle::Drag);
        const QPointF startPos = m_dragHandler->centroid().pressPosition();
        const QPointF dragPos = m_dragHandler->centroid().position();
        const auto modifiers = m_dragHandler->centroid().modifiers();
        if (modifiers & ~(Qt::ControlModifier | Qt::ShiftModifier))
            return;

        // A selection rectangle is not valid when its width or height is 0
        const auto isSelectionRectValid = [](const QRectF &selectionRect) -> bool {
            return ((selectionRect.width() != 0) || (selectionRect.height() != 0));
        };

        if (m_dragHandler->active()) {
            // Start a new selection unless there is an active selection
            // already, and one of the relevant modifiers are being held.
            // In that case we continue to extend the active selection instead.
            const bool modifiersHeld = modifiers & (Qt::ControlModifier | Qt::ShiftModifier);
            if (!m_active || !modifiersHeld) {
                if (!m_selectable->startSelection(startPos, modifiers))
                    return;
                m_selectable->setSelectionStartPos(startPos);
            }
            m_selectable->setSelectionEndPos(dragPos);
            m_draggedHandle = nullptr;
            if (!isSelectionRectValid(m_selectable->selectionRectangle()))
                return;
            updateHandles();
            updateActiveState(true);
            updateDraggingState(true);
        } else {
            m_scrollTimer.stop();
            m_selectable->normalizeSelection();
            updateDraggingState(false);
        }
    });

    QObject::connect(m_dragHandler, &QQuickDragHandler::centroidChanged, m_dragHandler, [this]() {
        if (!m_dragging)
            return;
        const QPointF pos = m_dragHandler->centroid().position();
        m_selectable->setSelectionEndPos(pos);
        updateHandles();
        scrollTowardsPos(pos);
    });
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 383, as _ZN31QQuickSelectionRectanglePrivate19updateDraggingStateEb
inline void QQuickSelectionRectanglePrivate::updateDraggingState(bool dragging)
{
    if (dragging != m_dragging) {
        m_dragging = dragging;
        emit q_func()->draggingChanged();
    }

    if (auto attached = getAttachedObject(m_draggedHandle))
        attached->setDragging(dragging);
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 394, as _ZN31QQuickSelectionRectanglePrivate17updateActiveStateEb
inline void QQuickSelectionRectanglePrivate::updateActiveState(bool active)
{
    if (active == m_active)
        return;

    m_active = active;

    if (const auto tableview = qobject_cast<QQuickTableView *>(m_target)) {
        if (active) {
            // If the position of rows and columns changes, we'll need to reposition the handles
            connect(tableview, &QQuickTableView::layoutChanged, this, &QQuickSelectionRectanglePrivate::updateHandles);
        } else {
            disconnect(tableview, &QQuickTableView::layoutChanged, this, &QQuickSelectionRectanglePrivate::updateHandles);
        }
    }

    emit q_func()->activeChanged();
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 496, as _ZN31QQuickSelectionRectanglePrivate13updateHandlesEv
inline void QQuickSelectionRectanglePrivate::updateHandles()
{
    const QRectF rect = m_selectable->selectionRectangle().normalized();

    if (!m_topLeftHandle && m_topLeftHandleDelegate)
        m_topLeftHandle.reset(createHandle(m_topLeftHandleDelegate, Qt::TopLeftCorner));

    if (!m_bottomRightHandle && m_bottomRightHandleDelegate)
        m_bottomRightHandle.reset(createHandle(m_bottomRightHandleDelegate, Qt::BottomRightCorner));

    if (m_topLeftHandle) {
        m_topLeftHandle->setX(rect.x() - (m_topLeftHandle->width() / 2));
        m_topLeftHandle->setY(rect.y() - (m_topLeftHandle->height() / 2));
    }

    if (m_bottomRightHandle) {
        m_bottomRightHandle->setX(rect.x() + rect.width() - (m_bottomRightHandle->width() / 2));
        m_bottomRightHandle->setY(rect.y() + rect.height() - (m_bottomRightHandle->height() / 2));
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 545, as _ZN31QQuickSelectionRectanglePrivate19updateSelectionModeEv
inline void QQuickSelectionRectanglePrivate::updateSelectionMode()
{
    Q_Q(QQuickSelectionRectangle);

    const bool enabled = q->isEnabled();
    m_tapHandler->setEnabled(enabled);

    if (m_selectionMode == QQuickSelectionRectangle::Auto) {
        if (m_target && qobject_cast<QQuickScrollView *>(m_target->parentItem())) {
            // ScrollView allows flicking with touch, but not with mouse. So we do
            // the opposite here: you can drag to select with a mouse, but not with touch.
            m_effectiveSelectionMode = QQuickSelectionRectangle::Drag;
            m_dragHandler->setAcceptedDevices(QInputDevice::DeviceType::Mouse);
            m_dragHandler->setEnabled(enabled);
        } else if (const auto flickable = qobject_cast<QQuickFlickable *>(m_target)) {
            // Flickable allows flicking with mouse by default, but it can be disabled by
            // changing acceptedMouseButtons(). Setting interactive to false disables flicking
            // altogether. So we allow Drag with devices that don't conflict with flicking.
            if (enabled && (!flickable->isInteractive() ||
                            !flickable->acceptedMouseButtons().testFlag(Qt::LeftButton))) {
                m_effectiveSelectionMode = QQuickSelectionRectangle::Drag;
                m_dragHandler->setAcceptedDevices(flickable->isInteractive()
                                                          ? QInputDevice::DeviceType::Mouse
                                                          : QInputDevice::DeviceType::AllDevices);
                m_dragHandler->setEnabled(true);
            } else {
                m_effectiveSelectionMode = QQuickSelectionRectangle::PressAndHold;
                m_dragHandler->setEnabled(false);
            }
        } else {
            m_effectiveSelectionMode = QQuickSelectionRectangle::Drag;
            m_dragHandler->setAcceptedDevices(QInputDevice::DeviceType::Mouse);
            m_dragHandler->setEnabled(enabled);
        }
    } else if (m_selectionMode == QQuickSelectionRectangle::Drag) {
        m_effectiveSelectionMode = QQuickSelectionRectangle::Drag;
        m_dragHandler->setAcceptedDevices(QInputDevice::DeviceType::AllDevices);
        m_dragHandler->setEnabled(enabled);
    } else {
        m_effectiveSelectionMode = QQuickSelectionRectangle::PressAndHold;
        m_dragHandler->setEnabled(false);
    }
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 517, as _ZN31QQuickSelectionRectanglePrivate15connectToTargetEv
inline void QQuickSelectionRectanglePrivate::connectToTarget()
{
    // To support QuickSelectionRectangle::Auto, we need to listen for changes to the target
    if (const auto flickable = qobject_cast<QQuickFlickable *>(m_target)) {
        connect(flickable, &QQuickFlickable::interactiveChanged, this, &QQuickSelectionRectanglePrivate::updateSelectionMode);
        connect(flickable, &QQuickFlickable::acceptedButtonsChanged, this, &QQuickSelectionRectanglePrivate::updateSelectionMode);
    }

    // Add a callback function that tells if the selection was
    // modified outside of the actions taken by SelectionRectangle.
    m_selectable->setCallback([this](QQuickSelectable::CallBackFlag flag){
        switch (flag) {
        case QQuickSelectable::CallBackFlag::CancelSelection:
            // The selection is either cleared, or can no longer be
            // represented as a rectangle with two selection handles.
            updateActiveState(false);
            break;
        case QQuickSelectable::CallBackFlag::SelectionRectangleChanged:
            // The selection has changed, but the selection is still
            // rectangular and without holes.
            updateHandles();
            break;
        default:
            Q_UNREACHABLE();
        }
    });
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 354, as _ZN31QQuickSelectionRectanglePrivate16scrollTowardsPosERK7QPointF
inline void QQuickSelectionRectanglePrivate::scrollTowardsPos(const QPointF &pos)
{
    m_scrollToPoint = pos;
    if (m_scrollTimer.isActive())
        return;

    const QSizeF dist = m_selectable->scrollTowardsPoint(m_scrollToPoint, m_scrollSpeed);
    if (!dist.isNull())
        m_scrollTimer.start(1);
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 365, as _ZN31QQuickSelectionRectanglePrivate14handleUnderPosERK7QPointF
inline QQuickItem *QQuickSelectionRectanglePrivate::handleUnderPos(const QPointF &pos)
{
    const auto handlerTarget = m_selectable->selectionPointerHandlerTarget();
    if (m_topLeftHandle) {
        const QPointF localPos = m_topLeftHandle->mapFromItem(handlerTarget, pos);
        if (m_topLeftHandle->contains(localPos))
            return m_topLeftHandle.data();
    }

    if (m_bottomRightHandle) {
        const QPointF localPos = m_bottomRightHandle->mapFromItem(handlerTarget, pos);
        if (m_bottomRightHandle->contains(localPos))
            return m_bottomRightHandle.data();
    }

    return nullptr;
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 413, as _ZN31QQuickSelectionRectanglePrivate12createHandleEP13QQmlComponentN2Qt6CornerE
inline QQuickItem *QQuickSelectionRectanglePrivate::createHandle(QQmlComponent *delegate, Qt::Corner corner)
{
    Q_Q(QQuickSelectionRectangle);

    // Incubate the handle
    QObject *obj = delegate->beginCreate(QQmlEngine::contextForObject(q));
    QQuickItem *handleItem = qobject_cast<QQuickItem*>(obj);
    const auto handlerTarget = m_selectable->selectionPointerHandlerTarget();
    handleItem->setParentItem(handlerTarget);
    if (auto attached = getAttachedObject(handleItem))
        attached->setControl(q);
    delegate->completeCreate();
    if (handleItem->z() == 0)
        handleItem->setZ(100);

    // Add pointer handlers to it
    QQuickDragHandler *dragHandler = new QQuickDragHandler();
    dragHandler->setTarget(nullptr);
    dragHandler->setParentItem(handleItem);
    dragHandler->setGrabPermissions(QQuickPointerHandler::CanTakeOverFromAnything);

    QQuickHoverHandler *hoverHandler = new QQuickHoverHandler();
    hoverHandler->setTarget(nullptr);
    hoverHandler->setParentItem(handleItem);
#if QT_CONFIG(cursor)
    hoverHandler->setCursorShape(Qt::SizeFDiagCursor);
#endif
    hoverHandler->setBlocking(true);

    // Add a dummy TapHandler that blocks the user from being
    // able to tap on a tap handler underneath the handle.
    QQuickTapHandler *tapHandler = new QQuickTapHandler();
    tapHandler->setTarget(nullptr);
    tapHandler->setParentItem(handleItem);
    // Set a dummy gesture policy so that the tap handler
    // will get an exclusive grab already on press
    tapHandler->setGesturePolicy(QQuickTapHandler::DragWithinBounds);

    QObject::connect(dragHandler, &QQuickDragHandler::activeChanged, q,
                     [this, corner, handleItem, dragHandler]() {
        if (dragHandler->active()) {
            const QPointF localPos = dragHandler->centroid().position();
            const QPointF pos = handleItem->mapToItem(handleItem->parentItem(), localPos);
            if (corner == Qt::TopLeftCorner)
                m_selectable->setSelectionStartPos(pos);
            else
                m_selectable->setSelectionEndPos(pos);

            m_draggedHandle = handleItem;
            updateHandles();
            updateDraggingState(true);
#if QT_CONFIG(cursor)
            QGuiApplication::setOverrideCursor(Qt::SizeFDiagCursor);
#endif
        } else {
            m_scrollTimer.stop();
            m_selectable->normalizeSelection();
            updateDraggingState(false);
#if QT_CONFIG(cursor)
            QGuiApplication::restoreOverrideCursor();
#endif
        }
    });

    QObject::connect(dragHandler, &QQuickDragHandler::centroidChanged, q,
                     [this, corner, handleItem, dragHandler]() {
        if (!m_dragging)
            return;

        const QPointF localPos = dragHandler->centroid().position();
        const QPointF pos = handleItem->mapToItem(handleItem->parentItem(), localPos);
        if (corner == Qt::TopLeftCorner)
            m_selectable->setSelectionStartPos(pos);
        else
            m_selectable->setSelectionEndPos(pos);

        updateHandles();
        scrollTowardsPos(pos);
    });

    return handleItem;
}

//  from ../qtdeclarative/src/quicktemplates/qquickselectionrectangle.cpp, line 589, as _ZNK31QQuickSelectionRectanglePrivate17getAttachedObjectEPK7QObject
inline QQuickSelectionRectangleAttached *QQuickSelectionRectanglePrivate::getAttachedObject(const QObject *object) const
{
    QObject *attachedObject = qmlAttachedPropertiesObject<QQuickSelectionRectangle>(object);
    return static_cast<QQuickSelectionRectangleAttached *>(attachedObject);
}
//  -----------------------------------------------------------------------

//  A QQuickSelectionRectanglePrivate that Python can take functions over in. Every QQuickSelectionRectanglePrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickSelectionRectanglePrivateCall0)(const void *, const QEventPoint *, int *);
#endif  // QT_CONFIG(quicktemplates2_multitouch)
typedef bool (*CuteQQuickSelectionRectanglePrivateCall1)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickSelectionRectanglePrivateCall2)(const void *, const QPointF *, ulong, int *);
typedef bool (*CuteQQuickSelectionRectanglePrivateCall3)(const void *, const QPointF *, ulong, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall4)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall5)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall6)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall7)(const void *, int *);
typedef void * (*CuteQQuickSelectionRectanglePrivateCall8)(const void *, int *);
#if QT_CONFIG(accessibility)
typedef void (*CuteQQuickSelectionRectanglePrivateCall9)(const void *, bool, int *);
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
typedef int (*CuteQQuickSelectionRectanglePrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void (*CuteQQuickSelectionRectanglePrivateCall11)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall12)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall13)(const void *, bool, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall14)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall15)(const void *, bool, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall16)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall17)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall18)(const void *, QQuickItem *, const QQuickGeometryChange *, const QRectF *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall19)(const void *, QQuickItem *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall20)(const void *, QQuickItem *, int, int *);
typedef bool (*CuteQQuickSelectionRectanglePrivateCall21)(const void *, int, int *);
typedef qreal (*CuteQQuickSelectionRectanglePrivateCall22)(const void *, int *);
typedef qreal (*CuteQQuickSelectionRectanglePrivateCall23)(const void *, int *);
typedef const QPalette * (*CuteQQuickSelectionRectanglePrivateCall24)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall25)(const void *, QQuickPointerHandler *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall26)(const void *, QQuickPointerHandler *, int *);
typedef void * (*CuteQQuickSelectionRectanglePrivateCall27)(const void *, const QMetaObject *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall28)(const void *, QQuickItem *, bool, int *);
typedef qreal (*CuteQQuickSelectionRectanglePrivateCall29)(const void *, int *);
typedef qreal (*CuteQQuickSelectionRectanglePrivateCall30)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall31)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall32)(const void *, int *);
typedef bool (*CuteQQuickSelectionRectanglePrivateCall33)(const void *, QQuickItem *, int *);
typedef bool (*CuteQQuickSelectionRectanglePrivateCall34)(const void *, QPointerEvent *, bool, int *);
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef bool (*CuteQQuickSelectionRectanglePrivateCall35)(const void *, QContextMenuEvent *, int *);
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
typedef void (*CuteQQuickSelectionRectanglePrivateCall36)(const void *, bool, int *);
typedef void * (*CuteQQuickSelectionRectanglePrivateCall37)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall38)(const void *, int *);
typedef void (*CuteQQuickSelectionRectanglePrivateCall39)(const void *, int, int *);
class CuteQQuickSelectionRectanglePrivate : public QQuickSelectionRectanglePrivate {
public:
  using QQuickSelectionRectanglePrivate::QQuickSelectionRectanglePrivate;
  void *taken[40] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11acceptTouchERK11QEventPoint")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quicktemplates2_multitouch)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11handlePressERK7QPointFm")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate10handleMoveERK7QPointFm")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13handleReleaseERK7QPointFm")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate12handleUngrabEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12mirrorChangeEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16resizeBackgroundEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13resizeContentEv")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate14getContentItemEv")) {
      taken[8] = call;
      return true;
    }
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN11QAccessible18ActivationObserver26accessibilityActiveChangedEb")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate14accessibleRoleEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate11resolveFontEv")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17cancelContentItemEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate18executeContentItemEb")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16cancelBackgroundEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate17executeBackgroundEb")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate24itemImplicitWidthChangedEP10QQuickItem")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate25itemImplicitHeightChangedEP10QQuickItem")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate19itemGeometryChangedEP10QQuickItem20QQuickGeometryChangeRK6QRectF")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate13itemDestroyedEP10QQuickItem")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN20QQuickControlPrivate16itemFocusChangedEP10QQuickItemN2Qt11FocusReasonE")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate24setLastFocusChangeReasonEN2Qt11FocusReasonE")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate15getContentWidthEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate16getContentHeightEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK20QQuickControlPrivate14defaultPaletteEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate17addPointerHandlerEP20QQuickPointerHandler")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20removePointerHandlerEP20QQuickPointerHandler")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate33attachedPropertyPropagator_parentEPK11QMetaObject")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate25registerAsContainmentMaskEP10QQuickItemb")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate16getImplicitWidthEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate17getImplicitHeightEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate20implicitWidthChangedEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate21implicitHeightChangedEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate16transformChangedEP10QQuickItem")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate18handlePointerEventEP13QPointerEventb")) {
      taken[34] = call;
      return true;
    }
#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate22handleContextMenuEventEP17QContextMenuEvent")) {
      taken[35] = call;
      return true;
    }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate10setVisibleEb")) {
      taken[36] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate19createTransformNodeEv")) {
      taken[37] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN17QQuickItemPrivate12updatePolishEv")) {
      taken[38] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK17QQuickItemPrivate12dumpItemTreeEi")) {
      taken[39] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quicktemplates2_multitouch)
  //  bool QQuickControlPrivate::acceptTouch(const QTouchEvent::TouchPoint
  //      &point)
  bool acceptTouch(const QTouchEvent::TouchPoint &point) override {
    if (taken[0]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall0 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall0>(taken[0]);
      bool given = call(this, &point, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::acceptTouch(point);
  }
#endif  // QT_CONFIG(quicktemplates2_multitouch)

  //  bool QQuickControlPrivate::handlePress(const QPointF &point, ulong
  //      timestamp)
  bool handlePress(const QPointF &point, ulong timestamp) override {
    if (taken[1]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall1 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall1>(taken[1]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handlePress(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleMove(const QPointF &point, ulong
  //      timestamp)
  bool handleMove(const QPointF &point, ulong timestamp) override {
    if (taken[2]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall2 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall2>(taken[2]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleMove(point, timestamp);
  }

  //  bool QQuickControlPrivate::handleRelease(const QPointF &point, ulong
  //      timestamp)
  bool handleRelease(const QPointF &point, ulong timestamp) override {
    if (taken[3]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall3 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall3>(taken[3]);
      bool given = call(this, &point, timestamp, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::handleRelease(point, timestamp);
  }

  //  void QQuickControlPrivate::handleUngrab()
  void handleUngrab() override {
    if (taken[4]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall4 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::handleUngrab();
  }

  //  void QQuickControlPrivate::mirrorChange()
  void mirrorChange() override {
    if (taken[5]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall5 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::mirrorChange();
  }

  //  void QQuickControlPrivate::resizeBackground()
  void resizeBackground() override {
    if (taken[6]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall6 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall6>(taken[6]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeBackground();
  }

  //  void QQuickControlPrivate::resizeContent()
  void resizeContent() override {
    if (taken[7]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall7 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resizeContent();
  }

  //  QQuickItem *QQuickControlPrivate::getContentItem()
  QQuickItem *getContentItem() override {
    if (taken[8]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall8 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall8>(taken[8]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QQuickItem *>(given);
    }
    return QQuickControlPrivate::getContentItem();
  }

#if QT_CONFIG(accessibility)
  //  void QQuickControlPrivate::accessibilityActiveChanged(bool active)
  void accessibilityActiveChanged(bool active) override {
    if (taken[9]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall9 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall9>(taken[9]);
      call(this, active, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::accessibilityActiveChanged(active);
  }
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
  //  QAccessible::Role QQuickControlPrivate::accessibleRole() const
  QAccessible::Role accessibleRole() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall10 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall10>(taken[10]);
      int given = call(this, &handled);
      if (handled) return static_cast<QAccessible::Role>(given);
    }
    return QQuickControlPrivate::accessibleRole();
  }
#endif  // QT_CONFIG(accessibility)

  //  void QQuickControlPrivate::resolveFont()
  void resolveFont() override {
    if (taken[11]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall11 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::resolveFont();
  }

  //  void QQuickControlPrivate::cancelContentItem()
  void cancelContentItem() override {
    if (taken[12]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall12 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelContentItem();
  }

  //  void QQuickControlPrivate::executeContentItem(bool complete)
  void executeContentItem(bool complete) override {
    if (taken[13]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall13 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall13>(taken[13]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeContentItem(complete);
  }

  //  void QQuickControlPrivate::cancelBackground()
  void cancelBackground() override {
    if (taken[14]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall14 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::cancelBackground();
  }

  //  void QQuickControlPrivate::executeBackground(bool complete)
  void executeBackground(bool complete) override {
    if (taken[15]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall15 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall15>(taken[15]);
      call(this, complete, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::executeBackground(complete);
  }

  //  void QQuickControlPrivate::itemImplicitWidthChanged(QQuickItem *item)
  void itemImplicitWidthChanged(QQuickItem *item) override {
    if (taken[16]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall16 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall16>(taken[16]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitWidthChanged(item);
  }

  //  void QQuickControlPrivate::itemImplicitHeightChanged(QQuickItem
  //      *item)
  void itemImplicitHeightChanged(QQuickItem *item) override {
    if (taken[17]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall17 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall17>(taken[17]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemImplicitHeightChanged(item);
  }

  //  void QQuickControlPrivate::itemGeometryChanged(QQuickItem *item,
  //      QQuickGeometryChange change, const QRectF &diff)
  void itemGeometryChanged(
      QQuickItem *item,
      QQuickGeometryChange change,
      const QRectF &diff) override {
    if (taken[18]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall18 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall18>(taken[18]);
      call(this, item, &change, &diff, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemGeometryChanged(item, change, diff);
  }

  //  void QQuickControlPrivate::itemDestroyed(QQuickItem *item)
  void itemDestroyed(QQuickItem *item) override {
    if (taken[19]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall19 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall19>(taken[19]);
      call(this, item, &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemDestroyed(item);
  }

  //  void QQuickControlPrivate::itemFocusChanged(QQuickItem *item,
  //      Qt::FocusReason reason)
  void itemFocusChanged(QQuickItem *item, Qt::FocusReason reason) override {
    if (taken[20]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall20 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall20>(taken[20]);
      call(this, item, static_cast<int>(reason), &handled);
      if (handled) return;
    }
    QQuickControlPrivate::itemFocusChanged(item, reason);
  }

  //  bool QQuickControlPrivate::setLastFocusChangeReason(Qt::FocusReason
  //      a0)
  bool setLastFocusChangeReason(Qt::FocusReason a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall21 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall21>(taken[21]);
      bool given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::setLastFocusChangeReason(a0);
  }

  //  qreal QQuickControlPrivate::getContentWidth() const
  qreal getContentWidth() const override {
    if (taken[22]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall22 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall22>(taken[22]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentWidth();
  }

  //  qreal QQuickControlPrivate::getContentHeight() const
  qreal getContentHeight() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall23 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall23>(taken[23]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickControlPrivate::getContentHeight();
  }

  //  QPalette QQuickControlPrivate::defaultPalette() const
  QPalette defaultPalette() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall24 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall24>(taken[24]);
      const QPalette * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QQuickControlPrivate::defaultPalette();
  }

  //  void QQuickItemPrivate::addPointerHandler(QQuickPointerHandler *h)
  void addPointerHandler(QQuickPointerHandler *h) override {
    if (taken[25]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall25 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall25>(taken[25]);
      call(this, h, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::addPointerHandler(h);
  }

  //  void QQuickItemPrivate::removePointerHandler(QQuickPointerHandler *h)
  void removePointerHandler(QQuickPointerHandler *h) override {
    if (taken[26]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall26 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall26>(taken[26]);
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
    if (taken[27]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall27 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall27>(taken[27]);
      void * given = call(this, attachedType, &handled);
      if (handled) return static_cast<QtPrivate::QQuickAttachedPropertyPropagator *>(given);
    }
    return QQuickItemPrivate::attachedPropertyPropagator_parent(attachedType);
  }

  //  void QQuickItemPrivate::registerAsContainmentMask(QQuickItem *a0,
  //      bool a1)
  void registerAsContainmentMask(QQuickItem *a0, bool a1) override {
    if (taken[28]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall28 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall28>(taken[28]);
      call(this, a0, a1, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::registerAsContainmentMask(a0, a1);
  }

  //  qreal QQuickItemPrivate::getImplicitWidth() const
  qreal getImplicitWidth() const override {
    if (taken[29]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall29 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall29>(taken[29]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitWidth();
  }

  //  qreal QQuickItemPrivate::getImplicitHeight() const
  qreal getImplicitHeight() const override {
    if (taken[30]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall30 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall30>(taken[30]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::getImplicitHeight();
  }

  //  void QQuickItemPrivate::implicitWidthChanged()
  void implicitWidthChanged() override {
    if (taken[31]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall31 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitWidthChanged();
  }

  //  void QQuickItemPrivate::implicitHeightChanged()
  void implicitHeightChanged() override {
    if (taken[32]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall32 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::implicitHeightChanged();
  }

  //  bool QQuickItemPrivate::transformChanged(QQuickItem *transformedItem)
  bool transformChanged(QQuickItem *transformedItem) override {
    if (taken[33]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall33 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall33>(taken[33]);
      bool given = call(this, transformedItem, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::transformChanged(transformedItem);
  }

  //  bool QQuickItemPrivate::handlePointerEvent(QPointerEvent *a0, bool
  //      avoidGrabbers)
  bool handlePointerEvent(QPointerEvent *a0, bool avoidGrabbers) override {
    if (taken[34]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall34 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall34>(taken[34]);
      bool given = call(this, a0, avoidGrabbers, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handlePointerEvent(a0, avoidGrabbers);
  }

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
  //  bool QQuickItemPrivate::handleContextMenuEvent(QContextMenuEvent
  //      *event)
  bool handleContextMenuEvent(QContextMenuEvent *event) override {
    if (taken[35]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall35 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall35>(taken[35]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QQuickItemPrivate::handleContextMenuEvent(event);
  }
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

  //  void QQuickItemPrivate::setVisible(bool visible)
  void setVisible(bool visible) override {
    if (taken[36]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall36 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall36>(taken[36]);
      call(this, visible, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::setVisible(visible);
  }

  //  QSGTransformNode *QQuickItemPrivate::createTransformNode()
  QSGTransformNode *createTransformNode() override {
    if (taken[37]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall37 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall37>(taken[37]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QSGTransformNode *>(given);
    }
    return QQuickItemPrivate::createTransformNode();
  }

  //  void QQuickItemPrivate::updatePolish()
  void updatePolish() override {
    if (taken[38]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall38 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall38>(taken[38]);
      call(this, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::updatePolish();
  }

  //  void QQuickItemPrivate::dumpItemTree(int indent) const
  void dumpItemTree(int indent) const override {
    if (taken[39]) {
      int handled = 0;
      CuteQQuickSelectionRectanglePrivateCall39 call = reinterpret_cast<CuteQQuickSelectionRectanglePrivateCall39>(taken[39]);
      call(this, indent, &handled);
      if (handled) return;
    }
    QQuickItemPrivate::dumpItemTree(indent);
  }
};

//  QQuickSelectionRectangle *QQuickSelectionRectanglePrivate::q_func()
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangle *ritual_ZN31QQuickSelectionRectanglePrivate6q_funcEv(
    QQuickSelectionRectanglePrivate *self) {
  return self->q_func();
}

//  const QQuickSelectionRectangle *QQuickSelectionRectanglePrivate::q_func()
//      const
extern "C" Q_DECL_EXPORT
const QQuickSelectionRectangle *ritual_ZNK31QQuickSelectionRectanglePrivate6q_funcEv(
    const QQuickSelectionRectanglePrivate *self) {
  return self->q_func();
}

//  QQuickSelectionRectanglePrivate::QQuickSelectionRectanglePrivate()
extern "C" Q_DECL_EXPORT
QQuickSelectionRectanglePrivate *ritual_ZN31QQuickSelectionRectanglePrivateC1Ev() {
  return new CuteQQuickSelectionRectanglePrivate();
}

//  void QQuickSelectionRectanglePrivate::updateDraggingState(bool
//      isDragging)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate19updateDraggingStateEb(
    QQuickSelectionRectanglePrivate *self,
    bool isDragging) {
  self->updateDraggingState(isDragging);
}

//  void QQuickSelectionRectanglePrivate::updateActiveState(bool isActive)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate17updateActiveStateEb(
    QQuickSelectionRectanglePrivate *self,
    bool isActive) {
  self->updateActiveState(isActive);
}

//  void QQuickSelectionRectanglePrivate::updateHandles()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate13updateHandlesEv(
    QQuickSelectionRectanglePrivate *self) {
  self->updateHandles();
}

//  void QQuickSelectionRectanglePrivate::updateSelectionMode()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate19updateSelectionModeEv(
    QQuickSelectionRectanglePrivate *self) {
  self->updateSelectionMode();
}

//  void QQuickSelectionRectanglePrivate::connectToTarget()
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate15connectToTargetEv(
    QQuickSelectionRectanglePrivate *self) {
  self->connectToTarget();
}

//  void QQuickSelectionRectanglePrivate::scrollTowardsPos(const QPointF
//      &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN31QQuickSelectionRectanglePrivate16scrollTowardsPosERK7QPointF(
    QQuickSelectionRectanglePrivate *self,
    const QPointF *pos) {
  self->scrollTowardsPos(*pos);
}

//  QQuickItem *QQuickSelectionRectanglePrivate::handleUnderPos(const QPointF
//      &pos)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN31QQuickSelectionRectanglePrivate14handleUnderPosERK7QPointF(
    QQuickSelectionRectanglePrivate *self,
    const QPointF *pos) {
  return self->handleUnderPos(*pos);
}

//  QQuickItem *QQuickSelectionRectanglePrivate::createHandle(QQmlComponent
//      *delegate, Qt::Corner corner)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN31QQuickSelectionRectanglePrivate12createHandleEP13QQmlComponentN2Qt6CornerE(
    QQuickSelectionRectanglePrivate *self,
    QQmlComponent *delegate,
    Qt::Corner corner) {
  return self->createHandle(delegate, corner);
}

//  QQuickSelectionRectangleAttached
//      *QQuickSelectionRectanglePrivate::getAttachedObject(const QObject
//      *object) const
extern "C" Q_DECL_EXPORT
QQuickSelectionRectangleAttached *ritual_ZNK31QQuickSelectionRectanglePrivate17getAttachedObjectEPK7QObject(
    const QQuickSelectionRectanglePrivate *self,
    const QObject *object) {
  return self->getAttachedObject(object);
}

//  a Python function taken by a CuteQQuickSelectionRectanglePrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QQuickSelectionRectanglePrivate(
    QQuickSelectionRectanglePrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQQuickSelectionRectanglePrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(quick_tableview)
