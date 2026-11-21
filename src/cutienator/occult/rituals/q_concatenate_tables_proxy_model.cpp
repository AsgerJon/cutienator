//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qconcatenatetablesproxymodel.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/qconcatenatetablesproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QConcatenateTablesProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QConcatenateTablesProxyModel10metaObjectEv(
    const QConcatenateTablesProxyModel *self) {
  return self->metaObject();
}

//  QString QConcatenateTablesProxyModel::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QConcatenateTablesProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QConcatenateTablesProxyModel::tr(s, c, n));
}

//  QConcatenateTablesProxyModel::QConcatenateTablesProxyModel(QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QConcatenateTablesProxyModel *ritual_ZN28QConcatenateTablesProxyModelC1EP7QObject(
    QObject *parent) {
  return new QConcatenateTablesProxyModel(parent);
}

//  QConcatenateTablesProxyModel::~QConcatenateTablesProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModelD1Ev(
    QConcatenateTablesProxyModel *self) {
  delete self;
}

//  void QConcatenateTablesProxyModel::addSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModel14addSourceModelEP18QAbstractItemModel(
    QConcatenateTablesProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->addSourceModel(sourceModel);
}

//  void QConcatenateTablesProxyModel::removeSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QConcatenateTablesProxyModel17removeSourceModelEP18QAbstractItemModel(
    QConcatenateTablesProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->removeSourceModel(sourceModel);
}

//  QModelIndex QConcatenateTablesProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel13mapFromSourceERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QConcatenateTablesProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel11mapToSourceERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QVariant QConcatenateTablesProxyModel::data(const QModelIndex &index, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QConcatenateTablesProxyModel4dataERK11QModelIndexi(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QConcatenateTablesProxyModel::setData(const QModelIndex &index,
//      const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QConcatenateTablesProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QConcatenateTablesProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  Qt::ItemFlags QConcatenateTablesProxyModel::flags(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel5flagsERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QModelIndex QConcatenateTablesProxyModel::index(int row, int column,
//      const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel5indexEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QConcatenateTablesProxyModel::parent(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK28QConcatenateTablesProxyModel6parentERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->parent(*index));
}

//  int QConcatenateTablesProxyModel::rowCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel8rowCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QConcatenateTablesProxyModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK28QConcatenateTablesProxyModel10headerDataEiN2Qt11OrientationEi(
    const QConcatenateTablesProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  int QConcatenateTablesProxyModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QConcatenateTablesProxyModel11columnCountERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QConcatenateTablesProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QConcatenateTablesProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QConcatenateTablesProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN28QConcatenateTablesProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QConcatenateTablesProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QSize QConcatenateTablesProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK28QConcatenateTablesProxyModel4spanERK11QModelIndex(
    const QConcatenateTablesProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}
