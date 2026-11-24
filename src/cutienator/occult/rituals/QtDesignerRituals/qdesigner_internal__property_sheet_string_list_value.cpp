//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const PropertySheetStringListValue &lhs, const
//      PropertySheetStringListValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_28PropertySheetStringListValueES2_(
    const qdesigner_internal::PropertySheetStringListValue *lhs,
    const qdesigner_internal::PropertySheetStringListValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetStringListValue &lhs, const
//      PropertySheetStringListValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_28PropertySheetStringListValueES2_(
    const qdesigner_internal::PropertySheetStringListValue *lhs,
    const qdesigner_internal::PropertySheetStringListValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetStringListValue::~PropertySheetStringLis
//      tValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28PropertySheetStringListValueD1Ev(
    qdesigner_internal::PropertySheetStringListValue *self) {
  delete self;
}
