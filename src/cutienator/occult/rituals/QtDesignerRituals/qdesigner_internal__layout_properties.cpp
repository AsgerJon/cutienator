//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/qlayout_widget_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  int qdesigner_internal::LayoutProperties::visibleProperties(const QLayout
//      *layout)
extern "C" Q_DECL_EXPORT
int ritual_ZN18qdesigner_internal16LayoutProperties17visiblePropertiesEPK7QLayout(
    const QLayout *layout) {
  return qdesigner_internal::LayoutProperties::visibleProperties(layout);
}

//  qdesigner_internal::LayoutProperties::~LayoutProperties()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal16LayoutPropertiesD1Ev(
    qdesigner_internal::LayoutProperties *self) {
  delete self;
}
