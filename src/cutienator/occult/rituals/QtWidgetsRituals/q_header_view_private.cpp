//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qheaderview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qheaderview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbitarray.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qabstractitemview.h>
#include <QtCore/qpointer.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qclipboard.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qevent.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtCore/qdatetime.h>
#if QT_CONFIG(lineedit)
#include <QtWidgets/qlineedit.h>
#endif
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#endif
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtWidgets/private/qabstractitemview_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#if QT_CONFIG(gestures) && QT_CONFIG(scroller)
#  include <QtWidgets/qscroller.h>
#endif
#include <algorithm>
#include <QtWidgets/qabstractscrollarea.h>
#if QT_CONFIG(scrollarea)
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qevent.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/qboxlayout.h>
#include <QtGui/qpainter.h>
#include <QtCore/qmargins.h>
#if QT_CONFIG(itemviews)
#include <QtWidgets/qheaderview.h>
#endif
#include <QtCore/QDebug>
#include <QtWidgets/private/qabstractscrollarea_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#include <QtWidgets/qwidget.h>
#include <QtGui/private/qguiapplication_p.h>
#include <QtGui/qpa/qplatformtheme.h>
#include <QtWidgets/private/qapplication_p.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/qapplication.h>
#include <QtCore/qbitarray.h>
#include <QtGui/qbrush.h>
#include <QtCore/qdebug.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtGui/qpainterstateguard.h>
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(tooltip)
#include <QtWidgets/qtooltip.h>
#endif
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qvariant.h>
#if QT_CONFIG(whatsthis)
#include <QtWidgets/qwhatsthis.h>
#endif
#include <QtWidgets/private/qheaderview_p.h>
#include <QtCore/private/qabstractitemmodel_p.h>
#include <QtWidgets/private/qabstractitemdelegate_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#ifndef QT_NO_DATASTREAM
#include <QtCore/qdatastream.h>
#endif
#include <QtCore/q26numeric.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/itemviews/qheaderview.cpp, line 3846, as local:qheaderview.cpp:flipOrder
static Qt::SortOrder flipOrder(Qt::SortOrder order)
{
    switch (order) {
    case Qt::AscendingOrder:
        return Qt::DescendingOrder;
    case Qt::DescendingOrder:
        return Qt::AscendingOrder;
    };
    Q_UNREACHABLE_RETURN(Qt::AscendingOrder);
};

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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4748, as _ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE
inline void QAbstractItemViewPrivate::selectAll(QItemSelectionModel::SelectionFlags command)
{
    if (!selectionModel)
        return;
    if (!model->hasChildren(root))
        return;

    QItemSelection selection;
    QModelIndex tl = model->index(0, 0, root);
    QModelIndex br = model->index(model->rowCount(root) - 1,
                                  model->columnCount(root) - 1,
                                  root);
    selection.append(QItemSelectionRange(tl, br));
    selectionModel->select(selection, command);
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4699, as _ZNK24QAbstractItemViewPrivate19draggablePaintPairsERK5QListI11QModelIndexEP5QRect
inline QItemViewPaintPairs QAbstractItemViewPrivate::draggablePaintPairs(const QModelIndexList &indexes, QRect *r) const
{
    Q_ASSERT(r);
    Q_Q(const QAbstractItemView);
    QRect &rect = *r;
    const QRect viewportRect = viewport->rect();
    QItemViewPaintPairs ret;
    for (const auto &index : indexes) {
        const QRect current = q->visualRect(index);
        if (current.intersects(viewportRect)) {
            ret.append({current, index});
            rect |= current;
        }
    }
    QRect clipped = rect & viewportRect;
    rect.setLeft(clipped.left());
    rect.setRight(clipped.right());
    return ret;
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4452, as _ZNK24QAbstractItemViewPrivate27interruptDelayedItemsLayoutEv
inline void QAbstractItemViewPrivate::interruptDelayedItemsLayout() const
{
    delayedLayout.stop();
    delayedPendingLayout = false;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4458, as _ZN24QAbstractItemViewPrivate14updateGeometryEv
inline void QAbstractItemViewPrivate::updateGeometry()
{
    Q_Q(QAbstractItemView);
    if (sizeAdjustPolicy == QAbstractScrollArea::AdjustIgnored)
        return;
    if (sizeAdjustPolicy == QAbstractScrollArea::AdjustToContents || !shownOnce)
        q->updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 2167, as _ZN24QAbstractItemViewPrivate16droppingOnItselfEP10QDropEventRK11QModelIndex
#if QT_CONFIG(draganddrop)
inline bool QAbstractItemViewPrivate::droppingOnItself(QDropEvent *event, const QModelIndex &index)
{
    Q_Q(QAbstractItemView);
    Qt::DropAction dropAction = event->dropAction();
    if (q->dragDropMode() == QAbstractItemView::InternalMove)
        dropAction = Qt::MoveAction;
    if (event->source() == q
        && event->possibleActions() & Qt::MoveAction
        && dropAction == Qt::MoveAction) {
        QModelIndexList selectedIndexes = q->selectedIndexes();
        QModelIndex child = index;
        while (child.isValid() && child != root) {
            if (selectedIndexes.contains(child))
                return true;
            child = child.parent();
        }
    }
    return false;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4444, as _ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi
inline void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
{
    if (!delayedPendingLayout) {
        delayedPendingLayout = true;
        delayedLayout.start(delay, q_func());
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3613, as _ZNK18QHeaderViewPrivate22lastVisibleVisualIndexEv
inline int QHeaderViewPrivate::lastVisibleVisualIndex() const
{
    Q_Q(const QHeaderView);
    for (int visual = q->count()-1; visual >= 0; --visual) {
        if (!q->isSectionHidden(q->logicalIndex(visual)))
            return visual;
    }

    //default value if no section is actually visible
    return -1;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3625, as _ZN18QHeaderViewPrivate28restoreSizeOnPrevLastSectionEv
inline void QHeaderViewPrivate::restoreSizeOnPrevLastSection()
{
    Q_Q(QHeaderView);
    if (lastSectionLogicalIdx < 0)
        return;
    int resizeLogIdx = lastSectionLogicalIdx;
    lastSectionLogicalIdx = -1; // We do not want resize to catch it as the last section.
    q->resizeSection(resizeLogIdx, lastSectionSize);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3635, as _ZN18QHeaderViewPrivate17setNewLastSectionEi
inline void QHeaderViewPrivate::setNewLastSection(int visualIndexForLastSection)
{
    Q_Q(QHeaderView);
    lastSectionSize = -1;
    lastSectionLogicalIdx = q->logicalIndex(visualIndexForLastSection);
    lastSectionSize = headerSectionSize(visualIndexForLastSection); // pick size directly since ...
    //  q->sectionSize(lastSectionLogicalIdx) may do delayed resize and stretch it before we get the value.
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3644, as _ZN18QHeaderViewPrivate41maybeRestorePrevLastSectionAndStretchLastEv
inline void QHeaderViewPrivate::maybeRestorePrevLastSectionAndStretchLast()
{
    Q_Q(const QHeaderView);
    if (!q->stretchLastSection())
        return;

    int nowLastVisualSection = lastVisibleVisualIndex();
    if (lastSectionLogicalIdx == q->logicalIndex(nowLastVisualSection))
        return;

    // restore old last section.
    restoreSizeOnPrevLastSection();
    setNewLastSection(nowLastVisualSection);
    doDelayedResizeSections(); // Do stretch of last section soon (but not now).
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3445, as _ZN18QHeaderViewPrivate15sectionHandleAtEi
inline int QHeaderViewPrivate::sectionHandleAt(int position)
{
    Q_Q(QHeaderView);
    int visual = q->visualIndexAt(position);
    if (visual == -1)
        return -1;
    int log = logicalIndex(visual);
    int pos = q->sectionViewportPosition(log);
    int grip = q->style()->pixelMetric(QStyle::PM_HeaderGripMargin, nullptr, q);

    bool atLeft = position < pos + grip;
    bool atRight = (position > pos + q->sectionSize(log) - grip);
    if (reverse())
        qSwap(atLeft, atRight);

    if (atLeft) {
        //grip at the beginning of the section
        while(visual > -1) {
            int logical = q->logicalIndex(--visual);
            if (!q->isSectionHidden(logical))
                return logical;
        }
    } else if (atRight) {
        //grip at the end of the section
        return log;
    }
    return -1;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3474, as _ZN18QHeaderViewPrivate21setupSectionIndicatorEii
inline void QHeaderViewPrivate::setupSectionIndicator(int section, int position)
{
    Q_Q(QHeaderView);
#if QT_CONFIG(label)
    if (!sectionIndicator) {
        sectionIndicator = new QLabel(viewport);
    }
#endif

    int w, h;
    int p = q->sectionViewportPosition(section);
    if (orientation == Qt::Horizontal) {
        w = q->sectionSize(section);
        h = viewport->height();
    } else {
        w = viewport->width();
        h = q->sectionSize(section);
    }
#if QT_CONFIG(label)
    sectionIndicator->resize(w, h);
#endif

    const qreal pixmapDevicePixelRatio = q->devicePixelRatio();
    QPixmap pm(QSize(w, h) * pixmapDevicePixelRatio);
    pm.setDevicePixelRatio(pixmapDevicePixelRatio);
    pm.fill(QColor(0, 0, 0, 45));
    QRect rect(0, 0, w, h);

    QPainter painter(&pm);
    const QVariant variant = model->headerData(section, orientation,
                                               Qt::FontRole);
    if (variant.isValid() && variant.canConvert<QFont>()) {
        const QFont sectionFont = qvariant_cast<QFont>(variant);
        painter.setFont(sectionFont);
    } else {
        painter.setFont(q->font());
    }

    painter.setOpacity(0.75);
    q->paintSection(&painter, rect, section);
    painter.end();

#if QT_CONFIG(label)
    sectionIndicator->setPixmap(pm);
#endif
    sectionIndicatorOffset = position - qMax(p, 0);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3522, as _ZN18QHeaderViewPrivate22updateSectionIndicatorEii
inline void QHeaderViewPrivate::updateSectionIndicator(int section, int position)
{
#if QT_CONFIG(label)
    if (!sectionIndicator)
        return;

    if (section == -1 || target == -1) {
        sectionIndicator->hide();
        return;
    }

    if (orientation == Qt::Horizontal)
        sectionIndicator->move(position - sectionIndicatorOffset, 0);
    else
        sectionIndicator->move(0, position - sectionIndicatorOffset);

    sectionIndicator->show();
#endif
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2083, as _ZN18QHeaderViewPrivate20updateHiddenSectionsEii
inline void QHeaderViewPrivate::updateHiddenSections(int logicalFirst, int logicalLast)
{
    Q_Q(QHeaderView);
    const int changeCount = logicalLast - logicalFirst + 1;

    // remove sections from hiddenSectionSize
    QHash<int, int> newHiddenSectionSize; // from logical index to section size
    for (int i = 0; i < logicalFirst; ++i)
        if (q->isSectionHidden(i))
            newHiddenSectionSize[i] = hiddenSectionSize[i];
    for (int j = logicalLast + 1; j < sectionCount(); ++j)
        if (q->isSectionHidden(j))
            newHiddenSectionSize[j - changeCount] = hiddenSectionSize[j];
    hiddenSectionSize = newHiddenSectionSize;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3674, as _ZN18QHeaderViewPrivate14resizeSectionsEN11QHeaderView10ResizeModeEb
inline void QHeaderViewPrivate::resizeSections(QHeaderView::ResizeMode globalMode, bool useGlobalMode)
{
    Q_Q(QHeaderView);
    //stop the timer in case it is delayed
    delayedResize.stop();

    executePostedLayout();

    if (noSectionMemoryUsage() && (hasAutoResizeSections() || globalMode != QHeaderView::Fixed))
        setHeaderMode(HeaderMode::FlexibleWithSectionMemoryUsage);

    if (sectionCount() == 0 )
        return;

    if (resizeRecursionBlock)
        return;
    resizeRecursionBlock = true;

    invalidateCachedSizeHint();
    const int lastSectionVisualIdx = q->visualIndex(lastSectionLogicalIdx);

    // find stretchLastSection if we have it
    int stretchSection = -1;
    if (stretchLastSection && !useGlobalMode)
        stretchSection = lastSectionVisualIdx;

    // count up the number of stretched sections and how much space left for them
    int lengthToStretch = (orientation == Qt::Horizontal ? viewport->width() : viewport->height());
    int numberOfStretchedSections = 0;
    QList<int> section_sizes;
    for (int i = 0; i < sectionCount(); ++i) {
        if (isVisualIndexHidden(i))
            continue;

        QHeaderView::ResizeMode resizeMode;
        if (useGlobalMode && (i != stretchSection))
            resizeMode = globalMode;
        else
            resizeMode = (i == stretchSection ? QHeaderView::Stretch : headerSectionResizeMode(i));

        if (resizeMode == QHeaderView::Stretch) {
            ++numberOfStretchedSections;
            section_sizes.append(headerSectionSize(i));
            continue;
        }

        // because it isn't stretch, determine its width and remove that from lengthToStretch
        int sectionSize = 0;
        if (resizeMode == QHeaderView::Interactive || resizeMode == QHeaderView::Fixed) {
            sectionSize = qBound(q->minimumSectionSize(), headerSectionSize(i), q->maximumSectionSize());
        } else { // resizeMode == QHeaderView::ResizeToContents
            int logicalIndex = q->logicalIndex(i);
            sectionSize = qMax(viewSectionSizeHint(logicalIndex),
                               q->sectionSizeHint(logicalIndex));
        }
        sectionSize = qBound(q->minimumSectionSize(),
                             sectionSize,
                             q->maximumSectionSize());

        section_sizes.append(sectionSize);
        lengthToStretch -= sectionSize;
    }

    // calculate the new length for all of the stretched sections
    int stretchSectionLength = -1;
    int pixelReminder = 0;
    if (numberOfStretchedSections > 0 && lengthToStretch > 0) { // we have room to stretch in
        int hintLengthForEveryStretchedSection = lengthToStretch / numberOfStretchedSections;
        stretchSectionLength = qMax(hintLengthForEveryStretchedSection, q->minimumSectionSize());
        pixelReminder = lengthToStretch % numberOfStretchedSections;
    }

    // ### The code below would be nicer if it was cleaned up a bit (since spans has been replaced with items)
    int spanStartSection = 0;
    int previousSectionLength = 0;

    QHeaderView::ResizeMode previousSectionResizeMode = QHeaderView::Interactive;

    // resize each section along the total length
    for (int i = 0; i < sectionCount(); ++i) {
        int oldSectionLength = headerSectionSize(i);
        int newSectionLength = -1;
        QHeaderView::ResizeMode newSectionResizeMode = headerSectionResizeMode(i);

        if (isVisualIndexHidden(i)) {
            newSectionLength = 0;
        } else {
            QHeaderView::ResizeMode resizeMode;
            if (useGlobalMode)
                resizeMode = globalMode;
            else
                resizeMode = (i == stretchSection
                              ? QHeaderView::Stretch
                              : newSectionResizeMode);
            if (resizeMode == QHeaderView::Stretch && stretchSectionLength != -1) {
                if (i == lastSectionVisualIdx)
                    newSectionLength = qMax(stretchSectionLength, lastSectionSize);
                else
                    newSectionLength = stretchSectionLength;
                if (pixelReminder > 0) {
                    newSectionLength += 1;
                    --pixelReminder;
                }
                section_sizes.removeFirst();
            } else {
                newSectionLength = section_sizes.takeFirst();
            }
        }

        //Q_ASSERT(newSectionLength > 0);
        if ((previousSectionResizeMode != newSectionResizeMode
            || previousSectionLength != newSectionLength) && i > 0) {
            createSectionItems(spanStartSection, i - 1, previousSectionLength, previousSectionResizeMode);
            //Q_ASSERT(headerLength() == length);
            spanStartSection = i;
        }

        if (newSectionLength != oldSectionLength)
            emit q->sectionResized(logicalIndex(i), oldSectionLength, newSectionLength);

        previousSectionLength = newSectionLength;
        previousSectionResizeMode = newSectionResizeMode;
    }

    createSectionItems(spanStartSection, sectionCount() - 1,
                       previousSectionLength, previousSectionResizeMode);
    //Q_ASSERT(headerLength() == length);
    resizeRecursionBlock = false;
    viewport->update();
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2099, as _ZN18QHeaderViewPrivate15sectionsRemovedERK11QModelIndexii
inline void QHeaderViewPrivate::sectionsRemoved(const QModelIndex &parent,
                                         int logicalFirst, int logicalLast)
{
    Q_Q(QHeaderView);
    if (parent != root)
        return; // we only handle changes in the root level
    if (qMin(logicalFirst, logicalLast) < 0
        || qMax(logicalLast, logicalFirst) >= sectionCount())
        return;
    int oldCount = q->count();
    int changeCount = logicalLast - logicalFirst + 1;

    if (state == QHeaderViewPrivate::ResizeSection)
        preventCursorChangeInSetOffset = true;

    // update sorting column
    if (sortIndicatorSection >= logicalFirst) {
        if (sortIndicatorSection <= logicalLast)
            sortIndicatorSection = -1;
        else
            sortIndicatorSection -= changeCount;
    }

    if (noSectionMemoryUsage()) {
        updateCountInNoSectionItemsMode(countInNoSectionItemsMode - changeCount);
        return;
    }

    updateHiddenSections(logicalFirst, logicalLast);

    if (visualIndices.isEmpty() && logicalIndices.isEmpty()) {
        //Q_ASSERT(headerSectionCount() == sectionCount);
        removeSectionsFromSectionItems(logicalFirst, logicalLast);
    } else {
        if (logicalFirst == logicalLast) { // Remove just one index.
            int l = logicalFirst;
            int visual = visualIndices.at(l);
            Q_ASSERT(sectionCount() == logicalIndices.size());
            for (int v = 0; v < sectionCount(); ++v) {
                if (v > visual) {
                    int logical = logicalIndices.at(v);
                    --(visualIndices[logical]);
                }
                if (logicalIndex(v) > l) // no need to move the positions before l
                    --(logicalIndices[v]);
            }
            logicalIndices.remove(visual);
            visualIndices.remove(l);
            //Q_ASSERT(headerSectionCount() == sectionCount);
            removeSectionsFromSectionItems(visual, visual);
        } else {
            sectionStartposRecalc = true; // We will need to recalc positions after removing items
            for (int u = 0; u < sectionItems.size(); ++u)  // Store section info
                sectionItems.at(u).tmpLogIdx = logicalIndices.at(u);
            for (int v = sectionItems.size() - 1; v >= 0; --v) {  // Remove the sections
                if (logicalFirst <= sectionItems.at(v).tmpLogIdx && sectionItems.at(v).tmpLogIdx <= logicalLast)
                    removeSectionsFromSectionItems(v, v);
            }
            visualIndices.resize(sectionItems.size());
            logicalIndices.resize(sectionItems.size());
            int* visual_data = visualIndices.data();
            int* logical_data = logicalIndices.data();
            for (int w = 0; w < sectionItems.size(); ++w) { // Restore visual and logical indexes
                int logindex = sectionItems.at(w).tmpLogIdx;
                if (logindex > logicalFirst)
                    logindex -= changeCount;
                visual_data[logindex] = w;
                logical_data[w] = logindex;
            }
        }
        // ### handle sectionSelection (sectionHidden is handled by updateHiddenSections)
    }

    // if we only have the last section (the "end" position) left, the header is empty
    if (sectionCount() <= 0)
        clear();
    invalidateCachedSizeHint();
    emit q->sectionCountChanged(oldCount, q->count());

    if (q->stretchLastSection()) {
        const bool lastSectionRemoved = lastSectionLogicalIdx >= logicalFirst && lastSectionLogicalIdx <= logicalLast;
        if (lastSectionRemoved)
            setNewLastSection(lastVisibleVisualIndex());
        else
            lastSectionLogicalIdx = logicalIndex(lastVisibleVisualIndex()); // Just update the last log index.
        doDelayedResizeSections();
    }

    viewport->update();
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2190, as _ZN18QHeaderViewPrivate22sectionsAboutToBeMovedERK11QModelIndexiiS2_i
inline void QHeaderViewPrivate::sectionsAboutToBeMoved(const QModelIndex &sourceParent, int logicalStart,
                                                int logicalEnd, const QModelIndex &destinationParent,
                                                int logicalDestination)
{
    if (sourceParent != root || destinationParent != root)
        return; // we only handle changes in the root level
    Q_UNUSED(logicalStart);
    Q_UNUSED(logicalEnd);
    Q_UNUSED(logicalDestination);
    sectionsAboutToBeChanged();
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2202, as _ZN18QHeaderViewPrivate13sectionsMovedERK11QModelIndexiiS2_i
inline void QHeaderViewPrivate::sectionsMoved(const QModelIndex &sourceParent, int logicalStart,
                                       int logicalEnd, const QModelIndex &destinationParent,
                                       int logicalDestination)
{
    if (sourceParent != root || destinationParent != root)
        return; // we only handle changes in the root level
    Q_UNUSED(logicalStart);
    Q_UNUSED(logicalEnd);
    Q_UNUSED(logicalDestination);
    sectionsChanged();
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2214, as _ZN18QHeaderViewPrivate24sectionsAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QHeaderViewPrivate::sectionsAboutToBeChanged(const QList<QPersistentModelIndex> &,
                                                  QAbstractItemModel::LayoutChangeHint hint)
{
    if ((hint == QAbstractItemModel::VerticalSortHint && orientation == Qt::Horizontal) ||
        (hint == QAbstractItemModel::HorizontalSortHint && orientation == Qt::Vertical))
        return;

    if (noSectionMemoryUsage()) {
        // This is about section mapping, but if there is no changes in sizes or
        // order, there is no need to care.
        return;
    }

    //if there is no row/column we can't have mapping for columns
    //because no QModelIndex in the model would be valid
    // ### this is far from being bullet-proof and we would need a real system to
    // ### map columns or rows persistently
    if ((orientation == Qt::Horizontal && model->rowCount(root) == 0)
        || model->columnCount(root) == 0)
        return;

    layoutChangePersistentSections.clear();
    layoutChangePersistentSections.reserve(std::min(10, int(sectionItems.size())));
    // after layoutChanged another section can be last stretched section
    if (stretchLastSection && lastSectionLogicalIdx >= 0 && lastSectionLogicalIdx < sectionItems.size()) {
        const int visual = visualIndex(lastSectionLogicalIdx);
        if (visual >= 0 && visual < sectionItems.size()) {
            auto &itemRef = sectionItems[visual];
            if (itemRef.size != lastSectionSize) {
                length += lastSectionSize - itemRef.size;
                itemRef.size = lastSectionSize;
            }
        }
    }
    for (int i = 0; i < sectionItems.size(); ++i) {
        auto s = sectionItems.at(i);
        // only add if the section is not default and not visually moved
        if (s.size == defaultSectionSize && !s.isHidden && s.resizeMode == globalResizeMode)
            continue;

        const int logical = logicalIndex(i);
        if (s.isHidden)
            s.size = hiddenSectionSize.value(logical);

        // ### note that we are using column or row 0
        layoutChangePersistentSections.append({orientation == Qt::Horizontal
                                                  ? model->index(0, logical, root)
                                                  : model->index(logical, 0, root),
                                              s});
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 2266, as _ZN18QHeaderViewPrivate15sectionsChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE
inline void QHeaderViewPrivate::sectionsChanged(const QList<QPersistentModelIndex> &,
                                         QAbstractItemModel::LayoutChangeHint hint)
{
    if ((hint == QAbstractItemModel::VerticalSortHint && orientation == Qt::Horizontal) ||
        (hint == QAbstractItemModel::HorizontalSortHint && orientation == Qt::Vertical))
        return;

    Q_Q(QHeaderView);
    viewport->update();

    const auto oldPersistentSections = layoutChangePersistentSections;
    layoutChangePersistentSections.clear();

    const int newCount = modelSectionCount();
    const int oldCount = sectionCount();
    if (newCount == 0) {
        clear();
        if (oldCount != 0)
            emit q->sectionCountChanged(oldCount, 0);
        return;
    }

    if (noSectionMemoryUsage()) {
        // Nothing relevant can have changed in this mode beside the count.
        updateCountInNoSectionItemsMode(newCount);
        return;
    }


    bool hasPersistantIndexes = false;
    for (const auto &item : oldPersistentSections) {
        if (item.index.isValid()) {
            hasPersistantIndexes = true;
            break;
        }
    }

    // Though far from perfect we here try to retain earlier/existing behavior
    // ### See QHeaderViewPrivate::layoutAboutToBeChanged()
    // When we don't have valid hasPersistantIndexes it can be due to
    // - all sections are default sections
    // - the row/column 0 which is used for persistent indexes is gone
    // - all non-default sections were removed
    // case one is trivial, in case two we assume nothing else changed (it's the best
    // guess we can do - everything else can not be handled correctly for now)
    // case three can not be handled correctly with layoutChanged - removeSections
    // should be used instead for this
    if (!hasPersistantIndexes) {
        if (oldCount != newCount)
            q->initializeSections();
        return;
    }

    // adjust section size
    if (newCount != oldCount) {
        const int min = qBound(0, oldCount, newCount - 1);
        q->initializeSections(min, newCount - 1);
    }
    // reset sections
    sectionItems.fill(SectionItem(defaultSectionSize, globalResizeMode), newCount);

    // all hidden sections are in oldPersistentSections
    hiddenSectionSize.clear();

    for (const auto &item : oldPersistentSections) {
        const auto &index = item.index;
        if (!index.isValid())
            continue;

        const int newLogicalIndex = (orientation == Qt::Horizontal
                                     ? index.column()
                                     : index.row());
        // the new visualIndices are already adjusted / reset by initializeSections()
        const int newVisualIndex = visualIndex(newLogicalIndex);
        if (newVisualIndex < sectionItems.size()) {
            auto &newSection = sectionItems[newVisualIndex];
            newSection = item.section;

            if (newSection.isHidden) {
                // otherwise setSectionHidden will return without doing anything
                newSection.isHidden = false;
                q->setSectionHidden(newLogicalIndex, true);
            }
        }
    }

    recalcSectionStartPos();
    length = headerLength();

    if (stretchLastSection) {
        // force rebuild of stretched section later on
        lastSectionLogicalIdx = -1;
        maybeRestorePrevLastSectionAndStretchLast();
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3569, as _ZNK18QHeaderViewPrivate17isSectionSelectedEi
inline bool QHeaderViewPrivate::isSectionSelected(int section) const
{
    int i = section * 2;
    if (i < 0 || i >= sectionSelected.size())
        return false;
    if (sectionSelected.testBit(i)) // if the value was cached
        return sectionSelected.testBit(i + 1);
    bool s = false;
    if (orientation == Qt::Horizontal)
        s = isColumnSelected(section);
    else
        s = isRowSelected(section);
    sectionSelected.setBit(i + 1, s); // selection state
    sectionSelected.setBit(i, true); // cache state
    return s;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3586, as _ZNK18QHeaderViewPrivate21isFirstVisibleSectionEi
inline bool QHeaderViewPrivate::isFirstVisibleSection(int section) const
{
    if (noSectionMemoryUsage())
        return section == 0 && countInNoSectionItemsMode > 0;

    if (sectionStartposRecalc)
        recalcSectionStartPos();
    const SectionItem &item = sectionItems.at(section);
    return item.size > 0 && item.calculated_startpos == 0;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3597, as _ZNK18QHeaderViewPrivate20isLastVisibleSectionEi
inline bool QHeaderViewPrivate::isLastVisibleSection(int section) const
{
    if (noSectionMemoryUsage())
        return section == countInNoSectionItemsMode - 1 &&
               countInNoSectionItemsMode > 0;

    if (sectionStartposRecalc)
        recalcSectionStartPos();
    const SectionItem &item = sectionItems.at(section);
    return item.size > 0 && item.calculatedEndPos() == length;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3831, as _ZN18QHeaderViewPrivate5clearEv
inline void QHeaderViewPrivate::clear()
{
    if (state != NoClear) {
        length = 0;
        countInNoSectionItemsMode = 0;
        visualIndices.clear();
        logicalIndices.clear();
        sectionSelected.clear();
        hiddenSectionSize.clear();
        sectionItems.clear();
        lastSectionLogicalIdx = -1;
        invalidateCachedSizeHint();
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3879, as _ZNK18QHeaderViewPrivate26defaultSortOrderForSectionEi
inline Qt::SortOrder QHeaderViewPrivate::defaultSortOrderForSection(int section) const
{
    const QVariant value = model->headerData(section, orientation, Qt::InitialSortOrderRole);
    if (value.canConvert<int>())
        return static_cast<Qt::SortOrder>(value.toInt());
    return Qt::AscendingOrder;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3887, as _ZN18QHeaderViewPrivate15cascadingResizeEii
inline void QHeaderViewPrivate::cascadingResize(int visual, int newSize)
{
    Q_Q(QHeaderView);
    const int minimumSize = q->minimumSectionSize();
    const int oldSize = headerSectionSize(visual);
    int delta = newSize - oldSize;

    if (delta > 0) { // larger
        bool sectionResized = false;

        // restore old section sizes
        for (int i = firstCascadingSection; i < visual; ++i) {
            if (cascadingSectionSize.contains(i)) {
                int currentSectionSize = headerSectionSize(i);
                int originalSectionSize = cascadingSectionSize.value(i);
                if (currentSectionSize < originalSectionSize) {
                    int newSectionSize = currentSectionSize + delta;
                    resizeSectionItem(i, currentSectionSize, newSectionSize);
                    if (newSectionSize >= originalSectionSize && false)
                        cascadingSectionSize.remove(i); // the section is now restored
                    sectionResized = true;
                    break;
                }
            }

        }

        // resize the section
        if (!sectionResized) {
            newSize = qMax(newSize, minimumSize);
            if (oldSize != newSize)
                resizeSectionItem(visual, oldSize, newSize);
        }

        // cascade the section size change
        for (int i = visual + 1; i < sectionCount(); ++i) {
            if (isVisualIndexHidden(i))
                continue;
            if (!sectionIsCascadable(i))
                continue;
            int currentSectionSize = headerSectionSize(i);
            if (currentSectionSize <= minimumSize)
                continue;
            int newSectionSize = qMax(currentSectionSize - delta, minimumSize);
            resizeSectionItem(i, currentSectionSize, newSectionSize);
            saveCascadingSectionSize(i, currentSectionSize);
            delta = delta - (currentSectionSize - newSectionSize);
            if (delta <= 0)
                break;
        }
    } else { // smaller
        bool sectionResized = false;

        // restore old section sizes
        for (int i = lastCascadingSection; i > visual; --i) {
            if (!cascadingSectionSize.contains(i))
                continue;
            int currentSectionSize = headerSectionSize(i);
            int originalSectionSize = cascadingSectionSize.value(i);
            if (currentSectionSize >= originalSectionSize)
                continue;
            int newSectionSize = currentSectionSize - delta;
            resizeSectionItem(i, currentSectionSize, newSectionSize);
            if (newSectionSize >= originalSectionSize && false) {
                cascadingSectionSize.remove(i); // the section is now restored
            }
            sectionResized = true;
            break;
        }

        // resize the section
        resizeSectionItem(visual, oldSize, qMax(newSize, minimumSize));

        // cascade the section size change
        if (delta < 0 && newSize < minimumSize) {
            for (int i = visual - 1; i >= 0; --i) {
                if (isVisualIndexHidden(i))
                    continue;
                if (!sectionIsCascadable(i))
                    continue;
                int sectionSize = headerSectionSize(i);
                if (sectionSize <= minimumSize)
                    continue;
                resizeSectionItem(i, sectionSize, qMax(sectionSize + delta, minimumSize));
                saveCascadingSectionSize(i, sectionSize);
                break;
            }
        }

        // let the next section get the space from the resized section
        if (!sectionResized) {
            for (int i = visual + 1; i < sectionCount(); ++i) {
                if (isVisualIndexHidden(i))
                    continue;
                if (!sectionIsCascadable(i))
                    continue;
                int currentSectionSize = headerSectionSize(i);
                int newSectionSize = qMax(currentSectionSize - delta, minimumSize);
                resizeSectionItem(i, currentSectionSize, newSectionSize);
                break;
            }
        }
    }

    if (hasAutoResizeSections())
        doDelayedResizeSections();

    viewport->update();
}

//  from src/widgets/itemviews/qheaderview.cpp, line 1805, as _ZN18QHeaderViewPrivate31updateCountInNoSectionItemsModeEi
inline void QHeaderViewPrivate::updateCountInNoSectionItemsMode(int newCount)
{
    Q_ASSERT(noSectionMemoryUsage());
    Q_Q(QHeaderView);
        const int oldCount = countInNoSectionItemsMode;
        countInNoSectionItemsMode = newCount;
        length = newCount * defaultSectionSize;
        invalidateCachedSizeHint();
        viewport->update();
        if (oldCount != newCount) {
            emit q->sectionCountChanged(oldCount, newCount);
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 1777, as _ZN18QHeaderViewPrivate13setHeaderModeE10HeaderMode
inline void QHeaderViewPrivate::setHeaderMode(HeaderMode mode)
{
    Q_Q(QHeaderView);

    if (mode == headerMode)
        return;

    const bool avoidSectionMemoryUsage = (mode == HeaderMode::InitialNoSectionMemoryUsage);
    headerMode = mode;

    QSignalBlocker b(q); // Avoid emit of section count changed.
    if (avoidSectionMemoryUsage) {
        const int sectionCount = sectionItems.count();
        countInNoSectionItemsMode = 0;
        sectionItems.clear();
        visualIndices.clear();
        logicalIndices.clear();
        hiddenSectionSize.clear();
        cascadingSectionSize.clear();
        updateCountInNoSectionItemsMode(sectionCount);
    }
    else {
        length = 0;
        countInNoSectionItemsMode = 0;
        q->initializeSections();
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3805, as _ZN18QHeaderViewPrivate18createSectionItemsEiiiN11QHeaderView10ResizeModeE
inline void QHeaderViewPrivate::createSectionItems(int start, int end, int sizePerSection, QHeaderView::ResizeMode mode)
{
    if (end >= sectionItems.size()) {
        sectionItems.resize(end + 1);
        sectionStartposRecalc = true;
    }
    SectionItem *sectiondata = sectionItems.data();
    for (int i = start; i <= end; ++i) {
        length += (sizePerSection - sectiondata[i].size);
        sectionStartposRecalc |= (sectiondata[i].size != sizePerSection);
        sectiondata[i].size = sizePerSection;
        sectiondata[i].resizeMode = mode;
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3820, as _ZN18QHeaderViewPrivate30removeSectionsFromSectionItemsEii
inline void QHeaderViewPrivate::removeSectionsFromSectionItems(int start, int end)
{
    // remove sections
    sectionStartposRecalc |= (end != sectionItems.size() - 1);
    int removedlength = 0;
    for (int u = start; u <= end; ++u)
        removedlength += sectionItems.at(u).size;
    length -= removedlength;
    sectionItems.remove(start, end - start + 1);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4058, as _ZN18QHeaderViewPrivate17resizeSectionItemEiii
inline void QHeaderViewPrivate::resizeSectionItem(int visualIndex, int oldSize, int newSize)
{
    Q_Q(QHeaderView);
    QHeaderView::ResizeMode mode = headerSectionResizeMode(visualIndex);
    createSectionItems(visualIndex, visualIndex, newSize, mode);
    emit q->sectionResized(logicalIndex(visualIndex), oldSize, newSize);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 3997, as _ZN18QHeaderViewPrivate21setDefaultSectionSizeEi
inline void QHeaderViewPrivate::setDefaultSectionSize(int size)
{
    Q_Q(QHeaderView);
    size = qBound(q->minimumSectionSize(), size, q->maximumSectionSize());
    executePostedLayout();
    invalidateCachedSizeHint();
    defaultSectionSize = size;
    customDefaultSectionSize = true;
    if (state == QHeaderViewPrivate::ResizeSection)
        preventCursorChangeInSetOffset = true;
    for (int i = 0; i < sectionItems.size(); ++i) {
        QHeaderViewPrivate::SectionItem &section = sectionItems[i];
        if (hiddenSectionSize.isEmpty() || !isVisualIndexHidden(i)) { // resize on not hidden.
            // Resize to the new default if the current size is the old default,
            // or 0. Otherwise don't change.
            const int newSize = (section.size == oldDefaultSectionSize || !section.size)
                              ? size
                              : section.size;
            if (newSize != section.size) {
                length += newSize - section.size; //the whole length is changed
                const int oldSectionSize = section.sectionSize();
                section.size = size;
                emit q->sectionResized(logicalIndex(i), oldSectionSize, size);
            }
        }
    }

    sectionStartposRecalc = true;
    if (hasAutoResizeSections())
        doDelayedResizeSections();
    viewport->update();

    if (noSectionMemoryUsage()) {
        length = countInNoSectionItemsMode * size;
        QAbstractItemView *parentView = qobject_cast<QAbstractItemView*>(q->parentWidget());
        if (parentView)
            parentView->viewport()->update();
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4037, as _ZN18QHeaderViewPrivate33updateDefaultSectionSizeFromStyleEv
inline void QHeaderViewPrivate::updateDefaultSectionSizeFromStyle()
{
    Q_Q(QHeaderView);
    if (orientation == Qt::Horizontal) {
        defaultSectionSize = q->style()->pixelMetric(QStyle::PM_HeaderDefaultSectionSizeHorizontal, nullptr, q);
    } else {
        defaultSectionSize = qMax(q->minimumSectionSize(),
                                  q->style()->pixelMetric(QStyle::PM_HeaderDefaultSectionSizeVertical, nullptr, q));
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4048, as _ZNK18QHeaderViewPrivate21recalcSectionStartPosEv
inline void QHeaderViewPrivate::recalcSectionStartPos() const // linear (but fast)
{
    int pixelpos = 0;
    for (const SectionItem &i : sectionItems) {
        i.calculated_startpos = pixelpos; // write into const mutable
        pixelpos += i.size;
    }
    sectionStartposRecalc = false;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4066, as _ZNK18QHeaderViewPrivate17headerSectionSizeEi
inline int QHeaderViewPrivate::headerSectionSize(int visual) const
{
    if (noSectionMemoryUsage()) {
        return defaultSectionSize;
    }

    if (visual < sectionCount() && visual >= 0)
        return sectionItems.at(visual).sectionSize();
    return -1;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4077, as _ZNK18QHeaderViewPrivate21headerSectionPositionEi
inline int QHeaderViewPrivate::headerSectionPosition(int visual) const
{
    if (noSectionMemoryUsage())
        return visual * defaultSectionSize;

    if (visual < sectionCount() && visual >= 0) {
        if (sectionStartposRecalc)
            recalcSectionStartPos();
        return sectionItems.at(visual).calculated_startpos;
    }
    return -1;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4090, as _ZNK18QHeaderViewPrivate19headerVisualIndexAtEi
inline int QHeaderViewPrivate::headerVisualIndexAt(int position) const
{
    if (noSectionMemoryUsage()) {
        if (position >= length || position < 0)
            return -1;
        if (defaultSectionSize > 0)
            return position / defaultSectionSize;
        return 0;
    }

    if (sectionStartposRecalc)
        recalcSectionStartPos();
    int startidx = 0;
    int endidx = sectionItems.size() - 1;
    while (startidx <= endidx) {
        int middle = (endidx + startidx) / 2;
        if (sectionItems.at(middle).calculated_startpos > position) {
            endidx = middle - 1;
        } else {
            if (sectionItems.at(middle).calculatedEndPos() <= position)
                startidx = middle + 1;
            else // we found it.
                return middle;
        }
    }
    return -1;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4118, as _ZN18QHeaderViewPrivate26setHeaderSectionResizeModeEiN11QHeaderView10ResizeModeE
inline void QHeaderViewPrivate::setHeaderSectionResizeMode(int visual, QHeaderView::ResizeMode mode)
{
    if (visual < 0)
        return;
    if (noSectionMemoryUsage())
        switchToFlexibleModeWithSectionMemoryUsage();
    int size = headerSectionSize(visual);
    createSectionItems(visual, visual, size, mode);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4128, as _ZNK18QHeaderViewPrivate23headerSectionResizeModeEi
inline QHeaderView::ResizeMode QHeaderViewPrivate::headerSectionResizeMode(int visual) const
{
    if (visual < 0 || visual >= sectionItems.size())
        return globalResizeMode;
    return static_cast<QHeaderView::ResizeMode>(sectionItems.at(visual).resizeMode);
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4135, as _ZN18QHeaderViewPrivate25setGlobalHeaderResizeModeEN11QHeaderView10ResizeModeE
inline void QHeaderViewPrivate::setGlobalHeaderResizeMode(QHeaderView::ResizeMode mode)
{
    globalResizeMode = mode;
    for (int i = 0; i < sectionItems.size(); ++i)
        sectionItems[i].resizeMode = mode;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4142, as _ZNK18QHeaderViewPrivate19viewSectionSizeHintEi
inline int QHeaderViewPrivate::viewSectionSizeHint(int logical) const
{
    if (QAbstractItemView *view = qobject_cast<QAbstractItemView*>(parent)) {
        return (orientation == Qt::Horizontal
                ? view->sizeHintForColumn(logical)
                : view->sizeHintForRow(logical));
    }
    return 0;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4152, as _ZNK18QHeaderViewPrivate19adjustedVisualIndexEi
inline int QHeaderViewPrivate::adjustedVisualIndex(int visualIndex) const
{
    if (!hiddenSectionSize.isEmpty()) {
        int adjustedVisualIndex = visualIndex;
        int currentVisualIndex = 0;
        for (int i = 0; i < sectionItems.size(); ++i) {
            if (isVisualIndexHidden(i))
                ++adjustedVisualIndex;
            else
                ++currentVisualIndex;
            if (currentVisualIndex >= visualIndex)
                break;
        }
        visualIndex = adjustedVisualIndex;
    }
    return visualIndex;
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4170, as _ZN18QHeaderViewPrivate15setScrollOffsetEPK10QScrollBarN17QAbstractItemView10ScrollModeE
inline void QHeaderViewPrivate::setScrollOffset(const QScrollBar *scrollBar, QAbstractItemView::ScrollMode scrollMode)
{
    Q_Q(QHeaderView);
    if (scrollMode == QAbstractItemView::ScrollPerItem) {
        if (scrollBar->maximum() > 0 && scrollBar->value() == scrollBar->maximum())
            q->setOffsetToLastSection();
        else
            q->setOffsetToSectionPosition(scrollBar->value());
    } else {
        q->setOffset(scrollBar->value());
    }
}

//  from src/widgets/itemviews/qheaderview.cpp, line 4183, as _ZN18QHeaderViewPrivate25updateSectionsBeforeAfterEi
inline void QHeaderViewPrivate::updateSectionsBeforeAfter(int logical)
{
    Q_Q(QHeaderView);
    const int visual = visualIndex(logical);
    int from = logicalIndex(visual > 1 ? visual - 1 : 0);
    int to = logicalIndex(visual + 1 >= sectionCount() ? visual : visual + 1);
    QRect updateRect;
    if (orientation == Qt::Horizontal) {
        if (reverse())
            std::swap(from, to);
        updateRect = QRect(QPoint(q->sectionViewportPosition(from), 0),
                           QPoint(q->sectionViewportPosition(to) + headerSectionSize(to), viewport->height()));
    } else {
        updateRect = QRect(QPoint(0, q->sectionViewportPosition(from)),
                           QPoint(viewport->width(), q->sectionViewportPosition(to) + headerSectionSize(to)));
    }
    viewport->update(updateRect);
}
//  -----------------------------------------------------------------------

//  A QHeaderViewPrivate that Python can take functions over in. Every QHeaderViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall0)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall7)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQHeaderViewPrivateCall9)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall10)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQHeaderViewPrivateCall11)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQHeaderViewPrivateCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
typedef int (*CuteQHeaderViewPrivateCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQHeaderViewPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQHeaderViewPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQHeaderViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQHeaderViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQHeaderViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQHeaderViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQHeaderViewPrivateCall20)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQHeaderViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQHeaderViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQHeaderViewPrivateCall24)(const void *, int *);
typedef int (*CuteQHeaderViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQHeaderViewPrivateCall26)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall27)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall28)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall29)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall30)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall31)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall32)(const void *, int *);
typedef void (*CuteQHeaderViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQHeaderViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQHeaderViewPrivateCall35)(const void *, int *);
class CuteQHeaderViewPrivate : public QHeaderViewPrivate {
public:
  using QHeaderViewPrivate::QHeaderViewPrivate;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14modelDestroyedEv")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate13layoutChangedEv")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(accessibility)
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
  //  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
  //      int start, int end)
  void rowsRemoved(const QModelIndex &parent, int start, int end) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall0 call = reinterpret_cast<CuteQHeaderViewPrivateCall0>(taken[0]);
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
    if (taken[1]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall1 call = reinterpret_cast<CuteQHeaderViewPrivateCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall2 call = reinterpret_cast<CuteQHeaderViewPrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall3 call = reinterpret_cast<CuteQHeaderViewPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall4 call = reinterpret_cast<CuteQHeaderViewPrivateCall4>(taken[4]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::modelDestroyed()
  void modelDestroyed() override {
    if (taken[5]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall5 call = reinterpret_cast<CuteQHeaderViewPrivateCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::modelDestroyed();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::layoutChanged()
  void layoutChanged() override {
    if (taken[6]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall6 call = reinterpret_cast<CuteQHeaderViewPrivateCall6>(taken[6]);
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
    if (taken[7]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall7 call = reinterpret_cast<CuteQHeaderViewPrivateCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall8 call = reinterpret_cast<CuteQHeaderViewPrivateCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall9 call = reinterpret_cast<CuteQHeaderViewPrivateCall9>(taken[9]);
      const QRect * given = call(this, &rect, &topLeft, &bottomRight, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemViewPrivate::intersectedRect(rect, topLeft, bottomRight);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::selectAll(QItemSelectionModel::Selecti
  //      onFlags command)
  void selectAll(QItemSelectionModel::SelectionFlags command) override {
    if (taken[10]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall10 call = reinterpret_cast<CuteQHeaderViewPrivateCall10>(taken[10]);
      call(this, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::selectAll(command);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::adjustViewOptionsForIndex(QStyleOption
  //      ViewItem *a0, const QModelIndex &a1) const
  void adjustViewOptionsForIndex(
      QStyleOptionViewItem *a0,
      const QModelIndex &a1) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall11 call = reinterpret_cast<CuteQHeaderViewPrivateCall11>(taken[11]);
      call(this, a0, &a1, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::adjustViewOptionsForIndex(a0, a1);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemViewPrivate::selectionAllowed(const QModelIndex
  //      &index) const
  bool selectionAllowed(const QModelIndex &index) const override {
    if (taken[12]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall12 call = reinterpret_cast<CuteQHeaderViewPrivateCall12>(taken[12]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemViewPrivate::selectionAllowed(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
  //  int QAbstractItemViewPrivate::accessibleChildIndex(const QModelIndex
  //      &index) const
  int accessibleChildIndex(const QModelIndex &index) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall13 call = reinterpret_cast<CuteQHeaderViewPrivateCall13>(taken[13]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemViewPrivate::accessibleChildIndex(index);
  }
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  QPoint QAbstractItemViewPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall14 call = reinterpret_cast<CuteQHeaderViewPrivateCall14>(taken[14]);
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
      CuteQHeaderViewPrivateCall15 call = reinterpret_cast<CuteQHeaderViewPrivateCall15>(taken[15]);
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
      CuteQHeaderViewPrivateCall16 call = reinterpret_cast<CuteQHeaderViewPrivateCall16>(taken[16]);
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
      CuteQHeaderViewPrivateCall17 call = reinterpret_cast<CuteQHeaderViewPrivateCall17>(taken[17]);
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
      CuteQHeaderViewPrivateCall18 call = reinterpret_cast<CuteQHeaderViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall19 call = reinterpret_cast<CuteQHeaderViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall20 call = reinterpret_cast<CuteQHeaderViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall21 call = reinterpret_cast<CuteQHeaderViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall22 call = reinterpret_cast<CuteQHeaderViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall23 call = reinterpret_cast<CuteQHeaderViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall24 call = reinterpret_cast<CuteQHeaderViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall25 call = reinterpret_cast<CuteQHeaderViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall26 call = reinterpret_cast<CuteQHeaderViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall27 call = reinterpret_cast<CuteQHeaderViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall28 call = reinterpret_cast<CuteQHeaderViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall29 call = reinterpret_cast<CuteQHeaderViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall30 call = reinterpret_cast<CuteQHeaderViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall31 call = reinterpret_cast<CuteQHeaderViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall32 call = reinterpret_cast<CuteQHeaderViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall33 call = reinterpret_cast<CuteQHeaderViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall34 call = reinterpret_cast<CuteQHeaderViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQHeaderViewPrivateCall35 call = reinterpret_cast<CuteQHeaderViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QHeaderView *QHeaderViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QHeaderView *ritual_ZN18QHeaderViewPrivate6q_funcEv(
    QHeaderViewPrivate *self) {
  return self->q_func();
}

//  const QHeaderView *QHeaderViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QHeaderView *ritual_ZNK18QHeaderViewPrivate6q_funcEv(
    const QHeaderViewPrivate *self) {
  return self->q_func();
}

//  int QHeaderViewPrivate::lastVisibleVisualIndex() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate22lastVisibleVisualIndexEv(
    const QHeaderViewPrivate *self) {
  return self->lastVisibleVisualIndex();
}

//  void QHeaderViewPrivate::restoreSizeOnPrevLastSection()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate28restoreSizeOnPrevLastSectionEv(
    QHeaderViewPrivate *self) {
  self->restoreSizeOnPrevLastSection();
}

//  void QHeaderViewPrivate::setNewLastSection(int visualIndexForLastSection)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate17setNewLastSectionEi(
    QHeaderViewPrivate *self,
    int visualIndexForLastSection) {
  self->setNewLastSection(visualIndexForLastSection);
}

//  void QHeaderViewPrivate::maybeRestorePrevLastSectionAndStretchLast()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate41maybeRestorePrevLastSectionAndStretchLastEv(
    QHeaderViewPrivate *self) {
  self->maybeRestorePrevLastSectionAndStretchLast();
}

//  int QHeaderViewPrivate::sectionHandleAt(int position)
extern "C" Q_DECL_EXPORT
int ritual_ZN18QHeaderViewPrivate15sectionHandleAtEi(
    QHeaderViewPrivate *self,
    int position) {
  return self->sectionHandleAt(position);
}

//  void QHeaderViewPrivate::setupSectionIndicator(int section, int position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate21setupSectionIndicatorEii(
    QHeaderViewPrivate *self,
    int section,
    int position) {
  self->setupSectionIndicator(section, position);
}

//  void QHeaderViewPrivate::updateSectionIndicator(int section, int
//      position)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate22updateSectionIndicatorEii(
    QHeaderViewPrivate *self,
    int section,
    int position) {
  self->updateSectionIndicator(section, position);
}

//  void QHeaderViewPrivate::updateHiddenSections(int logicalFirst, int
//      logicalLast)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate20updateHiddenSectionsEii(
    QHeaderViewPrivate *self,
    int logicalFirst,
    int logicalLast) {
  self->updateHiddenSections(logicalFirst, logicalLast);
}

//  void QHeaderViewPrivate::resizeSections(QHeaderView::ResizeMode
//      globalMode, bool useGlobalMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate14resizeSectionsEN11QHeaderView10ResizeModeEb(
    QHeaderViewPrivate *self,
    QHeaderView::ResizeMode globalMode,
    bool useGlobalMode) {
  self->resizeSections(globalMode, useGlobalMode);
}

//  void QHeaderViewPrivate::sectionsRemoved(const QModelIndex &a0, int a1,
//      int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate15sectionsRemovedERK11QModelIndexii(
    QHeaderViewPrivate *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->sectionsRemoved(*a0, a1, a2);
}

//  void QHeaderViewPrivate::sectionsAboutToBeMoved(const QModelIndex
//      &sourceParent, int logicalStart, int logicalEnd, const QModelIndex
//      &destinationParent, int logicalDestination)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate22sectionsAboutToBeMovedERK11QModelIndexiiS2_i(
    QHeaderViewPrivate *self,
    const QModelIndex *sourceParent,
    int logicalStart,
    int logicalEnd,
    const QModelIndex *destinationParent,
    int logicalDestination) {
  self->sectionsAboutToBeMoved(
      *sourceParent,
      logicalStart,
      logicalEnd,
      *destinationParent,
      logicalDestination);
}

//  void QHeaderViewPrivate::sectionsMoved(const QModelIndex &sourceParent,
//      int logicalStart, int logicalEnd, const QModelIndex
//      &destinationParent, int logicalDestination)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate13sectionsMovedERK11QModelIndexiiS2_i(
    QHeaderViewPrivate *self,
    const QModelIndex *sourceParent,
    int logicalStart,
    int logicalEnd,
    const QModelIndex *destinationParent,
    int logicalDestination) {
  self->sectionsMoved(
      *sourceParent,
      logicalStart,
      logicalEnd,
      *destinationParent,
      logicalDestination);
}

//  void QHeaderViewPrivate::sectionsAboutToBeChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate24sectionsAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QHeaderViewPrivate *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->sectionsAboutToBeChanged(*parents, hint);
}

//  void QHeaderViewPrivate::sectionsChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate15sectionsChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QHeaderViewPrivate *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->sectionsChanged(*parents, hint);
}

//  bool QHeaderViewPrivate::isSectionSelected(int section) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate17isSectionSelectedEi(
    const QHeaderViewPrivate *self,
    int section) {
  return self->isSectionSelected(section);
}

//  bool QHeaderViewPrivate::isFirstVisibleSection(int section) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate21isFirstVisibleSectionEi(
    const QHeaderViewPrivate *self,
    int section) {
  return self->isFirstVisibleSection(section);
}

//  bool QHeaderViewPrivate::isLastVisibleSection(int section) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate20isLastVisibleSectionEi(
    const QHeaderViewPrivate *self,
    int section) {
  return self->isLastVisibleSection(section);
}

//  bool QHeaderViewPrivate::rowIntersectsSelection(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate22rowIntersectsSelectionEi(
    const QHeaderViewPrivate *self,
    int row) {
  return self->rowIntersectsSelection(row);
}

//  bool QHeaderViewPrivate::columnIntersectsSelection(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate25columnIntersectsSelectionEi(
    const QHeaderViewPrivate *self,
    int column) {
  return self->columnIntersectsSelection(column);
}

//  bool QHeaderViewPrivate::sectionIntersectsSelection(int logical) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate26sectionIntersectsSelectionEi(
    const QHeaderViewPrivate *self,
    int logical) {
  return self->sectionIntersectsSelection(logical);
}

//  bool QHeaderViewPrivate::isRowSelected(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate13isRowSelectedEi(
    const QHeaderViewPrivate *self,
    int row) {
  return self->isRowSelected(row);
}

//  bool QHeaderViewPrivate::isColumnSelected(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate16isColumnSelectedEi(
    const QHeaderViewPrivate *self,
    int column) {
  return self->isColumnSelected(column);
}

//  void QHeaderViewPrivate::prepareSectionSelected()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate22prepareSectionSelectedEv(
    QHeaderViewPrivate *self) {
  self->prepareSectionSelected();
}

//  int QHeaderViewPrivate::sectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate12sectionCountEv(
    const QHeaderViewPrivate *self) {
  return self->sectionCount();
}

//  bool QHeaderViewPrivate::reverse() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate7reverseEv(
    const QHeaderViewPrivate *self) {
  return self->reverse();
}

//  int QHeaderViewPrivate::logicalIndex(int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate12logicalIndexEi(
    const QHeaderViewPrivate *self,
    int visualIndex) {
  return self->logicalIndex(visualIndex);
}

//  int QHeaderViewPrivate::visualIndex(int logicalIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate11visualIndexEi(
    const QHeaderViewPrivate *self,
    int logicalIndex) {
  return self->visualIndex(logicalIndex);
}

//  void QHeaderViewPrivate::setDefaultValues(Qt::Orientation o)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate16setDefaultValuesEN2Qt11OrientationE(
    QHeaderViewPrivate *self,
    Qt::Orientation o) {
  self->setDefaultValues(o);
}

//  bool QHeaderViewPrivate::isVisualIndexHidden(int visual) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate19isVisualIndexHiddenEi(
    const QHeaderViewPrivate *self,
    int visual) {
  return self->isVisualIndexHidden(visual);
}

//  void QHeaderViewPrivate::setVisualIndexHidden(int visual, bool hidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate20setVisualIndexHiddenEib(
    QHeaderViewPrivate *self,
    int visual,
    bool hidden) {
  self->setVisualIndexHidden(visual, hidden);
}

//  bool QHeaderViewPrivate::hasAutoResizeSections() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate21hasAutoResizeSectionsEv(
    const QHeaderViewPrivate *self) {
  return self->hasAutoResizeSections();
}

//  void QHeaderViewPrivate::invalidateCachedSizeHint() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QHeaderViewPrivate24invalidateCachedSizeHintEv(
    const QHeaderViewPrivate *self) {
  self->invalidateCachedSizeHint();
}

//  void QHeaderViewPrivate::initializeIndexMapping() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QHeaderViewPrivate22initializeIndexMappingEv(
    const QHeaderViewPrivate *self) {
  self->initializeIndexMapping();
}

//  void QHeaderViewPrivate::clearCascadingSections()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate22clearCascadingSectionsEv(
    QHeaderViewPrivate *self) {
  self->clearCascadingSections();
}

//  void QHeaderViewPrivate::saveCascadingSectionSize(int visual, int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate24saveCascadingSectionSizeEii(
    QHeaderViewPrivate *self,
    int visual,
    int size) {
  self->saveCascadingSectionSize(visual, size);
}

//  bool QHeaderViewPrivate::sectionIsCascadable(int visual) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate19sectionIsCascadableEi(
    const QHeaderViewPrivate *self,
    int visual) {
  return self->sectionIsCascadable(visual);
}

//  int QHeaderViewPrivate::modelSectionCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate17modelSectionCountEv(
    const QHeaderViewPrivate *self) {
  return self->modelSectionCount();
}

//  void QHeaderViewPrivate::doDelayedResizeSections()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate23doDelayedResizeSectionsEv(
    QHeaderViewPrivate *self) {
  self->doDelayedResizeSections();
}

//  void QHeaderViewPrivate::executePostedResize() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QHeaderViewPrivate19executePostedResizeEv(
    const QHeaderViewPrivate *self) {
  self->executePostedResize();
}

//  void QHeaderViewPrivate::disconnectModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate15disconnectModelEv(
    QHeaderViewPrivate *self) {
  self->disconnectModel();
}

//  void QHeaderViewPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate5clearEv(QHeaderViewPrivate *self) {
  self->clear();
}

//  Qt::SortOrder QHeaderViewPrivate::defaultSortOrderForSection(int section)
//      const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK18QHeaderViewPrivate26defaultSortOrderForSectionEi(
    const QHeaderViewPrivate *self,
    int section) {
  return self->defaultSortOrderForSection(section);
}

//  void QHeaderViewPrivate::cascadingResize(int visual, int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate15cascadingResizeEii(
    QHeaderViewPrivate *self,
    int visual,
    int newSize) {
  self->cascadingResize(visual, newSize);
}

//  bool QHeaderViewPrivate::noSectionMemoryUsage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QHeaderViewPrivate20noSectionMemoryUsageEv(
    const QHeaderViewPrivate *self) {
  return self->noSectionMemoryUsage();
}

//  void QHeaderViewPrivate::switchToFlexibleModeWithSectionMemoryUsage()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate42switchToFlexibleModeWithSectionMemoryUsageEv(
    QHeaderViewPrivate *self) {
  self->switchToFlexibleModeWithSectionMemoryUsage();
}

//  void QHeaderViewPrivate::updateCountInNoSectionItemsMode(int newCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate31updateCountInNoSectionItemsModeEi(
    QHeaderViewPrivate *self,
    int newCount) {
  self->updateCountInNoSectionItemsMode(newCount);
}

//  void QHeaderViewPrivate::setHeaderMode(HeaderMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate13setHeaderModeE10HeaderMode(
    QHeaderViewPrivate *self,
    HeaderMode mode) {
  self->setHeaderMode(mode);
}

//  void QHeaderViewPrivate::createSectionItems(int start, int end, int
//      sectionSize, QHeaderView::ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate18createSectionItemsEiiiN11QHeaderView10ResizeModeE(
    QHeaderViewPrivate *self,
    int start,
    int end,
    int sectionSize,
    QHeaderView::ResizeMode mode) {
  self->createSectionItems(start, end, sectionSize, mode);
}

//  void QHeaderViewPrivate::removeSectionsFromSectionItems(int start, int
//      end)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate30removeSectionsFromSectionItemsEii(
    QHeaderViewPrivate *self,
    int start,
    int end) {
  self->removeSectionsFromSectionItems(start, end);
}

//  void QHeaderViewPrivate::resizeSectionItem(int visualIndex, int oldSize,
//      int newSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate17resizeSectionItemEiii(
    QHeaderViewPrivate *self,
    int visualIndex,
    int oldSize,
    int newSize) {
  self->resizeSectionItem(visualIndex, oldSize, newSize);
}

//  void QHeaderViewPrivate::setDefaultSectionSize(int size)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate21setDefaultSectionSizeEi(
    QHeaderViewPrivate *self,
    int size) {
  self->setDefaultSectionSize(size);
}

//  void QHeaderViewPrivate::updateDefaultSectionSizeFromStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate33updateDefaultSectionSizeFromStyleEv(
    QHeaderViewPrivate *self) {
  self->updateDefaultSectionSizeFromStyle();
}

//  void QHeaderViewPrivate::recalcSectionStartPos() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QHeaderViewPrivate21recalcSectionStartPosEv(
    const QHeaderViewPrivate *self) {
  self->recalcSectionStartPos();
}

//  int QHeaderViewPrivate::headerLength() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate12headerLengthEv(
    const QHeaderViewPrivate *self) {
  return self->headerLength();
}

//  QBitArray QHeaderViewPrivate::sectionsHiddenToBitVector() const
extern "C" Q_DECL_EXPORT
QBitArray *ritual_ZNK18QHeaderViewPrivate25sectionsHiddenToBitVectorEv(
    const QHeaderViewPrivate *self) {
  return new QBitArray(self->sectionsHiddenToBitVector());
}

//  void QHeaderViewPrivate::setHiddenSectionsFromBitVector(const QBitArray
//      &sectionHidden)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate30setHiddenSectionsFromBitVectorERK9QBitArray(
    QHeaderViewPrivate *self,
    const QBitArray *sectionHidden) {
  self->setHiddenSectionsFromBitVector(*sectionHidden);
}

//  int QHeaderViewPrivate::headerSectionSize(int visual) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate17headerSectionSizeEi(
    const QHeaderViewPrivate *self,
    int visual) {
  return self->headerSectionSize(visual);
}

//  int QHeaderViewPrivate::headerSectionPosition(int visual) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate21headerSectionPositionEi(
    const QHeaderViewPrivate *self,
    int visual) {
  return self->headerSectionPosition(visual);
}

//  int QHeaderViewPrivate::headerVisualIndexAt(int position) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate19headerVisualIndexAtEi(
    const QHeaderViewPrivate *self,
    int position) {
  return self->headerVisualIndexAt(position);
}

//  void QHeaderViewPrivate::setHeaderSectionResizeMode(int visual,
//      QHeaderView::ResizeMode mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate26setHeaderSectionResizeModeEiN11QHeaderView10ResizeModeE(
    QHeaderViewPrivate *self,
    int visual,
    QHeaderView::ResizeMode mode) {
  self->setHeaderSectionResizeMode(visual, mode);
}

//  QHeaderView::ResizeMode QHeaderViewPrivate::headerSectionResizeMode(int
//      visual) const
extern "C" Q_DECL_EXPORT
QHeaderView::ResizeMode ritual_ZNK18QHeaderViewPrivate23headerSectionResizeModeEi(
    const QHeaderViewPrivate *self,
    int visual) {
  return self->headerSectionResizeMode(visual);
}

//  void
//      QHeaderViewPrivate::setGlobalHeaderResizeMode(QHeaderView::ResizeMode
//      mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate25setGlobalHeaderResizeModeEN11QHeaderView10ResizeModeE(
    QHeaderViewPrivate *self,
    QHeaderView::ResizeMode mode) {
  self->setGlobalHeaderResizeMode(mode);
}

//  int QHeaderViewPrivate::viewSectionSizeHint(int logical) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate19viewSectionSizeHintEi(
    const QHeaderViewPrivate *self,
    int logical) {
  return self->viewSectionSizeHint(logical);
}

//  int QHeaderViewPrivate::adjustedVisualIndex(int visualIndex) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QHeaderViewPrivate19adjustedVisualIndexEi(
    const QHeaderViewPrivate *self,
    int visualIndex) {
  return self->adjustedVisualIndex(visualIndex);
}

//  void QHeaderViewPrivate::setScrollOffset(const QScrollBar *scrollBar,
//      QAbstractItemView::ScrollMode scrollMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate15setScrollOffsetEPK10QScrollBarN17QAbstractItemView10ScrollModeE(
    QHeaderViewPrivate *self,
    const QScrollBar *scrollBar,
    QAbstractItemView::ScrollMode scrollMode) {
  self->setScrollOffset(scrollBar, scrollMode);
}

//  void QHeaderViewPrivate::updateSectionsBeforeAfter(int logical)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QHeaderViewPrivate25updateSectionsBeforeAfterEi(
    QHeaderViewPrivate *self,
    int logical) {
  self->updateSectionsBeforeAfter(logical);
}

//  a Python function taken by a CuteQHeaderViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHeaderViewPrivate(
    QHeaderViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHeaderViewPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
