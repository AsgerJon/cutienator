//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/shared_settings_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/shared_settings_p.h>
#include <QtDesigner/6.12.0/QtDesigner/private/grid_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qsize.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h>
#include <QtDesigner/6.12.0/QtDesigner/private/deviceprofile_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qlist.h>

//  qdesigner_internal::QDesignerSharedSettings::QDesignerSharedSettings(QDes
//      ignerFormEditorInterface *core)
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerSharedSettings *ritual_ZN18qdesigner_internal23QDesignerSharedSettingsC1EP28QDesignerFormEditorInterface(
    QDesignerFormEditorInterface *core) {
  return new qdesigner_internal::QDesignerSharedSettings(core);
}

//  Grid qdesigner_internal::QDesignerSharedSettings::defaultGrid() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::Grid *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11defaultGridEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new qdesigner_internal::Grid(self->defaultGrid());
}

//  void qdesigner_internal::QDesignerSharedSettings::setDefaultGrid(const
//      Grid &grid)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setDefaultGridERKNS_4GridE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const qdesigner_internal::Grid *grid) {
  self->setDefaultGrid(*grid);
}

//  QStringList
//      qdesigner_internal::QDesignerSharedSettings::formTemplatePaths()
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings17formTemplatePathsEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QList<QString>(self->formTemplatePaths());
}

//  void
//      qdesigner_internal::QDesignerSharedSettings::setFormTemplatePaths(con
//      st QStringList &paths)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings20setFormTemplatePathsERK5QListI7QStringE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const QList<QString> *paths) {
  self->setFormTemplatePaths(*paths);
}

//  void qdesigner_internal::QDesignerSharedSettings::setAdditionalFormTempla
//      tePaths(const QStringList &additionalPaths)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings30setAdditionalFormTemplatePathsERK5QListI7QStringE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const QList<QString> *additionalPaths) {
  self->setAdditionalFormTemplatePaths(*additionalPaths);
}

//  QStringList qdesigner_internal::QDesignerSharedSettings::additionalFormTe
//      mplatePaths() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings27additionalFormTemplatePathsEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QList<QString>(self->additionalFormTemplatePaths());
}

//  QString qdesigner_internal::QDesignerSharedSettings::formTemplate() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings12formTemplateEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QString(self->formTemplate());
}

//  void qdesigner_internal::QDesignerSharedSettings::setFormTemplate(const
//      QString &t)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings15setFormTemplateERK7QString(
    qdesigner_internal::QDesignerSharedSettings *self,
    const QString *t) {
  self->setFormTemplate(*t);
}

//  QSize qdesigner_internal::QDesignerSharedSettings::newFormSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11newFormSizeEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QSize(self->newFormSize());
}

//  void qdesigner_internal::QDesignerSharedSettings::setNewFormSize(const
//      QSize &s)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setNewFormSizeERK5QSize(
    qdesigner_internal::QDesignerSharedSettings *self,
    const QSize *s) {
  self->setNewFormSize(*s);
}

//  PreviewConfiguration
//      qdesigner_internal::QDesignerSharedSettings::customPreviewConfigurati
//      on() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewConfiguration *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings26customPreviewConfigurationEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new qdesigner_internal::PreviewConfiguration(
      self->customPreviewConfiguration());
}

//  void qdesigner_internal::QDesignerSharedSettings::setCustomPreviewConfigu
//      ration(const PreviewConfiguration &configuration)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings29setCustomPreviewConfigurationERKNS_20PreviewConfigurationE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const qdesigner_internal::PreviewConfiguration *configuration) {
  self->setCustomPreviewConfiguration(*configuration);
}

//  bool qdesigner_internal::QDesignerSharedSettings::isCustomPreviewConfigur
//      ationEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal23QDesignerSharedSettings35isCustomPreviewConfigurationEnabledEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->isCustomPreviewConfigurationEnabled();
}

//  void qdesigner_internal::QDesignerSharedSettings::setCustomPreviewConfigu
//      rationEnabled(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings36setCustomPreviewConfigurationEnabledEb(
    qdesigner_internal::QDesignerSharedSettings *self,
    bool enabled) {
  self->setCustomPreviewConfigurationEnabled(enabled);
}

//  QStringList
//      qdesigner_internal::QDesignerSharedSettings::userDeviceSkins() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings15userDeviceSkinsEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QList<QString>(self->userDeviceSkins());
}

//  void
//      qdesigner_internal::QDesignerSharedSettings::setUserDeviceSkins(const
//      QStringList &userDeviceSkins)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings18setUserDeviceSkinsERK5QListI7QStringE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const QList<QString> *userDeviceSkins) {
  self->setUserDeviceSkins(*userDeviceSkins);
}

//  bool qdesigner_internal::QDesignerSharedSettings::zoomEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18qdesigner_internal23QDesignerSharedSettings11zoomEnabledEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->zoomEnabled();
}

//  void qdesigner_internal::QDesignerSharedSettings::setZoomEnabled(bool v)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings14setZoomEnabledEb(
    qdesigner_internal::QDesignerSharedSettings *self,
    bool v) {
  self->setZoomEnabled(v);
}

//  int qdesigner_internal::QDesignerSharedSettings::zoom() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal23QDesignerSharedSettings4zoomEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->zoom();
}

//  void qdesigner_internal::QDesignerSharedSettings::setZoom(int z)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings7setZoomEi(
    qdesigner_internal::QDesignerSharedSettings *self,
    int z) {
  self->setZoom(z);
}

//  ObjectNamingMode
//      qdesigner_internal::QDesignerSharedSettings::objectNamingMode() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::ObjectNamingMode ritual_ZNK18qdesigner_internal23QDesignerSharedSettings16objectNamingModeEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->objectNamingMode();
}

//  void qdesigner_internal::QDesignerSharedSettings::setObjectNamingMode(Obj
//      ectNamingMode n)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings19setObjectNamingModeENS_16ObjectNamingModeE(
    qdesigner_internal::QDesignerSharedSettings *self,
    qdesigner_internal::ObjectNamingMode n) {
  self->setObjectNamingMode(n);
}

//  DeviceProfile
//      qdesigner_internal::QDesignerSharedSettings::currentDeviceProfile()
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings20currentDeviceProfileEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new qdesigner_internal::DeviceProfile(self->currentDeviceProfile());
}

//  void qdesigner_internal::QDesignerSharedSettings::setCurrentDeviceProfile
//      Index(int i)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings28setCurrentDeviceProfileIndexEi(
    qdesigner_internal::QDesignerSharedSettings *self,
    int i) {
  self->setCurrentDeviceProfileIndex(i);
}

//  int
//      qdesigner_internal::QDesignerSharedSettings::currentDeviceProfileInde
//      x() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK18qdesigner_internal23QDesignerSharedSettings25currentDeviceProfileIndexEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->currentDeviceProfileIndex();
}

//  DeviceProfile
//      qdesigner_internal::QDesignerSharedSettings::deviceProfileAt(int idx)
//      const
extern "C" Q_DECL_EXPORT
qdesigner_internal::DeviceProfile *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings15deviceProfileAtEi(
    const qdesigner_internal::QDesignerSharedSettings *self,
    int idx) {
  return new qdesigner_internal::DeviceProfile(self->deviceProfileAt(idx));
}

//  DeviceProfileList
//      qdesigner_internal::QDesignerSharedSettings::deviceProfiles() const
extern "C" Q_DECL_EXPORT
qdesigner_internal::QDesignerSharedSettings::DeviceProfileList *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings14deviceProfilesEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new qdesigner_internal::QDesignerSharedSettings::DeviceProfileList(
      self->deviceProfiles());
}

//  void qdesigner_internal::QDesignerSharedSettings::setDeviceProfiles(const
//      DeviceProfileList &dp)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings17setDeviceProfilesERK5QListINS_13DeviceProfileEE(
    qdesigner_internal::QDesignerSharedSettings *self,
    const qdesigner_internal::QDesignerSharedSettings::DeviceProfileList *dp) {
  self->setDeviceProfiles(*dp);
}

//  const QStringList
//      &qdesigner_internal::QDesignerSharedSettings::defaultFormTemplatePath
//      s()
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN18qdesigner_internal23QDesignerSharedSettings24defaultFormTemplatePathsEv() {
  return new QList<QString>(
      qdesigner_internal::QDesignerSharedSettings::defaultFormTemplatePaths());
}

//  void qdesigner_internal::QDesignerSharedSettings::migrateTemplates()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettings16migrateTemplatesEv() {
  qdesigner_internal::QDesignerSharedSettings::migrateTemplates();
}

//  QDesignerSettingsInterface
//      *qdesigner_internal::QDesignerSharedSettings::settings() const
extern "C" Q_DECL_EXPORT
QDesignerSettingsInterface *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings8settingsEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return self->settings();
}

//  QStringList
//      qdesigner_internal::QDesignerSharedSettings::deviceProfileXml() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK18qdesigner_internal23QDesignerSharedSettings16deviceProfileXmlEv(
    const qdesigner_internal::QDesignerSharedSettings *self) {
  return new QList<QString>(self->deviceProfileXml());
}

//  qdesigner_internal::QDesignerSharedSettings::~QDesignerSharedSettings()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal23QDesignerSharedSettingsD1Ev(
    qdesigner_internal::QDesignerSharedSettings *self) {
  delete self;
}

//  a qdesigner_internal::QDesignerSharedSettings::DeviceProfileList a ritual
//      of qdesigner_internal::QDesignerSharedSettings gave
extern "C" Q_DECL_EXPORT
void ritual_drop_qdesigner_internal_QDesignerSharedSettings__qdesigner_internal_QDesignerSharedSettings_DeviceProfileList(
    qdesigner_internal::QDesignerSharedSettings::DeviceProfileList *self) {
  delete self;
}
