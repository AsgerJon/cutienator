//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicsproxywidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicsproxywidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicsproxywidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qglobal.h"
#include <QtCore/qdebug.h>
#include <QtCore/qnumeric.h>
#include "qgraphicswidget_p.h"
#include "qgraphicslayoutitem_p.h"
#include "qgraphicslayout.h"
#include "qgraphicsscene_p.h"
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/QStyleOptionTitleBar>
#include <QtWidgets/QGraphicsSceneMouseEvent>
#include "qglobal.h"
#include "qgraphicslayout.h"
#include "qgraphicsproxywidget.h"
#include "private/qgraphicsproxywidget_p.h"
#include "private/qwidget_p.h"
#include "private/qapplication_p.h"
#include <QtCore/qdebug.h>
#include <QtGui/qevent.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicssceneevent.h>
#include <QtWidgets/qlayout.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qgraphicsview.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(textedit)
#include <QtWidgets/qtextedit.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 806, as _ZN22QGraphicsWidgetPrivate10resetWidthEv
inline void QGraphicsWidgetPrivate::resetWidth()
{
    Q_Q(QGraphicsWidget);
    q->setGeometry(QRectF(q->x(), q->y(), 0, height()));
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 829, as _ZN22QGraphicsWidgetPrivate11resetHeightEv
inline void QGraphicsWidgetPrivate::resetHeight()
{
    Q_Q(QGraphicsWidget);
    q->setGeometry(QRectF(q->x(), q->y(), width(), 0));
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 216, as _ZN22QGraphicsWidgetPrivate11resolveFontEj
inline void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
{
    Q_Q(QGraphicsWidget);
    inheritedFontResolveMask = inheritedMask;
    if (QGraphicsWidget *p = q->parentWidget())
        inheritedFontResolveMask |= p->d_func()->inheritedFontResolveMask;
    QFont naturalFont = naturalWidgetFont();
    QFont resolvedFont = font.resolve(naturalFont);
    updateFont(resolvedFont);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 121, as _ZN22QGraphicsWidgetPrivate14resolvePaletteEj
inline void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
{
    inheritedPaletteResolveMask = inheritedMask;
    QPalette naturalPalette = naturalWidgetPalette();
    QPalette resolvedPalette = palette.resolve(naturalPalette);
    updatePalette(resolvedPalette);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 795, as _ZN22QGraphicsWidgetPrivate8setWidthEd
inline void QGraphicsWidgetPrivate::setWidth(qreal w)
{
    if (qIsNaN(w))
        return;
    Q_Q(QGraphicsWidget);
    if (q->geometry().width() == w)
        return;

    q->setGeometry(QRectF(q->x(), q->y(), w, height()));
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 818, as _ZN22QGraphicsWidgetPrivate9setHeightEd
inline void QGraphicsWidgetPrivate::setHeight(qreal h)
{
    if (qIsNaN(h))
        return;
    Q_Q(QGraphicsWidget);
    if (q->geometry().height() == h)
        return;

    q->setGeometry(QRectF(q->x(), q->y(), width(), h));
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 55, as _ZN22QGraphicsWidgetPrivateC2Ev
inline QGraphicsWidgetPrivate::QGraphicsWidgetPrivate()
    : margins(nullptr),
      layout(nullptr),
      inheritedPaletteResolveMask(0),
      inheritedFontResolveMask(0),
      inSetGeometry(false),
      polished(false),
      inSetPos(false),
      autoFillBackground(false),
      focusPolicy(Qt::NoFocus),
      focusNext(nullptr),
      focusPrev(nullptr),
      windowFlags(),
      windowData(nullptr),
      setWindowFrameMargins(false),
      windowFrameMargins(nullptr)
{
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 74, as _ZN22QGraphicsWidgetPrivateD2Ev
inline QGraphicsWidgetPrivate::~QGraphicsWidgetPrivate()
{
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 789, as _ZNK22QGraphicsWidgetPrivate5widthEv
inline qreal QGraphicsWidgetPrivate::width() const
{
    Q_Q(const QGraphicsWidget);
    return q->geometry().width();
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 812, as _ZNK22QGraphicsWidgetPrivate6heightEv
inline qreal QGraphicsWidgetPrivate::height() const
{
    Q_Q(const QGraphicsWidget);
    return q->geometry().height();
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 183, as _ZN27QGraphicsProxyWidgetPrivateD1Ev
inline QGraphicsProxyWidgetPrivate::~QGraphicsProxyWidgetPrivate()
{
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 190, as _ZN27QGraphicsProxyWidgetPrivate4initEv
inline void QGraphicsProxyWidgetPrivate::init()
{
    Q_Q(QGraphicsProxyWidget);
    q->setFocusPolicy(Qt::WheelFocus);
    q->setAcceptDrops(true);
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 216, as _ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QGraphicsSceneMouseEvent
inline void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(QGraphicsSceneMouseEvent *event)
{
    if (!event || !widget || !widget->isVisible())
        return;
    Q_Q(QGraphicsProxyWidget);

    // Find widget position and receiver.
    QPointF pos = event->pos();
    QPointer<QWidget> alienWidget = widget->childAt(pos);
    QPointer<QWidget> receiver =  alienWidget ? alienWidget : widget;

    if (QWidgetPrivate::nearestGraphicsProxyWidget(receiver) != q)
        return; //another proxywidget will handle the events

    // Translate QGraphicsSceneMouse events to QMouseEvents.
    QEvent::Type type = QEvent::None;
    switch (event->type()) {
    case QEvent::GraphicsSceneMousePress:
        type = QEvent::MouseButtonPress;
        if (!embeddedMouseGrabber)
            embeddedMouseGrabber = receiver;
        else
            receiver = embeddedMouseGrabber;
        break;
    case QEvent::GraphicsSceneMouseRelease:
        type = QEvent::MouseButtonRelease;
        if (embeddedMouseGrabber)
            receiver = embeddedMouseGrabber;
        break;
    case QEvent::GraphicsSceneMouseDoubleClick:
        type = QEvent::MouseButtonDblClick;
        if (!embeddedMouseGrabber)
            embeddedMouseGrabber = receiver;
        else
            receiver = embeddedMouseGrabber;
        break;
    case QEvent::GraphicsSceneMouseMove:
        type = QEvent::MouseMove;
        if (embeddedMouseGrabber)
            receiver = embeddedMouseGrabber;
        break;
    default:
        Q_ASSERT_X(false, "QGraphicsProxyWidget", "internal error");
        break;
    }

    if (!lastWidgetUnderMouse) {
        QApplicationPrivate::dispatchEnterLeave(embeddedMouseGrabber ? embeddedMouseGrabber : receiver, nullptr, event->screenPos());
        lastWidgetUnderMouse = receiver;
    }

    // Map event position from us to the receiver
    pos = mapToReceiver(pos, receiver);

    // Send mouse event.
    QMouseEvent mouseEvent(type, pos, receiver->mapTo(receiver->topLevelWidget(), pos),
                           receiver->mapToGlobal(pos),
                           event->button(), event->buttons(), event->modifiers(), event->source());
    mouseEvent.setTimestamp(event->timestamp());

    QWidget *embeddedMouseGrabberPtr = (QWidget *)embeddedMouseGrabber;
    QApplicationPrivate::sendMouseEvent(receiver, &mouseEvent, alienWidget, widget,
                                        &embeddedMouseGrabberPtr, lastWidgetUnderMouse, event->spontaneous());
    embeddedMouseGrabber = embeddedMouseGrabberPtr;

    // Handle enter/leave events when last button is released from mouse
    // grabber child widget.
    if (embeddedMouseGrabber && type == QEvent::MouseButtonRelease && !event->buttons()) {
        Q_Q(QGraphicsProxyWidget);
        if (q->rect().contains(event->pos()) && q->acceptHoverEvents())
            lastWidgetUnderMouse = alienWidget ? alienWidget : widget;
        else // released on the frame our outside the item, or doesn't accept hover events.
            lastWidgetUnderMouse = nullptr;

        QApplicationPrivate::dispatchEnterLeave(lastWidgetUnderMouse, embeddedMouseGrabber, event->screenPos());
        embeddedMouseGrabber = nullptr;

#ifndef QT_NO_CURSOR
        // ### Restore the cursor, don't override it.
        if (!lastWidgetUnderMouse)
            q->unsetCursor();
#endif
    }

#ifndef QT_NO_CURSOR
    // Keep cursor in sync
    if (lastWidgetUnderMouse) {
        QCursor widgetsCursor = lastWidgetUnderMouse->cursor();
        if (q->cursor() != widgetsCursor)
            q->setCursor(widgetsCursor);
    }
#endif

    event->setAccepted(mouseEvent.isAccepted());
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 200, as _ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QGraphicsSceneHoverEvent
inline void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(QGraphicsSceneHoverEvent *event)
{
    QGraphicsSceneMouseEvent mouseEvent(QEvent::GraphicsSceneMouseMove);
    mouseEvent.setPos(event->pos());
    mouseEvent.setScreenPos(event->screenPos());
    mouseEvent.setButton(Qt::NoButton);
    mouseEvent.setButtons({ });
    mouseEvent.setModifiers(event->modifiers());
    mouseEvent.setTimestamp(event->timestamp());
    sendWidgetMouseEvent(&mouseEvent);
    event->setAccepted(mouseEvent.isAccepted());
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 312, as _ZN27QGraphicsProxyWidgetPrivate18sendWidgetKeyEventEP9QKeyEvent
inline void QGraphicsProxyWidgetPrivate::sendWidgetKeyEvent(QKeyEvent *event)
{
    Q_Q(QGraphicsProxyWidget);
    if (!event || !widget || !widget->isVisible())
        return;

    QPointer<QWidget> receiver = widget->focusWidget();
    if (!receiver)
        receiver = widget;
    Q_ASSERT(receiver);

    do {
        bool res = QCoreApplication::sendEvent(receiver, event);
        if ((res && event->isAccepted()) || (q->isWindow() && receiver == widget))
            break;
        receiver = receiver->parentWidget();
    } while (receiver);
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 571, as _ZN27QGraphicsProxyWidgetPrivate16setWidget_helperEP7QWidgetb
inline void QGraphicsProxyWidgetPrivate::setWidget_helper(QWidget *newWidget, bool autoShow)
{
    Q_Q(QGraphicsProxyWidget);
    if (newWidget == widget)
        return;
    if (widget) {
        QObject::disconnect(widget, SIGNAL(destroyed()), q, SLOT(_q_removeWidgetSlot()));
        widget->removeEventFilter(q);
        widget->setAttribute(Qt::WA_DontShowOnScreen, false);
        widget->d_func()->extra->proxyWidget = nullptr;
        resolveFont(inheritedFontResolveMask);
        resolvePalette(inheritedPaletteResolveMask);
        widget->update();

        const auto childItems = q->childItems();
        for (QGraphicsItem *child : childItems) {
            if (child->d_ptr->isProxyWidget()) {
                QGraphicsProxyWidget *childProxy = static_cast<QGraphicsProxyWidget *>(child);
                QWidget *parent = childProxy->widget();
                while (parent && parent->parentWidget()) {
                    if (parent == widget)
                        break;
                    parent = parent->parentWidget();
                }
                if (!childProxy->widget() || parent != widget)
                    continue;
                childProxy->setWidget(nullptr);
                delete childProxy;
            }
        }

        widget = nullptr;
#ifndef QT_NO_CURSOR
        q->unsetCursor();
#endif
        q->setAcceptHoverEvents(false);
        if (!newWidget)
            q->update();
    }
    if (!newWidget)
        return;
    if (!newWidget->isWindow()) {
        const auto &extra = newWidget->parentWidget()->d_func()->extra;
        if (!extra || !extra->proxyWidget)  {
            qWarning("QGraphicsProxyWidget::setWidget: cannot embed widget %p "
                     "which is not a toplevel widget, and is not a child of an embedded widget", newWidget);
            return;
        }
    }

    // Register this proxy within the widget's private.
    // ### This is a bit backdoorish
    QWExtra *extra = newWidget->d_func()->extra.get();
    if (!extra) {
        newWidget->d_func()->createExtra();
        extra = newWidget->d_func()->extra.get();
    }
    QGraphicsProxyWidget **proxyWidget = &extra->proxyWidget;
    if (*proxyWidget) {
        if (*proxyWidget != q) {
            qWarning("QGraphicsProxyWidget::setWidget: cannot embed widget %p"
                        "; already embedded", newWidget);
        }
        return;
    }
    *proxyWidget = q;

    newWidget->setAttribute(Qt::WA_DontShowOnScreen);
    newWidget->ensurePolished();
    // Do not wait for this widget to close before the app closes ###
    // shouldn't this widget inherit the attribute?
    newWidget->setAttribute(Qt::WA_QuitOnClose, false);
    q->setAcceptHoverEvents(true);

    if (newWidget->testAttribute(Qt::WA_NoSystemBackground))
        q->setAttribute(Qt::WA_NoSystemBackground);
    if (newWidget->testAttribute(Qt::WA_OpaquePaintEvent))
        q->setAttribute(Qt::WA_OpaquePaintEvent);

    widget = newWidget;

    // Changes only go from the widget to the proxy.
    enabledChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;
    visibleChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;
    posChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;
    sizeChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;

    if ((autoShow && !newWidget->testAttribute(Qt::WA_WState_ExplicitShowHide)) || !newWidget->testAttribute(Qt::WA_WState_Hidden)) {
        newWidget->show();
    }

    // Copy the state from the widget onto the proxy.
#ifndef QT_NO_CURSOR
    if (newWidget->testAttribute(Qt::WA_SetCursor))
        q->setCursor(widget->cursor());
#endif
    q->setEnabled(newWidget->isEnabled());
    q->setVisible(newWidget->isVisible());
    q->setLayoutDirection(newWidget->layoutDirection());
    if (newWidget->testAttribute(Qt::WA_SetStyle))
        q->setStyle(widget->style());

    resolveFont(inheritedFontResolveMask);
    resolvePalette(inheritedPaletteResolveMask);

    if (!newWidget->testAttribute(Qt::WA_Resized))
        newWidget->adjustSize();

    q->setContentsMargins(newWidget->contentsMargins());
    q->setWindowTitle(newWidget->windowTitle());

    // size policies and constraints..
    q->setSizePolicy(newWidget->sizePolicy());
    QSize sz = newWidget->minimumSize();
    q->setMinimumSize(sz.isNull() ? QSizeF() : QSizeF(sz));
    sz = newWidget->maximumSize();
    q->setMaximumSize(sz.isNull() ? QSizeF() : QSizeF(sz));

    updateProxyGeometryFromWidget();

    updateProxyInputMethodAcceptanceFromWidget();

    // Hook up the event filter to keep the state up to date.
    newWidget->installEventFilter(q);
    QObject::connect(newWidget, SIGNAL(destroyed()), q, SLOT(_q_removeWidgetSlot()));

    // Changes no longer go only from the widget to the proxy.
    enabledChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
    visibleChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
    posChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
    sizeChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 334, as _ZN27QGraphicsProxyWidgetPrivate20removeSubFocusHelperEP7QWidgetN2Qt11FocusReasonE
inline void QGraphicsProxyWidgetPrivate::removeSubFocusHelper(QWidget *widget, Qt::FocusReason reason)
{
    QFocusEvent event(QEvent::FocusOut, reason);
    QPointer<QWidget> widgetGuard = widget;
    QCoreApplication::sendEvent(widget, &event);
    if (widgetGuard && event.isAccepted())
        QCoreApplication::sendEvent(widget->style(), &event);
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 382, as _ZN27QGraphicsProxyWidgetPrivate19_q_removeWidgetSlotEv
inline void QGraphicsProxyWidgetPrivate::_q_removeWidgetSlot()
{
    Q_Q(QGraphicsProxyWidget);
    if (!widget.isNull()) {
        if (const auto &extra = widget->d_func()->extra)
            extra->proxyWidget = nullptr;
    }
    widget = nullptr;
    delete q;
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 457, as _ZN27QGraphicsProxyWidgetPrivate14embedSubWindowEP7QWidget
inline void QGraphicsProxyWidgetPrivate::embedSubWindow(QWidget *subWin)
{
    const auto &extra = subWin->d_func()->extra;
    if (!extra || !extra->proxyWidget) {
        QGraphicsProxyWidget *subProxy = new QGraphicsProxyWidget(q_func(), subWin->windowFlags());
        subProxy->d_func()->setWidget_helper(subWin, false);
    }
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 473, as _ZN27QGraphicsProxyWidgetPrivate16unembedSubWindowEP7QWidget
inline void QGraphicsProxyWidgetPrivate::unembedSubWindow(QWidget *subWin)
{
    for (QGraphicsItem *child : std::as_const(children)) {
        if (child->isWidget()) {
            if (QGraphicsProxyWidget *proxy = qobject_cast<QGraphicsProxyWidget *>(static_cast<QGraphicsWidget *>(child))) {
                if (proxy->widget() == subWin) {
                    proxy->setWidget(nullptr);
                    scene->removeItem(proxy);
                    delete proxy;
                    return;
                }
            }
        }
    }
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 489, as _ZNK27QGraphicsProxyWidgetPrivate13isProxyWidgetEv
inline bool QGraphicsProxyWidgetPrivate::isProxyWidget() const
{
    return true;
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 396, as _ZN27QGraphicsProxyWidgetPrivate29updateWidgetGeometryFromProxyEv
inline void QGraphicsProxyWidgetPrivate::updateWidgetGeometryFromProxy()
{
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 403, as _ZN27QGraphicsProxyWidgetPrivate29updateProxyGeometryFromWidgetEv
inline void QGraphicsProxyWidgetPrivate::updateProxyGeometryFromWidget()
{
    Q_Q(QGraphicsProxyWidget);
    if (!widget)
        return;

    QRectF widgetGeometry = widget->geometry();
    QWidget *parentWidget = widget->parentWidget();
    if (widget->isWindow()) {
        QGraphicsProxyWidget *proxyParent = nullptr;
        if (parentWidget && (proxyParent = qobject_cast<QGraphicsProxyWidget *>(q->parentWidget()))) {
            // Nested window proxy (e.g., combobox popup), map widget to the
            // parent widget's global coordinates, and map that to the parent
            // proxy's child coordinates.
            widgetGeometry.moveTo(proxyParent->subWidgetRect(parentWidget).topLeft()
                                  + parentWidget->mapFromGlobal(widget->pos()));
        }
    }

    // Adjust to size hint if the widget has never been resized.
    if (!widget->size().isValid())
        widgetGeometry.setSize(widget->sizeHint());

    // Assign new geometry.
    posChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;
    sizeChangeMode = QGraphicsProxyWidgetPrivate::WidgetToProxyMode;
    q->setGeometry(widgetGeometry);
    posChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
    sizeChangeMode = QGraphicsProxyWidgetPrivate::NoMode;
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 437, as _ZN27QGraphicsProxyWidgetPrivate42updateProxyInputMethodAcceptanceFromWidgetEv
inline void QGraphicsProxyWidgetPrivate::updateProxyInputMethodAcceptanceFromWidget()
{
    Q_Q(QGraphicsProxyWidget);
    if (!widget)
        return;

    QWidget *focusWidget = widget->focusWidget();
    if (!focusWidget)
        focusWidget = widget;
    q->setFlag(QGraphicsItem::ItemAcceptsInputMethod,
               focusWidget->testAttribute(Qt::WA_InputMethodEnabled));
}

//  from src/widgets/graphicsview/qgraphicsproxywidget.cpp, line 497, as _ZNK27QGraphicsProxyWidgetPrivate13mapToReceiverERK7QPointFPK7QWidget
inline QPointF QGraphicsProxyWidgetPrivate::mapToReceiver(const QPointF &pos, const QWidget *receiver) const
{
    QPointF p = pos;
    // Map event position from us to the receiver, preserving its
    // precision (don't use QWidget::mapFrom here).
    while (receiver && receiver != widget) {
        p -= QPointF(receiver->pos());
        receiver = receiver->parentWidget();
    }
    return p;
}
//  -----------------------------------------------------------------------

//  A QGraphicsProxyWidgetPrivate that Python can take functions over in. Every QGraphicsProxyWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsProxyWidgetPrivateCall0)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall1)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall2)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsProxyWidgetPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall4)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsProxyWidgetPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall7)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall10)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall13)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsProxyWidgetPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsProxyWidgetPrivate : public QGraphicsProxyWidgetPrivate {
public:
  using QGraphicsProxyWidgetPrivate::QGraphicsProxyWidgetPrivate;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate13isProxyWidgetEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate14resolvePaletteEj")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resolveFontEj")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate5widthEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate8setWidthEd")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate10resetWidthEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate6heightEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate9setHeightEd")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resetHeightEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate16transformChangedEv")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate18subFocusItemChangeEv")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate20focusScopeItemChangeEb")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate18siblingOrderChangeEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
    return false;
  }

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsProxyWidgetPrivate::isProxyWidget() const
  bool isProxyWidget() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall0 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsProxyWidgetPrivate::isProxyWidget();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
  void resolvePalette(uint inheritedMask) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall1 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall1>(taken[1]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resolvePalette(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
  void resolveFont(uint inheritedMask) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall2 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall2>(taken[2]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resolveFont(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsWidgetPrivate::width() const
  qreal width() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall3 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall3>(taken[3]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidgetPrivate::width();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::setWidth(qreal a0)
  void setWidth(qreal a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall4 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::setWidth(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resetWidth()
  void resetWidth() override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall5 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resetWidth();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsWidgetPrivate::height() const
  qreal height() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall6 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall6>(taken[6]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidgetPrivate::height();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::setHeight(qreal a0)
  void setHeight(qreal a0) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall7 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall7>(taken[7]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::setHeight(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resetHeight()
  void resetHeight() override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall8 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resetHeight();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::updateSceneTransformFromParent()
  void updateSceneTransformFromParent() override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall9 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::updateSceneTransformFromParent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
  void setPosHelper(const QPointF &pos) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall10 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall10>(taken[10]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::setPosHelper(pos);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::transformChanged()
  void transformChanged() override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall11 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::transformChanged();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::subFocusItemChange()
  void subFocusItemChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall12 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall12>(taken[12]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::subFocusItemChange();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::focusScopeItemChange(bool isSubFocusItem)
  void focusScopeItemChange(bool isSubFocusItem) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall13 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall13>(taken[13]);
      call(this, isSubFocusItem, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::focusScopeItemChange(isSubFocusItem);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::siblingOrderChange()
  void siblingOrderChange() override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsProxyWidgetPrivateCall14 call = reinterpret_cast<CuteQGraphicsProxyWidgetPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::siblingOrderChange();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsProxyWidget *QGraphicsProxyWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN27QGraphicsProxyWidgetPrivate6q_funcEv(
    QGraphicsProxyWidgetPrivate *self) {
  return self->q_func();
}

//  const QGraphicsProxyWidget *QGraphicsProxyWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsProxyWidget *ritual_ZNK27QGraphicsProxyWidgetPrivate6q_funcEv(
    const QGraphicsProxyWidgetPrivate *self) {
  return self->q_func();
}

//  QGraphicsProxyWidgetPrivate::~QGraphicsProxyWidgetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivateD1Ev(
    QGraphicsProxyWidgetPrivate *self) {
  delete self;
}

//  void QGraphicsProxyWidgetPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate4initEv(
    QGraphicsProxyWidgetPrivate *self) {
  self->init();
}

//  void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(QGraphicsSceneMous
//      eEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsProxyWidgetPrivate *self,
    QGraphicsSceneMouseEvent *event) {
  self->sendWidgetMouseEvent(event);
}

//  void QGraphicsProxyWidgetPrivate::sendWidgetMouseEvent(QGraphicsSceneHove
//      rEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate20sendWidgetMouseEventEP24QGraphicsSceneHoverEvent(
    QGraphicsProxyWidgetPrivate *self,
    QGraphicsSceneHoverEvent *event) {
  self->sendWidgetMouseEvent(event);
}

//  void QGraphicsProxyWidgetPrivate::sendWidgetKeyEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate18sendWidgetKeyEventEP9QKeyEvent(
    QGraphicsProxyWidgetPrivate *self,
    QKeyEvent *event) {
  self->sendWidgetKeyEvent(event);
}

//  void QGraphicsProxyWidgetPrivate::setWidget_helper(QWidget *widget, bool
//      autoShow)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate16setWidget_helperEP7QWidgetb(
    QGraphicsProxyWidgetPrivate *self,
    QWidget *widget,
    bool autoShow) {
  self->setWidget_helper(widget, autoShow);
}

//  void QGraphicsProxyWidgetPrivate::removeSubFocusHelper(QWidget *widget,
//      Qt::FocusReason reason)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate20removeSubFocusHelperEP7QWidgetN2Qt11FocusReasonE(
    QGraphicsProxyWidgetPrivate *self,
    QWidget *widget,
    Qt::FocusReason reason) {
  self->removeSubFocusHelper(widget, reason);
}

//  void QGraphicsProxyWidgetPrivate::_q_removeWidgetSlot()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate19_q_removeWidgetSlotEv(
    QGraphicsProxyWidgetPrivate *self) {
  self->_q_removeWidgetSlot();
}

//  void QGraphicsProxyWidgetPrivate::embedSubWindow(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate14embedSubWindowEP7QWidget(
    QGraphicsProxyWidgetPrivate *self,
    QWidget *a0) {
  self->embedSubWindow(a0);
}

//  void QGraphicsProxyWidgetPrivate::unembedSubWindow(QWidget *a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate16unembedSubWindowEP7QWidget(
    QGraphicsProxyWidgetPrivate *self,
    QWidget *a0) {
  self->unembedSubWindow(a0);
}

//  bool QGraphicsProxyWidgetPrivate::isProxyWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK27QGraphicsProxyWidgetPrivate13isProxyWidgetEv(
    const QGraphicsProxyWidgetPrivate *self) {
  return self->isProxyWidget();
}

//  void QGraphicsProxyWidgetPrivate::updateWidgetGeometryFromProxy()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate29updateWidgetGeometryFromProxyEv(
    QGraphicsProxyWidgetPrivate *self) {
  self->updateWidgetGeometryFromProxy();
}

//  void QGraphicsProxyWidgetPrivate::updateProxyGeometryFromWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate29updateProxyGeometryFromWidgetEv(
    QGraphicsProxyWidgetPrivate *self) {
  self->updateProxyGeometryFromWidget();
}

//  void
//      QGraphicsProxyWidgetPrivate::updateProxyInputMethodAcceptanceFromWidg
//      et()
extern "C" Q_DECL_EXPORT
void ritual_ZN27QGraphicsProxyWidgetPrivate42updateProxyInputMethodAcceptanceFromWidgetEv(
    QGraphicsProxyWidgetPrivate *self) {
  self->updateProxyInputMethodAcceptanceFromWidget();
}

//  QPointF QGraphicsProxyWidgetPrivate::mapToReceiver(const QPointF &pos,
//      const QWidget *receiver) const
extern "C" Q_DECL_EXPORT
QPointF *ritual_ZNK27QGraphicsProxyWidgetPrivate13mapToReceiverERK7QPointFPK7QWidget(
    const QGraphicsProxyWidgetPrivate *self,
    const QPointF *pos,
    const QWidget *receiver) {
  return new QPointF(self->mapToReceiver(*pos, receiver));
}

//  a Python function taken by a CuteQGraphicsProxyWidgetPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsProxyWidgetPrivate(
    QGraphicsProxyWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsProxyWidgetPrivate *>(self)->take(key, call);
}

//  bool QGraphicsProxyWidgetPrivate::isProxyWidget() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK27QGraphicsProxyWidgetPrivate13isProxyWidgetEv(
    const QGraphicsProxyWidgetPrivate *self) {
  return self->QGraphicsProxyWidgetPrivate::isProxyWidget();
}

#endif  // QT_CONFIG(graphicsview)
