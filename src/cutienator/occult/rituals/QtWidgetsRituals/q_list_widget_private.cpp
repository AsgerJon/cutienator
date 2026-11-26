//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listwidget)
#if QT_CONFIG(listwidget)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistwidget_p.h>
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
#include <QtWidgets/qlistwidget.h>
#include <QtWidgets/private/qlistview_p.h>
#include <QtWidgets/private/qwidgetitemdata_p.h>
#include <QtWidgets/private/qlistwidget_p.h>
#include <algorithm>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

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

//  from src/widgets/itemviews/qlistview.cpp, line 1728, as _ZN16QListViewPrivateC2Ev
inline QListViewPrivate::QListViewPrivate()
    : QAbstractItemViewPrivate(),
      commonListView(nullptr),
      wrap(false),
      space(0),
      flow(QListView::TopToBottom),
      movement(QListView::Static),
      resizeMode(QListView::Fixed),
      layoutMode(QListView::SinglePass),
      viewMode(QListView::ListMode),
      modeProperties(0),
      column(0),
      uniformItemSizes(false),
      batchSize(100),
      showElasticBand(false),
      itemAlignment(Qt::Alignment())
{
}

//  from src/widgets/itemviews/qlistview.cpp, line 1747, as _ZN16QListViewPrivateD2Ev
inline QListViewPrivate::~QListViewPrivate()
{
    delete commonListView;
}

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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 3781, as _ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i
inline void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &, int, int, const QModelIndex &, int)
{
    layoutChanged();
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

//  from src/widgets/itemviews/qlistview.cpp, line 1942, as _ZNK16QListViewPrivate20accessibleChildIndexERK11QModelIndex
#if QT_CONFIG(accessibility)
inline int QListViewPrivate::accessibleChildIndex(const QModelIndex &index) const
{
    Q_Q(const QListView);
    Q_ASSERT(index.isValid());
    return q->visualIndex(index);
}
#endif  // QT_CONFIG(accessibility)

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

//  from src/widgets/itemviews/qlistwidget.cpp, line 338, as _ZN10QListModel12ensureSortedEiN2Qt9SortOrderEii
inline void QListModel::ensureSorted(int column, Qt::SortOrder order, int start, int end)
{
    if (column != 0)
        return;

    const auto compareLt = [](const QListWidgetItem *left, const QListWidgetItem *right) -> bool {
        return *left < *right;
    };

    const auto compareGt = [](const QListWidgetItem *left, const QListWidgetItem *right) -> bool {
        return *right < *left;
    };

    /** Check if range [start,end] is already in sorted position in list.
     *  Take for this the assumption, that outside [start,end] the list
     *  is already sorted. Therefore the sorted check has to be extended
     *  to the first element that is known to be sorted before the range
     *  [start, end], which is (start-1) and the first element after the
     *  range [start, end], which is (end+2) due to end being included.
    */
    const auto beginChangedIterator = items.constBegin() + qMax(start - 1, 0);
    const auto endChangedIterator = items.constBegin() + qMin(end + 2, items.size());
    const bool needsSorting = !std::is_sorted(beginChangedIterator, endChangedIterator,
                                              order == Qt::AscendingOrder ? compareLt : compareGt);

    if (needsSorting)
        sort(column, order);
}

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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4458, as _ZN24QAbstractItemViewPrivate14updateGeometryEv
inline void QAbstractItemViewPrivate::updateGeometry()
{
    Q_Q(QAbstractItemView);
    if (sizeAdjustPolicy == QAbstractScrollArea::AdjustIgnored)
        return;
    if (sizeAdjustPolicy == QAbstractScrollArea::AdjustToContents || !shownOnce)
        q->updateGeometry();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4444, as _ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi
inline void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
{
    if (!delayedPendingLayout) {
        delayedPendingLayout = true;
        delayedLayout.start(delay, q_func());
    }
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 1104, as _ZN18QListWidgetPrivate16clearConnectionsEv
inline void QListWidgetPrivate::clearConnections()
{
    for (QMetaObject::Connection &connection : connections)
        QObject::disconnect(connection);
    for (QMetaObject::Connection &connection : selectionModelConnections)
        QObject::disconnect(connection);
}

//  from src/widgets/itemviews/qlistwidget.cpp, line 1166, as _ZN18QListWidgetPrivate4sortEv
inline void QListWidgetPrivate::sort()
{
    if (sortingEnabled)
        model->sort(0, sortOrder);
}
//  -----------------------------------------------------------------------

//  A QListWidgetPrivate that Python can take functions over in. Every QListWidgetPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef bool (*CuteQListWidgetPrivateCall0)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(listview)
typedef void (*CuteQListWidgetPrivateCall1)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(listview)
typedef int (*CuteQListWidgetPrivateCall2)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall5)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall6)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall7)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall8)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall9)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall10)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall11)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQListWidgetPrivateCall12)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQListWidgetPrivateCall13)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQListWidgetPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQListWidgetPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQListWidgetPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQListWidgetPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQListWidgetPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQListWidgetPrivateCall19)(const void *, int, int *);
typedef void (*CuteQListWidgetPrivateCall20)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall21)(const void *, int *);
typedef void * (*CuteQListWidgetPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQListWidgetPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQListWidgetPrivateCall24)(const void *, int *);
typedef int (*CuteQListWidgetPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQListWidgetPrivateCall26)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall27)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall28)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall29)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall30)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall31)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall32)(const void *, int *);
typedef void (*CuteQListWidgetPrivateCall33)(const void *, int *);
typedef bool (*CuteQListWidgetPrivateCall34)(const void *, int *);
typedef bool (*CuteQListWidgetPrivateCall35)(const void *, int *);
class CuteQListWidgetPrivate : public QListWidgetPrivate {
public:
  using QListWidgetPrivate::QListWidgetPrivate;
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
      CuteQListWidgetPrivateCall0 call = reinterpret_cast<CuteQListWidgetPrivateCall0>(taken[0]);
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
      CuteQListWidgetPrivateCall1 call = reinterpret_cast<CuteQListWidgetPrivateCall1>(taken[1]);
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
      CuteQListWidgetPrivateCall2 call = reinterpret_cast<CuteQListWidgetPrivateCall2>(taken[2]);
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
      CuteQListWidgetPrivateCall3 call = reinterpret_cast<CuteQListWidgetPrivateCall3>(taken[3]);
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
      CuteQListWidgetPrivateCall4 call = reinterpret_cast<CuteQListWidgetPrivateCall4>(taken[4]);
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
      CuteQListWidgetPrivateCall5 call = reinterpret_cast<CuteQListWidgetPrivateCall5>(taken[5]);
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
      CuteQListWidgetPrivateCall6 call = reinterpret_cast<CuteQListWidgetPrivateCall6>(taken[6]);
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
      CuteQListWidgetPrivateCall7 call = reinterpret_cast<CuteQListWidgetPrivateCall7>(taken[7]);
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
      CuteQListWidgetPrivateCall8 call = reinterpret_cast<CuteQListWidgetPrivateCall8>(taken[8]);
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
      CuteQListWidgetPrivateCall9 call = reinterpret_cast<CuteQListWidgetPrivateCall9>(taken[9]);
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
      CuteQListWidgetPrivateCall10 call = reinterpret_cast<CuteQListWidgetPrivateCall10>(taken[10]);
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
      CuteQListWidgetPrivateCall11 call = reinterpret_cast<CuteQListWidgetPrivateCall11>(taken[11]);
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
      CuteQListWidgetPrivateCall12 call = reinterpret_cast<CuteQListWidgetPrivateCall12>(taken[12]);
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
      CuteQListWidgetPrivateCall13 call = reinterpret_cast<CuteQListWidgetPrivateCall13>(taken[13]);
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
      CuteQListWidgetPrivateCall14 call = reinterpret_cast<CuteQListWidgetPrivateCall14>(taken[14]);
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
      CuteQListWidgetPrivateCall15 call = reinterpret_cast<CuteQListWidgetPrivateCall15>(taken[15]);
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
      CuteQListWidgetPrivateCall16 call = reinterpret_cast<CuteQListWidgetPrivateCall16>(taken[16]);
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
      CuteQListWidgetPrivateCall17 call = reinterpret_cast<CuteQListWidgetPrivateCall17>(taken[17]);
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
      CuteQListWidgetPrivateCall18 call = reinterpret_cast<CuteQListWidgetPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQListWidgetPrivateCall19 call = reinterpret_cast<CuteQListWidgetPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQListWidgetPrivateCall20 call = reinterpret_cast<CuteQListWidgetPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQListWidgetPrivateCall21 call = reinterpret_cast<CuteQListWidgetPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQListWidgetPrivateCall22 call = reinterpret_cast<CuteQListWidgetPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQListWidgetPrivateCall23 call = reinterpret_cast<CuteQListWidgetPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQListWidgetPrivateCall24 call = reinterpret_cast<CuteQListWidgetPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQListWidgetPrivateCall25 call = reinterpret_cast<CuteQListWidgetPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQListWidgetPrivateCall26 call = reinterpret_cast<CuteQListWidgetPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQListWidgetPrivateCall27 call = reinterpret_cast<CuteQListWidgetPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQListWidgetPrivateCall28 call = reinterpret_cast<CuteQListWidgetPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQListWidgetPrivateCall29 call = reinterpret_cast<CuteQListWidgetPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQListWidgetPrivateCall30 call = reinterpret_cast<CuteQListWidgetPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQListWidgetPrivateCall31 call = reinterpret_cast<CuteQListWidgetPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQListWidgetPrivateCall32 call = reinterpret_cast<CuteQListWidgetPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQListWidgetPrivateCall33 call = reinterpret_cast<CuteQListWidgetPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQListWidgetPrivateCall34 call = reinterpret_cast<CuteQListWidgetPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQListWidgetPrivateCall35 call = reinterpret_cast<CuteQListWidgetPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QListWidget *QListWidgetPrivate::q_func()
extern "C" Q_DECL_EXPORT
QListWidget *ritual_ZN18QListWidgetPrivate6q_funcEv(
    QListWidgetPrivate *self) {
  return self->q_func();
}

//  const QListWidget *QListWidgetPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QListWidget *ritual_ZNK18QListWidgetPrivate6q_funcEv(
    const QListWidgetPrivate *self) {
  return self->q_func();
}

//  void QListWidgetPrivate::clearConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QListWidgetPrivate16clearConnectionsEv(
    QListWidgetPrivate *self) {
  self->clearConnections();
}

//  void QListWidgetPrivate::sort()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QListWidgetPrivate4sortEv(QListWidgetPrivate *self) {
  self->sort();
}

//  a Python function taken by a CuteQListWidgetPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QListWidgetPrivate(
    QListWidgetPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQListWidgetPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(listwidget)
#endif  // QT_CONFIG(listwidget)
