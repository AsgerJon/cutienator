//  Written by dev_tooling.RitualGenerator from the records of
//  Qt3DRender/6.12.0/Qt3DRender/private/qshaderformat_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <Qt3DRender/6.12.0/Qt3DRender/private/qt3drender_global_p.h>
#include <Qt3DRender/Qt3DRender>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <Qt3DRender/6.12.0/Qt3DRender/private/qshaderformat_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qversionnumber.h>
#include <QtCore/qstring.h>
#include <QtCore/qlist.h>

//  Qt3DRender::QShaderFormat::QShaderFormat()
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderFormat *ritual_ZN10Qt3DRender13QShaderFormatC1Ev() {
  return new Qt3DRender::QShaderFormat();
}

//  Api Qt3DRender::QShaderFormat::api() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderFormat::Api ritual_ZNK10Qt3DRender13QShaderFormat3apiEv(
    const Qt3DRender::QShaderFormat *self) {
  return self->api();
}

//  void Qt3DRender::QShaderFormat::setApi(Api api)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormat6setApiENS0_3ApiE(
    Qt3DRender::QShaderFormat *self,
    Qt3DRender::QShaderFormat::Api api) {
  self->setApi(api);
}

//  QVersionNumber Qt3DRender::QShaderFormat::version() const
extern "C" Q_DECL_EXPORT
QVersionNumber *ritual_ZNK10Qt3DRender13QShaderFormat7versionEv(
    const Qt3DRender::QShaderFormat *self) {
  return new QVersionNumber(self->version());
}

//  void Qt3DRender::QShaderFormat::setVersion(const QVersionNumber &version)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormat10setVersionERK14QVersionNumber(
    Qt3DRender::QShaderFormat *self,
    const QVersionNumber *version) {
  self->setVersion(*version);
}

//  QStringList Qt3DRender::QShaderFormat::extensions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK10Qt3DRender13QShaderFormat10extensionsEv(
    const Qt3DRender::QShaderFormat *self) {
  return new QList<QString>(self->extensions());
}

//  void Qt3DRender::QShaderFormat::setExtensions(const QStringList
//      &extensions)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormat13setExtensionsERK5QListI7QStringE(
    Qt3DRender::QShaderFormat *self,
    const QList<QString> *extensions) {
  self->setExtensions(*extensions);
}

//  QString Qt3DRender::QShaderFormat::vendor() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK10Qt3DRender13QShaderFormat6vendorEv(
    const Qt3DRender::QShaderFormat *self) {
  return new QString(self->vendor());
}

//  void Qt3DRender::QShaderFormat::setVendor(const QString &vendor)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormat9setVendorERK7QString(
    Qt3DRender::QShaderFormat *self,
    const QString *vendor) {
  self->setVendor(*vendor);
}

//  bool Qt3DRender::QShaderFormat::isValid() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QShaderFormat7isValidEv(
    const Qt3DRender::QShaderFormat *self) {
  return self->isValid();
}

//  bool Qt3DRender::QShaderFormat::supports(const QShaderFormat &other)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK10Qt3DRender13QShaderFormat8supportsERKS0_(
    const Qt3DRender::QShaderFormat *self,
    const Qt3DRender::QShaderFormat *other) {
  return self->supports(*other);
}

//  ShaderType Qt3DRender::QShaderFormat::shaderType() const
extern "C" Q_DECL_EXPORT
Qt3DRender::QShaderFormat::ShaderType ritual_ZNK10Qt3DRender13QShaderFormat10shaderTypeEv(
    const Qt3DRender::QShaderFormat *self) {
  return self->shaderType();
}

//  void Qt3DRender::QShaderFormat::setShaderType(ShaderType shaderType)
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormat13setShaderTypeENS0_10ShaderTypeE(
    Qt3DRender::QShaderFormat *self,
    Qt3DRender::QShaderFormat::ShaderType shaderType) {
  self->setShaderType(shaderType);
}

//  Qt3DRender::QShaderFormat::~QShaderFormat()
extern "C" Q_DECL_EXPORT
void ritual_ZN10Qt3DRender13QShaderFormatD1Ev(
    Qt3DRender::QShaderFormat *self) {
  delete self;
}
