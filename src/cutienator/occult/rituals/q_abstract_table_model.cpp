//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractitemmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qstring.h>

//  const QMetaObject *QAbstractTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractTableModel10metaObjectEv(
    const QAbstractTableModel *self) {
  return self->metaObject();
}

//  QString QAbstractTableModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractTableModel::tr(s, c, n));
}

//  QAbstractTableModel::~QAbstractTableModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractTableModelD1Ev(QAbstractTableModel *self) {
  delete self;
}

//  QModelIndex QAbstractTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel5indexEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QAbstractTableModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractTableModel7siblingEiiRK11QModelIndex(
    const QAbstractTableModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QAbstractTableModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractTableModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractTableModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::ItemFlags QAbstractTableModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractTableModel5flagsERK11QModelIndex(
    const QAbstractTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}
