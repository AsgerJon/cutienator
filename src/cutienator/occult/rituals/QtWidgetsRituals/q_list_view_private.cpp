//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlistview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qitemselectionmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qlistview.h"
#include <qabstractitemdelegate.h>
#if QT_CONFIG(accessibility)
#include <qaccessible.h>
#endif
#include <qapplication.h>
#include <qstylepainter.h>
#include <qbitmap.h>
#include <qdebug.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qevent.h>
#include <qlist.h>
#if QT_CONFIG(rubberband)
#include <qrubberband.h>
#endif
#include <qscrollbar.h>
#include <qstyle.h>
#include <private/qapplication_p.h>
#include <private/qlistview_p.h>
#include <private/qscrollbar_p.h>
#include <algorithm>
#include "qabstractitemview.h"
#include <qpointer.h>
#include <qapplication.h>
#include <qclipboard.h>
#include <qpainter.h>
#include <qstyle.h>
#if QT_CONFIG(draganddrop)
#include <qdrag.h>
#endif
#include <qevent.h>
#include <qscrollbar.h>
#if QT_CONFIG(tooltip)
#include <qtooltip.h>
#endif
#include <qdatetime.h>
#if QT_CONFIG(lineedit)
#include <qlineedit.h>
#endif
#if QT_CONFIG(spinbox)
#include <qspinbox.h>
#endif
#include <qheaderview.h>
#include <qstyleditemdelegate.h>
#include <private/qabstractitemview_p.h>
#include <private/qabstractitemmodel_p.h>
#include <private/qapplication_p.h>
#include <private/qguiapplication_p.h>
#include <private/qscrollbar_p.h>
#if QT_CONFIG(accessibility)
#include <qaccessible.h>
#endif
#if QT_CONFIG(gestures) && QT_CONFIG(scroller)
#  include <qscroller.h>
#endif
#include <algorithm>
#include "qabstractscrollarea.h"
#if QT_CONFIG(scrollarea)
#include "qscrollbar.h"
#include "qapplication.h"
#include "qstyle.h"
#include "qstyleoption.h"
#include "qevent.h"
#include "qdebug.h"
#include "qboxlayout.h"
#include "qpainter.h"
#include "qmargins.h"
#if QT_CONFIG(itemviews)
#include "qheaderview.h"
#endif
#include <QDebug>
#include "qabstractscrollarea_p.h"
#include "qscrollbar_p.h"
#include <qwidget.h>
#include <private/qguiapplication_p.h>
#include <qpa/qplatformtheme.h>
#include <private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <qt_windows.h>
#endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qlistview.cpp, line 2216, as _ZN17QListModeViewBase6dropOnEP10QDropEventPiS2_P11QModelIndex
#if QT_CONFIG(draganddrop)
inline bool QListModeViewBase::dropOn(QDropEvent *event, int *dropRow, int *dropCol, QModelIndex *dropIndex)
{
    if (event->isAccepted())
        return false;

    QModelIndex index;
    if (dd->viewport->rect().contains(event->position().toPoint())) {
        // can't use indexAt, doesn't account for spacing.
        QPoint p = event->position().toPoint();
        QRect rect(p.x() + horizontalOffset(), p.y() + verticalOffset(), 1, 1);
        rect.adjust(-dd->spacing(), -dd->spacing(), dd->spacing(), dd->spacing());
        const QList<QModelIndex> intersectVector = dd->intersectingSet(rect);
        index = intersectVector.size() > 0
            ? intersectVector.last() : QModelIndex();
        if (!index.isValid())
            index = dd->root;
    }

    // If we are allowed to do the drop
    if (dd->model->supportedDropActions() & event->dropAction()) {
        int row = -1;
        int col = -1;
        if (index != dd->root) {
            dd->dropIndicatorPosition = position(event->position().toPoint(), qq->visualRect(index), index);
            switch (dd->dropIndicatorPosition) {
            case QAbstractItemView::AboveItem:
                row = index.row();
                col = index.column();
                index = index.parent();
                break;
            case QAbstractItemView::BelowItem:
                row = index.row() + 1;
                col = index.column();
                index = index.parent();
                break;
            case QAbstractItemView::OnItem:
            case QAbstractItemView::OnViewport:
                break;
            }
        } else {
            dd->dropIndicatorPosition = QAbstractItemView::OnViewport;
        }
        *dropIndex = index;
        *dropRow = row;
        *dropCol = col;
        if (!dd->droppingOnItself(event, index))
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3594, as _ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii
inline void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &index, int start, int end)
{
    Q_UNUSED(index);
    Q_UNUSED(start);
    Q_UNUSED(end);

    Q_Q(QAbstractItemView);
    if (q->isVisible())
        q->updateEditorGeometries();
    q->setState(QAbstractItemView::NoState);
#if QT_CONFIG(accessibility)
    if (QAccessible::isActive()) {
        QAccessibleTableModelChangeEvent accessibleEvent(q, QAccessibleTableModelChangeEvent::RowsRemoved);
        accessibleEvent.setFirstRow(start);
        accessibleEvent.setLastRow(end);
        QAccessible::updateAccessibility(&accessibleEvent);
    }
#endif
    updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3786, as _ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i
inline void QAbstractItemViewPrivate::columnsMoved(const QModelIndex &, int, int, const QModelIndex &, int)
{
    layoutChanged();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3712, as _ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii
inline void QAbstractItemViewPrivate::rowsInserted(const QModelIndex &index, int start, int end)
{
    Q_UNUSED(index);
    Q_UNUSED(start);
    Q_UNUSED(end);

#if QT_CONFIG(accessibility)
    Q_Q(QAbstractItemView);
    if (QAccessible::isActive()) {
        QAccessibleTableModelChangeEvent accessibleEvent(q, QAccessibleTableModelChangeEvent::RowsInserted);
        accessibleEvent.setFirstRow(start);
        accessibleEvent.setLastRow(end);
        QAccessible::updateAccessibility(&accessibleEvent);
    }
#endif
    updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3769, as _ZN24QAbstractItemViewPrivate13layoutChangedEv
inline void QAbstractItemViewPrivate::layoutChanged()
{
    doDelayedItemsLayout();
#if QT_CONFIG(accessibility)
    Q_Q(QAbstractItemView);
    if (QAccessible::isActive()) {
        QAccessibleTableModelChangeEvent accessibleEvent(q, QAccessibleTableModelChangeEvent::ModelReset);
        QAccessible::updateAccessibility(&accessibleEvent);
    }
#endif
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3685, as _ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii
inline void QAbstractItemViewPrivate::columnsRemoved(const QModelIndex &index, int start, int end)
{
    Q_UNUSED(index);
    Q_UNUSED(start);
    Q_UNUSED(end);

    Q_Q(QAbstractItemView);
    if (q->isVisible())
        q->updateEditorGeometries();
    q->setState(QAbstractItemView::NoState);
#if QT_CONFIG(accessibility)
    if (QAccessible::isActive()) {
        QAccessibleTableModelChangeEvent accessibleEvent(q, QAccessibleTableModelChangeEvent::ColumnsRemoved);
        accessibleEvent.setFirstColumn(start);
        accessibleEvent.setLastColumn(end);
        QAccessible::updateAccessibility(&accessibleEvent);
    }
#endif
    updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3758, as _ZN24QAbstractItemViewPrivate14modelDestroyedEv
inline void QAbstractItemViewPrivate::modelDestroyed()
{
    model = QAbstractItemModelPrivate::staticEmptyModel();
    doDelayedReset();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3735, as _ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii
inline void QAbstractItemViewPrivate::columnsInserted(const QModelIndex &index, int start, int end)
{
    Q_UNUSED(index);
    Q_UNUSED(start);
    Q_UNUSED(end);

    Q_Q(QAbstractItemView);
    if (q->isVisible())
        q->updateEditorGeometries();
#if QT_CONFIG(accessibility)
    if (QAccessible::isActive()) {
        QAccessibleTableModelChangeEvent accessibleEvent(q, QAccessibleTableModelChangeEvent::ColumnsInserted);
        accessibleEvent.setFirstColumn(start);
        accessibleEvent.setLastColumn(end);
        QAccessible::updateAccessibility(&accessibleEvent);
    }
#endif
    updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 2247, as _ZN24QAbstractItemViewPrivate6dropOnEP10QDropEventPiS2_P11QModelIndex
#if QT_CONFIG(draganddrop)
inline bool QAbstractItemViewPrivate::dropOn(QDropEvent *event, int *dropRow, int *dropCol, QModelIndex *dropIndex)
{
    Q_Q(QAbstractItemView);
    if (event->isAccepted())
        return false;

    QModelIndex index;
    // rootIndex() (i.e. the viewport) might be a valid index
    if (viewport->rect().contains(event->position().toPoint())) {
        index = q->indexAt(event->position().toPoint());
        if (!index.isValid())
            index = root;
    }

    // If we are allowed to do the drop
    if (model->supportedDropActions() & event->dropAction()) {
        int row = -1;
        int col = -1;
        if (index != root) {
            dropIndicatorPosition = position(event->position().toPoint(), q->visualRect(index), index);
            switch (dropIndicatorPosition) {
            case QAbstractItemView::AboveItem:
                row = index.row();
                col = index.column();
                index = index.parent();
                break;
            case QAbstractItemView::BelowItem:
                row = index.row() + 1;
                col = index.column();
                index = index.parent();
                break;
            case QAbstractItemView::OnItem:
            case QAbstractItemView::OnViewport:
                break;
            }
        } else {
            dropIndicatorPosition = QAbstractItemView::OnViewport;
        }
        *dropIndex = index;
        *dropRow = row;
        *dropCol = col;
        if (!droppingOnItself(event, index))
            return true;
    }
    return false;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3781, as _ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i
inline void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &, int, int, const QModelIndex &, int)
{
    layoutChanged();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 46, as _ZN24QAbstractItemViewPrivateC2Ev
inline QAbstractItemViewPrivate::QAbstractItemViewPrivate()
    :   model(QAbstractItemModelPrivate::staticEmptyModel()),
        itemDelegate(nullptr),
        selectionModel(nullptr),
        ctrlDragSelectionFlag(QItemSelectionModel::NoUpdate),
        noSelectionOnMousePress(false),
        selectionMode(QAbstractItemView::ExtendedSelection),
        selectionBehavior(QAbstractItemView::SelectItems),
        currentlyCommittingEditor(nullptr),
        pressClosedEditor(false),
        waitForIMCommit(false),
        pressedModifiers(Qt::NoModifier),
        pressedPosition(QPoint(-1, -1)),
        pressedAlreadySelected(false),
        releaseFromDoubleClick(false),
        viewportEnteredNeeded(false),
        state(QAbstractItemView::NoState),
        stateBeforeAnimation(QAbstractItemView::NoState),
        editTriggers(QAbstractItemView::DoubleClicked|QAbstractItemView::EditKeyPressed),
        lastTrigger(QAbstractItemView::NoEditTriggers),
        tabKeyNavigation(false),
#if QT_CONFIG(draganddrop)
        showDropIndicator(true),
        dragEnabled(false),
        dragDropMode(QAbstractItemView::NoDragDrop),
        overwrite(false),
        dropEventMoved(false),
        dropIndicatorPosition(QAbstractItemView::OnItem),
        defaultDropAction(Qt::IgnoreAction),
#endif
        autoScroll(true),
        autoScrollMargin(16),
        autoScrollCount(0),
        shouldScrollToCurrentOnShow(false),
        shouldClearStatusTip(false),
        alternatingColors(false),
        textElideMode(Qt::ElideRight),
        verticalScrollMode(QAbstractItemView::ScrollPerItem),
        horizontalScrollMode(QAbstractItemView::ScrollPerItem),
        currentIndexSet(false),
        wrapItemText(false),
        delayedPendingLayout(true),
        moveCursorUpdatedView(false),
        verticalScrollModeSet(false),
        horizontalScrollModeSet(false),
        updateThreshold(200)
{
    keyboardInputTime.invalidate();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 96, as _ZN24QAbstractItemViewPrivateD2Ev
inline QAbstractItemViewPrivate::~QAbstractItemViewPrivate()
{
}

//  from src/widgets/itemviews/qlistview.cpp, line 2109, as _ZNK17QListModeViewBase8positionERK6QPointRK5QRectRK11QModelIndex
#if QT_CONFIG(draganddrop)
inline QAbstractItemView::DropIndicatorPosition QListModeViewBase::position(const QPoint &pos, const QRect &rect, const QModelIndex &index) const
{
    QAbstractItemView::DropIndicatorPosition r = QAbstractItemView::OnViewport;
    if (!dd->overwrite) {
        const int margin = 2;
        if (pos.x() - rect.left() < margin) {
            r = QAbstractItemView::AboveItem;   // Visually, on the left
        } else if (rect.right() - pos.x() < margin) {
            r = QAbstractItemView::BelowItem;   // Visually, on the right
        } else if (rect.contains(pos, true)) {
            r = QAbstractItemView::OnItem;
        }
    } else {
        QRect touchingRect = rect;
        touchingRect.adjust(-1, -1, 1, 1);
        if (touchingRect.contains(pos, false)) {
            r = QAbstractItemView::OnItem;
        }
    }

    if (r == QAbstractItemView::OnItem && (!(dd->model->flags(index) & Qt::ItemIsDropEnabled)))
        r = pos.x() < rect.center().x() ? QAbstractItemView::AboveItem : QAbstractItemView::BelowItem;

    return r;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3791, as _ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_
inline QRect QAbstractItemViewPrivate::intersectedRect(const QRect rect, const QModelIndex &topLeft, const QModelIndex &bottomRight) const
{
    Q_Q(const QAbstractItemView);

    const auto parentIdx = topLeft.parent();
    QRect updateRect;
    for (int r = topLeft.row(); r <= bottomRight.row(); ++r) {
        for (int c = topLeft.column(); c <= bottomRight.column(); ++c)
            updateRect |= q->visualRect(model->index(r, c, parentIdx));
    }
    return rect.intersected(updateRect);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4452, as _ZNK24QAbstractItemViewPrivate27interruptDelayedItemsLayoutEv
inline void QAbstractItemViewPrivate::interruptDelayedItemsLayout() const
{
    delayedLayout.stop();
    delayedPendingLayout = false;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 2294, as _ZNK24QAbstractItemViewPrivate8positionERK6QPointRK5QRectRK11QModelIndex
#if QT_CONFIG(draganddrop)
inline QAbstractItemView::DropIndicatorPosition
QAbstractItemViewPrivate::position(const QPoint &pos, const QRect &rect, const QModelIndex &index) const
{
    QAbstractItemView::DropIndicatorPosition r = QAbstractItemView::OnViewport;
    if (!overwrite) {
        const int margin = qBound(2, qRound(qreal(rect.height()) / 5.5), 12);
        if (pos.y() - rect.top() < margin) {
            r = QAbstractItemView::AboveItem;
        } else if (rect.bottom() - pos.y() < margin) {
            r = QAbstractItemView::BelowItem;
        } else if (rect.contains(pos, true)) {
            r = QAbstractItemView::OnItem;
        }
    } else {
        QRect touchingRect = rect;
        touchingRect.adjust(-1, -1, 1, 1);
        if (touchingRect.contains(pos, false)) {
            r = QAbstractItemView::OnItem;
        }
    }

    if (r == QAbstractItemView::OnItem && (!(model->flags(index) & Qt::ItemIsDropEnabled)))
        r = pos.y() < rect.center().y() ? QAbstractItemView::AboveItem : QAbstractItemView::BelowItem;

    return r;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1315, as _ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint
#if QT_CONFIG(scrollarea)
inline bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint &startPos) const
{
    Q_Q(const QAbstractScrollArea);

    // don't start scrolling on a QAbstractSlider
    if (qobject_cast<QAbstractSlider *>(q->viewport()->childAt(startPos)))
        return false;

    return true;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 288, as _ZN26QAbstractScrollAreaPrivate14layoutChildrenEv
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::layoutChildren()
{
    bool needH = false;
    bool needV = false;
    layoutChildren_helper(&needH, &needV);
    // Call a second time if one scrollbar was needed and not the other to
    // check if it needs to readjust accordingly
    if (needH != needV)
        layoutChildren_helper(&needH, &needV);
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 299, as _ZN26QAbstractScrollAreaPrivate21layoutChildren_helperEPbS0_
#if QT_CONFIG(scrollarea)
inline void QAbstractScrollAreaPrivate::layoutChildren_helper(bool *needHorizontalScrollbar, bool *needVerticalScrollbar)
{
    Q_Q(QAbstractScrollArea);
    QStyleOptionSlider barOpt;

    hbar->initStyleOption(&barOpt);
    bool htransient = hbar->style()->styleHint(QStyle::SH_ScrollBar_Transient, &barOpt, hbar);
    bool needh = *needHorizontalScrollbar || ((hbarpolicy != Qt::ScrollBarAlwaysOff) && ((hbarpolicy == Qt::ScrollBarAlwaysOn && !htransient)
                            || ((hbarpolicy == Qt::ScrollBarAsNeeded || htransient)
                            && hbar->minimum() < hbar->maximum() && !hbar->sizeHint().isEmpty())));
    const int hscrollOverlap = hbar->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarOverlap, &barOpt, hbar);

    vbar->initStyleOption(&barOpt);
    bool vtransient = vbar->style()->styleHint(QStyle::SH_ScrollBar_Transient, &barOpt, vbar);
    bool needv = *needVerticalScrollbar || ((vbarpolicy != Qt::ScrollBarAlwaysOff) && ((vbarpolicy == Qt::ScrollBarAlwaysOn && !vtransient)
                            || ((vbarpolicy == Qt::ScrollBarAsNeeded || vtransient)
                            && vbar->minimum() < vbar->maximum() && !vbar->sizeHint().isEmpty())));
    const int vscrollOverlap = vbar->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarOverlap, &barOpt, vbar);

    QStyleOption opt(0);
    opt.initFrom(q);

    const int hsbExt = hbar->sizeHint().height();
    const int vsbExt = vbar->sizeHint().width();
    const QPoint extPoint(vsbExt, hsbExt);
    const QSize extSize(vsbExt, hsbExt);

    const QRect widgetRect = q->rect();

    const bool hasCornerWidget = (cornerWidget != nullptr);

    QPoint cornerOffset((needv && vscrollOverlap == 0) ? vsbExt : 0, (needh && hscrollOverlap == 0) ? hsbExt : 0);
    QRect controlsRect;
    QRect viewportRect;

    // In FrameOnlyAroundContents mode the frame is drawn between the controls and
    // the viewport, else the frame rect is equal to the widget rect.
    if ((frameStyle != QFrame::NoFrame) &&
        q->style()->styleHint(QStyle::SH_ScrollView_FrameOnlyAroundContents, &opt, q)) {
        controlsRect = widgetRect;
        const int spacing = q->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarSpacing, &opt, q);
        const QPoint cornerExtra(needv ? spacing + vscrollOverlap : 0, needh ? spacing + hscrollOverlap : 0);
        QRect frameRect = widgetRect;
        frameRect.adjust(0, 0, -cornerOffset.x() - cornerExtra.x(), -cornerOffset.y() - cornerExtra.y());
        q->setFrameRect(QStyle::visualRect(opt.direction, opt.rect, frameRect));
        // The frame rect needs to be in logical coords, however we need to flip
        // the contentsRect back before passing it on to the viewportRect
        // since the viewportRect has its logical coords calculated later.
        viewportRect = QStyle::visualRect(opt.direction, opt.rect, q->contentsRect());
    } else {
        q->setFrameRect(QStyle::visualRect(opt.direction, opt.rect, widgetRect));
        controlsRect = q->contentsRect();
        viewportRect = QRect(controlsRect.topLeft(), controlsRect.bottomRight() - cornerOffset);
    }

    cornerOffset = QPoint(needv ? vsbExt : 0, needh ? hsbExt : 0);

    // If we have a corner widget and are only showing one scroll bar, we need to move it
    // to make room for the corner widget.
    if (hasCornerWidget && ((needv && vscrollOverlap == 0) || (needh && hscrollOverlap == 0)))
        cornerOffset =  extPoint;

    // The corner point is where the scroll bar rects, the corner widget rect and the
    // viewport rect meets.
    const QPoint cornerPoint(controlsRect.bottomRight() + QPoint(1, 1) - cornerOffset);

    // Some styles paints the corner if both scorllbars are showing and there is
    // no corner widget.
    if (needv && needh && !hasCornerWidget && hscrollOverlap == 0 && vscrollOverlap == 0)
        cornerPaintingRect = QStyle::visualRect(opt.direction, opt.rect, QRect(cornerPoint, extSize));
    else
        cornerPaintingRect = QRect();

    // move the scrollbars away from top/left headers
    int vHeaderRight = 0;
    int hHeaderBottom = 0;
#if QT_CONFIG(itemviews)
    if ((vscrollOverlap > 0 && needv) || (hscrollOverlap > 0 && needh)) {
        const QList<QHeaderView *> headers = q->findChildren<QHeaderView*>();
        if (headers.size() <= 2) {
            for (const QHeaderView *header : headers) {
                const QRect geo = header->geometry();
                if (header->orientation() == Qt::Vertical && header->isVisible() && QStyle::visualRect(opt.direction, opt.rect, geo).left() <= opt.rect.width() / 2)
                    vHeaderRight = QStyle::visualRect(opt.direction, opt.rect, geo).right();
                else if (header->orientation() == Qt::Horizontal && header->isVisible() && geo.top() <= q->frameWidth())
                    hHeaderBottom = geo.bottom();
             }
         }
    }
#endif // QT_CONFIG(itemviews)
    if (needh) {
        QRect horizontalScrollBarRect(QPoint(controlsRect.left() + vHeaderRight, cornerPoint.y()), QPoint(cornerPoint.x() - 1, controlsRect.bottom()));

        if (!hasCornerWidget && htransient)
            horizontalScrollBarRect.adjust(0, 0, cornerOffset.x(), 0);
        scrollBarContainers[Qt::Horizontal]->setGeometry(QStyle::visualRect(opt.direction, opt.rect, horizontalScrollBarRect));
        scrollBarContainers[Qt::Horizontal]->raise();
    }

    if (needv) {
        QRect verticalScrollBarRect  (QPoint(cornerPoint.x(), controlsRect.top() + hHeaderBottom),  QPoint(controlsRect.right(), cornerPoint.y() - 1));
        if (!hasCornerWidget && vtransient)
            verticalScrollBarRect.adjust(0, 0, 0, cornerOffset.y());
        scrollBarContainers[Qt::Vertical]->setGeometry(QStyle::visualRect(opt.direction, opt.rect, verticalScrollBarRect));
        scrollBarContainers[Qt::Vertical]->raise();
    }

    if (cornerWidget) {
        const QRect cornerWidgetRect(cornerPoint, controlsRect.bottomRight());
        cornerWidget->setGeometry(QStyle::visualRect(opt.direction, opt.rect, cornerWidgetRect));
    }

    scrollBarContainers[Qt::Horizontal]->setVisible(needh);
    scrollBarContainers[Qt::Vertical]->setVisible(needv);

    if (q->isRightToLeft())
        viewportRect.adjust(right, top, -left, -bottom);
    else
        viewportRect.adjust(left, top, -right, -bottom);
    viewportRect = QStyle::visualRect(opt.direction, opt.rect, viewportRect);
    viewportRect.translate(-overshoot);
    viewport->setGeometry(viewportRect); // resize the viewport last

    *needHorizontalScrollbar = needh;
    *needVerticalScrollbar = needv;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/itemviews/qlistview.cpp, line 1747, as _ZN16QListViewPrivateD1Ev
inline QListViewPrivate::~QListViewPrivate()
{
    delete commonListView;
}

//  from src/widgets/itemviews/qlistview.cpp, line 1752, as _ZN16QListViewPrivate5clearEv
inline void QListViewPrivate::clear()
{
    // initialization of data structs
    cachedItemSize = QSize();
    commonListView->clear();
}

//  from src/widgets/itemviews/qlistview.cpp, line 1759, as _ZN16QListViewPrivate18prepareItemsLayoutEv
inline void QListViewPrivate::prepareItemsLayout()
{
    Q_Q(QListView);
    clear();

    //take the size as if there were scrollbar in order to prevent scrollbar to blink
    layoutBounds = QRect(QPoint(), q->maximumViewportSize());

    int frameAroundContents = 0;
    if (q->style()->styleHint(QStyle::SH_ScrollView_FrameOnlyAroundContents, nullptr, q)) {
        QStyleOption option;
        option.initFrom(q);
        frameAroundContents = q->style()->pixelMetric(QStyle::PM_DefaultFrameWidth, &option, q) * 2;
    }

    // maximumViewportSize() already takes scrollbar into account if policy is
    // Qt::ScrollBarAlwaysOn but scrollbar extent must be deduced if policy
    // is Qt::ScrollBarAsNeeded
    int verticalMargin = (vbarpolicy == Qt::ScrollBarAsNeeded) && (flow == QListView::LeftToRight || vbar->isVisible())
                        && !q->style()->pixelMetric(QStyle::PM_ScrollView_ScrollBarOverlap, nullptr, vbar)
        ? q->style()->pixelMetric(QStyle::PM_ScrollBarExtent, nullptr, vbar) + frameAroundContents
        : 0;
    int horizontalMargin =  hbarpolicy==Qt::ScrollBarAsNeeded
        ? q->style()->pixelMetric(QStyle::PM_ScrollBarExtent, nullptr, hbar) + frameAroundContents
        : 0;

    layoutBounds.adjust(0, 0, -verticalMargin, -horizontalMargin);

    int rowCount = model->columnCount(root) <= 0 ? 0 : model->rowCount(root);
    commonListView->setRowCount(rowCount);
}

//  from src/widgets/itemviews/qlistview.cpp, line 1794, as _ZN16QListViewPrivate13doItemsLayoutEi
inline bool QListViewPrivate::doItemsLayout(int delta)
{
    int max = model->rowCount(root) - 1;
    int first = batchStartRow();
    int last = qMin(first + delta - 1, max);

    if (first == 0) {
        layoutChildren(); // make sure the viewport has the right size
        prepareItemsLayout();
    }

    if (max < 0 || last < first) {
        return true; // nothing to do
    }

    QListViewLayoutInfo info;
    info.bounds = layoutBounds;
    info.grid = gridSize();
    info.spacing = (info.grid.isValid() ? 0 : spacing());
    info.first = first;
    info.last = last;
    info.wrap = isWrapping();
    info.flow = flow;
    info.max = max;

    return commonListView->doBatchedItemLayout(info, max);
}

//  from src/widgets/itemviews/qlistview.cpp, line 1822, as _ZNK16QListViewPrivate19indexToListViewItemERK11QModelIndex
inline QListViewItem QListViewPrivate::indexToListViewItem(const QModelIndex &index) const
{
    if (!index.isValid() || isHidden(index.row()))
        return QListViewItem();

    return commonListView->indexToListViewItem(index);
}

//  from src/widgets/itemviews/qlistview.cpp, line 1830, as _ZNK16QListViewPrivate13mapToViewportERK5QRectb
inline QRect QListViewPrivate::mapToViewport(const QRect &rect, bool extend) const
{
    Q_Q(const QListView);
    if (!rect.isValid())
        return rect;

    QRect result = extend ? commonListView->mapToViewport(rect) : rect;
    int dx = -q->horizontalOffset();
    int dy = -q->verticalOffset();
    return result.adjusted(dx, dy, dx, dy);
}

//  from src/widgets/itemviews/qlistview.cpp, line 1842, as _ZNK16QListViewPrivate12closestIndexERK5QRectRK5QListI11QModelIndexE
inline QModelIndex QListViewPrivate::closestIndex(const QRect &target,
                                           const QList<QModelIndex> &candidates) const
{
    int distance = 0;
    int shortest = INT_MAX;
    QModelIndex closest;
    QList<QModelIndex>::const_iterator it = candidates.begin();

    for (; it != candidates.end(); ++it) {
        if (!(*it).isValid())
            continue;

        const QRect indexRect = indexToListViewItem(*it).rect();

        //if the center x (or y) position of an item is included in the rect of the other item,
        //we define the distance between them as the difference in x (or y) of their respective center.
        // Otherwise, we use the nahattan  length between the 2 items
        if ((target.center().x() >= indexRect.x() && target.center().x() < indexRect.right())
            || (indexRect.center().x() >= target.x() && indexRect.center().x() < target.right())) {
                //one item's center is at the vertical of the other
                distance = qAbs(indexRect.center().y() - target.center().y());
        } else if ((target.center().y() >= indexRect.y() && target.center().y() < indexRect.bottom())
            || (indexRect.center().y() >= target.y() && indexRect.center().y() < target.bottom())) {
                //one item's center is at the vertical of the other
                distance = qAbs(indexRect.center().x() - target.center().x());
        } else {
            distance = (indexRect.center() - target.center()).manhattanLength();
        }
        if (distance < shortest) {
            shortest = distance;
            closest = *it;
        }
    }
    return closest;
}

//  from src/widgets/itemviews/qlistview.cpp, line 1878, as _ZNK16QListViewPrivate8itemSizeERK20QStyleOptionViewItemRK11QModelIndex
inline QSize QListViewPrivate::itemSize(const QStyleOptionViewItem &option, const QModelIndex &index) const
{
    Q_Q(const QListView);
    if (!uniformItemSizes) {
        const QAbstractItemDelegate *delegate = q->itemDelegateForIndex(index);
        return delegate ? delegate->sizeHint(option, index) : QSize();
    }
    if (!cachedItemSize.isValid()) { // the last item is probably the largest, so we use its size
        int row = model->rowCount(root) - 1;
        QModelIndex sample = model->index(row, column, root);
        const QAbstractItemDelegate *delegate = q->itemDelegateForIndex(sample);
        cachedItemSize = delegate ? delegate->sizeHint(option, sample) : QSize();
    }
    return cachedItemSize;
}

//  from src/widgets/itemviews/qlistview.cpp, line 1894, as _ZNK16QListViewPrivate9selectionERK5QRect
inline QItemSelection QListViewPrivate::selection(const QRect &rect) const
{
    QItemSelection selection;
    QModelIndex tl, br;
    const QList<QModelIndex> intersectVector = intersectingSet(rect);
    QList<QModelIndex>::const_iterator it = intersectVector.begin();
    for (; it != intersectVector.end(); ++it) {
        if (!tl.isValid() && !br.isValid()) {
            tl = br = *it;
        } else if ((*it).row() == (tl.row() - 1)) {
            tl = *it; // expand current range
        } else if ((*it).row() == (br.row() + 1)) {
            br = (*it); // expand current range
        } else {
            selection.select(tl, br); // select current range
            tl = br = *it; // start new range
        }
    }

    if (tl.isValid() && br.isValid())
        selection.select(tl, br);
    else if (tl.isValid())
        selection.select(tl, tl);
    else if (br.isValid())
        selection.select(br, br);

    return selection;
}

//  from src/widgets/itemviews/qlistview.cpp, line 575, as _ZN16QListViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE
inline void QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags command)
{
    if (!selectionModel)
        return;

    QItemSelection selection;
    QModelIndex topLeft;
    int row = 0;
    const int colCount = model->columnCount(root);
    const int rowCount = model->rowCount(root);
    for ( ; row < rowCount; ++row) {
        if (isHidden(row)) {
            //it might be the end of a selection range
            if (topLeft.isValid()) {
                QModelIndex bottomRight = model->index(row - 1, colCount - 1, root);
                selection.append(QItemSelectionRange(topLeft, bottomRight));
                topLeft = QModelIndex();
            }
            continue;
        }

        if (!topLeft.isValid()) //start of a new selection range
            topLeft = model->index(row, 0, root);
    }

    if (topLeft.isValid()) {
        //last selected range
        QModelIndex bottomRight = model->index(row - 1, colCount - 1, root);
        selection.append(QItemSelectionRange(topLeft, bottomRight));
    }

    if (!selection.isEmpty())
        selectionModel->select(selection, command);
}

//  from src/widgets/itemviews/qlistview.cpp, line 1924, as _ZNK16QListViewPrivate8positionERK6QPointRK5QRectRK11QModelIndex
#if QT_CONFIG(draganddrop)
inline QAbstractItemView::DropIndicatorPosition QListViewPrivate::position(const QPoint &pos, const QRect &rect, const QModelIndex &idx) const
{
    if (viewMode == QListView::ListMode && flow == QListView::LeftToRight)
        return static_cast<QListModeViewBase *>(commonListView)->position(pos, rect, idx);
    else
        return QAbstractItemViewPrivate::position(pos, rect, idx);
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 1932, as _ZN16QListViewPrivate6dropOnEP10QDropEventPiS2_P11QModelIndex
#if QT_CONFIG(draganddrop)
inline bool QListViewPrivate::dropOn(QDropEvent *event, int *dropRow, int *dropCol, QModelIndex *dropIndex)
{
    if (viewMode == QListView::ListMode && flow == QListView::LeftToRight)
        return static_cast<QListModeViewBase *>(commonListView)->dropOn(event, dropRow, dropCol, dropIndex);
    else
        return QAbstractItemViewPrivate::dropOn(event, dropRow, dropCol, dropIndex);
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 1942, as _ZNK16QListViewPrivate20accessibleChildIndexERK11QModelIndex
#if QT_CONFIG(accessibility)
inline int QListViewPrivate::accessibleChildIndex(const QModelIndex &index) const
{
    Q_Q(const QListView);
    Q_ASSERT(index.isValid());
    return q->visualIndex(index);
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/itemviews/qlistview.cpp, line 3354, as _ZN16QListViewPrivate19scrollElasticBandByEii
inline void QListViewPrivate::scrollElasticBandBy(int dx, int dy)
{
    if (dx > 0) // right
        elasticBand.moveRight(elasticBand.right() + dx);
    else if (dx < 0) // left
        elasticBand.moveLeft(elasticBand.left() - dx);
    if (dy > 0) // down
        elasticBand.moveBottom(elasticBand.bottom() + dy);
    else if (dy < 0) // up
        elasticBand.moveTop(elasticBand.top() - dy);
}

//  from src/widgets/itemviews/qlistview.cpp, line 622, as _ZNK16QListViewPrivate19draggablePaintPairsERK5QListI11QModelIndexEP5QRect
inline QItemViewPaintPairs QListViewPrivate::draggablePaintPairs(const QModelIndexList &indexes, QRect *r) const
{
    Q_ASSERT(r);
    Q_Q(const QListView);
    QRect &rect = *r;
    const QRect viewportRect = viewport->rect();
    QItemViewPaintPairs ret;
    QList<QModelIndex> visibleIndexes =
            intersectingSet(viewportRect.translated(q->horizontalOffset(), q->verticalOffset()));
    std::sort(visibleIndexes.begin(), visibleIndexes.end());
    for (const auto &index : indexes) {
        if (std::binary_search(visibleIndexes.cbegin(), visibleIndexes.cend(), index)) {
            const QRect current = q->visualRect(index);
            ret.append({current, index});
            rect |= current;
        }
    }
    QRect clipped = rect & viewportRect;
    rect.setLeft(clipped.left());
    rect.setRight(clipped.right());
    return ret;
}
//  -----------------------------------------------------------------------

//  A QListViewPrivate that Python can take functions over in. Every QListViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQListViewPrivateCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListViewPrivateCall1)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
typedef int (*CuteQListViewPrivateCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall5)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall6)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall7)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall10)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall11)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQListViewPrivateCall12)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListViewPrivateCall13)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQListViewPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQListViewPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQListViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQListViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQListViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQListViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQListViewPrivateCall20)(const void *, int *);
typedef void (*CuteQListViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQListViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQListViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQListViewPrivateCall24)(const void *, int *);
typedef int (*CuteQListViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQListViewPrivateCall26)(const void *, int *);
typedef void (*CuteQListViewPrivateCall27)(const void *, int *);
typedef void (*CuteQListViewPrivateCall28)(const void *, int *);
typedef void (*CuteQListViewPrivateCall29)(const void *, int *);
typedef void (*CuteQListViewPrivateCall30)(const void *, int *);
typedef void (*CuteQListViewPrivateCall31)(const void *, int *);
typedef void (*CuteQListViewPrivateCall32)(const void *, int *);
typedef void (*CuteQListViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQListViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQListViewPrivateCall35)(const void *, int *);
class CuteQListViewPrivate : public QListViewPrivate {
public:
  using QListViewPrivate::QListViewPrivate;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14modelDestroyedEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate13layoutChangedEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN26QAbstractScrollAreaPrivate22scrollBarPolicyChangedEN2Qt11OrientationENS0_15ScrollBarPolicyE")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate19canStartScrollingAtERK6QPoint")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(scrollarea)
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10setVisibleEb")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14setWindowFlagsE6QFlagsIN2Qt10WindowTypeEE")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14aboutToDestroyEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate8recreateEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate11focusObjectEv")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate9rhiConfigEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK14QWidgetPrivate7textureEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate16textureListFlagsEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15grabFramebufferEv")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25beginBackingStorePaintingEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate23endBackingStorePaintingEv")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate12beginComposeEv")) {
      taken[29] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate10endComposeEv")) {
      taken[30] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate29initializeViewportFramebufferEv")) {
      taken[31] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate25resizeViewportFramebufferEv")) {
      taken[32] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate14resolveSamplesEv")) {
      taken[33] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate15isStereoEnabledEv")) {
      taken[34] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QWidgetPrivate24toggleStereoTargetBufferEv")) {
      taken[35] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  bool QListViewPrivate::selectionAllowed(const QModelIndex &index)
  //      const
  bool selectionAllowed(const QModelIndex &index) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQListViewPrivateCall0 call = reinterpret_cast<CuteQListViewPrivateCall0>(taken[0]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListViewPrivate::selectionAllowed(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
  //  void QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
  //      command)
  void selectAll(QItemSelectionModel::SelectionFlags command) override {
    if (taken[1]) {
      int handled = 0;
      CuteQListViewPrivateCall1 call = reinterpret_cast<CuteQListViewPrivateCall1>(taken[1]);
      call(this, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QListViewPrivate::selectAll(command);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
  //  int QListViewPrivate::accessibleChildIndex(const QModelIndex &index)
  //      const
  int accessibleChildIndex(const QModelIndex &index) const override {
    if (taken[2]) {
      int handled = 0;
      CuteQListViewPrivateCall2 call = reinterpret_cast<CuteQListViewPrivateCall2>(taken[2]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QListViewPrivate::accessibleChildIndex(index);
  }
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
  //      int start, int end)
  void rowsRemoved(const QModelIndex &parent, int start, int end) override {
    if (taken[3]) {
      int handled = 0;
      CuteQListViewPrivateCall3 call = reinterpret_cast<CuteQListViewPrivateCall3>(taken[3]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::rowsRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsInserted(const QModelIndex
  //      &parent, int start, int end)
  void rowsInserted(const QModelIndex &parent, int start, int end) override {
    if (taken[4]) {
      int handled = 0;
      CuteQListViewPrivateCall4 call = reinterpret_cast<CuteQListViewPrivateCall4>(taken[4]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::columnsAboutToBeRemoved(const
  //      QModelIndex &parent, int start, int end)
  void columnsAboutToBeRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[5]) {
      int handled = 0;
      CuteQListViewPrivateCall5 call = reinterpret_cast<CuteQListViewPrivateCall5>(taken[5]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsAboutToBeRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::columnsRemoved(const QModelIndex
  //      &parent, int start, int end)
  void columnsRemoved(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[6]) {
      int handled = 0;
      CuteQListViewPrivateCall6 call = reinterpret_cast<CuteQListViewPrivateCall6>(taken[6]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::columnsInserted(const QModelIndex
  //      &parent, int start, int end)
  void columnsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[7]) {
      int handled = 0;
      CuteQListViewPrivateCall7 call = reinterpret_cast<CuteQListViewPrivateCall7>(taken[7]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::modelDestroyed()
  void modelDestroyed() override {
    if (taken[8]) {
      int handled = 0;
      CuteQListViewPrivateCall8 call = reinterpret_cast<CuteQListViewPrivateCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::modelDestroyed();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::layoutChanged()
  void layoutChanged() override {
    if (taken[9]) {
      int handled = 0;
      CuteQListViewPrivateCall9 call = reinterpret_cast<CuteQListViewPrivateCall9>(taken[9]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::layoutChanged();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &source,
  //      int sourceStart, int sourceEnd, const QModelIndex &destination,
  //      int destinationStart)
  void rowsMoved(
      const QModelIndex &source,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destination,
      int destinationStart) override {
    if (taken[10]) {
      int handled = 0;
      CuteQListViewPrivateCall10 call = reinterpret_cast<CuteQListViewPrivateCall10>(taken[10]);
      call(this, &source, sourceStart, sourceEnd, &destination, destinationStart, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::rowsMoved(source, sourceStart, sourceEnd, destination, destinationStart);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::columnsMoved(const QModelIndex
  //      &source, int sourceStart, int sourceEnd, const QModelIndex
  //      &destination, int destinationStart)
  void columnsMoved(
      const QModelIndex &source,
      int sourceStart,
      int sourceEnd,
      const QModelIndex &destination,
      int destinationStart) override {
    if (taken[11]) {
      int handled = 0;
      CuteQListViewPrivateCall11 call = reinterpret_cast<CuteQListViewPrivateCall11>(taken[11]);
      call(this, &source, sourceStart, sourceEnd, &destination, destinationStart, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsMoved(source, sourceStart, sourceEnd, destination, destinationStart);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  QRect QAbstractItemViewPrivate::intersectedRect(const QRect rect,
  //      const QModelIndex &topLeft, const QModelIndex &bottomRight) const
  QRect intersectedRect(
      const QRect rect,
      const QModelIndex &topLeft,
      const QModelIndex &bottomRight) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQListViewPrivateCall12 call = reinterpret_cast<CuteQListViewPrivateCall12>(taken[12]);
      const QRect * given = call(this, &rect, &topLeft, &bottomRight, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemViewPrivate::intersectedRect(rect, topLeft, bottomRight);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::adjustViewOptionsForIndex(QStyleOption
  //      ViewItem *a0, const QModelIndex &a1) const
  void adjustViewOptionsForIndex(
      QStyleOptionViewItem *a0,
      const QModelIndex &a1) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQListViewPrivateCall13 call = reinterpret_cast<CuteQListViewPrivateCall13>(taken[13]);
      call(this, a0, &a1, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::adjustViewOptionsForIndex(a0, a1);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  QPoint QAbstractItemViewPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQListViewPrivateCall14 call = reinterpret_cast<CuteQListViewPrivateCall14>(taken[14]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemViewPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(itemviews)
  //  QRect QAbstractItemViewPrivate::visualRect(const QModelIndex &index)
  //      const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[15]) {
      int handled = 0;
      CuteQListViewPrivateCall15 call = reinterpret_cast<CuteQListViewPrivateCall15>(taken[15]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemViewPrivate::visualRect(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQListViewPrivateCall16 call = reinterpret_cast<CuteQListViewPrivateCall16>(taken[16]);
      call(this, static_cast<int>(a0), static_cast<int>(a1), &handled);
      if (handled) return;
    }
    QAbstractScrollAreaPrivate::scrollBarPolicyChanged(a0, a1);
  }
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  bool QAbstractScrollAreaPrivate::canStartScrollingAt(const QPoint
  //      &startPos) const
  bool canStartScrollingAt(const QPoint &startPos) const override {
    if (taken[17]) {
      int handled = 0;
      CuteQListViewPrivateCall17 call = reinterpret_cast<CuteQListViewPrivateCall17>(taken[17]);
      bool given = call(this, &startPos, &handled);
      if (handled) return given;
    }
    return QAbstractScrollAreaPrivate::canStartScrollingAt(startPos);
  }
#endif  // QT_CONFIG(scrollarea)

  //  void QWidgetPrivate::setVisible(bool a0)
  void setVisible(bool a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQListViewPrivateCall18 call = reinterpret_cast<CuteQListViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQListViewPrivateCall19 call = reinterpret_cast<CuteQListViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQListViewPrivateCall20 call = reinterpret_cast<CuteQListViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQListViewPrivateCall21 call = reinterpret_cast<CuteQListViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQListViewPrivateCall22 call = reinterpret_cast<CuteQListViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQListViewPrivateCall23 call = reinterpret_cast<CuteQListViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQListViewPrivateCall24 call = reinterpret_cast<CuteQListViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQListViewPrivateCall25 call = reinterpret_cast<CuteQListViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQListViewPrivateCall26 call = reinterpret_cast<CuteQListViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQListViewPrivateCall27 call = reinterpret_cast<CuteQListViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQListViewPrivateCall28 call = reinterpret_cast<CuteQListViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQListViewPrivateCall29 call = reinterpret_cast<CuteQListViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQListViewPrivateCall30 call = reinterpret_cast<CuteQListViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQListViewPrivateCall31 call = reinterpret_cast<CuteQListViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQListViewPrivateCall32 call = reinterpret_cast<CuteQListViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQListViewPrivateCall33 call = reinterpret_cast<CuteQListViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQListViewPrivateCall34 call = reinterpret_cast<CuteQListViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQListViewPrivateCall35 call = reinterpret_cast<CuteQListViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QListView *QListViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QListView *ritual_ZN16QListViewPrivate6q_funcEv(QListViewPrivate *self) {
  return self->q_func();
}

//  const QListView *QListViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QListView *ritual_ZNK16QListViewPrivate6q_funcEv(
    const QListViewPrivate *self) {
  return self->q_func();
}

//  QListViewPrivate::~QListViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivateD1Ev(QListViewPrivate *self) {
  delete self;
}

//  void QListViewPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate5clearEv(QListViewPrivate *self) {
  self->clear();
}

//  void QListViewPrivate::prepareItemsLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate18prepareItemsLayoutEv(
    QListViewPrivate *self) {
  self->prepareItemsLayout();
}

#if QT_CONFIG(scrollarea)
//  bool QListViewPrivate::doItemsLayout(int num)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QListViewPrivate13doItemsLayoutEi(
    QListViewPrivate *self,
    int num) {
  return self->doItemsLayout(num);
}
#endif  // QT_CONFIG(scrollarea)

//  QList<QModelIndex> QListViewPrivate::intersectingSet(const QRect &area,
//      bool doLayout) const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK16QListViewPrivate15intersectingSetERK5QRectb(
    const QListViewPrivate *self,
    const QRect *area,
    bool doLayout) {
  return new QList<QModelIndex>(self->intersectingSet(*area, doLayout));
}

//  void QListViewPrivate::resetBatchStartRow()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate18resetBatchStartRowEv(
    QListViewPrivate *self) {
  self->resetBatchStartRow();
}

//  int QListViewPrivate::batchStartRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QListViewPrivate13batchStartRowEv(
    const QListViewPrivate *self) {
  return self->batchStartRow();
}

//  QSize QListViewPrivate::contentsSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QListViewPrivate12contentsSizeEv(
    const QListViewPrivate *self) {
  return new QSize(self->contentsSize());
}

//  void QListViewPrivate::setContentsSize(int w, int h)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate15setContentsSizeEii(
    QListViewPrivate *self,
    int w,
    int h) {
  self->setContentsSize(w, h);
}

//  int QListViewPrivate::flipX(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QListViewPrivate5flipXEi(
    const QListViewPrivate *self,
    int x) {
  return self->flipX(x);
}

//  QPoint QListViewPrivate::flipX(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK16QListViewPrivate5flipXERK6QPoint(
    const QListViewPrivate *self,
    const QPoint *p) {
  return new QPoint(self->flipX(*p));
}

//  QRect QListViewPrivate::flipX(const QRect &r) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QListViewPrivate5flipXERK5QRect(
    const QListViewPrivate *self,
    const QRect *r) {
  return new QRect(self->flipX(*r));
}

//  QRect QListViewPrivate::viewItemRect(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QListViewPrivate12viewItemRectERK13QListViewItem(
    const QListViewPrivate *self,
    const QListViewItem *item) {
  return new QRect(self->viewItemRect(*item));
}

//  QListViewItem QListViewPrivate::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZNK16QListViewPrivate19indexToListViewItemERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return new QListViewItem(self->indexToListViewItem(*index));
}

//  QModelIndex QListViewPrivate::listViewItemToIndex(const QListViewItem
//      &item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QListViewPrivate19listViewItemToIndexERK13QListViewItem(
    const QListViewPrivate *self,
    const QListViewItem *item) {
  return new QModelIndex(self->listViewItemToIndex(*item));
}

//  bool QListViewPrivate::hasRectForIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate15hasRectForIndexERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return self->hasRectForIndex(*index);
}

//  QRect QListViewPrivate::rectForIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QListViewPrivate12rectForIndexERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->rectForIndex(*index));
}

//  QRect QListViewPrivate::cellRectForIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
QRect *ritual_ZN16QListViewPrivate16cellRectForIndexERK11QModelIndex(
    QListViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->cellRectForIndex(*index));
}

//  void QListViewPrivate::viewUpdateGeometries()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate20viewUpdateGeometriesEv(
    QListViewPrivate *self) {
  self->viewUpdateGeometries();
}

//  QRect QListViewPrivate::mapToViewport(const QRect &rect, bool extend)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QListViewPrivate13mapToViewportERK5QRectb(
    const QListViewPrivate *self,
    const QRect *rect,
    bool extend) {
  return new QRect(self->mapToViewport(*rect, extend));
}

//  QModelIndex QListViewPrivate::closestIndex(const QRect &target, const
//      QList<QModelIndex> &candidates) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QListViewPrivate12closestIndexERK5QRectRK5QListI11QModelIndexE(
    const QListViewPrivate *self,
    const QRect *target,
    const QList<QModelIndex> *candidates) {
  return new QModelIndex(self->closestIndex(*target, *candidates));
}

//  QSize QListViewPrivate::itemSize(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QListViewPrivate8itemSizeERK20QStyleOptionViewItemRK11QModelIndex(
    const QListViewPrivate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->itemSize(*option, *index));
}

//  bool QListViewPrivate::selectionAllowed(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate16selectionAllowedERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return self->selectionAllowed(*index);
}

//  QItemSelection QListViewPrivate::selection(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK16QListViewPrivate9selectionERK5QRect(
    const QListViewPrivate *self,
    const QRect *rect) {
  return new QItemSelection(self->selection(*rect));
}

//  void QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
//      command)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListViewPrivate *self,
    int command) {
  self->selectAll(
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

#if QT_CONFIG(draganddrop)
//  QAbstractItemView::DropIndicatorPosition QListViewPrivate::position(const
//      QPoint &pos, const QRect &rect, const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DropIndicatorPosition ritual_ZNK16QListViewPrivate8positionERK6QPointRK5QRectRK11QModelIndex(
    const QListViewPrivate *self,
    const QPoint *pos,
    const QRect *rect,
    const QModelIndex *idx) {
  return self->position(*pos, *rect, *idx);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QListViewPrivate::dropOn(QDropEvent *event, int *row, int *col,
//      QModelIndex *index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QListViewPrivate6dropOnEP10QDropEventPiS2_P11QModelIndex(
    QListViewPrivate *self,
    QDropEvent *event,
    int *row,
    int *col,
    QModelIndex *index) {
  return self->dropOn(event, row, col, index);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(accessibility)
//  int QListViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QListViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return self->accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

//  void QListViewPrivate::setGridSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate11setGridSizeERK5QSize(
    QListViewPrivate *self,
    const QSize *size) {
  self->setGridSize(*size);
}

//  QSize QListViewPrivate::gridSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK16QListViewPrivate8gridSizeEv(
    const QListViewPrivate *self) {
  return new QSize(self->gridSize());
}

//  void QListViewPrivate::setWrapping(bool b)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate11setWrappingEb(
    QListViewPrivate *self,
    bool b) {
  self->setWrapping(b);
}

//  bool QListViewPrivate::isWrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate10isWrappingEv(
    const QListViewPrivate *self) {
  return self->isWrapping();
}

//  void QListViewPrivate::setSpacing(int s)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate10setSpacingEi(
    QListViewPrivate *self,
    int s) {
  self->setSpacing(s);
}

//  int QListViewPrivate::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QListViewPrivate7spacingEv(const QListViewPrivate *self) {
  return self->spacing();
}

//  void QListViewPrivate::setSelectionRectVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate23setSelectionRectVisibleEb(
    QListViewPrivate *self,
    bool visible) {
  self->setSelectionRectVisible(visible);
}

//  bool QListViewPrivate::isSelectionRectVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate22isSelectionRectVisibleEv(
    const QListViewPrivate *self) {
  return self->isSelectionRectVisible();
}

//  QModelIndex QListViewPrivate::modelIndex(int row) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QListViewPrivate10modelIndexEi(
    const QListViewPrivate *self,
    int row) {
  return new QModelIndex(self->modelIndex(row));
}

//  bool QListViewPrivate::isHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate8isHiddenEi(
    const QListViewPrivate *self,
    int row) {
  return self->isHidden(row);
}

//  bool QListViewPrivate::isHiddenOrDisabled(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QListViewPrivate18isHiddenOrDisabledEi(
    const QListViewPrivate *self,
    int row) {
  return self->isHiddenOrDisabled(row);
}

//  void QListViewPrivate::scrollElasticBandBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate19scrollElasticBandByEii(
    QListViewPrivate *self,
    int dx,
    int dy) {
  self->scrollElasticBandBy(dx, dy);
}

//  QItemViewPaintPairs QListViewPrivate::draggablePaintPairs(const
//      QModelIndexList &indexes, QRect *r) const
extern "C" Q_DECL_EXPORT
QList<QItemViewPaintPair> *ritual_ZNK16QListViewPrivate19draggablePaintPairsERK5QListI11QModelIndexEP5QRect(
    const QListViewPrivate *self,
    const QList<QModelIndex> *indexes,
    QRect *r) {
  return new QList<QItemViewPaintPair>(
      self->draggablePaintPairs(
          *indexes,
          r));
}

//  void QListViewPrivate::emitIndexesMoved(const QModelIndexList &indexes)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QListViewPrivate16emitIndexesMovedERK5QListI11QModelIndexE(
    QListViewPrivate *self,
    const QList<QModelIndex> *indexes) {
  self->emitIndexesMoved(*indexes);
}

//  a Python function taken by a CuteQListViewPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QListViewPrivate(
    QListViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQListViewPrivate *>(self)->take(key, call);
}

//  bool QListViewPrivate::selectionAllowed(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK16QListViewPrivate16selectionAllowedERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return self->QListViewPrivate::selectionAllowed(*index);
}

//  void QListViewPrivate::selectAll(QItemSelectionModel::SelectionFlags
//      command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QListViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListViewPrivate *self,
    int command) {
  self->QListViewPrivate::selectAll(
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

#if QT_CONFIG(accessibility)
//  int QListViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QListViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QListViewPrivate *self,
    const QModelIndex *index) {
  return self->QListViewPrivate::accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(listview)
