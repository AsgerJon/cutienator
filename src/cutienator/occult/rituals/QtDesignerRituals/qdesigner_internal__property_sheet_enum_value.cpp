//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::PropertySheetEnumValue::PropertySheetEnumValue(int v,
//      const DesignerMetaEnum &me)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetEnumValue *ritual_ZN18qdesigner_internal22PropertySheetEnumValueC1EiRKNS_16DesignerMetaEnumE(
    int v,
    const qdesigner_internal::DesignerMetaEnum *me) {
  return new qdesigner_internal::PropertySheetEnumValue(v, *me);
}

//  qdesigner_internal::PropertySheetEnumValue::PropertySheetEnumValue()
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetEnumValue *ritual_ZN18qdesigner_internal22PropertySheetEnumValueC1Ev() {
  return new qdesigner_internal::PropertySheetEnumValue();
}

//  qdesigner_internal::PropertySheetEnumValue::~PropertySheetEnumValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal22PropertySheetEnumValueD1Ev(
    qdesigner_internal::PropertySheetEnumValue *self) {
  delete self;
}
