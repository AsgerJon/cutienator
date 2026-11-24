//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(treeview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qtreeview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qtreeview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qpixmap.h>
#include <QtCore/qpoint.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/qpa/qplatformbackingstore.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qwidget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qimage.h>
#include <QtCore/qlist.h>
#include <cstring>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
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
//  -----------------------------------------------------------------------

//  A QTreeViewPrivate that Python can take functions over in. Every QTreeViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivateCall0)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef void (*CuteQTreeViewPrivateCall3)(const void *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeViewPrivateCall4)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(treeview)
typedef const QRect * (*CuteQTreeViewPrivateCall5)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
#if QT_CONFIG(treeview)
typedef int (*CuteQTreeViewPrivateCall6)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(treeview)
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall7)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall8)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall9)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall10)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall11)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall12)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQTreeViewPrivateCall13)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQTreeViewPrivateCall14)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQTreeViewPrivateCall15)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQTreeViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQTreeViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQTreeViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQTreeViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQTreeViewPrivateCall20)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQTreeViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQTreeViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQTreeViewPrivateCall24)(const void *, int *);
typedef int (*CuteQTreeViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQTreeViewPrivateCall26)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall27)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall28)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall29)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall30)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall31)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall32)(const void *, int *);
typedef void (*CuteQTreeViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQTreeViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQTreeViewPrivateCall35)(const void *, int *);
class CuteQTreeViewPrivate : public QTreeViewPrivate {
public:
  using QTreeViewPrivate::QTreeViewPrivate;
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
      CuteQTreeViewPrivateCall0 call = reinterpret_cast<CuteQTreeViewPrivateCall0>(taken[0]);
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
      CuteQTreeViewPrivateCall1 call = reinterpret_cast<CuteQTreeViewPrivateCall1>(taken[1]);
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
      CuteQTreeViewPrivateCall2 call = reinterpret_cast<CuteQTreeViewPrivateCall2>(taken[2]);
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
      CuteQTreeViewPrivateCall3 call = reinterpret_cast<CuteQTreeViewPrivateCall3>(taken[3]);
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
      CuteQTreeViewPrivateCall4 call = reinterpret_cast<CuteQTreeViewPrivateCall4>(taken[4]);
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
      CuteQTreeViewPrivateCall5 call = reinterpret_cast<CuteQTreeViewPrivateCall5>(taken[5]);
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
      CuteQTreeViewPrivateCall6 call = reinterpret_cast<CuteQTreeViewPrivateCall6>(taken[6]);
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
      CuteQTreeViewPrivateCall7 call = reinterpret_cast<CuteQTreeViewPrivateCall7>(taken[7]);
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
      CuteQTreeViewPrivateCall8 call = reinterpret_cast<CuteQTreeViewPrivateCall8>(taken[8]);
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
      CuteQTreeViewPrivateCall9 call = reinterpret_cast<CuteQTreeViewPrivateCall9>(taken[9]);
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
      CuteQTreeViewPrivateCall10 call = reinterpret_cast<CuteQTreeViewPrivateCall10>(taken[10]);
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
      CuteQTreeViewPrivateCall11 call = reinterpret_cast<CuteQTreeViewPrivateCall11>(taken[11]);
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
      CuteQTreeViewPrivateCall12 call = reinterpret_cast<CuteQTreeViewPrivateCall12>(taken[12]);
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
      CuteQTreeViewPrivateCall13 call = reinterpret_cast<CuteQTreeViewPrivateCall13>(taken[13]);
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
      CuteQTreeViewPrivateCall14 call = reinterpret_cast<CuteQTreeViewPrivateCall14>(taken[14]);
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
      CuteQTreeViewPrivateCall15 call = reinterpret_cast<CuteQTreeViewPrivateCall15>(taken[15]);
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
      CuteQTreeViewPrivateCall16 call = reinterpret_cast<CuteQTreeViewPrivateCall16>(taken[16]);
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
      CuteQTreeViewPrivateCall17 call = reinterpret_cast<CuteQTreeViewPrivateCall17>(taken[17]);
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
      CuteQTreeViewPrivateCall18 call = reinterpret_cast<CuteQTreeViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQTreeViewPrivateCall19 call = reinterpret_cast<CuteQTreeViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQTreeViewPrivateCall20 call = reinterpret_cast<CuteQTreeViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQTreeViewPrivateCall21 call = reinterpret_cast<CuteQTreeViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQTreeViewPrivateCall22 call = reinterpret_cast<CuteQTreeViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQTreeViewPrivateCall23 call = reinterpret_cast<CuteQTreeViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQTreeViewPrivateCall24 call = reinterpret_cast<CuteQTreeViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQTreeViewPrivateCall25 call = reinterpret_cast<CuteQTreeViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQTreeViewPrivateCall26 call = reinterpret_cast<CuteQTreeViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQTreeViewPrivateCall27 call = reinterpret_cast<CuteQTreeViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQTreeViewPrivateCall28 call = reinterpret_cast<CuteQTreeViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQTreeViewPrivateCall29 call = reinterpret_cast<CuteQTreeViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQTreeViewPrivateCall30 call = reinterpret_cast<CuteQTreeViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQTreeViewPrivateCall31 call = reinterpret_cast<CuteQTreeViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQTreeViewPrivateCall32 call = reinterpret_cast<CuteQTreeViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQTreeViewPrivateCall33 call = reinterpret_cast<CuteQTreeViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQTreeViewPrivateCall34 call = reinterpret_cast<CuteQTreeViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQTreeViewPrivateCall35 call = reinterpret_cast<CuteQTreeViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QTreeView *QTreeViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QTreeView *ritual_ZN16QTreeViewPrivate6q_funcEv(QTreeViewPrivate *self) {
  return self->q_func();
}

//  const QTreeView *QTreeViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QTreeView *ritual_ZNK16QTreeViewPrivate6q_funcEv(
    const QTreeViewPrivate *self) {
  return self->q_func();
}

//  QTreeViewPrivate::~QTreeViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivateD1Ev(QTreeViewPrivate *self) {
  delete self;
}

//  void QTreeViewPrivate::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate10initializeEv(QTreeViewPrivate *self) {
  self->initialize();
}

//  void QTreeViewPrivate::clearConnections()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate16clearConnectionsEv(
    QTreeViewPrivate *self) {
  self->clearConnections();
}

//  int QTreeViewPrivate::logicalIndexForTree() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate19logicalIndexForTreeEv(
    const QTreeViewPrivate *self) {
  return self->logicalIndexForTree();
}

//  bool QTreeViewPrivate::isTreePosition(int logicalIndex) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTreeViewPrivate14isTreePositionEi(
    const QTreeViewPrivate *self,
    int logicalIndex) {
  return self->isTreePosition(logicalIndex);
}

//  QItemViewPaintPairs QTreeViewPrivate::draggablePaintPairs(const
//      QModelIndexList &indexes, QRect *r) const
extern "C" Q_DECL_EXPORT
QList<QItemViewPaintPair> *ritual_ZNK16QTreeViewPrivate19draggablePaintPairsERK5QListI11QModelIndexEP5QRect(
    const QTreeViewPrivate *self,
    const QList<QModelIndex> *indexes,
    QRect *r) {
  return new QList<QItemViewPaintPair>(
      self->draggablePaintPairs(
          *indexes,
          r));
}

//  void QTreeViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem
//      *option, const QModelIndex &current) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QTreeViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex(
    const QTreeViewPrivate *self,
    QStyleOptionViewItem *option,
    const QModelIndex *current) {
  self->adjustViewOptionsForIndex(option, *current);
}

#if QT_CONFIG(animation)
//  void QTreeViewPrivate::beginAnimatedOperation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate22beginAnimatedOperationEv(
    QTreeViewPrivate *self) {
  self->beginAnimatedOperation();
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QTreeViewPrivate::drawAnimatedOperation(QPainter *painter) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QTreeViewPrivate21drawAnimatedOperationEP8QPainter(
    const QTreeViewPrivate *self,
    QPainter *painter) {
  self->drawAnimatedOperation(painter);
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  QPixmap QTreeViewPrivate::renderTreeToPixmapForAnimation(const QRect
//      &rect) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK16QTreeViewPrivate30renderTreeToPixmapForAnimationERK5QRect(
    const QTreeViewPrivate *self,
    const QRect *rect) {
  return new QPixmap(self->renderTreeToPixmapForAnimation(*rect));
}
#endif  // QT_CONFIG(animation)

#if QT_CONFIG(animation)
//  void QTreeViewPrivate::endAnimatedOperation()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate20endAnimatedOperationEv(
    QTreeViewPrivate *self) {
  self->endAnimatedOperation();
}
#endif  // QT_CONFIG(animation)

//  void QTreeViewPrivate::expand(int item, bool emitSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate6expandEib(
    QTreeViewPrivate *self,
    int item,
    bool emitSignal) {
  self->expand(item, emitSignal);
}

//  void QTreeViewPrivate::collapse(int item, bool emitSignal)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate8collapseEib(
    QTreeViewPrivate *self,
    int item,
    bool emitSignal) {
  self->collapse(item, emitSignal);
}

//  void QTreeViewPrivate::columnsAboutToBeRemoved(const QModelIndex &a0, int
//      a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii(
    QTreeViewPrivate *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->columnsAboutToBeRemoved(*a0, a1, a2);
}

//  void QTreeViewPrivate::columnsRemoved(const QModelIndex &a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate14columnsRemovedERK11QModelIndexii(
    QTreeViewPrivate *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->columnsRemoved(*a0, a1, a2);
}

//  void QTreeViewPrivate::modelAboutToBeReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate19modelAboutToBeResetEv(
    QTreeViewPrivate *self) {
  self->modelAboutToBeReset();
}

//  void QTreeViewPrivate::sortIndicatorChanged(int column, Qt::SortOrder
//      order)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate20sortIndicatorChangedEiN2Qt9SortOrderE(
    QTreeViewPrivate *self,
    int column,
    Qt::SortOrder order) {
  self->sortIndicatorChanged(column, order);
}

//  void QTreeViewPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate14modelDestroyedEv(QTreeViewPrivate *self) {
  self->modelDestroyed();
}

//  QRect QTreeViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QTreeViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QTreeViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(self->intersectedRect(*rect, *topLeft, *bottomRight));
}

//  void QTreeViewPrivate::layout(int item, ExpandItems expandItems,
//      InitializeNewItems initializeNewItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate6layoutEiNS_11ExpandItemsENS_18InitializeNewItemsE(
    QTreeViewPrivate *self,
    int item,
    QTreeViewPrivate::ExpandItems expandItems,
    QTreeViewPrivate::InitializeNewItems initializeNewItems) {
  self->layout(item, expandItems, initializeNewItems);
}

//  void QTreeViewPrivate::doItemsLayout(ExpandItems expandItems,
//      InitializeNewItems initializeNewItems)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate13doItemsLayoutENS_11ExpandItemsENS_18InitializeNewItemsE(
    QTreeViewPrivate *self,
    QTreeViewPrivate::ExpandItems expandItems,
    QTreeViewPrivate::InitializeNewItems initializeNewItems) {
  self->doItemsLayout(expandItems, initializeNewItems);
}

//  int QTreeViewPrivate::pageUp(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate6pageUpEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->pageUp(item);
}

//  int QTreeViewPrivate::pageDown(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate8pageDownEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->pageDown(item);
}

//  int QTreeViewPrivate::itemForKeyHome() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate14itemForKeyHomeEv(
    const QTreeViewPrivate *self) {
  return self->itemForKeyHome();
}

//  int QTreeViewPrivate::itemForKeyEnd() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate13itemForKeyEndEv(
    const QTreeViewPrivate *self) {
  return self->itemForKeyEnd();
}

//  int QTreeViewPrivate::itemHeight(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate10itemHeightEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->itemHeight(item);
}

//  int QTreeViewPrivate::indentationForItem(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate18indentationForItemEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->indentationForItem(item);
}

//  int QTreeViewPrivate::coordinateForItem(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate17coordinateForItemEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->coordinateForItem(item);
}

//  int QTreeViewPrivate::itemAtCoordinate(int coordinate) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate16itemAtCoordinateEi(
    const QTreeViewPrivate *self,
    int coordinate) {
  return self->itemAtCoordinate(coordinate);
}

//  int QTreeViewPrivate::viewIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate9viewIndexERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return self->viewIndex(*index);
}

//  QModelIndex QTreeViewPrivate::modelIndex(int i, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QTreeViewPrivate10modelIndexEii(
    const QTreeViewPrivate *self,
    int i,
    int column) {
  return new QModelIndex(self->modelIndex(i, column));
}

//  void QTreeViewPrivate::insertViewItems(int pos, int count, const
//      QTreeViewItem &viewItem)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate15insertViewItemsEiiRK13QTreeViewItem(
    QTreeViewPrivate *self,
    int pos,
    int count,
    const QTreeViewItem *viewItem) {
  self->insertViewItems(pos, count, *viewItem);
}

//  void QTreeViewPrivate::removeViewItems(int pos, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate15removeViewItemsEii(
    QTreeViewPrivate *self,
    int pos,
    int count) {
  self->removeViewItems(pos, count);
}

//  int QTreeViewPrivate::firstVisibleItem(int *offset) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate16firstVisibleItemEPi(
    const QTreeViewPrivate *self,
    int *offset) {
  return self->firstVisibleItem(offset);
}

//  int QTreeViewPrivate::lastVisibleItem(int firstVisual, int offset) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate15lastVisibleItemEii(
    const QTreeViewPrivate *self,
    int firstVisual,
    int offset) {
  return self->lastVisibleItem(firstVisual, offset);
}

//  int QTreeViewPrivate::columnAt(int x) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate8columnAtEi(
    const QTreeViewPrivate *self,
    int x) {
  return self->columnAt(x);
}

//  bool QTreeViewPrivate::hasVisibleChildren(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTreeViewPrivate18hasVisibleChildrenERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *parent) {
  return self->hasVisibleChildren(*parent);
}

//  bool QTreeViewPrivate::expandOrCollapseItemAtPos(const QPoint &pos)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QTreeViewPrivate25expandOrCollapseItemAtPosERK6QPoint(
    QTreeViewPrivate *self,
    const QPoint *pos) {
  return self->expandOrCollapseItemAtPos(*pos);
}

//  void QTreeViewPrivate::updateScrollBars()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate16updateScrollBarsEv(
    QTreeViewPrivate *self) {
  self->updateScrollBars();
}

//  int QTreeViewPrivate::itemDecorationAt(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate16itemDecorationAtERK6QPoint(
    const QTreeViewPrivate *self,
    const QPoint *pos) {
  return self->itemDecorationAt(*pos);
}

//  QRect QTreeViewPrivate::itemDecorationRect(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QTreeViewPrivate18itemDecorationRectERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->itemDecorationRect(*index));
}

//  void QTreeViewPrivate::select(const QModelIndex &start, const QModelIndex
//      &stop, QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate6selectERK11QModelIndexS2_6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTreeViewPrivate *self,
    const QModelIndex *start,
    const QModelIndex *stop,
    int command) {
  self->select(
      *start,
      *stop,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QTreeViewPrivate::paintAlternatingRowColors(QPainter *painter,
//      QStyleOptionViewItem *option, int y, int bottom) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QTreeViewPrivate25paintAlternatingRowColorsEP8QPainterP20QStyleOptionViewItemii(
    const QTreeViewPrivate *self,
    QPainter *painter,
    QStyleOptionViewItem *option,
    int y,
    int bottom) {
  self->paintAlternatingRowColors(painter, option, y, bottom);
}

//  int QTreeViewPrivate::widthHintForIndex(const QModelIndex &index, int
//      hint, const QStyleOptionViewItem &option, int i) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate17widthHintForIndexERK11QModelIndexiRK20QStyleOptionViewItemi(
    const QTreeViewPrivate *self,
    const QModelIndex *index,
    int hint,
    const QStyleOptionViewItem *option,
    int i) {
  return self->widthHintForIndex(*index, hint, *option, i);
}

//  QRect QTreeViewPrivate::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QTreeViewPrivate10visualRectERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  QRect QTreeViewPrivate::visualRect(const QModelIndex &index, RectRule
//      rule) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK16QTreeViewPrivate10visualRectERK11QModelIndexNS_8RectRuleE(
    const QTreeViewPrivate *self,
    const QModelIndex *index,
    QTreeViewPrivate::RectRule rule) {
  return new QRect(self->visualRect(*index, rule));
}

//  bool QTreeViewPrivate::storeExpanded(const QPersistentModelIndex &idx)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QTreeViewPrivate13storeExpandedERK21QPersistentModelIndex(
    QTreeViewPrivate *self,
    const QPersistentModelIndex *idx) {
  return self->storeExpanded(*idx);
}

//  bool QTreeViewPrivate::isIndexExpanded(const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTreeViewPrivate15isIndexExpandedERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *idx) {
  return self->isIndexExpanded(*idx);
}

//  bool QTreeViewPrivate::isRowHidden(const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTreeViewPrivate11isRowHiddenERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *idx) {
  return self->isRowHidden(*idx);
}

//  bool QTreeViewPrivate::isItemHiddenOrDisabled(int i) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK16QTreeViewPrivate22isItemHiddenOrDisabledEi(
    const QTreeViewPrivate *self,
    int i) {
  return self->isItemHiddenOrDisabled(i);
}

//  int QTreeViewPrivate::above(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate5aboveEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->above(item);
}

//  int QTreeViewPrivate::below(int item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate5belowEi(
    const QTreeViewPrivate *self,
    int item) {
  return self->below(item);
}

//  void QTreeViewPrivate::invalidateHeightCache(int item) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK16QTreeViewPrivate21invalidateHeightCacheEi(
    const QTreeViewPrivate *self,
    int item) {
  self->invalidateHeightCache(item);
}

//  int QTreeViewPrivate::accessibleTable2Index(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate21accessibleTable2IndexERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return self->accessibleTable2Index(*index);
}

#if QT_CONFIG(accessibility)
//  int QTreeViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QTreeViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return self->accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

//  void QTreeViewPrivate::updateIndentationFromStyle()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate26updateIndentationFromStyleEv(
    QTreeViewPrivate *self) {
  self->updateIndentationFromStyle();
}

//  void QTreeViewPrivate::updateAccessibility()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QTreeViewPrivate19updateAccessibilityEv(
    QTreeViewPrivate *self) {
  self->updateAccessibility();
}

//  a Python function taken by a CuteQTreeViewPrivate, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTreeViewPrivate(
    QTreeViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQTreeViewPrivate *>(self)->take(key, call);
}

//  void QTreeViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewItem
//      *option, const QModelIndex &current) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK16QTreeViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex(
    const QTreeViewPrivate *self,
    QStyleOptionViewItem *option,
    const QModelIndex *current) {
  self->QTreeViewPrivate::adjustViewOptionsForIndex(option, *current);
}

//  void QTreeViewPrivate::columnsAboutToBeRemoved(const QModelIndex &a0, int
//      a1, int a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTreeViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii(
    QTreeViewPrivate *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->QTreeViewPrivate::columnsAboutToBeRemoved(*a0, a1, a2);
}

//  void QTreeViewPrivate::columnsRemoved(const QModelIndex &a0, int a1, int
//      a2)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTreeViewPrivate14columnsRemovedERK11QModelIndexii(
    QTreeViewPrivate *self,
    const QModelIndex *a0,
    int a1,
    int a2) {
  self->QTreeViewPrivate::columnsRemoved(*a0, a1, a2);
}

//  void QTreeViewPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QTreeViewPrivate14modelDestroyedEv(
    QTreeViewPrivate *self) {
  self->QTreeViewPrivate::modelDestroyed();
}

//  QRect QTreeViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK16QTreeViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QTreeViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(
      self->QTreeViewPrivate::intersectedRect(
          *rect,
          *topLeft,
          *bottomRight));
}

//  QRect QTreeViewPrivate::visualRect(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK16QTreeViewPrivate10visualRectERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->QTreeViewPrivate::visualRect(*index));
}

#if QT_CONFIG(accessibility)
//  int QTreeViewPrivate::accessibleChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QTreeViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QTreeViewPrivate *self,
    const QModelIndex *index) {
  return self->QTreeViewPrivate::accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

#endif  // QT_CONFIG(treeview)
