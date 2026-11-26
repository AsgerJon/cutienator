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
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>
#include <QtCore/qlist.h>
#include <QtWidgets/QListView>
#include <QtCore/QRect>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It stays under the license
//  of each file it comes from, as its own SPDX line has it:
//    LicenseRef-Qt-Commercial OR LGPL-3.0-only OR GPL-2.0-only OR
//      GPL-3.0-only
//  Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/widgets/itemviews/qlistview.cpp, line 2451, as _ZNK17QListModeViewBase19indexToListViewItemERK11QModelIndex
inline QListViewItem QListModeViewBase::indexToListViewItem(const QModelIndex &index) const
{
    if (flowPositions.isEmpty()
        || segmentPositions.isEmpty()
        || index.row() >= flowPositions.size() - 1)
        return QListViewItem();

    const int segment = qBinarySearch<int>(segmentStartRows, index.row(),
                                           0, segmentStartRows.size() - 1);


    QStyleOptionViewItem options;
    initViewItemOption(&options);
    options.rect.setSize(contentsSize);
    QSize size = (uniformItemSizes() && cachedItemSize().isValid())
                 ? cachedItemSize() : itemSize(options, index);
    QSize cellSize = size;

    QPoint pos;
    if (flow() == QListView::LeftToRight) {
        pos.setX(flowPositions.at(index.row()));
        pos.setY(segmentPositions.at(segment));
    } else { // TopToBottom
        pos.setY(flowPositions.at(index.row()));
        pos.setX(segmentPositions.at(segment));
        if (isWrapping()) { // make the items as wide as the segment
            int right = (segment + 1 >= segmentPositions.size()
                     ? contentsSize.width()
                     : segmentPositions.at(segment + 1));
            cellSize.setWidth(right - pos.x());
        } else { // make the items as wide as the viewport
            cellSize.setWidth(qMax(size.width(), viewport()->width() - 2 * spacing()));
        }
    }

    if (dd->itemAlignment & Qt::AlignHorizontal_Mask) {
        size.setWidth(qMin(size.width(), cellSize.width()));
        if (dd->itemAlignment & Qt::AlignRight)
            pos.setX(pos.x() + cellSize.width() - size.width());
        if (dd->itemAlignment & Qt::AlignHCenter)
            pos.setX(pos.x() + (cellSize.width() - size.width()) / 2);
    } else {
        size.setWidth(cellSize.width());
    }

    return QListViewItem(QRect(pos, size), index.row());
}

//  from src/widgets/itemviews/qlistview.cpp, line 2445, as _ZN17QListModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi
inline bool QListModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo &info, int max)
{
    doStaticLayout(info);
    return batchStartRow > max; // returning true stops items layout
}

//  from src/widgets/itemviews/qlistview.cpp, line 2826, as _ZN17QListModeViewBase5clearEv
inline void QListModeViewBase::clear()
{
    flowPositions.clear();
    segmentPositions.clear();
    segmentStartRows.clear();
    segmentExtents.clear();
    batchSavedPosition = 0;
    batchStartRow = 0;
    batchSavedDeltaSeg = 0;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2642, as _ZNK17QListModeViewBase15intersectingSetERK5QRect
inline QList<QModelIndex> QListModeViewBase::intersectingSet(const QRect &area) const
{
    QList<QModelIndex> ret;
    int segStartPosition;
    int segEndPosition;
    int flowStartPosition;
    int flowEndPosition;
    if (flow() == QListView::LeftToRight) {
        segStartPosition = area.top();
        segEndPosition = area.bottom();
        flowStartPosition = area.left();
        flowEndPosition = area.right();
    } else {
        segStartPosition = area.left();
        segEndPosition = area.right();
        flowStartPosition = area.top();
        flowEndPosition = area.bottom();
    }
    if (segmentPositions.size() < 2 || flowPositions.isEmpty())
        return ret;
    // the last segment position is actually the edge of the last segment
    const int segLast = segmentPositions.size() - 2;
    int seg = qBinarySearch<int>(segmentPositions, segStartPosition, 0, segLast + 1);
    for (; seg <= segLast && segmentPositions.at(seg) <= segEndPosition; ++seg) {
        int first = segmentStartRows.at(seg);
        int last = (seg < segLast ? segmentStartRows.at(seg + 1) : batchStartRow) - 1;
        if (segmentExtents.at(seg) < flowStartPosition)
            continue;
        int row = qBinarySearch<int>(flowPositions, flowStartPosition, first, last);
        for (; row <= last && flowPositions.at(row) <= flowEndPosition; ++row) {
            if (isHidden(row))
                continue;
            QModelIndex index = modelIndex(row);
            if (index.isValid()) {
                if (flow() == QListView::LeftToRight || dd->itemAlignment == Qt::Alignment()) {
                    ret += index;
                } else {
                    const auto viewItem = indexToListViewItem(index);
                    const int iw = viewItem.width();
                    const int startPos = qMax(segStartPosition, segmentPositions.at(seg));
                    const int endPos = qMin(segmentPositions.at(seg + 1), segEndPosition);
                    if (endPos >= viewItem.x && startPos < viewItem.x + iw)
                        ret += index;
                }
            }
#if 0 // for debugging
            else
                qWarning("intersectingSet: row %d was invalid", row);
#endif
        }
    }
    return ret;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2696, as _ZN17QListModeViewBase11dataChangedERK11QModelIndexS2_
inline void QListModeViewBase::dataChanged(const QModelIndex &, const QModelIndex &)
{
    dd->doDelayedItemsLayout();
}

//  from src/widgets/itemviews/qlistview.cpp, line 2378, as _ZNK17QListModeViewBase23horizontalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_
inline int QListModeViewBase::horizontalScrollToValue(int index, QListView::ScrollHint hint,
                                            bool leftOf, bool rightOf, const QRect &area, const QRect &rect) const
{
    if (horizontalScrollMode() != QAbstractItemView::ScrollPerItem)
        return QCommonListViewBase::horizontalScrollToValue(index, hint, leftOf, rightOf, area, rect);

    int value;
    if (scrollValueMap.isEmpty())
        value = 0;
    else
        value = qBound(0, scrollValueMap.at(horizontalScrollBar()->value()), flowPositions.size() - 1);
    if (leftOf)
        hint = QListView::PositionAtTop;
    else if (rightOf)
        hint = QListView::PositionAtBottom;
    if (hint == QListView::EnsureVisible)
        return value;

    return perItemScrollToValue(index, value, area.width(), hint, Qt::Horizontal, isWrapping(), rect.width());
}

//  from src/widgets/itemviews/qlistview.cpp, line 2309, as _ZNK17QListModeViewBase21verticalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_
inline int QListModeViewBase::verticalScrollToValue(int index, QListView::ScrollHint hint,
                                          bool above, bool below, const QRect &area, const QRect &rect) const
{
    if (verticalScrollMode() == QAbstractItemView::ScrollPerItem) {
        int value;
        if (scrollValueMap.isEmpty()) {
            value = 0;
        } else {
            int scrollBarValue = verticalScrollBar()->value();
            int numHidden = 0;
            for (const auto &idx : std::as_const(dd->hiddenRows))
                if (idx.row() <= scrollBarValue)
                    ++numHidden;
            value = qBound(0, scrollValueMap.at(verticalScrollBar()->value()) - numHidden, flowPositions.size() - 1);
        }
        if (above)
            hint = QListView::PositionAtTop;
        else if (below)
            hint = QListView::PositionAtBottom;
        if (hint == QListView::EnsureVisible)
            return value;

        return perItemScrollToValue(index, value, area.height(), hint, Qt::Vertical, isWrapping(), rect.height());
    }

    return QCommonListViewBase::verticalScrollToValue(index, hint, above, below, area, rect);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2399, as _ZN17QListModeViewBase16scrollContentsByEiib
inline void QListModeViewBase::scrollContentsBy(int dx, int dy, bool scrollElasticBand)
{
    // ### reorder this logic
    const int verticalValue = verticalScrollBar()->value();
    const int horizontalValue = horizontalScrollBar()->value();
    const bool vertical = (verticalScrollMode() == QAbstractItemView::ScrollPerItem);
    const bool horizontal = (horizontalScrollMode() == QAbstractItemView::ScrollPerItem);

    if (isWrapping()) {
        if (segmentPositions.isEmpty())
            return;
        const int max = segmentPositions.size() - 1;
        if (horizontal && flow() == QListView::TopToBottom && dx != 0) {
            int currentValue = qBound(0, horizontalValue, max);
            int previousValue = qBound(0, currentValue + dx, max);
            int currentCoordinate = segmentPositions.at(currentValue) - spacing();
            int previousCoordinate = segmentPositions.at(previousValue) - spacing();
            dx = previousCoordinate - currentCoordinate;
        } else if (vertical && flow() == QListView::LeftToRight && dy != 0) {
            int currentValue = qBound(0, verticalValue, max);
            int previousValue = qBound(0, currentValue + dy, max);
            int currentCoordinate = segmentPositions.at(currentValue) - spacing();
            int previousCoordinate = segmentPositions.at(previousValue) - spacing();
            dy = previousCoordinate - currentCoordinate;
        }
    } else {
        if (flowPositions.isEmpty())
            return;
        const int max = scrollValueMap.size() - 1;
        if (vertical && flow() == QListView::TopToBottom && dy != 0) {
            int currentValue = qBound(0, verticalValue, max);
            int previousValue = qBound(0, currentValue + dy, max);
            int currentCoordinate = flowPositions.at(scrollValueMap.at(currentValue));
            int previousCoordinate = flowPositions.at(scrollValueMap.at(previousValue));
            dy = previousCoordinate - currentCoordinate;
        } else if (horizontal && flow() == QListView::LeftToRight && dx != 0) {
            int currentValue = qBound(0, horizontalValue, max);
            int previousValue = qBound(0, currentValue + dx, max);
            int currentCoordinate = flowPositions.at(scrollValueMap.at(currentValue));
            int previousCoordinate = flowPositions.at(scrollValueMap.at(previousValue));
            dx = previousCoordinate - currentCoordinate;
        }
    }
    QCommonListViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2702, as _ZNK17QListModeViewBase13mapToViewportERK5QRect
inline QRect QListModeViewBase::mapToViewport(const QRect &rect) const
{
    if (isWrapping())
        return rect;
    // If the listview is in "listbox-mode", the items are as wide as the view.
    // But we don't shrink the items.
    QRect result = rect;
    if (flow() == QListView::TopToBottom) {
        result.setLeft(spacing());
        result.setWidth(qMax(rect.width(), qMax(contentsSize.width(), viewport()->width()) - 2 * spacing()));
    } else { // LeftToRight
        result.setTop(spacing());
        result.setHeight(qMax(rect.height(), qMax(contentsSize.height(), viewport()->height()) - 2 * spacing()));
    }
    return result;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2337, as _ZNK17QListModeViewBase16horizontalOffsetEv
inline int QListModeViewBase::horizontalOffset() const
{
    if (horizontalScrollMode() == QAbstractItemView::ScrollPerItem) {
        if (isWrapping()) {
            if (flow() == QListView::TopToBottom && !segmentPositions.isEmpty()) {
                const int max = segmentPositions.size() - 1;
                int currentValue = qBound(0, horizontalScrollBar()->value(), max);
                int position = segmentPositions.at(currentValue);
                int maximumValue = qBound(0, horizontalScrollBar()->maximum(), max);
                int maximum = segmentPositions.at(maximumValue);
                return (isRightToLeft() ? maximum - position : position);
            }
        } else if (flow() == QListView::LeftToRight && !flowPositions.isEmpty()) {
            int position = flowPositions.at(scrollValueMap.at(horizontalScrollBar()->value()));
            int maximum = flowPositions.at(scrollValueMap.at(horizontalScrollBar()->maximum()));
            return (isRightToLeft() ? maximum - position : position);
        }
    }
    return QCommonListViewBase::horizontalOffset();
}

//  from src/widgets/itemviews/qlistview.cpp, line 2358, as _ZNK17QListModeViewBase14verticalOffsetEv
inline int QListModeViewBase::verticalOffset() const
{
    if (verticalScrollMode() == QAbstractItemView::ScrollPerItem) {
        if (isWrapping()) {
            if (flow() == QListView::LeftToRight && !segmentPositions.isEmpty()) {
                int value = verticalScrollBar()->value();
                if (value >= segmentPositions.size())
                    return 0;
                return segmentPositions.at(value) - spacing();
            }
        } else if (flow() == QListView::TopToBottom && !flowPositions.isEmpty()) {
            int value = verticalScrollBar()->value();
            if (value > scrollValueMap.size())
                return 0;
            return flowPositions.at(scrollValueMap.at(value)) - spacing();
        }
    }
    return QCommonListViewBase::verticalOffset();
}

//  from src/widgets/itemviews/qlistview.cpp, line 2290, as _ZN17QListModeViewBase25updateHorizontalScrollBarERK5QSize
inline void QListModeViewBase::updateHorizontalScrollBar(const QSize &step)
{
    if (horizontalScrollMode() == QAbstractItemView::ScrollPerItem
        && ((flow() == QListView::TopToBottom && isWrapping())
        || (flow() == QListView::LeftToRight && !isWrapping()))) {
            int steps = (flow() == QListView::TopToBottom ? segmentPositions : scrollValueMap).size() - 1;
            if (steps > 0) {
                const int pageSteps = perItemScrollingPageSteps(viewport()->width(), contentsSize.width(), isWrapping());
                horizontalScrollBar()->setSingleStep(1);
                horizontalScrollBar()->setPageStep(pageSteps);
                horizontalScrollBar()->setRange(0, steps - pageSteps);
            } else {
                horizontalScrollBar()->setRange(0, 0);
            }
    } else {
        QCommonListViewBase::updateHorizontalScrollBar(step);
    }
}

//  from src/widgets/itemviews/qlistview.cpp, line 2269, as _ZN17QListModeViewBase23updateVerticalScrollBarERK5QSize
inline void QListModeViewBase::updateVerticalScrollBar(const QSize &step)
{
    if (verticalScrollMode() == QAbstractItemView::ScrollPerItem
        && ((flow() == QListView::TopToBottom && !isWrapping())
        || (flow() == QListView::LeftToRight && isWrapping()))) {
            const int steps = (flow() == QListView::TopToBottom ? scrollValueMap : segmentPositions).size() - 1;
            if (steps > 0) {
                const int pageSteps = perItemScrollingPageSteps(viewport()->height(), contentsSize.height(), isWrapping());
                verticalScrollBar()->setSingleStep(1);
                verticalScrollBar()->setPageStep(pageSteps);
                verticalScrollBar()->setRange(0, steps - pageSteps);
            } else {
                verticalScrollBar()->setRange(0, 0);
            }
            // } else if (vertical && d->isWrapping() && d->movement == Static) {
            // ### wrapped scrolling in flow direction
    } else {
        QCommonListViewBase::updateVerticalScrollBar(step);
    }
}

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

//  from src/widgets/widgets/qabstractslider.cpp, line 816, as _ZN22QAbstractSliderPrivate24itemviewChangeSingleStepEi
inline void QAbstractSliderPrivate::itemviewChangeSingleStep(int step)
{
    singleStepFromItemView = step;
    if (viewMayChangeSingleStep && singleStep != step)
        setSteps(step, pageStep);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4444, as _ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi
inline void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
{
    if (!delayedPendingLayout) {
        delayedPendingLayout = true;
        delayedLayout.start(delay, q_func());
    }
}

//  from src/widgets/widgets/qabstractslider.cpp, line 215, as _ZN22QAbstractSliderPrivate8setStepsEii
inline void QAbstractSliderPrivate::setSteps(int single, int page)
{
    Q_Q(QAbstractSlider);
    singleStep = qAbs(single);
    pageStep = qAbs(page);
    q->sliderChange(QAbstractSlider::SliderStepsChange);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2100, as _ZN17QListModeViewBaseC1EP9QListViewP16QListViewPrivate
inline QListModeViewBase::QListModeViewBase(QListView *q, QListViewPrivate *d)
    : QCommonListViewBase(q, d)
{
#if QT_CONFIG(draganddrop)
    dd->defaultDropAction = Qt::CopyAction;
#endif
}

//  from src/widgets/itemviews/qlistview.cpp, line 1982, as _ZN17QListModeViewBase12viewportSizeEPK17QAbstractItemView
inline QSize QListModeViewBase::viewportSize(const QAbstractItemView *v)
{
    return v->contentsRect().marginsRemoved(v->viewportMargins()).size();
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

//  from src/widgets/itemviews/qlistview.cpp, line 2135, as _ZN17QListModeViewBase13dragMoveEventEP14QDragMoveEvent
#if QT_CONFIG(draganddrop)
inline void QListModeViewBase::dragMoveEvent(QDragMoveEvent *event)
{
    if (qq->dragDropMode() == QAbstractItemView::InternalMove
        && (event->source() != qq || !(event->possibleActions() & Qt::MoveAction)))
        return;

    // ignore by default
    event->ignore();

    // can't use indexAt, doesn't account for spacing.
    QPoint p = event->position().toPoint();
    QRect rect(p.x() + horizontalOffset(), p.y() + verticalOffset(), 1, 1);
    rect.adjust(-dd->spacing(), -dd->spacing(), dd->spacing(), dd->spacing());
    const QList<QModelIndex> intersectVector = dd->intersectingSet(rect);
    QModelIndex index = intersectVector.size() > 0
                        ? intersectVector.last() : QModelIndex();
    dd->hover = index;
    if (!dd->droppingOnItself(event, index)
        && dd->canDrop(event)) {

        if (index.isValid() && dd->showDropIndicator) {
            QRect rect = qq->visualRect(index);
            dd->dropIndicatorPosition = position(event->position().toPoint(), rect, index);
            // if spacing, should try to draw between items, not just next to item.
            switch (dd->dropIndicatorPosition) {
            case QAbstractItemView::AboveItem:
                if (dd->isIndexDropEnabled(index.parent())) {
                    dd->dropIndicatorRect = QRect(rect.left()-dd->spacing(), rect.top(), 0, rect.height());
                    event->accept();
                } else {
                    dd->dropIndicatorRect = QRect();
                }
                break;
            case QAbstractItemView::BelowItem:
                if (dd->isIndexDropEnabled(index.parent())) {
                    dd->dropIndicatorRect = QRect(rect.right()+dd->spacing(), rect.top(), 0, rect.height());
                    event->accept();
                } else {
                    dd->dropIndicatorRect = QRect();
                }
                break;
            case QAbstractItemView::OnItem:
                if (dd->isIndexDropEnabled(index)) {
                    dd->dropIndicatorRect = rect;
                    event->accept();
                } else {
                    dd->dropIndicatorRect = QRect();
                }
                break;
            case QAbstractItemView::OnViewport:
                dd->dropIndicatorRect = QRect();
                if (dd->isIndexDropEnabled(qq->rootIndex())) {
                    event->accept(); // allow dropping in empty areas
                }
                break;
            }
        } else {
            dd->dropIndicatorRect = QRect();
            dd->dropIndicatorPosition = QAbstractItemView::OnViewport;
            if (dd->isIndexDropEnabled(qq->rootIndex())) {
                event->accept(); // allow dropping in empty areas
            }
        }
        dd->viewport->update();
    } // can drop

    if (dd->shouldAutoScroll(event->position().toPoint()))
        qq->startAutoScroll();
}
#endif  // QT_CONFIG(draganddrop)

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

//  from src/widgets/itemviews/qlistview.cpp, line 2499, as _ZN17QListModeViewBase16initStaticLayoutERK19QListViewLayoutInfo
inline QPoint QListModeViewBase::initStaticLayout(const QListViewLayoutInfo &info)
{
    int x, y;
    if (info.first == 0) {
        flowPositions.clear();
        segmentPositions.clear();
        segmentStartRows.clear();
        segmentExtents.clear();
        scrollValueMap.clear();
        x = info.bounds.left() + info.spacing;
        y = info.bounds.top() + info.spacing;
        segmentPositions.append(info.flow == QListView::LeftToRight ? y : x);
        segmentStartRows.append(0);
    } else if (info.wrap) {
        if (info.flow == QListView::LeftToRight) {
            x = batchSavedPosition;
            y = segmentPositions.constLast();
        } else { // flow == QListView::TopToBottom
            x = segmentPositions.constLast();
            y = batchSavedPosition;
        }
    } else { // not first and not wrap
        if (info.flow == QListView::LeftToRight) {
            x = batchSavedPosition;
            y = info.bounds.top() + info.spacing;
        } else { // flow == QListView::TopToBottom
            x = info.bounds.left() + info.spacing;
            y = batchSavedPosition;
        }
    }
    return QPoint(x, y);
}

//  from src/widgets/itemviews/qlistview.cpp, line 2535, as _ZN17QListModeViewBase14doStaticLayoutERK19QListViewLayoutInfo
inline void QListModeViewBase::doStaticLayout(const QListViewLayoutInfo &info)
{
    const bool useItemSize = !info.grid.isValid();
    const QPoint topLeft = initStaticLayout(info);
    QStyleOptionViewItem option;
    initViewItemOption(&option);
    option.rect = info.bounds;
    option.rect.adjust(info.spacing, info.spacing, -info.spacing, -info.spacing);

    // The static layout data structures are as follows:
    // One vector contains the coordinate in the direction of layout flow.
    // Another vector contains the coordinates of the segments.
    // A third vector contains the index (model row) of the first item
    // of each segment.

    int segStartPosition;
    int segEndPosition;
    int deltaFlowPosition;
    int deltaSegPosition;
    int deltaSegHint;
    int flowPosition;
    int segPosition;

    if (info.flow == QListView::LeftToRight) {
        segStartPosition = info.bounds.left();
        segEndPosition = info.bounds.width();
        flowPosition = topLeft.x();
        segPosition = topLeft.y();
        deltaFlowPosition = info.grid.width(); // dx
        deltaSegPosition = useItemSize ? batchSavedDeltaSeg : info.grid.height(); // dy
        deltaSegHint = info.grid.height();
    } else { // flow == QListView::TopToBottom
        segStartPosition = info.bounds.top();
        segEndPosition = info.bounds.height();
        flowPosition = topLeft.y();
        segPosition = topLeft.x();
        deltaFlowPosition = info.grid.height(); // dy
        deltaSegPosition = useItemSize ? batchSavedDeltaSeg : info.grid.width(); // dx
        deltaSegHint = info.grid.width();
    }

    for (int row = info.first; row <= info.last; ++row) {
        if (isHidden(row)) { // ###
            flowPositions.append(flowPosition);
        } else {
            // if we are not using a grid, we need to find the deltas
            if (useItemSize) {
                QSize hint = itemSize(option, modelIndex(row));
                if (info.flow == QListView::LeftToRight) {
                    deltaFlowPosition = hint.width() + info.spacing;
                    deltaSegHint = hint.height() + info.spacing;
                } else { // TopToBottom
                    deltaFlowPosition = hint.height() + info.spacing;
                    deltaSegHint = hint.width() + info.spacing;
                }
            }
            // create new segment
            if (info.wrap && (flowPosition + deltaFlowPosition >= segEndPosition)) {
                segmentExtents.append(flowPosition);
                flowPosition = info.spacing + segStartPosition;
                segPosition += info.spacing + deltaSegPosition;
                segmentPositions.append(segPosition);
                segmentStartRows.append(row);
                deltaSegPosition = 0;
            }
            // save the flow position of this item
            scrollValueMap.append(flowPositions.size());
            flowPositions.append(flowPosition);
            // prepare for the next item
            deltaSegPosition = qMax(deltaSegHint, deltaSegPosition);
            flowPosition += info.spacing + deltaFlowPosition;
        }
    }
    // used when laying out next batch
    batchSavedPosition = flowPosition;
    batchSavedDeltaSeg = deltaSegPosition;
    batchStartRow = info.last + 1;
    if (info.last == info.max)
        flowPosition -= info.spacing; // remove extra spacing
    // set the contents size
    QRect rect = info.bounds;
    if (info.flow == QListView::LeftToRight) {
        rect.setRight(segmentPositions.size() == 1 ? flowPosition : info.bounds.right());
        rect.setBottom(segPosition + deltaSegPosition);
    } else { // TopToBottom
        rect.setRight(segPosition + deltaSegPosition);
        rect.setBottom(segmentPositions.size() == 1 ? flowPosition : info.bounds.bottom());
    }
    contentsSize = QSize(rect.right(), rect.bottom());
    // if it is the last batch, save the end of the segments
    if (info.last == info.max) {
        segmentExtents.append(flowPosition);
        scrollValueMap.append(flowPositions.size());
        flowPositions.append(flowPosition);
        segmentPositions.append(info.wrap ? segPosition + deltaSegPosition : INT_MAX);
    }
    // if the new items are visible, update the viewport
    QRect changedRect(topLeft, rect.bottomRight());
    if (clipRect().intersects(changedRect))
        viewport()->update();
}

//  from src/widgets/itemviews/qlistview.cpp, line 2754, as _ZNK17QListModeViewBase20perItemScrollToValueEiiiN17QAbstractItemView10ScrollHintEN2Qt11OrientationEbi
inline int QListModeViewBase::perItemScrollToValue(int index, int scrollValue, int viewportSize,
                                                 QAbstractItemView::ScrollHint hint,
                                                 Qt::Orientation orientation, bool wrap, int itemExtent) const
{
    if (index < 0)
        return scrollValue;

    itemExtent += spacing();
    QList<int> hiddenRows = dd->hiddenRowIds();
    std::sort(hiddenRows.begin(), hiddenRows.end());
    int hiddenRowsBefore = 0;
    for (int i = 0; i < hiddenRows.size() - 1; ++i)
        if (hiddenRows.at(i) > index + hiddenRowsBefore)
            break;
        else
            ++hiddenRowsBefore;
    if (!wrap) {
        int topIndex = index;
        const int bottomIndex = topIndex;
        const int bottomCoordinate = flowPositions.at(index + hiddenRowsBefore);
        while (topIndex > 0 &&
               (bottomCoordinate - flowPositions.at(topIndex + hiddenRowsBefore - 1) + itemExtent) <= (viewportSize)) {
            topIndex--;
            // will the next one be a hidden row -> skip
            while (hiddenRowsBefore > 0 && hiddenRows.at(hiddenRowsBefore - 1) >= topIndex + hiddenRowsBefore - 1)
                hiddenRowsBefore--;
        }

        const int itemCount = bottomIndex - topIndex + 1;
        switch (hint) {
        case QAbstractItemView::PositionAtTop:
            return index;
        case QAbstractItemView::PositionAtBottom:
            return index - itemCount + 1;
        case QAbstractItemView::PositionAtCenter:
            return index - (itemCount / 2);
        default:
            break;
        }
    } else { // wrapping
        Qt::Orientation flowOrientation = (flow() == QListView::LeftToRight
                                           ? Qt::Horizontal : Qt::Vertical);
        if (flowOrientation == orientation) { // scrolling in the "flow" direction
            // ### wrapped scrolling in the flow direction
            return flowPositions.at(index + hiddenRowsBefore); // ### always pixel based for now
        } else if (!segmentStartRows.isEmpty()) { // we are scrolling in the "segment" direction
            int segment = qBinarySearch<int>(segmentStartRows, index, 0, segmentStartRows.size() - 1);
            int leftSegment = segment;
            const int rightSegment = leftSegment;
            const int bottomCoordinate = segmentPositions.at(segment);

            while (leftSegment > scrollValue &&
                (bottomCoordinate - segmentPositions.at(leftSegment-1) + itemExtent) <= (viewportSize)) {
                    leftSegment--;
            }

            const int segmentCount = rightSegment - leftSegment + 1;
            switch (hint) {
            case QAbstractItemView::PositionAtTop:
                return segment;
            case QAbstractItemView::PositionAtBottom:
                return segment - segmentCount + 1;
            case QAbstractItemView::PositionAtCenter:
                return segment - (segmentCount / 2);
            default:
                break;
            }
        }
    }
    return scrollValue;
}

//  from src/widgets/itemviews/qlistview.cpp, line 2719, as _ZNK17QListModeViewBase25perItemScrollingPageStepsEiib
inline int QListModeViewBase::perItemScrollingPageSteps(int length, int bounds, bool wrap) const
{
    QList<int> positions;
    if (wrap)
        positions = segmentPositions;
    else if (!flowPositions.isEmpty()) {
        positions.reserve(scrollValueMap.size());
        for (int itemShown : scrollValueMap)
            positions.append(flowPositions.at(itemShown));
    }
    if (positions.isEmpty() || bounds <= length)
        return positions.size();
    if (uniformItemSizes()) {
        for (int i = 1; i < positions.size(); ++i)
            if (positions.at(i) > 0)
                return length / positions.at(i);
        return 0; // all items had height 0
    }
    int pageSteps = 0;
    int steps = positions.size() - 1;
    int max = qMax(length, bounds);
    int min = qMin(length, bounds);
    int pos = min - (max - positions.constLast());

    while (pos >= 0 && steps > 0) {
        pos -= (positions.at(steps) - positions.at(steps - 1));
        if (pos >= 0) //this item should be visible
            ++pageSteps;
        --steps;
    }

    // at this point we know that positions has at least one entry
    return qMax(pageSteps, 1);
}
//  -----------------------------------------------------------------------

#if QT_CONFIG(draganddrop)
//  QListModeViewBase::QListModeViewBase(QListView *q, QListViewPrivate *d)
extern "C" Q_DECL_EXPORT
QListModeViewBase *ritual_ZN17QListModeViewBaseC1EP9QListViewP16QListViewPrivate(
    QListView *q,
    QListViewPrivate *d) {
  return new QListModeViewBase(q, d);
}
#endif  // QT_CONFIG(draganddrop)

//  int QListModeViewBase::itemIndex(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase9itemIndexERK13QListViewItem(
    const QListModeViewBase *self,
    const QListViewItem *item) {
  return self->itemIndex(*item);
}

//  QListViewItem QListModeViewBase::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZNK17QListModeViewBase19indexToListViewItemERK11QModelIndex(
    const QListModeViewBase *self,
    const QModelIndex *index) {
  return new QListViewItem(self->indexToListViewItem(*index));
}

//  bool QListModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
//      &info, int max)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QListModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi(
    QListModeViewBase *self,
    const QListViewLayoutInfo *info,
    int max) {
  return self->doBatchedItemLayout(*info, max);
}

//  void QListModeViewBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase5clearEv(QListModeViewBase *self) {
  self->clear();
}

//  void QListModeViewBase::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase11setRowCountEi(
    QListModeViewBase *self,
    int rowCount) {
  self->setRowCount(rowCount);
}

//  QList<QModelIndex> QListModeViewBase::intersectingSet(const QRect &area)
//      const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK17QListModeViewBase15intersectingSetERK5QRect(
    const QListModeViewBase *self,
    const QRect *area) {
  return new QList<QModelIndex>(self->intersectingSet(*area));
}

//  void QListModeViewBase::dataChanged(const QModelIndex &a0, const
//      QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase11dataChangedERK11QModelIndexS2_(
    QListModeViewBase *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  self->dataChanged(*a0, *a1);
}

//  int QListModeViewBase::horizontalScrollToValue(int index,
//      QListView::ScrollHint hint, bool leftOf, bool rightOf, const QRect
//      &area, const QRect &rect) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase23horizontalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_(
    const QListModeViewBase *self,
    int index,
    const QListView::ScrollHint *hint,
    bool leftOf,
    bool rightOf,
    const QRect *area,
    const QRect *rect) {
  return self->horizontalScrollToValue(
      index,
      *hint,
      leftOf,
      rightOf,
      *area,
      *rect);
}

//  int QListModeViewBase::verticalScrollToValue(int index,
//      QListView::ScrollHint hint, bool above, bool below, const QRect
//      &area, const QRect &rect) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase21verticalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_(
    const QListModeViewBase *self,
    int index,
    const QListView::ScrollHint *hint,
    bool above,
    bool below,
    const QRect *area,
    const QRect *rect) {
  return self->verticalScrollToValue(
      index,
      *hint,
      above,
      below,
      *area,
      *rect);
}

//  void QListModeViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase16scrollContentsByEiib(
    QListModeViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->scrollContentsBy(dx, dy, scrollElasticBand);
}

//  QRect QListModeViewBase::mapToViewport(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QListModeViewBase13mapToViewportERK5QRect(
    const QListModeViewBase *self,
    const QRect *rect) {
  return new QRect(self->mapToViewport(*rect));
}

//  int QListModeViewBase::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase16horizontalOffsetEv(
    const QListModeViewBase *self) {
  return self->horizontalOffset();
}

//  int QListModeViewBase::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase14verticalOffsetEv(
    const QListModeViewBase *self) {
  return self->verticalOffset();
}

//  QSize QListModeViewBase::viewportSize(const QAbstractItemView *v)
extern "C" Q_DECL_EXPORT
QSize *ritual_ZN17QListModeViewBase12viewportSizeEPK17QAbstractItemView(
    const QAbstractItemView *v) {
  return new QSize(QListModeViewBase::viewportSize(v));
}

//  void QListModeViewBase::updateHorizontalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase25updateHorizontalScrollBarERK5QSize(
    QListModeViewBase *self,
    const QSize *step) {
  self->updateHorizontalScrollBar(*step);
}

//  void QListModeViewBase::updateVerticalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase23updateVerticalScrollBarERK5QSize(
    QListModeViewBase *self,
    const QSize *step) {
  self->updateVerticalScrollBar(*step);
}

#if QT_CONFIG(draganddrop)
//  QAbstractItemView::DropIndicatorPosition
//      QListModeViewBase::position(const QPoint &pos, const QRect &rect,
//      const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DropIndicatorPosition ritual_ZNK17QListModeViewBase8positionERK6QPointRK5QRectRK11QModelIndex(
    const QListModeViewBase *self,
    const QPoint *pos,
    const QRect *rect,
    const QModelIndex *idx) {
  return self->position(*pos, *rect, *idx);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QListModeViewBase::dragMoveEvent(QDragMoveEvent *e)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase13dragMoveEventEP14QDragMoveEvent(
    QListModeViewBase *self,
    QDragMoveEvent *e) {
  self->dragMoveEvent(e);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QListModeViewBase::dropOn(QDropEvent *event, int *row, int *col,
//      QModelIndex *index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QListModeViewBase6dropOnEP10QDropEventPiS2_P11QModelIndex(
    QListModeViewBase *self,
    QDropEvent *event,
    int *row,
    int *col,
    QModelIndex *index) {
  return self->dropOn(event, row, col, index);
}
#endif  // QT_CONFIG(draganddrop)

//  QPoint QListModeViewBase::initStaticLayout(const QListViewLayoutInfo
//      &info)
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZN17QListModeViewBase16initStaticLayoutERK19QListViewLayoutInfo(
    QListModeViewBase *self,
    const QListViewLayoutInfo *info) {
  return new QPoint(self->initStaticLayout(*info));
}

//  void QListModeViewBase::doStaticLayout(const QListViewLayoutInfo &info)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBase14doStaticLayoutERK19QListViewLayoutInfo(
    QListModeViewBase *self,
    const QListViewLayoutInfo *info) {
  self->doStaticLayout(*info);
}

//  int QListModeViewBase::perItemScrollToValue(int index, int value, int
//      height, QAbstractItemView::ScrollHint hint, Qt::Orientation
//      orientation, bool wrap, int extent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase20perItemScrollToValueEiiiN17QAbstractItemView10ScrollHintEN2Qt11OrientationEbi(
    const QListModeViewBase *self,
    int index,
    int value,
    int height,
    QAbstractItemView::ScrollHint hint,
    Qt::Orientation orientation,
    bool wrap,
    int extent) {
  return self->perItemScrollToValue(
      index,
      value,
      height,
      hint,
      orientation,
      wrap,
      extent);
}

//  int QListModeViewBase::perItemScrollingPageSteps(int length, int bounds,
//      bool wrap) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QListModeViewBase25perItemScrollingPageStepsEiib(
    const QListModeViewBase *self,
    int length,
    int bounds,
    bool wrap) {
  return self->perItemScrollingPageSteps(length, bounds, wrap);
}

//  QListModeViewBase::~QListModeViewBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QListModeViewBaseD1Ev(QListModeViewBase *self) {
  delete self;
}

//  int QListModeViewBase::itemIndex(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QListModeViewBase9itemIndexERK13QListViewItem(
    const QListModeViewBase *self,
    const QListViewItem *item) {
  return self->QListModeViewBase::itemIndex(*item);
}

//  QListViewItem QListModeViewBase::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_own_ZNK17QListModeViewBase19indexToListViewItemERK11QModelIndex(
    const QListModeViewBase *self,
    const QModelIndex *index) {
  return new QListViewItem(
      self->QListModeViewBase::indexToListViewItem(
          *index));
}

//  bool QListModeViewBase::doBatchedItemLayout(const QListViewLayoutInfo
//      &info, int max)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN17QListModeViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi(
    QListModeViewBase *self,
    const QListViewLayoutInfo *info,
    int max) {
  return self->QListModeViewBase::doBatchedItemLayout(*info, max);
}

//  void QListModeViewBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase5clearEv(QListModeViewBase *self) {
  self->QListModeViewBase::clear();
}

//  void QListModeViewBase::setRowCount(int rowCount)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase11setRowCountEi(
    QListModeViewBase *self,
    int rowCount) {
  self->QListModeViewBase::setRowCount(rowCount);
}

//  void QListModeViewBase::dataChanged(const QModelIndex &a0, const
//      QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase11dataChangedERK11QModelIndexS2_(
    QListModeViewBase *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  self->QListModeViewBase::dataChanged(*a0, *a1);
}

//  void QListModeViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase16scrollContentsByEiib(
    QListModeViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->QListModeViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
}

//  QRect QListModeViewBase::mapToViewport(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK17QListModeViewBase13mapToViewportERK5QRect(
    const QListModeViewBase *self,
    const QRect *rect) {
  return new QRect(self->QListModeViewBase::mapToViewport(*rect));
}

//  int QListModeViewBase::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QListModeViewBase16horizontalOffsetEv(
    const QListModeViewBase *self) {
  return self->QListModeViewBase::horizontalOffset();
}

//  int QListModeViewBase::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QListModeViewBase14verticalOffsetEv(
    const QListModeViewBase *self) {
  return self->QListModeViewBase::verticalOffset();
}

//  void QListModeViewBase::updateHorizontalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase25updateHorizontalScrollBarERK5QSize(
    QListModeViewBase *self,
    const QSize *step) {
  self->QListModeViewBase::updateHorizontalScrollBar(*step);
}

//  void QListModeViewBase::updateVerticalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QListModeViewBase23updateVerticalScrollBarERK5QSize(
    QListModeViewBase *self,
    const QSize *step) {
  self->QListModeViewBase::updateVerticalScrollBar(*step);
}

#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(listview)
