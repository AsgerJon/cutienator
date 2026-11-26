//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qcolumnview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h>
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
#include <QtCore/qglobal.h>
#include <QtWidgets/qcolumnview.h>
#if QT_CONFIG(columnview)
#include <QtWidgets/private/qcolumnview_p.h>
#include <QtWidgets/private/qcolumnviewgrip_p.h>
#include <QtWidgets/qlistview.h>
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtWidgets/qscrollbar.h>
#include <QtGui/qpainter.h>
#include <QtCore/qdebug.h>
#endif
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
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/itemviews/qcolumnview.cpp, line 1095, as _ZN18QColumnViewPrivate15columnsInsertedERK11QModelIndexii
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::columnsInserted(const QModelIndex &parent, int start, int end)
{
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
    checkColumnCreation(parent);
}
#endif  // QT_CONFIG(columnview)

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

//  from src/widgets/itemviews/qcolumnview.cpp, line 1107, as _ZN18QColumnViewPrivate19checkColumnCreationERK11QModelIndex
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::checkColumnCreation(const QModelIndex &parent)
{
    if (parent == q_func()->currentIndex() && model->hasChildren(parent)) {
        //the parent has children and is the current
        //let's try to find out if there is already a mapping that is good
        for (int i = 0; i < columns.size(); ++i) {
            QAbstractItemView *view = columns.at(i);
            if (view->rootIndex() == parent) {
                if (view == previewColumn) {
                    //let's recreate the parent
                    closeColumns(parent, false);
                    createColumn(parent, true /*show*/);
                }
                break;
            }
        }
    }
}
#endif  // QT_CONFIG(columnview)

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

//  from src/widgets/itemviews/qcolumnview.cpp, line 564, as _ZN18QColumnViewPrivate12closeColumnsERK11QModelIndexb
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::closeColumns(const QModelIndex &parent, bool build)
{
    if (columns.isEmpty())
        return;

    bool clearAll = !parent.isValid();
    bool passThroughRoot = false;

    QList<QModelIndex> dirsToAppend;

    // Find the last column that matches the parent's tree
    int currentColumn = -1;
    QModelIndex parentIndex = parent;
    while (currentColumn == -1 && parentIndex.isValid()) {
        if (columns.isEmpty())
            break;
        parentIndex = parentIndex.parent();
        if (root == parentIndex)
            passThroughRoot = true;
        if (!parentIndex.isValid())
            break;
        for (int i = columns.size() - 1; i >= 0; --i) {
            if (columns.at(i)->rootIndex() == parentIndex) {
                currentColumn = i;
                break;
            }
        }
        if (currentColumn == -1)
            dirsToAppend.append(parentIndex);
    }

    // Someone wants to go to an index that can be reached without changing
    // the root index, don't allow them
    if (!clearAll && !passThroughRoot && currentColumn == -1)
        return;

    if (currentColumn == -1 && parent.isValid())
        currentColumn = 0;

    // Optimization so we don't go deleting and then creating the same thing
    bool alreadyExists = false;
    if (build && columns.size() > currentColumn + 1) {
        bool viewingParent = (columns.at(currentColumn + 1)->rootIndex() == parent);
        bool viewingChild = (!model->hasChildren(parent)
                             && !columns.at(currentColumn + 1)->rootIndex().isValid());
        if (viewingParent || viewingChild) {
            currentColumn++;
            alreadyExists = true;
        }
    }

    // Delete columns that don't match our path
    for (int i = columns.size() - 1; i > currentColumn; --i) {
        QAbstractItemView* notShownAnymore = columns.at(i);
        columns.removeAt(i);
        notShownAnymore->setVisible(false);
        if (notShownAnymore != previewColumn) {
            notShownAnymore->deleteLater();
            disconnectView(notShownAnymore);
        }
    }

    if (columns.isEmpty()) {
        offset = 0;
        updateScrollbars();
    }

    // Now fill in missing columns
    while (!dirsToAppend.isEmpty()) {
        QAbstractItemView *newView = createColumn(dirsToAppend.takeLast(), true);
        if (!dirsToAppend.isEmpty())
            newView->setCurrentIndex(dirsToAppend.constLast());
    }

    if (build && !alreadyExists)
        createColumn(parent, false);
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 681, as _ZN18QColumnViewPrivate12createColumnERK11QModelIndexb
#if QT_CONFIG(columnview)
inline QAbstractItemView *QColumnViewPrivate::createColumn(const QModelIndex &index, bool show)
{
    Q_Q(QColumnView);
    QAbstractItemView *view = nullptr;
    QMetaObject::Connection clickedConnection;
    if (model->hasChildren(index)) {
        view = q->createColumn(index);
        clickedConnection = QObjectPrivate::connect(view, &QAbstractItemView::clicked,
                                                    this, &QColumnViewPrivate::clicked);
    } else {
        if (!previewColumn)
            previewColumn = createPreviewColumn();
        view = previewColumn;
        if (previewWidget)
            view->setMinimumWidth(qMax(view->minimumWidth(), previewWidget->minimumWidth()));
    }

    viewConnections[view] = {
        QObject::connect(view, &QAbstractItemView::activated, q, &QColumnView::activated),
        QObject::connect(view, &QAbstractItemView::clicked, q, &QColumnView::clicked),
        QObject::connect(view, &QAbstractItemView::doubleClicked, q, &QColumnView::doubleClicked),
        QObject::connect(view, &QAbstractItemView::entered, q, &QColumnView::entered),
        QObject::connect(view, &QAbstractItemView::pressed, q, &QColumnView::pressed),
        std::move(clickedConnection),
    };

    view->setFocusPolicy(Qt::NoFocus);
    view->setParent(viewport);
    Q_ASSERT(view);

    // Setup corner grip
    if (showResizeGrips) {
        QColumnViewGrip *grip = new QColumnViewGrip(view);
        view->setCornerWidget(grip);
        gripConnections.push_back(
            QObjectPrivate::connect(grip, &QColumnViewGrip::gripMoved,
                                    this, &QColumnViewPrivate::gripMoved)
        );
    }

    if (columnSizes.size() > columns.size()) {
        view->setGeometry(0, 0, columnSizes.at(columns.size()), viewport->height());
    } else {
        int initialWidth = view->sizeHint().width();
        if (q->isRightToLeft())
            view->setGeometry(viewport->width() - initialWidth, 0, initialWidth, viewport->height());
        else
            view->setGeometry(0, 0, initialWidth, viewport->height());
        columnSizes.resize(qMax(columnSizes.size(), columns.size() + 1));
        columnSizes[columns.size()] = initialWidth;
    }
    if (!columns.isEmpty() && columns.constLast()->isHidden())
        columns.constLast()->setVisible(true);

    columns.append(view);
    doLayout();
    updateScrollbars();
    if (show && view->isHidden() && view != previewColumn)
        view->setVisible(true);
    if (view == previewColumn)
        view->setVisible(showPreviewColumn);
    return view;
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 1087, as _ZN18QColumnViewPrivateD1Ev
#if QT_CONFIG(columnview)
inline QColumnViewPrivate::~QColumnViewPrivate()
{
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 405, as _ZN18QColumnViewPrivate16updateScrollbarsEv
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::updateScrollbars()
{
    Q_Q(QColumnView);
#if QT_CONFIG(animation)
    if (currentAnimation.state() == QPropertyAnimation::Running)
        return;
#endif // animation

    // find the total horizontal length of the laid out columns
    int horizontalLength = 0;
    if (!columns.isEmpty()) {
        horizontalLength = (columns.constLast()->x() + columns.constLast()->width()) - columns.constFirst()->x();
        if (horizontalLength <= 0) // reverse mode
            horizontalLength = (columns.constFirst()->x() + columns.constFirst()->width()) - columns.constLast()->x();
    }

    QSize viewportSize = viewport->size();
    if (horizontalLength < viewportSize.width() && hbar->value() == 0) {
        hbar->setRange(0, 0);
    } else {
        int visibleLength = qMin(horizontalLength + q->horizontalOffset(), viewportSize.width());
        int hiddenLength = horizontalLength - visibleLength;
        if (hiddenLength != hbar->maximum())
            hbar->setRange(0, hiddenLength);
    }
    if (!columns.isEmpty()) {
        int pageStepSize = columns.at(0)->width();
        if (pageStepSize != hbar->pageStep())
            hbar->setPageStep(pageStepSize);
    }
    bool visible = (hbar->maximum() > 0);
    if (visible != hbar->isVisible())
        hbar->setVisible(visible);
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 642, as _ZN18QColumnViewPrivate14disconnectViewEP17QAbstractItemView
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::disconnectView(QAbstractItemView *view)
{
    const auto it = viewConnections.find(view);
    if (it == viewConnections.end())
        return;
    for (QMetaObject::Connection &connection : it.value())
        QObject::disconnect(connection);
    viewConnections.erase(it);
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 1130, as _ZN18QColumnViewPrivate8doLayoutEv
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::doLayout()
{
    Q_Q(QColumnView);
    if (!model || columns.isEmpty())
        return;

    int viewportHeight = viewport->height();
    int x = columns.at(0)->x();

    if (q->isRightToLeft()) {
        x = viewport->width() + q->horizontalOffset();
        for (int i = 0; i < columns.size(); ++i) {
            QAbstractItemView *view = columns.at(i);
            x -= view->width();
            if (x != view->x() || viewportHeight != view->height())
                view->setGeometry(x, 0, view->width(), viewportHeight);
        }
    } else {
        for (int i = 0; i < columns.size(); ++i) {
            QAbstractItemView *view = columns.at(i);
            int currentColumnWidth = view->width();
            if (x != view->x() || viewportHeight != view->height())
                view->setGeometry(x, 0, currentColumnWidth, viewportHeight);
            x += currentColumnWidth;
        }
    }
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 851, as _ZN18QColumnViewPrivate16setPreviewWidgetEP7QWidget
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::setPreviewWidget(QWidget *widget)
{
    QColumnViewPreviewColumn *column = createPreviewColumn();
    previewColumn = column;
    column->setPreviewWidget(widget);
    previewWidget = widget;
    if (previewWidget)
        previewWidget->setParent(column->viewport());
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 864, as _ZN18QColumnViewPrivate19createPreviewColumnEv
#if QT_CONFIG(columnview)
inline QColumnViewPreviewColumn *QColumnViewPrivate::createPreviewColumn()
{
    Q_Q(QColumnView);
    if (previewColumn) {
        if (!columns.isEmpty() && columns.constLast() == previewColumn)
            columns.removeLast();
        previewColumn->deleteLater();
    }
    QColumnViewPreviewColumn *column = new QColumnViewPreviewColumn(q);
    column->hide();
    column->setFrameShape(QFrame::NoFrame);
    column->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);
    column->setSelectionMode(QAbstractItemView::NoSelection);
    column->setMinimumWidth(qMax(column->verticalScrollBar()->width(),
                                 column->minimumWidth()));
    column->setPreviewWidget(nullptr);
    return column;
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 528, as _ZN18QColumnViewPrivate9gripMovedEi
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::gripMoved(int offset)
{
    Q_Q(QColumnView);

    QObject *grip = q->sender();
    Q_ASSERT(grip);

    if (q->isRightToLeft())
        offset = -1 * offset;

    bool found = false;
    for (int i = 0; i < columns.size(); ++i) {
        if (!found && columns.at(i)->cornerWidget() == grip) {
            found = true;
            columnSizes[i] = columns.at(i)->width();
            if (q->isRightToLeft())
                columns.at(i)->move(columns.at(i)->x() + offset, 0);
            continue;
        }
        if (!found)
            continue;

        int currentX = columns.at(i)->x();
        columns.at(i)->move(currentX + offset, 0);
    }

    updateScrollbars();
}
#endif  // QT_CONFIG(columnview)

//  from src/widgets/itemviews/qcolumnview.cpp, line 652, as _ZN18QColumnViewPrivate7clickedERK11QModelIndex
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::clicked(const QModelIndex &index)
{
    Q_Q(QColumnView);
    QModelIndex parent = index.parent();
    QAbstractItemView *columnClicked = nullptr;
    for (int column = 0; column < columns.size(); ++column) {
        if (columns.at(column)->rootIndex() == parent) {
            columnClicked = columns[column];
            break;
        }
    }
    if (q->selectionModel() && columnClicked) {
        QItemSelectionModel::SelectionFlags flags = QItemSelectionModel::Current;
        if (columnClicked->selectionModel()->isSelected(index))
            flags |= QItemSelectionModel::Select;
        q->selectionModel()->setCurrentIndex(index, flags);
    }
}
#endif  // QT_CONFIG(columnview)
//  -----------------------------------------------------------------------

//  A QColumnViewPrivate that Python can take functions over in. Every QColumnViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(columnview)
typedef void (*CuteQColumnViewPrivateCall0)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall7)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQColumnViewPrivateCall9)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall10)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQColumnViewPrivateCall11)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQColumnViewPrivateCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
typedef int (*CuteQColumnViewPrivateCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQColumnViewPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQColumnViewPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQColumnViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQColumnViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQColumnViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQColumnViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQColumnViewPrivateCall20)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQColumnViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQColumnViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQColumnViewPrivateCall24)(const void *, int *);
typedef int (*CuteQColumnViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQColumnViewPrivateCall26)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall27)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall28)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall29)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall30)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall31)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall32)(const void *, int *);
typedef void (*CuteQColumnViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQColumnViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQColumnViewPrivateCall35)(const void *, int *);
class CuteQColumnViewPrivate : public QColumnViewPrivate {
public:
  using QColumnViewPrivate::QColumnViewPrivate;
  void *taken[36] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(itemviews)
#if QT_CONFIG(columnview)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
    if (!std::strcmp(key, "_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii")) {
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
#if QT_CONFIG(columnview)
  //  void QColumnViewPrivate::columnsInserted(const QModelIndex &parent,
  //      int start, int end)
  void columnsInserted(
      const QModelIndex &parent,
      int start,
      int end) override {
    if (taken[0]) {
      int handled = 0;
      CuteQColumnViewPrivateCall0 call = reinterpret_cast<CuteQColumnViewPrivateCall0>(taken[0]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QColumnViewPrivate::columnsInserted(parent, start, end);
  }
#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent,
  //      int start, int end)
  void rowsRemoved(const QModelIndex &parent, int start, int end) override {
    if (taken[1]) {
      int handled = 0;
      CuteQColumnViewPrivateCall1 call = reinterpret_cast<CuteQColumnViewPrivateCall1>(taken[1]);
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
    if (taken[2]) {
      int handled = 0;
      CuteQColumnViewPrivateCall2 call = reinterpret_cast<CuteQColumnViewPrivateCall2>(taken[2]);
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
    if (taken[3]) {
      int handled = 0;
      CuteQColumnViewPrivateCall3 call = reinterpret_cast<CuteQColumnViewPrivateCall3>(taken[3]);
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
    if (taken[4]) {
      int handled = 0;
      CuteQColumnViewPrivateCall4 call = reinterpret_cast<CuteQColumnViewPrivateCall4>(taken[4]);
      call(this, &parent, start, end, &handled);
      if (handled) return;
    }
    QAbstractItemViewPrivate::columnsRemoved(parent, start, end);
  }
#endif  // QT_CONFIG(itemviews)

#if QT_CONFIG(itemviews)
  //  void QAbstractItemViewPrivate::modelDestroyed()
  void modelDestroyed() override {
    if (taken[5]) {
      int handled = 0;
      CuteQColumnViewPrivateCall5 call = reinterpret_cast<CuteQColumnViewPrivateCall5>(taken[5]);
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
      CuteQColumnViewPrivateCall6 call = reinterpret_cast<CuteQColumnViewPrivateCall6>(taken[6]);
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
      CuteQColumnViewPrivateCall7 call = reinterpret_cast<CuteQColumnViewPrivateCall7>(taken[7]);
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
      CuteQColumnViewPrivateCall8 call = reinterpret_cast<CuteQColumnViewPrivateCall8>(taken[8]);
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
      CuteQColumnViewPrivateCall9 call = reinterpret_cast<CuteQColumnViewPrivateCall9>(taken[9]);
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
      CuteQColumnViewPrivateCall10 call = reinterpret_cast<CuteQColumnViewPrivateCall10>(taken[10]);
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
      CuteQColumnViewPrivateCall11 call = reinterpret_cast<CuteQColumnViewPrivateCall11>(taken[11]);
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
      CuteQColumnViewPrivateCall12 call = reinterpret_cast<CuteQColumnViewPrivateCall12>(taken[12]);
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
      CuteQColumnViewPrivateCall13 call = reinterpret_cast<CuteQColumnViewPrivateCall13>(taken[13]);
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
      CuteQColumnViewPrivateCall14 call = reinterpret_cast<CuteQColumnViewPrivateCall14>(taken[14]);
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
      CuteQColumnViewPrivateCall15 call = reinterpret_cast<CuteQColumnViewPrivateCall15>(taken[15]);
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
      CuteQColumnViewPrivateCall16 call = reinterpret_cast<CuteQColumnViewPrivateCall16>(taken[16]);
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
      CuteQColumnViewPrivateCall17 call = reinterpret_cast<CuteQColumnViewPrivateCall17>(taken[17]);
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
      CuteQColumnViewPrivateCall18 call = reinterpret_cast<CuteQColumnViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQColumnViewPrivateCall19 call = reinterpret_cast<CuteQColumnViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQColumnViewPrivateCall20 call = reinterpret_cast<CuteQColumnViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQColumnViewPrivateCall21 call = reinterpret_cast<CuteQColumnViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQColumnViewPrivateCall22 call = reinterpret_cast<CuteQColumnViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQColumnViewPrivateCall23 call = reinterpret_cast<CuteQColumnViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQColumnViewPrivateCall24 call = reinterpret_cast<CuteQColumnViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQColumnViewPrivateCall25 call = reinterpret_cast<CuteQColumnViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQColumnViewPrivateCall26 call = reinterpret_cast<CuteQColumnViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQColumnViewPrivateCall27 call = reinterpret_cast<CuteQColumnViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQColumnViewPrivateCall28 call = reinterpret_cast<CuteQColumnViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQColumnViewPrivateCall29 call = reinterpret_cast<CuteQColumnViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQColumnViewPrivateCall30 call = reinterpret_cast<CuteQColumnViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQColumnViewPrivateCall31 call = reinterpret_cast<CuteQColumnViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQColumnViewPrivateCall32 call = reinterpret_cast<CuteQColumnViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQColumnViewPrivateCall33 call = reinterpret_cast<CuteQColumnViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQColumnViewPrivateCall34 call = reinterpret_cast<CuteQColumnViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQColumnViewPrivateCall35 call = reinterpret_cast<CuteQColumnViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QColumnView *QColumnViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QColumnView *ritual_ZN18QColumnViewPrivate6q_funcEv(
    QColumnViewPrivate *self) {
  return self->q_func();
}

//  const QColumnView *QColumnViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QColumnView *ritual_ZNK18QColumnViewPrivate6q_funcEv(
    const QColumnViewPrivate *self) {
  return self->q_func();
}

//  QColumnViewPrivate::~QColumnViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivateD1Ev(QColumnViewPrivate *self) {
  delete self;
}

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::updateScrollbars()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate16updateScrollbarsEv(
    QColumnViewPrivate *self) {
  self->updateScrollbars();
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::disconnectView(QAbstractItemView *view)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate14disconnectViewEP17QAbstractItemView(
    QColumnViewPrivate *self,
    QAbstractItemView *view) {
  self->disconnectView(view);
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::doLayout()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate8doLayoutEv(QColumnViewPrivate *self) {
  self->doLayout();
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::setPreviewWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate16setPreviewWidgetEP7QWidget(
    QColumnViewPrivate *self,
    QWidget *widget) {
  self->setPreviewWidget(widget);
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  QColumnViewPreviewColumn *QColumnViewPrivate::createPreviewColumn()
extern "C" Q_DECL_EXPORT
QColumnViewPreviewColumn *ritual_ZN18QColumnViewPrivate19createPreviewColumnEv(
    QColumnViewPrivate *self) {
  return self->createPreviewColumn();
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::gripMoved(int offset)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate9gripMovedEi(
    QColumnViewPrivate *self,
    int offset) {
  self->gripMoved(offset);
}
#endif  // QT_CONFIG(columnview)

#if QT_CONFIG(columnview)
//  void QColumnViewPrivate::clicked(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate7clickedERK11QModelIndex(
    QColumnViewPrivate *self,
    const QModelIndex *index) {
  self->clicked(*index);
}
#endif  // QT_CONFIG(columnview)

//  void QColumnViewPrivate::columnsInserted(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QColumnViewPrivate15columnsInsertedERK11QModelIndexii(
    QColumnViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsInserted(*parent, start, end);
}

//  a Python function taken by a CuteQColumnViewPrivate, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QColumnViewPrivate(
    QColumnViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQColumnViewPrivate *>(self)->take(key, call);
}

#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(columnview)
