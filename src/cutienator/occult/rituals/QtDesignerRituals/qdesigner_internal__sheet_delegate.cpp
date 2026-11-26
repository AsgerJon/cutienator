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
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#endif
#include <QtCore/qsize.h>

//  const QMetaObject *qdesigner_internal::SheetDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18qdesigner_internal13SheetDelegate10metaObjectEv(
    const qdesigner_internal::SheetDelegate *self) {
  return self->metaObject();
}

//  void *qdesigner_internal::SheetDelegate::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN18qdesigner_internal13SheetDelegate11qt_metacastEPKc(
    qdesigner_internal::SheetDelegate *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int qdesigner_internal::SheetDelegate::qt_metacall(QMetaObject::Call a0,
//      int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal13SheetDelegate11qt_metacallEN11QMetaObject4CallEiPPv(
    qdesigner_internal::SheetDelegate *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
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

//  qdesigner_internal::SheetDelegate::SheetDelegate(QTreeView *view, QWidget
//      *parent)
extern "C" Q_DECL_EXPORT
qdesigner_internal::SheetDelegate *ritual_ZN18qdesigner_internal13SheetDelegateC1EP9QTreeViewP7QWidget(
    QTreeView *view,
    QWidget *parent) {
  return new qdesigner_internal::SheetDelegate(view, parent);
}

//  void qdesigner_internal::SheetDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal13SheetDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const qdesigner_internal::SheetDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize qdesigner_internal::SheetDelegate::sizeHint(const
//      QStyleOptionViewItem &opt, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal13SheetDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const qdesigner_internal::SheetDelegate *self,
    const QStyleOptionViewItem *opt,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*opt, *index));
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
