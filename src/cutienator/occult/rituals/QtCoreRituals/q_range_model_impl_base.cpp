//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qrangemodel_impl.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#if QT_CONFIG(rangemodel)
#if !defined(Q_QDOC)
#include <QtCore/qrangemodel.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qabstractitemmodel.h>
#include <QtCore/qvariant.h>
#include <QtCore/qcompare.h>
#include <QtCore/qobjectdefs.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>
#include <QtCore/qmap.h>
#include <QtCore/qhash.h>
#include <iterator>
#include <QtCore/QScopedValueRollback>

//  QHash<int, QByteArray> QRangeModelImplBase::roleNames() const
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZNK19QRangeModelImplBase9roleNamesEv(
    const QRangeModelImplBase *self) {
  return new QHash<int, QByteArray>(self->roleNames());
}

//  QRangeModelImplBase *QRangeModelImplBase::getImplementation(QRangeModel
//      *model)
extern "C" Q_DECL_EXPORT
QRangeModelImplBase *ritual_ZN19QRangeModelImplBase17getImplementationEP11QRangeModel(
    QRangeModel *model) {
  return QRangeModelImplBase::getImplementation(model);
}

//  const QRangeModelImplBase *QRangeModelImplBase::getImplementation(const
//      QRangeModel *model)
extern "C" Q_DECL_EXPORT
const QRangeModelImplBase *ritual_ZN19QRangeModelImplBase17getImplementationEPK11QRangeModel(
    const QRangeModel *model) {
  return QRangeModelImplBase::getImplementation(model);
}

//  QRangeModelImplBase::QRangeModelImplBase(QRangeModel *itemModel)
extern "C" Q_DECL_EXPORT
QRangeModelImplBase *ritual_ZN19QRangeModelImplBaseC1EP11QRangeModel(
    QRangeModel *itemModel) {
  return new QRangeModelImplBase(itemModel);
}

//  QModelIndex QRangeModelImplBase::createIndex(int row, int column, const
//      void *ptr) const
extern "C" Q_DECL_EXPORT
QModelIndex *ritual_ZNK19QRangeModelImplBase11createIndexEiiPKv(
    const QRangeModelImplBase *self,
    int row,
    int column,
    const void *ptr) {
  return new QModelIndex(self->createIndex(row, column, ptr));
}

//  QModelIndexList QRangeModelImplBase::persistentIndexList() const
extern "C" Q_DECL_EXPORT
QList<QModelIndex> *ritual_ZNK19QRangeModelImplBase19persistentIndexListEv(
    const QRangeModelImplBase *self) {
  return new QList<QModelIndex>(self->persistentIndexList());
}

//  void QRangeModelImplBase::changePersistentIndex(const QModelIndex &from,
//      const QModelIndex &to)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase21changePersistentIndexERK11QModelIndexS2_(
    QRangeModelImplBase *self,
    const QModelIndex *from,
    const QModelIndex *to) {
  self->changePersistentIndex(*from, *to);
}

//  void QRangeModelImplBase::dataChanged(const QModelIndex &from, const
//      QModelIndex &to, const QList<int> &roles)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase11dataChangedERK11QModelIndexS2_RK5QListIiE(
    QRangeModelImplBase *self,
    const QModelIndex *from,
    const QModelIndex *to,
    const QList<int> *roles) {
  self->dataChanged(*from, *to, *roles);
}

//  void QRangeModelImplBase::beginResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase15beginResetModelEv(
    QRangeModelImplBase *self) {
  self->beginResetModel();
}

//  void QRangeModelImplBase::endResetModel()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase13endResetModelEv(
    QRangeModelImplBase *self) {
  self->endResetModel();
}

//  void QRangeModelImplBase::beginInsertColumns(const QModelIndex &parent,
//      int start, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase18beginInsertColumnsERK11QModelIndexii(
    QRangeModelImplBase *self,
    const QModelIndex *parent,
    int start,
    int count) {
  self->beginInsertColumns(*parent, start, count);
}

//  void QRangeModelImplBase::endInsertColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase16endInsertColumnsEv(
    QRangeModelImplBase *self) {
  self->endInsertColumns();
}

//  void QRangeModelImplBase::beginRemoveColumns(const QModelIndex &parent,
//      int start, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase18beginRemoveColumnsERK11QModelIndexii(
    QRangeModelImplBase *self,
    const QModelIndex *parent,
    int start,
    int count) {
  self->beginRemoveColumns(*parent, start, count);
}

//  void QRangeModelImplBase::endRemoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase16endRemoveColumnsEv(
    QRangeModelImplBase *self) {
  self->endRemoveColumns();
}

//  bool QRangeModelImplBase::beginMoveColumns(const QModelIndex
//      &sourceParent, int sourceFirst, int sourceLast, const QModelIndex
//      &destParent, int destRow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase16beginMoveColumnsERK11QModelIndexiiS2_i(
    QRangeModelImplBase *self,
    const QModelIndex *sourceParent,
    int sourceFirst,
    int sourceLast,
    const QModelIndex *destParent,
    int destRow) {
  return self->beginMoveColumns(
      *sourceParent,
      sourceFirst,
      sourceLast,
      *destParent,
      destRow);
}

//  void QRangeModelImplBase::endMoveColumns()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase14endMoveColumnsEv(
    QRangeModelImplBase *self) {
  self->endMoveColumns();
}

//  void QRangeModelImplBase::beginInsertRows(const QModelIndex &parent, int
//      start, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase15beginInsertRowsERK11QModelIndexii(
    QRangeModelImplBase *self,
    const QModelIndex *parent,
    int start,
    int count) {
  self->beginInsertRows(*parent, start, count);
}

//  void QRangeModelImplBase::endInsertRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase13endInsertRowsEv(
    QRangeModelImplBase *self) {
  self->endInsertRows();
}

//  void QRangeModelImplBase::beginRemoveRows(const QModelIndex &parent, int
//      start, int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase15beginRemoveRowsERK11QModelIndexii(
    QRangeModelImplBase *self,
    const QModelIndex *parent,
    int start,
    int count) {
  self->beginRemoveRows(*parent, start, count);
}

//  void QRangeModelImplBase::endRemoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase13endRemoveRowsEv(
    QRangeModelImplBase *self) {
  self->endRemoveRows();
}

//  bool QRangeModelImplBase::beginMoveRows(const QModelIndex &sourceParent,
//      int sourceFirst, int sourceLast, const QModelIndex &destParent, int
//      destRow)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase13beginMoveRowsERK11QModelIndexiiS2_i(
    QRangeModelImplBase *self,
    const QModelIndex *sourceParent,
    int sourceFirst,
    int sourceLast,
    const QModelIndex *destParent,
    int destRow) {
  return self->beginMoveRows(
      *sourceParent,
      sourceFirst,
      sourceLast,
      *destParent,
      destRow);
}

//  void QRangeModelImplBase::endMoveRows()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase11endMoveRowsEv(
    QRangeModelImplBase *self) {
  self->endMoveRows();
}

//  void QRangeModelImplBase::beginLayoutChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase17beginLayoutChangeEv(
    QRangeModelImplBase *self) {
  self->beginLayoutChange();
}

//  void QRangeModelImplBase::endLayoutChange()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QRangeModelImplBase15endLayoutChangeEv(
    QRangeModelImplBase *self) {
  self->endLayoutChange();
}

//  AutoConnectPolicy QRangeModelImplBase::autoConnectPolicy() const
extern "C" Q_DECL_EXPORT
QRangeModelImplBase::AutoConnectPolicy ritual_ZNK19QRangeModelImplBase17autoConnectPolicyEv(
    const QRangeModelImplBase *self) {
  return self->autoConnectPolicy();
}

//  Qt::weak_ordering QRangeModelImplBase::compareData(const QVariant &lhs,
//      const QVariant &rhs, const QCollator *collator)
extern "C" Q_DECL_EXPORT
Qt::weak_ordering *ritual_ZN19QRangeModelImplBase11compareDataERK8QVariantS2_PK9QCollator(
    const QVariant *lhs,
    const QVariant *rhs,
    const QCollator *collator) {
  return new Qt::weak_ordering(
      QRangeModelImplBase::compareData(
          *lhs,
          *rhs,
          collator));
}

//  QAbstractItemModel &QRangeModelImplBase::itemModel()
extern "C" Q_DECL_EXPORT
QAbstractItemModel *ritual_ZN19QRangeModelImplBase9itemModelEv(
    QRangeModelImplBase *self) {
  return &(self->itemModel());
}

//  const QAbstractItemModel &QRangeModelImplBase::itemModel() const
extern "C" Q_DECL_EXPORT
const QAbstractItemModel *ritual_ZNK19QRangeModelImplBase9itemModelEv(
    const QRangeModelImplBase *self) {
  return &(self->itemModel());
}

//  QHash<int, QByteArray> QRangeModelImplBase::roleNamesForMetaObject(const
//      QAbstractItemModel &model, const QMetaObject &metaObject)
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZN19QRangeModelImplBase22roleNamesForMetaObjectERK18QAbstractItemModelRK11QMetaObject(
    const QAbstractItemModel *model,
    const QMetaObject *metaObject) {
  return new QHash<int, QByteArray>(
      QRangeModelImplBase::roleNamesForMetaObject(
          *model,
          *metaObject));
}

//  QHash<int, QByteArray> QRangeModelImplBase::roleNamesForSimpleType()
extern "C" Q_DECL_EXPORT
QHash<int, QByteArray> *ritual_ZN19QRangeModelImplBase22roleNamesForSimpleTypeEv() {
  return new QHash<int, QByteArray>(
      QRangeModelImplBase::roleNamesForSimpleType());
}

//  QScopedValueRollback<bool>
//      QRangeModelImplBase::blockDataChangedDispatch()
extern "C" Q_DECL_EXPORT
QScopedValueRollback<bool> *ritual_ZN19QRangeModelImplBase24blockDataChangedDispatchEv(
    QRangeModelImplBase *self) {
  return new QScopedValueRollback<bool>(self->blockDataChangedDispatch());
}

//  QHash<int, QMetaProperty> QRangeModelImplBase::roleProperties(const
//      QAbstractItemModel &model, const QMetaObject &metaObject)
extern "C" Q_DECL_EXPORT
QHash<int, QMetaProperty> *ritual_ZN19QRangeModelImplBase14rolePropertiesERK18QAbstractItemModelRK11QMetaObject(
    const QAbstractItemModel *model,
    const QMetaObject *metaObject) {
  return new QHash<int, QMetaProperty>(
      QRangeModelImplBase::roleProperties(
          *model,
          *metaObject));
}

//  QHash<int, QMetaProperty> QRangeModelImplBase::columnProperties(const
//      QMetaObject &metaObject)
extern "C" Q_DECL_EXPORT
QHash<int, QMetaProperty> *ritual_ZN19QRangeModelImplBase16columnPropertiesERK11QMetaObject(
    const QMetaObject *metaObject) {
  return new QHash<int, QMetaProperty>(
      QRangeModelImplBase::columnProperties(
          *metaObject));
}

//  bool QRangeModelImplBase::connectProperty(const QModelIndex &index, const
//      QObject *item, QRangeModelDetails::AutoConnectContext *context, int
//      role, const QMetaProperty &property)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase15connectPropertyERK11QModelIndexPK7QObjectPN18QRangeModelDetails18AutoConnectContextEiRK13QMetaProperty(
    const QModelIndex *index,
    const QObject *item,
    QRangeModelDetails::AutoConnectContext *context,
    int role,
    const QMetaProperty *property) {
  return QRangeModelImplBase::connectProperty(
      *index,
      item,
      context,
      role,
      *property);
}

//  bool QRangeModelImplBase::connectPropertyConst(const QModelIndex &index,
//      const QObject *item, QRangeModelDetails::AutoConnectContext *context,
//      int role, const QMetaProperty &property)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase20connectPropertyConstERK11QModelIndexPK7QObjectPN18QRangeModelDetails18AutoConnectContextEiRK13QMetaProperty(
    const QModelIndex *index,
    const QObject *item,
    QRangeModelDetails::AutoConnectContext *context,
    int role,
    const QMetaProperty *property) {
  return QRangeModelImplBase::connectPropertyConst(
      *index,
      item,
      context,
      role,
      *property);
}

//  bool QRangeModelImplBase::connectProperties(const QModelIndex &index,
//      const QObject *item, QRangeModelDetails::AutoConnectContext *context,
//      const QHash<int, QMetaProperty> &properties)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase17connectPropertiesERK11QModelIndexPK7QObjectPN18QRangeModelDetails18AutoConnectContextERK5QHashIi13QMetaPropertyE(
    const QModelIndex *index,
    const QObject *item,
    QRangeModelDetails::AutoConnectContext *context,
    const QHash<int, QMetaProperty> *properties) {
  return QRangeModelImplBase::connectProperties(
      *index,
      item,
      context,
      *properties);
}

//  bool QRangeModelImplBase::connectPropertiesConst(const QModelIndex
//      &index, const QObject *item, QRangeModelDetails::AutoConnectContext
//      *context, const QHash<int, QMetaProperty> &properties)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase22connectPropertiesConstERK11QModelIndexPK7QObjectPN18QRangeModelDetails18AutoConnectContextERK5QHashIi13QMetaPropertyE(
    const QModelIndex *index,
    const QObject *item,
    QRangeModelDetails::AutoConnectContext *context,
    const QHash<int, QMetaProperty> *properties) {
  return QRangeModelImplBase::connectPropertiesConst(
      *index,
      item,
      context,
      *properties);
}

//  int QRangeModelImplBase::sortRole() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QRangeModelImplBase8sortRoleEv(
    const QRangeModelImplBase *self) {
  return self->sortRole();
}

//  const QCollator *QRangeModelImplBase::sortCollator() const
extern "C" Q_DECL_EXPORT
const QCollator *ritual_ZNK19QRangeModelImplBase12sortCollatorEv(
    const QRangeModelImplBase *self) {
  return self->sortCollator();
}

//  QVariant QRangeModelImplBase::convertMatchValue(const QVariant &value,
//      Qt::MatchFlags flags)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN19QRangeModelImplBase17convertMatchValueERK8QVariant6QFlagsIN2Qt9MatchFlagEE(
    const QVariant *value,
    int flags) {
  return new QVariant(
      QRangeModelImplBase::convertMatchValue(
          *value,
          QFlags<Qt::MatchFlag>::fromInt(flags)));
}

//  bool QRangeModelImplBase::matchValue(const QString &itemData, const
//      QVariant &value, Qt::MatchFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase10matchValueERK7QStringRK8QVariant6QFlagsIN2Qt9MatchFlagEE(
    const QString *itemData,
    const QVariant *value,
    int flags) {
  return QRangeModelImplBase::matchValue(
      *itemData,
      *value,
      QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  bool QRangeModelImplBase::matchValue(const QVariant &itemData, const
//      QVariant &value, Qt::MatchFlags flags)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase10matchValueERK8QVariantS2_6QFlagsIN2Qt9MatchFlagEE(
    const QVariant *itemData,
    const QVariant *value,
    int flags) {
  return QRangeModelImplBase::matchValue(
      *itemData,
      *value,
      QFlags<Qt::MatchFlag>::fromInt(flags));
}

//  bool QRangeModelImplBase::dropDataOnItem(const QMimeData *data, const
//      QModelIndex &index)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QRangeModelImplBase14dropDataOnItemEPK9QMimeDataRK11QModelIndex(
    QRangeModelImplBase *self,
    const QMimeData *data,
    const QModelIndex *index) {
  return self->dropDataOnItem(data, *index);
}

//  a QScopedValueRollback<bool> a ritual of QRangeModelImplBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QRangeModelImplBase__QScopedValueRollback_bool(
    QScopedValueRollback<bool> *self) {
  delete self;
}

#endif  // !defined(Q_QDOC)
#endif  // QT_CONFIG(rangemodel)
