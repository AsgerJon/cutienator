//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
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
#include <qglobal.h>
#include "qcolumnview.h"
#if QT_CONFIG(columnview)
#include "qcolumnview_p.h"
#include "qcolumnviewgrip_p.h"
#include <qlistview.h>
#include <qabstractitemdelegate.h>
#include <qscrollbar.h>
#include <qpainter.h>
#include <qdebug.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/itemviews/qcolumnview.cpp, line 1095, as _ZN18QColumnViewPrivate15columnsInsertedERK11QModelIndexii
#if QT_CONFIG(columnview)
inline void QColumnViewPrivate::columnsInserted(const QModelIndex &parent, int start, int end)
{
    QAbstractItemViewPrivate::columnsInserted(parent, start, end);
    checkColumnCreation(parent);
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
