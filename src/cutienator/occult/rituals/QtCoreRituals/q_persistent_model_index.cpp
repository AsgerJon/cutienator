//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(itemmodel)
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlist.h>

//  QPersistentModelIndex::QPersistentModelIndex()
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZN21QPersistentModelIndexC1Ev() {
  return new QPersistentModelIndex();
}

//  QPersistentModelIndex::QPersistentModelIndex(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZN21QPersistentModelIndexC1ERK11QModelIndex(
    const QModelIndex *index) {
  return new QPersistentModelIndex(*index);
}

//  QPersistentModelIndex::QPersistentModelIndex(const QPersistentModelIndex
//      &other)
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_ZN21QPersistentModelIndexC1ERKS_(
    const QPersistentModelIndex *other) {
  return new QPersistentModelIndex(*other);
}

//  QPersistentModelIndex::~QPersistentModelIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QPersistentModelIndexD1Ev(QPersistentModelIndex *self) {
  delete self;
}

//  QModelIndex QPersistentModelIndex::operator QModelIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QPersistentModelIndexcv11QModelIndexEv(
    const QPersistentModelIndex *self) {
  return new QModelIndex(self->operator QModelIndex());
}

//  int QPersistentModelIndex::row() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QPersistentModelIndex3rowEv(
    const QPersistentModelIndex *self) {
  return self->row();
}

//  int QPersistentModelIndex::column() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QPersistentModelIndex6columnEv(
    const QPersistentModelIndex *self) {
  return self->column();
}

//  quintptr QPersistentModelIndex::internalId() const
extern "C" Q_DECL_EXPORT
quintptr ritual_ZNK21QPersistentModelIndex10internalIdEv(
    const QPersistentModelIndex *self) {
  return self->internalId();
}

//  QModelIndex QPersistentModelIndex::parent() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QPersistentModelIndex6parentEv(
    const QPersistentModelIndex *self) {
  return new QModelIndex(self->parent());
}

//  QModelIndex QPersistentModelIndex::sibling(int row, int column) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QPersistentModelIndex7siblingEii(
    const QPersistentModelIndex *self,
    int row,
    int column) {
  return new QModelIndex(self->sibling(row, column));
}

//  QVariant QPersistentModelIndex::data(int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QPersistentModelIndex4dataEi(
    const QPersistentModelIndex *self,
    int role) {
  return new QVariant(self->data(role));
}

//  void QPersistentModelIndex::multiData(QModelRoleDataSpan roleDataSpan)
//      const
extern "C" Q_DECL_EXPORT
void ritual_ZNK21QPersistentModelIndex9multiDataE18QModelRoleDataSpan(
    const QPersistentModelIndex *self,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*roleDataSpan);
}

//  Qt::ItemFlags QPersistentModelIndex::flags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QPersistentModelIndex5flagsEv(
    const QPersistentModelIndex *self) {
  return static_cast<int>(self->flags().toInt());
}

//  const QAbstractItemModel *QPersistentModelIndex::model() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK21QPersistentModelIndex5modelEv(
    const QPersistentModelIndex *self) {
  return self->model();
}

//  bool QPersistentModelIndex::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QPersistentModelIndex7isValidEv(
    const QPersistentModelIndex *self) {
  return self->isValid();
}

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator==(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator!=(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<=(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>=(const QPersistentModelIndex &lhs, const
//      QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK21QPersistentModelIndexS1_(
    const QPersistentModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator==(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator!=(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<=(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>=(const QPersistentModelIndex &lhs, const QModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK21QPersistentModelIndexRK11QModelIndex(
    const QPersistentModelIndex *lhs,
    const QModelIndex *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator==(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator==(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator!=(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator!=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZltRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator<(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgtRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator>(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator<=(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZleRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator<=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !QT_CORE_REMOVED_SINCE(6, 8)
//  bool operator>=(const QModelIndex &lhs, const QPersistentModelIndex &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZgeRK11QModelIndexRK21QPersistentModelIndex(
    const QModelIndex *lhs,
    const QPersistentModelIndex *rhs) {
  return operator>=(*lhs, *rhs);
}
#endif  // !QT_CORE_REMOVED_SINCE(6, 8)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QPersistentModelIndex &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK21QPersistentModelIndex(
    const QDebug *a0,
    const QPersistentModelIndex *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QList<QPersistentModelIndex>::QList()
extern "C" Q_DECL_EXPORT
QList<QPersistentModelIndex> *ritual_list_make_QPersistentModelIndex() {
  return new QList<QPersistentModelIndex>();
}

//  void QList<QPersistentModelIndex>::append(const QPersistentModelIndex
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QPersistentModelIndex(
    QList<QPersistentModelIndex> *self,
    const QPersistentModelIndex *element) {
  self->append(*element);
}

//  qsizetype QList<QPersistentModelIndex>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QPersistentModelIndex(
    const QList<QPersistentModelIndex> *self) {
  return self->size();
}

//  const QPersistentModelIndex &QList<QPersistentModelIndex>::at(qsizetype
//      i) const
extern "C" Q_DECL_EXPORT
QPersistentModelIndex *ritual_list_at_QPersistentModelIndex(
    const QList<QPersistentModelIndex> *self,
    long long index) {
  return new QPersistentModelIndex(self->at(index));
}

//  QList<QPersistentModelIndex>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QPersistentModelIndex(
    QList<QPersistentModelIndex> *self) {
  delete self;
}

#endif  // QT_CONFIG(itemmodel)
