//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qabstractproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qabstractproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QAbstractProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QAbstractProxyModel10metaObjectEv(
    const QAbstractProxyModel *self) {
  return self->metaObject();
}

//  QString QAbstractProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QAbstractProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstractProxyModel::tr(s, c, n));
}

//  QAbstractProxyModel::~QAbstractProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModelD1Ev(QAbstractProxyModel *self) {
  delete self;
}

//  void QAbstractProxyModel::setSourceModel(QAbstractItemModel *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel14setSourceModelEP18QAbstractItemModel(
    QAbstractProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  QAbstractItemModel *QAbstractProxyModel::sourceModel() const
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZNK19QAbstractProxyModel11sourceModelEv(
    const QAbstractProxyModel *self) {
  return self->sourceModel();
}

//  QModelIndex QAbstractProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel11mapToSourceERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QAbstractProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel13mapFromSourceERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QItemSelection QAbstractProxyModel::mapSelectionToSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QAbstractProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionToSource(*selection));
}

//  QItemSelection QAbstractProxyModel::mapSelectionFromSource(const
//      QItemSelection &selection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK19QAbstractProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QAbstractProxyModel *self,
    const QItemSelection *selection) {
  return new QItemSelection(self->mapSelectionFromSource(*selection));
}

//  bool QAbstractProxyModel::submit()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel6submitEv(QAbstractProxyModel *self) {
  return self->submit();
}

//  void QAbstractProxyModel::revert()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel6revertEv(QAbstractProxyModel *self) {
  self->revert();
}

//  QVariant QAbstractProxyModel::data(const QModelIndex &proxyIndex, int
//      role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAbstractProxyModel4dataERK11QModelIndexi(
    const QAbstractProxyModel *self,
    const QModelIndex *proxyIndex,
    int role) {
  return new QVariant(self->data(*proxyIndex, role));
}

//  QVariant QAbstractProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK19QAbstractProxyModel10headerDataEiN2Qt11OrientationEi(
    const QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  Qt::ItemFlags QAbstractProxyModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel5flagsERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  bool QAbstractProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QAbstractProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QAbstractProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QAbstractProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QAbstractProxyModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel13clearItemDataERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  QModelIndex QAbstractProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel5buddyERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  bool QAbstractProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel12canFetchMoreERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QAbstractProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel9fetchMoreERK11QModelIndex(
    QAbstractProxyModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  void QAbstractProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QAbstractProxyModel4sortEiN2Qt9SortOrderE(
    QAbstractProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QSize QAbstractProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK19QAbstractProxyModel4spanERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  bool QAbstractProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel11hasChildrenERK11QModelIndex(
    const QAbstractProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QModelIndex QAbstractProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QAbstractProxyModel7siblingEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  bool QAbstractProxyModel::canDropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QAbstractProxyModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QAbstractProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QAbstractProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QAbstractProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  Qt::DropActions QAbstractProxyModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel20supportedDragActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  Qt::DropActions QAbstractProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QAbstractProxyModel20supportedDropActionsEv(
    const QAbstractProxyModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}
