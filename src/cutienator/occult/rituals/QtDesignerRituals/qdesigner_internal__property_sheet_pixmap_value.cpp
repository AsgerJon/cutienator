//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_utils_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  PixmapSource qdesigner_internal::PropertySheetPixmapValue::pixmapSource(Q
//      DesignerFormEditorInterface *core) const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PropertySheetPixmapValue::PixmapSource ritual_ZNK18qdesigner_internal24PropertySheetPixmapValue12pixmapSourceEP28QDesignerFormEditorInterface(
    const qdesigner_internal::PropertySheetPixmapValue *self,
    QDesignerFormEditorInterface *core) {
  return self->pixmapSource(core);
}

//  bool operator==(const PropertySheetPixmapValue &lhs, const
//      PropertySheetPixmapValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_24PropertySheetPixmapValueES2_(
    const qdesigner_internal::PropertySheetPixmapValue *lhs,
    const qdesigner_internal::PropertySheetPixmapValue *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PropertySheetPixmapValue &lhs, const
//      PropertySheetPixmapValue &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_24PropertySheetPixmapValueES2_(
    const qdesigner_internal::PropertySheetPixmapValue *lhs,
    const qdesigner_internal::PropertySheetPixmapValue *rhs) {
  return operator!=(*lhs, *rhs);
}

//  qdesigner_internal::PropertySheetPixmapValue::~PropertySheetPixmapValue()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal24PropertySheetPixmapValueD1Ev(
    qdesigner_internal::PropertySheetPixmapValue *self) {
  delete self;
}
