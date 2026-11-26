//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 10 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tablewidget)
#if QT_CONFIG(tablewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtablewidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtablewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
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
#include <QtWidgets/qtableview.h>
#include <QtWidgets/qheaderview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/qapplication.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtCore/qsize.h>
#include <QtGui/qevent.h>
#include <QtCore/qbitarray.h>
#include <QtWidgets/qscrollbar.h>
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qtableview_p.h>
#include <QtWidgets/private/qheaderview_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
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
#include <QtWidgets/qtablewidget.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/private/qtablewidget_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  from src/widgets/itemviews/qtableview.cpp, line 661, as _ZNK17QTableViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_
inline QRect QTableViewPrivate::intersectedRect(const QRect rect, const QModelIndex &topLeft, const QModelIndex &bottomRight) const
{
    Q_Q(const QTableView);

    using minMaxPair = std::pair<int, int>;
    const auto calcMinMax = [q](QHeaderView *hdr, int startIdx, int endIdx, minMaxPair bounds) -> minMaxPair
    {
        minMaxPair ret(std::numeric_limits<int>::max(), std::numeric_limits<int>::min());
        if (hdr->sectionsMoved()) {
            for (int i = startIdx; i <= endIdx; ++i) {
                const int start = hdr->sectionViewportPosition(i);
                const int end = start + hdr->sectionSize(i);
                ret.first = std::min(start, ret.first);
                ret.second = std::max(end, ret.second);
                if (ret.first <= bounds.first && ret.second >= bounds.second)
                    break;
            }
        } else {
            if (q->isRightToLeft() && q->horizontalHeader() == hdr)
                std::swap(startIdx, endIdx);
            ret.first = hdr->sectionViewportPosition(startIdx);
            ret.second = hdr->sectionViewportPosition(endIdx) +
                         hdr->sectionSize(endIdx);
        }
        return ret;
    };

    const auto yVals = calcMinMax(verticalHeader, topLeft.row(), bottomRight.row(),
                                  minMaxPair(rect.top(), rect.bottom()));
    if (yVals.first == yVals.second) // all affected rows are hidden
        return QRect();

    // short circuit: check if no row is inside rect
    const QRect colRect(QPoint(rect.left(), yVals.first),
                        QPoint(rect.right(), yVals.second));
    const QRect intersected = rect.intersected(colRect);
    if (intersected.isNull())
        return QRect();

    const auto xVals = calcMinMax(horizontalHeader, topLeft.column(), bottomRight.column(),
                                  minMaxPair(rect.left(), rect.right()));
    const QRect updateRect(QPoint(xVals.first, yVals.first),
                           QPoint(xVals.second, yVals.second));
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

//  from src/widgets/itemviews/qtablewidget.cpp, line 549, as _ZN11QTableModel12ensureSortedEiN2Qt9SortOrderEii
inline void QTableModel::ensureSorted(int column, Qt::SortOrder order,
                               int start, int end)
{
    int count = end - start + 1;
    QList<std::pair<QTableWidgetItem *, int>> sorting;
    sorting.reserve(count);
    for (int row = start; row <= end; ++row) {
        QTableWidgetItem *itm = item(row, column);
        if (itm == nullptr) {
            // no more sortable items (all 0-items are
            // at the end of the table when it is sorted)
            break;
        }
        sorting.emplace_back(itm, row);
    }

    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sorting.begin(), sorting.end(), compare);
    QModelIndexList oldPersistentIndexes, newPersistentIndexes;
    QList<QTableWidgetItem *> newTable = tableItems;
    QList<QTableWidgetItem *> newVertical = verticalHeaderItems;
    QList<QTableWidgetItem *> colItems = columnItems(column);
    QList<QTableWidgetItem *>::iterator vit = colItems.begin();
    qsizetype distanceFromBegin = 0;
    bool changed = false;
    for (int i = 0; i < sorting.size(); ++i) {
        distanceFromBegin = std::distance(colItems.begin(), vit);
        int oldRow = sorting.at(i).second;
        QTableWidgetItem *item = colItems.at(oldRow);
        colItems.remove(oldRow);
        vit = sortedInsertionIterator(colItems.begin() + distanceFromBegin, colItems.end(), order,
                                      item);
        int newRow = qMax((int)(vit - colItems.begin()), 0);
        if ((newRow < oldRow) && !(*item < *colItems.at(oldRow - 1)) && !(*colItems.at(oldRow - 1) < *item))
            newRow = oldRow;
        vit = colItems.insert(vit, item);
        if (newRow != oldRow) {
            if (!changed) {
                emit layoutAboutToBeChanged({}, QAbstractItemModel::VerticalSortHint);
                oldPersistentIndexes = persistentIndexList();
                newPersistentIndexes = oldPersistentIndexes;
                changed = true;
            }
            // move the items @ oldRow to newRow
            int cc = columnCount();
            QList<QTableWidgetItem *> rowItems(cc);
            for (int j = 0; j < cc; ++j)
                rowItems[j] = newTable.at(tableIndex(oldRow, j));
            newTable.remove(tableIndex(oldRow, 0), cc);
            newTable.insert(tableIndex(newRow, 0), cc, 0);
            for (int j = 0; j < cc; ++j)
                newTable[tableIndex(newRow, j)] = rowItems.at(j);
            QTableWidgetItem *header = newVertical.at(oldRow);
            newVertical.remove(oldRow);
            newVertical.insert(newRow, header);
            // update persistent indexes
            updateRowIndexes(newPersistentIndexes, oldRow, newRow);
            // the index of the remaining rows may have changed
            for (int j = i + 1; j < sorting.size(); ++j) {
                int otherRow = sorting.at(j).second;
                if (oldRow < otherRow && newRow >= otherRow)
                    --sorting[j].second;
                else if (oldRow > otherRow && newRow <= otherRow)
                    ++sorting[j].second;
            }
        }
    }

    if (changed) {
        tableItems = newTable;
        verticalHeaderItems = newVertical;
        changePersistentIndexList(oldPersistentIndexes,
                                  newPersistentIndexes);
        emit layoutChanged({}, QAbstractItemModel::VerticalSortHint);
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 224, as _ZNK11QTableModel4itemERK11QModelIndex
inline QTableWidgetItem *QTableModel::item(const QModelIndex &index) const
{
    if (!isValid(index))
        return nullptr;
    return tableItems.at(tableIndex(index.row(), index.column()));
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

//  from src/widgets/itemviews/qtablewidget.cpp, line 690, as _ZN11QTableModel12itemLessThanERKSt4pairIP16QTableWidgetItemiES5_
inline bool QTableModel::itemLessThan(const std::pair<QTableWidgetItem*,int> &left,
                               const std::pair<QTableWidgetItem*,int> &right)
{
    return *(left.first) < *(right.first);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 696, as _ZN11QTableModel15itemGreaterThanERKSt4pairIP16QTableWidgetItemiES5_
inline bool QTableModel::itemGreaterThan(const std::pair<QTableWidgetItem*,int> &left,
                                  const std::pair<QTableWidgetItem*,int> &right)
{
    return (*(right.first) < *(left .first));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 655, as _ZN11QTableModel16updateRowIndexesER5QListI11QModelIndexEii
inline void QTableModel::updateRowIndexes(QModelIndexList &indexes,
                                   int movedFromRow, int movedToRow)
{
    QModelIndexList::iterator it;
    for (it = indexes.begin(); it != indexes.end(); ++it) {
        int oldRow = (*it).row();
        int newRow = oldRow;
        if (oldRow == movedFromRow)
            newRow = movedToRow;
        else if (movedFromRow < oldRow && movedToRow >= oldRow)
            newRow = oldRow - 1;
        else if (movedFromRow > oldRow && movedToRow <= oldRow)
            newRow = oldRow + 1;
        if (newRow != oldRow)
            *it = index(newRow, (*it).column(), (*it).parent());
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 680, as _ZN11QTableModel23sortedInsertionIteratorERKN5QListIP16QTableWidgetItemE8iteratorES6_N2Qt9SortOrderES2_
inline QList<QTableWidgetItem *>::iterator
QTableModel::sortedInsertionIterator(const QList<QTableWidgetItem *>::iterator &begin,
                                     const QList<QTableWidgetItem *>::iterator &end,
                                     Qt::SortOrder order, QTableWidgetItem *item)
{
    if (order == Qt::AscendingOrder)
        return std::lower_bound(begin, end, item, QTableModelLessThan());
    return std::lower_bound(begin, end, item, QTableModelGreaterThan());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 631, as _ZNK11QTableModel11columnItemsEi
inline QList<QTableWidgetItem *> QTableModel::columnItems(int column) const
{
    QList<QTableWidgetItem *> items;
    int rc = rowCount();
    items.reserve(rc);
    for (int row = 0; row < rc; ++row) {
        QTableWidgetItem *itm = item(row, column);
        if (itm == nullptr) {
            // no more sortable items (all 0-items are
            // at the end of the table when it is sorted)
            break;
        }
        items.append(itm);
    }
    return items;
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 219, as _ZNK11QTableModel4itemEii
inline QTableWidgetItem *QTableModel::item(int row, int column) const
{
    return item(index(row, column));
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 742, as _ZNK11QTableModel7isValidERK11QModelIndex
inline bool QTableModel::isValid(const QModelIndex &index) const
{
    return (index.isValid()
            && index.row() < verticalHeaderItems.size()
            && index.column() < horizontalHeaderItems.size());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1614, as _ZN19QTableWidgetPrivate5setupEv
inline void QTableWidgetPrivate::setup()
{
    Q_Q(QTableWidget);
    connections = {
        // view signals
        QObjectPrivate::connect(q, &QTableWidget::pressed,
                                this, &QTableWidgetPrivate::emitItemPressed),
        QObjectPrivate::connect(q, &QTableWidget::clicked,
                                this, &QTableWidgetPrivate::emitItemClicked),
        QObjectPrivate::connect(q, &QTableWidget::doubleClicked,
                                this, &QTableWidgetPrivate::emitItemDoubleClicked),
        QObjectPrivate::connect(q, &QTableWidget::activated,
                                this, &QTableWidgetPrivate::emitItemActivated),
        QObjectPrivate::connect(q, &QTableWidget::entered,
                                this, &QTableWidgetPrivate::emitItemEntered),
        // model signals
        QObjectPrivate::connect(model, &QAbstractItemModel::dataChanged,
                                this, &QTableWidgetPrivate::emitItemChanged),
        // selection signals
        QObjectPrivate::connect(q->selectionModel(), &QItemSelectionModel::currentChanged,
                                this, &QTableWidgetPrivate::emitCurrentItemChanged),
        QObject::connect(q->selectionModel(), &QItemSelectionModel::selectionChanged,
                         q, &QTableWidget::itemSelectionChanged),
        // sorting
        QObjectPrivate::connect(model, &QAbstractItemModel::dataChanged,
                                this, &QTableWidgetPrivate::dataChanged),
        QObjectPrivate::connect(model, &QAbstractItemModel::columnsRemoved,
                                this, &QTableWidgetPrivate::sort)
    };
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1645, as _ZN19QTableWidgetPrivate16clearConnectionsEv
inline void QTableWidgetPrivate::clearConnections()
{
    for (QMetaObject::Connection &connection : connections)
        QObject::disconnect(connection);
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1651, as _ZN19QTableWidgetPrivate15emitItemPressedERK11QModelIndex
inline void QTableWidgetPrivate::emitItemPressed(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemPressed(item);
    emit q->cellPressed(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1659, as _ZN19QTableWidgetPrivate15emitItemClickedERK11QModelIndex
inline void QTableWidgetPrivate::emitItemClicked(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemClicked(item);
    emit q->cellClicked(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1667, as _ZN19QTableWidgetPrivate21emitItemDoubleClickedERK11QModelIndex
inline void QTableWidgetPrivate::emitItemDoubleClicked(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemDoubleClicked(item);
    emit q->cellDoubleClicked(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1675, as _ZN19QTableWidgetPrivate17emitItemActivatedERK11QModelIndex
inline void QTableWidgetPrivate::emitItemActivated(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemActivated(item);
    emit q->cellActivated(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1683, as _ZN19QTableWidgetPrivate15emitItemEnteredERK11QModelIndex
inline void QTableWidgetPrivate::emitItemEntered(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemEntered(item);
    emit q->cellEntered(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1691, as _ZN19QTableWidgetPrivate15emitItemChangedERK11QModelIndex
inline void QTableWidgetPrivate::emitItemChanged(const QModelIndex &index)
{
    Q_Q(QTableWidget);
    if (QTableWidgetItem *item = tableModel()->item(index))
        emit q->itemChanged(item);
    emit q->cellChanged(index.row(), index.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1699, as _ZN19QTableWidgetPrivate22emitCurrentItemChangedERK11QModelIndexS2_
inline void QTableWidgetPrivate::emitCurrentItemChanged(const QModelIndex &current,
                                                 const QModelIndex &previous)
{
    Q_Q(QTableWidget);
    QTableWidgetItem *currentItem = tableModel()->item(current);
    QTableWidgetItem *previousItem = tableModel()->item(previous);
    if (currentItem || previousItem)
        emit q->currentItemChanged(currentItem, previousItem);
    emit q->currentCellChanged(current.row(), current.column(), previous.row(), previous.column());
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1710, as _ZN19QTableWidgetPrivate4sortEv
inline void QTableWidgetPrivate::sort()
{
    if (sortingEnabled) {
        int column = horizontalHeader->sortIndicatorSection();
        Qt::SortOrder order = horizontalHeader->sortIndicatorOrder();
        model->sort(column, order);
    }
}

//  from src/widgets/itemviews/qtablewidget.cpp, line 1719, as _ZN19QTableWidgetPrivate11dataChangedERK11QModelIndexS2_
inline void QTableWidgetPrivate::dataChanged(const QModelIndex &topLeft,
                                      const QModelIndex &bottomRight)
{
    if (sortingEnabled && topLeft.isValid() && bottomRight.isValid()) {
        int column = horizontalHeader->sortIndicatorSection();
        if (column >= topLeft.column() && column <= bottomRight.column()) {
            Qt::SortOrder order = horizontalHeader->sortIndicatorOrder();
            tableModel()->ensureSorted(column, order, topLeft.row(), bottomRight.row());
        }
    }
}
//  -----------------------------------------------------------------------

//  A QTableWidgetPrivate that Python can take functions over in. Every QTableWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef const QRect * (*CuteQTableWidgetPrivateCall0)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableWidgetPrivateCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall5)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall6)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall9)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall10)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall11)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableWidgetPrivateCall12)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableWidgetPrivateCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQTableWidgetPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQTableWidgetPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTableWidgetPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTableWidgetPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTableWidgetPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQTableWidgetPrivateCall19)(const void *, int, int *);
typedef void (*CuteQTableWidgetPrivateCall20)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall21)(const void *, int *);
typedef void * (*CuteQTableWidgetPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTableWidgetPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTableWidgetPrivateCall24)(const void *, int *);
typedef int (*CuteQTableWidgetPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQTableWidgetPrivateCall26)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall27)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall28)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall29)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall30)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall31)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall32)(const void *, int *);
typedef void (*CuteQTableWidgetPrivateCall33)(const void *, int *);
typedef bool (*CuteQTableWidgetPrivateCall34)(const void *, int *);
typedef bool (*CuteQTableWidgetPrivateCall35)(const void *, int *);
class CuteQTableWidgetPrivate : public QTableWidgetPrivate {
public:
  using QTableWidgetPrivate::QTableWidgetPrivate;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tableview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14modelDestroyedEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate13layoutChangedEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex")) {
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
#if QT_CONFIG(tableview)
  //  QRect QTableViewPrivate::intersectedRect(const QRect rect, const
  //      QModelIndex &topLeft, const QModelIndex &bottomRight) const
  QRect intersectedRect(
      const QRect rect,
      const QModelIndex &topLeft,
      const QModelIndex &bottomRight) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall0 call = reinterpret_cast<CuteQTableWidgetPrivateCall0>(taken[0]);
      const QRect * given = call(this, &rect, &topLeft, &bottomRight, &handled);
      if (handled && given) return *given;
    }
    return QTableViewPrivate::intersectedRect(rect, topLeft, bottomRight);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tableview)
  //  int QTableViewPrivate::accessibleChildIndex(const QModelIndex &index)
  //      const
  int accessibleChildIndex(const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall1 call = reinterpret_cast<CuteQTableWidgetPrivateCall1>(taken[1]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTableViewPrivate::accessibleChildIndex(index);
  }
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
  //      int start, int end)
  void rowsRemoved(const QModelIndex &parent, int start, int end) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall2 call = reinterpret_cast<CuteQTableWidgetPrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall3 call = reinterpret_cast<CuteQTableWidgetPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall4 call = reinterpret_cast<CuteQTableWidgetPrivateCall4>(taken[4]);
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
    if (taken[5]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall5 call = reinterpret_cast<CuteQTableWidgetPrivateCall5>(taken[5]);
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
    if (taken[6]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall6 call = reinterpret_cast<CuteQTableWidgetPrivateCall6>(taken[6]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::modelDestroyed()
  void modelDestroyed() override {
    if (taken[7]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall7 call = reinterpret_cast<CuteQTableWidgetPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::modelDestroyed();
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::layoutChanged()
  void layoutChanged() override {
    if (taken[8]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall8 call = reinterpret_cast<CuteQTableWidgetPrivateCall8>(taken[8]);
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
    if (taken[9]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall9 call = reinterpret_cast<CuteQTableWidgetPrivateCall9>(taken[9]);
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
    if (taken[10]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall10 call = reinterpret_cast<CuteQTableWidgetPrivateCall10>(taken[10]);
      call(this, &source, sourceStart, sourceEnd, &destination, destinationStart, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsMoved(source, sourceStart, sourceEnd, destination, destinationStart);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::selectAll(QItemSelectionModel::Selecti
  //      onFlags command)
  void selectAll(QItemSelectionModel::SelectionFlags command) override {
    if (taken[11]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall11 call = reinterpret_cast<CuteQTableWidgetPrivateCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall12 call = reinterpret_cast<CuteQTableWidgetPrivateCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall13 call = reinterpret_cast<CuteQTableWidgetPrivateCall13>(taken[13]);
      bool given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QAbstractItemViewPrivate::selectionAllowed(index);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
  //  QPoint QAbstractItemViewPrivate::contentsOffset() const
  QPoint contentsOffset() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall14 call = reinterpret_cast<CuteQTableWidgetPrivateCall14>(taken[14]);
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
      CuteQTableWidgetPrivateCall15 call = reinterpret_cast<CuteQTableWidgetPrivateCall15>(taken[15]);
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
      CuteQTableWidgetPrivateCall16 call = reinterpret_cast<CuteQTableWidgetPrivateCall16>(taken[16]);
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
      CuteQTableWidgetPrivateCall17 call = reinterpret_cast<CuteQTableWidgetPrivateCall17>(taken[17]);
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
      CuteQTableWidgetPrivateCall18 call = reinterpret_cast<CuteQTableWidgetPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall19 call = reinterpret_cast<CuteQTableWidgetPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall20 call = reinterpret_cast<CuteQTableWidgetPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall21 call = reinterpret_cast<CuteQTableWidgetPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall22 call = reinterpret_cast<CuteQTableWidgetPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall23 call = reinterpret_cast<CuteQTableWidgetPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall24 call = reinterpret_cast<CuteQTableWidgetPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall25 call = reinterpret_cast<CuteQTableWidgetPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall26 call = reinterpret_cast<CuteQTableWidgetPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall27 call = reinterpret_cast<CuteQTableWidgetPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall28 call = reinterpret_cast<CuteQTableWidgetPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall29 call = reinterpret_cast<CuteQTableWidgetPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall30 call = reinterpret_cast<CuteQTableWidgetPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall31 call = reinterpret_cast<CuteQTableWidgetPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall32 call = reinterpret_cast<CuteQTableWidgetPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall33 call = reinterpret_cast<CuteQTableWidgetPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall34 call = reinterpret_cast<CuteQTableWidgetPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTableWidgetPrivateCall35 call = reinterpret_cast<CuteQTableWidgetPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTableWidget *QTableWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZN19QTableWidgetPrivate6q_funcEv(
    QTableWidgetPrivate *self) {
  return self->q_func();
}

//  const QTableWidget *QTableWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTableWidget *ritual_ZNK19QTableWidgetPrivate6q_funcEv(
    const QTableWidgetPrivate *self) {
  return self->q_func();
}

//  QTableModel *QTableWidgetPrivate::tableModel() const
extern "C" Q_DECL_EXPORT
QTableModel *ritual_ZNK19QTableWidgetPrivate10tableModelEv(
    const QTableWidgetPrivate *self) {
  return self->tableModel();
}

//  void QTableWidgetPrivate::setup()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate5setupEv(QTableWidgetPrivate *self) {
  self->setup();
}

//  void QTableWidgetPrivate::clearConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate16clearConnectionsEv(
    QTableWidgetPrivate *self) {
  self->clearConnections();
}

//  void QTableWidgetPrivate::emitItemPressed(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate15emitItemPressedERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemPressed(*index);
}

//  void QTableWidgetPrivate::emitItemClicked(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate15emitItemClickedERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemClicked(*index);
}

//  void QTableWidgetPrivate::emitItemDoubleClicked(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate21emitItemDoubleClickedERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemDoubleClicked(*index);
}

//  void QTableWidgetPrivate::emitItemActivated(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate17emitItemActivatedERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemActivated(*index);
}

//  void QTableWidgetPrivate::emitItemEntered(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate15emitItemEnteredERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemEntered(*index);
}

//  void QTableWidgetPrivate::emitItemChanged(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate15emitItemChangedERK11QModelIndex(
    QTableWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemChanged(*index);
}

//  void QTableWidgetPrivate::emitCurrentItemChanged(const QModelIndex
//      &previous, const QModelIndex &current)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate22emitCurrentItemChangedERK11QModelIndexS2_(
    QTableWidgetPrivate *self,
    const QModelIndex *previous,
    const QModelIndex *current) {
  self->emitCurrentItemChanged(*previous, *current);
}

//  void QTableWidgetPrivate::sort()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate4sortEv(QTableWidgetPrivate *self) {
  self->sort();
}

//  void QTableWidgetPrivate::dataChanged(const QModelIndex &topLeft, const
//      QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QTableWidgetPrivate11dataChangedERK11QModelIndexS2_(
    QTableWidgetPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->dataChanged(*topLeft, *bottomRight);
}

//  a Python function taken by a CuteQTableWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableWidgetPrivate(
    QTableWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableWidgetPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(tablewidget)
#endif  // QT_CONFIG(tablewidget)
