//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/shared_settings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/shared_settings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QDesignerSettingsInterface
//      *qdesigner_internal::QDesignerSharedSettings::settings() const
extern "C" Q_DECL_EXPORT
QDesignerSettingsInterface *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings8settingsEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->settings();
}

//  qdesigner_internal::QDesignerSharedSettings::~QDesignerSharedSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettingsD1Ev(
    qdesigner_internal::QDesignerSharedSettings *self) {
  delete self;
}
