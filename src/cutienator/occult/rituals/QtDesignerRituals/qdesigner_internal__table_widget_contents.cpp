//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_command_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const TableWidgetContents &lhs, const TableWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_19TableWidgetContentsES2_(
    const qdesigner_internal::TableWidgetContents *lhs,
    const qdesigner_internal::TableWidgetContents *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const TableWidgetContents &lhs, const TableWidgetContents
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_19TableWidgetContentsES2_(
    const qdesigner_internal::TableWidgetContents *lhs,
    const qdesigner_internal::TableWidgetContents *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::TableWidgetContents::~TableWidgetContents()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal19TableWidgetContentsD1Ev(
    qdesigner_internal::TableWidgetContents *self) {
  delete self;
}
