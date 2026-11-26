//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::LayoutProperties::LayoutProperties()
extern "C" Q_DECL_EXPORT
qdesigner_internal::LayoutProperties *ritual_ZN18qdesigner_internal16LayoutPropertiesC1Ev() {
  return new qdesigner_internal::LayoutProperties();
}

//  void qdesigner_internal::LayoutProperties::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16LayoutProperties5clearEv(
    qdesigner_internal::LayoutProperties *self) {
  self->clear();
}

//  int qdesigner_internal::LayoutProperties::visibleProperties(const QLayout
//      *layout)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal16LayoutProperties17visiblePropertiesEPK7QLayout(
    const QLayout *layout) {
  return qdesigner_internal::LayoutProperties::visibleProperties(layout);
}

//  int qdesigner_internal::LayoutProperties::fromPropertySheet(const
//      QDesignerFormEditorInterface *core, QLayout *l, int mask)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal16LayoutProperties17fromPropertySheetEPK28QDesignerFormEditorInterfaceP7QLayouti(
    qdesigner_internal::LayoutProperties *self,
    const QDesignerFormEditorInterface *core,
    QLayout *l,
    int mask) {
  return self->fromPropertySheet(core, l, mask);
}

//  int qdesigner_internal::LayoutProperties::toPropertySheet(const
//      QDesignerFormEditorInterface *core, QLayout *l, int mask, bool
//      applyChanged) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal16LayoutProperties15toPropertySheetEPK28QDesignerFormEditorInterfaceP7QLayoutib(
    const qdesigner_internal::LayoutProperties *self,
    const QDesignerFormEditorInterface *core,
    QLayout *l,
    int mask,
    bool applyChanged) {
  return self->toPropertySheet(core, l, mask, applyChanged);
}

//  qdesigner_internal::LayoutProperties::~LayoutProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16LayoutPropertiesD1Ev(
    qdesigner_internal::LayoutProperties *self) {
  delete self;
}
