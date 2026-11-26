//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qgraphicswidget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qgraphicswidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qpalette.h>
#include <QtGui/qfont.h>
#include <QtCore/qpoint.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qglobal.h>
#include <QtCore/qdebug.h>
#include <QtCore/qnumeric.h>
#include <QtWidgets/private/qgraphicswidget_p.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/private/qgraphicsscene_p.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/QStyleOptionTitleBar>
#include <QtWidgets/QGraphicsSceneMouseEvent>
#include <QtCore/qglobal.h>
#include <QtWidgets/qgraphicslayout.h>
#include <QtWidgets/qgraphicsscene.h>
#include <QtWidgets/qgraphicslayoutitem.h>
#include <QtWidgets/private/qgraphicslayoutitem_p.h>
#include <QtWidgets/qwidget.h>
#include <QtWidgets/qgraphicswidget.h>
#include <QtWidgets/private/qgraphicsitem_p.h>
#include <QtCore/QtDebug>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 373, as local:qgraphicswidget_p.cpp:minimumHeightForWidth
static qreal minimumHeightForWidth(qreal width, qreal minh, qreal maxh,
                                   const QGraphicsWidget *widget,
                                   bool heightForWidth = true)
{
    qreal minimumHeightForWidth = -1;
    const bool hasHFW = QGraphicsLayoutItemPrivate::get(widget)->hasHeightForWidth();
    if (hasHFW == heightForWidth) {
        minimumHeightForWidth = hasHFW
                                ? widget->effectiveSizeHint(Qt::MinimumSize, QSizeF(width, -1)).height()
                                : widget->effectiveSizeHint(Qt::MinimumSize, QSizeF(-1, width)).width();    //"width" is here height!
    } else {
        // widthForHeight
        const qreal constraint = width;
        while (maxh - minh > 0.1) {
            qreal middle = minh + (maxh - minh)/2;
            // ### really bad, if we are a widget with a layout it will call
            // layout->effectiveSizeHint(Qt::MiniumumSize), which again will call
            // sizeHint three times because of how the cache works
            qreal hfw = hasHFW
                        ? widget->effectiveSizeHint(Qt::MinimumSize, QSizeF(middle, -1)).height()
                        : widget->effectiveSizeHint(Qt::MinimumSize, QSizeF(-1, middle)).width();
            if (hfw > constraint) {
                minh = middle;
            } else if (hfw <= constraint) {
                maxh = middle;
            }
        }
        minimumHeightForWidth = maxh;
    }
    return minimumHeightForWidth;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 405, as local:qgraphicswidget_p.cpp:minimumWidthForHeight
static qreal minimumWidthForHeight(qreal height, qreal minw, qreal maxw,
                                   const QGraphicsWidget *widget)
{
    return minimumHeightForWidth(height, minw, maxw, widget, false);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 411, as local:qgraphicswidget_p.cpp:closestAcceptableSize
static QSizeF closestAcceptableSize(const QSizeF &proposed,
                                    const QGraphicsWidget *widget)
{
    const QSizeF current = widget->size();

    qreal minw = proposed.width();
    qreal maxw = current.width();
    qreal minh = proposed.height();
    qreal maxh = current.height();

    qreal middlew = maxw;
    qreal middleh = maxh;
    qreal min_hfw;
    min_hfw = minimumHeightForWidth(maxw, minh, maxh, widget);

    do {
        if (maxw - minw < 0.1) {
            // we still haven't found anything, cut off binary search
            minw = maxw;
            minh = maxh;
        }
        middlew = minw + (maxw - minw)/2.0;
        middleh = minh + (maxh - minh)/2.0;

        min_hfw = minimumHeightForWidth(middlew, minh, maxh, widget);

        if (min_hfw > middleh) {
            minw = middlew;
            minh = middleh;
        } else if (min_hfw <= middleh) {
            maxw = middlew;
            maxh = middleh;
        }
    } while (maxw != minw);

    min_hfw = minimumHeightForWidth(middlew, minh, maxh, widget);

    QSizeF result;
    if (min_hfw < maxh) {
        result = QSizeF(middlew, min_hfw);
    } else {
        // Needed because of the cut-off we do above.
        result = QSizeF(minimumWidthForHeight(maxh, proposed.width(), current.width(), widget), maxh);
    }
    return result;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 458, as local:qgraphicswidget_p.cpp:_q_boundGeometryToSizeConstraints
static void _q_boundGeometryToSizeConstraints(const QRectF &startGeometry,
                                              QRectF *rect, Qt::WindowFrameSection section,
                                              const QSizeF &min, const QSizeF &max,
                                              const QGraphicsWidget *widget)
{
    const QRectF proposedRect = *rect;
    qreal width = qBound(min.width(), proposedRect.width(), max.width());
    qreal height = qBound(min.height(), proposedRect.height(), max.height());

    const bool hasHFW = QGraphicsLayoutItemPrivate::get(widget)->hasHeightForWidth();
    const bool hasWFH = QGraphicsLayoutItemPrivate::get(widget)->hasWidthForHeight();

    const bool widthChanged = proposedRect.width() != widget->size().width();
    const bool heightChanged = proposedRect.height() != widget->size().height();

    if (hasHFW || hasWFH) {
        if (widthChanged || heightChanged) {
            qreal minExtent;
            qreal maxExtent;
            qreal constraint;
            qreal proposed;
            if (hasHFW) {
                minExtent = min.height();
                maxExtent = max.height();
                constraint = width;
                proposed = proposedRect.height();
            } else {
                // width for height
                minExtent = min.width();
                maxExtent = max.width();
                constraint = height;
                proposed = proposedRect.width();
            }
            if (minimumHeightForWidth(constraint, minExtent, maxExtent, widget, hasHFW) > proposed) {
                QSizeF effectiveSize = closestAcceptableSize(QSizeF(width, height), widget);
                width = effectiveSize.width();
                height = effectiveSize.height();
            }
        }
    }

    switch (section) {
    case Qt::LeftSection:
        rect->setRect(startGeometry.right() - qRound(width), startGeometry.top(),
                      qRound(width), startGeometry.height());
        break;
    case Qt::TopLeftSection:
        rect->setRect(startGeometry.right() - qRound(width), startGeometry.bottom() - qRound(height),
                      qRound(width), qRound(height));
        break;
    case Qt::TopSection:
        rect->setRect(startGeometry.left(), startGeometry.bottom() - qRound(height),
                      startGeometry.width(), qRound(height));
        break;
    case Qt::TopRightSection:
        rect->setTop(rect->bottom() - qRound(height));
        rect->setWidth(qRound(width));
        break;
    case Qt::RightSection:
        rect->setWidth(qRound(width));
        break;
    case Qt::BottomRightSection:
        rect->setWidth(qRound(width));
        rect->setHeight(qRound(height));
        break;
    case Qt::BottomSection:
        rect->setHeight(qRound(height));
        break;
    case Qt::BottomLeftSection:
        rect->setRect(startGeometry.right() - qRound(width), startGeometry.top(),
                      qRound(width), qRound(height));
        break;
    default:
        break;
    }
}

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

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 239, as _ZNK26QGraphicsLayoutItemPrivate17hasHeightForWidthEv
inline bool QGraphicsLayoutItemPrivate::hasHeightForWidth() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasHeightForWidth())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasHeightForWidth();
            }
        }
    }
    return q->sizePolicy().hasHeightForWidth();
}

//  from src/widgets/graphicsview/qgraphicslayoutitem.cpp, line 259, as _ZNK26QGraphicsLayoutItemPrivate17hasWidthForHeightEv
inline bool QGraphicsLayoutItemPrivate::hasWidthForHeight() const
{
    Q_Q(const QGraphicsLayoutItem);
    if (isLayout) {
        const QGraphicsLayout *l = static_cast<const QGraphicsLayout *>(q);
        for (int i = l->count() - 1; i >= 0; --i) {
            if (QGraphicsLayoutItemPrivate::get(l->itemAt(i))->hasWidthForHeight())
                return true;
        }
    } else if (QGraphicsItem *item = q->graphicsItem()) {
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (w->layout()) {
                return QGraphicsLayoutItemPrivate::get(w->layout())->hasWidthForHeight();
            }
        }
    }
    return q->sizePolicy().hasWidthForHeight();
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 21, as _ZN22QGraphicsWidgetPrivate4initEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE
inline void QGraphicsWidgetPrivate::init(QGraphicsItem *parentItem, Qt::WindowFlags wFlags)
{
    Q_Q(QGraphicsWidget);

    attributes = 0;
    isWidget = 1; // QGraphicsItem::isWidget() returns true.
    focusNext = focusPrev = q;
    focusPolicy = Qt::NoFocus;

    adjustWindowFlags(&wFlags);
    windowFlags = wFlags;

    q->setParentItem(parentItem);
    q->setSizePolicy(QSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred, QSizePolicy::DefaultType));
    q->setGraphicsItem(q);

    resolveLayoutDirection();
    q->unsetWindowFrameMargins();
    flags |= QGraphicsItem::ItemUsesExtendedStyleOption;
    flags |= QGraphicsItem::ItemSendsGeometryChanges;
    if (windowFlags & Qt::Window)
        flags |= QGraphicsItem::ItemIsPanel;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 45, as _ZNK22QGraphicsWidgetPrivate14titleBarHeightERK20QStyleOptionTitleBar
inline qreal QGraphicsWidgetPrivate::titleBarHeight(const QStyleOptionTitleBar &options) const
{
    Q_Q(const QGraphicsWidget);
    int height = q->style()->pixelMetric(QStyle::PM_TitleBarHeight, &options);
    return (qreal)height;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 84, as _ZNK22QGraphicsWidgetPrivate13ensureMarginsEv
inline void QGraphicsWidgetPrivate::ensureMargins() const
{
    if (!margins)
        margins = std::make_unique<QMarginsF>();
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 719, as _ZN22QGraphicsWidgetPrivate30fixFocusChainBeforeReparentingEP15QGraphicsWidgetP14QGraphicsSceneS3_
inline void QGraphicsWidgetPrivate::fixFocusChainBeforeReparenting(QGraphicsWidget *newParent, QGraphicsScene *oldScene, QGraphicsScene *newScene)
{
    Q_Q(QGraphicsWidget);
    Q_ASSERT(focusNext && focusPrev);

    if (q_ptr->isPanel()) {
        // panels are never a part of their parent's or ancestors' focus
        // chains. so reparenting a panel is easy; there's nothing to
        // do.
        return;
    }

    // we're not a panel, so find the first widget in the focus chain
    // (this), and the last (this, or the last widget that is still
    // a descendent of this). also find the widgets that currently /
    // before reparenting point to this widgets' focus chain.
    QGraphicsWidget *focusFirst = q;
    QGraphicsWidget *focusBefore = focusPrev;
    QGraphicsWidget *focusLast = focusFirst;
    QGraphicsWidget *focusAfter = focusNext;
    do {
        if (!q->isAncestorOf(focusAfter))
            break;
        focusLast = focusAfter;
    } while ((focusAfter = focusAfter->d_func()->focusNext));

    if (!parent && oldScene && oldScene != newScene && oldScene->d_func()->tabFocusFirst == q) {
        // detach from old scene's top level focus chain.
        oldScene->d_func()->tabFocusFirst = (focusAfter != q) ? focusAfter : nullptr;
    }

    // detach from current focus chain; skip this widget subtree.
    focusBefore->d_func()->focusNext = focusAfter;
    if (focusAfter)
        focusAfter->d_func()->focusPrev = focusBefore;

    if (newParent) {
        // attach to new parent's focus chain as the last element
        // in its chain.
        QGraphicsWidget *newFocusFirst = newParent;
        QGraphicsWidget *newFocusLast = newFocusFirst;
        QGraphicsWidget *newFocusAfter = newFocusFirst->d_func()->focusNext;
        do {
            if (!newParent->isAncestorOf(newFocusAfter))
                break;
            newFocusLast = newFocusAfter;
        } while ((newFocusAfter = newFocusAfter->d_func()->focusNext));

        newFocusLast->d_func()->focusNext = q;
        focusLast->d_func()->focusNext = newFocusAfter;
        if (newFocusAfter)
            newFocusAfter->d_func()->focusPrev = focusLast;
        focusPrev = newFocusLast;
    } else {
        // no new parent, so just link up our own prev->last widgets.
        focusPrev = focusLast;
        focusLast->d_func()->focusNext = q;
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 779, as _ZN22QGraphicsWidgetPrivate16setLayout_helperEP15QGraphicsLayout
inline void QGraphicsWidgetPrivate::setLayout_helper(QGraphicsLayout *l)
{
    delete (this->layout);
    layout = l;
    if (!l) {
        Q_Q(QGraphicsWidget);
        q->updateGeometry();
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 157, as _ZN22QGraphicsWidgetPrivate25setLayoutDirection_helperEN2Qt15LayoutDirectionE
inline void QGraphicsWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection direction)
{
    Q_Q(QGraphicsWidget);
    if ((direction == Qt::RightToLeft) == (testAttribute(Qt::WA_RightToLeft)))
        return;
    q->setAttribute(Qt::WA_RightToLeft, (direction == Qt::RightToLeft));

    // Propagate this change to all children.
    for (int i = 0; i < children.size(); ++i) {
        QGraphicsItem *item = children.at(i);
        if (item->isWidget()) {
            QGraphicsWidget *widget = static_cast<QGraphicsWidget *>(item);
            if (widget->parentWidget() && !widget->testAttribute(Qt::WA_SetLayoutDirection))
                widget->d_func()->setLayoutDirection_helper(direction);
        }
    }

    // Send the notification event to this widget item.
    QEvent e(QEvent::LayoutDirectionChange);
    QCoreApplication::sendEvent(q, &e);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 179, as _ZN22QGraphicsWidgetPrivate22resolveLayoutDirectionEv
inline void QGraphicsWidgetPrivate::resolveLayoutDirection()
{
    Q_Q(QGraphicsWidget);
    if (q->testAttribute(Qt::WA_SetLayoutDirection)) {
        return;
    }
    if (QGraphicsWidget *parentWidget = q->parentWidget()) {
        setLayoutDirection_helper(parentWidget->layoutDirection());
    } else if (scene) {
        // ### shouldn't the scene have a layoutdirection really? how does
        // ### QGraphicsWidget get changes from QApplication::layoutDirection?
        setLayoutDirection_helper(QGuiApplication::layoutDirection());
    } else {
        setLayoutDirection_helper(QGuiApplication::layoutDirection());
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 114, as _ZN22QGraphicsWidgetPrivate17setPalette_helperERK8QPalette
inline void QGraphicsWidgetPrivate::setPalette_helper(const QPalette &palette)
{
    if (this->palette == palette && this->palette.resolveMask() == palette.resolveMask())
        return;
    updatePalette(palette);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 129, as _ZN22QGraphicsWidgetPrivate13updatePaletteERK8QPalette
inline void QGraphicsWidgetPrivate::updatePalette(const QPalette &palette)
{
    Q_Q(QGraphicsWidget);
    // Update local palette setting.
    this->palette = palette;

    // Calculate new mask.
    if (q->isWindow() && !q->testAttribute(Qt::WA_WindowPropagation))
        inheritedPaletteResolveMask = 0;
    int mask = palette.resolveMask() | inheritedPaletteResolveMask;

    // Propagate to children.
    for (int i = 0; i < children.size(); ++i) {
        QGraphicsItem *item = children.at(i);
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (!w->isWindow() || w->testAttribute(Qt::WA_WindowPropagation))
                w->d_func()->resolvePalette(mask);
        } else {
            item->d_ptr->resolvePalette(mask);
        }
    }

    // Notify change.
    QEvent event(QEvent::PaletteChange);
    QCoreApplication::sendEvent(q, &event);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 196, as _ZNK22QGraphicsWidgetPrivate20naturalWidgetPaletteEv
inline QPalette QGraphicsWidgetPrivate::naturalWidgetPalette() const
{
    Q_Q(const QGraphicsWidget);
    QPalette palette;
    if (QGraphicsWidget *parent = q->parentWidget()) {
        palette = parent->palette();
    } else if (scene) {
        palette = scene->palette();
    }
    palette.setResolveMask(0);
    return palette;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 209, as _ZN22QGraphicsWidgetPrivate14setFont_helperERK5QFont
inline void QGraphicsWidgetPrivate::setFont_helper(const QFont &font)
{
    if (this->font == font && this->font.resolveMask() == font.resolveMask())
        return;
    updateFont(font);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 227, as _ZN22QGraphicsWidgetPrivate10updateFontERK5QFont
inline void QGraphicsWidgetPrivate::updateFont(const QFont &font)
{
    Q_Q(QGraphicsWidget);
    // Update the local font setting.
    this->font = font;

    // Calculate new mask.
    if (q->isWindow() && !q->testAttribute(Qt::WA_WindowPropagation))
        inheritedFontResolveMask = 0;
    int mask = font.resolveMask() | inheritedFontResolveMask;

    // Propagate to children.
    for (int i = 0; i < children.size(); ++i) {
        QGraphicsItem *item = children.at(i);
        if (item->isWidget()) {
            QGraphicsWidget *w = static_cast<QGraphicsWidget *>(item);
            if (!w->isWindow() || w->testAttribute(Qt::WA_WindowPropagation))
                w->d_func()->resolveFont(mask);
        } else {
            item->d_ptr->resolveFont(mask);
        }
    }

    if (!polished)
        return;
    // Notify change.
    QEvent event(QEvent::FontChange);
    QCoreApplication::sendEvent(q, &event);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 257, as _ZNK22QGraphicsWidgetPrivate17naturalWidgetFontEv
inline QFont QGraphicsWidgetPrivate::naturalWidgetFont() const
{
    Q_Q(const QGraphicsWidget);
    QFont naturalFont; // ### no application font support
    if (QGraphicsWidget *parent = q->parentWidget()) {
        naturalFont = parent->font();
    } else if (scene) {
        naturalFont = scene->font();
    }
    naturalFont.setResolveMask(0);
    return naturalFont;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 270, as _ZN22QGraphicsWidgetPrivate23initStyleOptionTitleBarEP20QStyleOptionTitleBar
inline void QGraphicsWidgetPrivate::initStyleOptionTitleBar(QStyleOptionTitleBar *option)
{
    Q_Q(QGraphicsWidget);
    ensureWindowData();
    q->initStyleOption(option);
    option->rect.setHeight(titleBarHeight(*option));
    option->titleBarFlags = windowFlags;
    option->subControls = QStyle::SC_TitleBarCloseButton | QStyle::SC_TitleBarLabel | QStyle::SC_TitleBarSysMenu;
    option->activeSubControls = windowData->hoveredSubControl;
    bool isActive = q->isActiveWindow();
    option->state.setFlag(QStyle::State_Active, isActive);
    if (isActive) {
        option->titleBarState = Qt::WindowActive;
        option->titleBarState |= QStyle::State_Active;
    } else {
        option->titleBarState = Qt::WindowNoState;
    }
    QFont windowTitleFont = QApplication::font("QMdiSubWindowTitleBar");
    QRect textRect = q->style()->subControlRect(QStyle::CC_TitleBar, option, QStyle::SC_TitleBarLabel, nullptr);
    option->text = QFontMetrics(windowTitleFont).elidedText(
        windowData->windowTitle, Qt::ElideRight, textRect.width());
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 293, as _ZN22QGraphicsWidgetPrivate17adjustWindowFlagsEP6QFlagsIN2Qt10WindowTypeEE
inline void QGraphicsWidgetPrivate::adjustWindowFlags(Qt::WindowFlags *flags)
{
    bool customize =  (*flags & (Qt::CustomizeWindowHint
            | Qt::FramelessWindowHint
            | Qt::WindowTitleHint
            | Qt::WindowSystemMenuHint
            | Qt::WindowMinimizeButtonHint
            | Qt::WindowMaximizeButtonHint
            | Qt::WindowContextHelpButtonHint));

    uint type = (*flags & Qt::WindowType_Mask);
    if (customize)
        ;
    else if (type == Qt::Dialog || type == Qt::Sheet)
        *flags |= Qt::WindowTitleHint | Qt::WindowSystemMenuHint | Qt::WindowContextHelpButtonHint;
    else if (type == Qt::Tool)
        *flags |= Qt::WindowTitleHint | Qt::WindowSystemMenuHint;
    else if (type == Qt::Window || type == Qt::SubWindow)
        *flags |= Qt::WindowTitleHint | Qt::WindowSystemMenuHint
                  | Qt::WindowMinimizeButtonHint | Qt::WindowMaximizeButtonHint;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 315, as _ZN22QGraphicsWidgetPrivate28windowFrameMouseReleaseEventEP24QGraphicsSceneMouseEvent
inline void QGraphicsWidgetPrivate::windowFrameMouseReleaseEvent(QGraphicsSceneMouseEvent *event)
{
    Q_Q(QGraphicsWidget);
    ensureWindowData();
    if (windowData->grabbedSection != Qt::NoSection) {
        if (windowData->grabbedSection == Qt::TitleBarArea) {
            windowData->buttonSunken = false;
            QStyleOptionTitleBar bar;
            initStyleOptionTitleBar(&bar);
            // make sure that the coordinates (rect and pos) we send to the style are positive.
            bar.rect = q->windowFrameRect().toRect();
            bar.rect.moveTo(0,0);
            bar.rect.setHeight(q->style()->pixelMetric(QStyle::PM_TitleBarHeight, &bar));
            QPointF pos = event->pos();
            if (windowFrameMargins) {
                pos.rx() += windowFrameMargins->left();
                pos.ry() += windowFrameMargins->top();
            }
            bar.subControls = QStyle::SC_TitleBarCloseButton;
            if (q->style()->subControlRect(QStyle::CC_TitleBar, &bar,
                                           QStyle::SC_TitleBarCloseButton,
                                           event->widget()).contains(pos.toPoint())) {
                q->close();
            }
        }
        if (!(static_cast<QGraphicsSceneMouseEvent *>(event)->buttons()))
            windowData->grabbedSection = Qt::NoSection;
        event->accept();
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 346, as _ZN22QGraphicsWidgetPrivate26windowFrameMousePressEventEP24QGraphicsSceneMouseEvent
inline void QGraphicsWidgetPrivate::windowFrameMousePressEvent(QGraphicsSceneMouseEvent *event)
{
    Q_Q(QGraphicsWidget);
    if (event->button() != Qt::LeftButton)
        return;

    ensureWindowData();
    windowData->startGeometry = q->geometry();
    windowData->grabbedSection = q->windowFrameSectionAt(event->pos());
    ensureWindowData();
    if (windowData->grabbedSection == Qt::TitleBarArea
        && windowData->hoveredSubControl == QStyle::SC_TitleBarCloseButton) {
        windowData->buttonSunken = true;
        q->update();
    }
    event->setAccepted(windowData->grabbedSection != Qt::NoSection);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 535, as _ZN22QGraphicsWidgetPrivate25windowFrameMouseMoveEventEP24QGraphicsSceneMouseEvent
inline void QGraphicsWidgetPrivate::windowFrameMouseMoveEvent(QGraphicsSceneMouseEvent *event)
{
    Q_Q(QGraphicsWidget);
    ensureWindowData();
    if (!(event->buttons() & Qt::LeftButton) || windowData->hoveredSubControl != QStyle::SC_TitleBarLabel)
        return;

    QLineF delta(q->mapFromScene(event->buttonDownScenePos(Qt::LeftButton)), event->pos());
    QLineF parentDelta(q->mapToParent(delta.p1()), q->mapToParent(delta.p2()));
    QLineF parentXDelta(q->mapToParent(QPointF(delta.p1().x(), 0)), q->mapToParent(QPointF(delta.p2().x(), 0)));
    QLineF parentYDelta(q->mapToParent(QPointF(0, delta.p1().y())), q->mapToParent(QPointF(0, delta.p2().y())));

    QRectF newGeometry;
    switch (windowData->grabbedSection) {
    case Qt::LeftSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentXDelta.dx(), parentXDelta.dy()),
                             windowData->startGeometry.size() - QSizeF(delta.dx(), delta.dy()));
        break;
    case Qt::TopLeftSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentDelta.dx(), parentDelta.dy()),
                             windowData->startGeometry.size() - QSizeF(delta.dx(), delta.dy()));
        break;
    case Qt::TopSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentYDelta.dx(), parentYDelta.dy()),
                             windowData->startGeometry.size() - QSizeF(0, delta.dy()));
        break;
    case Qt::TopRightSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentYDelta.dx(), parentYDelta.dy()),
                             windowData->startGeometry.size() - QSizeF(-delta.dx(), delta.dy()));
        break;
    case Qt::RightSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft(),
                             windowData->startGeometry.size() + QSizeF(delta.dx(), 0));
        break;
    case Qt::BottomRightSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft(),
                             windowData->startGeometry.size() + QSizeF(delta.dx(), delta.dy()));
        break;
    case Qt::BottomSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft(),
                             windowData->startGeometry.size() + QSizeF(0, delta.dy()));
        break;
    case Qt::BottomLeftSection:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentXDelta.dx(), parentXDelta.dy()),
                             windowData->startGeometry.size() - QSizeF(delta.dx(), -delta.dy()));
        break;
    case Qt::TitleBarArea:
        newGeometry = QRectF(windowData->startGeometry.topLeft()
                             + QPointF(parentDelta.dx(), parentDelta.dy()),
                             windowData->startGeometry.size());
        break;
    case Qt::NoSection:
        break;
    }

    if (windowData->grabbedSection != Qt::NoSection) {
        _q_boundGeometryToSizeConstraints(windowData->startGeometry, &newGeometry,
                                          windowData->grabbedSection,
                                          q->effectiveSizeHint(Qt::MinimumSize),
                                          q->effectiveSizeHint(Qt::MaximumSize),
                                          q);
        q->setGeometry(newGeometry);
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 605, as _ZN22QGraphicsWidgetPrivate25windowFrameHoverMoveEventEP24QGraphicsSceneHoverEvent
inline void QGraphicsWidgetPrivate::windowFrameHoverMoveEvent(QGraphicsSceneHoverEvent *event)
{
    Q_Q(QGraphicsWidget);
    if (!hasDecoration())
        return;

    ensureWindowData();

    if (q->rect().contains(event->pos())) {
        if (windowData->buttonMouseOver || windowData->hoveredSubControl != QStyle::SC_None)
            windowFrameHoverLeaveEvent(event);
        return;
    }

    bool wasMouseOver = windowData->buttonMouseOver;
    QRect oldButtonRect = windowData->buttonRect;
    windowData->buttonRect = QRect();
    windowData->buttonMouseOver = false;
    QPointF pos = event->pos();
    QStyleOptionTitleBar bar;
    // make sure that the coordinates (rect and pos) we send to the style are positive.
    if (windowFrameMargins) {
        pos.rx() += windowFrameMargins->left();
        pos.ry() += windowFrameMargins->top();
    }
    initStyleOptionTitleBar(&bar);
    bar.rect = q->windowFrameRect().toRect();
    bar.rect.moveTo(0,0);
    bar.rect.setHeight(int(titleBarHeight(bar)));

    Qt::CursorShape cursorShape = Qt::ArrowCursor;
    bool needsSetCursorCall = true;
    switch (q->windowFrameSectionAt(event->pos())) {
        case Qt::TopLeftSection:
        case Qt::BottomRightSection:
            cursorShape = Qt::SizeFDiagCursor;
            break;
        case Qt::TopRightSection:
        case Qt::BottomLeftSection:
            cursorShape = Qt::SizeBDiagCursor;
            break;
        case Qt::LeftSection:
        case Qt::RightSection:
            cursorShape = Qt::SizeHorCursor;
            break;
        case Qt::TopSection:
        case Qt::BottomSection:
            cursorShape = Qt::SizeVerCursor;
            break;
        case Qt::TitleBarArea:
            windowData->buttonRect = q->style()->subControlRect(
                QStyle::CC_TitleBar, &bar, QStyle::SC_TitleBarCloseButton, nullptr);
            if (windowData->buttonRect.contains(pos.toPoint()))
                windowData->buttonMouseOver = true;
            event->ignore();
            break;
        default:
            needsSetCursorCall = false;
            event->ignore();
        }
#ifndef QT_NO_CURSOR
    if (needsSetCursorCall)
        q->setCursor(cursorShape);
#else
    Q_UNUSED(needsSetCursorCall);
    Q_UNUSED(cursorShape);
#endif
    // update buttons if we hover over them
    windowData->hoveredSubControl = q->style()->hitTestComplexControl(QStyle::CC_TitleBar, &bar, pos.toPoint(), nullptr);
    if (windowData->hoveredSubControl != QStyle::SC_TitleBarCloseButton)
        windowData->hoveredSubControl = QStyle::SC_TitleBarLabel;

    if (windowData->buttonMouseOver != wasMouseOver) {
        if (!oldButtonRect.isNull())
            q->update(QRectF(oldButtonRect).translated(q->windowFrameRect().topLeft()));
        if (!windowData->buttonRect.isNull())
            q->update(QRectF(windowData->buttonRect).translated(q->windowFrameRect().topLeft()));
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 685, as _ZN22QGraphicsWidgetPrivate26windowFrameHoverLeaveEventEP24QGraphicsSceneHoverEvent
inline void QGraphicsWidgetPrivate::windowFrameHoverLeaveEvent(QGraphicsSceneHoverEvent *event)
{
    Q_UNUSED(event);
    Q_Q(QGraphicsWidget);
    if (hasDecoration()) {
        // ### restore the cursor, don't override it
#ifndef QT_NO_CURSOR
        q->unsetCursor();
#endif

        ensureWindowData();

        bool needsUpdate = false;
        if (windowData->hoveredSubControl == QStyle::SC_TitleBarCloseButton
            || windowData->buttonMouseOver)
            needsUpdate = true;

        // update the hover state (of buttons etc...)
        windowData->hoveredSubControl = QStyle::SC_None;
        windowData->buttonMouseOver = false;
        windowData->buttonRect = QRect();
        if (needsUpdate)
            q->update(windowData->buttonRect);
    }
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 711, as _ZNK22QGraphicsWidgetPrivate13hasDecorationEv
inline bool QGraphicsWidgetPrivate::hasDecoration() const
{
    return (windowFlags & Qt::Window) && (windowFlags & Qt::WindowTitleHint);
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 835, as _ZN22QGraphicsWidgetPrivate21setGeometryFromSetPosEv
inline void QGraphicsWidgetPrivate::setGeometryFromSetPos()
{
    if (inSetGeometry)
        return;
    Q_Q(QGraphicsWidget);
    inSetPos = 1;
    // Ensure setGeometry is called (avoid recursion when setPos is
    // called from within setGeometry).
    q->setGeometry(QRectF(pos, q->size()));
    inSetPos = 0 ;
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 108, as _ZN22QGraphicsWidgetPrivate16ensureWindowDataEv
inline void QGraphicsWidgetPrivate::ensureWindowData()
{
    if (!windowData)
        windowData = std::make_unique<WindowData>();
}

//  from src/widgets/graphicsview/qgraphicswidget_p.cpp, line 96, as _ZNK22QGraphicsWidgetPrivate24ensureWindowFrameMarginsEv
inline void QGraphicsWidgetPrivate::ensureWindowFrameMargins() const
{
    if (!windowFrameMargins)
        windowFrameMargins = std::make_unique<QMarginsF>();
}
//  -----------------------------------------------------------------------

//  A QGraphicsWidgetPrivate that Python can take functions over in. Every QGraphicsWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall0)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall1)(const void *, uint, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsWidgetPrivateCall2)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall3)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall4)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef qreal (*CuteQGraphicsWidgetPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall6)(const void *, qreal, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall9)(const void *, const QPointF *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef bool (*CuteQGraphicsWidgetPrivateCall11)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall12)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall13)(const void *, bool, int *);
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
typedef void (*CuteQGraphicsWidgetPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(graphicsview)
class CuteQGraphicsWidgetPrivate : public QGraphicsWidgetPrivate {
public:
  using QGraphicsWidgetPrivate::QGraphicsWidgetPrivate;
  void *taken[15] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate14resolvePaletteEj")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resolveFontEj")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate5widthEv")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate8setWidthEd")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate10resetWidthEv")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate6heightEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate9setHeightEd")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate11resetHeightEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate30updateSceneTransformFromParentEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate12setPosHelperERK7QPointF")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZN20QGraphicsItemPrivate16transformChangedEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(graphicsview)
#if QT_CONFIG(graphicsview)
    if (!std::strcmp(key, "_ZNK20QGraphicsItemPrivate13isProxyWidgetEv")) {
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
  //  void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
  void resolvePalette(uint inheritedMask) override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall0 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall0>(taken[0]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resolvePalette(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
  void resolveFont(uint inheritedMask) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall1 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall1>(taken[1]);
      call(this, inheritedMask, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resolveFont(inheritedMask);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsWidgetPrivate::width() const
  qreal width() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall2 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall2>(taken[2]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidgetPrivate::width();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::setWidth(qreal a0)
  void setWidth(qreal a0) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall3 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall3>(taken[3]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::setWidth(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resetWidth()
  void resetWidth() override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall4 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resetWidth();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  qreal QGraphicsWidgetPrivate::height() const
  qreal height() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall5 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall5>(taken[5]);
      qreal given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsWidgetPrivate::height();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::setHeight(qreal a0)
  void setHeight(qreal a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall6 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall6>(taken[6]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::setHeight(a0);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsWidgetPrivate::resetHeight()
  void resetHeight() override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall7 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsWidgetPrivate::resetHeight();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::updateSceneTransformFromParent()
  void updateSceneTransformFromParent() override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall8 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::updateSceneTransformFromParent();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::setPosHelper(const QPointF &pos)
  void setPosHelper(const QPointF &pos) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall9 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall9>(taken[9]);
      call(this, &pos, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::setPosHelper(pos);
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::transformChanged()
  void transformChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall10 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall10>(taken[10]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::transformChanged();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  bool QGraphicsItemPrivate::isProxyWidget() const
  bool isProxyWidget() const override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall11 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall11>(taken[11]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QGraphicsItemPrivate::isProxyWidget();
  }
#endif  // QT_CONFIG(graphicsview)

#if QT_CONFIG(graphicsview)
  //  void QGraphicsItemPrivate::subFocusItemChange()
  void subFocusItemChange() override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsWidgetPrivateCall12 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall12>(taken[12]);
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
      CuteQGraphicsWidgetPrivateCall13 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall13>(taken[13]);
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
      CuteQGraphicsWidgetPrivateCall14 call = reinterpret_cast<CuteQGraphicsWidgetPrivateCall14>(taken[14]);
      call(this, &handled);
      if (handled) return;
    }
    QGraphicsItemPrivate::siblingOrderChange();
  }
#endif  // QT_CONFIG(graphicsview)
};

//  QGraphicsWidget *QGraphicsWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZN22QGraphicsWidgetPrivate6q_funcEv(
    QGraphicsWidgetPrivate *self) {
  return self->q_func();
}

//  const QGraphicsWidget *QGraphicsWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsWidget *ritual_ZNK22QGraphicsWidgetPrivate6q_funcEv(
    const QGraphicsWidgetPrivate *self) {
  return self->q_func();
}

//  QGraphicsWidgetPrivate::~QGraphicsWidgetPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivateD1Ev(QGraphicsWidgetPrivate *self) {
  delete self;
}

//  void QGraphicsWidgetPrivate::init(QGraphicsItem *parentItem,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate4initEP13QGraphicsItem6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsWidgetPrivate *self,
    QGraphicsItem *parentItem,
    int wFlags) {
  self->init(parentItem, QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  qreal QGraphicsWidgetPrivate::titleBarHeight(const QStyleOptionTitleBar
//      &options) const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsWidgetPrivate14titleBarHeightERK20QStyleOptionTitleBar(
    const QGraphicsWidgetPrivate *self,
    const QStyleOptionTitleBar *options) {
  return self->titleBarHeight(*options);
}

//  void QGraphicsWidgetPrivate::ensureMargins() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QGraphicsWidgetPrivate13ensureMarginsEv(
    const QGraphicsWidgetPrivate *self) {
  self->ensureMargins();
}

//  void
//      QGraphicsWidgetPrivate::fixFocusChainBeforeReparenting(QGraphicsWidge
//      t *newParent, QGraphicsScene *oldScene, QGraphicsScene *newScene)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate30fixFocusChainBeforeReparentingEP15QGraphicsWidgetP14QGraphicsSceneS3_(
    QGraphicsWidgetPrivate *self,
    QGraphicsWidget *newParent,
    QGraphicsScene *oldScene,
    QGraphicsScene *newScene) {
  self->fixFocusChainBeforeReparenting(newParent, oldScene, newScene);
}

//  void QGraphicsWidgetPrivate::setLayout_helper(QGraphicsLayout *l)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate16setLayout_helperEP15QGraphicsLayout(
    QGraphicsWidgetPrivate *self,
    QGraphicsLayout *l) {
  self->setLayout_helper(l);
}

//  void
//      QGraphicsWidgetPrivate::setLayoutDirection_helper(Qt::LayoutDirection
//      direction)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate25setLayoutDirection_helperEN2Qt15LayoutDirectionE(
    QGraphicsWidgetPrivate *self,
    Qt::LayoutDirection direction) {
  self->setLayoutDirection_helper(direction);
}

//  void QGraphicsWidgetPrivate::resolveLayoutDirection()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate22resolveLayoutDirectionEv(
    QGraphicsWidgetPrivate *self) {
  self->resolveLayoutDirection();
}

//  void QGraphicsWidgetPrivate::setPalette_helper(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate17setPalette_helperERK8QPalette(
    QGraphicsWidgetPrivate *self,
    const QPalette *palette) {
  self->setPalette_helper(*palette);
}

//  void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate14resolvePaletteEj(
    QGraphicsWidgetPrivate *self,
    uint inheritedMask) {
  self->resolvePalette(inheritedMask);
}

//  void QGraphicsWidgetPrivate::updatePalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate13updatePaletteERK8QPalette(
    QGraphicsWidgetPrivate *self,
    const QPalette *palette) {
  self->updatePalette(*palette);
}

//  QPalette QGraphicsWidgetPrivate::naturalWidgetPalette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK22QGraphicsWidgetPrivate20naturalWidgetPaletteEv(
    const QGraphicsWidgetPrivate *self) {
  return new QPalette(self->naturalWidgetPalette());
}

//  void QGraphicsWidgetPrivate::setFont_helper(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate14setFont_helperERK5QFont(
    QGraphicsWidgetPrivate *self,
    const QFont *font) {
  self->setFont_helper(*font);
}

//  void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate11resolveFontEj(
    QGraphicsWidgetPrivate *self,
    uint inheritedMask) {
  self->resolveFont(inheritedMask);
}

//  void QGraphicsWidgetPrivate::updateFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate10updateFontERK5QFont(
    QGraphicsWidgetPrivate *self,
    const QFont *font) {
  self->updateFont(*font);
}

//  QFont QGraphicsWidgetPrivate::naturalWidgetFont() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK22QGraphicsWidgetPrivate17naturalWidgetFontEv(
    const QGraphicsWidgetPrivate *self) {
  return new QFont(self->naturalWidgetFont());
}

//  void QGraphicsWidgetPrivate::initStyleOptionTitleBar(QStyleOptionTitleBar
//      *option)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate23initStyleOptionTitleBarEP20QStyleOptionTitleBar(
    QGraphicsWidgetPrivate *self,
    QStyleOptionTitleBar *option) {
  self->initStyleOptionTitleBar(option);
}

//  void QGraphicsWidgetPrivate::adjustWindowFlags(Qt::WindowFlags *wFlags)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate17adjustWindowFlagsEP6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsWidgetPrivate *self,
    Qt::WindowFlags *wFlags) {
  self->adjustWindowFlags(wFlags);
}

//  void QGraphicsWidgetPrivate::windowFrameMouseReleaseEvent(QGraphicsSceneM
//      ouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate28windowFrameMouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsWidgetPrivate *self,
    QGraphicsSceneMouseEvent *event) {
  self->windowFrameMouseReleaseEvent(event);
}

//  void QGraphicsWidgetPrivate::windowFrameMousePressEvent(QGraphicsSceneMou
//      seEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate26windowFrameMousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsWidgetPrivate *self,
    QGraphicsSceneMouseEvent *event) {
  self->windowFrameMousePressEvent(event);
}

//  void QGraphicsWidgetPrivate::windowFrameMouseMoveEvent(QGraphicsSceneMous
//      eEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate25windowFrameMouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsWidgetPrivate *self,
    QGraphicsSceneMouseEvent *event) {
  self->windowFrameMouseMoveEvent(event);
}

//  void QGraphicsWidgetPrivate::windowFrameHoverMoveEvent(QGraphicsSceneHove
//      rEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate25windowFrameHoverMoveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidgetPrivate *self,
    QGraphicsSceneHoverEvent *event) {
  self->windowFrameHoverMoveEvent(event);
}

//  void QGraphicsWidgetPrivate::windowFrameHoverLeaveEvent(QGraphicsSceneHov
//      erEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate26windowFrameHoverLeaveEventEP24QGraphicsSceneHoverEvent(
    QGraphicsWidgetPrivate *self,
    QGraphicsSceneHoverEvent *event) {
  self->windowFrameHoverLeaveEvent(event);
}

//  bool QGraphicsWidgetPrivate::hasDecoration() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGraphicsWidgetPrivate13hasDecorationEv(
    const QGraphicsWidgetPrivate *self) {
  return self->hasDecoration();
}

//  qreal QGraphicsWidgetPrivate::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsWidgetPrivate5widthEv(
    const QGraphicsWidgetPrivate *self) {
  return self->width();
}

//  void QGraphicsWidgetPrivate::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate8setWidthEd(
    QGraphicsWidgetPrivate *self,
    qreal a0) {
  self->setWidth(a0);
}

//  void QGraphicsWidgetPrivate::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate10resetWidthEv(
    QGraphicsWidgetPrivate *self) {
  self->resetWidth();
}

//  qreal QGraphicsWidgetPrivate::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK22QGraphicsWidgetPrivate6heightEv(
    const QGraphicsWidgetPrivate *self) {
  return self->height();
}

//  void QGraphicsWidgetPrivate::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate9setHeightEd(
    QGraphicsWidgetPrivate *self,
    qreal a0) {
  self->setHeight(a0);
}

//  void QGraphicsWidgetPrivate::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate11resetHeightEv(
    QGraphicsWidgetPrivate *self) {
  self->resetHeight();
}

//  void QGraphicsWidgetPrivate::setGeometryFromSetPos()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate21setGeometryFromSetPosEv(
    QGraphicsWidgetPrivate *self) {
  self->setGeometryFromSetPos();
}

//  int QGraphicsWidgetPrivate::attributeToBitIndex(Qt::WidgetAttribute att)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK22QGraphicsWidgetPrivate19attributeToBitIndexEN2Qt15WidgetAttributeE(
    const QGraphicsWidgetPrivate *self,
    Qt::WidgetAttribute att) {
  return self->attributeToBitIndex(att);
}

//  void QGraphicsWidgetPrivate::setAttribute(Qt::WidgetAttribute att, bool
//      value)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate12setAttributeEN2Qt15WidgetAttributeEb(
    QGraphicsWidgetPrivate *self,
    Qt::WidgetAttribute att,
    bool value) {
  self->setAttribute(att, value);
}

//  bool QGraphicsWidgetPrivate::testAttribute(Qt::WidgetAttribute att) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK22QGraphicsWidgetPrivate13testAttributeEN2Qt15WidgetAttributeE(
    const QGraphicsWidgetPrivate *self,
    Qt::WidgetAttribute att) {
  return self->testAttribute(att);
}

//  void QGraphicsWidgetPrivate::ensureWindowData()
extern "C" Q_DECL_EXPORT
void ritual_ZN22QGraphicsWidgetPrivate16ensureWindowDataEv(
    QGraphicsWidgetPrivate *self) {
  self->ensureWindowData();
}

//  void QGraphicsWidgetPrivate::ensureWindowFrameMargins() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QGraphicsWidgetPrivate24ensureWindowFrameMarginsEv(
    const QGraphicsWidgetPrivate *self) {
  self->ensureWindowFrameMargins();
}

//  a Python function taken by a CuteQGraphicsWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsWidgetPrivate(
    QGraphicsWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsWidgetPrivate *>(self)->take(key, call);
}

//  void QGraphicsWidgetPrivate::resolvePalette(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate14resolvePaletteEj(
    QGraphicsWidgetPrivate *self,
    uint inheritedMask) {
  self->QGraphicsWidgetPrivate::resolvePalette(inheritedMask);
}

//  void QGraphicsWidgetPrivate::resolveFont(uint inheritedMask)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate11resolveFontEj(
    QGraphicsWidgetPrivate *self,
    uint inheritedMask) {
  self->QGraphicsWidgetPrivate::resolveFont(inheritedMask);
}

//  qreal QGraphicsWidgetPrivate::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QGraphicsWidgetPrivate5widthEv(
    const QGraphicsWidgetPrivate *self) {
  return self->QGraphicsWidgetPrivate::width();
}

//  void QGraphicsWidgetPrivate::setWidth(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate8setWidthEd(
    QGraphicsWidgetPrivate *self,
    qreal a0) {
  self->QGraphicsWidgetPrivate::setWidth(a0);
}

//  void QGraphicsWidgetPrivate::resetWidth()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate10resetWidthEv(
    QGraphicsWidgetPrivate *self) {
  self->QGraphicsWidgetPrivate::resetWidth();
}

//  qreal QGraphicsWidgetPrivate::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_own_ZNK22QGraphicsWidgetPrivate6heightEv(
    const QGraphicsWidgetPrivate *self) {
  return self->QGraphicsWidgetPrivate::height();
}

//  void QGraphicsWidgetPrivate::setHeight(qreal a0)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate9setHeightEd(
    QGraphicsWidgetPrivate *self,
    qreal a0) {
  self->QGraphicsWidgetPrivate::setHeight(a0);
}

//  void QGraphicsWidgetPrivate::resetHeight()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN22QGraphicsWidgetPrivate11resetHeightEv(
    QGraphicsWidgetPrivate *self) {
  self->QGraphicsWidgetPrivate::resetHeight();
}

#endif  // QT_CONFIG(graphicsview)
#endif  // QT_CONFIG(graphicsview)
