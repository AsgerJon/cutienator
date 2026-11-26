//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ItemData::ItemData()
extern "C" Q_DECL_EXPORT
qdesigner_internal::ItemData *ritual_ZN18qdesigner_internal8ItemDataC1Ev() {
  return new qdesigner_internal::ItemData();
}

//  qdesigner_internal::ItemData::ItemData(const QListWidgetItem *item, bool
//      editor)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ItemData *ritual_ZN18qdesigner_internal8ItemDataC1EPK15QListWidgetItemb(
    const QListWidgetItem *item,
    bool editor) {
  return new qdesigner_internal::ItemData(item, editor);
}

//  qdesigner_internal::ItemData::ItemData(const QTableWidgetItem *item, bool
//      editor)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ItemData *ritual_ZN18qdesigner_internal8ItemDataC1EPK16QTableWidgetItemb(
    const QTableWidgetItem *item,
    bool editor) {
  return new qdesigner_internal::ItemData(item, editor);
}

//  qdesigner_internal::ItemData::ItemData(const QTreeWidgetItem *item, int
//      column)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ItemData *ritual_ZN18qdesigner_internal8ItemDataC1EPK15QTreeWidgetItemi(
    const QTreeWidgetItem *item,
    int column) {
  return new qdesigner_internal::ItemData(item, column);
}

//  QListWidgetItem
//      *qdesigner_internal::ItemData::createListItem(DesignerIconCache
//      *iconCache, bool editor) const
extern "C" Q_DECL_EXPORT
QListWidgetItem *ritual_ZNK18qdesigner_internal8ItemData14createListItemEPNS_17DesignerIconCacheEb(
    const qdesigner_internal::ItemData *self,
    qdesigner_internal::DesignerIconCache *iconCache,
    bool editor) {
  return self->createListItem(iconCache, editor);
}

//  QTableWidgetItem
//      *qdesigner_internal::ItemData::createTableItem(DesignerIconCache
//      *iconCache, bool editor) const
extern "C" Q_DECL_EXPORT
QTableWidgetItem *ritual_ZNK18qdesigner_internal8ItemData15createTableItemEPNS_17DesignerIconCacheEb(
    const qdesigner_internal::ItemData *self,
    qdesigner_internal::DesignerIconCache *iconCache,
    bool editor) {
  return self->createTableItem(iconCache, editor);
}

//  void qdesigner_internal::ItemData::fillTreeItemColumn(QTreeWidgetItem
//      *item, int column, DesignerIconCache *iconCache) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal8ItemData18fillTreeItemColumnEP15QTreeWidgetItemiPNS_17DesignerIconCacheE(
    const qdesigner_internal::ItemData *self,
    QTreeWidgetItem *item,
    int column,
    qdesigner_internal::DesignerIconCache *iconCache) {
  self->fillTreeItemColumn(item, column, iconCache);
}

//  bool qdesigner_internal::ItemData::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal8ItemData7isValidEv(
    const qdesigner_internal::ItemData *self) {
  return self->isValid();
}

//  bool operator==(const ItemData &lhs, const ItemData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_8ItemDataES2_(
    const qdesigner_internal::ItemData *lhs,
    const qdesigner_internal::ItemData *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ItemData &lhs, const ItemData &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_8ItemDataES2_(
    const qdesigner_internal::ItemData *lhs,
    const qdesigner_internal::ItemData *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::ItemData::~ItemData()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal8ItemDataD1Ev(
    qdesigner_internal::ItemData *self) {
  delete self;
}
