//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qrangemodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qcollator.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QRangeModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK11QRangeModel10metaObjectEv(
    const QRangeModel *self) {
  return self->metaObject();
}

//  QString QRangeModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN11QRangeModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QRangeModel::tr(s, c, n));
}

//  QRangeModel::~QRangeModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModelD1Ev(QRangeModel *self) {
  delete self;
}

//  QModelIndex QRangeModel::index(int row, int column, const QModelIndex
//      &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel5indexEiiRK11QModelIndex(
    const QRangeModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QRangeModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel6parentERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QRangeModel::sibling(int row, int column, const QModelIndex
//      &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel7siblingEiiRK11QModelIndex(
    const QRangeModel *self,
    int row,
    int column,
    const QModelIndex *index) {
  return new QModelIndex(self->sibling(row, column, *index));
}

//  int QRangeModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel8rowCountERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QRangeModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel11columnCountERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  Qt::ItemFlags QRangeModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel5flagsERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QVariant QRangeModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QRangeModel10headerDataEiN2Qt11OrientationEi(
    const QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QRangeModel::setHeaderData(int section, Qt::Orientation orientation,
//      const QVariant &data, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QRangeModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *data,
    int role) {
  return self->setHeaderData(section, orientation, *data, role);
}

//  QVariant QRangeModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK11QRangeModel4dataERK11QModelIndexi(
    const QRangeModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QRangeModel::setData(const QModelIndex &index, const QVariant &data,
//      int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel7setDataERK11QModelIndexRK8QVarianti(
    QRangeModel *self,
    const QModelIndex *index,
    const QVariant *data,
    int role) {
  return self->setData(*index, *data, role);
}

//  bool QRangeModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13clearItemDataERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  bool QRangeModel::insertColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13insertColumnsEiiRK11QModelIndex(
    QRangeModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QRangeModel::removeColumns(int column, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel13removeColumnsEiiRK11QModelIndex(
    QRangeModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  bool QRangeModel::moveColumns(const QModelIndex &sourceParent, int
//      sourceColumn, int count, const QModelIndex &destParent, int
//      destColumn)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel11moveColumnsERK11QModelIndexiiS2_i(
    QRangeModel *self,
    const QModelIndex *sourceParent,
    int sourceColumn,
    int count,
    const QModelIndex *destParent,
    int destColumn) {
  return self->moveColumns(
      *sourceParent,
      sourceColumn,
      count,
      *destParent,
      destColumn);
}

//  bool QRangeModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel10insertRowsEiiRK11QModelIndex(
    QRangeModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QRangeModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel10removeRowsEiiRK11QModelIndex(
    QRangeModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QRangeModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destParent, int destRow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel8moveRowsERK11QModelIndexiiS2_i(
    QRangeModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destParent,
    int destRow) {
  return self->moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destParent,
      destRow);
}

//  void QRangeModel::resetRoleNames()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel14resetRoleNamesEv(QRangeModel *self) {
  self->resetRoleNames();
}

//  bool QRangeModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel12canFetchMoreERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  void QRangeModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel9fetchMoreERK11QModelIndex(
    QRangeModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QRangeModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel11hasChildrenERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QModelIndex QRangeModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK11QRangeModel5buddyERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  bool QRangeModel::canDropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK11QRangeModel15canDropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    const QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->canDropMimeData(data, action, row, column, *parent);
}

//  bool QRangeModel::dropMimeData(const QMimeData *data, Qt::DropAction
//      action, int row, int column, const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN11QRangeModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QRangeModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  void QRangeModel::multiData(const QModelIndex &index, QModelRoleDataSpan
//      roleDataSpan) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK11QRangeModel9multiDataERK11QModelIndex18QModelRoleDataSpan(
    const QRangeModel *self,
    const QModelIndex *index,
    const QModelRoleDataSpan *roleDataSpan) {
  self->multiData(*index, *roleDataSpan);
}

//  void QRangeModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel4sortEiN2Qt9SortOrderE(
    QRangeModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QCollator QRangeModel::sortCollator() const
extern "C" Q_DECL_EXPORT
QCollator *ritual_ZNK11QRangeModel12sortCollatorEv(const QRangeModel *self) {
  return new QCollator(self->sortCollator());
}

//  void QRangeModel::setSortCollator(const QCollator &collator)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel15setSortCollatorERK9QCollator(
    QRangeModel *self,
    const QCollator *collator) {
  self->setSortCollator(*collator);
}

//  void QRangeModel::resetSortCollator()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel17resetSortCollatorEv(QRangeModel *self) {
  self->resetSortCollator();
}

//  int QRangeModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel8sortRoleEv(const QRangeModel *self) {
  return self->sortRole();
}

//  void QRangeModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel11setSortRoleEi(QRangeModel *self, int role) {
  self->setSortRole(role);
}

//  void QRangeModel::resetSortRole()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel13resetSortRoleEv(QRangeModel *self) {
  self->resetSortRole();
}

//  QSize QRangeModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK11QRangeModel4spanERK11QModelIndex(
    const QRangeModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  Qt::DropActions QRangeModel::supportedDragActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel20supportedDragActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->supportedDragActions().toInt());
}

//  void QRangeModel::setSupportedDragActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel23setSupportedDragActionsE6QFlagsIN2Qt10DropActionEE(
    QRangeModel *self,
    int actions) {
  self->setSupportedDragActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QRangeModel::resetSupportedDragActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel25resetSupportedDragActionsEv(QRangeModel *self) {
  self->resetSupportedDragActions();
}

//  Qt::DropActions QRangeModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK11QRangeModel20supportedDropActionsEv(
    const QRangeModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  void QRangeModel::setSupportedDropActions(Qt::DropActions actions)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel23setSupportedDropActionsE6QFlagsIN2Qt10DropActionEE(
    QRangeModel *self,
    int actions) {
  self->setSupportedDropActions(QFlags<Qt::DropAction>::fromInt(actions));
}

//  void QRangeModel::resetSupportedDropActions()
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel25resetSupportedDropActionsEv(QRangeModel *self) {
  self->resetSupportedDropActions();
}

//  AutoConnectPolicy QRangeModel::autoConnectPolicy() const
extern "C" Q_DECL_EXPORT
QRangeModel::AutoConnectPolicy ritual_ZNK11QRangeModel17autoConnectPolicyEv(
    const QRangeModel *self) {
  return self->autoConnectPolicy();
}

//  void QRangeModel::setAutoConnectPolicy(AutoConnectPolicy policy)
extern "C" Q_DECL_EXPORT
void ritual_ZN11QRangeModel20setAutoConnectPolicyENS_17AutoConnectPolicyE(
    QRangeModel *self,
    QRangeModel::AutoConnectPolicy policy) {
  self->setAutoConnectPolicy(policy);
}
