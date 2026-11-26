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
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qlist.h>
#include <cstring>
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
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

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

//  from src/widgets/widgets/qabstractslider.cpp, line 215, as _ZN22QAbstractSliderPrivate8setStepsEii
inline void QAbstractSliderPrivate::setSteps(int single, int page)
{
    Q_Q(QAbstractSlider);
    singleStep = qAbs(single);
    pageStep = qAbs(page);
    q->sliderChange(QAbstractSlider::SliderStepsChange);
}
//  -----------------------------------------------------------------------

//  A QCommonListViewBase that Python can take functions over in. Every QCommonListViewBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(listview)
typedef int (*CuteQCommonListViewBaseCall0)(const void *, const QListViewItem *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef const QListViewItem * (*CuteQCommonListViewBaseCall1)(const void *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef bool (*CuteQCommonListViewBaseCall2)(const void *, const QListViewLayoutInfo *, int, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall3)(const void *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall4)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall5)(const void *, const QModelIndex *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall6)(const void *, int, int, bool, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef const QRect * (*CuteQCommonListViewBaseCall7)(const void *, const QRect *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef int (*CuteQCommonListViewBaseCall8)(const void *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef int (*CuteQCommonListViewBaseCall9)(const void *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall10)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall11)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall12)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall13)(const void *, int, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
typedef void (*CuteQCommonListViewBaseCall14)(const void *, const QPoint *, const QModelIndex *, int *);
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
typedef void (*CuteQCommonListViewBaseCall15)(const void *, QPainter *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQCommonListViewBaseCall16)(const void *, QDragMoveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQCommonListViewBaseCall17)(const void *, QDragLeaveEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQCommonListViewBaseCall18)(const void *, QDropEvent *, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
typedef bool (*CuteQCommonListViewBaseCall19)(const void *, int, int *);
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
class CuteQCommonListViewBase : public QCommonListViewBase {
public:
  using QCommonListViewBase::QCommonListViewBase;
  void *taken[20] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QCommonListViewBase9itemIndexERK13QListViewItem")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QCommonListViewBase19indexToListViewItemERK11QModelIndex")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase5clearEv")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase11setRowCountEi")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase11dataChangedERK11QModelIndexS2_")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase16scrollContentsByEiib")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QCommonListViewBase13mapToViewportERK5QRect")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QCommonListViewBase16horizontalOffsetEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZNK19QCommonListViewBase14verticalOffsetEv")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize")) {
      taken[10] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize")) {
      taken[11] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase15appendHiddenRowEi")) {
      taken[12] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase15removeHiddenRowEi")) {
      taken[13] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase19setPositionForIndexERK6QPointRK11QModelIndex")) {
      taken[14] = call;
      return true;
    }
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase13paintDragDropEP8QPainter")) {
      taken[15] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase19filterDragMoveEventEP14QDragMoveEvent")) {
      taken[16] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDragLeaveEvent")) {
      taken[17] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase15filterDropEventEP10QDropEvent")) {
      taken[18] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
    if (!std::strcmp(key, "_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE")) {
      taken[19] = call;
      return true;
    }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
    return false;
  }

#if QT_CONFIG(listview)
  //  int QCommonListViewBase::itemIndex(const QListViewItem &item) const
  int itemIndex(const QListViewItem &item) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQCommonListViewBaseCall0 call = reinterpret_cast<CuteQCommonListViewBaseCall0>(taken[0]);
      int given = call(this, &item, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  QListViewItem QCommonListViewBase::indexToListViewItem(const
  //      QModelIndex &index) const
  QListViewItem indexToListViewItem(
      const QModelIndex &index) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQCommonListViewBaseCall1 call = reinterpret_cast<CuteQCommonListViewBaseCall1>(taken[1]);
      const QListViewItem * given = call(this, &index, &handled);
      if (handled && given) return *given;
    }
    return {};
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  bool QCommonListViewBase::doBatchedItemLayout(const
  //      QListViewLayoutInfo &info, int max)
  bool doBatchedItemLayout(
      const QListViewLayoutInfo &info,
      int max) override {
    if (taken[2]) {
      int handled = 0;
      CuteQCommonListViewBaseCall2 call = reinterpret_cast<CuteQCommonListViewBaseCall2>(taken[2]);
      bool given = call(this, &info, max, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::clear()
  void clear() override {
    if (taken[3]) {
      int handled = 0;
      CuteQCommonListViewBaseCall3 call = reinterpret_cast<CuteQCommonListViewBaseCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::setRowCount(int a0)
  void setRowCount(int a0) override {
    if (taken[4]) {
      int handled = 0;
      CuteQCommonListViewBaseCall4 call = reinterpret_cast<CuteQCommonListViewBaseCall4>(taken[4]);
      call(this, a0, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::dataChanged(const QModelIndex &a0, const
  //      QModelIndex &a1)
  void dataChanged(const QModelIndex &a0, const QModelIndex &a1) override {
    if (taken[5]) {
      int handled = 0;
      CuteQCommonListViewBaseCall5 call = reinterpret_cast<CuteQCommonListViewBaseCall5>(taken[5]);
      call(this, &a0, &a1, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::scrollContentsBy(int dx, int dy, bool
  //      scrollElasticBand)
  void scrollContentsBy(int dx, int dy, bool scrollElasticBand) override {
    if (taken[6]) {
      int handled = 0;
      CuteQCommonListViewBaseCall6 call = reinterpret_cast<CuteQCommonListViewBaseCall6>(taken[6]);
      call(this, dx, dy, scrollElasticBand, &handled);
      if (handled) return;
    }
    QCommonListViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  QRect QCommonListViewBase::mapToViewport(const QRect &rect) const
  QRect mapToViewport(const QRect &rect) const override {
    if (taken[7]) {
      int handled = 0;
      CuteQCommonListViewBaseCall7 call = reinterpret_cast<CuteQCommonListViewBaseCall7>(taken[7]);
      const QRect * given = call(this, &rect, &handled);
      if (handled && given) return *given;
    }
    return QCommonListViewBase::mapToViewport(rect);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  int QCommonListViewBase::horizontalOffset() const
  int horizontalOffset() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQCommonListViewBaseCall8 call = reinterpret_cast<CuteQCommonListViewBaseCall8>(taken[8]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::horizontalOffset();
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  int QCommonListViewBase::verticalOffset() const
  int verticalOffset() const override {
    if (taken[9]) {
      int handled = 0;
      CuteQCommonListViewBaseCall9 call = reinterpret_cast<CuteQCommonListViewBaseCall9>(taken[9]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::verticalOffset();
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::updateHorizontalScrollBar(const QSize
  //      &step)
  void updateHorizontalScrollBar(const QSize &step) override {
    if (taken[10]) {
      int handled = 0;
      CuteQCommonListViewBaseCall10 call = reinterpret_cast<CuteQCommonListViewBaseCall10>(taken[10]);
      call(this, &step, &handled);
      if (handled) return;
    }
    QCommonListViewBase::updateHorizontalScrollBar(step);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::updateVerticalScrollBar(const QSize &step)
  void updateVerticalScrollBar(const QSize &step) override {
    if (taken[11]) {
      int handled = 0;
      CuteQCommonListViewBaseCall11 call = reinterpret_cast<CuteQCommonListViewBaseCall11>(taken[11]);
      call(this, &step, &handled);
      if (handled) return;
    }
    QCommonListViewBase::updateVerticalScrollBar(step);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::appendHiddenRow(int row)
  void appendHiddenRow(int row) override {
    if (taken[12]) {
      int handled = 0;
      CuteQCommonListViewBaseCall12 call = reinterpret_cast<CuteQCommonListViewBaseCall12>(taken[12]);
      call(this, row, &handled);
      if (handled) return;
    }
    QCommonListViewBase::appendHiddenRow(row);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::removeHiddenRow(int row)
  void removeHiddenRow(int row) override {
    if (taken[13]) {
      int handled = 0;
      CuteQCommonListViewBaseCall13 call = reinterpret_cast<CuteQCommonListViewBaseCall13>(taken[13]);
      call(this, row, &handled);
      if (handled) return;
    }
    QCommonListViewBase::removeHiddenRow(row);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
  //  void QCommonListViewBase::setPositionForIndex(const QPoint &a0, const
  //      QModelIndex &a1)
  void setPositionForIndex(
      const QPoint &a0,
      const QModelIndex &a1) override {
    if (taken[14]) {
      int handled = 0;
      CuteQCommonListViewBaseCall14 call = reinterpret_cast<CuteQCommonListViewBaseCall14>(taken[14]);
      call(this, &a0, &a1, &handled);
      if (handled) return;
    }
    QCommonListViewBase::setPositionForIndex(a0, a1);
  }
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
  //  void QCommonListViewBase::paintDragDrop(QPainter *painter)
  void paintDragDrop(QPainter *painter) override {
    if (taken[15]) {
      int handled = 0;
      CuteQCommonListViewBaseCall15 call = reinterpret_cast<CuteQCommonListViewBaseCall15>(taken[15]);
      call(this, painter, &handled);
      if (handled) return;
    }
    QCommonListViewBase::paintDragDrop(painter);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
  //  bool QCommonListViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
  bool filterDragMoveEvent(QDragMoveEvent *a0) override {
    if (taken[16]) {
      int handled = 0;
      CuteQCommonListViewBaseCall16 call = reinterpret_cast<CuteQCommonListViewBaseCall16>(taken[16]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::filterDragMoveEvent(a0);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
  //  bool QCommonListViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
  bool filterDragLeaveEvent(QDragLeaveEvent *a0) override {
    if (taken[17]) {
      int handled = 0;
      CuteQCommonListViewBaseCall17 call = reinterpret_cast<CuteQCommonListViewBaseCall17>(taken[17]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::filterDragLeaveEvent(a0);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
  //  bool QCommonListViewBase::filterDropEvent(QDropEvent *a0)
  bool filterDropEvent(QDropEvent *a0) override {
    if (taken[18]) {
      int handled = 0;
      CuteQCommonListViewBaseCall18 call = reinterpret_cast<CuteQCommonListViewBaseCall18>(taken[18]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::filterDropEvent(a0);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)

#if QT_CONFIG(listview)
#if QT_CONFIG(draganddrop)
  //  bool QCommonListViewBase::filterStartDrag(Qt::DropActions a0)
  bool filterStartDrag(Qt::DropActions a0) override {
    if (taken[19]) {
      int handled = 0;
      CuteQCommonListViewBaseCall19 call = reinterpret_cast<CuteQCommonListViewBaseCall19>(taken[19]);
      bool given = call(this, static_cast<int>(a0.toInt()), &handled);
      if (handled) return given;
    }
    return QCommonListViewBase::filterStartDrag(a0);
  }
#endif  // QT_CONFIG(draganddrop)
#endif  // QT_CONFIG(listview)
};

//  QCommonListViewBase::~QCommonListViewBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBaseD1Ev(QCommonListViewBase *self) {
  delete self;
}

//  int QCommonListViewBase::itemIndex(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase9itemIndexERK13QListViewItem(
    const QCommonListViewBase *self,
    const QListViewItem *item) {
  return self->itemIndex(*item);
}

//  QListViewItem QCommonListViewBase::indexToListViewItem(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZNK19QCommonListViewBase19indexToListViewItemERK11QModelIndex(
    const QCommonListViewBase *self,
    const QModelIndex *index) {
  return new QListViewItem(self->indexToListViewItem(*index));
}

//  bool QCommonListViewBase::doBatchedItemLayout(const QListViewLayoutInfo
//      &info, int max)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonListViewBase19doBatchedItemLayoutERK19QListViewLayoutInfoi(
    QCommonListViewBase *self,
    const QListViewLayoutInfo *info,
    int max) {
  return self->doBatchedItemLayout(*info, max);
}

//  void QCommonListViewBase::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase5clearEv(QCommonListViewBase *self) {
  self->clear();
}

//  void QCommonListViewBase::setRowCount(int a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase11setRowCountEi(
    QCommonListViewBase *self,
    int a0) {
  self->setRowCount(a0);
}

//  QList<QModelIndex> QCommonListViewBase::intersectingSet(const QRect
//      &area) const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK19QCommonListViewBase15intersectingSetERK5QRect(
    const QCommonListViewBase *self,
    const QRect *area) {
  return new QList<QModelIndex>(self->intersectingSet(*area));
}

//  void QCommonListViewBase::dataChanged(const QModelIndex &a0, const
//      QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase11dataChangedERK11QModelIndexS2_(
    QCommonListViewBase *self,
    const QModelIndex *a0,
    const QModelIndex *a1) {
  self->dataChanged(*a0, *a1);
}

//  int QCommonListViewBase::horizontalScrollToValue(int index,
//      QListView::ScrollHint hint, bool leftOf, bool rightOf, const QRect
//      &area, const QRect &rect) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase23horizontalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_(
    const QCommonListViewBase *self,
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

//  int QCommonListViewBase::verticalScrollToValue(int index,
//      QListView::ScrollHint hint, bool above, bool below, const QRect
//      &area, const QRect &rect) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase21verticalScrollToValueEiN17QAbstractItemView10ScrollHintEbbRK5QRectS4_(
    const QCommonListViewBase *self,
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

//  void QCommonListViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase16scrollContentsByEiib(
    QCommonListViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->scrollContentsBy(dx, dy, scrollElasticBand);
}

//  QRect QCommonListViewBase::mapToViewport(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QCommonListViewBase13mapToViewportERK5QRect(
    const QCommonListViewBase *self,
    const QRect *rect) {
  return new QRect(self->mapToViewport(*rect));
}

//  int QCommonListViewBase::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase16horizontalOffsetEv(
    const QCommonListViewBase *self) {
  return self->horizontalOffset();
}

//  int QCommonListViewBase::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase14verticalOffsetEv(
    const QCommonListViewBase *self) {
  return self->verticalOffset();
}

//  void QCommonListViewBase::updateHorizontalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize(
    QCommonListViewBase *self,
    const QSize *step) {
  self->updateHorizontalScrollBar(*step);
}

//  void QCommonListViewBase::updateVerticalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize(
    QCommonListViewBase *self,
    const QSize *step) {
  self->updateVerticalScrollBar(*step);
}

//  void QCommonListViewBase::appendHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase15appendHiddenRowEi(
    QCommonListViewBase *self,
    int row) {
  self->appendHiddenRow(row);
}

//  void QCommonListViewBase::removeHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase15removeHiddenRowEi(
    QCommonListViewBase *self,
    int row) {
  self->removeHiddenRow(row);
}

//  void QCommonListViewBase::setPositionForIndex(const QPoint &a0, const
//      QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase19setPositionForIndexERK6QPointRK11QModelIndex(
    QCommonListViewBase *self,
    const QPoint *a0,
    const QModelIndex *a1) {
  self->setPositionForIndex(*a0, *a1);
}

#if QT_CONFIG(draganddrop)
//  void QCommonListViewBase::paintDragDrop(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QCommonListViewBase13paintDragDropEP8QPainter(
    QCommonListViewBase *self,
    QPainter *painter) {
  self->paintDragDrop(painter);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonListViewBase19filterDragMoveEventEP14QDragMoveEvent(
    QCommonListViewBase *self,
    QDragMoveEvent *a0) {
  return self->filterDragMoveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDragLeaveEvent(
    QCommonListViewBase *self,
    QDragLeaveEvent *a0) {
  return self->filterDragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonListViewBase15filterDropEventEP10QDropEvent(
    QCommonListViewBase *self,
    QDropEvent *a0) {
  return self->filterDropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterStartDrag(Qt::DropActions a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE(
    QCommonListViewBase *self,
    int a0) {
  return self->filterStartDrag(QFlags<Qt::DropAction>::fromInt(a0));
}
#endif  // QT_CONFIG(draganddrop)

//  int QCommonListViewBase::spacing() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase7spacingEv(
    const QCommonListViewBase *self) {
  return self->spacing();
}

//  bool QCommonListViewBase::isWrapping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCommonListViewBase10isWrappingEv(
    const QCommonListViewBase *self) {
  return self->isWrapping();
}

//  QSize QCommonListViewBase::gridSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QCommonListViewBase8gridSizeEv(
    const QCommonListViewBase *self) {
  return new QSize(self->gridSize());
}

//  QListView::Flow QCommonListViewBase::flow() const
extern "C" Q_DECL_EXPORT
QListView::Flow ritual_ZNK19QCommonListViewBase4flowEv(
    const QCommonListViewBase *self) {
  return self->flow();
}

//  QListView::Movement QCommonListViewBase::movement() const
extern "C" Q_DECL_EXPORT
QListView::Movement ritual_ZNK19QCommonListViewBase8movementEv(
    const QCommonListViewBase *self) {
  return self->movement();
}

//  QPoint QCommonListViewBase::offset() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QCommonListViewBase6offsetEv(
    const QCommonListViewBase *self) {
  return new QPoint(self->offset());
}

//  QPoint QCommonListViewBase::pressedPosition() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK19QCommonListViewBase15pressedPositionEv(
    const QCommonListViewBase *self) {
  return new QPoint(self->pressedPosition());
}

//  bool QCommonListViewBase::uniformItemSizes() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCommonListViewBase16uniformItemSizesEv(
    const QCommonListViewBase *self) {
  return self->uniformItemSizes();
}

//  int QCommonListViewBase::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase6columnEv(
    const QCommonListViewBase *self) {
  return self->column();
}

//  QScrollBar *QCommonListViewBase::verticalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QCommonListViewBase17verticalScrollBarEv(
    const QCommonListViewBase *self) {
  return self->verticalScrollBar();
}

//  QScrollBar *QCommonListViewBase::horizontalScrollBar() const
extern "C" Q_DECL_EXPORT
QScrollBar *ritual_ZNK19QCommonListViewBase19horizontalScrollBarEv(
    const QCommonListViewBase *self) {
  return self->horizontalScrollBar();
}

//  QListView::ScrollMode QCommonListViewBase::verticalScrollMode() const
extern "C" Q_DECL_EXPORT
QListView::ScrollMode *ritual_ZNK19QCommonListViewBase18verticalScrollModeEv(
    const QCommonListViewBase *self) {
  return new QListView::ScrollMode(self->verticalScrollMode());
}

//  QListView::ScrollMode QCommonListViewBase::horizontalScrollMode() const
extern "C" Q_DECL_EXPORT
QListView::ScrollMode *ritual_ZNK19QCommonListViewBase20horizontalScrollModeEv(
    const QCommonListViewBase *self) {
  return new QListView::ScrollMode(self->horizontalScrollMode());
}

//  QModelIndex QCommonListViewBase::modelIndex(int row) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QCommonListViewBase10modelIndexEi(
    const QCommonListViewBase *self,
    int row) {
  return new QModelIndex(self->modelIndex(row));
}

//  int QCommonListViewBase::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase8rowCountEv(
    const QCommonListViewBase *self) {
  return self->rowCount();
}

//  void QCommonListViewBase::initViewItemOption(QStyleOptionViewItem
//      *option) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QCommonListViewBase18initViewItemOptionEP20QStyleOptionViewItem(
    const QCommonListViewBase *self,
    QStyleOptionViewItem *option) {
  self->initViewItemOption(option);
}

//  QWidget *QCommonListViewBase::viewport() const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QCommonListViewBase8viewportEv(
    const QCommonListViewBase *self) {
  return self->viewport();
}

//  QRect QCommonListViewBase::clipRect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QCommonListViewBase8clipRectEv(
    const QCommonListViewBase *self) {
  return new QRect(self->clipRect());
}

//  QSize QCommonListViewBase::cachedItemSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QCommonListViewBase14cachedItemSizeEv(
    const QCommonListViewBase *self) {
  return new QSize(self->cachedItemSize());
}

//  QRect QCommonListViewBase::viewItemRect(const QListViewItem &item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK19QCommonListViewBase12viewItemRectERK13QListViewItem(
    const QCommonListViewBase *self,
    const QListViewItem *item) {
  return new QRect(self->viewItemRect(*item));
}

//  QSize QCommonListViewBase::itemSize(const QStyleOptionViewItem &opt,
//      const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QCommonListViewBase8itemSizeERK20QStyleOptionViewItemRK11QModelIndex(
    const QCommonListViewBase *self,
    const QStyleOptionViewItem *opt,
    const QModelIndex *idx) {
  return new QSize(self->itemSize(*opt, *idx));
}

//  QAbstractItemDelegate *QCommonListViewBase::delegate(const QModelIndex
//      &idx) const
extern "C" Q_DECL_EXPORT
QAbstractItemDelegate *ritual_ZNK19QCommonListViewBase8delegateERK11QModelIndex(
    const QCommonListViewBase *self,
    const QModelIndex *idx) {
  return self->delegate(*idx);
}

//  bool QCommonListViewBase::isHidden(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCommonListViewBase8isHiddenEi(
    const QCommonListViewBase *self,
    int row) {
  return self->isHidden(row);
}

//  int QCommonListViewBase::hiddenCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QCommonListViewBase11hiddenCountEv(
    const QCommonListViewBase *self) {
  return self->hiddenCount();
}

//  bool QCommonListViewBase::isRightToLeft() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QCommonListViewBase13isRightToLeftEv(
    const QCommonListViewBase *self) {
  return self->isRightToLeft();
}

//  a Python function taken by a CuteQCommonListViewBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QCommonListViewBase(
    QCommonListViewBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQCommonListViewBase *>(self)->take(key, call);
}

//  void QCommonListViewBase::scrollContentsBy(int dx, int dy, bool
//      scrollElasticBand)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase16scrollContentsByEiib(
    QCommonListViewBase *self,
    int dx,
    int dy,
    bool scrollElasticBand) {
  self->QCommonListViewBase::scrollContentsBy(dx, dy, scrollElasticBand);
}

//  QRect QCommonListViewBase::mapToViewport(const QRect &rect) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK19QCommonListViewBase13mapToViewportERK5QRect(
    const QCommonListViewBase *self,
    const QRect *rect) {
  return new QRect(self->QCommonListViewBase::mapToViewport(*rect));
}

//  int QCommonListViewBase::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QCommonListViewBase16horizontalOffsetEv(
    const QCommonListViewBase *self) {
  return self->QCommonListViewBase::horizontalOffset();
}

//  int QCommonListViewBase::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QCommonListViewBase14verticalOffsetEv(
    const QCommonListViewBase *self) {
  return self->QCommonListViewBase::verticalOffset();
}

//  void QCommonListViewBase::updateHorizontalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase25updateHorizontalScrollBarERK5QSize(
    QCommonListViewBase *self,
    const QSize *step) {
  self->QCommonListViewBase::updateHorizontalScrollBar(*step);
}

//  void QCommonListViewBase::updateVerticalScrollBar(const QSize &step)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase23updateVerticalScrollBarERK5QSize(
    QCommonListViewBase *self,
    const QSize *step) {
  self->QCommonListViewBase::updateVerticalScrollBar(*step);
}

//  void QCommonListViewBase::appendHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase15appendHiddenRowEi(
    QCommonListViewBase *self,
    int row) {
  self->QCommonListViewBase::appendHiddenRow(row);
}

//  void QCommonListViewBase::removeHiddenRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase15removeHiddenRowEi(
    QCommonListViewBase *self,
    int row) {
  self->QCommonListViewBase::removeHiddenRow(row);
}

//  void QCommonListViewBase::setPositionForIndex(const QPoint &a0, const
//      QModelIndex &a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase19setPositionForIndexERK6QPointRK11QModelIndex(
    QCommonListViewBase *self,
    const QPoint *a0,
    const QModelIndex *a1) {
  self->QCommonListViewBase::setPositionForIndex(*a0, *a1);
}

#if QT_CONFIG(draganddrop)
//  void QCommonListViewBase::paintDragDrop(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QCommonListViewBase13paintDragDropEP8QPainter(
    QCommonListViewBase *self,
    QPainter *painter) {
  self->QCommonListViewBase::paintDragDrop(painter);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDragMoveEvent(QDragMoveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QCommonListViewBase19filterDragMoveEventEP14QDragMoveEvent(
    QCommonListViewBase *self,
    QDragMoveEvent *a0) {
  return self->QCommonListViewBase::filterDragMoveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDragLeaveEvent(QDragLeaveEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QCommonListViewBase20filterDragLeaveEventEP15QDragLeaveEvent(
    QCommonListViewBase *self,
    QDragLeaveEvent *a0) {
  return self->QCommonListViewBase::filterDragLeaveEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterDropEvent(QDropEvent *a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QCommonListViewBase15filterDropEventEP10QDropEvent(
    QCommonListViewBase *self,
    QDropEvent *a0) {
  return self->QCommonListViewBase::filterDropEvent(a0);
}
#endif  // QT_CONFIG(draganddrop)

#if QT_CONFIG(draganddrop)
//  bool QCommonListViewBase::filterStartDrag(Qt::DropActions a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QCommonListViewBase15filterStartDragE6QFlagsIN2Qt10DropActionEE(
    QCommonListViewBase *self,
    int a0) {
  return self->QCommonListViewBase::filterStartDrag(
      QFlags<Qt::DropAction>::fromInt(a0));
}
#endif  // QT_CONFIG(draganddrop)

//  a QListView::ScrollMode a ritual of QCommonListViewBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QCommonListViewBase__QListView_ScrollMode(
    QListView::ScrollMode *self) {
  delete self;
}

#endif  // QT_CONFIG(listview)
#endif  // QT_CONFIG(listview)
