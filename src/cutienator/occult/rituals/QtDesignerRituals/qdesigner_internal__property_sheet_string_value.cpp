//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const PropertySheetStringValue &lhs, const
//      PropertySheetStringValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_24PropertySheetStringValueES2_(
    const qdesigner_internal::PropertySheetStringValue *lhs,
    const qdesigner_internal::PropertySheetStringValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetStringValue &lhs, const
//      PropertySheetStringValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_24PropertySheetStringValueES2_(
    const qdesigner_internal::PropertySheetStringValue *lhs,
    const qdesigner_internal::PropertySheetStringValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetStringValue::~PropertySheetStringValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24PropertySheetStringValueD1Ev(
    qdesigner_internal::PropertySheetStringValue *self) {
  delete self;
}
