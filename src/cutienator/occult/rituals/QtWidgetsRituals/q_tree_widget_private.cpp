//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h, Qt 6.12.0.
//  Edited by hand on 2026-11-26: added are 15 rituals that lean on what moc
//  writes for a class of the part Qt keeps to itself, whose ritual file
//  carries moc's output, drafted by a copy of the generator that lets those
//  names through. A copy of a meta-object is a second one: 'qobject_cast'
//  between it and Qt's own does not match. Kept as it is when the generator
//  runs again.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treewidget)
#if QT_CONFIG(treewidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreewidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
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
#include <QtWidgets/qtreewidget.h>
#include <QtWidgets/qheaderview.h>
#include <QtGui/qpainter.h>
#include <QtCore/qstack.h>
#include <QtCore/qdebug.h>
#include <QtWidgets/private/qtreewidget_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/private/qtreewidgetitemiterator_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <algorithm>
#include <QtWidgets/qframe.h>
#include <QtGui/qbitmap.h>
#include <QtWidgets/qdrawutil.h>
#include <QtGui/qevent.h>
#include <QtGui/qpainter.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qstylepainter.h>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/private/qframe_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/itemviews/qtreewidget.cpp, line 21, as local:qtreewidget.cpp:QTreeModelLessThan
class QTreeModelLessThan
{
public:
    inline bool operator()(QTreeWidgetItem *i1, QTreeWidgetItem *i2) const
        { return *i1 < *i2; }
};

//  from src/widgets/itemviews/qtreewidget.cpp, line 28, as local:qtreewidget.cpp:QTreeModelGreaterThan
class QTreeModelGreaterThan
{
public:
    inline bool operator()(QTreeWidgetItem *i1, QTreeWidgetItem *i2) const
        { return *i2 < *i1; }
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

//  from src/widgets/itemviews/qtreewidget.cpp, line 191, as _ZNK10QTreeModel5indexEPK15QTreeWidgetItemi
inline QModelIndex QTreeModel::index(const QTreeWidgetItem *item, int column) const
{
    executePendingSort();

    if (!item || (item == rootItem))
        return QModelIndex();
    const QTreeWidgetItem *par = item->parent();
    QTreeWidgetItem *itm = const_cast<QTreeWidgetItem*>(item);
    if (!par)
        par = rootItem;
    int row;
    int guess = item->d->rowGuess;
    if (guess >= 0
        && par->children.size() > guess
        && par->children.at(guess) == itm) {
        row = guess;
    } else {
        row = par->children.lastIndexOf(itm);
        itm->d->rowGuess = row;
    }
    return createIndex(row, column, itm);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 177, as _ZNK10QTreeModel4itemERK11QModelIndex
inline QTreeWidgetItem *QTreeModel::item(const QModelIndex &index) const
{
    if (!index.isValid())
        return nullptr;
    return static_cast<QTreeWidgetItem*>(index.internalPointer());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 569, as _ZN10QTreeModel12ensureSortedEiN2Qt9SortOrderEiiRK11QModelIndex
inline void QTreeModel::ensureSorted(int column, Qt::SortOrder order,
                              int start, int end, const QModelIndex &parent)
{
    if (isChanging())
        return;

    sortPendingTimer.stop();

    if (column < 0 || column >= columnCount())
        return;

    SkipSorting skipSorting(this);

    QTreeWidgetItem *itm = item(parent);
    if (!itm)
        itm = rootItem;
    QList<QTreeWidgetItem*> lst = itm->children;

    int count = end - start + 1;
    QList<std::pair<QTreeWidgetItem *, int>> sorting(count);
    for (int i = 0; i < count; ++i) {
        sorting[i].first = lst.at(start + i);
        sorting[i].second = start + i;
    }

    const auto compare = (order == Qt::AscendingOrder ? &itemLessThan : &itemGreaterThan);
    std::stable_sort(sorting.begin(), sorting.end(), compare);

    QModelIndexList oldPersistentIndexes;
    QModelIndexList newPersistentIndexes;
    QList<QTreeWidgetItem*>::iterator lit = lst.begin();
    bool changed = false;

    for (int i = 0; i < count; ++i) {
        int oldRow = sorting.at(i).second;

        int tmpitepos = lit - lst.begin();
        QTreeWidgetItem *item = lst.takeAt(oldRow);
        if (tmpitepos > lst.size())
            --tmpitepos;
        lit = lst.begin() + tmpitepos;

        lit = sortedInsertionIterator(lit, lst.end(), order, item);
        int newRow = qMax<qsizetype>(lit - lst.begin(), 0);

        if ((newRow < oldRow) && !(*item < *lst.at(oldRow - 1)) && !(*lst.at(oldRow - 1) < *item ))
            newRow = oldRow;

        lit = lst.insert(lit, item);
        if (newRow != oldRow) {
            // we are going to change the persistent indexes, so we need to prepare
            if (!changed) { // this will only happen once
                changed = true;
                emit layoutAboutToBeChanged({parent}, QAbstractItemModel::VerticalSortHint); // the selection model needs to know
                oldPersistentIndexes = persistentIndexList();
                newPersistentIndexes = oldPersistentIndexes;
            }
            for (int j = i + 1; j < count; ++j) {
                int otherRow = sorting.at(j).second;
                if (oldRow < otherRow && newRow >= otherRow)
                    --sorting[j].second;
                else if (oldRow > otherRow && newRow <= otherRow)
                    ++sorting[j].second;
            }
            for (int k = 0; k < newPersistentIndexes.size(); ++k) {
                QModelIndex pi = newPersistentIndexes.at(k);
                if (pi.parent() != parent)
                    continue;
                int oldPersistentRow = pi.row();
                int newPersistentRow = oldPersistentRow;
                if (oldPersistentRow == oldRow)
                    newPersistentRow = newRow;
                else if (oldRow < oldPersistentRow && newRow >= oldPersistentRow)
                    newPersistentRow = oldPersistentRow - 1;
                else if (oldRow > oldPersistentRow && newRow <= oldPersistentRow)
                    newPersistentRow = oldPersistentRow + 1;
                if (newPersistentRow != oldPersistentRow)
                    newPersistentIndexes[k] = createIndex(newPersistentRow,
                                                          pi.column(), pi.internalPointer());
            }
        }
    }

    if (changed) {
        itm->children = lst;
        changePersistentIndexList(oldPersistentIndexes, newPersistentIndexes);
        emit layoutChanged({parent}, QAbstractItemModel::VerticalSortHint);
    }
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

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 133, as _ZN26QAbstractScrollAreaPrivateC2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::QAbstractScrollAreaPrivate()
    :hbar(nullptr), vbar(nullptr), vbarpolicy(Qt::ScrollBarAsNeeded), hbarpolicy(Qt::ScrollBarAsNeeded),
     shownOnce(false), inResize(false), sizeAdjustPolicy(QAbstractScrollArea::AdjustIgnored),
     viewport(nullptr), cornerWidget(nullptr), left(0), top(0), right(0), bottom(0),
     xoffset(0), yoffset(0), viewportFilter(nullptr)
{
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 141, as _ZN26QAbstractScrollAreaPrivateD2Ev
#if QT_CONFIG(scrollarea)
inline QAbstractScrollAreaPrivate::~QAbstractScrollAreaPrivate()
{
}
#endif  // QT_CONFIG(scrollarea)

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

//  from src/widgets/widgets/qabstractscrollarea.cpp, line 1368, as _ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv
#if QT_CONFIG(scrollarea)
inline QPoint QAbstractScrollAreaPrivate::contentsOffset() const
{
    Q_Q(const QAbstractScrollArea);
    QPoint offset;
    if (vbar->isVisible())
        offset.setY(vbar->value());
    if (hbar->isVisible()) {
        if (q->isRightToLeft())
            offset.setX(hbar->maximum() - hbar->value());
        else
            offset.setX(hbar->value());
    }
    return offset;
}
#endif  // QT_CONFIG(scrollarea)

//  from src/widgets/itemviews/qtreewidget.cpp, line 766, as _ZNK10QTreeModel10isChangingEv
inline bool QTreeModel::isChanging() const
{
    Q_D(const QTreeModel);
    return !d->changes.isEmpty();
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 668, as _ZN10QTreeModel12itemLessThanERKSt4pairIP15QTreeWidgetItemiES5_
inline bool QTreeModel::itemLessThan(const std::pair<QTreeWidgetItem*,int> &left,
                              const std::pair<QTreeWidgetItem*,int> &right)
{
    return *(left.first) < *(right.first);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 683, as _ZN10QTreeModel15itemGreaterThanERKSt4pairIP15QTreeWidgetItemiES5_
inline bool QTreeModel::itemGreaterThan(const std::pair<QTreeWidgetItem*,int> &left,
                                 const std::pair<QTreeWidgetItem*,int> &right)
{
    return *(right.first) < *(left.first);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 692, as _ZN10QTreeModel23sortedInsertionIteratorERKN5QListIP15QTreeWidgetItemE8iteratorES6_N2Qt9SortOrderES2_
inline QList<QTreeWidgetItem*>::iterator QTreeModel::sortedInsertionIterator(
    const QList<QTreeWidgetItem*>::iterator &begin,
    const QList<QTreeWidgetItem*>::iterator &end,
    Qt::SortOrder order, QTreeWidgetItem *item)
{
    if (order == Qt::AscendingOrder)
        return std::lower_bound(begin, end, item, QTreeModelLessThan());
    return std::lower_bound(begin, end, item, QTreeModelGreaterThan());
}

//  from src/widgets/widgets/qframe.cpp, line 19, as _ZN13QFramePrivateC2Ev
inline QFramePrivate::QFramePrivate()
    : frect(0, 0, 0, 0),
      frameStyle(QFrame::NoFrame | QFrame::Plain),
      lineWidth(1),
      midLineWidth(0),
      frameWidth(0),
      leftFrameWidth(0), rightFrameWidth(0),
      topFrameWidth(0), bottomFrameWidth(0)
{
}

//  from src/widgets/widgets/qframe.cpp, line 30, as _ZN13QFramePrivateD2Ev
inline QFramePrivate::~QFramePrivate()
{
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2293, as _ZN18QTreeWidgetPrivate16clearConnectionsEv
inline void QTreeWidgetPrivate::clearConnections()
{
    for (QMetaObject::Connection &connection : connections)
        QObject::disconnect(connection);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2299, as _ZN18QTreeWidgetPrivate15emitItemPressedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemPressed(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemPressed(item(index), index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2305, as _ZN18QTreeWidgetPrivate15emitItemClickedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemClicked(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemClicked(item(index), index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2311, as _ZN18QTreeWidgetPrivate21emitItemDoubleClickedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemDoubleClicked(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemDoubleClicked(item(index), index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2317, as _ZN18QTreeWidgetPrivate17emitItemActivatedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemActivated(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemActivated(item(index), index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2323, as _ZN18QTreeWidgetPrivate15emitItemEnteredERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemEntered(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemEntered(item(index), index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2329, as _ZN18QTreeWidgetPrivate15emitItemChangedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemChanged(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    QTreeWidgetItem *indexItem = item(index);
    if (indexItem)
        emit q->itemChanged(indexItem, index.column());
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2337, as _ZN18QTreeWidgetPrivate16emitItemExpandedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemExpanded(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemExpanded(item(index));
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2343, as _ZN18QTreeWidgetPrivate17emitItemCollapsedERK11QModelIndex
inline void QTreeWidgetPrivate::emitItemCollapsed(const QModelIndex &index)
{
    Q_Q(QTreeWidget);
    emit q->itemCollapsed(item(index));
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2349, as _ZN18QTreeWidgetPrivate22emitCurrentItemChangedERK11QModelIndexS2_
inline void QTreeWidgetPrivate::emitCurrentItemChanged(const QModelIndex &current,
                                                const QModelIndex &previous)
{
    Q_Q(QTreeWidget);
    QTreeWidgetItem *currentItem = item(current);
    QTreeWidgetItem *previousItem = item(previous);
    emit q->currentItemChanged(currentItem, previousItem);
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2358, as _ZN18QTreeWidgetPrivate4sortEv
inline void QTreeWidgetPrivate::sort()
{
    if (sortingEnabled) {
        int column = header->sortIndicatorSection();
        Qt::SortOrder order = header->sortIndicatorOrder();
        treeModel()->sort(column, order);
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2387, as _ZN18QTreeWidgetPrivate11dataChangedERK11QModelIndexS2_
inline void QTreeWidgetPrivate::dataChanged(const QModelIndex &topLeft,
                                     const QModelIndex &bottomRight)
{
    if (sortingEnabled && topLeft.isValid() && bottomRight.isValid()
        && !treeModel()->sortPendingTimer.isActive()) {
        int column = header->sortIndicatorSection();
        if (column >= topLeft.column() && column <= bottomRight.column()) {
            Qt::SortOrder order = header->sortIndicatorOrder();
            treeModel()->ensureSorted(column, order, topLeft.row(),
                                  bottomRight.row(), topLeft.parent());
        }
    }
}

//  from src/widgets/itemviews/qtreewidget.cpp, line 2367, as _ZN18QTreeWidgetPrivate16selectionChangedERK14QItemSelectionS2_
inline void QTreeWidgetPrivate::selectionChanged(const QItemSelection &selected, const QItemSelection &deselected)
{
    Q_Q(QTreeWidget);
    QModelIndexList indices = selected.indexes();
    int i;
    QTreeModel *m = treeModel();
    for (i = 0; i < indices.size(); ++i) {
        QTreeWidgetItem *item = m->item(indices.at(i));
        item->d->selected = true;
    }

    indices = deselected.indexes();
    for (i = 0; i < indices.size(); ++i) {
        QTreeWidgetItem *item = m->item(indices.at(i));
        item->d->selected = false;
    }

    emit q->itemSelectionChanged();
}
//  -----------------------------------------------------------------------

//  A QTreeWidgetPrivate that Python can take functions over in. Every QTreeWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetPrivateCall0)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeWidgetPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeWidgetPrivateCall4)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeWidgetPrivateCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeWidgetPrivateCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall7)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall8)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall9)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall11)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall12)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeWidgetPrivateCall13)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeWidgetPrivateCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQTreeWidgetPrivateCall15)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeWidgetPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTreeWidgetPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTreeWidgetPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQTreeWidgetPrivateCall19)(const void *, int, int *);
typedef void (*CuteQTreeWidgetPrivateCall20)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall21)(const void *, int *);
typedef void * (*CuteQTreeWidgetPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTreeWidgetPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTreeWidgetPrivateCall24)(const void *, int *);
typedef int (*CuteQTreeWidgetPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQTreeWidgetPrivateCall26)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall27)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall28)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall29)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall30)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall31)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall32)(const void *, int *);
typedef void (*CuteQTreeWidgetPrivateCall33)(const void *, int *);
typedef bool (*CuteQTreeWidgetPrivateCall34)(const void *, int *);
typedef bool (*CuteQTreeWidgetPrivateCall35)(const void *, int *);
class CuteQTreeWidgetPrivate : public QTreeWidgetPrivate {
public:
  using QTreeWidgetPrivate::QTreeWidgetPrivate;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14modelDestroyedEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate13layoutChangedEv")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZNK26QAbstractScrollAreaPrivate14contentsOffsetEv")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
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
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem
  //      *option, const QModelIndex &current) const
  void adjustViewOptionsForIndex(
      QStyleOptionViewItem *option,
      const QModelIndex &current) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall0 call = reinterpret_cast<CuteQTreeWidgetPrivateCall0>(taken[0]);
      call(this, option, &current, &handled);
      if (handled) return;
    }
    QTreeViewPrivate::adjustViewOptionsForIndex(option, current);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::columnsAboutToBeRemoved(const QModelIndex &a0,
  //      int a1, int a2)
  void columnsAboutToBeRemoved(
      const QModelIndex &a0,
      int a1,
      int a2) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall1 call = reinterpret_cast<CuteQTreeWidgetPrivateCall1>(taken[1]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QTreeViewPrivate::columnsAboutToBeRemoved(a0, a1, a2);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::columnsRemoved(const QModelIndex &a0, int a1,
  //      int a2)
  void columnsRemoved(const QModelIndex &a0, int a1, int a2) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall2 call = reinterpret_cast<CuteQTreeWidgetPrivateCall2>(taken[2]);
      call(this, &a0, a1, a2, &handled);
      if (handled) return;
    }
    QTreeViewPrivate::columnsRemoved(a0, a1, a2);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  void QTreeViewPrivate::modelDestroyed()
  void modelDestroyed() override {
    if (taken[3]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall3 call = reinterpret_cast<CuteQTreeWidgetPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QTreeViewPrivate::modelDestroyed();
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  QRect QTreeViewPrivate::intersectedRect(const QRect rect, const
  //      QModelIndex &topLeft, const QModelIndex &bottomRight) const
  QRect intersectedRect(
      const QRect rect,
      const QModelIndex &topLeft,
      const QModelIndex &bottomRight) const override {
    if (taken[4]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall4 call = reinterpret_cast<CuteQTreeWidgetPrivateCall4>(taken[4]);
      const QRect * given = call(this, &rect, &topLeft, &bottomRight, &handled);
      if (handled && given) return *given;
    }
    return QTreeViewPrivate::intersectedRect(rect, topLeft, bottomRight);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
  //  QRect QTreeViewPrivate::visualRect(const QModelIndex &index) const
  QRect visualRect(const QModelIndex &index) const override {
    if (taken[5]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall5 call = reinterpret_cast<CuteQTreeWidgetPrivateCall5>(taken[5]);
      const QRect * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return QTreeViewPrivate::visualRect(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
  //  int QTreeViewPrivate::accessibleChildIndex(const QModelIndex &index)
  //      const
  int accessibleChildIndex(const QModelIndex &index) const override {
    if (taken[6]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall6 call = reinterpret_cast<CuteQTreeWidgetPrivateCall6>(taken[6]);
      int given = call(this, &index, &handled);
      if (handled) return given;
    }
    return QTreeViewPrivate::accessibleChildIndex(index);
  }
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
  //      int start, int end)
  void rowsRemoved(const QModelIndex &parent, int start, int end) override {
    if (taken[7]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall7 call = reinterpret_cast<CuteQTreeWidgetPrivateCall7>(taken[7]);
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
    if (taken[8]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall8 call = reinterpret_cast<CuteQTreeWidgetPrivateCall8>(taken[8]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::rowsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::columnsInserted(const QModelIndex
  //      &parent, int start, int end)
  void columnsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[9]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall9 call = reinterpret_cast<CuteQTreeWidgetPrivateCall9>(taken[9]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::layoutChanged()
  void layoutChanged() override {
    if (taken[10]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall10 call = reinterpret_cast<CuteQTreeWidgetPrivateCall10>(taken[10]);
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
    if (taken[11]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall11 call = reinterpret_cast<CuteQTreeWidgetPrivateCall11>(taken[11]);
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
    if (taken[12]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall12 call = reinterpret_cast<CuteQTreeWidgetPrivateCall12>(taken[12]);
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
    if (taken[13]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall13 call = reinterpret_cast<CuteQTreeWidgetPrivateCall13>(taken[13]);
      call(this, static_cast<int>(command.toInt()), &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::selectAll(command);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  bool QAbstractItemViewPrivate::selectionAllowed(const QModelIndex
  //      &index) const
  bool selectionAllowed(const QModelIndex &index) const override {
    if (taken[14]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall14 call = reinterpret_cast<CuteQTreeWidgetPrivateCall14>(taken[14]);
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
    if (taken[15]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall15 call = reinterpret_cast<CuteQTreeWidgetPrivateCall15>(taken[15]);
      const QPoint * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractItemViewPrivate::contentsOffset();
  }
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)

#if QT_CONFIG(scrollarea)
  //  void
  //      QAbstractScrollAreaPrivate::scrollBarPolicyChanged(Qt::Orientatio
  //      n a0, Qt::ScrollBarPolicy a1)
  void scrollBarPolicyChanged(
      Qt::Orientation a0,
      Qt::ScrollBarPolicy a1) override {
    if (taken[16]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall16 call = reinterpret_cast<CuteQTreeWidgetPrivateCall16>(taken[16]);
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
      CuteQTreeWidgetPrivateCall17 call = reinterpret_cast<CuteQTreeWidgetPrivateCall17>(taken[17]);
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
      CuteQTreeWidgetPrivateCall18 call = reinterpret_cast<CuteQTreeWidgetPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall19 call = reinterpret_cast<CuteQTreeWidgetPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall20 call = reinterpret_cast<CuteQTreeWidgetPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall21 call = reinterpret_cast<CuteQTreeWidgetPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall22 call = reinterpret_cast<CuteQTreeWidgetPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall23 call = reinterpret_cast<CuteQTreeWidgetPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall24 call = reinterpret_cast<CuteQTreeWidgetPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall25 call = reinterpret_cast<CuteQTreeWidgetPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall26 call = reinterpret_cast<CuteQTreeWidgetPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall27 call = reinterpret_cast<CuteQTreeWidgetPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall28 call = reinterpret_cast<CuteQTreeWidgetPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall29 call = reinterpret_cast<CuteQTreeWidgetPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall30 call = reinterpret_cast<CuteQTreeWidgetPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall31 call = reinterpret_cast<CuteQTreeWidgetPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall32 call = reinterpret_cast<CuteQTreeWidgetPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall33 call = reinterpret_cast<CuteQTreeWidgetPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall34 call = reinterpret_cast<CuteQTreeWidgetPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTreeWidgetPrivateCall35 call = reinterpret_cast<CuteQTreeWidgetPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTreeWidget *QTreeWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTreeWidget *ritual_ZN18QTreeWidgetPrivate6q_funcEv(
    QTreeWidgetPrivate *self) {
  return self->q_func();
}

//  const QTreeWidget *QTreeWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTreeWidget *ritual_ZNK18QTreeWidgetPrivate6q_funcEv(
    const QTreeWidgetPrivate *self) {
  return self->q_func();
}

//  void QTreeWidgetPrivate::clearConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate16clearConnectionsEv(
    QTreeWidgetPrivate *self) {
  self->clearConnections();
}

//  QTreeModel *QTreeWidgetPrivate::treeModel() const
extern "C" Q_DECL_EXPORT
QTreeModel *ritual_ZNK18QTreeWidgetPrivate9treeModelEv(
    const QTreeWidgetPrivate *self) {
  return self->treeModel();
}

//  QModelIndex QTreeWidgetPrivate::index(const QTreeWidgetItem *item, int
//      column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QTreeWidgetPrivate5indexEPK15QTreeWidgetItemi(
    const QTreeWidgetPrivate *self,
    const QTreeWidgetItem *item,
    int column) {
  return new QModelIndex(self->index(item, column));
}

//  QTreeWidgetItem *QTreeWidgetPrivate::item(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK18QTreeWidgetPrivate4itemERK11QModelIndex(
    const QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  return self->item(*index);
}

//  void QTreeWidgetPrivate::emitItemPressed(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate15emitItemPressedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemPressed(*index);
}

//  void QTreeWidgetPrivate::emitItemClicked(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate15emitItemClickedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemClicked(*index);
}

//  void QTreeWidgetPrivate::emitItemDoubleClicked(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate21emitItemDoubleClickedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemDoubleClicked(*index);
}

//  void QTreeWidgetPrivate::emitItemActivated(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate17emitItemActivatedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemActivated(*index);
}

//  void QTreeWidgetPrivate::emitItemEntered(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate15emitItemEnteredERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemEntered(*index);
}

//  void QTreeWidgetPrivate::emitItemChanged(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate15emitItemChangedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemChanged(*index);
}

//  void QTreeWidgetPrivate::emitItemExpanded(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate16emitItemExpandedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemExpanded(*index);
}

//  void QTreeWidgetPrivate::emitItemCollapsed(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate17emitItemCollapsedERK11QModelIndex(
    QTreeWidgetPrivate *self,
    const QModelIndex *index) {
  self->emitItemCollapsed(*index);
}

//  void QTreeWidgetPrivate::emitCurrentItemChanged(const QModelIndex
//      &previous, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate22emitCurrentItemChangedERK11QModelIndexS2_(
    QTreeWidgetPrivate *self,
    const QModelIndex *previous,
    const QModelIndex *index) {
  self->emitCurrentItemChanged(*previous, *index);
}

//  void QTreeWidgetPrivate::sort()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate4sortEv(QTreeWidgetPrivate *self) {
  self->sort();
}

//  void QTreeWidgetPrivate::dataChanged(const QModelIndex &topLeft, const
//      QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate11dataChangedERK11QModelIndexS2_(
    QTreeWidgetPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->dataChanged(*topLeft, *bottomRight);
}

//  void QTreeWidgetPrivate::selectionChanged(const QItemSelection &selected,
//      const QItemSelection &deselected)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QTreeWidgetPrivate16selectionChangedERK14QItemSelectionS2_(
    QTreeWidgetPrivate *self,
    const QItemSelection *selected,
    const QItemSelection *deselected) {
  self->selectionChanged(*selected, *deselected);
}

//  a Python function taken by a CuteQTreeWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeWidgetPrivate(
    QTreeWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTreeWidgetPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(treewidget)
#endif  // QT_CONFIG(treewidget)
