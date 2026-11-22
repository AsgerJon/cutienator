//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qstandarditemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qstandarditemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>

//  const QMetaObject *QStandardItemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QStandardItemModel10metaObjectEv(
    const QStandardItemModel *self) {
  return self->metaObject();
}

//  QString QStandardItemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QStandardItemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStandardItemModel::tr(s, c, n));
}

//  QStandardItemModel::QStandardItemModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZN18QStandardItemModelC1EP7QObject(
    QObject *parent) {
  return new QStandardItemModel(parent);
}

//  QStandardItemModel::QStandardItemModel(int rows, int columns, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QStandardItemModel *ritual_ZN18QStandardItemModelC1EiiP7QObject(
    int rows,
    int columns,
    QObject *parent) {
  return new QStandardItemModel(rows, columns, parent);
}

//  QStandardItemModel::~QStandardItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModelD1Ev(QStandardItemModel *self) {
  delete self;
}

//  QModelIndex QStandardItemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel5indexEiiRK11QModelIndex(
    const QStandardItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QStandardItemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel6parentERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QStandardItemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel8rowCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QStandardItemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel11columnCountERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QStandardItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QStandardItemModel11hasChildrenERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QStandardItemModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QStandardItemModel4dataERK11QModelIndexi(
    const QStandardItemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  void QStandardItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QStandardItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QStandardItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  bool QStandardItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel7setDataERK11QModelIndexRK8QVarianti(
    QStandardItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QStandardItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13clearItemDataERK11QModelIndex(
    QStandardItemModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QVariant QStandardItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QStandardItemModel10headerDataEiN2Qt11OrientationEi(
    const QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QStandardItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QStandardItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QStandardItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel10insertRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QStandardItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13insertColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QStandardItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel10removeRowsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QStandardItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel13removeColumnsEiiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  Qt::ItemFlags QStandardItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel5flagsERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  Qt::DropActions QStandardItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel20supportedDropActionsEv(
    const QStandardItemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  void QStandardItemModel::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel5clearEv(QStandardItemModel *self) {
  self->clear();
}

//  void QStandardItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel4sortEiN2Qt9SortOrderE(
    QStandardItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QStandardItem *QStandardItemModel::itemFromIndex(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel13itemFromIndexERK11QModelIndex(
    const QStandardItemModel *self,
    const QModelIndex *index) {
  return self->itemFromIndex(*index);
}

//  QModelIndex QStandardItemModel::indexFromItem(const QStandardItem *item)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QStandardItemModel13indexFromItemEPK13QStandardItem(
    const QStandardItemModel *self,
    const QStandardItem *item) {
  return new QModelIndex(self->indexFromItem(item));
}

//  QStandardItem *QStandardItemModel::item(int row, int column) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel4itemEii(
    const QStandardItemModel *self,
    int row,
    int column) {
  return self->item(row, column);
}

//  void QStandardItemModel::setItem(int row, int column, QStandardItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel7setItemEiiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    int column,
    QStandardItem *item) {
  self->setItem(row, column, item);
}

//  void QStandardItemModel::setItem(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel7setItemEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->setItem(row, item);
}

//  QStandardItem *QStandardItemModel::invisibleRootItem() const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel17invisibleRootItemEv(
    const QStandardItemModel *self) {
  return self->invisibleRootItem();
}

//  QStandardItem *QStandardItemModel::horizontalHeaderItem(int column) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel20horizontalHeaderItemEi(
    const QStandardItemModel *self,
    int column) {
  return self->horizontalHeaderItem(column);
}

//  void QStandardItemModel::setHorizontalHeaderItem(int column,
//      QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel23setHorizontalHeaderItemEiP13QStandardItem(
    QStandardItemModel *self,
    int column,
    QStandardItem *item) {
  self->setHorizontalHeaderItem(column, item);
}

//  QStandardItem *QStandardItemModel::verticalHeaderItem(int row) const
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZNK18QStandardItemModel18verticalHeaderItemEi(
    const QStandardItemModel *self,
    int row) {
  return self->verticalHeaderItem(row);
}

//  void QStandardItemModel::setVerticalHeaderItem(int row, QStandardItem
//      *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel21setVerticalHeaderItemEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->setVerticalHeaderItem(row, item);
}

//  void QStandardItemModel::setRowCount(int rows)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel11setRowCountEi(
    QStandardItemModel *self,
    int rows) {
  self->setRowCount(rows);
}

//  void QStandardItemModel::setColumnCount(int columns)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel14setColumnCountEi(
    QStandardItemModel *self,
    int columns) {
  self->setColumnCount(columns);
}

//  void QStandardItemModel::appendRow(QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9appendRowEP13QStandardItem(
    QStandardItemModel *self,
    QStandardItem *item) {
  self->appendRow(item);
}

//  void QStandardItemModel::insertRow(int row, QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel9insertRowEiP13QStandardItem(
    QStandardItemModel *self,
    int row,
    QStandardItem *item) {
  self->insertRow(row, item);
}

//  bool QStandardItemModel::insertRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel9insertRowEiRK11QModelIndex(
    QStandardItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->insertRow(row, *parent);
}

//  bool QStandardItemModel::insertColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel12insertColumnEiRK11QModelIndex(
    QStandardItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->insertColumn(column, *parent);
}

//  QStandardItem *QStandardItemModel::takeItem(int row, int column)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel8takeItemEii(
    QStandardItemModel *self,
    int row,
    int column) {
  return self->takeItem(row, column);
}

//  QStandardItem *QStandardItemModel::takeHorizontalHeaderItem(int column)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel24takeHorizontalHeaderItemEi(
    QStandardItemModel *self,
    int column) {
  return self->takeHorizontalHeaderItem(column);
}

//  QStandardItem *QStandardItemModel::takeVerticalHeaderItem(int row)
extern "C" Q_DECL_EXPORT
QStandardItem *ritual_ZN18QStandardItemModel22takeVerticalHeaderItemEi(
    QStandardItemModel *self,
    int row) {
  return self->takeVerticalHeaderItem(row);
}

//  const QStandardItem *QStandardItemModel::itemPrototype() const
extern "C" Q_DECL_EXPORT
const QStandardItem *ritual_ZNK18QStandardItemModel13itemPrototypeEv(
    const QStandardItemModel *self) {
  return self->itemPrototype();
}

//  void QStandardItemModel::setItemPrototype(const QStandardItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel16setItemPrototypeEPK13QStandardItem(
    QStandardItemModel *self,
    const QStandardItem *item) {
  self->setItemPrototype(item);
}

//  int QStandardItemModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QStandardItemModel8sortRoleEv(
    const QStandardItemModel *self) {
  return self->sortRole();
}

//  void QStandardItemModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStandardItemModel11setSortRoleEi(
    QStandardItemModel *self,
    int role) {
  self->setSortRole(role);
}

//  bool QStandardItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QStandardItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QStandardItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}
