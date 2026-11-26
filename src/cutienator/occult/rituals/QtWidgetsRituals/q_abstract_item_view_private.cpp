//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtGui/qtguiglobal.h>
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/qabstractitemview.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qabstractitemview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#include <QtWidgets/qstyleoption.h>
#include <QtGui/qregion.h>
#include <QtGui/qpixmap.h>
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 96, as _ZN24QAbstractItemViewPrivateD2Ev
inline QAbstractItemViewPrivate::~QAbstractItemViewPrivate()
{
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 100, as _ZN24QAbstractItemViewPrivate4initEv
inline void QAbstractItemViewPrivate::init()
{
    Q_Q(QAbstractItemView);
    q->setItemDelegate(new QStyledItemDelegate(q));

    vbar->setRange(0, 0);
    hbar->setRange(0, 0);

    scrollbarConnections = {
        QObject::connect(vbar, &QScrollBar::actionTriggered,
                         q, &QAbstractItemView::verticalScrollbarAction),
        QObject::connect(hbar, &QScrollBar::actionTriggered,
                         q, &QAbstractItemView::horizontalScrollbarAction),
        QObject::connect(vbar, &QScrollBar::valueChanged,
                         q, &QAbstractItemView::verticalScrollbarValueChanged),
        QObject::connect(hbar, &QScrollBar::valueChanged,
                         q, &QAbstractItemView::horizontalScrollbarValueChanged)
    };
    viewport->setBackgroundRole(QPalette::Base);

    q->setAttribute(Qt::WA_InputMethodEnabled);

    verticalScrollMode = static_cast<QAbstractItemView::ScrollMode>(q->style()->styleHint(QStyle::SH_ItemView_ScrollMode, nullptr, q, nullptr));
    horizontalScrollMode = static_cast<QAbstractItemView::ScrollMode>(q->style()->styleHint(QStyle::SH_ItemView_ScrollMode, nullptr, q, nullptr));
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 216, as _ZN24QAbstractItemViewPrivate20scrollerStateChangedEv
#if QT_CONFIG(gestures) && QT_CONFIG(scroller)
inline void QAbstractItemViewPrivate::scrollerStateChanged()
{
    Q_Q(QAbstractItemView);

    if (QScroller *scroller = QScroller::scroller(viewport)) {
        switch (scroller->state()) {
        case QScroller::Pressed:
            // store the current selection in case we start scrolling
            if (q->selectionModel()) {
                oldSelection = q->selectionModel()->selection();
                oldCurrent = q->selectionModel()->currentIndex();
            }
            break;

        case QScroller::Dragging:
            // restore the old selection if we really start scrolling
            if (q->selectionModel()) {
                q->selectionModel()->select(oldSelection, QItemSelectionModel::ClearAndSelect);
                // block autoScroll logic while we are already handling scrolling
                const bool wasAutoScroll = autoScroll;
                autoScroll = false;
                q->selectionModel()->setCurrentIndex(oldCurrent, QItemSelectionModel::NoUpdate);
                autoScroll = wasAutoScroll;
            }
            Q_FALLTHROUGH();

        default:
            oldSelection = QItemSelection();
            oldCurrent = QModelIndex();
            break;
        }
    }
}
#endif  // QT_CONFIG(gestures) && QT_CONFIG(scroller)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4376, as _ZN24QAbstractItemViewPrivate9fetchMoreEv
inline void QAbstractItemViewPrivate::fetchMore()
{
    fetchMoreTimer.stop();
    if (!model->canFetchMore(root))
        return;
    int last = model->rowCount(root) - 1;
    if (last < 0) {
        model->fetchMore(root);
        return;
    }

    QModelIndex index = model->index(last, 0, root);
    QRect rect = q_func()->visualRect(index);
    if (viewport->rect().intersects(rect))
        model->fetchMore(root);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4393, as _ZNK24QAbstractItemViewPrivate10shouldEditEN17QAbstractItemView11EditTriggerERK11QModelIndex
inline bool QAbstractItemViewPrivate::shouldEdit(QAbstractItemView::EditTrigger trigger,
                                          const QModelIndex &index) const
{
    if (!index.isValid())
        return false;
    Qt::ItemFlags flags = model->flags(index);
    if (((flags & Qt::ItemIsEditable) == 0) || ((flags & Qt::ItemIsEnabled) == 0))
        return false;
    if (state == QAbstractItemView::EditingState)
        return false;
    if (hasEditor(index))
        return false;
    if (trigger == QAbstractItemView::AllEditTriggers) // force editing
        return true;
    if ((trigger & editTriggers) == QAbstractItemView::SelectedClicked
        && !selectionModel->isSelected(index))
        return false;
    return (trigger & editTriggers);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4413, as _ZNK24QAbstractItemViewPrivate18shouldForwardEventEN17QAbstractItemView11EditTriggerEPK6QEvent
inline bool QAbstractItemViewPrivate::shouldForwardEvent(QAbstractItemView::EditTrigger trigger,
                                                  const QEvent *event) const
{
    if (!event || (trigger & editTriggers) != QAbstractItemView::AnyKeyPressed)
        return false;

    switch (event->type()) {
        case QEvent::KeyPress:
        case QEvent::MouseButtonDblClick:
        case QEvent::MouseButtonPress:
        case QEvent::MouseButtonRelease:
        case QEvent::MouseMove:
            return true;
        default:
            break;
    };

    return false;
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4444, as _ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi
inline void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
{
    if (!delayedPendingLayout) {
        delayedPendingLayout = true;
        delayedLayout.start(delay, q_func());
    }
}

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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4489, as _ZN24QAbstractItemViewPrivate6editorERK11QModelIndexRK20QStyleOptionViewItem
inline QWidget *QAbstractItemViewPrivate::editor(const QModelIndex &index,
                                          const QStyleOptionViewItem &options)
{
    Q_Q(QAbstractItemView);
    QWidget *w = editorForIndex(index).widget.data();
    if (!w) {
        QAbstractItemDelegate *delegate = q->itemDelegateForIndex(index);
        if (!delegate)
            return nullptr;
        w = delegate->createEditor(viewport, options, index);
        if (w) {
            w->installEventFilter(delegate);
            QObject::connect(w, &QWidget::destroyed, q, &QAbstractItemView::editorDestroyed);
            delegate->updateEditorGeometry(w, options, index);
            delegate->setEditorData(w, index);
            addEditor(index, w, false);
            if (w->parent() == viewport)
                QWidget::setTabOrder(q, w);

            selectAllInEditor(w);
        }
    }

    return w;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4654, as _ZNK24QAbstractItemViewPrivate17sendDelegateEventERK11QModelIndexP6QEvent
inline bool QAbstractItemViewPrivate::sendDelegateEvent(const QModelIndex &index, QEvent *event) const
{
    Q_Q(const QAbstractItemView);
    QModelIndex buddy = model->buddy(index);
    QStyleOptionViewItem options;
    q->initViewItemOption(&options);
    options.rect = q->visualRect(buddy);
    options.state |= (buddy == q->currentIndex() ? QStyle::State_HasFocus : QStyle::State_None);
    QAbstractItemDelegate *delegate = q->itemDelegateForIndex(index);
    return (event && delegate && delegate->editorEvent(event, model, options, buddy));
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4666, as _ZN24QAbstractItemViewPrivate10openEditorERK11QModelIndexP6QEvent
inline bool QAbstractItemViewPrivate::openEditor(const QModelIndex &index, QEvent *event)
{
    Q_Q(QAbstractItemView);

    QModelIndex buddy = model->buddy(index);
    QStyleOptionViewItem options;
    q->initViewItemOption(&options);
    options.rect = q->visualRect(buddy);
    options.state |= (buddy == q->currentIndex() ? QStyle::State_HasFocus : QStyle::State_None);

    QWidget *w = editor(buddy, options);
    if (!w)
        return false;

    q->setState(QAbstractItemView::EditingState);
    w->show();
    if (!waitForIMCommit)
        w->setFocus();
    else
        q->updateMicroFocus();

    if (event)
        QCoreApplication::sendEvent(w->focusProxy() ? w->focusProxy() : w, event);

    return true;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4515, as _ZN24QAbstractItemViewPrivate16updateEditorDataERK11QModelIndexS2_
inline void QAbstractItemViewPrivate::updateEditorData(const QModelIndex &tl, const QModelIndex &br)
{
    Q_Q(QAbstractItemView);
    // we are counting on having relatively few editors
    const bool checkIndexes = tl.isValid() && br.isValid();
    const QModelIndex parent = tl.parent();
    // QTBUG-25370: We need to copy the indexEditorHash, because while we're
    // iterating over it, we are calling methods which can allow user code to
    // call a method on *this which can modify the member indexEditorHash.
    const QIndexEditorHash indexEditorHashCopy = indexEditorHash;
    QIndexEditorHash::const_iterator it = indexEditorHashCopy.constBegin();
    for (; it != indexEditorHashCopy.constEnd(); ++it) {
        QWidget *editor = it.value().widget.data();
        const QModelIndex index = it.key();
        if (it.value().isStatic || !editor || !index.isValid() ||
            (checkIndexes
                && (index.row() < tl.row() || index.row() > br.row()
                    || index.column() < tl.column() || index.column() > br.column()
                    || index.parent() != parent)))
            continue;

        QAbstractItemDelegate *delegate = q->itemDelegateForIndex(index);
        if (delegate) {
            delegate->setEditorData(editor, index);
        }
    }
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4472, as _ZN24QAbstractItemViewPrivate17selectAllInEditorEP7QWidget
inline void QAbstractItemViewPrivate::selectAllInEditor(QWidget *editor)
{
    while (QWidget *fp = editor->focusProxy())
        editor = fp;

#if QT_CONFIG(lineedit)
    if (QLineEdit *le = qobject_cast<QLineEdit*>(editor))
        le->selectAll();
#endif
#if QT_CONFIG(spinbox)
    if (QSpinBox *sb = qobject_cast<QSpinBox*>(editor))
        sb->selectAll();
    else if (QDoubleSpinBox *dsb = qobject_cast<QDoubleSpinBox*>(editor))
        dsb->selectAll();
#endif
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4201, as _ZNK24QAbstractItemViewPrivate21multiSelectionCommandERK11QModelIndexPK6QEvent
inline QItemSelectionModel::SelectionFlags QAbstractItemViewPrivate::multiSelectionCommand(
    const QModelIndex &index, const QEvent *event) const
{
    Q_UNUSED(index);

    if (event) {
        switch (event->type()) {
        case QEvent::KeyPress:
            if (static_cast<const QKeyEvent*>(event)->key() == Qt::Key_Space
             || static_cast<const QKeyEvent*>(event)->key() == Qt::Key_Select)
                return QItemSelectionModel::Toggle|selectionBehaviorFlags();
            break;
        case QEvent::MouseButtonPress:
            if (static_cast<const QMouseEvent*>(event)->button() == Qt::LeftButton) {
                // since the press might start a drag, deselect only on release
                if (!pressedAlreadySelected
#if QT_CONFIG(draganddrop)
                        || !dragEnabled || !isIndexDragEnabled(index)
#endif
                        )
                    return QItemSelectionModel::Toggle|selectionBehaviorFlags(); // toggle
            }
            break;
        case QEvent::MouseButtonRelease:
            if (static_cast<const QMouseEvent*>(event)->button() == Qt::LeftButton) {
                if (pressedAlreadySelected
#if QT_CONFIG(draganddrop)
                        && dragEnabled && isIndexDragEnabled(index)
#endif
                        && index == pressedIndex)
                    return QItemSelectionModel::Toggle|selectionBehaviorFlags();
                return QItemSelectionModel::NoUpdate|selectionBehaviorFlags(); // finalize
            }
            break;
        case QEvent::MouseMove:
            if (static_cast<const QMouseEvent*>(event)->buttons() & Qt::LeftButton)
                return QItemSelectionModel::ToggleCurrent|selectionBehaviorFlags(); // toggle drag select
            break;
        default:
            break;
        }
        return QItemSelectionModel::NoUpdate;
    }

    return QItemSelectionModel::Toggle|selectionBehaviorFlags();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4248, as _ZNK24QAbstractItemViewPrivate24extendedSelectionCommandERK11QModelIndexPK6QEvent
inline QItemSelectionModel::SelectionFlags QAbstractItemViewPrivate::extendedSelectionCommand(
    const QModelIndex &index, const QEvent *event) const
{
    Qt::KeyboardModifiers modifiers = event && event->isInputEvent()
            ? static_cast<const QInputEvent*>(event)->modifiers()
            : QGuiApplication::keyboardModifiers();
    if (event) {
        switch (event->type()) {
        case QEvent::MouseMove: {
            // Toggle on MouseMove
            if (modifiers & Qt::ControlModifier)
                return QItemSelectionModel::ToggleCurrent|selectionBehaviorFlags();
            break;
        }
        case QEvent::MouseButtonPress: {
            const Qt::MouseButton button = static_cast<const QMouseEvent*>(event)->button();
            const bool rightButtonPressed = button & Qt::RightButton;
            const bool shiftKeyPressed = modifiers & Qt::ShiftModifier;
            const bool controlKeyPressed = modifiers & Qt::ControlModifier;
            const bool indexIsSelected = selectionModel->isSelected(index);
            if ((shiftKeyPressed || controlKeyPressed) && rightButtonPressed)
                return QItemSelectionModel::NoUpdate;
            if (!shiftKeyPressed && !controlKeyPressed && indexIsSelected)
                return QItemSelectionModel::NoUpdate;
            if (!index.isValid() && !rightButtonPressed && !shiftKeyPressed && !controlKeyPressed)
                return QItemSelectionModel::Clear;
            if (!index.isValid())
                return QItemSelectionModel::NoUpdate;
            // since the press might start a drag, deselect only on release
            if (controlKeyPressed && !rightButtonPressed && pressedAlreadySelected
#if QT_CONFIG(draganddrop)
                && dragEnabled && isIndexDragEnabled(index)
#endif
                    ) {
                return QItemSelectionModel::NoUpdate;
            }
            break;
        }
        case QEvent::MouseButtonRelease: {
            // ClearAndSelect on MouseButtonRelease if MouseButtonPress on selected item or empty area
            const Qt::MouseButton button = static_cast<const QMouseEvent*>(event)->button();
            const bool rightButtonPressed = button & Qt::RightButton;
            const bool shiftKeyPressed = modifiers & Qt::ShiftModifier;
            const bool controlKeyPressed = modifiers & Qt::ControlModifier;
            if (((index == pressedIndex && selectionModel->isSelected(index))
                || !index.isValid()) && state != QAbstractItemView::DragSelectingState
                && !shiftKeyPressed && !controlKeyPressed && (!rightButtonPressed || !index.isValid()))
                return QItemSelectionModel::ClearAndSelect|selectionBehaviorFlags();
            if (index == pressedIndex && controlKeyPressed && !rightButtonPressed
#if QT_CONFIG(draganddrop)
                && dragEnabled && isIndexDragEnabled(index)
#endif
                    ) {
                break;
            }
            return QItemSelectionModel::NoUpdate;
        }
        case QEvent::KeyPress: {
            // NoUpdate on Key movement and Ctrl
            switch (static_cast<const QKeyEvent*>(event)->key()) {
            case Qt::Key_Backtab:
                modifiers = modifiers & ~Qt::ShiftModifier; // special case for backtab
                Q_FALLTHROUGH();
            case Qt::Key_Down:
            case Qt::Key_Up:
            case Qt::Key_Left:
            case Qt::Key_Right:
            case Qt::Key_Home:
            case Qt::Key_End:
            case Qt::Key_PageUp:
            case Qt::Key_PageDown:
            case Qt::Key_Tab:
                if (modifiers & Qt::ControlModifier)
                    return QItemSelectionModel::NoUpdate;
                break;
            case Qt::Key_Select:
                return QItemSelectionModel::Toggle|selectionBehaviorFlags();
            case Qt::Key_Space:// Toggle on Ctrl-Qt::Key_Space, Select on Space
                if (modifiers & Qt::ControlModifier)
                    return QItemSelectionModel::Toggle|selectionBehaviorFlags();
                return QItemSelectionModel::Select|selectionBehaviorFlags();
            default:
                break;
            }
            break;
        }
        default:
            break;
        }
    }

    if (modifiers & Qt::ShiftModifier)
        return QItemSelectionModel::SelectCurrent|selectionBehaviorFlags();
    if (modifiers & Qt::ControlModifier)
        return QItemSelectionModel::Toggle|selectionBehaviorFlags();
    if (state == QAbstractItemView::DragSelectingState) {
        //when drag-selecting we need to clear any previous selection and select the current one
        return QItemSelectionModel::Clear|QItemSelectionModel::SelectCurrent|selectionBehaviorFlags();
    }

    return QItemSelectionModel::ClearAndSelect|selectionBehaviorFlags();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4351, as _ZNK24QAbstractItemViewPrivate26contiguousSelectionCommandERK11QModelIndexPK6QEvent
inline QItemSelectionModel::SelectionFlags
QAbstractItemViewPrivate::contiguousSelectionCommand(const QModelIndex &index,
                                                     const QEvent *event) const
{
    QItemSelectionModel::SelectionFlags flags = extendedSelectionCommand(index, event);
    const int Mask = QItemSelectionModel::Clear | QItemSelectionModel::Select
                     | QItemSelectionModel::Deselect | QItemSelectionModel::Toggle
                     | QItemSelectionModel::Current;

    switch (flags & Mask) {
    case QItemSelectionModel::Clear:
    case QItemSelectionModel::ClearAndSelect:
    case QItemSelectionModel::SelectCurrent:
        return flags;
    case QItemSelectionModel::NoUpdate:
        if (event &&
            (event->type() == QEvent::MouseButtonPress
             || event->type() == QEvent::MouseButtonRelease))
            return flags;
        return QItemSelectionModel::ClearAndSelect|selectionBehaviorFlags();
    default:
        return QItemSelectionModel::SelectCurrent|selectionBehaviorFlags();
    }
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 126, as _ZN24QAbstractItemViewPrivate13setHoverIndexERK21QPersistentModelIndex
inline void QAbstractItemViewPrivate::setHoverIndex(const QPersistentModelIndex &index)
{
    Q_Q(QAbstractItemView);
    if (hover == index)
        return;

    if (selectionBehavior != QAbstractItemView::SelectRows) {
        q->update(hover); //update the old one
        q->update(index); //update the new one
    } else {
        const QRect oldHoverRect = visualRect(hover);
        const QRect newHoverRect = visualRect(index);
        viewport->update(QRect(0, newHoverRect.y(), viewport->width(), newHoverRect.height()));
        viewport->update(QRect(0, oldHoverRect.y(), viewport->width(), oldHoverRect.height()));
    }
    hover = index;
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 144, as _ZN24QAbstractItemViewPrivate14checkMouseMoveERK21QPersistentModelIndex
inline void QAbstractItemViewPrivate::checkMouseMove(const QPersistentModelIndex &index)
{
    //we take a persistent model index because the model might change by emitting signals
    Q_Q(QAbstractItemView);
    setHoverIndex(index);
    if (viewportEnteredNeeded || enteredIndex != index) {
        viewportEnteredNeeded = false;

        if (index.isValid()) {
            emit q->entered(index);
#if QT_CONFIG(statustip)
            QString statustip = model->data(index, Qt::StatusTipRole).toString();
            if (parent && (shouldClearStatusTip || !statustip.isEmpty())) {
                QStatusTipEvent tip(statustip);
                QCoreApplication::sendEvent(parent, &tip);
                shouldClearStatusTip = !statustip.isEmpty();
            }
#endif
        } else {
#if QT_CONFIG(statustip)
            if (parent && shouldClearStatusTip) {
                QString emptyString;
                QStatusTipEvent tip( emptyString );
                QCoreApplication::sendEvent(parent, &tip);
            }
#endif
            emit q->viewportEntered();
        }
        enteredIndex = index;
    }
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4588, as _ZN24QAbstractItemViewPrivate26checkPersistentEditorFocusEv
inline void QAbstractItemViewPrivate::checkPersistentEditorFocus()
{
    Q_Q(QAbstractItemView);
    if (QWidget *widget = QApplication::focusWidget()) {
        if (persistent.contains(widget)) {
            //a persistent editor has gained the focus
            QModelIndex index = indexForEditor(widget);
            if (selectionModel->currentIndex() != index)
                q->setCurrentIndex(index);
        }
    }
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

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4617, as _ZNK24QAbstractItemViewPrivate9hasEditorERK11QModelIndex
inline bool QAbstractItemViewPrivate::hasEditor(const QModelIndex &index) const
{
    // Search's implicit cast (QModelIndex to QPersistentModelIndex) is slow; use cheap pre-test to avoid when we can.
    return !indexEditorHash.isEmpty() && indexEditorHash.contains(index);
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4623, as _ZNK24QAbstractItemViewPrivate14indexForEditorEP7QWidget
inline QModelIndex QAbstractItemViewPrivate::indexForEditor(QWidget *editor) const
{
    // do not try to search to avoid slow implicit cast from QModelIndex to QPersistentModelIndex
    if (indexEditorHash.isEmpty())
        return QModelIndex();

   QEditorIndexHash::const_iterator it = editorIndexHash.find(editor);
    if (it == editorIndexHash.end())
        return QModelIndex();

    return it.value();
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4648, as _ZN24QAbstractItemViewPrivate9addEditorERK11QModelIndexP7QWidgetb
inline void QAbstractItemViewPrivate::addEditor(const QModelIndex &index, QWidget *editor, bool isStatic)
{
    editorIndexHash.insert(editor, index);
    indexEditorHash.insert(index, QEditorInfo(editor, isStatic));
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4636, as _ZN24QAbstractItemViewPrivate12removeEditorEP7QWidget
inline void QAbstractItemViewPrivate::removeEditor(QWidget *editor)
{
    Q_Q(QAbstractItemView);
    if (editor)
        QObject::disconnect(editor, &QWidget::destroyed, q, &QAbstractItemView::editorDestroyed);
    const auto it = editorIndexHash.constFind(editor);
    if (it != editorIndexHash.cend()) {
        indexEditorHash.remove(it.value());
        editorIndexHash.erase(it);
    }
}

//  from src/widgets/itemviews/qabstractitemview.cpp, line 177, as _ZN24QAbstractItemViewPrivate23updateItemAccessibilityERK11QModelIndexRK5QListIiE
#if QT_CONFIG(accessibility)
inline void QAbstractItemViewPrivate::updateItemAccessibility(const QModelIndex &index,
                                                       const QList<int> &roles)
{
    Q_Q(QAbstractItemView);

    if (!QAccessible::isActive())
        return;

    const int childIndex = accessibleChildIndex(index);
    if (childIndex < 0)
        return;

    // see QAccessibleTableCell for how role data are mapped to the a11y layer

    for (int role : roles) {
        if (role == Qt::AccessibleTextRole
            || (role == Qt::DisplayRole
                && index.data(Qt::AccessibleTextRole).toString().isEmpty())) {
            QAccessibleEvent event(q, QAccessible::NameChanged);
            event.setChild(childIndex);
            QAccessible::updateAccessibility(&event);
        } else if (role == Qt::AccessibleDescriptionRole) {
            QAccessibleEvent event(q, QAccessible::DescriptionChanged);
            event.setChild(childIndex);
            QAccessible::updateAccessibility(&event);
        } else if (role == Qt::CheckStateRole) {
            QAccessible::State state;
            state.checked = true;
            QAccessibleStateChangeEvent event(q, state);
            event.setChild(childIndex);
            QAccessible::updateAccessibility(&event);
        }
    }
}
#endif  // QT_CONFIG(accessibility)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4765, as _ZNK24QAbstractItemViewPrivate24selectedDraggableIndexesEv
#if QT_CONFIG(draganddrop)
inline QModelIndexList QAbstractItemViewPrivate::selectedDraggableIndexes() const
{
    Q_Q(const QAbstractItemView);
    QModelIndexList indexes = q->selectedIndexes();
    auto isNotDragEnabled = [this](const QModelIndex &index) {
        return !isIndexDragEnabled(index);
    };
    indexes.removeIf(isNotDragEnabled);
    return indexes;
}
#endif  // QT_CONFIG(draganddrop)

//  from src/widgets/itemviews/qabstractitemview.cpp, line 4776, as _ZN24QAbstractItemViewPrivate14maybeStartDragE6QPoint
#if QT_CONFIG(draganddrop)
inline void QAbstractItemViewPrivate::maybeStartDrag(QPoint eventPosition)
{
    Q_Q(QAbstractItemView);

    const QPoint topLeft = pressedPosition - offset();
    if ((topLeft - eventPosition).manhattanLength() > QApplication::startDragDistance()) {
        pressedIndex = QModelIndex();
        q->startDrag(model->supportedDragActions());
        q->setState(QAbstractItemView::NoState); // the startDrag will return when the dnd operation
                                                 // is done
        q->stopAutoScroll();
    }
}
#endif  // QT_CONFIG(draganddrop)
//  -----------------------------------------------------------------------

//  A QAbstractItemViewPrivate that Python can take functions over in. Every QAbstractItemViewPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall0)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall1)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall2)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall3)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall4)(const void *, const QModelIndex *, int, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall5)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall6)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall7)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall8)(const void *, const QModelIndex *, int, int, const QModelIndex *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQAbstractItemViewPrivateCall9)(const void *, const QRect *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall10)(const void *, int, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef void (*CuteQAbstractItemViewPrivateCall11)(const void *, QStyleOptionViewItem *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
typedef bool (*CuteQAbstractItemViewPrivateCall12)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(itemviews)
#if QT_CONFIG(accessibility)
typedef int (*CuteQAbstractItemViewPrivateCall13)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(accessibility)
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QPoint * (*CuteQAbstractItemViewPrivateCall14)(const void *, int *);
#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(itemviews)
typedef const QRect * (*CuteQAbstractItemViewPrivateCall15)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(itemviews)
#if QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewPrivateCall16)(const void *, int, int, int *);
#endif  // QT_CONFIG(scrollarea)
#if QT_CONFIG(scrollarea)
typedef bool (*CuteQAbstractItemViewPrivateCall17)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(scrollarea)
typedef void (*CuteQAbstractItemViewPrivateCall18)(const void *, bool, int *);
typedef void (*CuteQAbstractItemViewPrivateCall19)(const void *, int, int *);
typedef void (*CuteQAbstractItemViewPrivateCall20)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall21)(const void *, int *);
typedef void * (*CuteQAbstractItemViewPrivateCall22)(const void *, int *);
typedef const QPlatformBackingStoreRhiConfig * (*CuteQAbstractItemViewPrivateCall23)(const void *, int *);
typedef const QWidgetPrivate::TextureData * (*CuteQAbstractItemViewPrivateCall24)(const void *, int *);
typedef int (*CuteQAbstractItemViewPrivateCall25)(const void *, int *);
typedef const QImage * (*CuteQAbstractItemViewPrivateCall26)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall27)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall28)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall29)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall30)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall31)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall32)(const void *, int *);
typedef void (*CuteQAbstractItemViewPrivateCall33)(const void *, int *);
typedef bool (*CuteQAbstractItemViewPrivateCall34)(const void *, int *);
typedef bool (*CuteQAbstractItemViewPrivateCall35)(const void *, int *);
class CuteQAbstractItemViewPrivate : public QAbstractItemViewPrivate {
public:
  using QAbstractItemViewPrivate::QAbstractItemViewPrivate;
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
      CuteQAbstractItemViewPrivateCall0 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall0>(taken[0]);
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
      CuteQAbstractItemViewPrivateCall1 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall1>(taken[1]);
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
      CuteQAbstractItemViewPrivateCall2 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall2>(taken[2]);
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
      CuteQAbstractItemViewPrivateCall3 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall3>(taken[3]);
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
      CuteQAbstractItemViewPrivateCall4 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall4>(taken[4]);
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
      CuteQAbstractItemViewPrivateCall5 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall5>(taken[5]);
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
      CuteQAbstractItemViewPrivateCall6 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall6>(taken[6]);
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
      CuteQAbstractItemViewPrivateCall7 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall7>(taken[7]);
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
      CuteQAbstractItemViewPrivateCall8 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall8>(taken[8]);
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
      CuteQAbstractItemViewPrivateCall9 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall9>(taken[9]);
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
      CuteQAbstractItemViewPrivateCall10 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall10>(taken[10]);
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
      CuteQAbstractItemViewPrivateCall11 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall11>(taken[11]);
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
      CuteQAbstractItemViewPrivateCall12 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall12>(taken[12]);
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
      CuteQAbstractItemViewPrivateCall13 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall13>(taken[13]);
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
      CuteQAbstractItemViewPrivateCall14 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall14>(taken[14]);
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
      CuteQAbstractItemViewPrivateCall15 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall15>(taken[15]);
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
      CuteQAbstractItemViewPrivateCall16 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall16>(taken[16]);
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
      CuteQAbstractItemViewPrivateCall17 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall17>(taken[17]);
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
      CuteQAbstractItemViewPrivateCall18 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall18>(taken[18]);
      call(this, a0, &handled);
      if (handled) return;
    }
    QWidgetPrivate::setVisible(a0);
  }

  //  void QWidgetPrivate::setWindowFlags(Qt::WindowFlags windowFlags)
  void setWindowFlags(Qt::WindowFlags windowFlags) override {
    if (taken[19]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall19 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall19>(taken[19]);
      call(this, static_cast<int>(windowFlags.toInt()), &handled);
      if (handled) return;
    }
    QWidgetPrivate::setWindowFlags(windowFlags);
  }

  //  void QWidgetPrivate::aboutToDestroy()
  void aboutToDestroy() override {
    if (taken[20]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall20 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall20>(taken[20]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::aboutToDestroy();
  }

  //  void QWidgetPrivate::recreate()
  void recreate() override {
    if (taken[21]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall21 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::recreate();
  }

  //  QObject *QWidgetPrivate::focusObject()
  QObject *focusObject() override {
    if (taken[22]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall22 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall22>(taken[22]);
      void * given = call(this, &handled);
      if (handled) return static_cast<QObject *>(given);
    }
    return QWidgetPrivate::focusObject();
  }

  //  QPlatformBackingStoreRhiConfig QWidgetPrivate::rhiConfig() const
  QPlatformBackingStoreRhiConfig rhiConfig() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall23 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall23>(taken[23]);
      const QPlatformBackingStoreRhiConfig * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::rhiConfig();
  }

  //  TextureData QWidgetPrivate::texture() const
  QWidgetPrivate::TextureData texture() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall24 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall24>(taken[24]);
      const QWidgetPrivate::TextureData * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::texture();
  }

  //  QPlatformTextureList::Flags QWidgetPrivate::textureListFlags()
  QPlatformTextureList::Flags textureListFlags() override {
    if (taken[25]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall25 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall25>(taken[25]);
      int given = call(this, &handled);
      if (handled) return QFlags<QPlatformTextureList::Flag>::fromInt(given);
    }
    return QWidgetPrivate::textureListFlags();
  }

  //  QImage QWidgetPrivate::grabFramebuffer()
  QImage grabFramebuffer() override {
    if (taken[26]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall26 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall26>(taken[26]);
      const QImage * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWidgetPrivate::grabFramebuffer();
  }

  //  void QWidgetPrivate::beginBackingStorePainting()
  void beginBackingStorePainting() override {
    if (taken[27]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall27 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall27>(taken[27]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginBackingStorePainting();
  }

  //  void QWidgetPrivate::endBackingStorePainting()
  void endBackingStorePainting() override {
    if (taken[28]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall28 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall28>(taken[28]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endBackingStorePainting();
  }

  //  void QWidgetPrivate::beginCompose()
  void beginCompose() override {
    if (taken[29]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall29 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall29>(taken[29]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::beginCompose();
  }

  //  void QWidgetPrivate::endCompose()
  void endCompose() override {
    if (taken[30]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall30 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall30>(taken[30]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::endCompose();
  }

  //  void QWidgetPrivate::initializeViewportFramebuffer()
  void initializeViewportFramebuffer() override {
    if (taken[31]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall31 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall31>(taken[31]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::initializeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resizeViewportFramebuffer()
  void resizeViewportFramebuffer() override {
    if (taken[32]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall32 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall32>(taken[32]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resizeViewportFramebuffer();
  }

  //  void QWidgetPrivate::resolveSamples()
  void resolveSamples() override {
    if (taken[33]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall33 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall33>(taken[33]);
      call(this, &handled);
      if (handled) return;
    }
    QWidgetPrivate::resolveSamples();
  }

  //  bool QWidgetPrivate::isStereoEnabled()
  bool isStereoEnabled() override {
    if (taken[34]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall34 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall34>(taken[34]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::isStereoEnabled();
  }

  //  bool QWidgetPrivate::toggleStereoTargetBuffer()
  bool toggleStereoTargetBuffer() override {
    if (taken[35]) {
      int handled = 0;
      CuteQAbstractItemViewPrivateCall35 call = reinterpret_cast<CuteQAbstractItemViewPrivateCall35>(taken[35]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWidgetPrivate::toggleStereoTargetBuffer();
  }
};

//  QAbstractItemView *QAbstractItemViewPrivate::q_func()
extern "C" Q_DECL_EXPORT
QAbstractItemView *ritual_ZN24QAbstractItemViewPrivate6q_funcEv(
    QAbstractItemViewPrivate *self) {
  return self->q_func();
}

//  const QAbstractItemView *QAbstractItemViewPrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QAbstractItemView *ritual_ZNK24QAbstractItemViewPrivate6q_funcEv(
    const QAbstractItemViewPrivate *self) {
  return self->q_func();
}

//  QAbstractItemViewPrivate::~QAbstractItemViewPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivateD1Ev(
    QAbstractItemViewPrivate *self) {
  delete self;
}

//  void QAbstractItemViewPrivate::init()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate4initEv(
    QAbstractItemViewPrivate *self) {
  self->init();
}

//  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsRemoved(*parent, start, end);
}

//  void QAbstractItemViewPrivate::rowsInserted(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->rowsInserted(*parent, start, end);
}

//  void QAbstractItemViewPrivate::columnsAboutToBeRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate23columnsAboutToBeRemovedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsAboutToBeRemoved(*parent, start, end);
}

//  void QAbstractItemViewPrivate::columnsRemoved(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsRemoved(*parent, start, end);
}

//  void QAbstractItemViewPrivate::columnsInserted(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->columnsInserted(*parent, start, end);
}

//  void QAbstractItemViewPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14modelDestroyedEv(
    QAbstractItemViewPrivate *self) {
  self->modelDestroyed();
}

//  void QAbstractItemViewPrivate::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate13layoutChangedEv(
    QAbstractItemViewPrivate *self) {
  self->layoutChanged();
}

//  void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &source, int
//      sourceStart, int sourceEnd, const QModelIndex &destination, int
//      destinationStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i(
    QAbstractItemViewPrivate *self,
    const QModelIndex *source,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destination,
    int destinationStart) {
  self->rowsMoved(
      *source,
      sourceStart,
      sourceEnd,
      *destination,
      destinationStart);
}

//  void QAbstractItemViewPrivate::columnsMoved(const QModelIndex &source,
//      int sourceStart, int sourceEnd, const QModelIndex &destination, int
//      destinationStart)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i(
    QAbstractItemViewPrivate *self,
    const QModelIndex *source,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destination,
    int destinationStart) {
  self->columnsMoved(
      *source,
      sourceStart,
      sourceEnd,
      *destination,
      destinationStart);
}

//  QRect QAbstractItemViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QAbstractItemViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(self->intersectedRect(*rect, *topLeft, *bottomRight));
}

//  void QAbstractItemViewPrivate::headerDataChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate17headerDataChangedEv(
    QAbstractItemViewPrivate *self) {
  self->headerDataChanged();
}

#if QT_CONFIG(gestures) && QT_CONFIG(scroller)
//  void QAbstractItemViewPrivate::scrollerStateChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate20scrollerStateChangedEv(
    QAbstractItemViewPrivate *self) {
  self->scrollerStateChanged();
}
#endif  // QT_CONFIG(gestures) && QT_CONFIG(scroller)

//  void QAbstractItemViewPrivate::fetchMore()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate9fetchMoreEv(
    QAbstractItemViewPrivate *self) {
  self->fetchMore();
}

//  bool QAbstractItemViewPrivate::shouldEdit(QAbstractItemView::EditTrigger
//      trigger, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate10shouldEditEN17QAbstractItemView11EditTriggerERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    QAbstractItemView::EditTrigger trigger,
    const QModelIndex *index) {
  return self->shouldEdit(trigger, *index);
}

//  bool QAbstractItemViewPrivate::shouldForwardEvent(QAbstractItemView::Edit
//      Trigger trigger, const QEvent *event) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate18shouldForwardEventEN17QAbstractItemView11EditTriggerEPK6QEvent(
    const QAbstractItemViewPrivate *self,
    QAbstractItemView::EditTrigger trigger,
    const QEvent *event) {
  return self->shouldForwardEvent(trigger, event);
}

//  bool QAbstractItemViewPrivate::shouldAutoScroll(const QPoint &pos) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate16shouldAutoScrollERK6QPoint(
    const QAbstractItemViewPrivate *self,
    const QPoint *pos) {
  return self->shouldAutoScroll(*pos);
}

//  void QAbstractItemViewPrivate::doDelayedItemsLayout(int delay)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate20doDelayedItemsLayoutEi(
    QAbstractItemViewPrivate *self,
    int delay) {
  self->doDelayedItemsLayout(delay);
}

//  void QAbstractItemViewPrivate::interruptDelayedItemsLayout() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAbstractItemViewPrivate27interruptDelayedItemsLayoutEv(
    const QAbstractItemViewPrivate *self) {
  self->interruptDelayedItemsLayout();
}

//  void QAbstractItemViewPrivate::updateGeometry()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14updateGeometryEv(
    QAbstractItemViewPrivate *self) {
  self->updateGeometry();
}

//  void QAbstractItemViewPrivate::startAutoScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate15startAutoScrollEv(
    QAbstractItemViewPrivate *self) {
  self->startAutoScroll();
}

//  void QAbstractItemViewPrivate::stopAutoScroll()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14stopAutoScrollEv(
    QAbstractItemViewPrivate *self) {
  self->stopAutoScroll();
}

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemViewPrivate::dropOn(QDropEvent *event, int *row, int
//      *col, QModelIndex *index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractItemViewPrivate6dropOnEP10QDropEventPiS2_P11QModelIndex(
    QAbstractItemViewPrivate *self,
    QDropEvent *event,
    int *row,
    int *col,
    QModelIndex *index) {
  return self->dropOn(event, row, col, index);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemViewPrivate::droppingOnItself(QDropEvent *event, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractItemViewPrivate16droppingOnItselfEP10QDropEventRK11QModelIndex(
    QAbstractItemViewPrivate *self,
    QDropEvent *event,
    const QModelIndex *index) {
  return self->droppingOnItself(event, *index);
}
#endif  // QT_CONFIG(draganddrop)

//  QWidget *QAbstractItemViewPrivate::editor(const QModelIndex &index, const
//      QStyleOptionViewItem &options)
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZN24QAbstractItemViewPrivate6editorERK11QModelIndexRK20QStyleOptionViewItem(
    QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    const QStyleOptionViewItem *options) {
  return self->editor(*index, *options);
}

//  bool QAbstractItemViewPrivate::sendDelegateEvent(const QModelIndex
//      &index, QEvent *event) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate17sendDelegateEventERK11QModelIndexP6QEvent(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    QEvent *event) {
  return self->sendDelegateEvent(*index, event);
}

//  bool QAbstractItemViewPrivate::openEditor(const QModelIndex &index,
//      QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractItemViewPrivate10openEditorERK11QModelIndexP6QEvent(
    QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    QEvent *event) {
  return self->openEditor(*index, event);
}

//  void QAbstractItemViewPrivate::updateEditorData(const QModelIndex
//      &topLeft, const QModelIndex &bottomRight)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate16updateEditorDataERK11QModelIndexS2_(
    QAbstractItemViewPrivate *self,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  self->updateEditorData(*topLeft, *bottomRight);
}

//  void QAbstractItemViewPrivate::selectAllInEditor(QWidget *w)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate17selectAllInEditorEP7QWidget(
    QAbstractItemViewPrivate *self,
    QWidget *w) {
  self->selectAllInEditor(w);
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemViewPrivate::multiSelectionCommand(const QModelIndex
//      &index, const QEvent *event) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate21multiSelectionCommandERK11QModelIndexPK6QEvent(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    const QEvent *event) {
  return static_cast<int>(
      self->multiSelectionCommand(
          *index,
          event).toInt());
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemViewPrivate::extendedSelectionCommand(const QModelIndex
//      &index, const QEvent *event) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate24extendedSelectionCommandERK11QModelIndexPK6QEvent(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    const QEvent *event) {
  return static_cast<int>(
      self->extendedSelectionCommand(
          *index,
          event).toInt());
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemViewPrivate::contiguousSelectionCommand(const
//      QModelIndex &index, const QEvent *event) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate26contiguousSelectionCommandERK11QModelIndexPK6QEvent(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    const QEvent *event) {
  return static_cast<int>(
      self->contiguousSelectionCommand(
          *index,
          event).toInt());
}

//  void
//      QAbstractItemViewPrivate::selectAll(QItemSelectionModel::SelectionFla
//      gs command)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QAbstractItemViewPrivate *self,
    int command) {
  self->selectAll(
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QAbstractItemViewPrivate::setHoverIndex(const QPersistentModelIndex
//      &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate13setHoverIndexERK21QPersistentModelIndex(
    QAbstractItemViewPrivate *self,
    const QPersistentModelIndex *index) {
  self->setHoverIndex(*index);
}

//  void QAbstractItemViewPrivate::checkMouseMove(const QPersistentModelIndex
//      &index)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14checkMouseMoveERK21QPersistentModelIndex(
    QAbstractItemViewPrivate *self,
    const QPersistentModelIndex *index) {
  self->checkMouseMove(*index);
}

//  void QAbstractItemViewPrivate::checkMouseMove(const QPoint &pos)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14checkMouseMoveERK6QPoint(
    QAbstractItemViewPrivate *self,
    const QPoint *pos) {
  self->checkMouseMove(*pos);
}

//  QItemSelectionModel::SelectionFlags
//      QAbstractItemViewPrivate::selectionBehaviorFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate22selectionBehaviorFlagsEv(
    const QAbstractItemViewPrivate *self) {
  return static_cast<int>(self->selectionBehaviorFlags().toInt());
}

#if QT_CONFIG(draganddrop)
//  QAbstractItemView::DropIndicatorPosition
//      QAbstractItemViewPrivate::position(const QPoint &pos, const QRect
//      &rect, const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QAbstractItemView::DropIndicatorPosition ritual_ZNK24QAbstractItemViewPrivate8positionERK6QPointRK5QRectRK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QPoint *pos,
    const QRect *rect,
    const QModelIndex *idx) {
  return self->position(*pos, *rect, *idx);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemViewPrivate::canDrop(QDropEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN24QAbstractItemViewPrivate7canDropEP10QDropEvent(
    QAbstractItemViewPrivate *self,
    QDropEvent *event) {
  return self->canDrop(event);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemViewPrivate::paintDropIndicator(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate18paintDropIndicatorEP8QPainter(
    QAbstractItemViewPrivate *self,
    QPainter *painter) {
  self->paintDropIndicator(painter);
}
#endif  // QT_CONFIG(draganddrop)

//  QItemViewPaintPairs QAbstractItemViewPrivate::draggablePaintPairs(const
//      QModelIndexList &indexes, QRect *r) const
extern "C" Q_DECL_EXPORT
QList<QItemViewPaintPair> *ritual_ZNK24QAbstractItemViewPrivate19draggablePaintPairsERK5QListI11QModelIndexEP5QRect(
    const QAbstractItemViewPrivate *self,
    const QList<QModelIndex> *indexes,
    QRect *r) {
  return new QList<QItemViewPaintPair>(
      self->draggablePaintPairs(
          *indexes,
          r));
}

//  void
//      QAbstractItemViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewI
//      tem *a0, const QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    QStyleOptionViewItem *a0,
    const QModelIndex *a1) {
  self->adjustViewOptionsForIndex(a0, *a1);
}

//  void QAbstractItemViewPrivate::releaseEditor(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAbstractItemViewPrivate13releaseEditorEP7QWidgetRK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->releaseEditor(editor, *index);
}

//  void QAbstractItemViewPrivate::executePostedLayout() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK24QAbstractItemViewPrivate19executePostedLayoutEv(
    const QAbstractItemViewPrivate *self) {
  self->executePostedLayout();
}

//  void QAbstractItemViewPrivate::setDirtyRegion(const QRegion
//      &visualRegion)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14setDirtyRegionERK7QRegion(
    QAbstractItemViewPrivate *self,
    const QRegion *visualRegion) {
  self->setDirtyRegion(*visualRegion);
}

//  void QAbstractItemViewPrivate::scrollDirtyRegion(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate17scrollDirtyRegionEii(
    QAbstractItemViewPrivate *self,
    int dx,
    int dy) {
  self->scrollDirtyRegion(dx, dy);
}

//  void QAbstractItemViewPrivate::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate16scrollContentsByEii(
    QAbstractItemViewPrivate *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  void QAbstractItemViewPrivate::updateDirtyRegion()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate17updateDirtyRegionEv(
    QAbstractItemViewPrivate *self) {
  self->updateDirtyRegion();
}

//  void QAbstractItemViewPrivate::clearOrRemove()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate13clearOrRemoveEv(
    QAbstractItemViewPrivate *self) {
  self->clearOrRemove();
}

//  void QAbstractItemViewPrivate::checkPersistentEditorFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate26checkPersistentEditorFocusEv(
    QAbstractItemViewPrivate *self) {
  self->checkPersistentEditorFocus();
}

//  QPixmap QAbstractItemViewPrivate::renderToPixmap(const QModelIndexList
//      &indexes, QRect *r) const
extern "C" Q_DECL_EXPORT
QPixmap *ritual_ZNK24QAbstractItemViewPrivate14renderToPixmapERK5QListI11QModelIndexEP5QRect(
    const QAbstractItemViewPrivate *self,
    const QList<QModelIndex> *indexes,
    QRect *r) {
  return new QPixmap(self->renderToPixmap(*indexes, r));
}

//  QPoint QAbstractItemViewPrivate::offset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QAbstractItemViewPrivate6offsetEv(
    const QAbstractItemViewPrivate *self) {
  return new QPoint(self->offset());
}

//  const QEditorInfo &QAbstractItemViewPrivate::editorForIndex(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QEditorInfo *ritual_ZNK24QAbstractItemViewPrivate14editorForIndexERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return new QEditorInfo(self->editorForIndex(*index));
}

//  bool QAbstractItemViewPrivate::hasEditor(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate9hasEditorERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->hasEditor(*index);
}

//  QModelIndex QAbstractItemViewPrivate::indexForEditor(QWidget *editor)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QAbstractItemViewPrivate14indexForEditorEP7QWidget(
    const QAbstractItemViewPrivate *self,
    QWidget *editor) {
  return new QModelIndex(self->indexForEditor(editor));
}

//  void QAbstractItemViewPrivate::addEditor(const QModelIndex &index,
//      QWidget *editor, bool isStatic)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate9addEditorERK11QModelIndexP7QWidgetb(
    QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    QWidget *editor,
    bool isStatic) {
  self->addEditor(*index, editor, isStatic);
}

//  void QAbstractItemViewPrivate::removeEditor(QWidget *editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate12removeEditorEP7QWidget(
    QAbstractItemViewPrivate *self,
    QWidget *editor) {
  self->removeEditor(editor);
}

//  bool QAbstractItemViewPrivate::isAnimating() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate11isAnimatingEv(
    const QAbstractItemViewPrivate *self) {
  return self->isAnimating();
}

//  bool QAbstractItemViewPrivate::isIndexValid(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate12isIndexValidERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isIndexValid(*index);
}

//  bool QAbstractItemViewPrivate::isIndexSelectable(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate17isIndexSelectableERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isIndexSelectable(*index);
}

//  bool QAbstractItemViewPrivate::isIndexEnabled(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate14isIndexEnabledERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isIndexEnabled(*index);
}

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemViewPrivate::isIndexDropEnabled(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate18isIndexDropEnabledERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isIndexDropEnabled(*index);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QAbstractItemViewPrivate::isIndexDragEnabled(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate18isIndexDragEnabledERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isIndexDragEnabled(*index);
}
#endif  // QT_CONFIG(draganddrop)

//  bool QAbstractItemViewPrivate::selectionAllowed(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->selectionAllowed(*index);
}

#if QT_CONFIG(accessibility)
//  int QAbstractItemViewPrivate::accessibleChildIndex(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

#if QT_CONFIG(accessibility)
//  void QAbstractItemViewPrivate::updateItemAccessibility(const QModelIndex
//      &index, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate23updateItemAccessibilityERK11QModelIndexRK5QListIiE(
    QAbstractItemViewPrivate *self,
    const QModelIndex *index,
    const QList<int> *roles) {
  self->updateItemAccessibility(*index, *roles);
}
#endif  // QT_CONFIG(accessibility)

//  QPoint QAbstractItemViewPrivate::contentsOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK24QAbstractItemViewPrivate14contentsOffsetEv(
    const QAbstractItemViewPrivate *self) {
  return new QPoint(self->contentsOffset());
}

//  int QAbstractItemViewPrivate::delegateRefCount(const
//      QAbstractItemDelegate *delegate) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QAbstractItemViewPrivate16delegateRefCountEPK21QAbstractItemDelegate(
    const QAbstractItemViewPrivate *self,
    const QAbstractItemDelegate *delegate) {
  return self->delegateRefCount(delegate);
}

//  bool QAbstractItemViewPrivate::isPersistent(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QAbstractItemViewPrivate12isPersistentERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->isPersistent(*index);
}

#if QT_CONFIG(draganddrop)
//  QModelIndexList QAbstractItemViewPrivate::selectedDraggableIndexes()
//      const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK24QAbstractItemViewPrivate24selectedDraggableIndexesEv(
    const QAbstractItemViewPrivate *self) {
  return new QList<QModelIndex>(self->selectedDraggableIndexes());
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  void QAbstractItemViewPrivate::maybeStartDrag(QPoint eventPoint)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14maybeStartDragE6QPoint(
    QAbstractItemViewPrivate *self,
    const QPoint *eventPoint) {
  self->maybeStartDrag(*eventPoint);
}
#endif  // QT_CONFIG(draganddrop)

//  void QAbstractItemViewPrivate::doDelayedReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QAbstractItemViewPrivate14doDelayedResetEv(
    QAbstractItemViewPrivate *self) {
  self->doDelayedReset();
}

//  QRect QAbstractItemViewPrivate::visualRect(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->visualRect(*index));
}

//  QAbstractItemDelegate *QAbstractItemViewPrivate::delegateForIndex(const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK24QAbstractItemViewPrivate16delegateForIndexERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->delegateForIndex(*index);
}

//  a Python function taken by a CuteQAbstractItemViewPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstractItemViewPrivate(
    QAbstractItemViewPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstractItemViewPrivate *>(self)->take(key, call);
}

//  void QAbstractItemViewPrivate::rowsRemoved(const QModelIndex &parent, int
//      start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate11rowsRemovedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->QAbstractItemViewPrivate::rowsRemoved(*parent, start, end);
}

//  void QAbstractItemViewPrivate::rowsInserted(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate12rowsInsertedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->QAbstractItemViewPrivate::rowsInserted(*parent, start, end);
}

//  void QAbstractItemViewPrivate::columnsRemoved(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate14columnsRemovedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->QAbstractItemViewPrivate::columnsRemoved(*parent, start, end);
}

//  void QAbstractItemViewPrivate::columnsInserted(const QModelIndex &parent,
//      int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate15columnsInsertedERK11QModelIndexii(
    QAbstractItemViewPrivate *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->QAbstractItemViewPrivate::columnsInserted(*parent, start, end);
}

//  void QAbstractItemViewPrivate::modelDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate14modelDestroyedEv(
    QAbstractItemViewPrivate *self) {
  self->QAbstractItemViewPrivate::modelDestroyed();
}

//  void QAbstractItemViewPrivate::layoutChanged()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate13layoutChangedEv(
    QAbstractItemViewPrivate *self) {
  self->QAbstractItemViewPrivate::layoutChanged();
}

//  void QAbstractItemViewPrivate::rowsMoved(const QModelIndex &source, int
//      sourceStart, int sourceEnd, const QModelIndex &destination, int
//      destinationStart)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate9rowsMovedERK11QModelIndexiiS2_i(
    QAbstractItemViewPrivate *self,
    const QModelIndex *source,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destination,
    int destinationStart) {
  self->QAbstractItemViewPrivate::rowsMoved(
      *source,
      sourceStart,
      sourceEnd,
      *destination,
      destinationStart);
}

//  void QAbstractItemViewPrivate::columnsMoved(const QModelIndex &source,
//      int sourceStart, int sourceEnd, const QModelIndex &destination, int
//      destinationStart)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate12columnsMovedERK11QModelIndexiiS2_i(
    QAbstractItemViewPrivate *self,
    const QModelIndex *source,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destination,
    int destinationStart) {
  self->QAbstractItemViewPrivate::columnsMoved(
      *source,
      sourceStart,
      sourceEnd,
      *destination,
      destinationStart);
}

//  QRect QAbstractItemViewPrivate::intersectedRect(const QRect rect, const
//      QModelIndex &topLeft, const QModelIndex &bottomRight) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK24QAbstractItemViewPrivate15intersectedRectE5QRectRK11QModelIndexS3_(
    const QAbstractItemViewPrivate *self,
    const QRect *rect,
    const QModelIndex *topLeft,
    const QModelIndex *bottomRight) {
  return new QRect(
      self->QAbstractItemViewPrivate::intersectedRect(
          *rect,
          *topLeft,
          *bottomRight));
}

//  void
//      QAbstractItemViewPrivate::selectAll(QItemSelectionModel::SelectionFla
//      gs command)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QAbstractItemViewPrivate9selectAllE6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QAbstractItemViewPrivate *self,
    int command) {
  self->QAbstractItemViewPrivate::selectAll(
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void
//      QAbstractItemViewPrivate::adjustViewOptionsForIndex(QStyleOptionViewI
//      tem *a0, const QModelIndex &a1) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK24QAbstractItemViewPrivate25adjustViewOptionsForIndexEP20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    QStyleOptionViewItem *a0,
    const QModelIndex *a1) {
  self->QAbstractItemViewPrivate::adjustViewOptionsForIndex(a0, *a1);
}

//  bool QAbstractItemViewPrivate::selectionAllowed(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QAbstractItemViewPrivate16selectionAllowedERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->QAbstractItemViewPrivate::selectionAllowed(*index);
}

#if QT_CONFIG(accessibility)
//  int QAbstractItemViewPrivate::accessibleChildIndex(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QAbstractItemViewPrivate20accessibleChildIndexERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return self->QAbstractItemViewPrivate::accessibleChildIndex(*index);
}
#endif  // QT_CONFIG(accessibility)

//  QPoint QAbstractItemViewPrivate::contentsOffset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_own_ZNK24QAbstractItemViewPrivate14contentsOffsetEv(
    const QAbstractItemViewPrivate *self) {
  return new QPoint(self->QAbstractItemViewPrivate::contentsOffset());
}

//  QRect QAbstractItemViewPrivate::visualRect(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK24QAbstractItemViewPrivate10visualRectERK11QModelIndex(
    const QAbstractItemViewPrivate *self,
    const QModelIndex *index) {
  return new QRect(self->QAbstractItemViewPrivate::visualRect(*index));
}

#endif  // QT_CONFIG(itemviews)
#endif  // QT_CONFIG(itemviews)
