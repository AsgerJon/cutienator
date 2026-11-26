//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetitem_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qdesigner_widgetitem_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  qdesigner_internal::QDesignerWidgetItemInstaller::QDesignerWidgetItemInst
//      aller()
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerWidgetItemInstaller *ritual_ZN18qdesigner_internal28QDesignerWidgetItemInstallerC1Ev() {
  return new qdesigner_internal::QDesignerWidgetItemInstaller();
}

//  qdesigner_internal::QDesignerWidgetItemInstaller::~QDesignerWidgetItemIns
//      taller()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal28QDesignerWidgetItemInstallerD1Ev(
    qdesigner_internal::QDesignerWidgetItemInstaller *self) {
  delete self;
}
