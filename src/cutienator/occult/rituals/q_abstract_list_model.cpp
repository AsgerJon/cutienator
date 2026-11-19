//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAbstractListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK18QAbstractListModel10metaObjectEv(
    const QAbstractListModel *self) {
  return self->metaObject();
}

//  QString QAbstractListModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN18QAbstractListModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractListModel::tr(s, c, n));
}

//  QAbstractListModel::~QAbstractListModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QAbstractListModelD1Ev(QAbstractListModel *self) {
  delete self;
}

//  QModelIndex QAbstractListModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractListModel5indexEiiRK11QModelIndex(
    const QAbstractListModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractListModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK18QAbstractListModel7siblingEiiRK11QModelIndex(
    const QAbstractListModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QAbstractListModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18QAbstractListModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractListModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::ItemFlags QAbstractListModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18QAbstractListModel5flagsERK11QModelIndex(
    const QAbstractListModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}
