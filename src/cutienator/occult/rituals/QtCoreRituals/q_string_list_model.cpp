//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qstringlistmodel.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(stringlistmodel)
#if QT_CONFIG(stringlistmodel)
#include <QtCore/qstringlistmodel.h>
#include <QtCore/qstring.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>

//  const QMetaObject *QStringListModel::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK16QStringListModel10metaObjectEv(
    const QStringListModel *self) {
  return self->metaObject();
}

//  QString QStringListModel::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN16QStringListModel2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QStringListModel::tr(s, c, n));
}

//  QStringListModel::QStringListModel(QObject *parent)
extern "C" Q_DECL_EXPORT
QStringListModel *ritual_ZN16QStringListModelC1EP7QObject(QObject *parent) {
  return new QStringListModel(parent);
}

//  QStringListModel::QStringListModel(const QStringList &strings, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QStringListModel *ritual_ZN16QStringListModelC1ERK5QListI7QStringEP7QObject(
    const QList<QString> *strings,
    QObject *parent) {
  return new QStringListModel(*strings, parent);
}

//  int QStringListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QStringListModel8rowCountERK11QModelIndex(
    const QStringListModel *self,
    const QModelIndex *parent) {
  return self->rowCount(*parent);
}

//  QModelIndex QStringListModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK16QStringListModel7siblingEiiRK11QModelIndex(
    const QStringListModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->sibling(row, column, *idx));
}

//  QVariant QStringListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK16QStringListModel4dataERK11QModelIndexi(
    const QStringListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->data(*index, role));
}

//  bool QStringListModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel7setDataERK11QModelIndexRK8QVarianti(
    QStringListModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->setData(*index, *value, role);
}

//  bool QStringListModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel13clearItemDataERK11QModelIndex(
    QStringListModel *self,
    const QModelIndex *index) {
  return self->clearItemData(*index);
}

//  Qt::ItemFlags QStringListModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QStringListModel5flagsERK11QModelIndex(
    const QStringListModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->flags(*index).toInt());
}

//  bool QStringListModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel10insertRowsEiiRK11QModelIndex(
    QStringListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->insertRows(row, count, *parent);
}

//  bool QStringListModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel10removeRowsEiiRK11QModelIndex(
    QStringListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->removeRows(row, count, *parent);
}

//  bool QStringListModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel8moveRowsERK11QModelIndexiiS2_i(
    QStringListModel *self,
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

//  QMap<int, QVariant> QStringListModel::itemData(const QModelIndex &index)
//      const
extern "C" Q_DECL_EXPORT
QMap<int, QVariant> *ritual_ZNK16QStringListModel8itemDataERK11QModelIndex(
    const QStringListModel *self,
    const QModelIndex *index) {
  return new QMap<int, QVariant>(self->itemData(*index));
}

//  bool QStringListModel::setItemData(const QModelIndex &index, const
//      QMap<int, QVariant> &roles)
extern "C" Q_DECL_EXPORT
bool ritual_ZN16QStringListModel11setItemDataERK11QModelIndexRK4QMapIi8QVariantE(
    QStringListModel *self,
    const QModelIndex *index,
    const QMap<int, QVariant> *roles) {
  return self->setItemData(*index, *roles);
}

//  void QStringListModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStringListModel4sortEiN2Qt9SortOrderE(
    QStringListModel *self,
    int column,
    Qt::SortOrder order) {
  self->sort(column, order);
}

//  QStringList QStringListModel::stringList() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK16QStringListModel10stringListEv(
    const QStringListModel *self) {
  return new QList<QString>(self->stringList());
}

//  void QStringListModel::setStringList(const QStringList &strings)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QStringListModel13setStringListERK5QListI7QStringE(
    QStringListModel *self,
    const QList<QString> *strings) {
  self->setStringList(*strings);
}

//  Qt::DropActions QStringListModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK16QStringListModel20supportedDropActionsEv(
    const QStringListModel *self) {
  return static_cast<int>(self->supportedDropActions().toInt());
}

//  int QStringListModel::rowCount(const QModelIndex &parent) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QStringListModel8rowCountERK11QModelIndex(
    const QStringListModel *self,
    const QModelIndex *parent) {
  return self->QStringListModel::rowCount(*parent);
}

//  QModelIndex QStringListModel::sibling(int row, int column, const
//      QModelIndex &idx) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_own_ZNK16QStringListModel7siblingEiiRK11QModelIndex(
    const QStringListModel *self,
    int row,
    int column,
    const QModelIndex *idx) {
  return new QModelIndex(self->QStringListModel::sibling(row, column, *idx));
}

//  QVariant QStringListModel::data(const QModelIndex &index, int role) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK16QStringListModel4dataERK11QModelIndexi(
    const QStringListModel *self,
    const QModelIndex *index,
    int role) {
  return new QVariant(self->QStringListModel::data(*index, role));
}

//  bool QStringListModel::setData(const QModelIndex &index, const QVariant
//      &value, int role)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QStringListModel7setDataERK11QModelIndexRK8QVarianti(
    QStringListModel *self,
    const QModelIndex *index,
    const QVariant *value,
    int role) {
  return self->QStringListModel::setData(*index, *value, role);
}

//  bool QStringListModel::clearItemData(const QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QStringListModel13clearItemDataERK11QModelIndex(
    QStringListModel *self,
    const QModelIndex *index) {
  return self->QStringListModel::clearItemData(*index);
}

//  Qt::ItemFlags QStringListModel::flags(const QModelIndex &index) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QStringListModel5flagsERK11QModelIndex(
    const QStringListModel *self,
    const QModelIndex *index) {
  return static_cast<int>(self->QStringListModel::flags(*index).toInt());
}

//  bool QStringListModel::insertRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QStringListModel10insertRowsEiiRK11QModelIndex(
    QStringListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QStringListModel::insertRows(row, count, *parent);
}

//  bool QStringListModel::removeRows(int row, int count, const QModelIndex
//      &parent)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QStringListModel10removeRowsEiiRK11QModelIndex(
    QStringListModel *self,
    int row,
    int count,
    const QModelIndex *parent) {
  return self->QStringListModel::removeRows(row, count, *parent);
}

//  bool QStringListModel::moveRows(const QModelIndex &sourceParent, int
//      sourceRow, int count, const QModelIndex &destinationParent, int
//      destinationChild)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN16QStringListModel8moveRowsERK11QModelIndexiiS2_i(
    QStringListModel *self,
    const QModelIndex *sourceParent,
    int sourceRow,
    int count,
    const QModelIndex *destinationParent,
    int destinationChild) {
  return self->QStringListModel::moveRows(
      *sourceParent,
      sourceRow,
      count,
      *destinationParent,
      destinationChild);
}

//  void QStringListModel::sort(int column, Qt::SortOrder order)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN16QStringListModel4sortEiN2Qt9SortOrderE(
    QStringListModel *self,
    int column,
    Qt::SortOrder order) {
  self->QStringListModel::sort(column, order);
}

//  Qt::DropActions QStringListModel::supportedDropActions() const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK16QStringListModel20supportedDropActionsEv(
    const QStringListModel *self) {
  return static_cast<int>(
      self->QStringListModel::supportedDropActions().toInt());
}

#endif  // QT_CONFIG(stringlistmodel)
#endif  // QT_CONFIG(stringlistmodel)
