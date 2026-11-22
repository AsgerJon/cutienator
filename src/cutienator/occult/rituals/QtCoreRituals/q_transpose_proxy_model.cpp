//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qtransposeproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qtransposeproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QTransposeProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK20QTransposeProxyModel10metaObjectEv(
    const QTransposeProxyModel *self) {
  return self->metaObject();
}

//  QString QTransposeProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN20QTransposeProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTransposeProxyModel::tr(s, c, n));
}

//  QTransposeProxyModel::QTransposeProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QTransposeProxyModel *ritual_ZN20QTransposeProxyModelC1EP7QObject(
    QObject *parent) {
  return new QTransposeProxyModel(parent);
}

//  QTransposeProxyModel::~QTransposeProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModelD1Ev(QTransposeProxyModel *self) {
  delete self;
}

//  void QTransposeProxyModel::setSourceModel(QAbstractItemModel
//      *newSourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModel14setSourceModelEP18QAbstractItemModel(
    QTransposeProxyModel *self,
    QAbstractItemModel *newSourceModel) {
  self->setSourceModel(newSourceModel);
}

//  int QTransposeProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTransposeProxyModel8rowCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QTransposeProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK20QTransposeProxyModel11columnCountERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QVariant QTransposeProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK20QTransposeProxyModel10headerDataEiN2Qt11OrientationEi(
    const QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QTransposeProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QTransposeProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  QSize QTransposeProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK20QTransposeProxyModel4spanERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  QModelIndex QTransposeProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel13mapFromSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QTransposeProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel11mapToSourceERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QTransposeProxyModel::parent(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel6parentERK11QModelIndex(
    const QTransposeProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  QModelIndex QTransposeProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK20QTransposeProxyModel5indexEiiRK11QModelIndex(
    const QTransposeProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  bool QTransposeProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel10insertRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QTransposeProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel10removeRowsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QTransposeProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
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

//  bool QTransposeProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13insertColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel13removeColumnsEiiRK11QModelIndex(
    QTransposeProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QTransposeProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QTransposeProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QTransposeProxyModel *self,
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

//  void QTransposeProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN20QTransposeProxyModel4sortEiN2Qt9SortOrderE(
    QTransposeProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}
