//  Written by dev_tooling.RitualGenerator from the records of
//  QtShaderTools/6.12.0/QtShaderTools/private/qspirvcompiler_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtShaderTools/QtShaderTools>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtShaderTools/6.12.0/QtShaderTools/private/qspirvcompiler_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

//  QSpirvCompiler::QSpirvCompiler()
extern "C" Q_DECL_EXPORT
QSpirvCompiler *ritual_ZN14QSpirvCompilerC1Ev() {
  return new QSpirvCompiler();
}

//  QSpirvCompiler::~QSpirvCompiler()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompilerD1Ev(QSpirvCompiler *self) {
  delete self;
}

//  void QSpirvCompiler::setSourceFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler17setSourceFileNameERK7QString(
    QSpirvCompiler *self,
    const QString *fileName) {
  self->setSourceFileName(*fileName);
}

//  void QSpirvCompiler::setSourceFileName(const QString &fileName,
//      QShader::Stage stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler17setSourceFileNameERK7QStringN7QShader5StageE(
    QSpirvCompiler *self,
    const QString *fileName,
    QShader::Stage stage) {
  self->setSourceFileName(*fileName, stage);
}

//  void QSpirvCompiler::setSourceDevice(QIODevice *device, QShader::Stage
//      stage, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler15setSourceDeviceEP9QIODeviceN7QShader5StageERK7QString(
    QSpirvCompiler *self,
    QIODevice *device,
    QShader::Stage stage,
    const QString *fileName) {
  self->setSourceDevice(device, stage, *fileName);
}

//  void QSpirvCompiler::setSourceString(const QByteArray &sourceString,
//      QShader::Stage stage, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler15setSourceStringERK10QByteArrayN7QShader5StageERK7QString(
    QSpirvCompiler *self,
    const QByteArray *sourceString,
    QShader::Stage stage,
    const QString *fileName) {
  self->setSourceString(*sourceString, stage, *fileName);
}

//  void QSpirvCompiler::setFlags(Flags flags)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler8setFlagsE6QFlagsINS_4FlagEE(
    QSpirvCompiler *self,
    int flags) {
  self->setFlags(QFlags<QSpirvCompiler::Flag>::fromInt(flags));
}

//  void QSpirvCompiler::setPreamble(const QByteArray &preamble)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler11setPreambleERK10QByteArray(
    QSpirvCompiler *self,
    const QByteArray *preamble) {
  self->setPreamble(*preamble);
}

//  void QSpirvCompiler::setSGBatchingVertexInputLocation(int location)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QSpirvCompiler32setSGBatchingVertexInputLocationEi(
    QSpirvCompiler *self,
    int location) {
  self->setSGBatchingVertexInputLocation(location);
}

//  QByteArray QSpirvCompiler::compileToSpirv()
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZN14QSpirvCompiler14compileToSpirvEv(
    QSpirvCompiler *self) {
  return new QByteArray(self->compileToSpirv());
}

//  QString QSpirvCompiler::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK14QSpirvCompiler12errorMessageEv(
    const QSpirvCompiler *self) {
  return new QString(self->errorMessage());
}
