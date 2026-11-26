//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::ListContents::ListContents()
extern "C" Q_DECL_EXPORT
qdesigner_internal::ListContents *ritual_ZN18qdesigner_internal12ListContentsC1Ev() {
  return new qdesigner_internal::ListContents();
}

//  qdesigner_internal::ListContents::ListContents(const QTreeWidgetItem
//      *item)
extern "C" Q_DECL_EXPORT
qdesigner_internal::ListContents *ritual_ZN18qdesigner_internal12ListContentsC1EPK15QTreeWidgetItem(
    const QTreeWidgetItem *item) {
  return new qdesigner_internal::ListContents(item);
}

//  QTreeWidgetItem
//      *qdesigner_internal::ListContents::createTreeItem(DesignerIconCache
//      *iconCache) const
extern "C" Q_DECL_EXPORT
QTreeWidgetItem *ritual_ZNK18qdesigner_internal12ListContents14createTreeItemEPNS_17DesignerIconCacheE(
    const qdesigner_internal::ListContents *self,
    qdesigner_internal::DesignerIconCache *iconCache) {
  return self->createTreeItem(iconCache);
}

//  void qdesigner_internal::ListContents::createFromListWidget(const
//      QListWidget *listWidget, bool editor)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12ListContents20createFromListWidgetEPK11QListWidgetb(
    qdesigner_internal::ListContents *self,
    const QListWidget *listWidget,
    bool editor) {
  self->createFromListWidget(listWidget, editor);
}

//  void qdesigner_internal::ListContents::applyToListWidget(QListWidget
//      *listWidget, DesignerIconCache *iconCache, bool editor, Qt::Alignment
//      alignmentDefault) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal12ListContents17applyToListWidgetEP11QListWidgetPNS_17DesignerIconCacheEb6QFlagsIN2Qt13AlignmentFlagEE(
    const qdesigner_internal::ListContents *self,
    QListWidget *listWidget,
    qdesigner_internal::DesignerIconCache *iconCache,
    bool editor,
    int alignmentDefault) {
  self->applyToListWidget(
      listWidget,
      iconCache,
      editor,
      QFlags<Qt::AlignmentFlag>::fromInt(alignmentDefault));
}

//  void qdesigner_internal::ListContents::createFromComboBox(const QComboBox
//      *listWidget)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12ListContents18createFromComboBoxEPK9QComboBox(
    qdesigner_internal::ListContents *self,
    const QComboBox *listWidget) {
  self->createFromComboBox(listWidget);
}

//  void qdesigner_internal::ListContents::applyToComboBox(QComboBox
//      *listWidget, DesignerIconCache *iconCache) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal12ListContents15applyToComboBoxEP9QComboBoxPNS_17DesignerIconCacheE(
    const qdesigner_internal::ListContents *self,
    QComboBox *listWidget,
    qdesigner_internal::DesignerIconCache *iconCache) {
  self->applyToComboBox(listWidget, iconCache);
}

//  bool operator==(const ListContents &lhs, const ListContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_12ListContentsES2_(
    const qdesigner_internal::ListContents *lhs,
    const qdesigner_internal::ListContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ListContents &lhs, const ListContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_12ListContentsES2_(
    const qdesigner_internal::ListContents *lhs,
    const qdesigner_internal::ListContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::ListContents::~ListContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal12ListContentsD1Ev(
    qdesigner_internal::ListContents *self) {
  delete self;
}
