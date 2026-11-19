//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QAbstractItemModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAbstractItemModel10metaObjectEv(
    const QAbstractItemModel *self) {
  return self->metaObject();
}

//  QString QAbstractItemModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAbstractItemModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractItemModel::tr(s, c, n));
}

//  QAbstractItemModel::~QAbstractItemModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModelD1Ev(QAbstractItemModel *self) {
  delete self;
}

//  bool QAbstractItemModel::hasIndex(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel8hasIndexEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->hasIndex(row, column, *parent);
}

//  QModelIndex QAbstractItemModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel5indexEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractItemModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel6parentERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QAbstractItemModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel7siblingEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  int QAbstractItemModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel8rowCountERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QAbstractItemModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel11columnCountERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QAbstractItemModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel11hasChildrenERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QAbstractItemModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QAbstractItemModel4dataERK11QModelIndexi(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QAbstractItemModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractItemModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QAbstractItemModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QAbstractItemModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QAbstractItemModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractItemModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QAbstractItemModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13clearItemDataERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  bool QAbstractItemModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QAbstractItemModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractItemModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QAbstractItemModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel20supportedDropActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  Qt::DropActions QAbstractItemModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel20supportedDragActionsEv(
    const QAbstractItemModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  bool QAbstractItemModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10insertRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QAbstractItemModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13insertColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QAbstractItemModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10removeRowsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QAbstractItemModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel13removeColumnsEiiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QAbstractItemModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel8moveRowsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::moveColumns(const QModelIndex &sourceParent, int
//      sourceColumn, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel11moveColumnsERK11QModelIndexiiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::insertRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel9insertRowEiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->insertRow(row, *parent);
}

//  bool QAbstractItemModel::insertColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12insertColumnEiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->insertColumn(column, *parent);
}

//  bool QAbstractItemModel::removeRow(int row, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel9removeRowEiRK11QModelIndex(
    QAbstractItemModel *self,
    int row,
    const QModelIndex *parent) {
  return self->removeRow(row, *parent);
}

//  bool QAbstractItemModel::removeColumn(int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel12removeColumnEiRK11QModelIndex(
    QAbstractItemModel *self,
    int column,
    const QModelIndex *parent) {
  return self->removeColumn(column, *parent);
}

//  bool QAbstractItemModel::moveRow(const QModelIndex &sourceParent, int
//      sourceRow, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel7moveRowERK11QModelIndexiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveRow(
      *sourceParent,
      sourceRow,
      *destinationParent,
      destinationChild);
}

//  bool QAbstractItemModel::moveColumn(const QModelIndex &sourceParent, int
//      sourceColumn, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel10moveColumnERK11QModelIndexiS2_i(
    QAbstractItemModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->moveColumn(
      *sourceParent,
      sourceColumn,
      *destinationParent,
      destinationChild);
}

//  void QAbstractItemModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel9fetchMoreERK11QModelIndex(
    QAbstractItemModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QAbstractItemModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel12canFetchMoreERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  Qt::ItemFlags QAbstractItemModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractItemModel5flagsERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QAbstractItemModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel4sortEiN2Qt9SortOrderE(
    QAbstractItemModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QModelIndex QAbstractItemModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractItemModel5buddyERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  QSize QAbstractItemModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18QAbstractItemModel4spanERK11QModelIndex(
    const QAbstractItemModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  bool QAbstractItemModel::checkIndex(const QModelIndex &index,
//      CheckIndexOptions options) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QAbstractItemModel10checkIndexERK11QModelIndex6QFlagsINS_16CheckIndexOptionEE(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    int options) {
  return self->checkIndex(
      *index,
      QFlags<QAbstractItemModel::CheckIndexOption>::fromInt(options));
}

//  void QAbstractItemModel::multiData(const QModelIndex &index,
//      QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18QAbstractItemModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QAbstractItemModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  bool QAbstractItemModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractItemModel6submitEv(QAbstractItemModel *self) {
  return self->submit();
}

//  void QAbstractItemModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractItemModel6revertEv(QAbstractItemModel *self) {
  self->revert();
}
