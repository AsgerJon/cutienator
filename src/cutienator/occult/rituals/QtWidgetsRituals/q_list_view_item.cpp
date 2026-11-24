//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(listview)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qlistview_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qpoint.h>

//  QListViewItem::QListViewItem()
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZN13QListViewItemC1Ev() {
  return new QListViewItem();
}

//  QListViewItem::QListViewItem(QRect r, int i)
extern "C" Q_DECL_EXPORT
QListViewItem *ritual_ZN13QListViewItemC1E5QRecti(const QRect *r, int i) {
  return new QListViewItem(*r, i);
}

//  bool QListViewItem::operator==(const QListViewItem &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QListViewItemeqERKS_(
    const QListViewItem *self,
    const QListViewItem *other) {
  return self->operator==(*other);
}

//  bool QListViewItem::operator!=(const QListViewItem &other) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QListViewItemneERKS_(
    const QListViewItem *self,
    const QListViewItem *other) {
  return self->operator!=(*other);
}

//  bool QListViewItem::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QListViewItem7isValidEv(const QListViewItem *self) {
  return self->isValid();
}

//  void QListViewItem::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QListViewItem10invalidateEv(QListViewItem *self) {
  self->invalidate();
}

//  void QListViewItem::resize(QSize size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QListViewItem6resizeE5QSize(
    QListViewItem *self,
    const QSize *size) {
  self->resize(*size);
}

//  void QListViewItem::move(QPoint position)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QListViewItem4moveE6QPoint(
    QListViewItem *self,
    const QPoint *position) {
  self->move(*position);
}

//  int QListViewItem::width() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QListViewItem5widthEv(const QListViewItem *self) {
  return self->width();
}

//  int QListViewItem::height() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK13QListViewItem6heightEv(const QListViewItem *self) {
  return self->height();
}

//  QRect QListViewItem::rect() const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK13QListViewItem4rectEv(const QListViewItem *self) {
  return new QRect(self->rect());
}

//  QListViewItem::~QListViewItem()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QListViewItemD1Ev(QListViewItem *self) {
  delete self;
}

#endif  // QT_CONFIG(listview)
