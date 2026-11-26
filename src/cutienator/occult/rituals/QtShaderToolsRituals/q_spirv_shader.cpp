//  Written by dev_tooling.RitualGenerator from the records of
//  QtShaderTools/6.12.0/QtShaderTools/private/qspirvshader_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtShaderTools/QtShaderTools>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtShaderTools/6.12.0/QtShaderTools/private/qspirvshader_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qbytearray.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshaderdescription.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>

//  QSpirvShader::QSpirvShader()
extern "C" Q_DECL_EXPORT
QSpirvShader *ritual_ZN12QSpirvShaderC1Ev() {
  return new QSpirvShader();
}

//  QSpirvShader::~QSpirvShader()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSpirvShaderD1Ev(QSpirvShader *self) {
  delete self;
}

//  void QSpirvShader::setSpirvBinary(const QByteArray &spirv, QShader::Stage
//      stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QSpirvShader14setSpirvBinaryERK10QByteArrayN7QShader5StageE(
    QSpirvShader *self,
    const QByteArray *spirv,
    QShader::Stage stage) {
  self->setSpirvBinary(*spirv, stage);
}

//  QShaderDescription QSpirvShader::shaderDescription() const
extern "C" Q_DECL_EXPORT
QShaderDescription *ritual_ZNK12QSpirvShader17shaderDescriptionEv(
    const QSpirvShader *self) {
  return new QShaderDescription(self->shaderDescription());
}

//  QByteArray QSpirvShader::spirvBinary() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QSpirvShader11spirvBinaryEv(
    const QSpirvShader *self) {
  return new QByteArray(self->spirvBinary());
}

//  QByteArray QSpirvShader::remappedSpirvBinary(RemapFlags flags, QString
//      *errorMessage) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QSpirvShader19remappedSpirvBinaryE6QFlagsINS_9RemapFlagEEP7QString(
    const QSpirvShader *self,
    int flags,
    QString *errorMessage) {
  return new QByteArray(
      self->remappedSpirvBinary(
          QFlags<QSpirvShader::RemapFlag>::fromInt(flags),
          errorMessage));
}

//  QByteArray QSpirvShader::translateToGLSL(int version, GlslFlags flags,
//      QShader::Stage stage, const MultiViewInfo &multiViewInfo,
//      QVector<SeparateToCombinedImageSamplerMapping>
//      *separateToCombinedImageSamplerMappings) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QSpirvShader15translateToGLSLEi6QFlagsINS_8GlslFlagEEN7QShader5StageERKNS_13MultiViewInfoEP5QListINS_37SeparateToCombinedImageSamplerMappingEE(
    const QSpirvShader *self,
    int version,
    int flags,
    QShader::Stage stage,
    const QSpirvShader::MultiViewInfo *multiViewInfo,
    QVector<QSpirvShader::SeparateToCombinedImageSamplerMapping> *separateToCombinedImageSamplerMappings) {
  return new QByteArray(
      self->translateToGLSL(
          version,
          QFlags<QSpirvShader::GlslFlag>::fromInt(flags),
          stage,
          *multiViewInfo,
          separateToCombinedImageSamplerMappings));
}

//  QByteArray QSpirvShader::translateToHLSL(int version,
//      QShader::NativeResourceBindingMap *nativeBindings) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QSpirvShader15translateToHLSLEiP4QMapIiSt4pairIiiEE(
    const QSpirvShader *self,
    int version,
    QShader::NativeResourceBindingMap *nativeBindings) {
  return new QByteArray(self->translateToHLSL(version, nativeBindings));
}

//  QByteArray QSpirvShader::translateToMSL(int version, MslFlags flags,
//      QShader::Stage stage, QShader::NativeResourceBindingMap
//      *nativeBindings, QShader::NativeShaderInfo *shaderInfo, const
//      MultiViewInfo &multiViewInfo, const TessellationInfo &tessInfo) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK12QSpirvShader14translateToMSLEi6QFlagsINS_7MslFlagEEN7QShader5StageEP4QMapIiSt4pairIiiEEPNS3_16NativeShaderInfoERKNS_13MultiViewInfoERKNS_16TessellationInfoE(
    const QSpirvShader *self,
    int version,
    int flags,
    QShader::Stage stage,
    QShader::NativeResourceBindingMap *nativeBindings,
    QShader::NativeShaderInfo *shaderInfo,
    const QSpirvShader::MultiViewInfo *multiViewInfo,
    const QSpirvShader::TessellationInfo *tessInfo) {
  return new QByteArray(
      self->translateToMSL(
          version,
          QFlags<QSpirvShader::MslFlag>::fromInt(flags),
          stage,
          nativeBindings,
          shaderInfo,
          *multiViewInfo,
          *tessInfo));
}

//  QString QSpirvShader::translationErrorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSpirvShader23translationErrorMessageEv(
    const QSpirvShader *self) {
  return new QString(self->translationErrorMessage());
}
