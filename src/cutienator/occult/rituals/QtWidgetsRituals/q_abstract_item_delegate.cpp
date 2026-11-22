//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qabstractitemdelegate.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qabstractitemdelegate.h>
#include <QtCore/qstring.h>
#include <QtWidgets/qstyleoption.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QAbstractItemDelegate::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QAbstractItemDelegate10metaObjectEv(
    const QAbstractItemDelegate *self) {
  return self->metaObject();
}

//  QString QAbstractItemDelegate::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QAbstractItemDelegate2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemDelegate::tr(s, c, n));
}

//  QAbstractItemDelegate::~QAbstractItemDelegate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QAbstractItemDelegateD1Ev(QAbstractItemDelegate *self) {
  delete self;
}

//  void QAbstractItemDelegate::paint(QPainter *painter, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate5paintEP8QPainterRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QPainter *painter,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->paint(painter, *option, *index);
}

//  QSize QAbstractItemDelegate::sizeHint(const QStyleOptionViewItem &option,
//      const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QAbstractItemDelegate8sizeHintERK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return new QSize(self->sizeHint(*option, *index));
}

//  QWidget *QAbstractItemDelegate::createEditor(QWidget *parent, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK21QAbstractItemDelegate12createEditorEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *parent,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->createEditor(parent, *option, *index);
}

//  void QAbstractItemDelegate::destroyEditor(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate13destroyEditorEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->destroyEditor(editor, *index);
}

//  void QAbstractItemDelegate::setEditorData(QWidget *editor, const
//      QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate13setEditorDataEP7QWidgetRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QModelIndex *index) {
  self->setEditorData(editor, *index);
}

//  void QAbstractItemDelegate::setModelData(QWidget *editor,
//      QAbstractItemModel *model, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate12setModelDataEP7QWidgetP18QAbstractItemModelRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    QAbstractItemModel *model,
    const QModelIndex *index) {
  self->setModelData(editor, model, *index);
}

//  void QAbstractItemDelegate::updateEditorGeometry(QWidget *editor, const
//      QStyleOptionViewItem &option, const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QAbstractItemDelegate20updateEditorGeometryEP7QWidgetRK20QStyleOptionViewItemRK11QModelIndex(
    const QAbstractItemDelegate *self,
    QWidget *editor,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  self->updateEditorGeometry(editor, *option, *index);
}

//  bool QAbstractItemDelegate::editorEvent(QEvent *event, QAbstractItemModel
//      *model, const QStyleOptionViewItem &option, const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate11editorEventEP6QEventP18QAbstractItemModelRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QEvent *event,
    QAbstractItemModel *model,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->editorEvent(event, model, *option, *index);
}

//  bool QAbstractItemDelegate::handleEditorEvent(QObject *object, QEvent
//      *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate17handleEditorEventEP7QObjectP6QEvent(
    QAbstractItemDelegate *self,
    QObject *object,
    QEvent *event) {
  return self->handleEditorEvent(object, event);
}

//  bool QAbstractItemDelegate::helpEvent(QHelpEvent *event,
//      QAbstractItemView *view, const QStyleOptionViewItem &option, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QAbstractItemDelegate9helpEventEP10QHelpEventP17QAbstractItemViewRK20QStyleOptionViewItemRK11QModelIndex(
    QAbstractItemDelegate *self,
    QHelpEvent *event,
    QAbstractItemView *view,
    const QStyleOptionViewItem *option,
    const QModelIndex *index) {
  return self->helpEvent(event, view, *option, *index);
}
