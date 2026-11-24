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

//  QString QSpirvShader::translationErrorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QSpirvShader23translationErrorMessageEv(
    const QSpirvShader *self) {
  return new QString(self->translationErrorMessage());
}
