//  Written by dev_tooling.RitualGenerator from the records of
//  QtShaderTools/6.12.0/QtShaderTools/rhi/qshaderbaker.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtShaderTools/QtShaderTools>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtShaderTools/6.12.0/QtShaderTools/rhi/qshaderbaker.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  QShaderBaker::QShaderBaker()
extern "C" Q_DECL_EXPORT
QShaderBaker *ritual_ZN12QShaderBakerC1Ev() {
  return new QShaderBaker();
}

//  QShaderBaker::~QShaderBaker()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBakerD1Ev(QShaderBaker *self) {
  delete self;
}

//  void QShaderBaker::setSourceFileName(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker17setSourceFileNameERK7QString(
    QShaderBaker *self,
    const QString *fileName) {
  self->setSourceFileName(*fileName);
}

//  void QShaderBaker::setSourceFileName(const QString &fileName,
//      QShader::Stage stage)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker17setSourceFileNameERK7QStringN7QShader5StageE(
    QShaderBaker *self,
    const QString *fileName,
    QShader::Stage stage) {
  self->setSourceFileName(*fileName, stage);
}

//  void QShaderBaker::setSourceDevice(QIODevice *device, QShader::Stage
//      stage, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker15setSourceDeviceEP9QIODeviceN7QShader5StageERK7QString(
    QShaderBaker *self,
    QIODevice *device,
    QShader::Stage stage,
    const QString *fileName) {
  self->setSourceDevice(device, stage, *fileName);
}

//  void QShaderBaker::setSourceString(const QByteArray &sourceString,
//      QShader::Stage stage, const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker15setSourceStringERK10QByteArrayN7QShader5StageERK7QString(
    QShaderBaker *self,
    const QByteArray *sourceString,
    QShader::Stage stage,
    const QString *fileName) {
  self->setSourceString(*sourceString, stage, *fileName);
}

//  void QShaderBaker::setPreamble(const QByteArray &preamble)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker11setPreambleERK10QByteArray(
    QShaderBaker *self,
    const QByteArray *preamble) {
  self->setPreamble(*preamble);
}

//  void QShaderBaker::setBatchableVertexShaderExtraInputLocation(int
//      location)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker42setBatchableVertexShaderExtraInputLocationEi(
    QShaderBaker *self,
    int location) {
  self->setBatchableVertexShaderExtraInputLocation(location);
}

//  void QShaderBaker::setPerTargetCompilation(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker23setPerTargetCompilationEb(
    QShaderBaker *self,
    bool enable) {
  self->setPerTargetCompilation(enable);
}

//  void QShaderBaker::setBreakOnShaderTranslationError(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker32setBreakOnShaderTranslationErrorEb(
    QShaderBaker *self,
    bool enable) {
  self->setBreakOnShaderTranslationError(enable);
}

//  void
//      QShaderBaker::setTessellationMode(QShaderDescription::TessellationMod
//      e mode)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker19setTessellationModeEN18QShaderDescription16TessellationModeE(
    QShaderBaker *self,
    QShaderDescription::TessellationMode mode) {
  self->setTessellationMode(mode);
}

//  void QShaderBaker::setTessellationOutputVertexCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker32setTessellationOutputVertexCountEi(
    QShaderBaker *self,
    int count) {
  self->setTessellationOutputVertexCount(count);
}

//  void QShaderBaker::setMultiViewCount(int count)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker17setMultiViewCountEi(
    QShaderBaker *self,
    int count) {
  self->setMultiViewCount(count);
}

//  void QShaderBaker::setSpirvOptions(SpirvOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker15setSpirvOptionsE6QFlagsINS_11SpirvOptionEE(
    QShaderBaker *self,
    int options) {
  self->setSpirvOptions(QFlags<QShaderBaker::SpirvOption>::fromInt(options));
}

//  void QShaderBaker::setGlslOptions(GlslOptions options)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QShaderBaker14setGlslOptionsE6QFlagsINS_10GlslOptionEE(
    QShaderBaker *self,
    int options) {
  self->setGlslOptions(QFlags<QShaderBaker::GlslOption>::fromInt(options));
}

//  QShader QShaderBaker::bake()
extern "C" Q_DECL_EXPORT
QShader *ritual_ZN12QShaderBaker4bakeEv(QShaderBaker *self) {
  return new QShader(self->bake());
}

//  QString QShaderBaker::errorMessage() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QShaderBaker12errorMessageEv(const QShaderBaker *self) {
  return new QString(self->errorMessage());
}
