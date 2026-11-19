//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qtablewidget.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qtablewidget.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>

//  const QMetaObject *QTableWidget::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QTableWidget10metaObjectEv(
    const QTableWidget *self) {
  return self->metaObject();
}

//  QString QTableWidget::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QTableWidget2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTableWidget::tr(s, c, n));
}

//  QTableWidget::QTableWidget(QWidget *parent)
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZN12QTableWidgetC1EP7QWidget(QWidget *parent) {
  return new QTableWidget(parent);
}

//  QTableWidget::QTableWidget(int rows, int columns, QWidget *parent)
extern "C" Q_DECL_EXPORT
QTableWidget *ritual_ZN12QTableWidgetC1EiiP7QWidget(
    int rows,
    int columns,
    QWidget *parent) {
  return new QTableWidget(rows, columns, parent);
}

//  QTableWidget::~QTableWidget()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidgetD1Ev(QTableWidget *self) {
  delete self;
}

//  void QTableWidget::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget11setRowCountEi(QTableWidget *self, int rows) {
  self->setRowCount(rows);
}

//  int QTableWidget::rowCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget8rowCountEv(const QTableWidget *self) {
  return self->rowCount();
}

//  void QTableWidget::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setColumnCountEi(
    QTableWidget *self,
    int columns) {
  self->setColumnCount(columns);
}

//  int QTableWidget::columnCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget11columnCountEv(const QTableWidget *self) {
  return self->columnCount();
}

//  int QTableWidget::row(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget3rowEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return self->row(item);
}

//  int QTableWidget::column(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget6columnEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return self->column(item);
}

//  QTableWidgetItem *QTableWidget::item(int row, int column) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget4itemEii(
    const QTableWidget *self,
    int row,
    int column) {
  return self->item(row, column);
}

//  void QTableWidget::setItem(int row, int column, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget7setItemEiiP16QTableWidgetItem(
    QTableWidget *self,
    int row,
    int column,
    QTableWidgetItem *item) {
  self->setItem(row, column, item);
}

//  QTableWidgetItem *QTableWidget::takeItem(int row, int column)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget8takeItemEii(
    QTableWidget *self,
    int row,
    int column) {
  return self->takeItem(row, column);
}

//  QModelIndex QTableWidget::indexFromItem(const QTableWidgetItem *item)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK12QTableWidget13indexFromItemEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QTableWidgetItem *QTableWidget::itemFromIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget13itemFromIndexERK11QModelIndex(
    const QTableWidget *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  QTableWidgetItem *QTableWidget::verticalHeaderItem(int row) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget18verticalHeaderItemEi(
    const QTableWidget *self,
    int row) {
  return self->verticalHeaderItem(row);
}

//  void QTableWidget::setVerticalHeaderItem(int row, QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget21setVerticalHeaderItemEiP16QTableWidgetItem(
    QTableWidget *self,
    int row,
    QTableWidgetItem *item) {
  self->setVerticalHeaderItem(row, item);
}

//  QTableWidgetItem *QTableWidget::takeVerticalHeaderItem(int row)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget22takeVerticalHeaderItemEi(
    QTableWidget *self,
    int row) {
  return self->takeVerticalHeaderItem(row);
}

//  QTableWidgetItem *QTableWidget::horizontalHeaderItem(int column) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget20horizontalHeaderItemEi(
    const QTableWidget *self,
    int column) {
  return self->horizontalHeaderItem(column);
}

//  void QTableWidget::setHorizontalHeaderItem(int column, QTableWidgetItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget23setHorizontalHeaderItemEiP16QTableWidgetItem(
    QTableWidget *self,
    int column,
    QTableWidgetItem *item) {
  self->setHorizontalHeaderItem(column, item);
}

//  QTableWidgetItem *QTableWidget::takeHorizontalHeaderItem(int column)
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZN12QTableWidget24takeHorizontalHeaderItemEi(
    QTableWidget *self,
    int column) {
  return self->takeHorizontalHeaderItem(column);
}

//  int QTableWidget::currentRow() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget10currentRowEv(const QTableWidget *self) {
  return self->currentRow();
}

//  int QTableWidget::currentColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget13currentColumnEv(const QTableWidget *self) {
  return self->currentColumn();
}

//  QTableWidgetItem *QTableWidget::currentItem() const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget11currentItemEv(
    const QTableWidget *self) {
  return self->currentItem();
}

//  void QTableWidget::setCurrentItem(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->setCurrentItem(item);
}

//  void QTableWidget::setCurrentItem(QTableWidgetItem *item,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentItemEP16QTableWidgetItem6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableWidget *self,
    QTableWidgetItem *item,
    int command) {
  self->setCurrentItem(
      item,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QTableWidget::setCurrentCell(int row, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentCellEii(
    QTableWidget *self,
    int row,
    int column) {
  self->setCurrentCell(row, column);
}

//  void QTableWidget::setCurrentCell(int row, int column,
//      QItemSelectionModel::SelectionFlags command)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget14setCurrentCellEii6QFlagsIN19QItemSelectionModel13SelectionFlagEE(
    QTableWidget *self,
    int row,
    int column,
    int command) {
  self->setCurrentCell(
      row,
      column,
      QFlags<QItemSelectionModel::SelectionFlag>::fromInt(command));
}

//  void QTableWidget::sortItems(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9sortItemsEiN2Qt9SortOrderE(
    QTableWidget *self,
    int column,
    Qt::SortOrder order) {
  self->sortItems(column, order);
}

//  void QTableWidget::setSortingEnabled(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget17setSortingEnabledEb(
    QTableWidget *self,
    bool enable) {
  self->setSortingEnabled(enable);
}

//  bool QTableWidget::isSortingEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTableWidget16isSortingEnabledEv(const QTableWidget *self) {
  return self->isSortingEnabled();
}

//  void QTableWidget::editItem(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget8editItemEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->editItem(item);
}

//  void QTableWidget::openPersistentEditor(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget20openPersistentEditorEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->openPersistentEditor(item);
}

//  void QTableWidget::closePersistentEditor(QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget21closePersistentEditorEP16QTableWidgetItem(
    QTableWidget *self,
    QTableWidgetItem *item) {
  self->closePersistentEditor(item);
}

//  bool QTableWidget::isPersistentEditorOpen(QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QTableWidget22isPersistentEditorOpenEP16QTableWidgetItem(
    const QTableWidget *self,
    QTableWidgetItem *item) {
  return self->isPersistentEditorOpen(item);
}

//  QWidget *QTableWidget::cellWidget(int row, int column) const
extern "C" Q_DECL_EXPORT
QWidget *ritual_ZNK12QTableWidget10cellWidgetEii(
    const QTableWidget *self,
    int row,
    int column) {
  return self->cellWidget(row, column);
}

//  void QTableWidget::setCellWidget(int row, int column, QWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget13setCellWidgetEiiP7QWidget(
    QTableWidget *self,
    int row,
    int column,
    QWidget *widget) {
  self->setCellWidget(row, column, widget);
}

//  void QTableWidget::removeCellWidget(int row, int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16removeCellWidgetEii(
    QTableWidget *self,
    int row,
    int column) {
  self->removeCellWidget(row, column);
}

//  void QTableWidget::setRangeSelected(const QTableWidgetSelectionRange
//      &range, bool select)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16setRangeSelectedERK26QTableWidgetSelectionRangeb(
    QTableWidget *self,
    const QTableWidgetSelectionRange *range,
    bool select) {
  self->setRangeSelected(*range, select);
}

//  int QTableWidget::visualRow(int logicalRow) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget9visualRowEi(
    const QTableWidget *self,
    int logicalRow) {
  return self->visualRow(logicalRow);
}

//  int QTableWidget::visualColumn(int logicalColumn) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget12visualColumnEi(
    const QTableWidget *self,
    int logicalColumn) {
  return self->visualColumn(logicalColumn);
}

//  QTableWidgetItem *QTableWidget::itemAt(const QPoint &p) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget6itemAtERK6QPoint(
    const QTableWidget *self,
    const QPoint *p) {
  return self->itemAt(*p);
}

//  QTableWidgetItem *QTableWidget::itemAt(int x, int y) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK12QTableWidget6itemAtEii(
    const QTableWidget *self,
    int x,
    int y) {
  return self->itemAt(x, y);
}

//  QRect QTableWidget::visualItemRect(const QTableWidgetItem *item) const
extern "C" Q_DECL_EXPORT
QRect *ritual_ZNK12QTableWidget14visualItemRectEPK16QTableWidgetItem(
    const QTableWidget *self,
    const QTableWidgetItem *item) {
  return new QRect(self->visualItemRect(item));
}

//  const QTableWidgetItem *QTableWidget::itemPrototype() const
extern "C" Q_DECL_EXPORT
const QTableWidgetItem *ritual_ZNK12QTableWidget13itemPrototypeEv(
    const QTableWidget *self) {
  return self->itemPrototype();
}

//  void QTableWidget::setItemPrototype(const QTableWidgetItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget16setItemPrototypeEPK16QTableWidgetItem(
    QTableWidget *self,
    const QTableWidgetItem *item) {
  self->setItemPrototype(item);
}

//  Qt::DropActions QTableWidget::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QTableWidget20supportedDragActionsEv(
    const QTableWidget *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QTableWidget::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QTableWidget *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QTableWidget::scrollToItem(const QTableWidgetItem *item,
//      QAbstractItemView::ScrollHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12scrollToItemEPK16QTableWidgetItemN17QAbstractItemView10ScrollHintE(
    QTableWidget *self,
    const QTableWidgetItem *item,
    QAbstractItemView::ScrollHint hint) {
  self->scrollToItem(item, hint);
}

//  void QTableWidget::insertRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9insertRowEi(QTableWidget *self, int row) {
  self->insertRow(row);
}

//  void QTableWidget::insertColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12insertColumnEi(
    QTableWidget *self,
    int column) {
  self->insertColumn(column);
}

//  void QTableWidget::removeRow(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget9removeRowEi(QTableWidget *self, int row) {
  self->removeRow(row);
}

//  void QTableWidget::removeColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget12removeColumnEi(
    QTableWidget *self,
    int column) {
  self->removeColumn(column);
}

//  void QTableWidget::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget5clearEv(QTableWidget *self) {
  self->clear();
}

//  void QTableWidget::clearContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QTableWidget13clearContentsEv(QTableWidget *self) {
  self->clearContents();
}
