//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(completer)
#if QT_CONFIG(completer)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qcompleter_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/qstyleoption.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif

//  QCompleterItemDelegate::QCompleterItemDelegate(QAbstractItemView *view)
extern "C" Q_DECL_EXPORT
QCompleterItemDelegate *ritual_ZN22QCompleterItemDelegateC1EP17QAbstractItemView(
    QAbstractItemView *view) {
  return new QCompleterItemDelegate(view);
}

//  void QCompleterItemDelegate::paint(QPainter *p, const
//      QStyleOptionViewItem &opt, const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK22QCompleterItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QCompleterItemDelegate *self,
    QPainter *p,
    const QStyleOptionViewItem *opt,
    const QModelIndex *idx) {
  self->paint(p, *opt, *idx);
}

//  void QCompleterItemDelegate::paint(QPainter *p, const
//      QStyleOptionViewItem &opt, const QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK22QCompleterItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QCompleterItemDelegate *self,
    QPainter *p,
    const QStyleOptionViewItem *opt,
    const QModelIndex *idx) {
  self->QCompleterItemDelegate::paint(p, *opt, *idx);
}

#endif  // QT_CONFIG(completer)
#endif  // QT_CONFIG(completer)
