//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qidentityproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qidentityproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qitemselectionmodel.h>

//  const QMetaObject *QIdentityProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QIdentityProxyModel10metaObjectEv(
    const QIdentityProxyModel *self) {
  return self->metaObject();
}

//  QString QIdentityProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QIdentityProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QIdentityProxyModel::tr(s, c, n));
}

//  QIdentityProxyModel::QIdentityProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QIdentityProxyModel *ritual_ZN19QIdentityProxyModelC1EP7QObject(
    QObject *parent) {
  return new QIdentityProxyModel(parent);
}

//  QIdentityProxyModel::~QIdentityProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIdentityProxyModelD1Ev(QIdentityProxyModel *self) {
  delete self;
}

//  int QIdentityProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIdentityProxyModel11columnCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QModelIndex QIdentityProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel5indexEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QIdentityProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel13mapFromSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QModelIndex QIdentityProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel11mapToSourceERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QIdentityProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel6parentERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QIdentityProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QIdentityProxyModel8rowCountERK11QModelIndex(
    const QIdentityProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QVariant QIdentityProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QIdentityProxyModel10headerDataEiN2Qt11OrientationEi(
    const QIdentityProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QIdentityProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  QModelIndex QIdentityProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QIdentityProxyModel7siblingEiiRK11QModelIndex(
    const QIdentityProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  QItemSelection QIdentityProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QIdentityProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionFromSource(*selection));
}

//  QItemSelection QIdentityProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QIdentityProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QIdentityProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionToSource(*selection));
}

//  void QIdentityProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QIdentityProxyModel14setSourceModelEP18QAbstractItemModel(
    QIdentityProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  bool QIdentityProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel13insertColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel10insertRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QIdentityProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel13removeColumnsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QIdentityProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel10removeRowsEiiRK11QModelIndex(
    QIdentityProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QIdentityProxyModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel8moveRowsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
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

//  bool QIdentityProxyModel::moveColumns(const QModelIndex &sourceParent,
//      int sourceColumn, int count, const QModelIndex &destinationParent,
//      int destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QIdentityProxyModel11moveColumnsERK11QModelIndexiiS2_i(
    QIdentityProxyModel *self,
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

//  bool QIdentityProxyModel::handleSourceLayoutChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIdentityProxyModel25handleSourceLayoutChangesEv(
    const QIdentityProxyModel *self) {
  return self->handleSourceLayoutChanges();
}

//  bool QIdentityProxyModel::handleSourceDataChanges() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QIdentityProxyModel23handleSourceDataChangesEv(
    const QIdentityProxyModel *self) {
  return self->handleSourceDataChanges();
}
