//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qstyleditemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qstyleditemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlocale.h>

//  const QMetaObject *QStyledItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QStyledItemDelegate10metaObjectEv(
    const QStyledItemDelegate *self) {
  return self->metaObject();
}

//  QString QStyledItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QStyledItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStyledItemDelegate::tr(s, c, n));
}

//  QStyledItemDelegate::QStyledItemDelegate(QObject *parent)
extern "C" Q_DECL_EXPORT
QStyledItemDelegate *ritual_ZN19QStyledItemDelegateC1EP7QObject(
    QObject *parent) {
  return new QStyledItemDelegate(parent);
}

//  QStyledItemDelegate::~QStyledItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyledItemDelegateD1Ev(QStyledItemDelegate *self) {
  delete self;
}

//  void QStyledItemDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QStyledItemDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QStyledItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QStyledItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK19QStyledItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QStyledItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QStyledItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QStyledItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK19QStyledItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QStyledItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  QItemEditorFactory *QStyledItemDelegate::itemEditorFactory() const
extern "C" Q_DECL_EXPORT
QItemEditorFactory *ritual_ZNK19QStyledItemDelegate17itemEditorFactoryEv(
    const QStyledItemDelegate *self) {
  return self->itemEditorFactory();
}

//  void QStyledItemDelegate::setItemEditorFactory(QItemEditorFactory
//      *factory)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QStyledItemDelegate20setItemEditorFactoryEP18QItemEditorFactory(
    QStyledItemDelegate *self,
    QItemEditorFactory *factory) {
  self->setItemEditorFactory(factory);
}

//  QString QStyledItemDelegate::displayText(const QVariant &value, const
//      QLocale &locale) const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QStyledItemDelegate11displayTextERK8QVariantRK7QLocale(
    const QStyledItemDelegate *self,
    const QVariant *value,
    const QLocale *locale) {
  return new QString(self->displayText(*value, *locale));
}
