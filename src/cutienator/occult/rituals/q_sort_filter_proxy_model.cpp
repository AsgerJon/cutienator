//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qsortfilterproxymodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qsortfilterproxymodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qitemselectionmodel.h>
#include <QtCore/qregularexpression.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>

//  const QMetaObject *QSortFilterProxyModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK21QSortFilterProxyModel10metaObjectEv(
    const QSortFilterProxyModel *self) {
  return self->metaObject();
}

//  QString QSortFilterProxyModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN21QSortFilterProxyModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QSortFilterProxyModel::tr(s, c, n));
}

//  QSortFilterProxyModel::QSortFilterProxyModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QSortFilterProxyModel *ritual_ZN21QSortFilterProxyModelC1EP7QObject(
    QObject *parent) {
  return new QSortFilterProxyModel(parent);
}

//  QSortFilterProxyModel::~QSortFilterProxyModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModelD1Ev(QSortFilterProxyModel *self) {
  delete self;
}

//  void QSortFilterProxyModel::setSourceModel(QAbstractItemModel
//      *sourceModel)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel14setSourceModelEP18QAbstractItemModel(
    QSortFilterProxyModel *self,
    QAbstractItemModel *sourceModel) {
  self->setSourceModel(sourceModel);
}

//  QModelIndex QSortFilterProxyModel::mapToSource(const QModelIndex
//      &proxyIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel11mapToSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *proxyIndex) {
  return new QModelIndex(self->mapToSource(*proxyIndex));
}

//  QModelIndex QSortFilterProxyModel::mapFromSource(const QModelIndex
//      &sourceIndex) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel13mapFromSourceERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *sourceIndex) {
  return new QModelIndex(self->mapFromSource(*sourceIndex));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionToSource(const
//      QItemSelection &proxySelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK21QSortFilterProxyModel20mapSelectionToSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *proxySelection) {
  return new QItemSelection(self->mapSelectionToSource(*proxySelection));
}

//  QItemSelection QSortFilterProxyModel::mapSelectionFromSource(const
//      QItemSelection &sourceSelection) const
extern "C" Q_DECL_EXPORT
QItemSelection *ritual_ZNK21QSortFilterProxyModel22mapSelectionFromSourceERK14QItemSelection(
    const QSortFilterProxyModel *self,
    const QItemSelection *sourceSelection) {
  return new QItemSelection(self->mapSelectionFromSource(*sourceSelection));
}

//  QRegularExpression QSortFilterProxyModel::filterRegularExpression() const
extern "C" Q_DECL_EXPORT
QRegularExpression *ritual_ZNK21QSortFilterProxyModel23filterRegularExpressionEv(
    const QSortFilterProxyModel *self) {
  return new QRegularExpression(self->filterRegularExpression());
}

//  int QSortFilterProxyModel::filterKeyColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel15filterKeyColumnEv(
    const QSortFilterProxyModel *self) {
  return self->filterKeyColumn();
}

//  void QSortFilterProxyModel::setFilterKeyColumn(int column)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel18setFilterKeyColumnEi(
    QSortFilterProxyModel *self,
    int column) {
  self->setFilterKeyColumn(column);
}

//  Qt::CaseSensitivity QSortFilterProxyModel::filterCaseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK21QSortFilterProxyModel21filterCaseSensitivityEv(
    const QSortFilterProxyModel *self) {
  return self->filterCaseSensitivity();
}

//  void QSortFilterProxyModel::setFilterCaseSensitivity(Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel24setFilterCaseSensitivityEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity cs) {
  self->setFilterCaseSensitivity(cs);
}

//  Qt::CaseSensitivity QSortFilterProxyModel::sortCaseSensitivity() const
extern "C" Q_DECL_EXPORT
Qt::CaseSensitivity ritual_ZNK21QSortFilterProxyModel19sortCaseSensitivityEv(
    const QSortFilterProxyModel *self) {
  return self->sortCaseSensitivity();
}

//  void QSortFilterProxyModel::setSortCaseSensitivity(Qt::CaseSensitivity
//      cs)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel22setSortCaseSensitivityEN2Qt15CaseSensitivityE(
    QSortFilterProxyModel *self,
    Qt::CaseSensitivity cs) {
  self->setSortCaseSensitivity(cs);
}

//  bool QSortFilterProxyModel::isSortLocaleAware() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel17isSortLocaleAwareEv(
    const QSortFilterProxyModel *self) {
  return self->isSortLocaleAware();
}

//  void QSortFilterProxyModel::setSortLocaleAware(bool on)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel18setSortLocaleAwareEb(
    QSortFilterProxyModel *self,
    bool on) {
  self->setSortLocaleAware(on);
}

//  int QSortFilterProxyModel::sortColumn() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel10sortColumnEv(
    const QSortFilterProxyModel *self) {
  return self->sortColumn();
}

//  Qt::SortOrder QSortFilterProxyModel::sortOrder() const
extern "C" Q_DECL_EXPORT
Qt::SortOrder ritual_ZNK21QSortFilterProxyModel9sortOrderEv(
    const QSortFilterProxyModel *self) {
  return self->sortOrder();
}

//  bool QSortFilterProxyModel::dynamicSortFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel17dynamicSortFilterEv(
    const QSortFilterProxyModel *self) {
  return self->dynamicSortFilter();
}

//  void QSortFilterProxyModel::setDynamicSortFilter(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel20setDynamicSortFilterEb(
    QSortFilterProxyModel *self,
    bool enable) {
  self->setDynamicSortFilter(enable);
}

//  int QSortFilterProxyModel::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel8sortRoleEv(
    const QSortFilterProxyModel *self) {
  return self->sortRole();
}

//  void QSortFilterProxyModel::setSortRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel11setSortRoleEi(
    QSortFilterProxyModel *self,
    int role) {
  self->setSortRole(role);
}

//  int QSortFilterProxyModel::filterRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel10filterRoleEv(
    const QSortFilterProxyModel *self) {
  return self->filterRole();
}

//  void QSortFilterProxyModel::setFilterRole(int role)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel13setFilterRoleEi(
    QSortFilterProxyModel *self,
    int role) {
  self->setFilterRole(role);
}

//  bool QSortFilterProxyModel::isRecursiveFilteringEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel27isRecursiveFilteringEnabledEv(
    const QSortFilterProxyModel *self) {
  return self->isRecursiveFilteringEnabled();
}

//  void QSortFilterProxyModel::setRecursiveFilteringEnabled(bool recursive)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel28setRecursiveFilteringEnabledEb(
    QSortFilterProxyModel *self,
    bool recursive) {
  self->setRecursiveFilteringEnabled(recursive);
}

//  bool QSortFilterProxyModel::autoAcceptChildRows() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel19autoAcceptChildRowsEv(
    const QSortFilterProxyModel *self) {
  return self->autoAcceptChildRows();
}

//  void QSortFilterProxyModel::setAutoAcceptChildRows(bool accept)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel22setAutoAcceptChildRowsEb(
    QSortFilterProxyModel *self,
    bool accept) {
  self->setAutoAcceptChildRows(accept);
}

//  void QSortFilterProxyModel::setFilterRegularExpression(const QString
//      &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterRegularExpression(*pattern);
}

//  void QSortFilterProxyModel::setFilterRegularExpression(const
//      QRegularExpression &regularExpression)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel26setFilterRegularExpressionERK18QRegularExpression(
    QSortFilterProxyModel *self,
    const QRegularExpression *regularExpression) {
  self->setFilterRegularExpression(*regularExpression);
}

//  void QSortFilterProxyModel::setFilterWildcard(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel17setFilterWildcardERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterWildcard(*pattern);
}

//  void QSortFilterProxyModel::setFilterFixedString(const QString &pattern)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel20setFilterFixedStringERK7QString(
    QSortFilterProxyModel *self,
    const QString *pattern) {
  self->setFilterFixedString(*pattern);
}

//  void QSortFilterProxyModel::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel10invalidateEv(
    QSortFilterProxyModel *self) {
  self->invalidate();
}

//  QModelIndex QSortFilterProxyModel::index(int row, int column, const
//      QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel5indexEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *parent) {
  return new QModelIndex(self->index(row, column, *parent));
}

//  QModelIndex QSortFilterProxyModel::parent(const QModelIndex &child) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel6parentERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *child) {
  return new QModelIndex(self->parent(*child));
}

//  QModelIndex QSortFilterProxyModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel7siblingEiiRK11QModelIndex(
    const QSortFilterProxyModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  int QSortFilterProxyModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel8rowCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  int QSortFilterProxyModel::columnCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel11columnCountERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->columnCount(*parent);
}

//  bool QSortFilterProxyModel::hasChildren(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel11hasChildrenERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->hasChildren(*parent);
}

//  QVariant QSortFilterProxyModel::data(const QModelIndex &index, int role)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QSortFilterProxyModel4dataERK11QModelIndexi(
    const QSortFilterProxyModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QSortFilterProxyModel::setData(const QModelIndex &index, const
//      QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel7setDataERK11QModelIndexRK8QVarianti(
    QSortFilterProxyModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  QVariant QSortFilterProxyModel::headerData(int section, Qt::Orientation
//      orientation, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK21QSortFilterProxyModel10headerDataEiN2Qt11OrientationEi(
    const QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    int role) {
  return new QVariant(self->headerData(section, orientation, role));
}

//  bool QSortFilterProxyModel::setHeaderData(int section, Qt::Orientation
//      orientation, const QVariant &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13setHeaderDataEiN2Qt11OrientationERK8QVarianti(
    QSortFilterProxyModel *self,
    int section,
    Qt::Orientation orientation,
    const QVariant *value,
    int role) {
  return self->setHeaderData(section, orientation, *value, role);
}

//  bool QSortFilterProxyModel::dropMimeData(const QMimeData *data,
//      Qt::DropAction action, int row, int column, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel12dropMimeDataEPK9QMimeDataN2Qt10DropActionEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    const QMimeData *data,
    Qt::DropAction action,
    int row,
    int column,
    const QModelIndex *parent) {
  return self->dropMimeData(data, action, row, column, *parent);
}

//  bool QSortFilterProxyModel::insertRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel10insertRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::insertColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13insertColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->insertColumns(column, count, *parent);
}

//  bool QSortFilterProxyModel::removeRows(int row, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel10removeRowsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QSortFilterProxyModel::removeColumns(int column, int count, const
//      QModelIndex &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN21QSortFilterProxyModel13removeColumnsEiiRK11QModelIndex(
    QSortFilterProxyModel *self,
    int column,
    int count,
    const QModelIndex *parent) {
  return self->removeColumns(column, count, *parent);
}

//  void QSortFilterProxyModel::fetchMore(const QModelIndex &parent)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel9fetchMoreERK11QModelIndex(
    QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  self->fetchMore(*parent);
}

//  bool QSortFilterProxyModel::canFetchMore(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QSortFilterProxyModel12canFetchMoreERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *parent) {
  return self->canFetchMore(*parent);
}

//  Qt::ItemFlags QSortFilterProxyModel::flags(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel5flagsERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  QModelIndex QSortFilterProxyModel::buddy(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK21QSortFilterProxyModel5buddyERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QModelIndex(self->buddy(*index));
}

//  QSize QSortFilterProxyModel::span(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK21QSortFilterProxyModel4spanERK11QModelIndex(
    const QSortFilterProxyModel *self,
    const QModelIndex *index) {
  return new QSize(self->span(*index));
}

//  void QSortFilterProxyModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QSortFilterProxyModel4sortEiN2Qt9SortOrderE(
    QSortFilterProxyModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  Qt::DropActions QSortFilterProxyModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QSortFilterProxyModel20supportedDropActionsEv(
    const QSortFilterProxyModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}
