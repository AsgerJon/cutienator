//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::TreeWidgetContents::ItemContents::ItemContents()
extern "C" Q_DECL_EXPORT
qdesigner_internal::TreeWidgetContents::ItemContents *ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsC1Ev() {
  return new qdesigner_internal::TreeWidgetContents::ItemContents();
}

//  bool operator==(const ItemContents &lhs, const ItemContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_18TreeWidgetContents12ItemContentsES3_(
    const qdesigner_internal::TreeWidgetContents::ItemContents *lhs,
    const qdesigner_internal::TreeWidgetContents::ItemContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const ItemContents &lhs, const ItemContents &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_18TreeWidgetContents12ItemContentsES3_(
    const qdesigner_internal::TreeWidgetContents::ItemContents *lhs,
    const qdesigner_internal::TreeWidgetContents::ItemContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::TreeWidgetContents::ItemContents::~ItemContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18TreeWidgetContents12ItemContentsD1Ev(
    qdesigner_internal::TreeWidgetContents::ItemContents *self) {
  delete self;
}
