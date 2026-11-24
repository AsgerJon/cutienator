//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const TreeWidgetContents &lhs, const TreeWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_18TreeWidgetContentsES2_(
    const qdesigner_internal::TreeWidgetContents *lhs,
    const qdesigner_internal::TreeWidgetContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const TreeWidgetContents &lhs, const TreeWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_18TreeWidgetContentsES2_(
    const qdesigner_internal::TreeWidgetContents *lhs,
    const qdesigner_internal::TreeWidgetContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::TreeWidgetContents::~TreeWidgetContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal18TreeWidgetContentsD1Ev(
    qdesigner_internal::TreeWidgetContents *self) {
  delete self;
}
