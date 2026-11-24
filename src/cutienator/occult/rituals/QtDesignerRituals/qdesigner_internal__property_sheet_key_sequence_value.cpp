//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  bool operator==(const PropertySheetKeySequenceValue &lhs, const
//      PropertySheetKeySequenceValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_29PropertySheetKeySequenceValueES2_(
    const qdesigner_internal::PropertySheetKeySequenceValue *lhs,
    const qdesigner_internal::PropertySheetKeySequenceValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetKeySequenceValue &lhs, const
//      PropertySheetKeySequenceValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_29PropertySheetKeySequenceValueES2_(
    const qdesigner_internal::PropertySheetKeySequenceValue *lhs,
    const qdesigner_internal::PropertySheetKeySequenceValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetKeySequenceValue::~PropertySheetKeySeque
//      nceValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal29PropertySheetKeySequenceValueD1Ev(
    qdesigner_internal::PropertySheetKeySequenceValue *self) {
  delete self;
}
