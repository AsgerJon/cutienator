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
