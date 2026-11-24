//  Written by dev_tooling.RitualGenerator from the records of
//  QtQmlModels/6.12.0/QtQmlModels/private/qqmltreemodeltotablemodel_p_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtQmlModels/6.12.0/QtQmlModels/private/qtqmlmodelsglobal_p.h>
#include <QtQmlModels/QtQmlModels>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQmlModels/6.12.0/QtQmlModels/private/qqmltreemodeltotablemodel_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qvariant.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QQmlTreeModelToTableModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK25QQmlTreeModelToTableModel10metaObjectEv(
    const QQmlTreeModelToTableModel *self) {
  return self->metaObject();
}

//  QString QQmlTreeModelToTableModel::tr(const char *s, const char *c, int
//      n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN25QQmlTreeModelToTableModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QQmlTreeModelToTableModel::tr(s, c, n));
}

//  QQmlTreeModelToTableModel::QQmlTreeModelToTableModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QQmlTreeModelToTableModel *ritual_ZN25QQmlTreeModelToTableModelC1EP7QObject(
    QObject *parent) {
  return new QQmlTreeModelToTableModel(parent);
}

//  QAbstractItemModel *QQmlTreeModelToTableModel::model() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK25QQmlTreeModelToTableModel5modelEv(
    const QQmlTreeModelToTableModel *self) {
  return self->model();
}

//  QModelIndex QQmlTreeModelToTableModel::rootIndex() const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel9rootIndexEv(
    const QQmlTreeModelToTableModel *self) {
  return new QModelIndex(self->rootIndex());
}

//  void QQmlTreeModelToTableModel::setRootIndex(const QModelIndex &idx)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel12setRootIndexERK11QModelIndex(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *idx) {
  self->setRootIndex(*idx);
}

//  void QQmlTreeModelToTableModel::resetRootIndex()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel14resetRootIndexEv(
    QQmlTreeModelToTableModel *self) {
  self->resetRootIndex();
}

//  QModelIndex QQmlTreeModelToTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel5indexEiiRK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QQmlTreeModelToTableModel::parent(const QModelIndex &child)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel6parentERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  int QQmlTreeModelToTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel8rowCountERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QQmlTreeModelToTableModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel11columnCountERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  QHash<int, QByteArray> QQmlTreeModelToTableModel::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK25QQmlTreeModelToTableModel9roleNamesEv(
    const QQmlTreeModelToTableModel *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QVariant QQmlTreeModelToTableModel::data(const QModelIndex &a0, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QQmlTreeModelToTableModel4dataERK11QModelIndexi(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *a0,
    int role) {
  return new QVariant(self->data(*a0, role));
}

//  bool QQmlTreeModelToTableModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlTreeModelToTableModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QQmlTreeModelToTableModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK25QQmlTreeModelToTableModel10headerDataEiN2Qt11OrientationEi(
    const QQmlTreeModelToTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  Qt::ItemFlags QQmlTreeModelToTableModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel5flagsERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  void QQmlTreeModelToTableModel::clearModelData()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel14clearModelDataEv(
    QQmlTreeModelToTableModel *self) {
  self->clearModelData();
}

//  bool QQmlTreeModelToTableModel::isVisible(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlTreeModelToTableModel9isVisibleERK11QModelIndex(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return self->isVisible(*index);
}

//  bool QQmlTreeModelToTableModel::childrenVisible(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN25QQmlTreeModelToTableModel15childrenVisibleERK11QModelIndex(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return self->childrenVisible(*index);
}

//  QModelIndex QQmlTreeModelToTableModel::mapToModel(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel10mapToModelERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->mapToModel(*index));
}

//  QModelIndex QQmlTreeModelToTableModel::mapFromModel(const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel12mapFromModelERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->mapFromModel(*index));
}

//  QModelIndex QQmlTreeModelToTableModel::mapToModel(int row) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK25QQmlTreeModelToTableModel10mapToModelEi(
    const QQmlTreeModelToTableModel *self,
    int row) {
  return new QModelIndex(self->mapToModel(row));
}

//  QItemSelection QQmlTreeModelToTableModel::selectionForRowRange(const
//      QModelIndex &fromIndex, const QModelIndex &toIndex) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK25QQmlTreeModelToTableModel20selectionForRowRangeERK11QModelIndexS2_(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *fromIndex,
    const QModelIndex *toIndex) {
  return new QItemSelection(
      self->selectionForRowRange(
          *fromIndex,
          *toIndex));
}

//  void QQmlTreeModelToTableModel::showModelTopLevelItems(bool doInsertRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel22showModelTopLevelItemsEb(
    QQmlTreeModelToTableModel *self,
    bool doInsertRows) {
  self->showModelTopLevelItems(doInsertRows);
}

//  int QQmlTreeModelToTableModel::itemIndex(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel9itemIndexERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return self->itemIndex(*index);
}

//  void QQmlTreeModelToTableModel::expandPendingRows(bool doInsertRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17expandPendingRowsEb(
    QQmlTreeModelToTableModel *self,
    bool doInsertRows) {
  self->expandPendingRows(doInsertRows);
}

//  int QQmlTreeModelToTableModel::lastChildIndex(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel14lastChildIndexERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return self->lastChildIndex(*index);
}

//  void QQmlTreeModelToTableModel::removeVisibleRows(int startIndex, int
//      endIndex, bool doRemoveRows)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17removeVisibleRowsEiib(
    QQmlTreeModelToTableModel *self,
    int startIndex,
    int endIndex,
    bool doRemoveRows) {
  self->removeVisibleRows(startIndex, endIndex, doRemoveRows);
}

//  void QQmlTreeModelToTableModel::dump() const
extern "C" Q_DECL_EXPORT
void ritual_ZNK25QQmlTreeModelToTableModel4dumpEv(
    const QQmlTreeModelToTableModel *self) {
  self->dump();
}

//  bool QQmlTreeModelToTableModel::testConsistency(bool dumpOnFail) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel15testConsistencyEb(
    const QQmlTreeModelToTableModel *self,
    bool dumpOnFail) {
  return self->testConsistency(dumpOnFail);
}

//  void QQmlTreeModelToTableModel::expand(const QModelIndex &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel6expandERK11QModelIndex(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *a0) {
  self->expand(*a0);
}

//  void QQmlTreeModelToTableModel::collapse(const QModelIndex &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel8collapseERK11QModelIndex(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *a0) {
  self->collapse(*a0);
}

//  void QQmlTreeModelToTableModel::setModel(QAbstractItemModel *model)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel8setModelEP18QAbstractItemModel(
    QQmlTreeModelToTableModel *self,
    QAbstractItemModel *model) {
  self->setModel(model);
}

//  bool QQmlTreeModelToTableModel::isExpanded(const QModelIndex &a0) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel10isExpandedERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *a0) {
  return self->isExpanded(*a0);
}

//  bool QQmlTreeModelToTableModel::isExpanded(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel10isExpandedEi(
    const QQmlTreeModelToTableModel *self,
    int row) {
  return self->isExpanded(row);
}

//  bool QQmlTreeModelToTableModel::hasChildren(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel11hasChildrenEi(
    const QQmlTreeModelToTableModel *self,
    int row) {
  return self->hasChildren(row);
}

//  bool QQmlTreeModelToTableModel::hasSiblings(int row) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel11hasSiblingsEi(
    const QQmlTreeModelToTableModel *self,
    int row) {
  return self->hasSiblings(row);
}

//  int QQmlTreeModelToTableModel::depthAtRow(int row) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK25QQmlTreeModelToTableModel10depthAtRowEi(
    const QQmlTreeModelToTableModel *self,
    int row) {
  return self->depthAtRow(row);
}

//  void QQmlTreeModelToTableModel::expandRow(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel9expandRowEi(
    QQmlTreeModelToTableModel *self,
    int n) {
  self->expandRow(n);
}

//  void QQmlTreeModelToTableModel::expandRecursively(int row, int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17expandRecursivelyEii(
    QQmlTreeModelToTableModel *self,
    int row,
    int depth) {
  self->expandRecursively(row, depth);
}

//  void QQmlTreeModelToTableModel::collapseRow(int n)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel11collapseRowEi(
    QQmlTreeModelToTableModel *self,
    int n) {
  self->collapseRow(n);
}

//  void QQmlTreeModelToTableModel::collapseRecursively(int row)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel19collapseRecursivelyEi(
    QQmlTreeModelToTableModel *self,
    int row) {
  self->collapseRecursively(row);
}

//  void QQmlTreeModelToTableModel::modelHasBeenDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel21modelHasBeenDestroyedEv(
    QQmlTreeModelToTableModel *self) {
  self->modelHasBeenDestroyed();
}

//  void QQmlTreeModelToTableModel::modelHasBeenReset()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17modelHasBeenResetEv(
    QQmlTreeModelToTableModel *self) {
  self->modelHasBeenReset();
}

//  void QQmlTreeModelToTableModel::modelLayoutAboutToBeChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel27modelLayoutAboutToBeChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQmlTreeModelToTableModel *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->modelLayoutAboutToBeChanged(*parents, hint);
}

//  void QQmlTreeModelToTableModel::modelLayoutChanged(const
//      QList<QPersistentModelIndex> &parents,
//      QAbstractItemModel::LayoutChangeHint hint)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel18modelLayoutChangedERK5QListI21QPersistentModelIndexEN18QAbstractItemModel16LayoutChangeHintE(
    QQmlTreeModelToTableModel *self,
    const QList<QPersistentModelIndex> *parents,
    QAbstractItemModel::LayoutChangeHint hint) {
  self->modelLayoutChanged(*parents, hint);
}

//  void QQmlTreeModelToTableModel::modelRowsAboutToBeInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel26modelRowsAboutToBeInsertedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAboutToBeInserted(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelRowsAboutToBeMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel23modelRowsAboutToBeMovedERK11QModelIndexiiS2_i(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationRow) {
  self->modelRowsAboutToBeMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationRow);
}

//  void QQmlTreeModelToTableModel::modelRowsAboutToBeRemoved(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel25modelRowsAboutToBeRemovedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsAboutToBeRemoved(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelRowsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17modelRowsInsertedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsInserted(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelRowsMoved(const QModelIndex
//      &sourceParent, int sourceStart, int sourceEnd, const QModelIndex
//      &destinationParent, int destinationRow)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel14modelRowsMovedERK11QModelIndexiiS2_i(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *sourceParent,
    int sourceStart,
    int sourceEnd,
    const QModelIndex *destinationParent,
    int destinationRow) {
  self->modelRowsMoved(
      *sourceParent,
      sourceStart,
      sourceEnd,
      *destinationParent,
      destinationRow);
}

//  void QQmlTreeModelToTableModel::modelRowsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel16modelRowsRemovedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelRowsRemoved(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelColumnsAboutToBeInserted(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel29modelColumnsAboutToBeInsertedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAboutToBeInserted(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelColumnsAboutToBeRemoved(const
//      QModelIndex &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel28modelColumnsAboutToBeRemovedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsAboutToBeRemoved(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelColumnsInserted(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel20modelColumnsInsertedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsInserted(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::modelColumnsRemoved(const QModelIndex
//      &parent, int start, int end)
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel19modelColumnsRemovedERK11QModelIndexii(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *parent,
    int start,
    int end) {
  self->modelColumnsRemoved(*parent, start, end);
}

//  void QQmlTreeModelToTableModel::enableSignalAggregation()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel23enableSignalAggregationEv(
    QQmlTreeModelToTableModel *self) {
  self->enableSignalAggregation();
}

//  void QQmlTreeModelToTableModel::disableSignalAggregation()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel24disableSignalAggregationEv(
    QQmlTreeModelToTableModel *self) {
  self->disableSignalAggregation();
}

//  bool QQmlTreeModelToTableModel::isAggregatingSignals() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK25QQmlTreeModelToTableModel20isAggregatingSignalsEv(
    const QQmlTreeModelToTableModel *self) {
  return self->isAggregatingSignals();
}

//  void QQmlTreeModelToTableModel::emitQueuedSignals()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel17emitQueuedSignalsEv(
    QQmlTreeModelToTableModel *self) {
  self->emitQueuedSignals();
}

//  void QQmlTreeModelToTableModel::connectToModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN25QQmlTreeModelToTableModel14connectToModelEv(
    QQmlTreeModelToTableModel *self) {
  self->connectToModel();
}

//  QModelIndex QQmlTreeModelToTableModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK25QQmlTreeModelToTableModel5indexEiiRK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(
      self->QQmlTreeModelToTableModel::index(
          row,
          column,
          *parent));
}

//  QModelIndex QQmlTreeModelToTableModel::parent(const QModelIndex &child)
//      const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK25QQmlTreeModelToTableModel6parentERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->QQmlTreeModelToTableModel::parent(*child));
}

//  int QQmlTreeModelToTableModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QQmlTreeModelToTableModel8rowCountERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *parent) {
  return self->QQmlTreeModelToTableModel::rowCount(*parent);
}

//  int QQmlTreeModelToTableModel::columnCount(const QModelIndex &parent)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QQmlTreeModelToTableModel11columnCountERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *parent) {
  return self->QQmlTreeModelToTableModel::columnCount(*parent);
}

//  QVariant QQmlTreeModelToTableModel::data(const QModelIndex &a0, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QQmlTreeModelToTableModel4dataERK11QModelIndexi(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *a0,
    int role) {
  return new QVariant(self->QQmlTreeModelToTableModel::data(*a0, role));
}

//  bool QQmlTreeModelToTableModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN25QQmlTreeModelToTableModel7setDataERK11QModelIndexRK8QVarianti(
    QQmlTreeModelToTableModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QQmlTreeModelToTableModel::setData(*index, *value, role);
}

//  QVariant QQmlTreeModelToTableModel::headerData(int section,
//      Qt::Orientation orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK25QQmlTreeModelToTableModel10headerDataEiN2Qt11OrientationEi(
    const QQmlTreeModelToTableModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(
      self->QQmlTreeModelToTableModel::headerData(
          section,
          orientation,
          role));
}

//  Qt::ItemFlags QQmlTreeModelToTableModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK25QQmlTreeModelToTableModel5flagsERK11QModelIndex(
    const QQmlTreeModelToTableModel *self,
    const QModelIndex *index) {
  return static_cast<int>(
      self->QQmlTreeModelToTableModel::flags(
          *index).toInt());
}
