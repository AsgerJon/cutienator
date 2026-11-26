//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qwidgetwindow_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qwidgetwindow_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/qsurfaceformat.h>
#include <QtCore/qsize.h>
#include <QtCore/qmetaobject.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/private/qwindow_p.h>
#include <QtWidgets/private/qwidgetwindow_p.h>
#include <QtWidgets/qlayout.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtWidgets/private/qapplication_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/private/qwidgetrepaintmanager_p.h>
#include <QtGui/qpa/qwindowsysteminterface_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtGui/qpa/qplatformwindow.h>
#include <QtWidgets/private/qgesturemanager_p.h>
#include <QtGui/private/qhighdpiscaling_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/kernel/qwidgetwindow.cpp, line 35, as local:qwidgetwindow.cpp:QWidgetWindowPrivate
class QWidgetWindowPrivate : public QWindowPrivate
{
    Q_DECLARE_PUBLIC(QWidgetWindow)
public:
    void setVisible(bool visible) override
    {
        Q_Q(QWidgetWindow);
        qCDebug(lcWidgetShowHide) << "Setting visibility of" << q->widget()
               << "to" << visible << "via QWidgetWindowPrivate";

        if (QWidget *widget = q->widget()) {
            // If the widget's visible state is already matching the new QWindow
            // visible state we assume the widget has already synced up.
            if (visible != widget->isVisible())
                QWidgetPrivate::get(widget)->setVisible(visible);
        }

        // If we end up calling QWidgetPrivate::setVisible() above, we will
        // in most cases recurse back into setNativeWindowVisibility() to
        // update the QWindow state. But during QWidget::destroy() this is
        // not the case, as Qt::WA_WState_Created has been unset by the time
        // we check if we should call hide_helper(). We handle this case, as
        // well as the cases where we don't call QWidgetPrivate::setVisible(),
        // by syncing up the QWindow state here if needed.
        if (q->isVisible() != visible)
            QWindowPrivate::setVisible(visible);
    }

    QWindow *eventReceiver() override {
        Q_Q(QWidgetWindow);
        QWindow *w = q;
        while (w->parent() && qobject_cast<QWidgetWindow *>(w) && qobject_cast<QWidgetWindow *>(w->parent())) {
            w = w->parent();
        }
        return w;
    }

    void clearFocusObject() override
    {
        Q_Q(QWidgetWindow);
        QWidget *widget = q->widget();
        if (widget && widget->focusWidget())
            widget->focusWidget()->clearFocus();
    }

    void setFocusToTarget(FocusTarget target, Qt::FocusReason reason) override
    {
        Q_Q(QWidgetWindow);
        QWidget *widget = q->widget();
        if (!widget)
            return;

        switch (target) {
        case FocusTarget::Prev:
        case FocusTarget::Next: {
            QWidget *focusWidget = widget->focusWidget() ? widget->focusWidget() : widget;
            q->focusNextPrevChild(focusWidget, target == FocusTarget::Next);
            return;
        }
        case FocusTarget::First:
        case FocusTarget::Last: {
            QWidgetWindow::FocusWidgets fw = target == FocusTarget::First
                ? QWidgetWindow::FirstFocusWidget
                : QWidgetWindow::LastFocusWidget;
            if (QWidget *newFocusWidget = q->getFocusWidget(fw))
                newFocusWidget->setFocus(reason);
            break;
        }
        default:
            break;
        }
    }

    QRectF closestAcceptableGeometry(const QRectF &rect) const override;

    bool participatesInLastWindowClosed() const override;
    bool treatAsVisible() const override;

    QPalette windowPalette() const override
    {
        Q_Q(const QWidgetWindow);
        if (const auto *widget = q->widget())
            return widget->palette();
        return QWindowPrivate::windowPalette();
    }
};

//  from src/widgets/kernel/qwidgetwindow.cpp, line 122, as local:qwidgetwindow.cpp:QWidgetWindowPrivate::closestAcceptableGeometry
inline QRectF QWidgetWindowPrivate::closestAcceptableGeometry(const QRectF &rect) const
{
    Q_Q(const QWidgetWindow);
    const QWidget *widget = q->widget();
    if (!widget || !widget->isWindow() || !widget->hasHeightForWidth())
        return QRect();
    const QSize oldSize = rect.size().toSize();
    const QSize newSize = QLayout::closestAcceptableSize(widget, oldSize);
    if (newSize == oldSize)
        return QRectF();
    const int dw = newSize.width() - oldSize.width();
    const int dh = newSize.height() - oldSize.height();
    QRectF result = rect;
    const QRectF currentGeometry(widget->geometry());
    const qreal topOffset = result.top() - currentGeometry.top();
    const qreal bottomOffset = result.bottom() - currentGeometry.bottom();
    if (qAbs(topOffset) > qAbs(bottomOffset))
        result.setTop(result.top() - dh); // top edge drag
    else
        result.setBottom(result.bottom() + dh); // bottom edge drag
    const qreal leftOffset = result.left() - currentGeometry.left();
    const qreal rightOffset = result.right() - currentGeometry.right();
    if (qAbs(leftOffset) > qAbs(rightOffset))
        result.setLeft(result.left() - dw); // left edge drag
    else
        result.setRight(result.right() + dw); // right edge drag
    return result;
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 772, as local:qwidgetwindow.cpp:sendChangeRecursively
static void sendChangeRecursively(QWidget *widget, QEvent::Type type)
{
    QEvent e(type);
    QCoreApplication::sendEvent(widget, &e);
    QWidgetPrivate *d = QWidgetPrivate::get(widget);
    for (int i = 0; i < d->children.size(); ++i) {
        QWidget *w = qobject_cast<QWidget *>(d->children.at(i));
        if (w)
            sendChangeRecursively(w, type);
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 903, as local:qwidgetwindow.cpp:QWidgetWindowPrivate::participatesInLastWindowClosed
inline bool QWidgetWindowPrivate::participatesInLastWindowClosed() const
{
    Q_Q(const QWidgetWindow);

    // For historical reasons WA_QuitOnClose has been closely tied
    // to the lastWindowClosed signal, since the default behavior
    // is to quit the application after emitting lastWindowClosed.
    // ### Qt 7: Rename this attribute, or decouple behavior.
    if (!q->widget()->testAttribute(Qt::WA_QuitOnClose))
        return false;

    return QWindowPrivate::participatesInLastWindowClosed();
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 917, as local:qwidgetwindow.cpp:QWidgetWindowPrivate::treatAsVisible
inline bool QWidgetWindowPrivate::treatAsVisible() const
{
    Q_Q(const QWidgetWindow);

    // Widget windows may have Qt::WA_DontShowOnScreen, in which case the
    // QQWidget will be visible, but the corresponding QWindow will not.
    // Since the lastWindowClosed logic relies on checking whether the
    // closed window was visible, and if there are any remaining visible
    // windows, we need to reflect the QWidget state, not the QWindow one.
    return q->widget()->isVisible();
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 966, as local:qwidgetwindow.cpp:findDnDTarget
#if QT_CONFIG(draganddrop)
static QWidget *findDnDTarget(QWidget *parent, const QPointF &pos)
{
    // Find a target widget under mouse that accepts drops (QTBUG-22987).
    QWidget *widget = parent->childAt(pos);
    if (!widget)
        widget = parent;
    for ( ; widget && !widget->isWindow() && !widget->acceptDrops(); widget = widget->parentWidget()) ;
    if (widget && !widget->acceptDrops())
        widget = nullptr;
    return widget;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 191, as _ZNK13QWidgetWindow14accessibleRootEv
#if QT_CONFIG(accessibility)
inline QAccessibleInterface *QWidgetWindow::accessibleRoot() const
{
    if (m_widget)
        return QAccessible::queryAccessibleInterface(m_widget);
    return nullptr;
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 199, as _ZNK13QWidgetWindow11focusObjectEv
inline QObject *QWidgetWindow::focusObject() const
{
    QWidget *windowWidget = m_widget;
    if (!windowWidget)
        return nullptr;

    // A window can't have a focus object if it's being destroyed.
    if (QWidgetPrivate::get(windowWidget)->data.in_destructor)
        return nullptr;

    QWidget *widget = windowWidget->focusWidget();

    if (!widget)
        widget = windowWidget;

    QObject *focusObj = QWidgetPrivate::get(widget)->focusObject();
    if (focusObj)
        return focusObj;

    return widget;
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 168, as _ZN13QWidgetWindowD1Ev
inline QWidgetWindow::~QWidgetWindow()
{
    // destroy while we are still alive
    destroy();

    if (!m_widget)
        return;

    QTLWExtra *topData = QWidgetPrivate::get(m_widget)->topData();
    Q_ASSERT(topData);

    // The QPlaformBackingStore may hold a reference to the window,
    // so the backingstore needs to be deleted first.
    topData->repaintManager.reset(nullptr);
    delete topData->backingStore;
    topData->backingStore = nullptr;
    topData->widgetTextures.clear();

    // Too late to do anything beyond this point
    topData->window = nullptr;
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 233, as _ZN13QWidgetWindow18focusNextPrevChildEP7QWidgetb
inline void QWidgetWindow::focusNextPrevChild(QWidget *widget, bool next)
{
    Q_ASSERT(widget);
    widget->focusNextPrevChild(next);
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 510, as _ZN13QWidgetWindow29handleNonClientAreaMouseEventEP11QMouseEvent
inline void QWidgetWindow::handleNonClientAreaMouseEvent(QMouseEvent *e)
{
    QApplication::forwardEvent(m_widget, e);
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 713, as _ZN13QWidgetWindow16handleTouchEventEP11QTouchEvent
inline void QWidgetWindow::handleTouchEvent(QTouchEvent *event)
{
    if (event->type() == QEvent::TouchCancel) {
        QApplicationPrivate::translateTouchCancel(event->pointingDevice(), event->timestamp());
        event->accept();
    } else if (QApplication::activePopupWidget()) {
        // Ignore touch events for popups. This will cause QGuiApplication to synthesise mouse
        // events instead, which QWidgetWindow::handleMouseEvent will forward correctly:
        event->ignore();
    } else {
        event->setAccepted(QApplicationPrivate::translateRawTouchEvent(m_widget, event));
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 845, as _ZN13QWidgetWindow15handleMoveEventEP10QMoveEvent
inline void QWidgetWindow::handleMoveEvent(QMoveEvent *event)
{
    if (m_widget->testAttribute(Qt::WA_OutsideWSRange))
        return;
    if (m_widget->testAttribute(Qt::WA_DontShowOnScreen))
        return;

    auto oldPosition = m_widget->data->crect.topLeft();
    auto newPosition = geometry().topLeft();

    if (!m_widget->isWindow()) {
        if (auto *nativeParent = m_widget->nativeParentWidget())
            newPosition = m_widget->parentWidget()->mapFrom(nativeParent, newPosition);
    }

    bool changed = newPosition != oldPosition;

    if (changed)
        m_widget->data->crect.moveTopLeft(newPosition);

    updateMargins(); // FIXME: Only do when changed?

    if (changed) {
        QMoveEvent widgetEvent(newPosition, oldPosition);
        QGuiApplication::forwardEvent(m_widget, &widgetEvent, event);
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 873, as _ZN13QWidgetWindow17handleResizeEventEP12QResizeEvent
inline void QWidgetWindow::handleResizeEvent(QResizeEvent *event)
{
    auto oldRect = m_widget->rect();

    if (updateSize()) {
        QGuiApplication::forwardEvent(m_widget, event);

        if (m_widget->d_func()->shouldPaintOnScreen()) {
            QRegion dirtyRegion = m_widget->rect();
            if (m_widget->testAttribute(Qt::WA_StaticContents))
                dirtyRegion -= oldRect;
            m_widget->d_func()->syncBackingStore(dirtyRegion);
        } else {
            m_widget->d_func()->syncBackingStore();
        }
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 988, as _ZN13QWidgetWindow20handleDragEnterEventEP14QDragMoveEventP7QWidget
#if QT_CONFIG(draganddrop)
inline void QWidgetWindow::handleDragEnterEvent(QDragMoveEvent *event, QWidget *widget)
{
    Q_ASSERT(m_dragTarget == nullptr);
    if (!widget)
        widget = findDnDTarget(m_widget, event->position());
    if (!widget) {
        event->ignore();
        return;
    }
    m_dragTarget = widget;

    const QPointF mapped = widget->mapFromGlobal(m_widget->mapToGlobal(event->position()));
    QDragEnterEvent translated(mapped, event->possibleActions(), event->mimeData(),
                               event->buttons(), event->modifiers());
    QGuiApplication::forwardEvent(m_dragTarget, &translated, event);
    event->setAccepted(translated.isAccepted());
    event->setDropAction(translated.dropAction());
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1052, as _ZN13QWidgetWindow20handleDragLeaveEventEP15QDragLeaveEvent
#if QT_CONFIG(draganddrop)
inline void QWidgetWindow::handleDragLeaveEvent(QDragLeaveEvent *event)
{
    if (m_dragTarget) {
        QWidget *dragTarget = m_dragTarget;
        m_dragTarget = nullptr;
        QGuiApplication::forwardEvent(dragTarget, event);
    }
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1061, as _ZN13QWidgetWindow15handleDropEventEP10QDropEvent
#if QT_CONFIG(draganddrop)
inline void QWidgetWindow::handleDropEvent(QDropEvent *event)
{
    if (Q_UNLIKELY(m_dragTarget.isNull())) {
        qWarning() << m_widget << ": No drag target set.";
        event->ignore();
        return;
    }
    const QPointF mapped = m_dragTarget->mapFromGlobal(m_widget->mapToGlobal(event->position()));
    QDropEvent translated(mapped, event->possibleActions(), event->mimeData(), event->buttons(), event->modifiers());
    QWidget *dragTarget = m_dragTarget;
    m_dragTarget = nullptr;
    QGuiApplication::forwardEvent(dragTarget, &translated, event);
    event->setAccepted(translated.isAccepted());
    event->setDropAction(translated.dropAction());
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1079, as _ZN13QWidgetWindow17handleExposeEventEP12QExposeEvent
inline void QWidgetWindow::handleExposeEvent(QExposeEvent *event)
{
    if (m_widget->testAttribute(Qt::WA_DontShowOnScreen))
        return; // Ignore for widgets that fake exposure

    QWidgetPrivate *wPriv = m_widget->d_func();
    const bool exposed = isExposed();

    // We might get an expose event from the platform as part of
    // closing the window from ~QWidget, to support animated close
    // transitions. But at that point we no longer have a widget
    // subclass to draw a new frame, so skip the expose event.
    if (exposed && wPriv->data.in_destructor)
        return;

    if (wPriv->childrenHiddenByWState) {
        // If widgets has been previously hidden by window state change event
        // and they aren't yet shown...
        if (exposed) {
            // If the window becomes exposed...
            if (!wPriv->childrenShownByExpose) {
                // ... and they haven't been shown by this function yet - show it.
                wPriv->showChildren(true);
                QShowEvent showEvent;
                QCoreApplication::forwardEvent(m_widget, &showEvent, event);
                wPriv->childrenShownByExpose = true;
            }
        } else {
            // If the window becomes not exposed...
            if (wPriv->childrenShownByExpose) {
                // ... and child widgets was previously shown by the expose event - hide widgets again.
                // This is a workaround, because sometimes when window is minimized programmatically,
                // the QPA can notify that the window is exposed after changing window state to minimized
                // and then, the QPA can send next expose event with null exposed region (not exposed).
                wPriv->hideChildren(true);
                QHideEvent hideEvent;
                QCoreApplication::forwardEvent(m_widget, &hideEvent, event);
                wPriv->childrenShownByExpose = false;
            }
        }
    }

    if (exposed) {
        // QTBUG-39220, QTBUG-58575: set all (potentially fully obscured parent widgets) mapped.
        m_widget->setAttribute(Qt::WA_Mapped);
        for (QWidget *p = m_widget->parentWidget(); p && !p->testAttribute(Qt::WA_Mapped); p = p->parentWidget())
            p->setAttribute(Qt::WA_Mapped);
        if (!event->m_region.isNull())
            wPriv->syncBackingStore(event->m_region);
    } else {
        m_widget->setAttribute(Qt::WA_Mapped, false);
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1133, as _ZN13QWidgetWindow29handleWindowStateChangedEventEP23QWindowStateChangeEvent
inline void QWidgetWindow::handleWindowStateChangedEvent(QWindowStateChangeEvent *event)
{
    // QWindow does currently not know 'active'.
    Qt::WindowStates eventState = event->oldState();
    Qt::WindowStates widgetState = m_widget->windowState();
    Qt::WindowStates windowState = windowStates();
    if (widgetState & Qt::WindowActive)
        eventState |= Qt::WindowActive;

    // Determine the new widget state, remember maximized/full screen
    // during minimized.
    if (windowState & Qt::WindowMinimized) {
        widgetState |= Qt::WindowMinimized;
    } else {
        widgetState = windowState | (widgetState & Qt::WindowActive);
        if (windowState) // Maximized or FullScreen
            updateNormalGeometry();
    }

    // Sent event if the state changed (that is, it is not triggered by
    // QWidget::setWindowState(), which also sends an event to the widget).
    if (widgetState != Qt::WindowStates::Int(m_widget->data->window_state)) {
        m_widget->data->window_state = uint(widgetState);
        QWindowStateChangeEvent widgetEvent(eventState);
        QGuiApplication::forwardEvent(m_widget, &widgetEvent, event);
    }
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1167, as _ZN13QWidgetWindow17handleTabletEventEP12QTabletEvent
#if QT_CONFIG(tabletevent)
inline void QWidgetWindow::handleTabletEvent(QTabletEvent *event)
{
    static QPointer<QWidget> qt_tablet_target = nullptr;

    QWidget *widget = qt_tablet_target;

    if (!widget) {
        widget = m_widget->childAt(event->position());
        if (!widget)
            widget = m_widget;
        if (event->type() == QEvent::TabletPress)
            qt_tablet_target = widget;
    }

    if (widget) {
        const QPointF mapped = widget->mapFromGlobal(event->globalPosition());
        QTabletEvent ev(event->type(), event->pointingDevice(), mapped, event->globalPosition(),
                        event->pressure(), event->xTilt(), event->yTilt(), event->tangentialPressure(),
                        event->rotation(), event->z(), event->modifiers(), event->button(), event->buttons());
        ev.setTimestamp(event->timestamp());
        ev.setAccepted(false);
        QGuiApplication::forwardEvent(widget, &ev, event);
        event->setAccepted(ev.isAccepted());
    }

    if (event->type() == QEvent::TabletRelease && event->buttons() == Qt::NoButton)
        qt_tablet_target = nullptr;
}
#endif  // QT_CONFIG(tabletevent)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 1198, as _ZN13QWidgetWindow18handleGestureEventEP19QNativeGestureEvent
#if !defined(QT_NO_GESTURES)
inline void QWidgetWindow::handleGestureEvent(QNativeGestureEvent *e)
{
    // copy-pasted code to find correct widget follows:
    QObject *receiver = nullptr;
    if (auto *popup = QApplication::activePopupWidget()) {
        QWidget *popupFocusWidget = popup->focusWidget();
        receiver = popupFocusWidget ? popupFocusWidget : popup;
    }
    if (!receiver)
        receiver = QApplication::widgetAt(e->globalPosition().toPoint());
    if (!receiver)
        receiver = m_widget; // last resort

    QApplication::forwardEvent(receiver, e);
}
#endif  // !defined(QT_NO_GESTURES)

//  from src/widgets/kernel/qwidgetwindow.cpp, line 742, as _ZN13QWidgetWindow10updateSizeEv
inline bool QWidgetWindow::updateSize()
{
    bool changed = false;
    if (m_widget->testAttribute(Qt::WA_OutsideWSRange))
        return changed;
    if (m_widget->testAttribute(Qt::WA_DontShowOnScreen))
        return changed;

    if (m_widget->data->crect.size() != geometry().size()) {
        changed = true;
        m_widget->data->crect.setSize(geometry().size());
    }

    updateMargins();
    return changed;
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 759, as _ZN13QWidgetWindow13updateMarginsEv
inline void QWidgetWindow::updateMargins()
{
    // QTBUG-79147 (Windows): Bail out on resize events after closing a dialog
    // and destroying the platform window which would clear the margins.
    QTLWExtra *te = m_widget->d_func()->topData();
    if (te->window == nullptr || te->window->handle() == nullptr)
        return;
    const QMargins margins = frameMargins();
    te->posIncludesFrame= false;
    te->frameStrut.setCoords(margins.left(), margins.top(), margins.right(), margins.bottom());
    m_widget->data->fstrut_dirty = false;
}

//  from src/widgets/kernel/qwidgetwindow.cpp, line 830, as _ZN13QWidgetWindow20updateNormalGeometryEv
inline void QWidgetWindow::updateNormalGeometry()
{
    QTLWExtra *tle = m_widget->d_func()->maybeTopData();
    if (!tle)
        return;
     // Ask platform window, default to widget geometry.
    QRect normalGeometry;
    if (const QPlatformWindow *pw = handle())
        normalGeometry = QHighDpi::fromNativePixels(pw->normalGeometry(), this);
    if (!normalGeometry.isValid() && !(m_widget->windowState() & ~Qt::WindowActive))
        normalGeometry = m_widget->geometry();
    if (normalGeometry.isValid())
        tle->normalGeometry = normalGeometry;
}
//  -----------------------------------------------------------------------

//  A QWidgetWindow that Python can take functions over in. Every QWidgetWindow
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(accessibility)
typedef void * (*CuteQWidgetWindowCall0)(const void *, int *);
#endif  // QT_CONFIG(accessibility)
typedef void * (*CuteQWidgetWindowCall1)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWidgetWindowCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall3)(const void *, QCloseEvent *, int *);
typedef int (*CuteQWidgetWindowCall4)(const void *, int *);
typedef const QSurfaceFormat * (*CuteQWidgetWindowCall5)(const void *, int *);
typedef const QSize * (*CuteQWidgetWindowCall6)(const void *, int *);
typedef void (*CuteQWidgetWindowCall7)(const void *, QExposeEvent *, int *);
typedef void (*CuteQWidgetWindowCall8)(const void *, QResizeEvent *, int *);
typedef void (*CuteQWidgetWindowCall9)(const void *, QPaintEvent *, int *);
typedef void (*CuteQWidgetWindowCall10)(const void *, QMoveEvent *, int *);
typedef void (*CuteQWidgetWindowCall11)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWidgetWindowCall12)(const void *, QFocusEvent *, int *);
typedef void (*CuteQWidgetWindowCall13)(const void *, QShowEvent *, int *);
typedef void (*CuteQWidgetWindowCall14)(const void *, QHideEvent *, int *);
typedef void (*CuteQWidgetWindowCall15)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWidgetWindowCall16)(const void *, QKeyEvent *, int *);
typedef void (*CuteQWidgetWindowCall17)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetWindowCall18)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetWindowCall19)(const void *, QMouseEvent *, int *);
typedef void (*CuteQWidgetWindowCall20)(const void *, QMouseEvent *, int *);
#if QT_CONFIG(wheelevent)
typedef void (*CuteQWidgetWindowCall21)(const void *, QWheelEvent *, int *);
#endif  // QT_CONFIG(wheelevent)
typedef void (*CuteQWidgetWindowCall22)(const void *, QTouchEvent *, int *);
#if QT_CONFIG(tabletevent)
typedef void (*CuteQWidgetWindowCall23)(const void *, QTabletEvent *, int *);
#endif  // QT_CONFIG(tabletevent)
typedef void * (*CuteQWidgetWindowCall24)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWidgetWindowCall25)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall26)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall27)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall28)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall29)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWidgetWindowCall30)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWidgetWindow : public QWidgetWindow {
public:
  using QWidgetWindow::QWidgetWindow;
  void *taken[31] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow14accessibleRootEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK7QWindow11focusObjectEv")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QWindow10closeEventEP11QCloseEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface11surfaceTypeEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface6formatEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK8QSurface4sizeEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11exposeEventEP12QExposeEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow11resizeEventEP12QResizeEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow10paintEventEP11QPaintEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9moveEventEP10QMoveEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow12focusInEventEP11QFocusEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13focusOutEventEP11QFocusEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9showEventEP10QShowEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow9hideEventEP10QHideEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow13keyPressEventEP9QKeyEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15keyReleaseEventEP9QKeyEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow15mousePressEventEP11QMouseEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow17mouseReleaseEventEP11QMouseEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow21mouseDoubleClickEventEP11QMouseEvent")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QWindow14mouseMoveEventEP11QMouseEvent")) {
      taken[20] = call;
      return true;
    }
#if QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10wheelEventEP11QWheelEvent")) {
      taken[21] = call;
      return true;
    }
#endif  // QT_CONFIG(wheelevent)
    if (!std::strcmp(key, "_ZN7QWindow10touchEventEP11QTouchEvent")) {
      taken[22] = call;
      return true;
    }
#if QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZN7QWindow11tabletEventEP12QTabletEvent")) {
      taken[23] = call;
      return true;
    }
#endif  // QT_CONFIG(tabletevent)
    if (!std::strcmp(key, "_ZNK8QSurface13surfaceHandleEv")) {
      taken[24] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[25] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[26] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[27] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[28] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[29] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[30] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if QT_CONFIG(accessibility)
  //  QAccessibleInterface *QWidgetWindow::accessibleRoot() const
  QAccessibleInterface *accessibleRoot() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQWidgetWindowCall0 call = reinterpret_cast<CuteQWidgetWindowCall0>(taken[0]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QAccessibleInterface *>(given);
    }
    return QWidgetWindow::accessibleRoot();
  }
#endif  // QT_CONFIG(accessibility)

  //  QObject *QWidgetWindow::focusObject() const
  QObject *focusObject() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQWidgetWindowCall1 call = reinterpret_cast<CuteQWidgetWindowCall1>(taken[1]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetWindow::focusObject();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QWidgetWindow::event(QEvent *a0)
  bool event(QEvent *a0) override {
    if (taken[2]) {
      int handled = 0;
      CuteQWidgetWindowCall2 call = reinterpret_cast<CuteQWidgetWindowCall2>(taken[2]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QWidgetWindow::event(a0);
  }
#endif  // !defined(QT_NO_QOBJECT)

  //  void QWidgetWindow::closeEvent(QCloseEvent *a0)
  void closeEvent(QCloseEvent *a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQWidgetWindowCall3 call = reinterpret_cast<CuteQWidgetWindowCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetWindow::closeEvent(a0);
  }

  //  SurfaceType QWindow::surfaceType() const
  QSurface::SurfaceType surfaceType() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQWidgetWindowCall4 call = reinterpret_cast<CuteQWidgetWindowCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSurface::SurfaceType>(given);
    }
    return QWindow::surfaceType();
  }

  //  QSurfaceFormat QWindow::format() const
  QSurfaceFormat format() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQWidgetWindowCall5 call = reinterpret_cast<CuteQWidgetWindowCall5>(taken[5]);
      const QSurfaceFormat * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::format();
  }

  //  QSize QWindow::size() const
  QSize size() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQWidgetWindowCall6 call = reinterpret_cast<CuteQWidgetWindowCall6>(taken[6]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWindow::size();
  }

  //  void QWindow::exposeEvent(QExposeEvent *a0)
  void exposeEvent(QExposeEvent *a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWidgetWindowCall7 call = reinterpret_cast<CuteQWidgetWindowCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::exposeEvent(a0);
  }

  //  void QWindow::resizeEvent(QResizeEvent *a0)
  void resizeEvent(QResizeEvent *a0) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWidgetWindowCall8 call = reinterpret_cast<CuteQWidgetWindowCall8>(taken[8]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::resizeEvent(a0);
  }

  //  void QWindow::paintEvent(QPaintEvent *a0)
  void paintEvent(QPaintEvent *a0) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWidgetWindowCall9 call = reinterpret_cast<CuteQWidgetWindowCall9>(taken[9]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::paintEvent(a0);
  }

  //  void QWindow::moveEvent(QMoveEvent *a0)
  void moveEvent(QMoveEvent *a0) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWidgetWindowCall10 call = reinterpret_cast<CuteQWidgetWindowCall10>(taken[10]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::moveEvent(a0);
  }

  //  void QWindow::focusInEvent(QFocusEvent *a0)
  void focusInEvent(QFocusEvent *a0) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWidgetWindowCall11 call = reinterpret_cast<CuteQWidgetWindowCall11>(taken[11]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusInEvent(a0);
  }

  //  void QWindow::focusOutEvent(QFocusEvent *a0)
  void focusOutEvent(QFocusEvent *a0) override {
    if (taken[12]) {
      int handled = 0;
      CuteQWidgetWindowCall12 call = reinterpret_cast<CuteQWidgetWindowCall12>(taken[12]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::focusOutEvent(a0);
  }

  //  void QWindow::showEvent(QShowEvent *a0)
  void showEvent(QShowEvent *a0) override {
    if (taken[13]) {
      int handled = 0;
      CuteQWidgetWindowCall13 call = reinterpret_cast<CuteQWidgetWindowCall13>(taken[13]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::showEvent(a0);
  }

  //  void QWindow::hideEvent(QHideEvent *a0)
  void hideEvent(QHideEvent *a0) override {
    if (taken[14]) {
      int handled = 0;
      CuteQWidgetWindowCall14 call = reinterpret_cast<CuteQWidgetWindowCall14>(taken[14]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::hideEvent(a0);
  }

  //  void QWindow::keyPressEvent(QKeyEvent *a0)
  void keyPressEvent(QKeyEvent *a0) override {
    if (taken[15]) {
      int handled = 0;
      CuteQWidgetWindowCall15 call = reinterpret_cast<CuteQWidgetWindowCall15>(taken[15]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyPressEvent(a0);
  }

  //  void QWindow::keyReleaseEvent(QKeyEvent *a0)
  void keyReleaseEvent(QKeyEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQWidgetWindowCall16 call = reinterpret_cast<CuteQWidgetWindowCall16>(taken[16]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::keyReleaseEvent(a0);
  }

  //  void QWindow::mousePressEvent(QMouseEvent *a0)
  void mousePressEvent(QMouseEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQWidgetWindowCall17 call = reinterpret_cast<CuteQWidgetWindowCall17>(taken[17]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mousePressEvent(a0);
  }

  //  void QWindow::mouseReleaseEvent(QMouseEvent *a0)
  void mouseReleaseEvent(QMouseEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQWidgetWindowCall18 call = reinterpret_cast<CuteQWidgetWindowCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseReleaseEvent(a0);
  }

  //  void QWindow::mouseDoubleClickEvent(QMouseEvent *a0)
  void mouseDoubleClickEvent(QMouseEvent *a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQWidgetWindowCall19 call = reinterpret_cast<CuteQWidgetWindowCall19>(taken[19]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseDoubleClickEvent(a0);
  }

  //  void QWindow::mouseMoveEvent(QMouseEvent *a0)
  void mouseMoveEvent(QMouseEvent *a0) override {
    if (taken[20]) {
      int handled = 0;
      CuteQWidgetWindowCall20 call = reinterpret_cast<CuteQWidgetWindowCall20>(taken[20]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::mouseMoveEvent(a0);
  }

#if QT_CONFIG(wheelevent)
  //  void QWindow::wheelEvent(QWheelEvent *a0)
  void wheelEvent(QWheelEvent *a0) override {
    if (taken[21]) {
      int handled = 0;
      CuteQWidgetWindowCall21 call = reinterpret_cast<CuteQWidgetWindowCall21>(taken[21]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::wheelEvent(a0);
  }
#endif  // QT_CONFIG(wheelevent)

  //  void QWindow::touchEvent(QTouchEvent *a0)
  void touchEvent(QTouchEvent *a0) override {
    if (taken[22]) {
      int handled = 0;
      CuteQWidgetWindowCall22 call = reinterpret_cast<CuteQWidgetWindowCall22>(taken[22]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::touchEvent(a0);
  }

#if QT_CONFIG(tabletevent)
  //  void QWindow::tabletEvent(QTabletEvent *a0)
  void tabletEvent(QTabletEvent *a0) override {
    if (taken[23]) {
      int handled = 0;
      CuteQWidgetWindowCall23 call = reinterpret_cast<CuteQWidgetWindowCall23>(taken[23]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWindow::tabletEvent(a0);
  }
#endif  // QT_CONFIG(tabletevent)

  //  QPlatformSurface *QWindow::surfaceHandle() const
  QPlatformSurface *surfaceHandle() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQWidgetWindowCall24 call = reinterpret_cast<CuteQWidgetWindowCall24>(taken[24]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QPlatformSurface *>(given);
    }
    return QWindow::surfaceHandle();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[25]) {
      int handled = 0;
      CuteQWidgetWindowCall25 call = reinterpret_cast<CuteQWidgetWindowCall25>(taken[25]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[26]) {
      int handled = 0;
      CuteQWidgetWindowCall26 call = reinterpret_cast<CuteQWidgetWindowCall26>(taken[26]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[27]) {
      int handled = 0;
      CuteQWidgetWindowCall27 call = reinterpret_cast<CuteQWidgetWindowCall27>(taken[27]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[28]) {
      int handled = 0;
      CuteQWidgetWindowCall28 call = reinterpret_cast<CuteQWidgetWindowCall28>(taken[28]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[29]) {
      int handled = 0;
      CuteQWidgetWindowCall29 call = reinterpret_cast<CuteQWidgetWindowCall29>(taken[29]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[30]) {
      int handled = 0;
      CuteQWidgetWindowCall30 call = reinterpret_cast<CuteQWidgetWindowCall30>(taken[30]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWidgetWindow::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QWidgetWindow10metaObjectEv(
    const QWidgetWindow *self) {
  return self->metaObject();
}

//  void *QWidgetWindow::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN13QWidgetWindow11qt_metacastEPKc(
    QWidgetWindow *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWidgetWindow::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN13QWidgetWindow11qt_metacallEN11QMetaObject4CallEiPPv(
    QWidgetWindow *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QWidgetWindowPrivate *QWidgetWindow::d_func()
extern "C" Q_DECL_EXPORT
QWidgetWindowPrivate *ritual_ZN13QWidgetWindow6d_funcEv(
    QWidgetWindow *self) {
  return self->d_func();
}

//  const QWidgetWindowPrivate *QWidgetWindow::d_func() const
extern "C" Q_DECL_EXPORT
const QWidgetWindowPrivate *ritual_ZNK13QWidgetWindow6d_funcEv(
    const QWidgetWindow *self) {
  return self->d_func();
}

//  QWidgetWindow::~QWidgetWindow()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindowD1Ev(QWidgetWindow *self) {
  delete self;
}

//  QWidget *QWidgetWindow::widget() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QWidgetWindow6widgetEv(const QWidgetWindow *self) {
  return self->widget();
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QWidgetWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_ZNK13QWidgetWindow14accessibleRootEv(
    const QWidgetWindow *self) {
  return self->accessibleRoot();
}
#endif  // QT_CONFIG(accessibility)

//  QObject *QWidgetWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK13QWidgetWindow11focusObjectEv(
    const QWidgetWindow *self) {
  return self->focusObject();
}

//  void QWidgetWindow::focusNextPrevChild(QWidget *widget, bool next)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow18focusNextPrevChildEP7QWidgetb(
    QWidget *widget,
    bool next) {
  QWidgetWindow::focusNextPrevChild(widget, next);
}

//  bool QWidgetWindow::event(QEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWidgetWindow5eventEP6QEvent(
    QWidgetWindow *self,
    QEvent *a0) {
  return self->event(a0);
}

//  void QWidgetWindow::closeEvent(QCloseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow10closeEventEP11QCloseEvent(
    QWidgetWindow *self,
    QCloseEvent *a0) {
  self->closeEvent(a0);
}

//  void QWidgetWindow::handleNonClientAreaMouseEvent(QMouseEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow29handleNonClientAreaMouseEventEP11QMouseEvent(
    QWidgetWindow *self,
    QMouseEvent *a0) {
  self->handleNonClientAreaMouseEvent(a0);
}

//  void QWidgetWindow::handleTouchEvent(QTouchEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow16handleTouchEventEP11QTouchEvent(
    QWidgetWindow *self,
    QTouchEvent *a0) {
  self->handleTouchEvent(a0);
}

//  void QWidgetWindow::handleMoveEvent(QMoveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow15handleMoveEventEP10QMoveEvent(
    QWidgetWindow *self,
    QMoveEvent *a0) {
  self->handleMoveEvent(a0);
}

//  void QWidgetWindow::handleResizeEvent(QResizeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow17handleResizeEventEP12QResizeEvent(
    QWidgetWindow *self,
    QResizeEvent *a0) {
  self->handleResizeEvent(a0);
}

#if QT_CONFIG(draganddrop)
//  void QWidgetWindow::handleDragEnterEvent(QDragMoveEvent *a0, QWidget
//      *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow20handleDragEnterEventEP14QDragMoveEventP7QWidget(
    QWidgetWindow *self,
    QDragMoveEvent *a0,
    QWidget *widget) {
  self->handleDragEnterEvent(a0, widget);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWidgetWindow::handleDragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow20handleDragLeaveEventEP15QDragLeaveEvent(
    QWidgetWindow *self,
    QDragLeaveEvent *a0) {
  self->handleDragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QWidgetWindow::handleDropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow15handleDropEventEP10QDropEvent(
    QWidgetWindow *self,
    QDropEvent *a0) {
  self->handleDropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

//  void QWidgetWindow::handleExposeEvent(QExposeEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow17handleExposeEventEP12QExposeEvent(
    QWidgetWindow *self,
    QExposeEvent *a0) {
  self->handleExposeEvent(a0);
}

//  void QWidgetWindow::handleWindowStateChangedEvent(QWindowStateChangeEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow29handleWindowStateChangedEventEP23QWindowStateChangeEvent(
    QWidgetWindow *self,
    QWindowStateChangeEvent *event) {
  self->handleWindowStateChangedEvent(event);
}

//  bool QWidgetWindow::nativeEvent(const QByteArray &eventType, void
//      *message, qintptr *result)
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWidgetWindow11nativeEventERK10QByteArrayPvPx(
    QWidgetWindow *self,
    const QByteArray *eventType,
    void *message,
    qintptr *result) {
  return self->nativeEvent(*eventType, message, result);
}

#if QT_CONFIG(tabletevent)
//  void QWidgetWindow::handleTabletEvent(QTabletEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow17handleTabletEventEP12QTabletEvent(
    QWidgetWindow *self,
    QTabletEvent *a0) {
  self->handleTabletEvent(a0);
}
#endif  // QT_CONFIG(tabletevent)

#if !defined(QT_NO_GESTURES)
//  void QWidgetWindow::handleGestureEvent(QNativeGestureEvent *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow18handleGestureEventEP19QNativeGestureEvent(
    QWidgetWindow *self,
    QNativeGestureEvent *a0) {
  self->handleGestureEvent(a0);
}
#endif  // !defined(QT_NO_GESTURES)

//  void QWidgetWindow::updateObjectName()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow16updateObjectNameEv(QWidgetWindow *self) {
  const QObject *object = self;
  const QMetaObject *meta = object->metaObject();
  for (const QMetaObject *up = meta; up; up = up->superClass()) {
    if (!qstrcmp(up->className(), "QWidgetWindow")) {
      meta = up;
      break;
    }
  }
  const int index = meta->indexOfMethod(
      QMetaObject::normalizedSignature(
          "updateObjectName()").constData());
  if (index < 0)
    qFatal("cutienator: the meta-object of %s has no %s",
           meta->className(), "updateObjectName()");
  void *arguments[] = {
      nullptr,
  };
  static_cast<QObject *>(self)->qt_metacall(
      QMetaObject::InvokeMetaMethod, index, arguments);
}

//  bool QWidgetWindow::updateSize()
extern "C" Q_DECL_EXPORT
bool ritual_ZN13QWidgetWindow10updateSizeEv(QWidgetWindow *self) {
  return self->updateSize();
}

//  void QWidgetWindow::updateMargins()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow13updateMarginsEv(QWidgetWindow *self) {
  self->updateMargins();
}

//  void QWidgetWindow::updateNormalGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QWidgetWindow20updateNormalGeometryEv(QWidgetWindow *self) {
  self->updateNormalGeometry();
}

//  a Python function taken by a CuteQWidgetWindow, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWidgetWindow(
    QWidgetWindow *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWidgetWindow *>(self)->take(key, call);
}

#if QT_CONFIG(accessibility)
//  QAccessibleInterface *QWidgetWindow::accessibleRoot() const
extern "C" Q_DECL_EXPORT
QAccessibleInterface *ritual_own_ZNK13QWidgetWindow14accessibleRootEv(
    const QWidgetWindow *self) {
  return self->QWidgetWindow::accessibleRoot();
}
#endif  // QT_CONFIG(accessibility)

//  QObject *QWidgetWindow::focusObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_own_ZNK13QWidgetWindow11focusObjectEv(
    const QWidgetWindow *self) {
  return self->QWidgetWindow::focusObject();
}
