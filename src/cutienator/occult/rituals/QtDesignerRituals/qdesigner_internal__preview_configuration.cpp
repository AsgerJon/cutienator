//  Written by dev_tooling.RitualGenerator from the records of
//  QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtDesigner/QtDesigner>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtDesigner/6.12.0/QtDesigner/private/previewmanager_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  qdesigner_internal::PreviewConfiguration::PreviewConfiguration()
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewConfiguration *ritual_ZN18qdesigner_internal20PreviewConfigurationC1Ev() {
  return new qdesigner_internal::PreviewConfiguration();
}

//  qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
//      QString &style, const QString &applicationStyleSheet, const QString
//      &deviceSkin)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewConfiguration *ritual_ZN18qdesigner_internal20PreviewConfigurationC1ERK7QStringS3_S3_(
    const QString *style,
    const QString *applicationStyleSheet,
    const QString *deviceSkin) {
  return new qdesigner_internal::PreviewConfiguration(
      *style,
      *applicationStyleSheet,
      *deviceSkin);
}

//  qdesigner_internal::PreviewConfiguration::PreviewConfiguration(const
//      PreviewConfiguration &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewConfiguration *ritual_ZN18qdesigner_internal20PreviewConfigurationC1ERKS0_(
    const qdesigner_internal::PreviewConfiguration *a0) {
  return new qdesigner_internal::PreviewConfiguration(*a0);
}

//  PreviewConfiguration
//      &qdesigner_internal::PreviewConfiguration::operator=(const
//      PreviewConfiguration &a0)
extern "C" Q_DECL_EXPORT
qdesigner_internal::PreviewConfiguration *ritual_ZN18qdesigner_internal20PreviewConfigurationaSERKS0_(
    qdesigner_internal::PreviewConfiguration *self,
    const qdesigner_internal::PreviewConfiguration *a0) {
  return &(self->operator=(*a0));
}

//  qdesigner_internal::PreviewConfiguration::~PreviewConfiguration()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfigurationD1Ev(
    qdesigner_internal::PreviewConfiguration *self) {
  delete self;
}

//  QString qdesigner_internal::PreviewConfiguration::style() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal20PreviewConfiguration5styleEv(
    const qdesigner_internal::PreviewConfiguration *self) {
  return new QString(self->style());
}

//  void qdesigner_internal::PreviewConfiguration::setStyle(const QString
//      &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfiguration8setStyleERK7QString(
    qdesigner_internal::PreviewConfiguration *self,
    const QString *a0) {
  self->setStyle(*a0);
}

//  QString qdesigner_internal::PreviewConfiguration::applicationStyleSheet()
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal20PreviewConfiguration21applicationStyleSheetEv(
    const qdesigner_internal::PreviewConfiguration *self) {
  return new QString(self->applicationStyleSheet());
}

//  void
//      qdesigner_internal::PreviewConfiguration::setApplicationStyleSheet(co
//      nst QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfiguration24setApplicationStyleSheetERK7QString(
    qdesigner_internal::PreviewConfiguration *self,
    const QString *a0) {
  self->setApplicationStyleSheet(*a0);
}

//  QString qdesigner_internal::PreviewConfiguration::deviceSkin() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK18qdesigner_internal20PreviewConfiguration10deviceSkinEv(
    const qdesigner_internal::PreviewConfiguration *self) {
  return new QString(self->deviceSkin());
}

//  void qdesigner_internal::PreviewConfiguration::setDeviceSkin(const
//      QString &a0)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfiguration13setDeviceSkinERK7QString(
    qdesigner_internal::PreviewConfiguration *self,
    const QString *a0) {
  self->setDeviceSkin(*a0);
}

//  void qdesigner_internal::PreviewConfiguration::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfiguration5clearEv(
    qdesigner_internal::PreviewConfiguration *self) {
  self->clear();
}

//  void qdesigner_internal::PreviewConfiguration::toSettings(const QString
//      &prefix, QDesignerSettingsInterface *settings) const
extern "C" Q_DECL_EXPORT
void ritual_ZNK18qdesigner_internal20PreviewConfiguration10toSettingsERK7QStringP26QDesignerSettingsInterface(
    const qdesigner_internal::PreviewConfiguration *self,
    const QString *prefix,
    QDesignerSettingsInterface *settings) {
  self->toSettings(*prefix, settings);
}

//  void qdesigner_internal::PreviewConfiguration::fromSettings(const QString
//      &prefix, const QDesignerSettingsInterface *settings)
extern "C" Q_DECL_EXPORT
void ritual_ZN18qdesigner_internal20PreviewConfiguration12fromSettingsERK7QStringPK26QDesignerSettingsInterface(
    qdesigner_internal::PreviewConfiguration *self,
    const QString *prefix,
    const QDesignerSettingsInterface *settings) {
  self->fromSettings(*prefix, settings);
}

//  bool operator==(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internaleqERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalneERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator!=(*lhs, *rhs);
}

//  bool operator<(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalltERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator<(*lhs, *rhs);
}

//  bool operator>(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalgtERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator>(*lhs, *rhs);
}

//  bool operator<=(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalleERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator<=(*lhs, *rhs);
}

//  bool operator>=(const PreviewConfiguration &lhs, const
//      PreviewConfiguration &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZN18qdesigner_internalgeERKNS_20PreviewConfigurationES2_(
    const qdesigner_internal::PreviewConfiguration *lhs,
    const qdesigner_internal::PreviewConfiguration *rhs) {
  return operator>=(*lhs, *rhs);
}
