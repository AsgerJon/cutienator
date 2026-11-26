//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(tableview)
#if QT_CONFIG(tableview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtableview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtableview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtGui/qregion.h>
#include <QtWidgets/qstyleoption.h>
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/itemviews/qtableview.cpp, line 554, as local:qtableview.cpp:QTableCornerButton
#if QT_CONFIG(abstractbutton)
class QTableCornerButton : public QAbstractButton
{
    Q_OBJECT
public:
    QTableCornerButton(QWidget *parent) : QAbstractButton(parent) {
        setObjectName(QLatin1String("qt_tableview_cornerbutton"));
    }
    void paintEvent(QPaintEvent*) override {
        QStyleOptionHeader opt;
        opt.initFrom(this);
        QStyle::State state = QStyle::State_None;
        if (isEnabled())
            state |= QStyle::State_Enabled;
        if (isActiveWindow())
            state |= QStyle::State_Active;
        if (isDown())
            state |= QStyle::State_Sunken;
        opt.state = state;
        opt.rect = rect();
        opt.position = QStyleOptionHeader::OnlyOneSection;
        QPainter painter(this);
        style()->drawControl(QStyle::CE_Header, &opt, &painter, this);
    }
};
#endif  // QT_CONFIG(abstractbutton)

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

//  from src/widgets/itemviews/qtableview.cpp, line 143, as _ZNK15QSpanCollection11spansInRectEiiii
inline QSet<QSpanCollection::Span *> QSpanCollection::spansInRect(int x, int y, int w, int h) const
{
    QSet<Span *> list;
    Index::const_iterator it_y = index.lowerBound(-y);
    if (it_y == index.end())
        --it_y;
    while(-it_y.key() <= y + h) {
        SubIndex::const_iterator it_x = (*it_y).lowerBound(-x);
        if (it_x == (*it_y).end())
            --it_x;
        while(-it_x.key() <= x + w) {
            Span *s = *it_x;
            if (s->bottom() >= y && s->right() >= x)
                list << s;
            if (it_x == (*it_y).begin())
                break;
            --it_x;
        }
        if (it_y == index.begin())
            break;
        --it_y;
    }
    return list;
}

//  from src/widgets/itemviews/qtableview.cpp, line 115, as _ZNK15QSpanCollection6spanAtEii
inline QSpanCollection::Span *QSpanCollection::spanAt(int x, int y) const
{
    Index::const_iterator it_y = index.lowerBound(-y);
    if (it_y == index.end())
        return nullptr;
    SubIndex::const_iterator it_x = (*it_y).lowerBound(-x);
    if (it_x == (*it_y).end())
        return nullptr;
    Span *span = *it_x;
    if (span->right() >= x && span->bottom() >= y)
        return span;
    return nullptr;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4602, as _ZNK24QAbstractItemViewPrivate14editorForIndexERK11QModelIndex
inline const QEditorInfo & QAbstractItemViewPrivate::editorForIndex(const QModelIndex &index) const
{
    static QEditorInfo nullInfo;

    // do not try to search to avoid slow implicit cast from QModelIndex to QPersistentModelIndex
    if (indexEditorHash.isEmpty())
        return nullInfo;

    QIndexEditorHash::const_iterator it = indexEditorHash.find(index);
    if (it == indexEditorHash.end())
        return nullInfo;

    return it.value();
}

//  from src/widgets/itemviews/qtableview.cpp, line 74, as _ZN15QSpanCollection10updateSpanEPNS_4SpanEi
inline void QSpanCollection::updateSpan(QSpanCollection::Span *span, int old_height)
{
    if (old_height < span->height()) {
        //add the span as subspan in all the lists that intersect the new covered columns
        Index::iterator it_y = index.lowerBound(-(span->top() + old_height - 1));
        Q_ASSERT(it_y != index.end()); //it_y must exist since the span is in the list
        while (-it_y.key() <= span->bottom()) {
            (*it_y).insert(-span->left(), span);
            if (it_y == index.begin())
                break;
            --it_y;
        }
    } else if (old_height > span->height()) {
        //remove the span from all the subspans lists that intersect the columns not covered anymore
        Index::iterator it_y = index.lowerBound(-qMax(span->bottom(), span->top())); //qMax useful if height is 0
        Q_ASSERT(it_y != index.end()); //it_y must exist since the span is in the list
        while (-it_y.key() <= span->top() + old_height -1) {
            if (-it_y.key() > span->bottom()) {
                int removed = (*it_y).remove(-span->left());
                Q_ASSERT(removed == 1);
                Q_UNUSED(removed);
                if (it_y->isEmpty()) {
                    it_y = index.erase(it_y);
                }
            }
            if (it_y == index.begin())
                break;
            --it_y;
        }
    }

    if (span->width() == 0 && span->height() == 0) {
        spans.remove(span);
        delete span;
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 36, as _ZN15QSpanCollection7addSpanEPNS_4SpanE
inline void QSpanCollection::addSpan(QSpanCollection::Span *span)
{
    spans.push_back(span);
    Index::iterator it_y = index.lowerBound(-span->top());
    if (it_y == index.end() || it_y.key() != -span->top()) {
        //there is no spans that starts with the row in the index, so create a sublist for it.
        SubIndex sub_index;
        if (it_y != index.end()) {
            //the previouslist is the list of spans that sarts _before_ the row of the span.
            // and which may intersect this row.
            const SubIndex previousList = it_y.value();
            for (Span *s : previousList) {
                //If a subspans intersect the row, we need to split it into subspans
                if (s->bottom() >= span->top())
                    sub_index.insert(-s->left(), s);
            }
        }
        it_y = index.insert(-span->top(), sub_index);
        //we will insert span to *it_y in the later loop
    }

    //insert the span as supspan in all the lists that intesects the span
    while(-it_y.key() <= span->bottom()) {
        (*it_y).insert(-span->left(), span);
        if (it_y == index.begin())
            break;
        --it_y;
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 188, as _ZN15QSpanCollection18updateInsertedRowsEii
inline void QSpanCollection::updateInsertedRows(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (Span *span : spans) {
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_bottom < start)
            continue;
        if (span->m_top >= start)
            span->m_top += delta;
        span->m_bottom += delta;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ) {
        int y = -it_y.key();
        if (y < start) {
            ++it_y;
            continue;
        }

        index.insert(-y - delta, it_y.value());
        it_y = index.erase(it_y);
    }
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
#endif
}

//  from src/widgets/itemviews/qtableview.cpp, line 234, as _ZN15QSpanCollection21updateInsertedColumnsEii
inline void QSpanCollection::updateInsertedColumns(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (Span *span : spans) {
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_right < start)
            continue;
        if (span->m_left >= start)
            span->m_left += delta;
        span->m_right += delta;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ++it_y) {
        SubIndex &subindex = it_y.value();
        for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ) {
            int x = -it.key();
            if (x < start) {
                ++it;
                continue;
            }
            subindex.insert(-x - delta, it.value());
            it = subindex.erase(it);
        }
    }
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
#endif
}

//  from src/widgets/itemviews/qtableview.cpp, line 313, as _ZN15QSpanCollection17updateRemovedRowsEii
inline void QSpanCollection::updateRemovedRows(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    SpanList spansToBeDeleted;
    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (SpanList::iterator it = spans.begin(); it != spans.end(); ) {
        Span *span = *it;
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_bottom < start) {
            ++it;
            continue;
        }
        if (span->m_top < start) {
            if (span->m_bottom <= end)
                span->m_bottom = start - 1;
            else
                span->m_bottom -= delta;
        } else {
            if (span->m_bottom > end) {
                if (span->m_top <= end)
                    span->m_top = start;
                else
                    span->m_top -= delta;
                span->m_bottom -= delta;
            } else {
                span->will_be_deleted = true;
            }
        }
        if (span->m_top == span->m_bottom && span->m_left == span->m_right)
            span->will_be_deleted = true;
        if (span->will_be_deleted) {
            spansToBeDeleted.push_back(span);
            it = spans.erase(it);
        } else {
            ++it;
        }
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif
    if (spans.empty()) {
        qDeleteAll(spansToBeDeleted);
        index.clear();
        return;
    }

    Index::iterator it_y = index.end();
    do {
        --it_y;
        int y = -it_y.key();
        SubIndex &subindex = it_y.value();
        if (y < start) {
            if (cleanSpanSubIndex(subindex, y))
                it_y = index.erase(it_y);
        } else if (y >= start && y <= end) {
            bool span_at_start = false;
            SubIndex spansToBeMoved;
            for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ++it) {
                Span *span = it.value();
                if (span->will_be_deleted)
                    continue;
                if (!span_at_start && span->m_top == start)
                    span_at_start = true;
                spansToBeMoved.insert(it.key(), span);
            }

            if (y == start && span_at_start)
                subindex.clear();
            else
                it_y = index.erase(it_y);

            if (span_at_start) {
                Index::iterator it_start;
                if (y == start)
                    it_start = it_y;
                else {
                    it_start = index.find(-start);
                    if (it_start == index.end())
                        it_start = index.insert(-start, SubIndex());
                }
                SubIndex &start_subindex = it_start.value();
                for (SubIndex::iterator it = spansToBeMoved.begin(); it != spansToBeMoved.end(); ++it)
                    start_subindex.insert(it.key(), it.value());
            }
        } else {
            if (y == end + 1) {
                Index::iterator it_top = index.find(-y + delta);
                if (it_top == index.end())
                    it_top = index.insert(-y + delta, SubIndex());
                for (SubIndex::iterator it = subindex.begin(); it != subindex.end(); ) {
                    Span *span = it.value();
                    if (!span->will_be_deleted)
                        it_top.value().insert(it.key(), span);
                    ++it;
                }
            } else {
                index.insert(-y + delta, subindex);
            }
            it_y = index.erase(it_y);
        }
    } while (it_y != index.begin());

#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
    qDebug("Deleted");
    qDebug() << spansToBeDeleted;
#endif
    qDeleteAll(spansToBeDeleted);
}

//  from src/widgets/itemviews/qtableview.cpp, line 438, as _ZN15QSpanCollection20updateRemovedColumnsEii
inline void QSpanCollection::updateRemovedColumns(int start, int end)
{
#ifdef DEBUG_SPAN_UPDATE
    qDebug() << start << end << Qt::endl << index;
#endif
    if (spans.empty())
        return;

    SpanList toBeDeleted;
    int delta = end - start + 1;
#ifdef DEBUG_SPAN_UPDATE
    qDebug("Before");
#endif
    for (SpanList::iterator it = spans.begin(); it != spans.end(); ) {
        Span *span = *it;
#ifdef DEBUG_SPAN_UPDATE
        qDebug() << span << *span;
#endif
        if (span->m_right < start) {
            ++it;
            continue;
        }
        if (span->m_left < start) {
            if (span->m_right <= end)
                span->m_right = start - 1;
            else
                span->m_right -= delta;
        } else {
            if (span->m_right > end) {
                if (span->m_left <= end)
                    span->m_left = start;
                else
                    span->m_left -= delta;
                span->m_right -= delta;
            } else {
                span->will_be_deleted = true;
            }
        }
        if (span->m_top == span->m_bottom && span->m_left == span->m_right)
            span->will_be_deleted = true;
        if (span->will_be_deleted) {
            toBeDeleted.push_back(span);
            it = spans.erase(it);
        } else {
            ++it;
        }
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug("After");
    qDebug() << spans;
#endif
    if (spans.empty()) {
        qDeleteAll(toBeDeleted);
        index.clear();
        return;
    }

    for (Index::iterator it_y = index.begin(); it_y != index.end(); ) {
        int y = -it_y.key();
        if (cleanSpanSubIndex(it_y.value(), y, true))
            it_y = index.erase(it_y);
        else
            ++it_y;
    }

#ifdef DEBUG_SPAN_UPDATE
    qDebug() << index;
    qDebug("Deleted");
    qDebug() << toBeDeleted;
#endif
    qDeleteAll(toBeDeleted);
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

//  from src/widgets/itemviews/qtableview.cpp, line 284, as _ZN15QSpanCollection17cleanSpanSubIndexER4QMapIiPNS_4SpanEEib
inline bool QSpanCollection::cleanSpanSubIndex(QSpanCollection::SubIndex &subindex, int y, bool update)
{
    if (subindex.isEmpty())
        return true;

    bool should_be_deleted = true;
    SubIndex::iterator it = subindex.end();
    do {
        --it;
        int x = -it.key();
        Span *span = it.value();
        if (span->will_be_deleted) {
            it = subindex.erase(it);
            continue;
        }
        if (update && span->m_left != x) {
            subindex.insert(-span->m_left, span);
            it = subindex.erase(it);
        }
        if (should_be_deleted && span->m_top == y)
            should_be_deleted = false;
    } while (it != subindex.begin());

    return should_be_deleted;
}

//  from src/widgets/itemviews/qtableview.cpp, line 607, as _ZN17QTableViewPrivate16clearConnectionsEv
inline void QTableViewPrivate::clearConnections()
{
    for (QMetaObject::Connection &connection : modelConnections)
        QObject::disconnect(connection);
    for (QMetaObject::Connection &connection : verHeaderConnections)
        QObject::disconnect(connection);
    for (QMetaObject::Connection &connection : horHeaderConnections)
        QObject::disconnect(connection);
    for (QMetaObject::Connection &connection : dynHorHeaderConnections)
        QObject::disconnect(connection);
    QObject::disconnect(selectionmodelConnection);
#if QT_CONFIG(abstractbutton)
    QObject::disconnect(cornerWidgetConnection);
#endif
}

//  from src/widgets/itemviews/qtableview.cpp, line 627, as _ZNK17QTableViewPrivate20trimHiddenSelectionsEP19QItemSelectionRange
inline void QTableViewPrivate::trimHiddenSelections(QItemSelectionRange *range) const
{
    Q_ASSERT(range && range->isValid());

    int top = range->top();
    int left = range->left();
    int bottom = range->bottom();
    int right = range->right();

    while (bottom >= top && verticalHeader->isSectionHidden(bottom))
        --bottom;
    while (right >= left && horizontalHeader->isSectionHidden(right))
        --right;

    if (top > bottom || left > right) { // everything is hidden
        *range = QItemSelectionRange();
        return;
    }

    while (verticalHeader->isSectionHidden(top) && top <= bottom)
        ++top;
    while (horizontalHeader->isSectionHidden(left) && left <= right)
        ++left;

    if (top > bottom || left > right) { // everything is hidden
        *range = QItemSelectionRange();
        return;
    }

    QModelIndex bottomRight = model->index(bottom, right, range->parent());
    QModelIndex topLeft = model->index(top, left, range->parent());
    *range = QItemSelectionRange(topLeft, bottomRight);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1028, as _ZNK17QTableViewPrivate16viewItemPositionERK11QModelIndex
inline QStyleOptionViewItem::ViewItemPosition QTableViewPrivate::viewItemPosition(
        const QModelIndex &index) const
{
    int visualColumn = horizontalHeader->visualIndex(index.column());
    int count = horizontalHeader->count();

    if (count <= 0 || visualColumn < 0 || visualColumn >= count)
        return QStyleOptionViewItem::Invalid;

    if (count == 1 && visualColumn == 0)
        return QStyleOptionViewItem::OnlyOne;
    else if (visualColumn == 0)
        return QStyleOptionViewItem::Beginning;
    else if (visualColumn == count - 1)
        return QStyleOptionViewItem::End;
    else
        return QStyleOptionViewItem::Middle;
}

//  from src/widgets/itemviews/qtableview.cpp, line 757, as _ZNK17QTableViewPrivate21sectionSpanEndLogicalEPK11QHeaderViewii
inline int QTableViewPrivate::sectionSpanEndLogical(const QHeaderView *header, int logical, int span) const
{
    int visual = header->visualIndex(logical);
    for (int i = 1; i < span; ) {
        if (++visual >= header->count())
            break;
        logical = header->logicalIndex(visual);
        ++i;
    }
    return logical;
}

//  from src/widgets/itemviews/qtableview.cpp, line 774, as _ZNK17QTableViewPrivate15sectionSpanSizeEPK11QHeaderViewii
inline int QTableViewPrivate::sectionSpanSize(const QHeaderView *header, int logical, int span) const
{
    int endLogical = sectionSpanEndLogical(header, logical, span);
    return header->sectionPosition(endLogical)
        - header->sectionPosition(logical)
        + header->sectionSize(endLogical);
}

//  from src/widgets/itemviews/qtableview.cpp, line 788, as _ZNK17QTableViewPrivate19spanContainsSectionEPK11QHeaderViewiii
inline bool QTableViewPrivate::spanContainsSection(const QHeaderView *header, int logical, int spanLogical, int span) const
{
    if (logical == spanLogical)
        return true; // it's the start of the span
    int visual = header->visualIndex(spanLogical);
    for (int i = 1; i < span; ) {
        if (++visual >= header->count())
            break;
        spanLogical = header->logicalIndex(visual);
        if (logical == spanLogical)
            return true;
        ++i;
    }
    return false;
}

//  from src/widgets/itemviews/qtableview.cpp, line 894, as _ZN17QTableViewPrivate16drawAndClipSpansERK7QRegionP8QPainterRK20QStyleOptionViewItemP9QBitArrayiiii
inline void QTableViewPrivate::drawAndClipSpans(const QRegion &area, QPainter *painter,
                                         const QStyleOptionViewItem &option, QBitArray *drawn,
                                         int firstVisualRow, int lastVisualRow, int firstVisualColumn, int lastVisualColumn)
{
    Q_Q(const QTableView);
    bool alternateBase = false;
    QRegion region = viewport->rect();

    QSet<QSpanCollection::Span *> visibleSpans;
    bool sectionMoved = verticalHeader->sectionsMoved() || horizontalHeader->sectionsMoved();

    if (!sectionMoved) {
        visibleSpans = spans.spansInRect(logicalColumn(firstVisualColumn), logicalRow(firstVisualRow),
                                         lastVisualColumn - firstVisualColumn + 1, lastVisualRow - firstVisualRow + 1);
    } else {
        // Any cell outside the viewport, on the top or left, can still end up visible inside the
        // viewport if is has a span. Calculating if a spanned cell overlaps with the viewport is
        // "easy" enough when the columns (or rows) in the view are aligned with the columns
        // in the model; In that case you know that if a column is outside the viewport on the
        // right, it cannot affect the drawing of the cells inside the viewport, even with a span.
        // And under that assumption, the spansInRect() function can be used (which is optimized
        // to only iterate the spans that are close to the viewport).
        // But when the view has rearranged the columns (or rows), this is no longer true. In that
        // case, even if a column, according to the model, is outside the viewport on the right, it
        // can still overlap with the viewport. This can happen if it was moved to the left of the
        // viewport and one of its cells has a span. In that case we need to take the theoretically
        // slower route and iterate through all the spans, and check if any of them overlaps with
        // the viewport.
        const auto spanList = spans.spans;
        for (QSpanCollection::Span *span : spanList) {
            const int spanVisualLeft = visualColumn(span->left());
            const int spanVisualTop = visualRow(span->top());
            const int spanVisualRight = spanVisualLeft + span->width() - 1;
            const int spanVisualBottom = spanVisualTop + span->height() - 1;
            if ((spanVisualLeft <= lastVisualColumn && spanVisualRight >= firstVisualColumn)
                    && (spanVisualTop <= lastVisualRow && spanVisualBottom >= firstVisualRow))
                visibleSpans.insert(span);
        }
    }

    for (QSpanCollection::Span *span : std::as_const(visibleSpans)) {
        int row = span->top();
        int col = span->left();
        QModelIndex index = model->index(row, col, root);
        if (!index.isValid())
            continue;
        QRect rect = visualSpanRect(*span);
        rect.translate(scrollDelayOffset);
        if (!area.intersects(rect))
            continue;
        QStyleOptionViewItem opt = option;
        opt.rect = rect;
        alternateBase = alternatingColors && (span->top() & 1);
        opt.features.setFlag(QStyleOptionViewItem::Alternate, alternateBase);
        drawCell(painter, opt, index);
        if (showGrid) {
            // adjust the clip rect to be able to paint the top & left grid lines
            // if the headers are not visible, see paintEvent()
            if (horizontalHeader->visualIndex(row) == 0)
                rect.setTop(rect.top() + 1);
            if (verticalHeader->visualIndex(row) == 0) {
                if (q->isLeftToRight())
                    rect.setLeft(rect.left() + 1);
                else
                    rect.setRight(rect.right() - 1);
            }
        }
        region -= rect;
        for (int r = span->top(); r <= span->bottom(); ++r) {
            const int vr = visualRow(r);
            if (vr < firstVisualRow || vr > lastVisualRow)
                continue;
            for (int c = span->left(); c <= span->right(); ++c) {
                const int vc = visualColumn(c);
                if (vc < firstVisualColumn  || vc > lastVisualColumn)
                    continue;
                drawn->setBit((vr - firstVisualRow) * (lastVisualColumn - firstVisualColumn + 1)
                             + vc - firstVisualColumn);
            }
        }

    }
    painter->setClipRegion(region);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1051, as _ZN17QTableViewPrivate8drawCellEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex
inline void QTableViewPrivate::drawCell(QPainter *painter, const QStyleOptionViewItem &option, const QModelIndex &index)
{
    Q_Q(QTableView);
    QStyleOptionViewItem opt = option;

    if (selectionModel && selectionModel->isSelected(index))
        opt.state |= QStyle::State_Selected;
    if (index == hover)
        opt.state |= QStyle::State_MouseOver;
    if (option.state & QStyle::State_Enabled) {
        QPalette::ColorGroup cg;
        if ((model->flags(index) & Qt::ItemIsEnabled) == 0) {
            opt.state &= ~QStyle::State_Enabled;
            cg = QPalette::Disabled;
        } else {
            cg = QPalette::Normal;
        }
        opt.palette.setCurrentColorGroup(cg);
    }
    opt.viewItemPosition = viewItemPosition(index);

    if (index == q->currentIndex()) {
        const bool focus = (q->hasFocus() || viewport->hasFocus()) && q->currentIndex().isValid();
        if (focus)
            opt.state |= QStyle::State_HasFocus;
    }

    q->style()->drawPrimitive(QStyle::PE_PanelItemViewRow, &opt, painter, q);

    q->itemDelegateForIndex(index)->paint(painter, opt, index);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1087, as _ZNK17QTableViewPrivate17widthHintForIndexERK11QModelIndexiRK20QStyleOptionViewItem
inline int QTableViewPrivate::widthHintForIndex(const QModelIndex &index, int hint, const QStyleOptionViewItem &option) const
{
    Q_Q(const QTableView);
    const int oldHint = hint;
    QWidget *editor = editorForIndex(index).widget.data();
    if (editor && persistent.contains(editor)) {
        hint = qMax(hint, editor->sizeHint().width());
        int min = editor->minimumSize().width();
        int max = editor->maximumSize().width();
        hint = qBound(min, hint, max);
    }
    hint = qMax(hint, q->itemDelegateForIndex(index)->sizeHint(option, index).width());

    if (hasSpans()) {
        auto span = spans.spanAt(index.column(), index.row());
        if (span && span->m_left == index.column() && span->m_top == index.row()) {
            // spans are screwed up when sections are moved
            const auto left = logicalColumn(span->m_left);
            for (int i = 1; i <= span->width(); ++i)
               hint -= q->columnWidth(visualColumn(left + i));
        }
        hint = std::max(hint, oldHint);
    }
    return hint;
}

//  from src/widgets/itemviews/qtableview.cpp, line 1117, as _ZNK17QTableViewPrivate18heightHintForIndexERK11QModelIndexiR20QStyleOptionViewItem
inline int QTableViewPrivate::heightHintForIndex(const QModelIndex &index, int hint, QStyleOptionViewItem &option) const
{
    Q_Q(const QTableView);
    QWidget *editor = editorForIndex(index).widget.data();
    if (editor && persistent.contains(editor)) {
        hint = qMax(hint, editor->sizeHint().height());
        int min = editor->minimumSize().height();
        int max = editor->maximumSize().height();
        hint = qBound(min, hint, max);
    }

    if (wrapItemText) {// for wrapping boundaries
        option.rect.setY(q->rowViewportPosition(index.row()));
        int height = q->rowHeight(index.row());
        // if the option.height == 0 then q->itemDelegateForIndex(index)->sizeHint(option, index) will be wrong.
        // The option.height == 0 is used to conclude that the text is not wrapped, and hence it will
        // (exactly like widthHintForIndex) return a QSize with a long width (that we don't use) -
        // and the height of the text if it was/is on one line.
        // What we want is a height hint for the current width (and we know that this section is not hidden)
        // Therefore we catch this special situation with:
        if (height == 0)
            height = 1;
        option.rect.setHeight(height);
        option.rect.setX(q->columnViewportPosition(index.column()));
        option.rect.setWidth(q->columnWidth(index.column()));
        if (hasSpans()) {
            auto span = spans.spanAt(index.column(), index.row());
            if (span && span->m_left == index.column() && span->m_top == index.row())
                option.rect.setWidth(std::max(option.rect.width(), visualSpanRect(*span).width()));
        }
        // 1px less space when grid is shown (see drawCell)
        if (showGrid)
            option.rect.setWidth(option.rect.width() - 1);
    }
    hint = qMax(hint, q->itemDelegateForIndex(index)->sizeHint(option, index).height());
    return hint;
}

//  from src/widgets/itemviews/qtableview.cpp, line 711, as _ZN17QTableViewPrivate7setSpanEiiii
inline void QTableViewPrivate::setSpan(int row, int column, int rowSpan, int columnSpan)
{
    if (Q_UNLIKELY(row < 0 || column < 0 || rowSpan <= 0 || columnSpan <= 0)) {
        qWarning("QTableView::setSpan: invalid span given: (%d, %d, %d, %d)",
                 row, column, rowSpan, columnSpan);
        return;
    }
    QSpanCollection::Span *sp = spans.spanAt(column, row);
    if (sp) {
        if (sp->top() != row || sp->left() != column) {
            qWarning("QTableView::setSpan: span cannot overlap");
            return;
        }
        if (rowSpan == 1 && columnSpan == 1) {
            rowSpan = columnSpan = 0;
        }
        const int old_height = sp->height();
        sp->m_bottom = row + rowSpan - 1;
        sp->m_right = column + columnSpan - 1;
        spans.updateSpan(sp, old_height);
        return;
    } else if (Q_UNLIKELY(rowSpan == 1 && columnSpan == 1)) {
        qWarning("QTableView::setSpan: single cell span won't be added");
        return;
    }
    sp = new QSpanCollection::Span(row, column, rowSpan, columnSpan);
    spans.addSpan(sp);
}

//  from src/widgets/itemviews/qtableview.cpp, line 744, as _ZNK17QTableViewPrivate4spanEii
inline QSpanCollection::Span QTableViewPrivate::span(int row, int column) const
{
    QSpanCollection::Span *sp = spans.spanAt(column, row);
    if (sp)
        return *sp;

    return QSpanCollection::Span(row, column, 1, 1);
}

//  from src/widgets/itemviews/qtableview.cpp, line 809, as _ZNK17QTableViewPrivate19nextActiveVisualRowEiiiNS_15SearchDirectionE
inline int QTableViewPrivate::nextActiveVisualRow(int rowToStart, int column, int limit,
                                           SearchDirection searchDirection) const
{
    const int lc = logicalColumn(column);
    int visualRow = rowToStart;
    const auto isCellActive = [this](int vr, int lc)
    {
        const int lr = logicalRow(vr);
        return !isRowHidden(lr) && isCellEnabled(lr, lc);
    };
    switch (searchDirection) {
    case SearchDirection::Increasing:
        if (visualRow < limit) {
            while (!isCellActive(visualRow, lc)) {
                if (++visualRow == limit)
                    return rowToStart;
            }
        }
        break;
    case SearchDirection::Decreasing:
        while (visualRow > limit && !isCellActive(visualRow, lc))
            --visualRow;
        break;
    }
    return visualRow;
}

//  from src/widgets/itemviews/qtableview.cpp, line 841, as _ZNK17QTableViewPrivate22nextActiveVisualColumnEiiiNS_15SearchDirectionE
inline int QTableViewPrivate::nextActiveVisualColumn(int row, int columnToStart, int limit,
                                              SearchDirection searchDirection) const
{
    const int lr = logicalRow(row);
    int visualColumn = columnToStart;
    const auto isCellActive = [this](int lr, int vc)
    {
        const int lc = logicalColumn(vc);
        return !isColumnHidden(lc) && isCellEnabled(lr, lc);
    };
    switch (searchDirection) {
    case SearchDirection::Increasing:
        while (visualColumn < limit && !isCellActive(lr, visualColumn))
            ++visualColumn;
        break;
    case SearchDirection::Decreasing:
        while (visualColumn > limit && !isCellActive(lr, visualColumn))
            --visualColumn;
        break;
    }
    return visualColumn;
}

//  from src/widgets/itemviews/qtableview.cpp, line 868, as _ZNK17QTableViewPrivate14visualSpanRectERKN15QSpanCollection4SpanE
inline QRect QTableViewPrivate::visualSpanRect(const QSpanCollection::Span &span) const
{
    Q_Q(const QTableView);
    // vertical
    int row = span.top();
    int rowp = verticalHeader->sectionViewportPosition(row);
    int rowh = rowSpanHeight(row, span.height());
    // horizontal
    int column = span.left();
    int colw = columnSpanWidth(column, span.width());
    if (q->isRightToLeft())
        column = span.right();
    int colp = horizontalHeader->sectionViewportPosition(column);

    const int i = showGrid ? 1 : 0;
    if (q->isRightToLeft())
        return QRect(colp + i, rowp, colw - i, rowh - i);
    return QRect(colp, rowp, colw - i, rowh - i);
}

//  from src/widgets/itemviews/qtableview.cpp, line 3485, as _ZN17QTableViewPrivate9selectRowEib
inline void QTableViewPrivate::selectRow(int row, bool anchor)
{
    Q_Q(QTableView);

    if (q->selectionBehavior() == QTableView::SelectColumns
        || (q->selectionMode() == QTableView::SingleSelection
            && q->selectionBehavior() == QTableView::SelectItems))
        return;

    if (row >= 0 && row < model->rowCount(root)) {
        int column = horizontalHeader->logicalIndexAt(q->isRightToLeft() ? viewport->width() : 0);
        QModelIndex index = model->index(row, column, root);
        QItemSelectionModel::SelectionFlags command = q->selectionCommand(index);

        {
            // currentSelectionStartIndex gets modified inside QAbstractItemView::currentChanged()
            const auto startIndex = currentSelectionStartIndex;
            selectionModel->setCurrentIndex(index, QItemSelectionModel::NoUpdate);
            currentSelectionStartIndex = startIndex;
        }

        if ((anchor && !(command & QItemSelectionModel::Current))
            || (q->selectionMode() == QTableView::SingleSelection))
            currentSelectionStartIndex = model->index(row, column, root);

        if (q->selectionMode() != QTableView::SingleSelection
            && command.testFlag(QItemSelectionModel::Toggle)) {
            if (anchor)
                ctrlDragSelectionFlag = verticalHeader->selectionModel()->selectedRows(column).contains(index)
                                    ? QItemSelectionModel::Deselect : QItemSelectionModel::Select;
            command &= ~QItemSelectionModel::Toggle;
            command |= ctrlDragSelectionFlag;
            if (!anchor)
                command |= QItemSelectionModel::Current;
        }

        const auto rowSectionAnchor = currentSelectionStartIndex.row();
        QModelIndex upper = model->index(qMin(rowSectionAnchor, row), column, root);
        QModelIndex lower = model->index(qMax(rowSectionAnchor, row), column, root);
        if ((verticalHeader->sectionsMoved() && upper.row() != lower.row())) {
            q->setSelection(q->visualRect(upper) | q->visualRect(lower), command | QItemSelectionModel::Rows);
        } else {
            selectionModel->select(QItemSelection(upper, lower), command | QItemSelectionModel::Rows);
        }
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 3532, as _ZN17QTableViewPrivate12selectColumnEib
inline void QTableViewPrivate::selectColumn(int column, bool anchor)
{
    Q_Q(QTableView);

    if (q->selectionBehavior() == QTableView::SelectRows
        || (q->selectionMode() == QTableView::SingleSelection
            && q->selectionBehavior() == QTableView::SelectItems))
        return;

    if (column >= 0 && column < model->columnCount(root)) {
        int row = verticalHeader->logicalIndexAt(0);
        QModelIndex index = model->index(row, column, root);
        QItemSelectionModel::SelectionFlags command = q->selectionCommand(index);

        {
            // currentSelectionStartIndex gets modified inside QAbstractItemView::currentChanged()
            const auto startIndex = currentSelectionStartIndex;
            selectionModel->setCurrentIndex(index, QItemSelectionModel::NoUpdate);
            currentSelectionStartIndex = startIndex;
        }

        if ((anchor && !(command & QItemSelectionModel::Current))
            || (q->selectionMode() == QTableView::SingleSelection))
            currentSelectionStartIndex = model->index(row, column, root);

        if (q->selectionMode() != QTableView::SingleSelection
            && command.testFlag(QItemSelectionModel::Toggle)) {
            if (anchor)
                ctrlDragSelectionFlag = horizontalHeader->selectionModel()->selectedColumns(row).contains(index)
                                    ? QItemSelectionModel::Deselect : QItemSelectionModel::Select;
            command &= ~QItemSelectionModel::Toggle;
            command |= ctrlDragSelectionFlag;
            if (!anchor)
                command |= QItemSelectionModel::Current;
        }

        const auto columnSectionAnchor = currentSelectionStartIndex.column();
        QModelIndex left = model->index(row, qMin(columnSectionAnchor, column), root);
        QModelIndex right = model->index(row, qMax(columnSectionAnchor, column), root);
        if ((horizontalHeader->sectionsMoved() && left.column() != right.column())) {
            q->setSelection(q->visualRect(left) | q->visualRect(right), command | QItemSelectionModel::Columns);
        } else {
            selectionModel->select(QItemSelection(left, right), command | QItemSelectionModel::Columns);
        }
    }
}

//  from src/widgets/itemviews/qtableview.cpp, line 983, as _ZN17QTableViewPrivate22updateSpanInsertedRowsERK11QModelIndexii
inline void QTableViewPrivate::updateSpanInsertedRows(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    spans.updateInsertedRows(start, end);
}

//  from src/widgets/itemviews/qtableview.cpp, line 993, as _ZN17QTableViewPrivate25updateSpanInsertedColumnsERK11QModelIndexii
inline void QTableViewPrivate::updateSpanInsertedColumns(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    spans.updateInsertedColumns(start, end);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1003, as _ZN17QTableViewPrivate21updateSpanRemovedRowsERK11QModelIndexii
inline void QTableViewPrivate::updateSpanRemovedRows(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    spans.updateRemovedRows(start, end);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1013, as _ZN17QTableViewPrivate24updateSpanRemovedColumnsERK11QModelIndexii
inline void QTableViewPrivate::updateSpanRemovedColumns(const QModelIndex &parent, int start, int end)
{
    Q_UNUSED(parent);
    spans.updateRemovedColumns(start, end);
}

//  from src/widgets/itemviews/qtableview.cpp, line 1023, as _ZN17QTableViewPrivate20sortIndicatorChangedEiN2Qt9SortOrderE
inline void QTableViewPrivate::sortIndicatorChanged(int column, Qt::SortOrder order)
{
    model->sort(column, order);
}
//  -----------------------------------------------------------------------

//  A QTableViewPrivate that Python can take functions over in. Every QTableViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(tableview)
typedef const QRect * (*CuteQTableViewPrivateCall0)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(tableview)
typedef int (*CuteQTableViewPrivateCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall5)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall6)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall7)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall9)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall10)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall11)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTableViewPrivateCall12)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTableViewPrivateCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQTableViewPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQTableViewPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTableViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTableViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTableViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQTableViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQTableViewPrivateCall20)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQTableViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTableViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTableViewPrivateCall24)(const void *, int *);
typedef int (*CuteQTableViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQTableViewPrivateCall26)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall27)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall28)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall29)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall30)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall31)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall32)(const void *, int *);
typedef void (*CuteQTableViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQTableViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQTableViewPrivateCall35)(const void *, int *);
class CuteQTableViewPrivate : public QTableViewPrivate {
public:
  using QTableViewPrivate::QTableViewPrivate;
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
      CuteQTableViewPrivateCall0 call = reinterpret_cast<CuteQTableViewPrivateCall0>(taken[0]);
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
      CuteQTableViewPrivateCall1 call = reinterpret_cast<CuteQTableViewPrivateCall1>(taken[1]);
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
      CuteQTableViewPrivateCall2 call = reinterpret_cast<CuteQTableViewPrivateCall2>(taken[2]);
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
      CuteQTableViewPrivateCall3 call = reinterpret_cast<CuteQTableViewPrivateCall3>(taken[3]);
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
      CuteQTableViewPrivateCall4 call = reinterpret_cast<CuteQTableViewPrivateCall4>(taken[4]);
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
      CuteQTableViewPrivateCall5 call = reinterpret_cast<CuteQTableViewPrivateCall5>(taken[5]);
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
      CuteQTableViewPrivateCall6 call = reinterpret_cast<CuteQTableViewPrivateCall6>(taken[6]);
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
      CuteQTableViewPrivateCall7 call = reinterpret_cast<CuteQTableViewPrivateCall7>(taken[7]);
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
      CuteQTableViewPrivateCall8 call = reinterpret_cast<CuteQTableViewPrivateCall8>(taken[8]);
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
      CuteQTableViewPrivateCall9 call = reinterpret_cast<CuteQTableViewPrivateCall9>(taken[9]);
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
      CuteQTableViewPrivateCall10 call = reinterpret_cast<CuteQTableViewPrivateCall10>(taken[10]);
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
      CuteQTableViewPrivateCall11 call = reinterpret_cast<CuteQTableViewPrivateCall11>(taken[11]);
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
      CuteQTableViewPrivateCall12 call = reinterpret_cast<CuteQTableViewPrivateCall12>(taken[12]);
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
      CuteQTableViewPrivateCall13 call = reinterpret_cast<CuteQTableViewPrivateCall13>(taken[13]);
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
      CuteQTableViewPrivateCall14 call = reinterpret_cast<CuteQTableViewPrivateCall14>(taken[14]);
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
      CuteQTableViewPrivateCall15 call = reinterpret_cast<CuteQTableViewPrivateCall15>(taken[15]);
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
      CuteQTableViewPrivateCall16 call = reinterpret_cast<CuteQTableViewPrivateCall16>(taken[16]);
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
      CuteQTableViewPrivateCall17 call = reinterpret_cast<CuteQTableViewPrivateCall17>(taken[17]);
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
      CuteQTableViewPrivateCall18 call = reinterpret_cast<CuteQTableViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTableViewPrivateCall19 call = reinterpret_cast<CuteQTableViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTableViewPrivateCall20 call = reinterpret_cast<CuteQTableViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQTableViewPrivateCall21 call = reinterpret_cast<CuteQTableViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQTableViewPrivateCall22 call = reinterpret_cast<CuteQTableViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTableViewPrivateCall23 call = reinterpret_cast<CuteQTableViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTableViewPrivateCall24 call = reinterpret_cast<CuteQTableViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQTableViewPrivateCall25 call = reinterpret_cast<CuteQTableViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQTableViewPrivateCall26 call = reinterpret_cast<CuteQTableViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQTableViewPrivateCall27 call = reinterpret_cast<CuteQTableViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTableViewPrivateCall28 call = reinterpret_cast<CuteQTableViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTableViewPrivateCall29 call = reinterpret_cast<CuteQTableViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTableViewPrivateCall30 call = reinterpret_cast<CuteQTableViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTableViewPrivateCall31 call = reinterpret_cast<CuteQTableViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTableViewPrivateCall32 call = reinterpret_cast<CuteQTableViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQTableViewPrivateCall33 call = reinterpret_cast<CuteQTableViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQTableViewPrivateCall34 call = reinterpret_cast<CuteQTableViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTableViewPrivateCall35 call = reinterpret_cast<CuteQTableViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTableView *QTableViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTableView *ritual_ZN17QTableViewPrivate6q_funcEv(QTableViewPrivate *self) {
  return self->q_func();
}

//  const QTableView *QTableViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTableView *ritual_ZNK17QTableViewPrivate6q_funcEv(
    const QTableViewPrivate *self) {
  return self->q_func();
}

//  void QTableViewPrivate::clearConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate16clearConnectionsEv(
    QTableViewPrivate *self) {
  self->clearConnections();
}

//  void QTableViewPrivate::trimHiddenSelections(QItemSelectionRange *range)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK17QTableViewPrivate20trimHiddenSelectionsEP19QItemSelectionRange(
    const QTableViewPrivate *self,
    QItemSelectionRange *range) {
  self->trimHiddenSelections(range);
}

//  QRect QTableViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QTableViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QTableViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(self->intersectedRect(*rect, *topLeft, *bottomRight));
}

//  bool QTableViewPrivate::isHidden(int row, int col) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate8isHiddenEii(
    const QTableViewPrivate *self,
    int row,
    int col) {
  return self->isHidden(row, col);
}

//  int QTableViewPrivate::visualRow(int logicalRow) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate9visualRowEi(
    const QTableViewPrivate *self,
    int logicalRow) {
  return self->visualRow(logicalRow);
}

//  int QTableViewPrivate::visualColumn(int logicalCol) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate12visualColumnEi(
    const QTableViewPrivate *self,
    int logicalCol) {
  return self->visualColumn(logicalCol);
}

//  int QTableViewPrivate::logicalRow(int visualRow) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate10logicalRowEi(
    const QTableViewPrivate *self,
    int visualRow) {
  return self->logicalRow(visualRow);
}

//  int QTableViewPrivate::logicalColumn(int visualCol) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate13logicalColumnEi(
    const QTableViewPrivate *self,
    int visualCol) {
  return self->logicalColumn(visualCol);
}

//  QStyleOptionViewItem::ViewItemPosition
//      QTableViewPrivate::viewItemPosition(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QStyleOptionViewItem::ViewItemPosition ritual_ZNK17QTableViewPrivate16viewItemPositionERK11QModelIndex(
    const QTableViewPrivate *self,
    const QModelIndex *index) {
  return self->viewItemPosition(*index);
}

#if QT_CONFIG(accessibility)
//  int QTableViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QTableViewPrivate *self,
    const QModelIndex *index) {
  return self->accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

//  int QTableViewPrivate::sectionSpanEndLogical(const QHeaderView *header,
//      int logical, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate21sectionSpanEndLogicalEPK11QHeaderViewii(
    const QTableViewPrivate *self,
    const QHeaderView *header,
    int logical,
    int span) {
  return self->sectionSpanEndLogical(header, logical, span);
}

//  int QTableViewPrivate::sectionSpanSize(const QHeaderView *header, int
//      logical, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate15sectionSpanSizeEPK11QHeaderViewii(
    const QTableViewPrivate *self,
    const QHeaderView *header,
    int logical,
    int span) {
  return self->sectionSpanSize(header, logical, span);
}

//  bool QTableViewPrivate::spanContainsSection(const QHeaderView *header,
//      int logical, int spanLogical, int span) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate19spanContainsSectionEPK11QHeaderViewiii(
    const QTableViewPrivate *self,
    const QHeaderView *header,
    int logical,
    int spanLogical,
    int span) {
  return self->spanContainsSection(header, logical, spanLogical, span);
}

//  void QTableViewPrivate::drawAndClipSpans(const QRegion &area, QPainter
//      *painter, const QStyleOptionViewItem &option, QBitArray *drawn, int
//      firstVisualRow, int lastVisualRow, int firstVisualColumn, int
//      lastVisualColumn)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate16drawAndClipSpansERK7QRegionP8QPainterRK20QStyleOptionViewItemP9QBitArrayiiii(
    QTableViewPrivate *self,
    const QRegion *area,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    QBitArray *drawn,
    int firstVisualRow,
    int lastVisualRow,
    int firstVisualColumn,
    int lastVisualColumn) {
  self->drawAndClipSpans(
      *area,
      painter,
      *option,
      drawn,
      firstVisualRow,
      lastVisualRow,
      firstVisualColumn,
      lastVisualColumn);
}

//  void QTableViewPrivate::drawCell(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate8drawCellEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    QTableViewPrivate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->drawCell(painter, *option, *index);
}

//  int QTableViewPrivate::widthHintForIndex(const QModelIndex &index, int
//      hint, const QStyleOptionViewItem &option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate17widthHintForIndexERK11QModelIndexiRK20QStyleOptionViewItem(
    const QTableViewPrivate *self,
    const QModelIndex *index,
    int hint,
    const QStyleOptionViewItem *option) {
  return self->widthHintForIndex(*index, hint, *option);
}

//  int QTableViewPrivate::heightHintForIndex(const QModelIndex &index, int
//      hint, QStyleOptionViewItem &option) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate18heightHintForIndexERK11QModelIndexiR20QStyleOptionViewItem(
    const QTableViewPrivate *self,
    const QModelIndex *index,
    int hint,
    QStyleOptionViewItem *option) {
  return self->heightHintForIndex(*index, hint, *option);
}

//  void QTableViewPrivate::setSpan(int row, int column, int rowSpan, int
//      columnSpan)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate7setSpanEiiii(
    QTableViewPrivate *self,
    int row,
    int column,
    int rowSpan,
    int columnSpan) {
  self->setSpan(row, column, rowSpan, columnSpan);
}

//  QSpanCollection::Span QTableViewPrivate::span(int row, int column) const
extern "C" Q_DECL_EXPORT
QSpanCollection::Span *ritual_ZNK17QTableViewPrivate4spanEii(
    const QTableViewPrivate *self,
    int row,
    int column) {
  return new QSpanCollection::Span(self->span(row, column));
}

//  int QTableViewPrivate::rowSpan(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate7rowSpanEii(
    const QTableViewPrivate *self,
    int row,
    int column) {
  return self->rowSpan(row, column);
}

//  int QTableViewPrivate::columnSpan(int row, int column) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate10columnSpanEii(
    const QTableViewPrivate *self,
    int row,
    int column) {
  return self->columnSpan(row, column);
}

//  bool QTableViewPrivate::hasSpans() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate8hasSpansEv(
    const QTableViewPrivate *self) {
  return self->hasSpans();
}

//  int QTableViewPrivate::rowSpanHeight(int row, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate13rowSpanHeightEii(
    const QTableViewPrivate *self,
    int row,
    int span) {
  return self->rowSpanHeight(row, span);
}

//  int QTableViewPrivate::columnSpanWidth(int column, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate15columnSpanWidthEii(
    const QTableViewPrivate *self,
    int column,
    int span) {
  return self->columnSpanWidth(column, span);
}

//  int QTableViewPrivate::rowSpanEndLogical(int row, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate17rowSpanEndLogicalEii(
    const QTableViewPrivate *self,
    int row,
    int span) {
  return self->rowSpanEndLogical(row, span);
}

//  int QTableViewPrivate::columnSpanEndLogical(int column, int span) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate20columnSpanEndLogicalEii(
    const QTableViewPrivate *self,
    int column,
    int span) {
  return self->columnSpanEndLogical(column, span);
}

//  bool QTableViewPrivate::isRowHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate11isRowHiddenEi(
    const QTableViewPrivate *self,
    int row) {
  return self->isRowHidden(row);
}

//  bool QTableViewPrivate::isColumnHidden(int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate14isColumnHiddenEi(
    const QTableViewPrivate *self,
    int column) {
  return self->isColumnHidden(column);
}

//  bool QTableViewPrivate::isCellEnabled(int row, int column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QTableViewPrivate13isCellEnabledEii(
    const QTableViewPrivate *self,
    int row,
    int column) {
  return self->isCellEnabled(row, column);
}

//  int QTableViewPrivate::nextActiveVisualRow(int rowToStart, int column,
//      int limit, SearchDirection searchDirection) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate19nextActiveVisualRowEiiiNS_15SearchDirectionE(
    const QTableViewPrivate *self,
    int rowToStart,
    int column,
    int limit,
    QTableViewPrivate::SearchDirection searchDirection) {
  return self->nextActiveVisualRow(
      rowToStart,
      column,
      limit,
      searchDirection);
}

//  int QTableViewPrivate::nextActiveVisualColumn(int row, int columnToStart,
//      int limit, SearchDirection searchDirection) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK17QTableViewPrivate22nextActiveVisualColumnEiiiNS_15SearchDirectionE(
    const QTableViewPrivate *self,
    int row,
    int columnToStart,
    int limit,
    QTableViewPrivate::SearchDirection searchDirection) {
  return self->nextActiveVisualColumn(
      row,
      columnToStart,
      limit,
      searchDirection);
}

//  QRect QTableViewPrivate::visualSpanRect(const QSpanCollection::Span
//      &span) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK17QTableViewPrivate14visualSpanRectERKN15QSpanCollection4SpanE(
    const QTableViewPrivate *self,
    const QSpanCollection::Span *span) {
  return new QRect(self->visualSpanRect(*span));
}

//  void QTableViewPrivate::selectRow(int row, bool anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate9selectRowEib(
    QTableViewPrivate *self,
    int row,
    bool anchor) {
  self->selectRow(row, anchor);
}

//  void QTableViewPrivate::selectColumn(int column, bool anchor)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate12selectColumnEib(
    QTableViewPrivate *self,
    int column,
    bool anchor) {
  self->selectColumn(column, anchor);
}

//  void QTableViewPrivate::updateSpanInsertedRows(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate22updateSpanInsertedRowsERK11QModelIndexii(
    QTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->updateSpanInsertedRows(*parent, start, end);
}

//  void QTableViewPrivate::updateSpanInsertedColumns(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate25updateSpanInsertedColumnsERK11QModelIndexii(
    QTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->updateSpanInsertedColumns(*parent, start, end);
}

//  void QTableViewPrivate::updateSpanRemovedRows(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate21updateSpanRemovedRowsERK11QModelIndexii(
    QTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->updateSpanRemovedRows(*parent, start, end);
}

//  void QTableViewPrivate::updateSpanRemovedColumns(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate24updateSpanRemovedColumnsERK11QModelIndexii(
    QTableViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->updateSpanRemovedColumns(*parent, start, end);
}

//  void QTableViewPrivate::sortIndicatorChanged(int column, Qt::SortOrder
//      order)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QTableViewPrivate20sortIndicatorChangedEiN2Qt9SortOrderE(
    QTableViewPrivate *self,
    int column,
    Qt::SortOrder order) {
  self->sortIndicatorChanged(column, order);
}

//  a Python function taken by a CuteQTableViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTableViewPrivate(
    QTableViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTableViewPrivate *>(self)->take(key, call);
}

//  QRect QTableViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK17QTableViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QTableViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(
      self->QTableViewPrivate::intersectedRect(
          *rect,
          *topLeft,
          *bottomRight));
}

#if QT_CONFIG(accessibility)
//  int QTableViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK17QTableViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QTableViewPrivate *self,
    const QModelIndex *index) {
  return self->QTableViewPrivate::accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(tableview)
#endif  // QT_CONFIG(tableview)
