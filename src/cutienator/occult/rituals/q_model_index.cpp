//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>

//  QModelIndex::QModelIndex()
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN11QModelIndexC1Ev() {
  return new QModelIndex();
}

//  int QModelIndex::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QModelIndex3rowEv(const QModelIndex *self) {
  return self->row();
}

//  int QModelIndex::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QModelIndex6columnEv(const QModelIndex *self) {
  return self->column();
}

//  quintptr QModelIndex::internalId() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK11QModelIndex10internalIdEv(const QModelIndex *self) {
  return self->internalId();
}

//  QModelIndex QModelIndex::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QModelIndex6parentEv(const QModelIndex *self) {
  return new QModelIndex(self->parent());
}

//  QModelIndex QModelIndex::sibling(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QModelIndex7siblingEii(
    const QModelIndex *self,
    int row,
    int column) {
  return new QModelIndex(self->sibling(row, column));
}

//  QModelIndex QModelIndex::siblingAtColumn(int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QModelIndex15siblingAtColumnEi(
    const QModelIndex *self,
    int column) {
  return new QModelIndex(self->siblingAtColumn(column));
}

//  QModelIndex QModelIndex::siblingAtRow(int row) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QModelIndex12siblingAtRowEi(
    const QModelIndex *self,
    int row) {
  return new QModelIndex(self->siblingAtRow(row));
}

//  QVariant QModelIndex::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QModelIndex4dataEi(const QModelIndex *self, int role) {
  return new QVariant(self->data(role));
}

//  void QModelIndex::multiData(QModelRoleDataSpan roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QModelIndex9multiDataE18QModelRoleDataSpan(
    const QModelIndex *self,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*roleDataSpan);
}

//  Qt::ItemFlags QModelIndex::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QModelIndex5flagsEv(const QModelIndex *self) {
  return static_cast<int>(self->flags().toInt());
}

//  const QAbstractItemModel *QModelIndex::model() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK11QModelIndex5modelEv(
    const QModelIndex *self) {
  return self->model();
}

//  bool QModelIndex::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QModelIndex7isValidEv(const QModelIndex *self) {
  return self->isValid();
}

//  QModelIndex::~QModelIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QModelIndexD1Ev(QModelIndex *self) {
  delete self;
}
