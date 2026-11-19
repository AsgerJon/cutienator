//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtreewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtreewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qabstractitemmodel.h>

//  const QMetaObject *QTreeWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QTreeWidget10metaObjectEv(
    const QTreeWidget *self) {
  return self->metaObject();
}

//  QString QTreeWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QTreeWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTreeWidget::tr(s, c, n));
}

//  QTreeWidget::QTreeWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTreeWidget *ritual_ZN11QTreeWidgetC1EP7QWidget(QWidget *parent) {
  return new QTreeWidget(parent);
}

//  QTreeWidget::~QTreeWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidgetD1Ev(QTreeWidget *self) {
  delete self;
}

//  int QTreeWidget::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget11columnCountEv(const QTreeWidget *self) {
  return self->columnCount();
}

//  void QTreeWidget::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setColumnCountEi(
    QTreeWidget *self,
    int columns) {
  self->setColumnCount(columns);
}

//  QTreeWidgetItem *QTreeWidget::invisibleRootItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget17invisibleRootItemEv(
    const QTreeWidget *self) {
  return self->invisibleRootItem();
}

//  QTreeWidgetItem *QTreeWidget::topLevelItem(int index) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget12topLevelItemEi(
    const QTreeWidget *self,
    int index) {
  return self->topLevelItem(index);
}

//  int QTreeWidget::topLevelItemCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget17topLevelItemCountEv(const QTreeWidget *self) {
  return self->topLevelItemCount();
}

//  void QTreeWidget::insertTopLevelItem(int index, QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget18insertTopLevelItemEiP15QTreeWidgetItem(
    QTreeWidget *self,
    int index,
    QTreeWidgetItem *item) {
  self->insertTopLevelItem(index, item);
}

//  void QTreeWidget::addTopLevelItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget15addTopLevelItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->addTopLevelItem(item);
}

//  QTreeWidgetItem *QTreeWidget::takeTopLevelItem(int index)
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZN11QTreeWidget16takeTopLevelItemEi(
    QTreeWidget *self,
    int index) {
  return self->takeTopLevelItem(index);
}

//  int QTreeWidget::indexOfTopLevelItem(QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget19indexOfTopLevelItemEP15QTreeWidgetItem(
    const QTreeWidget *self,
    QTreeWidgetItem *item) {
  return self->indexOfTopLevelItem(item);
}

//  QTreeWidgetItem *QTreeWidget::headerItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget10headerItemEv(
    const QTreeWidget *self) {
  return self->headerItem();
}

//  void QTreeWidget::setHeaderItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget13setHeaderItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->setHeaderItem(item);
}

//  void QTreeWidget::setHeaderLabel(const QString &label)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setHeaderLabelERK7QString(
    QTreeWidget *self,
    const QString *label) {
  self->setHeaderLabel(*label);
}

//  QTreeWidgetItem *QTreeWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget11currentItemEv(
    const QTreeWidget *self) {
  return self->currentItem();
}

//  int QTreeWidget::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget13currentColumnEv(const QTreeWidget *self) {
  return self->currentColumn();
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItem(
    QTreeWidget *self,
    QTreeWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->setCurrentItem(item, column);
}

//  void QTreeWidget::setCurrentItem(QTreeWidgetItem *item, int column,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget14setCurrentItemEP15QTreeWidgetItemi6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column,
    int command) {
  self->setCurrentItem(
      item,
      column,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  QTreeWidgetItem *QTreeWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget6itemAtERK6QPoint(
    const QTreeWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QTreeWidgetItem *QTreeWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget6itemAtEii(
    const QTreeWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QTreeWidget::visualItemRect(const QTreeWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK11QTreeWidget14visualItemRectEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  int QTreeWidget::sortColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget10sortColumnEv(const QTreeWidget *self) {
  return self->sortColumn();
}

//  void QTreeWidget::sortItems(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget9sortItemsEiN2Qt9SortOrderE(
    QTreeWidget *self,
    int column,
    Qt::SortOrder order) {
  self->sortItems(column, order);
}

//  void QTreeWidget::editItem(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget8editItemEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->editItem(item, column);
}

//  void QTreeWidget::openPersistentEditor(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget20openPersistentEditorEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->openPersistentEditor(item, column);
}

//  void QTreeWidget::closePersistentEditor(QTreeWidgetItem *item, int
//      column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget21closePersistentEditorEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->closePersistentEditor(item, column);
}

//  bool QTreeWidget::isPersistentEditorOpen(QTreeWidgetItem *item, int
//      column) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QTreeWidget22isPersistentEditorOpenEP15QTreeWidgetItemi(
    const QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  return self->isPersistentEditorOpen(item, column);
}

//  QWidget *QTreeWidget::itemWidget(QTreeWidgetItem *item, int column) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK11QTreeWidget10itemWidgetEP15QTreeWidgetItemi(
    const QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  return self->itemWidget(item, column);
}

//  void QTreeWidget::setItemWidget(QTreeWidgetItem *item, int column,
//      QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget13setItemWidgetEP15QTreeWidgetItemiP7QWidget(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column,
    QWidget *widget) {
  self->setItemWidget(item, column, widget);
}

//  void QTreeWidget::removeItemWidget(QTreeWidgetItem *item, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget16removeItemWidgetEP15QTreeWidgetItemi(
    QTreeWidget *self,
    QTreeWidgetItem *item,
    int column) {
  self->removeItemWidget(item, column);
}

//  QTreeWidgetItem *QTreeWidget::itemAbove(const QTreeWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget9itemAboveEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return self->itemAbove(item);
}

//  QTreeWidgetItem *QTreeWidget::itemBelow(const QTreeWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget9itemBelowEPK15QTreeWidgetItem(
    const QTreeWidget *self,
    const QTreeWidgetItem *item) {
  return self->itemBelow(item);
}

//  QModelIndex QTreeWidget::indexFromItem(const QTreeWidgetItem *item, int
//      column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QTreeWidget13indexFromItemEPK15QTreeWidgetItemi(
    const QTreeWidget *self,
    const QTreeWidgetItem *item,
    int column) {
  return new QModelIndex(self->indexFromItem(item, column));
}

//  QTreeWidgetItem *QTreeWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK11QTreeWidget13itemFromIndexERK11QModelIndex(
    const QTreeWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  void QTreeWidget::setSelectionModel(QItemSelectionModel *selectionModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget17setSelectionModelEP19QItemSelectionModel(
    QTreeWidget *self,
    QItemSelectionModel *selectionModel) {
  self->setSelectionModel(selectionModel);
}

//  Qt::DropActions QTreeWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QTreeWidget20supportedDragActionsEv(
    const QTreeWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QTreeWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QTreeWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QTreeWidget::scrollToItem(const QTreeWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget12scrollToItemEPK15QTreeWidgetItemN17QAbstractItemView10ScrollHintE(
    QTreeWidget *self,
    const QTreeWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QTreeWidget::expandItem(const QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget10expandItemEPK15QTreeWidgetItem(
    QTreeWidget *self,
    const QTreeWidgetItem *item) {
  self->expandItem(item);
}

//  void QTreeWidget::collapseItem(const QTreeWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget12collapseItemEPK15QTreeWidgetItem(
    QTreeWidget *self,
    const QTreeWidgetItem *item) {
  self->collapseItem(item);
}

//  void QTreeWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QTreeWidget5clearEv(QTreeWidget *self) {
  self->clear();
}
