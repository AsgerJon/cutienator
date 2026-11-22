//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qitemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qitemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK13QItemDelegate10metaObjectEv(
    const QItemDelegate *self) {
  return self->metaObject();
}

//  QString QItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN13QItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QItemDelegate::tr(s, c, n));
}

//  QItemDelegate::QItemDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QItemDelegate *ritual_ZN13QItemDelegateC1EP7QObject(QObject *parent) {
  return new QItemDelegate(parent);
}

//  QItemDelegate::~QItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegateD1Ev(QItemDelegate *self) {
  delete self;
}

//  bool QItemDelegate::hasClipping() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK13QItemDelegate11hasClippingEv(const QItemDelegate *self) {
  return self->hasClipping();
}

//  void QItemDelegate::setClipping(bool clip)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegate11setClippingEb(
    QItemDelegate *self,
    bool clip) {
  self->setClipping(clip);
}

//  void QItemDelegate::paint(QPainter *painter, const QStyleOptionViewItem
//      &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QItemDelegate::sizeHint(const QStyleOptionViewItem &option, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK13QItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK13QItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QItemDelegate::setEditorData(QWidget *editor, const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QItemDelegate::setModelData(QWidget *editor, QAbstractItemModel
//      *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK13QItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  QItemEditorFactory *QItemDelegate::itemEditorFactory() const
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZNK13QItemDelegate17itemEditorFactoryEv(
    const QItemDelegate *self) {
  return self->itemEditorFactory();
}

//  void QItemDelegate::setItemEditorFactory(QItemEditorFactory *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QItemDelegate20setItemEditorFactoryEP18QItemEditorFactory(
    QItemDelegate *self,
    QItemEditorFactory *factory) {
  self->setItemEditorFactory(factory);
}
