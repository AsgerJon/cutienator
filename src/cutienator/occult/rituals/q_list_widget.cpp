//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qlistwidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qlistwidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QListWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QListWidget10metaObjectEv(
    const QListWidget *self) {
  return self->metaObject();
}

//  QString QListWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QListWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QListWidget::tr(s, c, n));
}

//  QListWidget::QListWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QListWidget *ritual_ZN11QListWidgetC1EP7QWidget(QWidget *parent) {
  return new QListWidget(parent);
}

//  QListWidget::~QListWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidgetD1Ev(QListWidget *self) {
  delete self;
}

//  void QListWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget17setSelectionModelEP19QItemSelectionModel(
    QListWidget *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  QListWidgetItem *QListWidget::item(int row) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget4itemEi(
    const QListWidget *self,
    int row) {
  return self->item(row);
}

//  int QListWidget::row(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget3rowEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return self->row(item);
}

//  void QListWidget::insertItem(int row, QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget10insertItemEiP15QListWidgetItem(
    QListWidget *self,
    int row,
    QListWidgetItem *item) {
  self->insertItem(row, item);
}

//  void QListWidget::insertItem(int row, const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget10insertItemEiRK7QString(
    QListWidget *self,
    int row,
    const QString *label) {
  self->insertItem(row, *label);
}

//  void QListWidget::addItem(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget7addItemERK7QString(
    QListWidget *self,
    const QString *label) {
  self->addItem(*label);
}

//  void QListWidget::addItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget7addItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->addItem(item);
}

//  QListWidgetItem *QListWidget::takeItem(int row)
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZN11QListWidget8takeItemEi(
    QListWidget *self,
    int row) {
  return self->takeItem(row);
}

//  int QListWidget::count() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget5countEv(const QListWidget *self) {
  return self->count();
}

//  QListWidgetItem *QListWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget11currentItemEv(
    const QListWidget *self) {
  return self->currentItem();
}

//  void QListWidget::setCurrentItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QListWidget::setCurrentItem(QListWidgetItem *item,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget14setCurrentItemEP15QListWidgetItem6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListWidget *self,
    QListWidgetItem *item,
    int command) {
  self->setCurrentItem(
      item,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  int QListWidget::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget10currentRowEv(const QListWidget *self) {
  return self->currentRow();
}

//  void QListWidget::setCurrentRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setCurrentRowEi(QListWidget *self, int row) {
  self->setCurrentRow(row);
}

//  void QListWidget::setCurrentRow(int row,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setCurrentRowEi6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QListWidget *self,
    int row,
    int command) {
  self->setCurrentRow(
      row,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QListWidgetItem *QListWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget6itemAtERK6QPoint(
    const QListWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QListWidgetItem *QListWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget6itemAtEii(
    const QListWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QListWidget::visualItemRect(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QListWidget14visualItemRectEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  void QListWidget::sortItems(Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget9sortItemsEN2Qt9SortOrderE(
    QListWidget *self,
    Qt::SortOrder order) {
  self->sortItems(order);
}

//  void QListWidget::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget17setSortingEnabledEb(
    QListWidget *self,
    bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QListWidget::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QListWidget16isSortingEnabledEv(const QListWidget *self) {
  return self->isSortingEnabled();
}

//  void QListWidget::editItem(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget8editItemEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->editItem(item);
}

//  void QListWidget::openPersistentEditor(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget20openPersistentEditorEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->openPersistentEditor(item);
}

//  void QListWidget::closePersistentEditor(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget21closePersistentEditorEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->closePersistentEditor(item);
}

//  bool QListWidget::isPersistentEditorOpen(QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QListWidget22isPersistentEditorOpenEP15QListWidgetItem(
    const QListWidget *self,
    QListWidgetItem *item) {
  return self->isPersistentEditorOpen(item);
}

//  QWidget *QListWidget::itemWidget(QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QListWidget10itemWidgetEP15QListWidgetItem(
    const QListWidget *self,
    QListWidgetItem *item) {
  return self->itemWidget(item);
}

//  void QListWidget::setItemWidget(QListWidgetItem *item, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget13setItemWidgetEP15QListWidgetItemP7QWidget(
    QListWidget *self,
    QListWidgetItem *item,
    QWidget *widget) {
  self->setItemWidget(item, widget);
}

//  void QListWidget::removeItemWidget(QListWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget16removeItemWidgetEP15QListWidgetItem(
    QListWidget *self,
    QListWidgetItem *item) {
  self->removeItemWidget(item);
}

//  QModelIndex QListWidget::indexFromItem(const QListWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QListWidget13indexFromItemEPK15QListWidgetItem(
    const QListWidget *self,
    const QListWidgetItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QListWidgetItem *QListWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK11QListWidget13itemFromIndexERK11QModelIndex(
    const QListWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  void QListWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QListWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  Qt::DropActions QListWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QListWidget20supportedDragActionsEv(
    const QListWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QListWidget::scrollToItem(const QListWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget12scrollToItemEPK15QListWidgetItemN17QAbstractItemView10ScrollHintE(
    QListWidget *self,
    const QListWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QListWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QListWidget5clearEv(QListWidget *self) {
  self->clear();
}
