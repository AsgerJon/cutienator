//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>

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

//  void *QModelIndex::internalPointer() const
extern "C" Q_DECL_EXPORT
void *ritual_ZNK11QModelIndex15internalPointerEv(const QModelIndex *self) {
  return self->internalPointer();
}

//  const void *QModelIndex::constInternalPointer() const
extern "C" Q_DECL_EXPORT
const void *ritual_ZNK11QModelIndex20constInternalPointerEv(
    const QModelIndex *self) {
  return self->constInternalPointer();
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

//  bool operator==(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const QModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QModelIndexS1_(
    const QModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator>=(*lhs, *rhs);
}

//  QModelIndex::QModelIndex(int arow, int acolumn, const void *ptr, const
//      QAbstractItemModel *amodel)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN11QModelIndexC1EiiPKvPK18QAbstractItemModel(
    int arow,
    int acolumn,
    const void *ptr,
    const QAbstractItemModel *amodel) {
  return new QModelIndex(arow, acolumn, ptr, amodel);
}

//  QModelIndex::QModelIndex(int arow, int acolumn, quintptr id, const
//      QAbstractItemModel *amodel)
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZN11QModelIndexC1EiiyPK18QAbstractItemModel(
    int arow,
    int acolumn,
    quintptr id,
    const QAbstractItemModel *amodel) {
  return new QModelIndex(arow, acolumn, id, amodel);
}

//  QModelIndex::~QModelIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QModelIndexD1Ev(QModelIndex *self) {
  delete self;
}

//  QList<QModelIndex>::QList()
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_list_make_QModelIndex() {
  return new QList<QModelIndex>();
}

//  void QList<QModelIndex>::append(const QModelIndex &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QModelIndex(
    QList<QModelIndex> *self,
    const QModelIndex *element) {
  self->append(*element);
}

//  qsizetype QList<QModelIndex>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QModelIndex(const QList<QModelIndex> *self) {
  return self->size();
}

//  const QModelIndex &QList<QModelIndex>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_list_at_QModelIndex(
    const QList<QModelIndex> *self,
    long long index) {
  return new QModelIndex(self->at(index));
}

//  QList<QModelIndex>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QModelIndex(QList<QModelIndex> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
#endif  // QT_CONFIG(itemmodel)
