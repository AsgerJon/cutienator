//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listview)
#if QT_CONFIG(listview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qbsptree_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qbsptree_p.h>
#include <QtWidgets/qlistview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qstylepainter.h>
#include <QtGui/qbitmap.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(draganddrop)
#include <QtGui/qdrag.h>
#endif
#include <QtGui/qevent.h>
#include <QtCore/qlist.h>
#if QT_CONFIG(rubberband)
#include <QtWidgets/qrubberband.h>
#endif
#include <QtWidgets/qscrollbar.h>
#include <QtWidgets/qstyle.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qlistview_p.h>
#include <QtWidgets/private/qscrollbar_p.h>
#include <algorithm>
#include <QtWidgets/qapplication.h>
#include <QtWidgets/qabstractslider.h>
#include <QtGui/qevent.h>
#include <QtWidgets/private/qabstractslider_p.h>
#include <QtCore/qdebug.h>
#if QT_CONFIG(accessibility)
#include <QtGui/qaccessible.h>
#endif
#include <limits.h>
#include <QtWidgets/private/qapplication_p.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qbsptree.cpp, line 9, as _ZN8QBspTreeC1Ev
inline QBspTree::QBspTree() : depth(6), visited(0) {}

//  from src/widgets/itemviews/qlistview.cpp, line 3254, as _ZNK17QIconModeViewBase9itemIndexERK13QListViewItem
inline int QIconModeViewBase::itemIndex(const QListViewItem &item) const
{
    if (!item.isValid())
        return -1;
    int i = item.indexHint;
    if (i < items.size()) {
        if (items.at(i) == item)
            return i;
    } else {
        i = items.size() - 1;
    }

    int j = i;
    int c = items.size();
    bool a = true;
    bool b = true;

    while (a || b) {
        if (a) {
            if (items.at(i) == item) {
                items.at(i).indexHint = i;
                return i;
            }
            a = ++i < c;
        }
        if (b) {
            if (items.at(j) == item) {
                items.at(j).indexHint = j;
                return j;
            }
            b = --j > -1;
        }
    }
    return -1;
}

//  from src/widgets/itemviews/qlistview.cpp, line 3050, as _ZNK17QIconModeViewBase19indexToListViewItemERK11QModelIndex
inline QListViewItem QIconModeViewBase::indexToListViewItem(const QModelIndex &index) const
{
    if (index.isValid() && index.row() < items.size())
        return items.at(index.row());
    return QListViewItem();
}

//  from src/widgets/itemviews/qlistview.cpp, line 3034, as _ZN17QIconModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi
inline bool QIconModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo &info, int max)
{
    if (info.last >= items.size()) {
        //first we create the items
        QStyleOptionViewItem option;
        initViewItemOption(&option);
        for (int row = items.size(); row <= info.last; ++row) {
            QSize size = itemSize(option, modelIndex(row));
            QListViewItem item(QRect(0, 0, size.width(), size.height()), row); // default pos
            items.append(item);
        }
        doDynamicLayout(info);
    }
    return (batchStartRow > max); // done
}

//  from src/widgets/itemviews/qlistview.cpp, line 3366, as _ZN17QIconModeViewBase5clearEv
inline void QIconModeViewBase::clear()
{
    tree.destroy();
    items.clear();
    moved.clear();
    batchStartRow = 0;
    batchSavedDeltaSeg = 0;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2999, as _ZN17QIconModeViewBase11setRowCountEi
inline void QIconModeViewBase::setRowCount(int rowCount)
{
    tree.create(qMax(rowCount - hiddenCount(), 0));
}

//  from src/widgets/itemviews/qlistview.cpp, line 3235, as _ZNK17QIconModeViewBase15intersectingSetERK5QRect
inline QList<QModelIndex> QIconModeViewBase::intersectingSet(const QRect &area) const
{
    QIconModeViewBase *that = const_cast<QIconModeViewBase*>(this);
    QBspTree::Data data(static_cast<void*>(that));
    QList<QModelIndex> res;
    that->interSectingVector = &res;
    that->tree.climbTree(area, &QIconModeViewBase::addLeaf, data);
    that->interSectingVector = nullptr;
    return res;
}

//  from src/widgets/itemviews/qlistview.cpp, line 3004, as _ZN17QIconModeViewBase16scrollContentsByEiib
inline void QIconModeViewBase::scrollContentsBy(int dx, int dy, bool scrollElasticBand)
{
    if (scrollElasticBand)
        dd->scrollElasticBandBy(isRightToLeft() ? -dx : dx, dy);

    QCommonListViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
    if (!draggedItems.isEmpty())
        viewport()->update(draggedItemsRect().translated(dx, dy));
}

//  from src/widgets/itemviews/qlistview.cpp, line 3014, as _ZN17QIconModeViewBase11dataChangedERK11QModelIndexS2_
inline void QIconModeViewBase::dataChanged(const QModelIndex &topLeft, const QModelIndex &bottomRight)
{
    if (column() >= topLeft.column() && column() <= bottomRight.column())  {
        QStyleOptionViewItem option;
        initViewItemOption(&option);
        const int bottom = qMin(items.size(), bottomRight.row() + 1);
        const bool useItemSize = !dd->grid.isValid();
        for (int row = topLeft.row(); row < bottom; ++row)
        {
            QSize s = itemSize(option, modelIndex(row));
            if (!useItemSize)
            {
                s.setWidth(qMin(dd->grid.width(), s.width()));
                s.setHeight(qMin(dd->grid.height(), s.height()));
            }
            items[row].resize(s);
        }
    }
}

//  from src/widgets/itemviews/qlistview.cpp, line 2854, as _ZN17QIconModeViewBase15appendHiddenRowEi
inline void QIconModeViewBase::appendHiddenRow(int row)
{
    if (row >= 0 && row < items.size()) //remove item
        tree.removeLeaf(items.at(row).rect(), row);
    QCommonListViewBase::appendHiddenRow(row);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2861, as _ZN17QIconModeViewBase15removeHiddenRowEi
inline void QIconModeViewBase::removeHiddenRow(int row)
{
    QCommonListViewBase::removeHiddenRow(row);
    if (row >= 0 && row < items.size()) //insert item
        tree.insertLeaf(items.at(row).rect(), row);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2841, as _ZN17QIconModeViewBase19setPositionForIndexERK6QPointRK11QModelIndex
inline void QIconModeViewBase::setPositionForIndex(const QPoint &position, const QModelIndex &index)
{
    if (index.row() >= items.size())
        return;
    const QSize oldContents = contentsSize;
    qq->update(index); // update old position
    moveItem(index.row(), position);
    qq->update(index); // update new position

    if (contentsSize != oldContents)
        dd->viewUpdateGeometries(); // update the scroll bars
}

//  from src/widgets/itemviews/qlistview.cpp, line 2955, as _ZN17QIconModeViewBase19filterDragMoveEventEP14QDragMoveEvent
#if QT_CONFIG(draganddrop)
inline bool QIconModeViewBase::filterDragMoveEvent(QDragMoveEvent *e)
{
    const bool wasAccepted = e->isAccepted();

    // ignore by default
    e->ignore();

    if (e->source() != qq || !dd->canDrop(e)) {
        // restore previous acceptance on failure
        e->setAccepted(wasAccepted);
        return false;
    }

    // get old dragged items rect
    QRect itemsRect = this->itemsRect(draggedItems);
    viewport()->update(itemsRect.translated(draggedItemsDelta()));
    // update position
    draggedItemsPos = e->position().toPoint();
    // get new items rect
    viewport()->update(itemsRect.translated(draggedItemsDelta()));
    // set the item under the cursor to current
    QModelIndex index;
    if (movement() == QListView::Snap) {
        QRect rect(snapToGrid(e->position().toPoint() + offset()), gridSize());
        const QList<QModelIndex> intersectVector = intersectingSet(rect);
        index = intersectVector.size() > 0 ? intersectVector.last() : QModelIndex();
    } else {
        index = qq->indexAt(e->position().toPoint());
    }
    // check if we allow drops here
    if (draggedItems.contains(index))
        e->accept(); // allow changing item position
    else if (dd->model->flags(index) & Qt::ItemIsDropEnabled)
        e->accept(); // allow dropping on dropenabled items
    else if (!index.isValid())
        e->accept(); // allow dropping in empty areas

    // the event was treated. do autoscrolling
    if (dd->shouldAutoScroll(e->position().toPoint()))
        dd->startAutoScroll();
    return true;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 2948, as _ZN17QIconModeViewBase20filterDragLeaveEventEP15QDragLeaveEvent
#if QT_CONFIG(draganddrop)
inline bool QIconModeViewBase::filterDragLeaveEvent(QDragLeaveEvent *e)
{
    viewport()->update(draggedItemsRect()); // erase the area
    draggedItemsPos = QPoint(-1, -1); // don't draw the dragged items
    return QCommonListViewBase::filterDragLeaveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 2904, as _ZN17QIconModeViewBase15filterDropEventEP10QDropEvent
#if QT_CONFIG(draganddrop)
inline bool QIconModeViewBase::filterDropEvent(QDropEvent *e)
{
    if (e->source() != qq)
        return false;

    const QSize contents = contentsSize;
    QPoint offset(horizontalOffset(), verticalOffset());
    QPoint end = e->position().toPoint() + offset;
    if (qq->acceptDrops()) {
        const Qt::ItemFlags dropableFlags = Qt::ItemIsDropEnabled|Qt::ItemIsEnabled;
        const QList<QModelIndex> &dropIndices = intersectingSet(QRect(end, QSize(1, 1)));
        for (const QModelIndex &index : dropIndices)
            if ((index.flags() & dropableFlags) == dropableFlags)
                return false;
    }
    QPoint start = dd->pressedPosition;
    QPoint delta = (dd->movement == QListView::Snap ? snapToGrid(end) - snapToGrid(start) : end - start);
    const QList<QModelIndex> indexes = dd->selectionModel->selectedIndexes();
    for (const auto &index : indexes) {
        QRect rect = dd->rectForIndex(index);
        viewport()->update(dd->mapToViewport(rect, false));
        QPoint dest = rect.topLeft() + delta;
        if (qq->isRightToLeft())
            dest.setX(dd->flipX(dest.x()) - rect.width());
        moveItem(index.row(), dest);
        qq->update(index);
    }
    dd->stopAutoScroll();
    draggedItems.clear();
    dd->emitIndexesMoved(indexes);
    // do not delete item on internal move, see filterStartDrag()
    dd->dropEventMoved = true;
    e->accept(); // we have handled the event
    // if the size has not grown, we need to check if it has shrunk
    if (contentsSize != contents) {
        if ((contentsSize.width() <= contents.width()
            || contentsSize.height() <= contents.height())) {
                updateContentsSize();
        }
        dd->viewUpdateGeometries();
    }
    return true;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 2869, as _ZN17QIconModeViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE
#if QT_CONFIG(draganddrop)
inline bool QIconModeViewBase::filterStartDrag(Qt::DropActions supportedActions)
{
    // This function does the same thing as in QAbstractItemView::startDrag(),
    // plus adding viewitems to the draggedItems list.
    // We need these items to draw the drag items
    QModelIndexList indexes = dd->selectionModel->selectedIndexes();
    if (indexes.size() > 0 ) {
        if (viewport()->acceptDrops()) {
            QModelIndexList::ConstIterator it = indexes.constBegin();
            for (; it != indexes.constEnd(); ++it)
                if (dd->model->flags(*it) & Qt::ItemIsDragEnabled
                    && (*it).column() == dd->column)
                    draggedItems.push_back(*it);
        }

        QRect rect;
        QPixmap pixmap = dd->renderToPixmap(indexes, &rect);
        rect.adjust(horizontalOffset(), verticalOffset(), 0, 0);
        QDrag *drag = new QDrag(qq);
        drag->setMimeData(dd->model->mimeData(indexes));
        drag->setPixmap(pixmap);
        drag->setHotSpot(dd->pressedPosition - rect.topLeft());
        dd->dropEventMoved = false;
        Qt::DropAction action = drag->exec(supportedActions, dd->defaultDropAction);
        draggedItems.clear();
        // delete item, unless it has already been moved internally (see filterDropEvent)
        if (action == Qt::MoveAction && !dd->dropEventMoved) {
            if (dd->dragDropMode != QAbstractItemView::InternalMove || drag->target() == qq->viewport())
                dd->clearOrRemove();
        }
        dd->dropEventMoved = false;
    }
    return true;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qlistview.cpp, line 2071, as _ZNK19QCommonListViewBase23horizontalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_
inline int QCommonListViewBase::horizontalScrollToValue(const int /*index*/, QListView::ScrollHint hint,
                                            bool leftOf, bool rightOf, const QRect &area, const QRect &rect) const
{
    int horizontalValue = horizontalScrollBar()->value();
    if (isRightToLeft()) {
        if (hint == QListView::PositionAtCenter) {
            horizontalValue += ((area.width() - rect.width()) / 2) - rect.left();
        } else {
            if (leftOf)
                horizontalValue -= rect.left();
            else if (rightOf)
                horizontalValue += qMin(rect.left(), area.width() - rect.right());
        }
    } else {
        if (hint == QListView::PositionAtCenter) {
            horizontalValue += rect.left() - ((area.width()- rect.width()) / 2);
        } else {
            if (leftOf)
                horizontalValue += rect.left();
            else if (rightOf)
                horizontalValue += qMin(rect.left(), rect.right() - area.width());
        }
    }
    return horizontalValue;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2052, as _ZNK19QCommonListViewBase21verticalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_
inline int QCommonListViewBase::verticalScrollToValue(int /*index*/, QListView::ScrollHint hint,
                                          bool above, bool below, const QRect &area, const QRect &rect) const
{
    int verticalValue = verticalScrollBar()->value();
    QRect adjusted = rect.adjusted(-spacing(), -spacing(), spacing(), spacing());
    if (hint == QListView::PositionAtTop || above)
        verticalValue += adjusted.top();
    else if (hint == QListView::PositionAtBottom || below)
        verticalValue += qMin(adjusted.top(), adjusted.bottom() - area.height() + 1);
    else if (hint == QListView::PositionAtCenter)
        verticalValue += adjusted.top() - ((area.height() - adjusted.height()) / 2);
    return verticalValue;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2047, as _ZN19QCommonListViewBase16scrollContentsByEiib
inline void QCommonListViewBase::scrollContentsBy(int dx, int dy, bool /*scrollElasticBand*/)
{
    dd->scrollContentsBy(isRightToLeft() ? -dx : dx, dy);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2066, as _ZNK19QCommonListViewBase16horizontalOffsetEv
inline int QCommonListViewBase::horizontalOffset() const
{
    return (isRightToLeft() ? horizontalScrollBar()->maximum() - horizontalScrollBar()->value() : horizontalScrollBar()->value());
}

//  from src/widgets/itemviews/qlistview.cpp, line 1987, as _ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize
inline void QCommonListViewBase::updateHorizontalScrollBar(const QSize &step)
{
    horizontalScrollBar()->d_func()->itemviewChangeSingleStep(step.width() + spacing());
    horizontalScrollBar()->setPageStep(viewport()->width());

    // If both scroll bars are set to auto, we might end up in a situation with enough space
    // for the actual content. But still one of the scroll bars will become enabled due to
    // the other one using the space. The other one will become invisible in the same cycle.
    // -> Infinite loop, QTBUG-39902
    const bool bothScrollBarsAuto = qq->verticalScrollBarPolicy() == Qt::ScrollBarAsNeeded &&
                                    qq->horizontalScrollBarPolicy() == Qt::ScrollBarAsNeeded;

    const QSize viewportSize = QListModeViewBase::viewportSize(qq);

    bool verticalWantsToShow = contentsSize.height() > viewportSize.height();
    bool horizontalWantsToShow;
    if (verticalWantsToShow)
        horizontalWantsToShow = contentsSize.width() > viewportSize.width() - qq->verticalScrollBar()->width();
    else
        horizontalWantsToShow = contentsSize.width() > viewportSize.width();

    if (bothScrollBarsAuto && !horizontalWantsToShow) {
        // break the infinite loop described above by setting the range to 0, 0.
        // QAbstractScrollArea will then hide the scroll bar for us
        horizontalScrollBar()->setRange(0, 0);
    } else {
        horizontalScrollBar()->setRange(0, contentsSize.width() - viewport()->width());
    }
}

//  from src/widgets/itemviews/qlistview.cpp, line 2017, as _ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize
inline void QCommonListViewBase::updateVerticalScrollBar(const QSize &step)
{
    verticalScrollBar()->d_func()->itemviewChangeSingleStep(step.height() + spacing());
    verticalScrollBar()->setPageStep(viewport()->height());

    // If both scroll bars are set to auto, we might end up in a situation with enough space
    // for the actual content. But still one of the scroll bars will become enabled due to
    // the other one using the space. The other one will become invisible in the same cycle.
    // -> Infinite loop, QTBUG-39902
    const bool bothScrollBarsAuto = qq->verticalScrollBarPolicy() == Qt::ScrollBarAsNeeded &&
                                    qq->horizontalScrollBarPolicy() == Qt::ScrollBarAsNeeded;

    const QSize viewportSize = QListModeViewBase::viewportSize(qq);

    bool horizontalWantsToShow = contentsSize.width() > viewportSize.width();
    bool verticalWantsToShow;
    if (horizontalWantsToShow)
        verticalWantsToShow = contentsSize.height() > viewportSize.height() - qq->horizontalScrollBar()->height();
    else
        verticalWantsToShow = contentsSize.height() > viewportSize.height();

    if (bothScrollBarsAuto && !verticalWantsToShow) {
        // break the infinite loop described above by setting the range to 0, 0.
        // QAbstractScrollArea will then hide the scroll bar for us
        verticalScrollBar()->setRange(0, 0);
    } else {
        verticalScrollBar()->setRange(0, contentsSize.height() - viewport()->height());
    }
}

//  from src/widgets/itemviews/qlistview.cpp, line 1963, as _ZN19QCommonListViewBase15appendHiddenRowEi
inline void QCommonListViewBase::appendHiddenRow(int row)
{
    dd->hiddenRows.insert(dd->model->index(row, 0, qq->rootIndex()));
}

//  from src/widgets/itemviews/qlistview.cpp, line 1968, as _ZN19QCommonListViewBase15removeHiddenRowEi
inline void QCommonListViewBase::removeHiddenRow(int row)
{
    dd->hiddenRows.remove(dd->model->index(row, 0, qq->rootIndex()));
}

//  from src/widgets/itemviews/qlistview.cpp, line 1974, as _ZN19QCommonListViewBase13paintDragDropEP8QPainter
#if QT_CONFIG(draganddrop)
inline void QCommonListViewBase::paintDragDrop(QPainter *painter)
{
    // FIXME: Until the we can provide a proper drop indicator
    // in IconMode, it makes no sense to show it
    dd->paintDropIndicator(painter);
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qbsptree.cpp, line 67, as _ZN8QBspTree4initERK5QRectiNS_4Node4TypeEi
inline void QBspTree::init(const QRect &area, int depth, NodeType type, int index)
{
    Node::Type t = Node::None; // t should never have this value
    if (type == Node::Both) // if both planes are specified, use 2d bsp
        t = (depth & 1) ? Node::HorizontalPlane : Node::VerticalPlane;
    else
        t = type;
    QPoint center = area.center();
    nodes[index].pos = (t == Node::VerticalPlane ? center.x() : center.y());
    nodes[index].type = t;

    QRect front = area;
    QRect back = area;

    if (t == Node::VerticalPlane) {
        front.setLeft(center.x());
        back.setRight(center.x() - 1); // front includes the center
    } else { // t == Node::HorizontalPlane
        front.setTop(center.y());
        back.setBottom(center.y() - 1);
    }

    int idx = firstChildIndex(index);
    if (--depth) {
        init(back, depth, type, idx);
        init(front, depth, type, idx + 1);
    }
}

//  from src/widgets/itemviews/qbsptree.cpp, line 96, as _ZN8QBspTree6insertER5QListIiERK5QRectjNS_4DataE
inline void QBspTree::insert(QList<int> &leaf, const QRect &, uint, QBspTreeData data)
{
    leaf.append(data.i);
}

//  from src/widgets/itemviews/qbsptree.cpp, line 42, as _ZN8QBspTree9climbTreeERK5QRectPFvR5QListIiES2_jNS_4DataEES6_i
inline void QBspTree::climbTree(const QRect &area, callback *function, QBspTreeData data, int index)
{
    if (index >= nodes.size()) { // the index points to a leaf
        Q_ASSERT(!nodes.isEmpty());
        function(leaf(index - nodes.size()), area, visited, data);
        return;
    }

    Node::Type t = (Node::Type) nodes.at(index).type;

    int pos = nodes.at(index).pos;
    int idx = firstChildIndex(index);
    if (t == Node::VerticalPlane) {
        if (area.left() < pos)
            climbTree(area, function, data, idx); // back
        if (area.right() >= pos)
            climbTree(area, function, data, idx + 1); // front
    } else {
        if (area.top() < pos)
            climbTree(area, function, data, idx); // back
        if (area.bottom() >= pos)
            climbTree(area, function, data, idx + 1); // front
    }
}

//  from src/widgets/itemviews/qbsptree.cpp, line 101, as _ZN8QBspTree6removeER5QListIiERK5QRectjNS_4DataE
inline void QBspTree::remove(QList<int> &leaf, const QRect &, uint, QBspTreeData data)
{
    int i = leaf.indexOf(data.i);
    if (i != -1)
        leaf.remove(i);
}

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

//  from src/widgets/itemviews/qlistview.cpp, line 1982, as _ZN17QListModeViewBase12viewportSizeEPK17QAbstractItemView
inline QSize QListModeViewBase::viewportSize(const QAbstractItemView *v)
{
    return v->contentsRect().marginsRemoved(v->viewportMargins()).size();
}

//  from src/widgets/widgets/qabstractslider.cpp, line 816, as _ZN22QAbstractSliderPrivate24itemviewChangeSingleStepEi
inline void QAbstractSliderPrivate::itemviewChangeSingleStep(int step)
{
    singleStepFromItemView = step;
    if (viewMayChangeSingleStep && singleStep != step)
        setSteps(step, pageStep);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4552, as _ZN24QAbstractItemViewPrivate13clearOrRemoveEv
inline void QAbstractItemViewPrivate::clearOrRemove()
{
#if QT_CONFIG(draganddrop)
    const QItemSelection selection = selectionModel->selection();
    QList<QItemSelectionRange>::const_iterator it = selection.constBegin();

    if (!overwrite) {
        for (; it != selection.constEnd(); ++it) {
            QModelIndex parent = (*it).parent();
            if ((*it).left() != 0)
                continue;
            if ((*it).right() != (model->columnCount(parent) - 1))
                continue;
            int count = (*it).bottom() - (*it).top() + 1;
            model->removeRows((*it).top(), count, parent);
        }
    } else {
        // we can't remove the rows so reset the items (i.e. the view is like a table)
        QModelIndexList list = selection.indexes();
        for (int i=0; i < list.size(); ++i) {
            QModelIndex index = list.at(i);
            QMap<int, QVariant> roles = model->itemData(index);
            for (QMap<int, QVariant>::Iterator it = roles.begin(); it != roles.end(); ++it)
                it.value() = QVariant();
            model->setItemData(index, roles);
        }
    }
#endif
}

//  from src/widgets/itemviews/qbsptree.cpp, line 11, as _ZN8QBspTree6createEii
inline void QBspTree::create(int n, int d)
{
    // simple heuristics to find the best tree depth
    if (d == -1) {
        int c;
        for (c = 0; n; ++c)
            n = n / 10;
        depth = c << 1;
    } else {
        depth = d;
    }
    depth = qMax(depth, uint(1));

    nodes.resize((1ll << depth) - 1); // resize to number of nodes
    leaves.resize(1ll << depth); // resize to number of leaves
}

//  from src/widgets/itemviews/qbsptree.cpp, line 28, as _ZN8QBspTree7destroyEv
inline void QBspTree::destroy()
{
    leaves.clear();
    nodes.clear();
}

//  from src/widgets/itemviews/qbsptree.cpp, line 34, as _ZN8QBspTree9climbTreeERK5QRectPFvR5QListIiES2_jNS_4DataEES6_
inline void QBspTree::climbTree(const QRect &rect, callback *function, QBspTreeData data)
{
    if (nodes.isEmpty())
        return;
    ++visited;
    climbTree(rect, function, data, 0);
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

//  from src/widgets/itemviews/qlistview.cpp, line 1822, as _ZNK16QListViewPrivate19indexToListViewItemERK11QModelIndex
inline QListViewItem QListViewPrivate::indexToListViewItem(const QModelIndex &index) const
{
    if (!index.isValid() || isHidden(index.row()))
        return QListViewItem();

    return commonListView->indexToListViewItem(index);
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4719, as _ZNK24QAbstractItemViewPrivate14renderToPixmapERK5QListI11QModelIndexEP5QRect
inline QPixmap QAbstractItemViewPrivate::renderToPixmap(const QModelIndexList &indexes, QRect *r) const
{
    Q_Q(const QAbstractItemView);
    Q_ASSERT(r);
    QItemViewPaintPairs paintPairs = draggablePaintPairs(indexes, r);
    if (paintPairs.isEmpty())
        return QPixmap();

    QWindow *window = windowHandle(WindowHandleMode::Closest);
    const qreal scale = window ? window->devicePixelRatio() : qreal(1);

    QPixmap pixmap(r->size() * scale);
    pixmap.setDevicePixelRatio(scale);

    pixmap.fill(Qt::transparent);
    QPainter painter(&pixmap);
    painter.setLayoutDirection(q->layoutDirection());
    QStyleOptionViewItem option;
    q->initViewItemOption(&option);
    option.state |= QStyle::State_Selected;
    for (int j = 0; j < paintPairs.size(); ++j) {
        option.rect = paintPairs.at(j).rect.translated(-r->topLeft());
        const QModelIndex &current = paintPairs.at(j).index;
        adjustViewOptionsForIndex(&option, current);
        q->itemDelegateForIndex(current)->paint(&painter, option, current);
    }
    return pixmap;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4433, as _ZNK24QAbstractItemViewPrivate16shouldAutoScrollERK6QPoint
inline bool QAbstractItemViewPrivate::shouldAutoScroll(const QPoint &pos) const
{
    if (!autoScroll)
        return false;
    const QRect area = QWidgetPrivate::get(viewport)->clipRect();
    return (pos.y() - area.top() < autoScrollMargin)
        || (area.bottom() - pos.y() < autoScrollMargin)
        || (pos.x() - area.left() < autoScrollMargin)
        || (area.right() - pos.x() < autoScrollMargin);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4452, as _ZNK24QAbstractItemViewPrivate27interruptDelayedItemsLayoutEv
inline void QAbstractItemViewPrivate::interruptDelayedItemsLayout() const
{
    delayedLayout.stop();
    delayedPendingLayout = false;
}

//  from src/widgets/widgets/qabstractslider.cpp, line 215, as _ZN22QAbstractSliderPrivate8setStepsEii
inline void QAbstractSliderPrivate::setSteps(int single, int page)
{
    Q_Q(QAbstractSlider);
    singleStep = qAbs(single);
    pageStep = qAbs(page);
    q->sliderChange(QAbstractSlider::SliderStepsChange);
}

//  from src/widgets/itemviews/qlistview.cpp, line 3057, as _ZN17QIconModeViewBase11initBspTreeERK5QSize
inline void QIconModeViewBase::initBspTree(const QSize &contents)
{
    // remove all items from the tree
    int leafCount = tree.leafCount();
    for (int l = 0; l < leafCount; ++l)
        tree.leaf(l).clear();
    // we have to get the bounding rect of the items before we can initialize the tree
    QBspTree::Node::Type type = QBspTree::Node::Both; // 2D
    // simple heuristics to get better bsp
    if (contents.height() / contents.width() >= 3)
        type = QBspTree::Node::HorizontalPlane;
    else if (contents.width() / contents.height() >= 3)
        type = QBspTree::Node::VerticalPlane;
    // build tree for the bounding rect (not just the contents rect)
    tree.init(QRect(0, 0, contents.width(), contents.height()), type);
}

//  from src/widgets/itemviews/qlistview.cpp, line 3074, as _ZN17QIconModeViewBase17initDynamicLayoutERK19QListViewLayoutInfo
inline QPoint QIconModeViewBase::initDynamicLayout(const QListViewLayoutInfo &info)
{
    int x, y;
    if (info.first == 0) {
        x = info.bounds.x() + info.spacing;
        y = info.bounds.y() + info.spacing;
        items.reserve(rowCount() - hiddenCount());
    } else {
        int idx = info.first - 1;
        while (idx > 0 && !items.at(idx).isValid())
            --idx;
        const QListViewItem &item = items.at(idx);
        x = item.x;
        y = item.y;
        if (info.flow == QListView::LeftToRight)
            x += (info.grid.isValid() ? info.grid.width() : item.w) + info.spacing;
        else
            y += (info.grid.isValid() ? info.grid.height() : item.h) + info.spacing;
    }
    return QPoint(x, y);
}

//  from src/widgets/itemviews/qlistview.cpp, line 3099, as _ZN17QIconModeViewBase15doDynamicLayoutERK19QListViewLayoutInfo
inline void QIconModeViewBase::doDynamicLayout(const QListViewLayoutInfo &info)
{
    const bool useItemSize = !info.grid.isValid();
    const QPoint topLeft = initDynamicLayout(info);

    int segStartPosition;
    int segEndPosition;
    int deltaFlowPosition;
    int deltaSegPosition;
    int deltaSegHint;
    int flowPosition;
    int segPosition;

    if (info.flow == QListView::LeftToRight) {
        segStartPosition = info.bounds.left() + info.spacing;
        segEndPosition = info.bounds.right();
        deltaFlowPosition = info.grid.width(); // dx
        deltaSegPosition = (useItemSize ? batchSavedDeltaSeg : info.grid.height()); // dy
        deltaSegHint = info.grid.height();
        flowPosition = topLeft.x();
        segPosition = topLeft.y();
    } else { // flow == QListView::TopToBottom
        segStartPosition = info.bounds.top() + info.spacing;
        segEndPosition = info.bounds.bottom();
        deltaFlowPosition = info.grid.height(); // dy
        deltaSegPosition = (useItemSize ? batchSavedDeltaSeg : info.grid.width()); // dx
        deltaSegHint = info.grid.width();
        flowPosition = topLeft.y();
        segPosition = topLeft.x();
    }

    if (moved.size() != items.size())
        moved.resize(items.size());

    QRect rect(QPoint(), topLeft);
    QListViewItem *item = nullptr;
    Q_ASSERT(info.first <= info.last);
    for (int row = info.first; row <= info.last; ++row) {
        item = &items[row];
        if (isHidden(row)) {
            item->invalidate();
        } else {
            // if we are not using a grid, we need to find the deltas
            if (useItemSize) {
                if (info.flow == QListView::LeftToRight)
                    deltaFlowPosition = item->w + info.spacing;
                else
                    deltaFlowPosition = item->h + info.spacing;
            } else {
                item->w = qMin<int>(info.grid.width(), item->w);
                item->h = qMin<int>(info.grid.height(), item->h);
            }

            // create new segment
            if (info.wrap
                && flowPosition + deltaFlowPosition > segEndPosition
                && flowPosition > segStartPosition) {
                flowPosition = segStartPosition;
                segPosition += deltaSegPosition;
                if (useItemSize)
                    deltaSegPosition = 0;
            }
            // We must delay calculation of the seg adjustment, as this item
            // may have caused a wrap to occur
            if (useItemSize) {
                if (info.flow == QListView::LeftToRight)
                    deltaSegHint = item->h + info.spacing;
                else
                    deltaSegHint = item->w + info.spacing;
                deltaSegPosition = qMax(deltaSegPosition, deltaSegHint);
            }

            // set the position of the item
            // ### idealy we should have some sort of alignment hint for the item
            // ### (normally that would be a point between the icon and the text)
            if (!moved.testBit(row)) {
                if (info.flow == QListView::LeftToRight) {
                    if (useItemSize) {
                        item->x = flowPosition;
                        item->y = segPosition;
                    } else { // use grid
                        item->x = flowPosition + ((deltaFlowPosition - item->w) / 2);
                        item->y = segPosition;
                    }
                } else { // TopToBottom
                    if (useItemSize) {
                        item->y = flowPosition;
                        item->x = segPosition;
                    } else { // use grid
                        item->y = flowPosition + ((deltaFlowPosition - item->h) / 2);
                        item->x = segPosition;
                    }
                }
            }

            // let the contents contain the new item
            if (useItemSize)
                rect |= item->rect();
            else if (info.flow == QListView::LeftToRight)
                rect |= QRect(flowPosition, segPosition, deltaFlowPosition, deltaSegPosition);
            else // flow == TopToBottom
                rect |= QRect(segPosition, flowPosition, deltaSegPosition, deltaFlowPosition);

            // prepare for next item
            flowPosition += deltaFlowPosition; // current position + item width + gap
        }
    }
    Q_ASSERT(item);
    batchSavedDeltaSeg = deltaSegPosition;
    batchStartRow = info.last + 1;
    bool done = (info.last >= rowCount() - 1);
    // resize the content area
    if (done || !info.bounds.contains(item->rect())) {
        contentsSize = rect.size();
        if (info.flow == QListView::LeftToRight)
            contentsSize.rheight() += info.spacing;
        else
            contentsSize.rwidth() += info.spacing;
    }
    if (rect.size().isEmpty())
        return;
    // resize tree
    int insertFrom = info.first;
    if (done || info.first == 0) {
        initBspTree(rect.size());
        insertFrom = 0;
    }
    // insert items in tree
    for (int row = insertFrom; row <= info.last; ++row)
        tree.insertLeaf(items.at(row).rect(), row);
    // if the new items are visible, update the viewport
    QRect changedRect(topLeft, rect.bottomRight());
    if (clipRect().intersects(changedRect))
        viewport()->update();
}

//  from src/widgets/itemviews/qlistview.cpp, line 3290, as _ZN17QIconModeViewBase7addLeafER5QListIiERK5QRectjN8QBspTree4DataE
inline void QIconModeViewBase::addLeaf(QList<int> &leaf, const QRect &area, uint visited,
                                QBspTree::Data data)
{
    QListViewItem *vi;
    QIconModeViewBase *_this = static_cast<QIconModeViewBase *>(data.ptr);
    for (int i = 0; i < leaf.size(); ++i) {
        int idx = leaf.at(i);
        if (idx < 0 || idx >= _this->items.size())
            continue;
        vi = &_this->items[idx];
        Q_ASSERT(vi);
        if (vi->isValid() && vi->rect().intersects(area) && vi->visited != visited) {
            QModelIndex index  = _this->dd->listViewItemToIndex(*vi);
            Q_ASSERT(index.isValid());
            _this->interSectingVector->append(index);
            vi->visited = visited;
        }
    }
}

//  from src/widgets/itemviews/qlistview.cpp, line 3246, as _ZNK17QIconModeViewBase9itemsRectERK5QListI11QModelIndexE
inline QRect QIconModeViewBase::itemsRect(const QList<QModelIndex> &indexes) const
{
    QRect rect;
    for (const auto &index : indexes)
        rect |= viewItemRect(indexToListViewItem(index));
    return rect;
}

//  from src/widgets/itemviews/qlistview.cpp, line 3347, as _ZNK17QIconModeViewBase16draggedItemsRectEv
inline QRect QIconModeViewBase::draggedItemsRect() const
{
    QRect rect = itemsRect(draggedItems);
    rect.translate(draggedItemsDelta());
    return rect;
}

//  from src/widgets/itemviews/qlistview.cpp, line 3330, as _ZNK17QIconModeViewBase10snapToGridERK6QPoint
inline QPoint QIconModeViewBase::snapToGrid(const QPoint &pos) const
{
    int x = pos.x() - (pos.x() % gridSize().width());
    int y = pos.y() - (pos.y() % gridSize().height());
    return QPoint(x, y);
}

//  from src/widgets/itemviews/qlistview.cpp, line 3375, as _ZN17QIconModeViewBase18updateContentsSizeEv
inline void QIconModeViewBase::updateContentsSize()
{
    QRect bounding;
    for (int i = 0; i < items.size(); ++i)
        bounding |= items.at(i).rect();
    contentsSize = bounding.size();
}

//  from src/widgets/itemviews/qlistview.cpp, line 3337, as _ZNK17QIconModeViewBase17draggedItemsDeltaEv
inline QPoint QIconModeViewBase::draggedItemsDelta() const
{
    if (movement() == QListView::Snap) {
        QPoint snapdelta = QPoint((offset().x() % gridSize().width()),
                                  (offset().y() % gridSize().height()));
        return snapToGrid(draggedItemsPos + snapdelta) - snapToGrid(pressedPosition()) - snapdelta;
    }
    return draggedItemsPos - pressedPosition();
}

//  from src/widgets/itemviews/qlistview.cpp, line 3310, as _ZN17QIconModeViewBase8moveItemEiRK6QPoint
inline void QIconModeViewBase::moveItem(int index, const QPoint &dest)
{
    // does not impact on the bintree itself or the contents rect
    QListViewItem *item = &items[index];
    QRect rect = item->rect();

    // move the item without removing it from the tree
    tree.removeLeaf(rect, index);
    item->move(dest);
    tree.insertLeaf(QRect(dest, rect.size()), index);

    // resize the contents area
    contentsSize = (QRect(QPoint(0, 0), contentsSize)|QRect(dest, rect.size())).size();

    // mark the item as moved
    if (moved.size() != items.size())
        moved.resize(items.size());
    moved.setBit(index, true);
}
//  -----------------------------------------------------------------------

#if QT_CONFIG(draganddrop)
//  QIconModeViewBase::QIconModeViewBase(QListView *q, QListViewPrivate *d)
extern "C" Q_DECL_EXPORT
QIconModeViewBase *ritual_ZN17QIconModeViewBaseC1EP9QListViewP16QListViewPrivate(
    QListView *q,
    QListViewPrivate *d) {
  return new QIconModeViewBase(q, d);
}
#endif  // QT_CONFIG(draganddrop)

//  int QIconModeViewBase::itemIndex(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QIconModeViewBase9itemIndexERK13QListViewItem(
    const QIconModeViewBase *self,
    const QListViewItem *item) {
  return self->itemIndex(*item);
}

//  QListViewItem QIconModeViewBase::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZNK17QIconModeViewBase19indexToListViewItemERK11QModelIndex(
    const QIconModeViewBase *self,
    const QModelIndex *index) {
  return new QListViewItem(self->indexToListViewItem(*index));
}

//  bool QIconModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
//      &info, int max)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi(
    QIconModeViewBase *self,
    const QListViewLayoutInfo *info,
    int max) {
  return self->doBatchedItemLayout(*info, max);
}

//  void QIconModeViewBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase5clearEv(QIconModeViewBase *self) {
  self->clear();
}

//  void QIconModeViewBase::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase11setRowCountEi(
    QIconModeViewBase *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  QList<QModelIndex> QIconModeViewBase::intersectingSet(const QRect &area)
//      const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK17QIconModeViewBase15intersectingSetERK5QRect(
    const QIconModeViewBase *self,
    const QRect *area) {
  return new QList<QModelIndex>(self->intersectingSet(*area));
}

//  void QIconModeViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase16scrollContentsByEiib(
    QIconModeViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->scrollContentsBy(dx, dy, scrollElasticBand);
}

//  void QIconModeViewBase::dataChanged(const QModelIndex &topLeft, const
//      QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase11dataChangedERK11QModelIndexS2_(
    QIconModeViewBase *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->dataChanged(*topLeft, *bottomRight);
}

//  void QIconModeViewBase::appendHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase15appendHiddenRowEi(
    QIconModeViewBase *self,
    int row) {
  self->appendHiddenRow(row);
}

//  void QIconModeViewBase::removeHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase15removeHiddenRowEi(
    QIconModeViewBase *self,
    int row) {
  self->removeHiddenRow(row);
}

//  void QIconModeViewBase::setPositionForIndex(const QPoint &position, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase19setPositionForIndexERK6QPointRK11QModelIndex(
    QIconModeViewBase *self,
    const QPoint *position,
    const QModelIndex *index) {
  self->setPositionForIndex(*position, *index);
}

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconModeViewBase19filterDragMoveEventEP14QDragMoveEvent(
    QIconModeViewBase *self,
    QDragMoveEvent *a0) {
  return self->filterDragMoveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconModeViewBase20filterDragLeaveEventEP15QDragLeaveEvent(
    QIconModeViewBase *self,
    QDragLeaveEvent *a0) {
  return self->filterDragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconModeViewBase15filterDropEventEP10QDropEvent(
    QIconModeViewBase *self,
    QDropEvent *e) {
  return self->filterDropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterStartDrag(Qt::DropActions a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QIconModeViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE(
    QIconModeViewBase *self,
    int a0) {
  return self->filterStartDrag(QFlags<Qt::DropAction>::fromInt(a0));
}
#endif  // QT_CONFIG(draganddrop)

//  void QIconModeViewBase::initBspTree(const QSize &contents)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase11initBspTreeERK5QSize(
    QIconModeViewBase *self,
    const QSize *contents) {
  self->initBspTree(*contents);
}

//  QPoint QIconModeViewBase::initDynamicLayout(const QListViewLayoutInfo
//      &info)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN17QIconModeViewBase17initDynamicLayoutERK19QListViewLayoutInfo(
    QIconModeViewBase *self,
    const QListViewLayoutInfo *info) {
  return new QPoint(self->initDynamicLayout(*info));
}

//  void QIconModeViewBase::doDynamicLayout(const QListViewLayoutInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase15doDynamicLayoutERK19QListViewLayoutInfo(
    QIconModeViewBase *self,
    const QListViewLayoutInfo *info) {
  self->doDynamicLayout(*info);
}

//  void QIconModeViewBase::addLeaf(QList<int> &leaf, const QRect &area, uint
//      visited, QBspTree::Data data)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase7addLeafER5QListIiERK5QRectjN8QBspTree4DataE(
    QList<int> *leaf,
    const QRect *area,
    uint visited,
    const QBspTree::Data *data) {
  QIconModeViewBase::addLeaf(*leaf, *area, visited, *data);
}

//  QRect QIconModeViewBase::itemsRect(const QList<QModelIndex> &indexes)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QIconModeViewBase9itemsRectERK5QListI11QModelIndexE(
    const QIconModeViewBase *self,
    const QList<QModelIndex> *indexes) {
  return new QRect(self->itemsRect(*indexes));
}

//  QRect QIconModeViewBase::draggedItemsRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QIconModeViewBase16draggedItemsRectEv(
    const QIconModeViewBase *self) {
  return new QRect(self->draggedItemsRect());
}

//  QPoint QIconModeViewBase::snapToGrid(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QIconModeViewBase10snapToGridERK6QPoint(
    const QIconModeViewBase *self,
    const QPoint *pos) {
  return new QPoint(self->snapToGrid(*pos));
}

//  void QIconModeViewBase::updateContentsSize()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase18updateContentsSizeEv(
    QIconModeViewBase *self) {
  self->updateContentsSize();
}

//  QPoint QIconModeViewBase::draggedItemsDelta() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK17QIconModeViewBase17draggedItemsDeltaEv(
    const QIconModeViewBase *self) {
  return new QPoint(self->draggedItemsDelta());
}

//  void QIconModeViewBase::moveItem(int index, const QPoint &dest)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBase8moveItemEiRK6QPoint(
    QIconModeViewBase *self,
    int index,
    const QPoint *dest) {
  self->moveItem(index, *dest);
}

//  QIconModeViewBase::~QIconModeViewBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QIconModeViewBaseD1Ev(QIconModeViewBase *self) {
  delete self;
}

//  int QIconModeViewBase::itemIndex(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QIconModeViewBase9itemIndexERK13QListViewItem(
    const QIconModeViewBase *self,
    const QListViewItem *item) {
  return self->QIconModeViewBase::itemIndex(*item);
}

//  QListViewItem QIconModeViewBase::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_own_ZNK17QIconModeViewBase19indexToListViewItemERK11QModelIndex(
    const QIconModeViewBase *self,
    const QModelIndex *index) {
  return new QListViewItem(
      self->QIconModeViewBase::indexToListViewItem(
          *index));
}

//  bool QIconModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
//      &info, int max)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi(
    QIconModeViewBase *self,
    const QListViewLayoutInfo *info,
    int max) {
  return self->QIconModeViewBase::doBatchedItemLayout(*info, max);
}

//  void QIconModeViewBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase5clearEv(QIconModeViewBase *self) {
  self->QIconModeViewBase::clear();
}

//  void QIconModeViewBase::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase11setRowCountEi(
    QIconModeViewBase *self,
    int rowCount) {
  self->QIconModeViewBase::setRowCount(rowCount);
}

//  void QIconModeViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase16scrollContentsByEiib(
    QIconModeViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->QIconModeViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
}

//  void QIconModeViewBase::dataChanged(const QModelIndex &topLeft, const
//      QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase11dataChangedERK11QModelIndexS2_(
    QIconModeViewBase *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->QIconModeViewBase::dataChanged(*topLeft, *bottomRight);
}

//  void QIconModeViewBase::appendHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase15appendHiddenRowEi(
    QIconModeViewBase *self,
    int row) {
  self->QIconModeViewBase::appendHiddenRow(row);
}

//  void QIconModeViewBase::removeHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase15removeHiddenRowEi(
    QIconModeViewBase *self,
    int row) {
  self->QIconModeViewBase::removeHiddenRow(row);
}

//  void QIconModeViewBase::setPositionForIndex(const QPoint &position, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QIconModeViewBase19setPositionForIndexERK6QPointRK11QModelIndex(
    QIconModeViewBase *self,
    const QPoint *position,
    const QModelIndex *index) {
  self->QIconModeViewBase::setPositionForIndex(*position, *index);
}

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconModeViewBase19filterDragMoveEventEP14QDragMoveEvent(
    QIconModeViewBase *self,
    QDragMoveEvent *a0) {
  return self->QIconModeViewBase::filterDragMoveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconModeViewBase20filterDragLeaveEventEP15QDragLeaveEvent(
    QIconModeViewBase *self,
    QDragLeaveEvent *a0) {
  return self->QIconModeViewBase::filterDragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterDropEvent(QDropEvent *e)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconModeViewBase15filterDropEventEP10QDropEvent(
    QIconModeViewBase *self,
    QDropEvent *e) {
  return self->QIconModeViewBase::filterDropEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QIconModeViewBase::filterStartDrag(Qt::DropActions a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QIconModeViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE(
    QIconModeViewBase *self,
    int a0) {
  return self->QIconModeViewBase::filterStartDrag(
      QFlags<Qt::DropAction>::fromInt(a0));
}
#endif  // QT_CONFIG(draganddrop)

#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(listview)
