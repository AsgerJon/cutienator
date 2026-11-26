//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(columnview)
#if QT_CONFIG(columnview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcolumnview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qrect.h>
#include <QtCore/qpoint.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qitemselectionmodel.h>
#endif
#include <QtGui/qregion.h>

//  QColumnViewPreviewColumn::QColumnViewPreviewColumn(QWidget *parent)
extern "C" Q_DECL_EXPORT
QColumnViewPreviewColumn *ritual_ZN24QColumnViewPreviewColumnC1EP7QWidget(
    QWidget *parent) {
  return new QColumnViewPreviewColumn(parent);
}

//  void QColumnViewPreviewColumn::setPreviewWidget(QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QColumnViewPreviewColumn16setPreviewWidgetEP7QWidget(
    QColumnViewPreviewColumn *self,
    QWidget *widget) {
  self->setPreviewWidget(widget);
}

//  void QColumnViewPreviewColumn::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QColumnViewPreviewColumn11resizeEventEP12QResizeEvent(
    QColumnViewPreviewColumn *self,
    QResizeEvent *event) {
  self->resizeEvent(event);
}

//  void QColumnViewPreviewColumn::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QColumnViewPreviewColumn16scrollContentsByEii(
    QColumnViewPreviewColumn *self,
    int dx,
    int dy) {
  self->scrollContentsBy(dx, dy);
}

//  QRect QColumnViewPreviewColumn::visualRect(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK24QColumnViewPreviewColumn10visualRectERK11QModelIndex(
    const QColumnViewPreviewColumn *self,
    const QModelIndex *a0) {
  return new QRect(self->visualRect(*a0));
}

//  void QColumnViewPreviewColumn::scrollTo(const QModelIndex &a0, ScrollHint
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QColumnViewPreviewColumn8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QColumnViewPreviewColumn *self,
    const QModelIndex *a0,
    QAbstractItemView::ScrollHint a1) {
  self->scrollTo(*a0, a1);
}

//  QModelIndex QColumnViewPreviewColumn::indexAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK24QColumnViewPreviewColumn7indexAtERK6QPoint(
    const QColumnViewPreviewColumn *self,
    const QPoint *a0) {
  return new QModelIndex(self->indexAt(*a0));
}

//  QModelIndex QColumnViewPreviewColumn::moveCursor(CursorAction a0,
//      Qt::KeyboardModifiers a1)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN24QColumnViewPreviewColumn10moveCursorEN17QAbstractItemView12CursorActionE6QFlagsIN2Qt16KeyboardModifierEE(
    QColumnViewPreviewColumn *self,
    QAbstractItemView::CursorAction a0,
    int a1) {
  return new QModelIndex(
      self->moveCursor(
          a0,
          QFlags<Qt::KeyboardModifier>::fromInt(a1)));
}

//  int QColumnViewPreviewColumn::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QColumnViewPreviewColumn16horizontalOffsetEv(
    const QColumnViewPreviewColumn *self) {
  return self->horizontalOffset();
}

//  int QColumnViewPreviewColumn::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK24QColumnViewPreviewColumn14verticalOffsetEv(
    const QColumnViewPreviewColumn *self) {
  return self->verticalOffset();
}

//  QRegion QColumnViewPreviewColumn::visualRegionForSelection(const
//      QItemSelection &a0) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZNK24QColumnViewPreviewColumn24visualRegionForSelectionERK14QItemSelection(
    const QColumnViewPreviewColumn *self,
    const QItemSelection *a0) {
  return new QRegion(self->visualRegionForSelection(*a0));
}

//  bool QColumnViewPreviewColumn::isIndexHidden(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QColumnViewPreviewColumn13isIndexHiddenERK11QModelIndex(
    const QColumnViewPreviewColumn *self,
    const QModelIndex *a0) {
  return self->isIndexHidden(*a0);
}

//  void QColumnViewPreviewColumn::setSelection(const QRect &a0,
//      QItemSelectionModel::SelectionFlags a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QColumnViewPreviewColumn12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QColumnViewPreviewColumn *self,
    const QRect *a0,
    int a1) {
  self->setSelection(
      *a0,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(a1));
}

//  void QColumnViewPreviewColumn::resizeEvent(QResizeEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QColumnViewPreviewColumn11resizeEventEP12QResizeEvent(
    QColumnViewPreviewColumn *self,
    QResizeEvent *event) {
  self->QColumnViewPreviewColumn::resizeEvent(event);
}

//  void QColumnViewPreviewColumn::scrollContentsBy(int dx, int dy)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QColumnViewPreviewColumn16scrollContentsByEii(
    QColumnViewPreviewColumn *self,
    int dx,
    int dy) {
  self->QColumnViewPreviewColumn::scrollContentsBy(dx, dy);
}

//  QRect QColumnViewPreviewColumn::visualRect(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
QRect *ritual_own_ZNK24QColumnViewPreviewColumn10visualRectERK11QModelIndex(
    const QColumnViewPreviewColumn *self,
    const QModelIndex *a0) {
  return new QRect(self->QColumnViewPreviewColumn::visualRect(*a0));
}

//  void QColumnViewPreviewColumn::scrollTo(const QModelIndex &a0, ScrollHint
//      a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QColumnViewPreviewColumn8scrollToERK11QModelIndexN17QAbstractItemView10ScrollHintE(
    QColumnViewPreviewColumn *self,
    const QModelIndex *a0,
    QAbstractItemView::ScrollHint a1) {
  self->QColumnViewPreviewColumn::scrollTo(*a0, a1);
}

//  QModelIndex QColumnViewPreviewColumn::indexAt(const QPoint &a0) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK24QColumnViewPreviewColumn7indexAtERK6QPoint(
    const QColumnViewPreviewColumn *self,
    const QPoint *a0) {
  return new QModelIndex(self->QColumnViewPreviewColumn::indexAt(*a0));
}

//  int QColumnViewPreviewColumn::horizontalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QColumnViewPreviewColumn16horizontalOffsetEv(
    const QColumnViewPreviewColumn *self) {
  return self->QColumnViewPreviewColumn::horizontalOffset();
}

//  int QColumnViewPreviewColumn::verticalOffset() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK24QColumnViewPreviewColumn14verticalOffsetEv(
    const QColumnViewPreviewColumn *self) {
  return self->QColumnViewPreviewColumn::verticalOffset();
}

//  QRegion QColumnViewPreviewColumn::visualRegionForSelection(const
//      QItemSelection &a0) const
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZNK24QColumnViewPreviewColumn24visualRegionForSelectionERK14QItemSelection(
    const QColumnViewPreviewColumn *self,
    const QItemSelection *a0) {
  return new QRegion(
      self->QColumnViewPreviewColumn::visualRegionForSelection(
          *a0));
}

//  bool QColumnViewPreviewColumn::isIndexHidden(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QColumnViewPreviewColumn13isIndexHiddenERK11QModelIndex(
    const QColumnViewPreviewColumn *self,
    const QModelIndex *a0) {
  return self->QColumnViewPreviewColumn::isIndexHidden(*a0);
}

//  void QColumnViewPreviewColumn::setSelection(const QRect &a0,
//      QItemSelectionModel::SelectionFlags a1)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QColumnViewPreviewColumn12setSelectionERK5QRect6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QColumnViewPreviewColumn *self,
    const QRect *a0,
    int a1) {
  self->QColumnViewPreviewColumn::setSelection(
      *a0,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(a1));
}

#endif  // QT_CONFIG(columnview)
#endif  // QT_CONFIG(columnview)
