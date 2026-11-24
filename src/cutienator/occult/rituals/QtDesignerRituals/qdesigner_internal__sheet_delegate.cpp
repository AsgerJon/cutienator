//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/sheet_delegate_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/sheet_delegate_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>

//  const QMetaObject *qdesigner_internal::SheetDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal13SheetDelegate10metaObjectEv(
    const qdesigner_internal::SheetDelegate *self) {
  return self->metaObject();
}

//  QString qdesigner_internal::SheetDelegate::tr(const char *s, const char
//      *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18qdesigner_internal13SheetDelegate2trEPKcS2_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(qdesigner_internal::SheetDelegate::tr(s, c, n));
}

//  void qdesigner_internal::SheetDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_own_ZNK18qdesigner_internal13SheetDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const qdesigner_internal::SheetDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->qdesigner_internal::SheetDelegate::paint(painter, *option, *index);
}

//  QSize qdesigner_internal::SheetDelegate::sizeHint(const
//      QStyleOptionViewItem &opt, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_own_ZNK18qdesigner_internal13SheetDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const qdesigner_internal::SheetDelegate *self,
    const QStyleOptionViewItem *opt,
    const QModelIndex *index) {
  return new QSize(
      self->qdesigner_internal::SheetDelegate::sizeHint(
          *opt,
          *index));
}
